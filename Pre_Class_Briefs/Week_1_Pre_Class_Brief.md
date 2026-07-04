# Week 1 Pre-Class Brief - Reporting Fire Drill

## Situation

Northstar Retail sends a weekly KPI pack to the COO. The report is due every Monday morning, but the current process depends on manual copying from several files. The usual analyst is unavailable this week, and the COO still needs a clear view of customer, revenue, and support performance.

The immediate concern is whether the team can produce the weekly numbers consistently from the available source files.

## Stakeholder

The COO wants a concise weekly view of business health.

Typical questions from the COO may include:

- How many customers are currently active?
- How much revenue was recorded for the month?
- Are there support issues that need attention?
- Can the numbers be traced back to source files?

## Data Available

The following files are available in `Starter_Kit/sample_data/`:

| File | Description |
|---|---|
| `week1_customers.csv` | Customer records, subscription status, plan type, login date, and paid status. |
| `week1_sales.csv` | June order records, gross amount, and refund amount. |
| `week1_support.csv` | Support ticket records, open/closed dates, and severity. |
| `week1_metric_definitions.md` | Business definitions for the weekly KPI pack. |

## Data Fields To Notice

`week1_customers.csv` includes:

- `customer_id`
- `signup_date`
- `subscription_status`
- `plan`
- `last_login_date`
- `is_paid`

`week1_sales.csv` includes:

- `order_id`
- `customer_id`
- `order_date`
- `gross_amount`
- `refund_amount`

`week1_support.csv` includes:

- `ticket_id`
- `customer_id`
- `opened_date`
- `closed_date`
- `severity`

## Pre-Class Thinking

Before class, write short notes on these questions:

1. Which numbers would you expect in a weekly KPI pack for the COO?
2. Which data file would you use for each number?
3. Which words or business terms might need clarification before the report is sent?
4. What would make you confident that a number in the report is traceable?
5. What questions would you ask the COO before treating the report as final?

## Bring To Class

Bring:

- The data files listed above.
- One or two questions about the meaning of the fields.
- A short list of the KPI numbers you think the COO would expect.

