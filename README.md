# 📊 Trading Profit Patterns

## 📌 Overview
**Python-based quantitative analysis** of high-frequency EURUSD price data.  

The project detects **short-term bullish and bearish patterns** and evaluates their predictive reliability using **1-minute and 2-minute candle data**.  

Demonstrates **data cleaning, aggregation, vectorized analysis, and reproducible workflows** for high-volume financial datasets.

---

## ⚙️ Workflow

### 1️⃣ System Recognition
- **Domain:** Forex high-frequency price pattern analysis  
- **Goal:** Identify statistically significant short-term patterns  
- **Constraint:** Efficiently handle millions of candles with reproducible analysis

### 2️⃣ Data Collection
- Source: [Kaggle – Forex EURUSD 1m Data](https://www.kaggle.com/datasets/ankitjha420/forex-eurusd-1m-data-2015-to-2021)  
- Aggregate raw 1-minute data into 2-minute intervals

### 3️⃣ Data Cleaning
- Deduplicate and sort data chronologically  
- Standardize columns and handle missing or unnecessary data  

### 4️⃣ Exploratory Analysis
- Compute candle features (body, top/bottom wicks)  
- Detect upward (bullish) and downward (bearish) patterns  
- Evaluate subsequent interval outcomes for reliability

### 5️⃣ Visualization
- Display representative **upward and downward patterns** for visual inspection  

**Upward Pattern:**  
[![Upward Pattern](patterns/upward_pattern.png)](patterns/upward_pattern.png)  

**Downward Pattern:**  
[![Downward Pattern](patterns/downward_pattern.png)](patterns/downward_pattern.png)

### 6️⃣ Insights
- **Patterns detected:** 81,938  
- **Success rate:** 51%  
- High-frequency price series are **noise-dominated**; short-term patterns show limited predictive power  
- Modular workflow ensures **reproducibility and scalability**

---

## 🚀 Key Features

| Feature | Technique / Concept |
|---------|-------------------|
| High-frequency analysis | 1-min and 2-min EURUSD candles |
| Pattern detection | Bullish & bearish candle patterns |
| Vectorized evaluation | Efficient analysis on millions of rows |
| Data aggregation | Deduplication, resampling, column standardization |
| Visualization | Sequential pattern inspection |
| Reproducible workflow | Modular scripts and backtesting pipeline |

---

## 🛠️ How to Run
1. Prepare raw EURUSD CSV files in a `data` folder  
2. Run cleaning and aggregation scripts  
3. Run pattern detection/backtesting scripts  
4. Outputs include **cleaned datasets, trade metrics, and pattern visualizations**

---

## 📊 Process Flow Diagram

[![Trading Workflow](patterns/trading_flow.png)](patterns/trading_flow.png)  
*Steps: data ingestion → cleaning → aggregation → pattern detection → evaluation → visualization*
