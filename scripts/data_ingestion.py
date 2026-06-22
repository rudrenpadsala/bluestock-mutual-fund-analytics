import pandas as pd
from pathlib import Path

data_path = Path("data/raw")

for file in data_path.glob("*.csv"):

    print("=" * 80)
    print("FILE:", file.name)

    df = pd.read_csv(file)

    print("\nShape")
    print(df.shape)

    print("\nColumns")
    print(df.columns.tolist())

    print("\nDtypes")
    print(df.dtypes)

    print("\nHead")
    print(df.head())

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nDuplicates")
    print(df.duplicated().sum())