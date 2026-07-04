# Sample Data and Scenarios

This file makes the studio missions self-contained. The data are synthetic and intentionally small. They are not intended for production-quality modelling; they are designed to reveal common analytics automation failures.

The sample files live in `Starter_Kit/sample_data/`. Instructors may replace them with richer datasets, but the teaching logic works with these files.

For the fuller weekly stakeholder stories, classroom traps, expected evidence, and instructor solution guidance, use `Weekly_Case_Packs.md`. This file focuses on the fictional organisation, data files, known checks, and intentional defects.

## Fictional Organisation

The course uses a fictional company, Northstar Retail. Northstar sells subscription-based retail analytics services to small merchants. The company tracks customers, sales, support tickets, product usage, cancellations, and retention offers.

The recurring stakeholder roles are:

- **COO:** wants the weekly KPI pack.
- **Finance lead:** owns billing definitions.
- **Product lead:** owns usage definitions.
- **Operations manager:** wants a usable internal tool.
- **CEO:** asks executive questions.
- **Launch committee:** decides whether the automation can go live.

## Week 1 Files

Files:

- `week1_customers.csv`
- `week1_sales.csv`
- `week1_support.csv`
- `week1_metric_definitions.md`

Teaching defects:

- "Active customer" can mean recent login or paid active account.
- Revenue can be gross or net of refunds.
- Support tickets can be counted by opened date or closed date.

Known checks for the sample data:

- Paid active accounts: 6.
- Customers with any login in the last 30 days from 2026-06-26: 7.
- Gross June revenue in the sample: 2860.
- Net June revenue after refunds in the sample: 2660.
- Open support tickets: 3.

Students should discover that the paid active count and recent-login count are different. If the agent uses recent login as the denominator for active customers, the KPI pack is wrong for the COO's definition.

## Week 2 Files

Files:

- `week2_subscriptions.csv`
- `week2_cancellations.csv`
- `week2_product_events.csv`

Teaching defects:

- One cancelled account has no product event.
- One product-active account is not in the subscription file.
- Cancellation date and billing-end date imply different churn windows.
- An inner join makes the data look cleaner than it is.

Expected student evidence:

- Source row counts.
- Join coverage.
- Quarantine table.
- Churn definition note.

Example row-count story:

- Subscriptions source has 10 rows.
- Cancellation source has 3 rows.
- Product events source has 9 rows.
- A left join from subscriptions to product events should expose missing usage for customer C204.
- A full outer review should expose product customer C999 as out of contract scope.

## Week 3 Files

Files:

- `week3_retention_training.csv`

Teaching defects:

- `retained_next_month` is the target and must not be used as a feature.
- `post_offer_response` is post-decision information and should be excluded.
- Accuracy can look high if most customers do not churn.
- The useful output is a ranked list or threshold, not only a model score.

Simple cost assumptions:

- Offer cost: 25 per customer.
- Expected saved margin: 120 for a truly saved customer.
- Capacity: contact only 30 percent of customers in the sample exercise.

Suggested baselines:

- Target customers with highest complaint count.
- Target customers with lowest product usage.
- Target customers with month-to-month plan and high support burden.

## Week 4 Scenario

Students can build any small internal tool, but the input contract should be explicit.

Suggested request schema:

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

Required behaviour:

- Return a retention recommendation for a valid request.
- Reject missing `customer_id`.
- Reject negative `tenure_months`.
- Reject unknown `plan_type`.
- Record the model or rule version used.

Students may implement the tool as:

- A Python function with tests.
- A command-line script.
- A small API.
- A lightweight dashboard.
- A spreadsheet with locked validation rules.

## Week 5 Files

Files:

- `week5_knowledge_base.md`
- `week5_eval_cases.csv`

Teaching defects:

- The agent may claim churn rose because of price changes even when evidence only shows timing.
- The agent may cite a source that mentions churn but does not support the specific claim.
- The agent may answer a policy question outside the approved evidence.

Expected answer structure:

1. Observed pattern.
2. Evidence and source reference.
3. Plausible explanation, labelled as uncertain.
4. Recommended next test.
5. What the agent should not claim.

## Week 6 Incident Injects

Use these incident injects during final demos:

1. **Metric drift:** the active customer count differs from last week's expected range.
2. **Bad input:** an operations user sends a request with missing fields.
3. **Unsupported executive claim:** a stakeholder asks the team to state that a campaign caused churn reduction.
4. **Ownership gap:** no one is assigned to monitor the daily run.
5. **Rollback pressure:** the demo works, but the latest data-quality gate failed.

Expected response:

- Pause the launch claim.
- Name the failed check.
- State the owner.
- Use the runbook or launch checklist.
- Decide what ships and what waits.
