# 📊 Stock Market Analysis (NSE Sectors)

## 🚀 Overview

This project performs end-to-end stock market analysis on NSE-listed companies across Banking, IT, and Energy sectors.

It is designed to simulate a real-world data analyst workflow, separating:

- Automated pipeline (production)
- Exploratory analysis (notebook)

---

## 🧠 Project Architecture (IMPORTANT)

This project follows a 2-layer design:

### 1️⃣ app.py → Production Pipeline

Runs a clean, automated workflow:

- Load cleaned data
- Compute returns & statistics
- Generate technical indicators
- Build correlation matrix
- Create visualizations
- Export Excel report

👉 Designed for:
text Fast execution | Reproducibility | Clean output 

---

### 2️⃣ notebooks/stock_analysis.ipynb → Analysis Layer

Used for:

- Deep analysis & explanations  
- Correlation insights  
- Sector-level breakdown  
- Validation checks (RSI, etc.)  
- Exploratory visualizations

👉 Designed for:
text Understanding | Storytelling | Portfolio presentation 

---

## 🔄 Data Flow Design

Raw Data → Cleaning → Clean CSV → Analysis Pipeline 

### First Run (Data Creation)

Set in app.py:

FETCH_NEW_DATA = True 

Run:

uv run python app.py 

This will:

- Fetch stock data
- Clean it
- Save to /data/clean_prices.csv

---

### Normal Usage (Recommended)

Set:

FETCH_NEW_DATA = False 

Run:

uv run python app.py 

This will:

- Load existing clean data
- Run full analysis pipeline

---

## 🧩 What This Project Does

- Fetches 12 months of OHLCV stock data  
- Cleans and validates financial data  
- Computes returns and statistical metrics  
- Implements technical indicators (SMA, RSI, Bollinger Bands) from scratch  
- Performs correlation analysis across stocks  
- Builds interactive Plotly dashboards  
- Generates a professional Excel report

---

## 🛠️ Tech Stack

- Python  
- pandas, numpy  
- matplotlib, seaborn  
- plotly  
- openpyxl  
- yfinance  
- Jupyter Notebook  
- uv (dependency management)

---

## 📁 Project Structure

## stock-analysis/

│
├── data/                      # Output files (CSV, charts, Excel)
├── notebooks/
│   └── stock_analysis.ipynb  # Analysis notebook
├── src/
│   ├── data_loader.py
│   ├── quality_checks.py
│   ├── analysis.py
│   ├── visualization.py
│   ├── report.py
│   └── config.py
│
├── app.py                    # Production pipeline
├── pyproject.toml
├── uv.lock
├── requirements.txt         # Optional fallback
└── README.md

## ⚙️ Installation & Setup

### 1. Clone repository

git clone [https://github.com/aditya2562/stock-analysis-project.git](https://github.com/aditya2562/stock-analysis-project.git) 
cd stock-analysis-project 

---

### 2. Install dependencies (uv)

uv sync 

---

### 3. Run pipeline

uv run python app.py 

---

### Alternative (without uv)

pip install -r requirements.txt 

python app.py 

---

### 4. Run Notebook

uv run jupyter notebook 

Open:

notebooks/stock_analysis.ipynb 

---

## 📊 Key Outputs

- 📈 Candlestick chart with volume  
- 📉 Normalized price comparison  
- ⚖️ Risk vs Return scatter  
- 🔥 Correlation matrix  
- 📑 Multi-sheet Excel report

---

## 🔍 Key Findings

- IT sector stocks (INFY, TCS, WIPRO) show strong positive correlation  
- Banking sector exhibits moderate volatility with stable returns  
- Cross-sector diversification reduces portfolio risk  
- Large-cap stocks influence broader market movement  
- Risk-return analysis identifies efficient stocks

---

## 📌 How to Use This Project

- Use app.py for automated execution  
- Use notebook for detailed analysis and explanation  
- Open Plotly HTML files in browser  
- Review Excel report for portfolio-level insights

---

## 🧠 Learning Outcomes

- Built a modular data pipeline from scratch  
- Implemented financial indicators without external libraries  
- Applied statistical analysis to real-world data  
- Designed production vs analysis architecture  
- Created portfolio-ready deliverables

---

## 📬 Final Note

This project reflects how real-world financial data analysis systems are structured — separating automation from exploration.

---

## ⭐ If you find this useful, consider starring the repo!

