# Week 3 Pre-Class Brief - Limited Retention Budget

## Situation

Northstar Retail wants to reduce customer churn, but the business cannot offer every customer a retention incentive. Customer Success has limited time, and each offer has a cost.

The business needs a way to decide which customers should be reviewed or contacted first. The decision should consider customer behaviour, account value, support burden, and business capacity.

## Stakeholders

The main stakeholders are:

- Customer Success manager.
- Finance lead.
- Retention programme owner.

They need a practical way to prioritise customers under a limited budget.

## Data Available

The following file is available in `Starter_Kit/sample_data/`:

| File | Description |
|---|---|
| `week3_retention_training.csv` | Customer-level data about tenure, monthly fee, product usage, support tickets, plan type, discounts, offer response, and next-month retention. |

## Data Fields To Notice

`week3_retention_training.csv` includes:

- `customer_id`
- `tenure_months`
- `monthly_fee`
- `usage_sessions_30d`
- `support_tickets_90d`
- `plan_type`
- `discount_last_90d`
- `post_offer_response`
- `retained_next_month`

## Business Assumptions

For class discussion, assume:

| Assumption | Value |
|---|---:|
| Offer cost | 25 per customer |
| Expected saved margin | 120 for a successfully retained customer |
| Capacity | Only a limited share of customers can be contacted |

## Pre-Class Thinking

Before class, write short notes on these questions:

1. What does the business need to decide?
2. Which fields might indicate that a customer needs attention?
3. Which fields might indicate that a customer is valuable to retain?
4. What would make a simple prioritisation rule acceptable to a business stakeholder?
5. What could go wrong if the business contacts the wrong customers?

## Bring To Class

Bring:

- The Week 3 data file.
- One simple customer-prioritisation idea.
- Two questions you would ask Customer Success before acting on the data.

