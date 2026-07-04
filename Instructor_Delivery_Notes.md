# Instructor Delivery Notes

These notes make the Studio Refresh package teachable without relying on the older ANL559 materials. They define the course assumptions, weekly context, instructor preparation, delivery prompts, expected outputs, and fallback options.

For the full teaching manual, read `Complete_Instructor_Guide.md` first. Use this file as the shorter week-by-week reference once you understand the course design.

## Course Identity

**Course name:** ANL559 - AI Agents for Analytics Automation

**Teaching premise:** Students learn to supervise AI agents as practical analytics workers. Each seminar starts from a realistic business problem, uses an AI agent to build a first version, then requires students to expose defects and defend what remains with evidence.

**Repeated habit:** Build quickly, break deliberately, defend with evidence.

## Target Learners

The course is designed for analytics, business, information systems, or operations students who can read basic data tables and follow simple Python or SQL workflows. It does not assume advanced machine learning expertise.

Expected baseline:

- Basic spreadsheet and data literacy.
- Ability to read simple Python or SQL, even if not fluent.
- Familiarity with business metrics such as churn, revenue, active customers, and conversion.
- Willingness to use an AI agent, inspect its output, and explain what was accepted or rejected.

If some students have weaker coding confidence, use the Driver / Reviewer / Reporter roles from `Facilitation_Guide.md`. A student can still meet the learning objective by reviewing diffs, writing tests, checking evidence, or preparing the defence note.

## Minimum Tool Setup

The package is tool-agnostic. The course can be delivered with any AI coding agent or chat-based assistant that can help draft code, tests, analysis notes, or documentation.

Recommended classroom setup:

- Python 3.10 or later.
- `pandas`, `pytest`, and `jupyter` or another notebook environment.
- Git or a shared folder where teams can save versions.
- One AI agent surface per team.
- The `Starter_Kit/` folder from this package.
- A projector view where the instructor can show the defect wall and live demo.

If students will run Python locally, distribute `Student_Local_Python_Setup.md` before Week 1 and ask them to run:

```powershell
python scripts\check_python_setup.py
python Starter_Kit\examples\week1_kpi_smoke_checks.py
```

Collecting the output before class prevents setup problems from consuming the first studio sprint.

Low-tech fallback:

- Students can use spreadsheet formulas instead of Python for Weeks 1-2.
- Students can audit a provided agent transcript instead of running an agent.
- Students can write acceptance tests as plain-language checks when code execution fails.

## Course-Level Learning Outcomes

By the end of the course, students should be able to:

1. Scope an analytics automation task as a clear agent work order.
2. Use an AI agent to create a first working artefact.
3. Detect common agent failures: invented definitions, hidden data loss, leakage, unsupported claims, and fragile deployment assumptions.
4. Add evidence through tests, reconciliation checks, evaluation cases, runbooks, and logs.
5. Explain what is trusted, what is rejected, and what still should not be shipped.
6. Defend an analytics automation system under stakeholder questioning.

## How To Use The Expanded Materials

Each seminar now has four levels of support:

1. **Slide deck:** use this for the live teaching flow.
2. **Weekly case pack:** use `Weekly_Case_Packs.md` for the detailed stakeholder story, data context, failure cards, expected evidence, and solution guidance.
3. **Exercise sheet:** use the matching file in `Exercises/` for timed classroom activities and instructor solution notes.
4. **Worked example:** show one example from `Worked_Examples.md` or `Starter_Kit/examples/` before students build.
5. **Template:** give students the relevant template from `Starter_Kit/templates/` so they know what evidence to submit.

Suggested pattern:

- Before class, read the weekly case pack and choose which failure cards to release.
- Before Sprint A, show one worked example for two minutes.
- During Sprint A, let students build with the template open.
- During the break moment, use the exercise sheet's instructor notes to target likely misconceptions.
- During peer demo, ask students to compare their evidence against the worked example.

Do not use the worked examples as answer keys too early. They are best used as models of evidence structure, not as completed solutions to copy.

## Week 1 - Reporting Fire Drill

### Teaching Purpose

Students learn that automation is not a polished output. Automation is the repeatable path from raw data to a checked business number.

### Before Class

- Place the Week 1 sample files from `Starter_Kit/sample_data/` in a shared repo or folder.
- Prepare a deliberately ambiguous metric definition: "active customer".
- Prepare a flawed agent-generated reporting script or demonstrate how quickly an agent may invent a denominator.
- Put the work-order template on the screen.

### Cold Open Prompt

"It is Monday morning. The COO wants the KPI pack by 10:00. The analyst who built last week's version is on leave. What must be true for this report to be safe to send?"

