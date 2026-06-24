import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

files = {
    "nav_history":
    "data/processed/nav_history_clean.csv",

    "investor_transactions":
    "data/processed/investor_transactions_clean.csv",

    "scheme_performance":
    "data/processed/scheme_performance_clean.csv"
}

for table, file in files.items():

    df = pd.read_csv(file)

    df.to_sql(
        table,
        engine,
        if_exists="replace",
        index=False
    )

    print(
        f"{table} loaded:",
        len(df)
    )

print("Database Created")