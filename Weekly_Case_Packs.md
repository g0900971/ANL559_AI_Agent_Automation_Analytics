# Weekly Case Packs

This document fills the detail gap between the short mission cards and the classroom exercise sheets. Use it as the practical case-study spine for ANL559 - AI Agents for Analytics Automation.

Each week includes:

- A business case brief students can read before class.
- Data and stakeholder context.
- A guided studio path for Build / Break / Defend.
- Expected evidence and instructor solution guidance.
- Low-code, no-code, and stretch options.

The sample data are intentionally small. The teaching goal is not industrial-scale accuracy; it is to make agent failure, analytics judgement, and operational evidence visible.

## How To Use These Case Packs

For instructors:

1. Read the weekly case pack before the seminar.
2. Use the short "Student brief" as the opening handout or LMS pre-read.
3. Use the "Instructor setup" section to prepare demo artefacts, failure cards, and fallback routes.
4. Use the "Expected evidence" section during peer review and marking.
5. Use the "Solution guidance" section to coach without turning the case into an answer key.

For students:

1. Read the case brief and identify the stakeholder decision.
2. Keep the approved definitions and constraints visible while prompting the agent.
3. Build a first version quickly.
4. Try to break it using the named traps and your own checks.
5. Submit the artefact plus the evidence that proves what can and cannot be trusted.

## Week 1 - Reporting Fire Drill

### Case Snapshot

| Item | Detail |
|---|---|
| Stakeholder | COO |
| Business pressure | The Monday KPI pack is due by 10:00 and the usual analyst is unavailable. |
| Student artefact | Repeatable KPI workflow with metric definitions and smoke tests. |
| Files | `week1_customers.csv`, `week1_sales.csv`, `week1_support.csv`, `week1_metric_definitions.md` |
| Main agent trap | The agent treats "active customer" as recent login instead of paid active account. |
| Defence evidence | Work order, metric contract, checked KPI output, smoke-test result, AI-use log. |

### Student Brief

Northstar Retail sends a weekly KPI pack to the COO. The pack is normally assembled through manual copy-paste from customer, sales, and support files. This week the analyst who owns the process is on leave, and the COO still expects the pack by 10:00.

Your team must use an AI agent to create a repeatable workflow from the starter CSV files. The COO does not need a beautiful dashboard yet. The COO needs numbers that can be rerun, checked, and defended.

The risky phrase is "active customer." Product often uses recent login. The COO means a paid account with active subscription status. If your workflow uses the wrong denominator, the report is not safe to send.

### Approved Business Definitions

| Metric | Approved definition | Expected check in sample data |
|---|---|---:|
| Paid active accounts | `subscription_status = active` and `is_paid = true` | 6 |
| Recent-login customers | `last_login_date` within 30 days of 2026-06-26 | 7 |
| Gross June revenue | Sum `gross_amount` for June 2026 orders | 2860 |
| Net June revenue | Sum `gross_amount - refund_amount` for June 2026 orders | 2660 |
| Open support tickets | Blank `closed_date` | 3 |

The paid-active and recent-login populations differ. For example, a cancelled or past-due customer can still log in, while a paid active customer may not have logged in recently. A reliable workflow should make this difference visible.

### Instructor Setup

Before class:

- Put the four Week 1 files in a shared folder or repo.
- Prepare a weak prompt on a slide: "Make me a KPI report from these CSVs."
- Prepare one flawed agent output or live-demo prompt where the agent defines active customers from `last_login_date`.
- Open `Starter_Kit/templates/work_order_template.md` and `Starter_Kit/templates/metric_definition_template.md`.

Failure cards to release after Sprint A:

- "The COO asks why active customers are 7 when Finance expected 6."
- "A refund was posted in June but the report shows gross revenue."
- "Support asks whether open tickets are based on opened date or unresolved status."

### Studio Path

