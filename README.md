# 📊 EURUSD M2 Breakout Pullback Strategy

## 📌 Executive Summary

This repository presents a high-resolution quantitative analysis of a structural breakout-followed-by-pullback strategy on EURUSD, leveraging:

- M2 timeframe for pattern identification  
- M1 timeframe for precise execution  
- Multi-million row dataset (2015–2021)  
- Fully vectorized backtesting pipeline (loop-free, optimized for performance)  

The objective is to rigorously evaluate whether immediate pullbacks after strong breakouts offer a statistically significant edge in ultra-short-term execution.

> **Data Acquisition & Processing:**  
> Raw M1 EURUSD data (2015–2021) was sourced from [Kaggle – Forex EURUSD 1m Data](https://www.kaggle.com/datasets/ankitjha420/forex-eurusd-1m-data-2015-to-2021).  
> Annual CSVs were programmatically ingested, merged, chronologically sorted, and meticulously cleaned to produce a **clean M1 dataset**.  
> Subsequently, 2-minute candles (M2) were generated from the cleaned M1 data, ensuring accurate aggregation and alignment for backtesting.  
> All preprocessing was performed in Python using Visual Studio Code, emphasizing reproducibility, chronological integrity, and completeness.

---

# 🧠 Strategy Framework

## 📈 Bullish Signal

A bullish pattern is confirmed when:

1. M2[i] closes above the high of M2[i-1]  
2. Candle body dominates wicks (body > upper & lower shadows)  

Execution logic:

- During the first minute of M2[i+1]  
- Enter LONG if price breaks above M2[i] open  
- Trade expires at M2[i+1] close

---

## 📉 Bearish Signal

Symmetric bearish logic:

1. M2[i] closes below the low of M2[i-1]  
2. Candle body dominates shadows  

Execution logic:

- During the first minute of M2[i+1]  
- Enter SHORT if price breaks below M2[i] open  
- Trade expires at M2[i+1] close

---

# 🖼 Structural Pattern Visualization

### Bullish Scenario
![Bullish Scenario](patterns/bullish_scenario.png)

### Bearish Scenario
![Bearish Scenario](patterns/bearish_scenario.png)

---

# ⚙️ Dataset Profile

| Metric | Value |
|--------|-------|
| Instrument | EURUSD |
| Timeframe | M1 & M2 |
| M1 Candles | 3,165,120 |
| M2 Candles | 1,582,560 |
| Backtest Type | Fully vectorized |
| Lookahead Bias | Eliminated |
| Data Integrity | M1 merged, cleaned, chronologically sorted, deduplicated; M2 generated from M1 |
| Environment | Python + Pandas in Visual Studio Code |

**Note:** Data preprocessing ensures reproducibility, chronological integrity, and proper aggregation of ultra-high-frequency financial data.

---

# 📈 Backtest Summary

| Metric | Value |
|--------|-------|
| Patterns Detected | 433,334 |
| Trades Executed | 51,980 |
| Wins | 24,330 |
| Losses | 27,650 |
| Win Rate | 46.81% |

---

# 📉 Statistical Evaluation

Assuming a typical 85% binary payout:

- Break-even win rate ≈ 54%  
- Strategy win rate = 46.81%  

Expected value per trade:

E = (0.4681 × 0.85) − (0.5319 × 1) ≈ −0.134R per trade

**Conclusion:** Under standard payout assumptions, the naive breakout-followed-by-pullback strategy does not provide a positive expected return.

---

# 🔎 Insights & Interpretation

- Breakouts frequently exhaust immediate momentum  
- Pullbacks may reflect temporary absorption, not continuation  
- Ultra-short timeframes remain noise-dominated  
- Large-scale testing confirms hypothesis rejection, showcasing quantitative discipline

---

# 🎯 Key Takeaways

- Validation on **3M+ candle dataset**, yielding **50k+ trades** → statistically robust  
- Vectorized implementation ensures computational efficiency and reproducibility  
- Preprocessing pipeline clearly separates **M1 ingestion, M2 generation, and backtesting**, highlighting modular workflow  
- Rigorous falsification of structural hypothesis demonstrates senior-level quantitative thinking

---

# 🚀 Potential Extensions

- Win rate segmentation by trading session (Asia / London / NY)  
- Volatility regime conditioning  
- Breakout size percentile analysis  
- Higher timeframe trend filter integration  
- Pre-breakout range compression detection  

Framework is modular, enabling rapid testing of multiple structural hypotheses.

---

# 🛠 Tech Stack

- Python  
- Pandas (vectorized operations for high-volume processing)  
- Visual Studio Code (robust development environment for large datasets)  

---

# 📌 Author Notes

This project exemplifies:

- Advanced statistical reasoning  
- Large-scale financial data wrangling (M1 → M2)  
- Hypothesis-driven backtesting  
- Clear separation of signal detection, data preparation, and execution logic  

In quantitative research, **robust rejection of hypotheses is as valuable as confirming a strategy**, providing actionable insight for future model iterations.
