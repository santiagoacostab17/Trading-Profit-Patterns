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

# 🔄 Data Processing & Backtest Pipeline

```mermaid
flowchart TD
    A[Raw M1 CSVs (2015–2021) from Kaggle] --> B[Merge & Clean M1 Data]
    B --> C[EURUSD_1m_clean.csv]
    C --> D[Generate 2-minute Candles (M2)]
    D --> E[EURUSD_2m_clean.csv]
    C & E --> F[Backtesting Engine]
    F --> G[Pattern Detection (Bull/Bear)]
    G --> H[Trade Simulation (First minute of next M2)]
    H --> I[Statistical Evaluation & Results]