| Phase | Student action | Instructor coaching |
|---|---|---|
| Build | Write an agent work order naming files, definitions, output format, and acceptance checks. | Ask where the metric owner appears in the work order. |
| Build | Ask the agent to draft a script, notebook, spreadsheet, or report workflow. | Encourage a rough first version; polish is not the objective. |
| Break | Compare the agent's metric definitions with `week1_metric_definitions.md`. | Ask which definition the agent invented or assumed. |
| Break | Run smoke checks for paid active accounts, revenue, and open tickets. | Ask students to make at least one check fail before they fix it. |
| Defend | Write a short note explaining which KPI can be trusted and which assumption was rejected. | Push for evidence-linked language, not "the script works." |

### Expected Evidence

Minimum evidence:

- Agent work order that names the files and approved definitions.
- Metric-definition table with at least three metrics.
- KPI output with the known checks above.
- One AI-use-log entry naming an accepted and rejected agent contribution.
- Defence note: "I trust this KPI pack because..."

Strong evidence:

- A check that would fail if recent login is used as paid active account.
- A notes section listing assumption, owner, and unresolved risk.
- A rerun instruction someone else can follow.

### Solution Guidance

Do not focus on a single implementation style. A spreadsheet, notebook, or Python script can all satisfy the case if the definitions and checks are visible.

Coach toward these insights:

- `C103` and `C106` are recent-login or recently active in product behaviour but are not paid active accounts.
- Gross and net revenue are both valid metrics, but they answer different questions.
- A smoke test should be tied to a known defect. "Paid active accounts should equal 6" is stronger than "the script ran."
- The agent can generate useful code structure, but it cannot own the metric definition.

Low-code route:

- Students compute counts and sums in a spreadsheet.
- They write smoke tests as formulas or a manual validation table.

Stretch route:

- Add a freshness check for each source file.
- Generate a one-page COO summary that cites only checked numbers.
- Add a "stop the send" condition if any check fails.

## Week 2 - The Board Number Is Wrong

### Case Snapshot

| Item | Detail |
|---|---|
| Stakeholder | Finance lead, Product lead, board secretary |
| Business pressure | Two churn numbers are in draft board materials. The board paper needs one trusted number and an explanation. |
| Student artefact | Reconciliation workflow with row-count bridge, quarantine table, and validation gate. |
| Files | `week2_subscriptions.csv`, `week2_cancellations.csv`, `week2_product_events.csv` |
| Main agent trap | The agent inner-joins sources, drops unmatched records, and calls the result clean. |
| Defence evidence | Source profile, join coverage, quarantined records, trusted-number note. |

### Student Brief

Finance and Product disagree about churn. Finance works from billing subscriptions. Product works from product usage. Both views matter, but the board needs a number tied to the decision being made.

Your team must reconcile the sources before choosing a number. The purpose is not to make the data look tidy. The purpose is to explain exactly which records match, which do not, and which definition should be used for the board paper.

The lab data are a small miniature of the business problem. They are not meant to reproduce the illustrative dashboard percentages in the slides. Use the sample rows to demonstrate reconciliation logic.

### Data Context

| Source | Business meaning | Expected profile |
|---|---|---|
| `week2_subscriptions.csv` | Billing scope and subscription status | 10 customer rows |
| `week2_cancellations.csv` | Cancellation requests and billing-end dates | 3 rows |
| `week2_product_events.csv` | Recent product activity | 9 rows |

Intentional defects:

- `C204` appears in subscriptions and cancellations but has no product event.
- `C999` appears in product events but not in subscriptions.
- `C204` has a blank cancellation reason.
- `C207` has a May billing-end date, so it may be outside a June billing churn window.

### Instructor Setup

Before class:

- Prepare a quick demo of an inner join that produces fewer rows than the subscription source.
- Write two competing numbers on the board and ask what evidence would make one trustworthy.
- Open `Starter_Kit/templates/reconciliation_report_template.md`.

Failure cards to release after Sprint A:

- "Your clean table has no unmatched records because the join removed them."
- "Product's denominator includes `C999`, but Finance says this customer is not in billing scope."
- "The cancellation request date and billing-end date imply different month windows."

### Studio Path

