# Airbnb Market Intelligence & Customer Behavior Analytics

An end-to-end data analytics project analyzing Airbnb listing data to uncover market patterns, availability trends, room-type distribution, and neighborhood-level insights using Python, SQL, MySQL, SQLite, and Power BI.

## 📊 Project Overview

This project demonstrates a complete analytics workflow — from data profiling and cleaning to exploratory analysis, SQL-based analysis, database integration, and interactive Power BI reporting.

The cleaned Airbnb dataset contains **30,259 records and 78 attributes**.

## 🎯 Objectives

- Profile and understand the Airbnb listings dataset
- Clean and prepare data for analysis
- Explore listing, availability, room-type, and neighborhood patterns
- Perform analytical queries using SQL
- Store and integrate cleaned data with MySQL
- Build interactive Power BI reporting
- Generate visual outputs to communicate business insights

## 🧠 Methods & Analysis

- Data Profiling
- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Descriptive Statistics
- Missing-Value Analysis
- Distribution Analysis
- Categorical Data Analysis
- Neighborhood-Level Analysis
- Availability Analysis
- Room-Type Analysis
- SQL Querying & Aggregation
- SQLite Database Analysis
- MySQL Database Integration
- Business Intelligence & Dashboarding

## 🛠 Tools & Technologies

**Programming & Data Analysis**
- Python
- Pandas
- NumPy
- Jupyter Notebook

**Databases & SQL**
- SQL
- SQLite
- MySQL
- MySQL Connector/Python
- SQLAlchemy

**Visualization & BI**
- Matplotlib
- Power BI
- Power BI Desktop

**Development & Version Control**
- Visual Studio Code
- Git
- GitHub
- Python-dotenv
- Environment Variables

## 📁 Project Structure

```text
Airbnb-Market-Intelligence-Customer-Behavior-Analytics/
│
├── data/
│   ├── raw/                         # Original source data
│   ├── clean/                       # Cleaned analytical datasets
│   │   ├── airbnb_analytics.csv
│   │   └── listings_clean.csv
│   └── reports/                     # Data-quality reports
│       └── missing_report.csv
│
├── notebooks/
│   ├── 01_data_profiling.ipynb      # Dataset profiling
│   ├── 02_data_cleaning.ipynb       # Cleaning and preprocessing
│   ├── 03_eda.ipynb                 # Exploratory data analysis
│   ├── 04_SQLite_and_SQL.ipynb      # SQLite and SQL workflow
│   └── 05_SQL_Analysis.ipynb        # SQL business analysis
│
├── sql/                              # SQL scripts and queries
│
├── scripts/
│   └── load_to_mysql.py              # MySQL data-loading script
│
├── powerbi/
│   └── Airbnb.pbix                   # Power BI dashboard
│
├── visuals/
│   ├── availability_distribution.png
│   ├── room_type_distribution.png
│   ├── top_10_neighbourhood.png
│   └── top_10_neighbourhoods.png
│
├── .gitignore
└── README.md
```

## 📈 Key Analysis Areas

### Listing & Market Analysis
- Listing distribution across neighborhoods
- Room-type composition
- Neighborhood-level listing concentration
- Availability patterns

### Data Quality
- Missing-value identification
- Dataset profiling
- Data cleaning and preprocessing
- Validation of cleaned analytical data

### SQL Analysis
- Filtering and aggregation
- Group-based analysis
- Listing and neighborhood comparisons
- Business-oriented analytical queries

### Business Intelligence
- Interactive Power BI dashboard
- KPI-oriented reporting
- Visual exploration of Airbnb market patterns
- Data-driven market insights

## 🔄 Analytics Workflow

```text
Raw Airbnb Data
      ↓
Data Profiling
      ↓
Data Cleaning & Validation
      ↓
Exploratory Data Analysis
      ↓
SQLite / SQL Analysis
      ↓
MySQL Database Integration
      ↓
Power BI Dashboard
      ↓
Business Insights
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/pakku251201/Airbnb-Market-Intelligence-Customer-Behavior-Analytics.git
cd Airbnb-Market-Intelligence-Customer-Behavior-Analytics
```

### 2. Install dependencies

```bash
pip install pandas numpy matplotlib mysql-connector-python sqlalchemy python-dotenv jupyter
```

### 3. Configure MySQL

Create a `.env` file in the project root:

```env
MYSQL_PASSWORD=your_mysql_password
```

The `.env` file is excluded from GitHub using `.gitignore`.

### 4. Run the notebooks

Execute the notebooks in order:

1. `01_data_profiling.ipynb`
2. `02_data_cleaning.ipynb`
3. `03_eda.ipynb`
4. `04_SQLite_and_SQL.ipynb`
5. `05_SQL_Analysis.ipynb`

### 5. Load data into MySQL

Ensure MySQL is running and the `airbnb_market_analysis` database exists.

```bash
python3 scripts/load_to_mysql.py
```

### 6. Open the Power BI dashboard

Open `powerbi/Airbnb.pbix` using Power BI Desktop.

## 📌 Project Highlights

- Processed **30,259 Airbnb listings across 78 attributes**
- Built an end-to-end workflow spanning profiling, cleaning, EDA, SQL, database integration, and BI
- Performed SQL-based market and listing analysis
- Integrated cleaned data with MySQL
- Developed Power BI reporting for interactive market exploration
- Created visual analyses for availability, room types, and top neighborhoods
- Used environment variables to keep database credentials out of source code

## 👤 Author

**Pratheek P Rao**

Data Analytics | Business Analytics | Python | SQL | Power BI
