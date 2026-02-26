import pandas as pd

print("\n===== START BACKTEST =====\n")

# -----------------------------
# 1️⃣ Read CSVs (M1 and M2 data)
# -----------------------------
print("Loading M1 and M2 data...")

df_1m = pd.read_csv("EURUSD_1m_clean.csv")
df_2m = pd.read_csv("EURUSD_2m_clean.csv")

df_1m['datetime'] = pd.to_datetime(df_1m['datetime'])
df_2m['datetime'] = pd.to_datetime(df_2m['datetime'])

for col in ["open", "high", "low", "close"]:
    df_1m[col] = df_1m[col].astype(float)
    df_2m[col] = df_2m[col].astype(float)

print("M1 candles:", len(df_1m))
print("M2 candles:", len(df_2m))

# -----------------------------
# 2️⃣ Calculate candle structure for M2
# -----------------------------
print("\nCalculating candle structure...")

df_2m['top_wick'] = df_2m['high'] - df_2m[['close','open']].max(axis=1)
df_2m['bot_wick'] = df_2m[['close','open']].min(axis=1) - df_2m['low']
df_2m['body'] = (df_2m['close'] - df_2m['open']).abs()

print("Structure calculated")

# -----------------------------
# 3️⃣ Detect bullish/bearish patterns
# -----------------------------
print("\nDetecting patterns...")

df_2m['bull_pattern'] = (
    (df_2m['close'] > df_2m['open']) &
    (df_2m['top_wick'] < df_2m['body']) &
    (df_2m['bot_wick'] < df_2m['body']) &
    (df_2m['close'] > df_2m['high'].shift(1))
)

df_2m['bear_pattern'] = (
    (df_2m['close'] < df_2m['open']) &
    (df_2m['top_wick'] < df_2m['body']) &
    (df_2m['bot_wick'] < df_2m['body']) &
    (df_2m['close'] < df_2m['low'].shift(1))
)

df_2m = df_2m.dropna().reset_index(drop=True)

bull_count = df_2m['bull_pattern'].sum()
bear_count = df_2m['bear_pattern'].sum()

print("Patterns detected")
print("Total bull patterns:", bull_count)
print("Total bear patterns:", bear_count)
print("Total patterns:", bull_count + bear_count)

# -----------------------------
# 4️⃣ Simulate trades using M1 for first minute of next M2
# -----------------------------
print("\nSimulating trades...")

wins = 0
losses = 0
total_trades = 0

# Ensure alignment: M2[i] corresponds to M1 rows (2 per M2)
for i in range(1, len(df_2m) - 1):

    # Index of the first M1 minute in the next 2M candle
    first_m1_next_2m_index = (i + 1) * 2

    if first_m1_next_2m_index >= len(df_1m):
        continue

    first_minute_next_2m = df_1m.iloc[first_m1_next_2m_index]

    entry_price = df_2m.loc[i, 'open']
    next_2m_close = df_2m.loc[i + 1, 'close']

    # Bullish trade
    if df_2m.loc[i, 'bull_pattern']:
        if first_minute_next_2m['low'] < entry_price:
            total_trades += 1
            if next_2m_close >= entry_price:
                wins += 1
            else:
                losses += 1

    # Bearish trade
    elif df_2m.loc[i, 'bear_pattern']:
        if first_minute_next_2m['high'] > entry_price:
            total_trades += 1
            if next_2m_close <= entry_price:
                wins += 1
            else:
                losses += 1

print("Trade simulation completed")

# -----------------------------
# 5️⃣ Results
# -----------------------------
winrate = wins / total_trades if total_trades > 0 else 0

print("\n------ RESULTS ------")
print("Wins:", wins)
print("Losses:", losses)
print("Total trades:", total_trades)
print("Winrate:", round(winrate * 100, 2), "%")

print("\n===== END BACKTEST =====\n")
