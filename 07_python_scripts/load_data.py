# =================================
# Import Libraries
# =================================

import os
import pandas as pd
from sqlalchemy import create_engine, URL

# ==================================
# Configuration
# ==================================

DATABASE_NAME = "cyclistic"
DATABASE_USER = "postgres"
DATABASE_PASSWORD = "sid@1201"
DATABASE_HOST = "localhost"
DATABASE_PORT ="5432"

DATA_FOLDER = r"C:\Users\Siddharth Ganvir\Desktop\Data Analytics Capstone Project\01_raw_data"

# ===================================
# Database Connection
# ===================================

def connect_database():

    connection_url = URL.create(
        drivername="postgresql+psycopg2",
        username=DATABASE_USER,
        password=DATABASE_PASSWORD,
        host=DATABASE_HOST,
        port=DATABASE_PORT,
        database=DATABASE_NAME,
    )

    engine = create_engine(connection_url)

    try:
        with engine.connect() as connection:
            print("Successfully connected to PostgreSQL !\n")
        return engine

    except Exception as e:
        print("Database Connection Failed")
        print(e)
        return None

# ===================================
# Get All CSV Filea
# ===================================

def get_csv_files():

    csv_files =sorted(
        [
        file for file in os.listdir(DATA_FOLDER)
        if file.endswith(".csv")
    ]
)

    if not csv_files:
        print("No CSV files found!")
        return[]

    print(f"Found {len(csv_files)} CSV files.\n")
    return csv_files

# ===================================
# Read First CSV
# ===================================

def read_csv_file(file_path):

    df = pd.read_csv(file_path)

    print(f"Rows   :  {len(df)}")
    print(f" Columns : {len(df.columns)}")

    return df


# ====================================
# Convert Data Types
# ====================================
def transform_data(df):

    df["started_at"] = pd.to_datetime(df["started_at"])
    df["ended_at"] = pd.to_datetime(df["ended_at"])

    return df


# ==================================
# Load Data into PostgreSQL
# ==================================

def load_to_database(df,engine):
    
    df.to_sql(
        name="bike_trips",
        con=engine,
        if_exists= "append",
        index = False,
        method = "multi"
    )

    print("Data successfully loaded into PostgreSQL! ")

# ================================
# Processing CSV files
# ================================

def process_files(engine,csv_files):

    for index, file in enumerate(csv_files, start=1):
        print("=" * 60)
        print(f"Processing File {index}/{len(csv_files)}")
        print(file)
        print("=" * 60)

        file_path = os.path.join(DATA_FOLDER, file)
        df = read_csv_file(file_path)
        df = transform_data(df)
        load_to_database(df, engine)

def main():

    engine = connect_database()

    if engine is None:
        return
    
    csv_files = get_csv_files()
    process_files(engine, csv_files)

if __name__ == "__main__":
    main()