| Phase | Student action | Instructor coaching |
|---|---|---|
| Build | Profile each source before joining. | Ask for row count, unique customer count, date fields, and obvious nulls. |
| Build | Ask the agent for join options, then compare inner, left, and full outer approaches. | Ask "what does this join preserve?" before "what number does it produce?" |
| Break | Identify rows lost by inner joins and rows outside billing scope. | Make teams name the disappeared customer IDs. |
| Break | Build a quarantine table for missing usage, product-only records, and blank reasons. | Reinforce that quarantine is evidence, not failure. |
| Defend | Write a trusted-number note naming definition, denominator, and remaining limitation. | Ask whether the board decision is about paying subscriptions or product activity. |

### Expected Evidence

Minimum evidence:

- Source profile table.
- Row-count bridge from source files to final calculation.
- Quarantine table with `C204` and `C999`.
- Validation gate that would prevent silent row loss.
- Board note recommending the number and definition.

Strong evidence:

- Separate billing churn and product-activity diagnostics.
- A check that fails when join coverage falls below a stated threshold.
- A definition-owner note naming Finance and Product responsibilities.

### Solution Guidance

Accepted recommendations can vary if the logic is explicit. For a board paper about paying subscriptions, the subscription file is usually the denominator. Product events are diagnostic evidence, not the billing source of truth.

Coach toward these insights:

- Inner joins can make defects invisible.
- `C204` should not disappear merely because product usage is missing.
- `C999` may be valid product activity, but it is outside billing churn scope until mapped to a subscription.
- The trusted number is only as strong as its definition and denominator.

Low-code route:

- Use spreadsheet lookups to mark matched, missing, and product-only records.
- Build the quarantine table manually from the row comparison.

Stretch route:

- Add a monthly validation checklist.
- Produce a dashboard note showing both billing churn and product inactivity.
- Add an owner and escalation rule for quarantined records.

## Week 3 - Limited Retention Budget

### Case Snapshot

| Item | Detail |
|---|---|
| Stakeholder | Customer Success and Finance |
| Business pressure | The business can contact only a limited share of customers with retention offers. |
| Student artefact | Cost-aware decision policy with baseline comparison, leakage audit, and memo. |
| File | `week3_retention_training.csv` |
| Main agent trap | The agent uses post-decision information and reports a model score instead of a decision policy. |
| Defence evidence | Feature-availability audit, baseline comparison, threshold rationale, decision memo. |

### Student Brief

Northstar wants to reduce churn, but retention offers cost money and Customer Success has limited capacity. A model score is not enough. The business needs a decision rule: who should receive an offer, why those customers, and what evidence says the policy is better than a simple rule.

Your task is to build a first decision policy with an AI agent, then prove that the policy does not use information that would be unavailable at the decision date.

### Decision Context

Use these case assumptions unless your instructor changes them:

| Assumption | Value |
|---|---:|
| Offer cost | 25 per contacted customer |
| Expected saved margin | 120 for a truly saved customer |
| Capacity | Contact only 30 percent of customers in the sample exercise |
| Break-even save rate | 20.8 percent |

For the 12-row sample, teams may choose the top 3 or top 4 customers if they explain their rounding rule. The important assessment point is the policy logic, not a hidden official top-N list.

### Feature Availability Guide

| Column | Expected treatment |
|---|---|
| `tenure_months` | Allowed if known before offer decision. |
| `monthly_fee` | Allowed. |
| `usage_sessions_30d` | Allowed if measured before decision date. |
| `support_tickets_90d` | Allowed if measured before decision date. |
| `plan_type` | Allowed. |
| `discount_last_90d` | Allowed with caution; may reflect prior intervention. |
| `post_offer_response` | Exclude; post-decision information. |
| `retained_next_month` | Target only; never a predictor. |

### Instructor Setup

Before class:

- Prepare a deliberately "too good" agent result that uses `post_offer_response`.
- Open `Starter_Kit/templates/leakage_audit_template.md`.
- Prepare a simple baseline such as "lowest usage" or "highest support burden."

Failure cards to release after Sprint A:

- "Your top feature is `post_offer_response`. Would that exist before the offer is sent?"
- "Accuracy is high because most customers are retained."
- "The agent recommends threshold 0.5, but the team can only contact 30 percent."

### Studio Path

