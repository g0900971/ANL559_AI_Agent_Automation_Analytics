# Week 1 Exercise Sheet - Reporting Fire Drill

## Purpose

Students learn that an AI-generated report is not trustworthy until the metric definitions, source files, checks, and rejected agent assumptions are visible.

Use this sheet with the Week 1 section of `Weekly_Case_Packs.md`. The case pack provides the fuller stakeholder story, intentional traps, and solution guidance.

## Materials

- `Starter_Kit/sample_data/week1_customers.csv`
- `Starter_Kit/sample_data/week1_sales.csv`
- `Starter_Kit/sample_data/week1_support.csv`
- `Starter_Kit/sample_data/week1_metric_definitions.md`
- `Starter_Kit/templates/work_order_template.md`
- `Starter_Kit/templates/ai_use_log_template.md`
- `Starter_Kit/templates/defence_note_template.md`

## Case Setup For Students

Northstar Retail's COO needs the weekly KPI pack by 10:00. The usual analyst is away, and last week's pack was created manually from CSV files. Your team must create a repeatable workflow that another analyst could rerun.

The main risk is the phrase "active customer." Product often means recent login. The COO means paid account with active subscription status. If the agent chooses the wrong definition, the report can look polished and still be wrong.

By the end of class, each team should be able to show:

- A work order that controlled the agent's task.
- The metric definitions used by the workflow.
- KPI output checked against known sample totals.
- One rejected or corrected agent assumption.
- A short defence of what can be trusted.

## Learning Outcomes

After this exercise, students should be able to:

- Convert a vague reporting request into an agent work order.
- Treat metric definitions as acceptance criteria.
- Design smoke tests that catch plausible agent errors.
- Explain why one agent output was accepted, rejected, or modified.

## Studio Flow

| Time | Activity | Concrete output |
|---:|---|---|
| 0-10 | Case briefing and file orientation | Students identify stakeholder, deadline, files, and risk phrase. |
| 10-25 | Exercise 1 | Metric contract table. |
| 25-40 | Exercise 2 | Revised agent work order. |
| 40-65 | Exercise 3 | Smoke checks and first KPI output. |
| 65-80 | Exercise 4 | AI-use-log entry. |
| 80-90 | Exercise 5 | 60-second defence. |

If running the full three-hour seminar, use this sheet as the guided core inside the longer Build / Break / Defend schedule from `Complete_Instructor_Guide.md`.

## Exercise 1 - Metric Contract Clinic

**Time:** 15 minutes

**Student task:** In pairs, list the metrics the COO probably expects in the Monday KPI pack. For each metric, write the definition, source file, formula, and one possible ambiguity.

Suggested table:

| Metric | Approved definition | Source | Formula | Possible ambiguity |
|---|---|---|---|---|
| Paid active accounts |  |  |  |  |
| Net June revenue |  |  |  |  |
| Open support tickets |  |  |  |  |

**Instructor prompt:** "If the agent used a different definition, how would you know before the COO sees the report?"

**Expected evidence:** A metric-definition table with at least one ambiguity clearly named.

**Look for:** Students should name who owns the definition, not only the formula. For example, paid active accounts is a COO or Finance definition, while recent login is a Product diagnostic.

## Exercise 2 - Rewrite the Weak Prompt

**Time:** 15 minutes

**Weak prompt:**

> Make me a KPI report from these CSVs.

**Student task:** Rewrite the prompt as an agent work order. It must include goal, inputs, acceptance criteria, and constraints.

**Minimum requirements:**

- Name all source files.
- State that the agent must not invent metric definitions.
- Require at least three smoke tests.
- Require a short explanation of any assumptions.

**Instructor note:** Push students to specify output format. A vague "make a report" prompt often produces a polished but uncheckable artefact.

**Acceptance check:** The revised prompt should be specific enough that a peer can predict the file names, metrics, and tests before the agent answers.

## Exercise 3 - Smoke-Test Hunt

**Time:** 25 minutes

**Student task:** Use the sample files to create at least three checks that would catch obvious errors.

Known checks:

- Paid active accounts should be 6.
- Recent-login customers should be 7.
- Gross June revenue should be 2860.
- Net June revenue should be 2660.
- Open support tickets should be 3.

**Challenge:** Write one check that would fail if the agent used recent-login customers instead of paid active accounts.

**Expected evidence:** A script, notebook, spreadsheet, or plain-language check list showing input, formula, expected value, and actual value.

**Instructor checkpoint:** Ask teams to explain the defect each smoke test is designed to catch. A check without a defect story is usually too generic.

## Exercise 4 - Agent Failure Log

**Time:** 15 minutes

**Student task:** Ask the agent to draft the KPI workflow. Identify one suggestion you would reject or modify.

Log it using:

| Agent suggestion | Risk | Evidence used | Team decision |
|---|---|---|---|
|  |  |  |  |

**Instructor prompt:** "The best log entry is not the longest. It is the entry that shows judgement."

Good entries name a concrete agent contribution:

- Accepted: file-loading structure, grouping logic, output format.
- Rejected: invented active-customer definition, gross/net confusion, unsupported executive summary.
- Modified: test names, assumption notes, error handling.

## Exercise 5 - Defence Rehearsal

**Time:** 10 minutes

Each pair gives a 60-second defence:

1. What number do you trust?
2. What did the agent get wrong or almost get wrong?
3. Which check would catch the problem next time?

Listeners ask one question: "What would still make this report unsafe?"

## End-Of-Class Bundle

Teams should submit or save:

- `work_order.md`
- Metric-definition table.
- KPI workflow artefact: script, notebook, spreadsheet, or documented manual workflow.
- Smoke-test evidence with expected and actual values.
- One AI-use-log entry.
- Defence note beginning: "I trust this KPI pack because..."

## Fallback Routes

If students cannot run code:

- Use spreadsheet formulas for the three CSV files.
- Write smoke tests as a validation table.
- Ask the agent to explain the calculation logic, then audit the explanation against the metric definitions.

If students finish early:

- Add a data-freshness check.
- Add a stop condition if any metric check fails.
- Generate a COO summary that cites only checked values.

## Instructor Solution Notes

Strong teams usually separate paid active accounts from recent login customers. If a team reports only one "active" number, ask who owns the definition and whether a logged-in cancelled customer should count.

Common mistakes:

- Treating the sample metric definitions as optional reading.
- Reporting gross revenue when the stakeholder expects net revenue.
- Writing tests after seeing the answer without explaining what defect the test prevents.
- Logging "AI helped with code" instead of a specific accepted or rejected output.

## Extension Options

- Add a generated executive summary that cites only checked numbers.
- Create a scheduled-run checklist.
- Add a "data freshness" check: no source file should be older than the reporting date.
