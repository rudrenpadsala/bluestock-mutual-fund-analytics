# 📊 Bluestock Mutual Fund Analytics

## Project Overview

This project is part of the Bluestock Internship Program and focuses on analyzing mutual fund data using Python, SQL, SQLite, and data analytics techniques.

The objective is to build a complete Mutual Fund Analytics platform that performs data ingestion, cleaning, validation, database management, and analytical reporting on mutual fund datasets.

---

## 🚀 Technologies Used

* Python
* Pandas
* NumPy
* Requests
* SQLAlchemy
* SQLite
* Jupyter Notebook
* Git & GitHub
* Matplotlib
* Seaborn
* Plotly

---

## 📂 Project Structure

```text
mutual_fund_analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── scripts/
│   ├── data_ingestion.py
│   ├── live_nav_fetch.py
│   ├── fetch_5_schemes.py
│   ├── clean_nav_history.py
│   ├── clean_investor_transactions.py
│   ├── clean_scheme_performance.py
│   └── load_sqlite.py
│
├── notebooks/
│   └── explore_fund_master.ipynb
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── reports/
│   ├── day1_data_quality_summary.md
│   └── data_dictionary.md
│
├── dashboard/
│
├── bluestock_mf.db
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📌 Project Tasks

### Day 1 – Data Ingestion

* Project setup and GitHub integration
* Dataset loading and inspection
* Data quality checks
* Fetching live NAV data from MFAPI
* Downloading NAV history for selected mutual funds
* Exploring Fund Master dataset
* AMFI code validation

### Day 2 – Data Cleaning & Database Design

* Cleaning NAV history dataset
* Cleaning investor transaction dataset
* Cleaning scheme performance dataset
* Data validation and anomaly detection
* SQLite database creation
* Star schema design
* Loading cleaned data into SQLite
* Writing analytical SQL queries
* Creating data dictionary

---

## 📈 Datasets Used

1. Fund Master
2. NAV History
3. AUM by Fund House
4. Monthly SIP Inflows
5. Category Inflows
6. Industry Folio Count
7. Scheme Performance
8. Investor Transactions
9. Portfolio Holdings
10. Benchmark Indices

---

## 🔍 Key Analysis

* Top Funds by AUM
* Average NAV Trends
* Investor Transaction Analysis
* SIP Growth Analysis
* Expense Ratio Comparison
* Fund Performance Evaluation
* Risk Metrics Analysis
* Category-wise Fund Insights

---

## 🗄 Database

Database File:

```text
bluestock_mf.db
```

Main Tables:

* dim_fund
* fact_nav
* fact_transactions
* fact_performance

---

## ▶️ How to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Data Ingestion

```bash
python scripts/data_ingestion.py
```

### Fetch Live NAV

```bash
python scripts/live_nav_fetch.py
```

### Fetch Mutual Fund NAV Data

```bash
python scripts/fetch_5_schemes.py
```

### Clean Data

```bash
python scripts/clean_nav_history.py

python scripts/clean_investor_transactions.py

python scripts/clean_scheme_performance.py
```

### Load Data into SQLite

```bash
python scripts/load_sqlite.py
```

---

## 📊 Future Enhancements

* Power BI Dashboard
* Risk Analytics Dashboard
* Sharpe Ratio Analysis
* Sortino Ratio Analysis
* Alpha & Beta Analysis
* Portfolio Performance Tracking
* Automated Data Refresh

---

## 👨‍💻 Author

**Rudren Padsala**

Bluestock Internship Project

Mutual Fund Analytics Capstone