Expected student answers:

- The definitions are known.
- The source files are named and available.
- The script can be rerun.
- The output can be checked against known totals.
- Someone knows what changed from last week.

### Concept Details

**Agent as junior analyst:** The agent can draft code quickly, but it does not own the metric. The human must provide definitions and acceptance criteria.

**Metric definition as contract:** If churn, active customers, or revenue are not defined, the agent will use a plausible definition. Plausible is not the same as approved.

**Smoke test:** A small check that catches obvious wrongness. Example: total paid customers should equal 6 in the sample file; net revenue should equal sales minus refunds.

### Studio Guidance

During Sprint A, let teams produce an imperfect first script. Do not rescue them too early. Ask:

- "Where is the metric definition written?"
- "What known total would catch a wrong denominator?"
- "Which agent output did you not trust?"

During the break moment, give this defect:

"The agent defines active customer as any login in the last 30 days. The COO means paid account with active subscription status."

### Expected End-of-Class Output

- `work_order.md`
- `metric_definitions.md`
- A reporting script, notebook, or spreadsheet.
- At least three smoke checks.
- One AI-use-log entry.
- A defence note beginning: "I trust this KPI pack because..."

### Minimum Acceptable Evidence

Students must show one metric definition, one check that can fail, and one correction to an agent-generated suggestion.

## Week 2 - The Board Number Is Wrong

### Teaching Purpose

Students learn that a trusted number needs a row-count story. AI agents are useful for joins and profiling, but they often choose joins that hide missing records.

### Before Class

- Provide `week2_subscriptions.csv`, `week2_cancellations.csv`, and `week2_product_events.csv`.
- Prepare a live example of an inner join that produces a clean-looking but incomplete table.
- Write the two competing churn numbers on the board: Finance 11.8 percent, Product 9.4 percent.

### Cold Open Prompt

"Two dashboards are already in the board pack. They disagree. What would make you comfortable replacing both numbers with one trusted number?"

Expected student answers:

- Source counts are shown.
- Lost records are explained.
- Definitions are compared.
- The join logic is visible.
- Unmatched rows are quarantined.

### Concept Details

**Source counts:** Count rows before transformation so data loss has a baseline.

**Join coverage:** Report how many records matched and how many did not.

**Quarantine table:** A table for records that should not be silently dropped.

**Business definition:** The real issue is often not just bad data. It may be that Finance and Product define churn differently.

### Studio Guidance

Ask students to make the agent produce a reconciliation report, not just a cleaned dataset.

Key coaching questions:

- "Which rows disappeared?"
- "Who owns the definition of churn?"
- "What would trigger an alert next month?"

### Expected End-of-Class Output

- Row-count bridge from source files to final churn calculation.
- Quarantine table for unmatched or ambiguous records.
- Churn definition note.
- Validation tests or plain-language quality checks.
- Defence note: "The number I would put in the board paper is..."

### Minimum Acceptable Evidence

Students must show source counts before and after joins, plus at least one quarantined record.

## Week 3 - Limited Retention Budget

### Teaching Purpose

Students learn that model quality is not the same as decision quality. A model only matters if it improves a constrained decision.

### Before Class

- Provide `week3_retention_training.csv`.
- Identify the leakage column in advance.
- Prepare simple cost assumptions: offer cost, expected saved margin, capacity limit.
- Prepare a simple baseline such as "target customers with highest past complaints" or "target longest-tenure at-risk customers".

### Cold Open Prompt

"The business can afford 8,000 offers, not 80,000. A model with a good score still needs to answer: who receives the next offer?"

Expected student answers:

- We need a ranking or threshold.
- We need cost and benefit assumptions.
- We need to compare with a simple rule.
- We need to check whether the model cheated.

### Concept Details

**Baseline:** A simple rule that the model must beat. Without a baseline, a model score has no business meaning.

**Leakage:** A feature that would not be known at decision time. In the sample file, columns such as `post_offer_response` or `retained_next_month` should not be used as predictors.

**Threshold:** A policy choice, not a default setting. It depends on budget, capacity, and expected value.

### Studio Guidance

If students focus only on AUC or accuracy, redirect them:

- "What action changes because of this model?"
- "What happens if we can only contact 10 percent of customers?"
- "Which columns would not exist at the decision date?"

### Expected End-of-Class Output

- Baseline comparison table.
- Leakage audit.
- Candidate model or scoring rule.
- Threshold rationale.
- One-page decision memo.

### Minimum Acceptable Evidence

Students must identify at least one forbidden feature and state a decision policy tied to cost or capacity.

## Week 4 - From Notebook to Tool

### Teaching Purpose

