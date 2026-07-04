# Week 2 Pre-Class Brief - The Board Number Is Wrong

## Situation

Northstar Retail is preparing board materials. Finance and Product have reported different churn numbers. Both teams believe their number is reasonable because each team works from a different operational view of the business.

The board paper needs one number that can be explained clearly. The team must understand which sources are available, what each source represents, and what questions need to be answered before a number is used in board materials.

## Stakeholders

The main stakeholders are:

- Finance lead.
- Product lead.
- Board secretary.

Each stakeholder may care about a different view of churn, customer activity, or subscription status.

## Data Available

The following files are available in `Starter_Kit/sample_data/`:

| File | Description |
|---|---|
| `week2_subscriptions.csv` | Subscription plan, billing status, billing start date, and billing end date. |
| `week2_cancellations.csv` | Cancellation request date, billing end date, and cancellation reason. |
| `week2_product_events.csv` | Recent product activity by customer, including sessions and active feature count. |

## Data Fields To Notice

`week2_subscriptions.csv` includes:

- `customer_id`
- `plan`
- `billing_status`
- `billing_start`
- `billing_end`

`week2_cancellations.csv` includes:

- `customer_id`
- `cancel_request_date`
- `billing_end_date`
- `cancel_reason`

`week2_product_events.csv` includes:

- `customer_id`
- `last_event_date`
- `sessions_30d`
- `active_feature_count`

## Pre-Class Thinking

Before class, write short notes on these questions:

1. What might Finance mean by churn?
2. What might Product mean by churn or customer activity?
3. Which source would you expect each team to trust most?
4. What information would you want before choosing one number for the board paper?
5. What could make two reasonable teams report different numbers?

## Bring To Class

Bring:

- The three Week 2 data files.
- A short description of what each file appears to represent.
- Two questions you would ask Finance or Product before using the number in board materials.

