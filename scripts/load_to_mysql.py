import os
from pathlib import Path

import pandas as pd
import mysql.connector
from dotenv import load_dotenv


# ==========================================
# PROJECT PATH
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent


# ==========================================
# LOAD ENVIRONMENT VARIABLES
# ==========================================

load_dotenv(BASE_DIR / ".env")

MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")

if not MYSQL_PASSWORD:
    raise ValueError(
        "MYSQL_PASSWORD was not found. "
        "Make sure your .env file exists in the project root."
    )


# ==========================================
# LOAD CLEAN DATASET
# ==========================================

print("Loading cleaned dataset...")

csv_path = BASE_DIR / "data" / "clean" / "listings_clean.csv"

listings = pd.read_csv(
    csv_path,
    low_memory=False
)

print(f"Rows: {len(listings)}")
print(f"Columns: {len(listings.columns)}")


# ==========================================
# CONNECT TO MYSQL
# ==========================================

print("\nConnecting to MySQL...")

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=MYSQL_PASSWORD,
    database="airbnb_market_analysis"
)

cursor = connection.cursor()

print("✅ Connected to MySQL successfully!")


# ==========================================
# VERIFY DATABASE
# ==========================================

cursor.execute("SELECT DATABASE();")

database = cursor.fetchone()[0]

print(f"Connected database: {database}")


# ==========================================
# CLOSE CONNECTION
# ==========================================

cursor.close()
connection.close()

print("\n✅ Connection test completed successfully!")