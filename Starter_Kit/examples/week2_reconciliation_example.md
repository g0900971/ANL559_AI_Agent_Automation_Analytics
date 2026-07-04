# Week 2 Example - Reconciliation Evidence

## Source Counts

| Source | Rows | Notes |
|---|---:|---|
| subscriptions | 10 | Billing source. |
| cancellations | 3 | Cancellation requests and billing end dates. |
| product events | 9 | Product activity source. |

## Quarantine Examples

| customer_id | issue | action |
|---|---|---|
| C204 | Cancelled subscription has no product event. | Keep in billing churn review; flag missing product usage. |
| C999 | Product event has no subscription record. | Exclude from billing churn; investigate mapping. |

## Defence

The billing churn number should be used for board reporting because the board decision concerns subscriptions. Product activity is diagnostic evidence, not the denominator.
