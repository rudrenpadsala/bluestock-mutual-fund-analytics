import pandas as pd

print("Loading Investor Transactions...")

df = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

print("Original Shape:", df.shape)

# Convert date
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

# Standardize transaction type
df["transaction_type"] = (
    df["transaction_type"]
    .astype(str)
    .str.strip()
    .str.title()
)

# Valid amount
df = df[df["amount_inr"] > 0]

# Valid KYC values
valid_kyc = [
    "Verified",
    "Pending",
    "Rejected"
]

df = df[
    df["kyc_status"].isin(valid_kyc)
]

# Remove duplicates
df = df.drop_duplicates()

print("Cleaned Shape:", df.shape)

df.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("investor_transactions_clean.csv saved")