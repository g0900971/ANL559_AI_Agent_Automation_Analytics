# Week 3 Exercise Sheet - Limited Retention Budget

## Purpose

Students learn that a model is useful only when it improves a constrained decision and survives leakage checks.

Use this sheet with the Week 3 section of `Weekly_Case_Packs.md`. The case pack gives the fuller decision story, capacity assumptions, feature-availability guide, and solution guidance.

## Materials

- `Starter_Kit/sample_data/week3_retention_training.csv`
- `Starter_Kit/templates/defence_note_template.md`
- `Starter_Kit/templates/leakage_audit_template.md`
- `Portfolio_and_Assessment_Model.md`

## Case Setup For Students

Northstar can contact only a limited number of customers with retention offers. A model score does not answer the business question by itself. The team needs a policy: who gets contacted, why those customers, what it costs, and what the policy should not claim.

The agent may produce a very strong model if it uses information from after the decision. Your job is to catch that failure before the policy is defended.

Use these assumptions unless your instructor changes them:

| Assumption | Value |
|---|---:|
| Offer cost | 25 per customer contacted |
| Expected saved margin | 120 for a truly saved customer |
| Capacity | Contact only 30 percent of customers in the exercise |
| Break-even save rate | 20.8 percent |

For the 12-row sample, a top-3 or top-4 policy can be acceptable if the rounding rule is stated clearly.

## Learning Outcomes

After this exercise, students should be able to:

- Frame a predictive model as a constrained business decision.
- Build and use simple baselines before accepting agent-generated modelling.
- Identify leakage and target columns.
- Tie thresholds or top-N choices to cost, capacity, or expected value.
- Write a decision memo that separates prioritisation from causal proof.

## Studio Flow

| Time | Activity | Concrete output |
|---:|---|---|
| 0-10 | Case briefing | Students state action, stakeholder, and capacity constraint. |
| 10-25 | Exercise 1 | Decision frame. |
| 25-45 | Exercise 2 | Leakage audit. |
| 45-70 | Exercise 3 | Baseline comparison. |
| 70-95 | Exercise 4 | Threshold or top-N rationale. |
| 95-110 | Exercise 5 | One-page decision memo draft. |

## Exercise 1 - Decision Frame

**Time:** 15 minutes

**Student task:** Complete the decision frame before building any model.

| Question | Team answer |
|---|---|
| What action will the business take? |  |
| Who is eligible? |  |
| What is the capacity or budget limit? |  |
| What is the cost of acting? |  |
| What is the value of a successful save? |  |
| What is the simplest baseline? |  |

**Instructor prompt:** "If no action changes, this is not a decision model yet."

**Look for:** Students should write the operational action, not only "predict churn." Example: "Customer Success contacts the top 30 percent of eligible customers with a retention offer."

## Exercise 2 - Leakage Hunt

**Time:** 20 minutes

**Student task:** Inspect every column and label it as allowed, target, leakage, or unclear.

| Column | Allowed at decision time? | Reason |
|---|---|---|
| tenure_months |  |  |
| monthly_fee |  |  |
| usage_sessions_30d |  |  |
| support_tickets_90d |  |  |
| plan_type |  |  |
| discount_last_90d |  |  |
| post_offer_response |  |  |
| retained_next_month |  |  |

**Expected finding:** `retained_next_month` is the target. `post_offer_response` is post-decision information and should not be used as a predictor.

**Instructor checkpoint:** If the model looks unusually strong, ask which column the agent found most predictive. Suspiciously convenient features are often leakage.

## Exercise 3 - Baseline Race

**Time:** 25 minutes

**Student task:** Build two simple baselines before accepting an agent-generated model.

Possible baselines:

- Highest support burden.
- Lowest product usage.
- Month-to-month plan with low usage.
- Highest monthly fee among low-usage customers.

For each baseline, record:

| Baseline | Rule | Who is selected | Why it might work | Why it might fail |
|---|---|---|---|---|
|  |  |  |  |  |

**Expected evidence:** At least two simple policies should be compared before accepting an agent-generated model. The comparison can be numeric or qualitative if coding time is limited, but the rule must be explicit.

## Exercise 4 - Threshold Economics

**Time:** 25 minutes

Use these assumptions:

- Offer cost: 25 per customer.
- Expected saved margin: 120 for a truly saved customer.
- Capacity: contact only 30 percent of customers in this exercise.

**Student task:** Choose a threshold or top-N policy. Explain why it is better than "send to everyone" or "use 0.5 as the default threshold."

Expected-value structure:

```text
Expected value = saved customers * 120 - contacted customers * 25
```

**Acceptance check:** The team should be able to explain why "send to everyone" and "use 0.5" are not automatically valid policies.

## Exercise 5 - Decision Memo Clinic

**Time:** 15 minutes

Draft a one-page memo with this structure:

1. Recommended decision policy.
2. Baseline comparison.
3. Leakage check.
4. Cost or capacity rationale.
5. What should not be claimed yet.

## End-Of-Class Bundle

Teams should submit or save:

- Decision frame.
- Leakage audit.
- Baseline comparison.
- Candidate model, score, or transparent rule.
- Threshold or top-N policy rationale.
- Decision memo.

## Fallback Routes

If students cannot code:

- Use a spreadsheet score based on low usage, support burden, and plan type.
- Compare transparent rules instead of training a model.
- Audit an agent-generated feature list for leakage and write the memo.

If students finish early:

- Compare top-3 and top-4 policies.
- Add a fairness or service-quality slice.
- Draft a pilot measurement plan that would estimate whether offers actually cause retention.

## Instructor Solution Notes

Strong teams do not worship model metrics. They explain the action, capacity, and threshold. They can say which columns were excluded and why.

Common mistakes:

- Using `post_offer_response` because it improves the score.
- Reporting accuracy without comparing to the majority class.
- Letting the agent pick a threshold without business logic.
- Writing a memo that says "the model predicts churn" without saying what action follows.

## Extension Options

- Add fairness or service-quality slices.
- Test whether the policy over-targets high-fee customers.
- Compare model recommendation with a transparent business rule.