Students learn that an analysis becomes operational only when it has a boundary: inputs, outputs, errors, tests, and ownership.

### Before Class

- Choose whether the class will build a small API, command-line tool, or lightweight dashboard.
- Provide the request schema from `Sample_Data_and_Scenarios.md`.
- Prepare one valid request and two invalid requests.
- Prepare a minimal runbook example.

### Cold Open Prompt

"Operations likes the model but will not run a notebook. What has to change before this becomes a tool?"

Expected student answers:

- Clear inputs and outputs.
- Bad input handling.
- Repeatable startup.
- Tests.
- Instructions for support and rollback.

### Concept Details

**Input contract:** The tool should reject missing, malformed, or out-of-scope input before producing an answer.

**CI or test gate:** A tool should have a check that can run without the original author.

**Runbook:** A practical operating note: how to start, stop, test, recover, and escalate.

### Studio Guidance

Do not let students hide a notebook behind a button. Ask:

- "Can a different person run it?"
- "What error message does a bad input receive?"
- "Where is the rollback step?"

### Expected End-of-Class Output

- API, dashboard, command-line tool, or spreadsheet tool with a fixed input contract.
- Good-input and bad-input examples.
- Test output.
- Runbook entry.
- Defence note: "This tool is ready for internal use if..."

### Minimum Acceptable Evidence

Students must show one successful request and one rejected bad request.

## Week 5 - The Executive Question

### Teaching Purpose

Students learn that an analyst agent should answer with evidence, uncertainty, and refusal behaviour. A fluent answer is not automatically analysis.

### Before Class

- Provide `week5_knowledge_base.md` and `week5_eval_cases.csv`.
- Prepare one question with a supported answer and one question that should be refused.
- Decide whether students will implement retrieval in code or simulate retrieval manually.

### Cold Open Prompt

"The CEO asks, 'Why did churn rise this month?' What would make an answer safe enough to send?"

Expected student answers:

- It cites supporting evidence.
- It separates observation from explanation.
- It labels uncertainty.
- It refuses claims outside the evidence.
- It suggests a next test.

### Concept Details

**Grounded answer:** An answer linked to sources that actually support the claim.

**Unsupported causal claim:** A statement that says X caused Y when the data only shows correlation or timing.

**Evaluation case:** A test question with expected behaviour. It can check factuality, citation support, uncertainty, and refusal.

### Studio Guidance

Push students to test uncomfortable questions, not only easy ones:

- "Where does the source support that sentence?"
- "What should the agent refuse?"
- "What would you send to the CEO, and what would you hold back?"

### Expected End-of-Class Output

- Five evaluation questions.
- Before-and-after answer.
- Citation or source-support check.
- Refusal case.
- Defence note: "The answer I would send to the CEO is safe because..."

### Minimum Acceptable Evidence

Students must show at least one unsupported claim caught by an evaluation case.

## Week 6 - Launch Review

### Teaching Purpose

Students learn to make a launch decision from evidence. The final seminar should feel like an operational review, not a feature tour.

### Before Class

- Ask teams to bring their weekly artefacts and defence notes.
- Prepare incident injects: drift alert, bad input, stakeholder pressure to overclaim.
- Prepare a five-minute demo timer.
- Prepare the viva prompts from `Portfolio_and_Assessment_Model.md`.

### Cold Open Prompt

"The launch committee asks: Can this system go live, and who owns it if something goes wrong?"

Expected student answers:

- It can ship only within tested scope.
- Risks and owners must be named.
- There must be a rollback path.
- Evidence must be linked, not merely claimed.

### Concept Details

**Launch checklist:** A decision tool that records scope, evidence, owners, known risks, and no-ship conditions.

**Incident drill:** A pressure test of whether the team can respond using evidence instead of improvising.

**Portfolio defence:** Proof that students understand the work they produced with the agent.

### Studio Guidance

During demo, interrupt politely with one incident inject. Ask:

- "What do you stop?"
- "Who owns the next action?"
- "Which evidence supports that decision?"
- "What should not be shipped yet?"

### Expected End-of-Class Output

- Evidence map.
- Launch checklist.
- Incident timeline.
- Final defence script.
- Ship / no-ship recommendation.

### Minimum Acceptable Evidence

Students must state what ships, what does not ship, the owner of the next action, and the evidence behind the decision.

## Instructor Quality Checks

At the end of each seminar, check whether the session produced all three learning moves:

- **Build:** Students created or improved a concrete artefact.
- **Break:** Students found a real or plausible failure.
- **Defend:** Students wrote an evidence-linked claim with limits.

If one of these is missing, the class may have been active but not fully educational. Use the next seminar's retrieval link to recover the missing move.