| Phase | Student action | Instructor coaching |
|---|---|---|
| Build | Define the action, eligible population, capacity, cost, and success measure. | Ask what business action changes because of the model. |
| Build | Build two simple baselines before accepting a model. | Ask what the agent must beat. |
| Break | Audit every column for decision-time availability. | Ask "would this be known at the moment of decision?" |
| Break | Re-run or revise the policy after excluding leakage. | Reward lower but honest performance. |
| Defend | Write a decision memo with policy, baseline, leakage check, cost logic, and limits. | Push students to avoid causal claims about offer effectiveness. |

### Expected Evidence

Minimum evidence:

- Decision frame naming action, eligibility, capacity, and cost.
- Leakage audit excluding `post_offer_response` and treating `retained_next_month` as target.
- Baseline comparison.
- Threshold or top-N rationale tied to capacity or expected value.
- One-page decision memo.

Strong evidence:

- Sensitivity check for top 3 versus top 4 customers.
- Plain-language explanation of why accuracy is insufficient.
- Explicit statement that the policy is for prioritisation, not causal proof of retention impact.

### Solution Guidance

Coach toward these insights:

- A model that includes `post_offer_response` has learned from the future.
- A baseline can be simple and still valuable.
- Thresholds are business policies. "0.5" is rarely defensible without capacity or cost logic.
- Break-even logic: 25 / 120 = 20.8 percent. If the contacted group saves less than that, the offer loses value before operational costs.

Low-code route:

- Students create rule-based scores in a spreadsheet.
- They compare two transparent rules rather than training a model.

Stretch route:

- Check whether the policy over-targets one plan type or fee segment.
- Add a fairness or customer-experience note.
- Draft a pilot measurement plan to estimate causal lift.

## Week 4 - From Notebook To Tool

### Case Snapshot

| Item | Detail |
|---|---|
| Stakeholder | Operations manager |
| Business pressure | Operations likes the retention logic but will not run a notebook. |
| Student artefact | Small internal tool with input contract, validation, tests, and runbook. |
| Inputs | Week 3 decision logic plus the request schema in `Sample_Data_and_Scenarios.md` |
| Main agent trap | The agent creates a happy-path demo that crashes or gives nonsense on invalid input. |
| Defence evidence | Valid request, rejected bad requests, test output, runbook entry. |

### Student Brief

Operations wants a small tool they can use during customer review. They do not want to open a notebook, inspect hidden variables, or guess how to format the input. Your job is to turn the Week 3 logic into something bounded and operable.

The tool does not need to be production-grade. It does need to be honest about inputs, outputs, errors, version, and ownership.

### Suggested Input Contract

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

Required rejection rules:

- Missing `customer_id`.
- Negative `tenure_months`.
- Unknown `plan_type`.
- Missing usage or support data.

Suggested output fields:

- `customer_id`
- `recommendation`
- `reason`
- `policy_version`
- `warnings`

### Instructor Setup

Before class:

- Decide whether teams should build a Python function, command-line script, API, dashboard, or spreadsheet tool.
- Prepare one valid request and three invalid requests.
- Open `Starter_Kit/templates/input_contract_template.md` and `Starter_Kit/templates/runbook_template.md`.

Failure cards to release after Sprint A:

- "The tool runs on your laptop but the reviewer cannot start it."
- "A missing `customer_id` produces a recommendation anyway."
- "The output does not state which model or rule version was used."

### Studio Path

| Phase | Student action | Instructor coaching |
|---|---|---|
| Build | Define user, scope, valid request, output, and refusal behaviour. | Ask what the tool should not do. |
| Build | Ask the agent to scaffold the tool and a good-input test. | Encourage the smallest runnable tool. |
| Break | Create invalid requests before adding validation. | Ask students to predict the expected error before implementation. |
| Break | Swap tools and run a handoff test. | Observe whether another team can start and inspect it. |
| Defend | Complete a runbook entry and internal-use defence note. | Ask who owns failures after launch. |

### Expected Evidence

Minimum evidence:

- Input contract.
- One valid request and response.
- At least three rejected bad requests.
- Test or manual check output.
- Runbook with owner, health check, known failure, and rollback.

Strong evidence:

