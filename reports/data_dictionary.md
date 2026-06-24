# Data Dictionary

## 02_nav_history.csv

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Mutual Fund Scheme Code |
| date | Date | NAV Date |
| nav | Float | Net Asset Value |

## 08_investor_transactions.csv

| Column | Type | Description |
|----------|----------|----------|
| investor_id | Integer | Investor ID |
| transaction_date | Date | Transaction Date |
| amfi_code | Integer | Fund Code |
| transaction_type | Text | SIP/Lumpsum/Redemption |
| amount_inr | Float | Investment Amount |
| state | Text | Investor State |
| city | Text | Investor City |
| kyc_status | Text | KYC Verification Status |

## 07_scheme_performance.csv

| Column | Type | Description |
|----------|----------|----------|
| scheme_name | Text | Fund Name |
| return_1yr_pct | Float | 1 Year Return |
| return_3yr_pct | Float | 3 Year Return |
| return_5yr_pct | Float | 5 Year Return |
| expense_ratio_pct | Float | Expense Ratio |
| sharpe_ratio | Float | Sharpe Ratio |
| aum_crore | Float | Assets Under Management |