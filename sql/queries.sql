-- Top 5 Funds by AUM

SELECT
scheme_name,
aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- Average NAV

SELECT
AVG(nav)
FROM nav_history;

-- Transactions by State

SELECT
state,
COUNT(*)
FROM investor_transactions
GROUP BY state;

-- Expense Ratio < 1

SELECT
scheme_name,
expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1;

-- Highest Return

SELECT
scheme_name,
return_1yr_pct
FROM scheme_performance
ORDER BY return_1yr_pct DESC
LIMIT 10;

-- Average Transaction Amount

SELECT
AVG(amount_inr)
FROM investor_transactions;

-- Total Investors

SELECT
COUNT(DISTINCT investor_id)
FROM investor_transactions;

-- Maximum NAV

SELECT
MAX(nav)
FROM nav_history;

-- Minimum NAV

SELECT
MIN(nav)
FROM nav_history;

-- Fund Count by Category

SELECT
category,
COUNT(*)
FROM scheme_performance
GROUP BY category;