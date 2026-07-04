# Worked Examples

These examples give instructors and students concrete models of the evidence expected in the Studio Refresh. They are intentionally short enough to discuss in class.

Use them in three ways:

- Before a sprint, show the structure of a strong artefact.
- During peer review, compare student evidence against the example.
- After class, use the examples as feedback language.

## Week 1 - Strong Agent Work Order

```text
Goal:
Create a reproducible weekly KPI workflow for the COO.

Inputs:
- week1_customers.csv
- week1_sales.csv
- week1_support.csv
- week1_metric_definitions.md

Definitions:
- Paid active accounts: subscription_status is active and is_paid is true.
- Net June revenue: sum gross_amount minus refund_amount for June orders.
- Open support tickets: tickets with blank closed_date.

Acceptance criteria:
- Script runs from a clean folder.
- Paid active accounts equals 6.
- Net June revenue equals 2660.
- Open support tickets equals 3.
- Output includes a short notes section listing assumptions.

Constraints:
- Do not redefine active customer.
- Do not use recent login as a substitute for paid active account.
- If a definition is missing, stop and ask.
```

### Why This Is Strong

- It gives the agent a job, not a vague wish.
- It names source files and approved definitions.
- It includes known checks that can fail.
- It tells the agent what not to do.

### Weak Version

```text
Make a KPI report and explain the numbers.
```

This is weak because the agent can choose definitions, output format, and checks without supervision.

## Week 1 - Example AI-Use Log Entry

| Task given to agent | Output accepted | Output rejected or changed | Evidence used |
|---|---|---|---|
| Draft a Python script for weekly KPI checks. | File loading structure and revenue calculation. | Agent counted active customers using last login instead of paid active subscription. | `week1_metric_definitions.md` and known check: paid active accounts equals 6. |

## Week 2 - Row-Count Bridge

| Step | Row count | Notes |
|---|---:|---|
| Subscriptions source | 10 | Billing system scope. |
| Product events source | 9 | Includes C999, not in billing system. |
| Left join subscriptions to product events | 10 | Keeps all subscription customers. |
| Customers without product events | 1 | C204 requires quarantine. |
| Product-only records | 1 | C999 is outside billing scope. |

### Example Quarantine Rows

| customer_id | issue_type | why_it_matters | recommended_action |
|---|---|---|---|
| C204 | Missing product event | Inner join would remove a cancelled subscription customer. | Keep in churn denominator; flag missing usage. |
| C999 | Product event without subscription | Product activity is outside billing scope. | Exclude from billing churn; investigate source mapping. |

## Week 2 - Trusted-Number Note

```text
We recommend using the billing churn number for the board paper because the board decision concerns paying subscriptions. Product activity remains useful as a diagnostic signal, but it should not define the denominator. The previous numbers differed because one workflow used billing-end dates and another workflow used product activity as the active base. The remaining limitation is that C204 has a missing cancellation reason and should be reviewed by Customer Success.
```

## Week 3 - Leakage Audit

| Column | Decision-time availability | Keep or exclude | Reason |
|---|---|---|---|
| tenure_months | Available | Keep | Known before offer decision. |
| monthly_fee | Available | Keep | Billing attribute. |
| usage_sessions_30d | Available | Keep | Observed before decision. |
| support_tickets_90d | Available | Keep | Observed before decision. |
| plan_type | Available | Keep | Customer attribute. |
| discount_last_90d | Available | Keep with caution | May reflect prior intervention. |
| post_offer_response | Not available | Exclude | It happens after offer decision. |
| retained_next_month | Not available | Target only | This is the outcome being predicted. |

## Week 3 - Decision Memo Excerpt

```text
Recommendation:
Run a limited retention pilot for the top 30 percent of customers ranked by churn risk, excluding any post-offer features from the model.

Evidence:
The candidate policy is compared against two baselines: highest support burden and lowest usage. The model excludes retained_next_month and post_offer_response because those fields are not known at decision time.

Decision logic:
At an offer cost of 25 and expected saved margin of 120, the policy needs to save more than 20.8 percent of contacted customers to break even.

Limit:
This is not a causal estimate of the offer effect. It is a prioritisation policy for a pilot.
```

## Week 4 - Input Contract

```json
{
  "customer_id": "string, required",
  "tenure_months": "integer >= 0, required",
  "monthly_fee": "number >= 0, required",
  "usage_sessions_30d": "integer >= 0, required",
  "support_tickets_90d": "integer >= 0, required",
  "plan_type": "one of: monthly, annual, enterprise"
}
```

### Expected Responses

| Request | Expected behaviour |
|---|---|
| Valid request for C301 | Return recommendation, score or rule, and version. |
| Missing customer_id | Reject with clear error message. |
| Negative tenure_months | Reject with clear error message. |
| Unknown plan_type | Reject with allowed values. |

## Week 4 - Runbook Excerpt

```text
Health check:
Run the good-input request and confirm the response includes recommendation, reason, and version.

Known failure:
Malformed request causes validation failure.

Immediate action:
Do not edit production data. Capture request payload, confirm validation message, and route to analytics owner.

Rollback:
Use previous rule version v0.1 if current version rejects valid requests.
```

## Week 5 - Safe Executive Answer

```text
June churn rose from 9.4 percent to 11.8 percent. The increase is concentrated among monthly-plan customers with fewer than five usage sessions in the last 30 days, based on the KPI Pack.

One plausible explanation is onboarding friction: the Support Summary says onboarding-delay tickets increased in June, especially for customers who signed up in April and May. This is not proof of causality.

The evidence does not support saying the May price increase caused the churn increase, because the Pricing Note says existing customers were not moved to the new price in June.

Recommended next test:
Compare churn among low-usage new customers with and without onboarding-delay tickets, then review whether the timing precedes cancellation.
```

### Why This Is Strong

- It separates observation from explanation.
- It cites evidence that supports each claim.
- It refuses an unsupported causal claim.
- It proposes a next test.

## Week 6 - Launch Recommendation

```text
Recommendation:
Limited pilot, not full launch.

Scope:
Use the automation for weekly KPI preparation and internal review. Do not use the analyst-agent output for external executive claims without human review.

Strongest evidence:
The KPI workflow has smoke checks for paid active accounts, net revenue, and open support tickets. The reconciliation workflow reports join coverage and quarantines unmatched records.

Residual risk:
The retention decision model has been checked for obvious leakage, but the business impact of offers has not been causally estimated.

Owner:
Analytics lead owns monitoring and rollback. Customer Success owns review of quarantined cancellation records.
```

## Feedback Language For Instructors

Use feedback that points to evidence:

- "Your artefact runs, but your defence does not name the failure it prevents."
- "This is a useful agent prompt, but it needs an acceptance test."
- "The model score is not yet a decision policy."
- "The answer is fluent, but the cited source does not support that causal claim."
- "A limited pilot is a valid launch recommendation because you named scope and owner."
