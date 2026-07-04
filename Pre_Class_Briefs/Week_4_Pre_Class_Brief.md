# Week 4 Pre-Class Brief - From Notebook To Tool

## Situation

Northstar Retail has analysis that may help Customer Success prioritise customers. Operations is interested, but they do not want to depend on an analyst manually running a notebook each time a decision is needed.

The business wants a small internal tool or operating process that takes a customer request and returns a clear recommendation or result.

## Stakeholders

The main stakeholders are:

- Operations manager.
- Customer Success team.
- Analytics team.

Operations wants something understandable, repeatable, and safe for internal use.

## Data Or Inputs Available

The class will use the Week 3 customer-prioritisation context and a suggested request format.

Suggested request fields:

| Field | Description |
|---|---|
| `customer_id` | Customer identifier. |
| `tenure_months` | Number of months the customer has been with Northstar. |
| `monthly_fee` | Current monthly fee. |
| `usage_sessions_30d` | Number of product usage sessions in the last 30 days. |
| `support_tickets_90d` | Number of support tickets in the last 90 days. |
| `plan_type` | Customer plan type. |

Example request:

```json
{
  "customer_id": "C301",
  "tenure_months": 14,
  "monthly_fee": 79,
  "usage_sessions_30d": 5,
  "support_tickets_90d": 3,
  "plan_type": "monthly"
}
```

## Pre-Class Thinking

Before class, write short notes on these questions:

1. Who would use this internal tool or process?
2. What information would the user need to provide?
3. What output would be useful to the user?
4. What could make a tool confusing or risky for an operations user?
5. What instructions would someone need if the original analyst is unavailable?

## Bring To Class

Bring:

- Your Week 3 prioritisation idea or notes.
- A sketch of what an operations user would enter.
- A sketch of what the user should receive back.
- Two questions you would ask Operations before releasing an internal tool.

