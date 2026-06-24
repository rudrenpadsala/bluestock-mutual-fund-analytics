import pandas as pd

print("Loading NAV History...")

df = pd.read_csv("data/raw/02_nav_history.csv")

print("Original Shape:", df.shape)

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Sort
df = df.sort_values(
    ["amfi_code", "date"]
)

# Forward fill missing NAV
df["nav"] = (
    df.groupby("amfi_code")["nav"]
      .ffill()
)

# Remove duplicates
df = df.drop_duplicates()

# Keep only positive NAV
df = df[df["nav"] > 0]

print("Cleaned Shape:", df.shape)

df.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

print("nav_history_clean.csv saved")