- Clear error messages that tell the user how to fix the request.
- A version field in every output.
- A clean-start instruction tested by a peer team.

### Solution Guidance

Coach toward these insights:

- A tool boundary is a safety feature.
- Error handling is not extra polish; it prevents confident nonsense.
- A reviewer should be able to run the tool without the original author explaining hidden state.
- A runbook should name immediate action, owner, and rollback. "Ask the agent" is not an operational plan.

Low-code route:

- Build a spreadsheet with protected input cells and validation rules.
- Use a manual test table for good and bad requests.

Stretch route:

- Add request logging.
- Add a simple latency or cost field.
- Add a monitoring check for input rejection rate.

## Week 5 - The Executive Question

### Case Snapshot

| Item | Detail |
|---|---|
| Stakeholder | CEO |
| Business pressure | The CEO asks why churn rose, but a fluent causal story could be misleading. |
| Student artefact | Analyst-agent workflow with evaluation cases, citation checks, and refusal behaviour. |
| Files | `week5_knowledge_base.md`, `week5_eval_cases.csv` |
| Main agent trap | The agent claims a price change or campaign caused churn without support. |
| Defence evidence | Evaluation set, source-support table, refusal case, CEO-ready answer. |

### Student Brief

The CEO asks: "Why did churn rise in June?" The agent can produce a confident answer quickly, but the business needs an answer that separates observation from explanation.

Your team must build or simulate an analyst agent that answers only with approved sources, labels uncertainty, and refuses unsupported causal claims.

### Approved Sources

| Source | What it supports | What it does not prove |
|---|---|---|
| Source A - KPI Pack | Churn rose from 9.4 percent to 11.8 percent; increase concentrated among monthly-plan low-usage customers. | The cause of the increase. |
| Source B - Pricing Note | New monthly-plan customers were affected by a May price increase; existing customers were not moved to the new price in June. | That the price change caused June churn. |
| Source C - Support Summary | Onboarding-delay tickets increased in June, especially for April and May signups. | That onboarding delays caused churn without further analysis. |
| Source D - Product Incident Note | Reporting API latency happened on 2026-06-11 and 2026-06-12; billing was not affected. | That the incident caused billing churn. |
| Source E - Marketing Campaign Note | Retention campaign began on 2026-06-24. | That the campaign reduced full-month June churn. |

### Instructor Setup

Before class:

- Decide whether retrieval is manual or implemented in code.
- Prepare one unsafe answer claiming "the May price increase caused churn."
- Open `Starter_Kit/templates/evaluation_case_template.md`.

Failure cards to release after Sprint A:

- "The answer cites Source B but claims existing customers churned because of the new price."
- "The answer says the retention campaign reduced June churn, but the campaign started on 2026-06-24."
- "The answer contains citations, but one cited source does not support the sentence."

### Studio Path

| Phase | Student action | Instructor coaching |
|---|---|---|
| Build | Expand the evaluation set with factual, causal, and out-of-scope questions. | Ask whether each case should answer, hedge, or refuse. |
| Build | Ask the agent to answer using approved sources. | Require source labels or citations for every evidence claim. |
| Break | Mark each cited claim as supported, partially supported, or unsupported. | Make students check the exact sentence, not the general topic. |
| Break | Rewrite unsafe causal claims as uncertainty or refusal. | Reinforce that refusal is a valid analyst behaviour. |
| Defend | Produce a CEO-ready answer with observed pattern, evidence, uncertainty, next test, and refused claim. | Ask what sentence they would remove before sending. |

### Expected Evidence

Minimum evidence:

- At least five evaluation cases, including one refusal case.
- Before-and-after answer for one risky question.
- Citation-support table.
- Final CEO-ready answer.
- Defence note explaining one claim the agent must not make.

Strong evidence:

- Evaluation cases include expected sources and expected refusal logic.
- Unsupported claims are rewritten into testable hypotheses.
- The answer recommends a next analysis rather than pretending the source base proves causality.

### Solution Guidance

Coach toward these insights:

