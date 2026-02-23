import pandas as pd

# -----------------------------
# 1️⃣ Read CSV and prepare data
# -----------------------------
df = pd.read_csv("data_binary.csv", sep="\t")
df.columns = ["date","time","open","high","low","close","tickvol","vol","spread"]

df["datetime"] = pd.to_datetime(df["date"] + " " + df["time"])
df = df.sort_values("datetime").reset_index(drop=True)

for col in ["open","high","low","close"]:
    df[col] = df[col].astype(float)

# -----------------------------
# 2️⃣ Build 1-minute candles from 30s data
# -----------------------------
df['group_1m'] = df.index // 2  # every 2 candles of 30s = 1 candle of 1 minute

df_1m = df.groupby('group_1m').agg({
    'datetime': 'first',
    'open': 'first',
    'high': 'max',
    'low': 'min',
    'close': 'last',
    'tickvol': 'sum',
    'vol': 'sum',
    'spread': 'mean'
}).reset_index(drop=True)

# -----------------------------
# 3️⃣ Calculate body and wicks in 1-minute candles
# -----------------------------
df_1m['body'] = abs(df_1m['close'] - df_1m['open'])
df_1m['wick_top'] = df_1m['high'] - df_1m[['open','close']].max(axis=1)
df_1m['wick_bot'] = df_1m[['open','close']].min(axis=1) - df_1m['low']

# -----------------------------
# 4️⃣ Detect strong candles
# -----------------------------
df_1m['bull_strong'] = (
    (df_1m['close'] > df_1m['open']) &
    (df_1m['body'] > df_1m['wick_top']) &
    (df_1m['body'] > df_1m['wick_bot']) &
    (df_1m['close'] > df_1m['high'].shift(1))
)

df_1m['bear_strong'] = (
    (df_1m['close'] < df_1m['open']) &
    (df_1m['body'] > df_1m['wick_top']) &
    (df_1m['body'] > df_1m['wick_bot']) &
    (df_1m['close'] < df_1m['low'].shift(1))
)

# -----------------------------
# 5️⃣ Simulate trades (entry in the first half of candle[i+1])
# -----------------------------
wins = 0
losses = 0

for i in range(1, len(df_1m)-1):
    # index of the first 30s candle of the next 1-minute candle (i+1)
    idx_first_30s_next_1m = (i+1)*2 - 1
    first_30s_next = df.loc[idx_first_30s_next_1m]

    # Bullish entry
    if df_1m.loc[i, 'bull_strong']:
        if first_30s_next['low'] <= df_1m.loc[i, 'open']:
            next_1m_close = df_1m.loc[i+1, 'close']
            if next_1m_close > df_1m.loc[i, 'open']:
                wins += 1
            else:
                losses += 1

    # Bearish entry
    if df_1m.loc[i, 'bear_strong']:
        if first_30s_next['high'] >= df_1m.loc[i, 'open']:
            next_1m_close = df_1m.loc[i+1, 'close']
            if next_1m_close < df_1m.loc[i, 'open']:
                wins += 1
            else:
                losses += 1

# -----------------------------
# 6️⃣ Results
# -----------------------------
total = wins + losses
print("\n----- RESULTS -----")
print("Total trades:", total)
print("Wins:", wins)
print("Losses:", losses)
print("Winrate:", round(wins/total*100,2) if total>0 else 0, "%")
