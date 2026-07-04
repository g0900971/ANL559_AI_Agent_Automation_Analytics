# Week 4 Example - Input Contract

Valid request:

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

Reject:

- Missing `customer_id`.
- Negative `tenure_months`.
- Unknown `plan_type`.
- Missing usage data.

Every successful response should include recommendation, reason, and version.