- Source A supports the observed churn pattern.
- Source C supports a plausible investigation path around onboarding friction.
- Source B weakens the claim that the May price increase caused June churn among existing customers.
- Source E is too late to support a full-month June churn reduction claim.
- A safe answer can say "one plausible explanation" only if it clearly labels uncertainty.

Low-code route:

- Students manually retrieve sources from the knowledge base.
- They evaluate the answer using a table rather than building retrieval code.

Stretch route:

- Add an automated answer-quality rubric.
- Compare two prompts on the same evaluation cases.
- Track retrieved source, answer sentence, review decision, and repair action.

## Week 6 - Launch Review

### Case Snapshot

| Item | Detail |
|---|---|
| Stakeholder | Launch committee |
| Business pressure | The committee asks what can go live, what must wait, and who owns the risks. |
| Student artefact | Portfolio evidence pack, launch checklist, incident timeline, and recommendation. |
| Inputs | Weekly artefacts from Weeks 1-5 |
| Main agent trap | The team turns a working demo into an overbroad launch claim. |
| Defence evidence | Evidence map, incident response, no-ship conditions, owner and rollback. |

### Student Brief

The final session is not a feature tour. The launch committee wants to know whether the automation is safe to use, in what scope, with which owners, and under what stop conditions.

Your team must defend a ship, limited-pilot, or no-ship recommendation using portfolio evidence. A limited pilot or no-ship recommendation can be excellent if it is evidence-based.

### Launch Decision Options

| Recommendation | When it is appropriate |
|---|---|
| Full launch | Every critical claim has evidence, owner, monitoring, and rollback. |
| Limited pilot | The system works in a controlled scope but has unresolved scale, impact, monitoring, or ownership risk. |
| No ship | Critical evidence is missing or incident response is not credible. |

For most student teams, a limited pilot is often the most defensible recommendation because the sample data and class setting cannot prove full production readiness.

### Instructor Setup

Before class:

- Ask teams to bring weekly artefacts, AI-use logs, and defence notes.
- Prepare a timer for five-minute demos.
- Prepare incident inject cards from the list below.
- Open `Starter_Kit/templates/evidence_map_template.md` and `Starter_Kit/templates/launch_checklist_template.md`.

Incident injects:

- Metric drift: active customer count differs from expected range.
- Bad input: an operations user sends a request with missing fields.
- Unsupported executive claim: a stakeholder asks the team to state that a campaign caused churn reduction.
- Ownership gap: no one is assigned to monitor the daily run.
- Rollback pressure: the demo works, but the latest data-quality gate failed.

### Studio Path

| Phase | Student action | Instructor coaching |
|---|---|---|
| Build | Map each launch claim to evidence, limitation, and owner. | Ask what each evidence item proves and does not prove. |
| Build | Complete launch checklist and no-ship conditions. | Push for concrete stop conditions. |
| Break | Respond to one incident inject during the demo. | Ask what pauses, who owns it, and what is communicated. |
| Break | Peer listener asks a viva question about the weakest claim. | Reward honest limits. |
| Defend | Write final recommendation: ship, limited pilot, or no ship. | Make them state what should not ship yet. |

### Expected Evidence

Minimum evidence:

- Evidence map across Weeks 1-5.
- Launch checklist with scope, owners, monitoring, rollback, and no-ship conditions.
- Incident timeline or response note.
- Final recommendation with strongest evidence and residual risk.
- Individual defence responses.

Strong evidence:

- Each claim has "what this proves" and "what this does not prove."
- Incident response pauses or narrows launch rather than improvising.
- The recommendation has a named owner for every unresolved risk.

### Solution Guidance

Coach toward these insights:

- A launch recommendation is a decision under uncertainty, not a celebration of work completed.
- "Limited pilot" is often stronger than a vague full launch.
- The agent should not be named as an operational owner.
- A failed gate should pause the relevant scope until evidence is restored.
- Stakeholder pressure to overclaim should be refused with evidence and a next action.

Low-code route:

- Students present screenshots, spreadsheets, and manual evidence tables.
- Incident response is written as a timeline rather than automated.

Stretch route:

- Run a cross-team red-team review.
- Draft a post-launch monitoring dashboard.
- Record a two-minute executive launch recommendation.

