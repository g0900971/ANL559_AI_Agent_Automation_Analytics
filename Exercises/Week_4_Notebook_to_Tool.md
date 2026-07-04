# Week 4 Exercise Sheet - From Notebook to Tool

## Purpose

Students learn how to turn an analysis into an internal analytics product with explicit inputs, outputs, error handling, tests, and operating notes.

Use this sheet with the Week 4 section of `Weekly_Case_Packs.md`. The case pack gives the fuller operations story, suggested request schema, expected output fields, and solution guidance.

## Materials

- Week 3 decision rule or model output.
- Week 4 request schema in `Sample_Data_and_Scenarios.md`.
- `Starter_Kit/templates/input_contract_template.md`
- `Starter_Kit/templates/runbook_template.md`
- `Starter_Kit/templates/peer_demo_review_template.md`

## Case Setup For Students

Operations likes the retention decision logic, but they will not run a notebook. They need a small internal tool that accepts a clearly defined request, returns a consistent recommendation, and refuses bad input.

Your tool can be a Python function, command-line script, small API, dashboard, or spreadsheet with validation rules. The implementation choice matters less than the boundary: what the tool accepts, what it returns, what it refuses, and who operates it.

Suggested valid request:

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

Suggested output fields:

- `customer_id`
- `recommendation`
- `reason`
- `policy_version`
- `warnings`

## Learning Outcomes

After this exercise, students should be able to:

- Define an analytics tool boundary.
- Write an input contract with required fields and rejection rules.
- Use the agent to add validation and tests, not only a happy-path demo.
- Conduct a peer handoff test.
- Write a runbook that names owner, health check, failure mode, and rollback.

## Studio Flow

| Time | Activity | Concrete output |
|---:|---|---|
| 0-10 | Case briefing and tool choice | Teams choose function, CLI, API, dashboard, or spreadsheet. |
| 10-25 | Exercise 1 | Product boundary table. |
| 25-45 | Exercise 2 | Input contract. |
| 45-70 | Exercise 3 | Bad-input tests and validation. |
| 70-90 | Exercise 4 | Peer handoff review. |
| 90-105 | Exercise 5 | Runbook entry. |

## Exercise 1 - Product Boundary

**Time:** 15 minutes

**Student task:** Define what the tool does and does not do.

| Boundary question | Team answer |
|---|---|
| Who is the user? |  |
| What input do they provide? |  |
| What output do they receive? |  |
| What should the tool refuse? |  |
| What is outside scope? |  |

**Instructor prompt:** "A tool boundary protects both the user and the analytics team."

**Look for:** Students should name at least one thing the tool must refuse. A tool with no refusal behaviour is usually just a demo.

## Exercise 2 - Input Contract

**Time:** 20 minutes

Use this suggested request:

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

**Student task:** Define required fields, types, allowed values, and rejection rules.

Minimum rejection rules:

- Missing `customer_id`.
- Negative `tenure_months`.
- Unknown `plan_type`.
- Missing usage or support data.

**Expected evidence:** A contract table that includes field type, allowed values, whether the field is required, and the exact error expected when invalid.

## Exercise 3 - Bad-Input Lab

**Time:** 25 minutes

**Student task:** Create three invalid requests and decide the expected response before implementing anything.

| Bad request | Expected response | Why this matters |
|---|---|---|
| Missing customer ID |  |  |
| Negative tenure |  |  |
| Unknown plan type |  |  |

Then ask the agent to add the validation logic and tests.

**Instructor checkpoint:** Require students to write expected responses before implementation. This prevents the agent from defining the acceptance standard after the fact.

## Exercise 4 - Handoff Test

**Time:** 20 minutes

Swap tools with another team. The receiving team must run the tool using only the README, runbook, or instructions provided.

Reviewer questions:

- Could you start it without asking the original team?
- Did the good request work?
- Did the bad request fail clearly?
- Was the output understandable?

**Expected evidence:** The receiving team should record one pass, one confusion, and one improvement request using `peer_demo_review_template.md`.

## Exercise 5 - Runbook Drill

**Time:** 15 minutes

Complete the runbook sections:

- Purpose.
- Owner.
- Start procedure.
- Health checks.
- Known failure modes.
- Rollback procedure.

## End-Of-Class Bundle

Teams should submit or save:

- Tool artefact or validated spreadsheet.
- Input contract.
- Good-input result.
- Bad-input rejection evidence.
- Test or manual check output.
- Peer handoff note.
- Runbook entry.

## Fallback Routes

If students cannot build an app:

- Create a spreadsheet tool with protected input cells and validation rules.
- Write the request validator as pseudocode and test table.
- Audit an agent-generated app design for missing input contracts.

If students finish early:

- Add version to every output.
- Add request logging.
- Add a lightweight monitoring check for rejection rate or failed requests.

## Instructor Solution Notes

Strong teams make failure boring. Bad input should produce a controlled rejection, not a crash or a confident nonsense answer.

Common mistakes:

- Shipping a notebook with hidden state.
- Accepting any JSON because the happy path works.
- Writing "contact IT" as the only recovery step.
- Failing to record which model, rule, or data version the tool used.

## Extension Options

- Add request logging.
- Add a simple latency or cost estimate.
- Add a version field to every output.
