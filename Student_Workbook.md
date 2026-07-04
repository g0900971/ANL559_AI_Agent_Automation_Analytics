# Student Workbook

This workbook is the student-facing companion for the Studio Refresh version of ANL559. It explains the course rhythm, weekly missions, expected evidence, and templates students should use in their portfolio.

## How This Course Works

Each week you work like an analytics automation team. You receive a business mission, use an AI agent to build a first version, test or challenge the result, then defend what can be trusted.

The weekly rhythm is:

1. **Build:** create a useful first version with the agent.
2. **Break:** find where the agent, data, prompt, model, or workflow fails.
3. **Defend:** explain what you trust, what you reject, and what still needs work.

You are not assessed on whether the agent gives a perfect answer. You are assessed on whether you supervised the agent into producing reliable analytics work.

## What To Bring Each Week

- A laptop with the agreed class tools.
- If your instructor requires local Python: a completed setup from `Student_Local_Python_Setup.md`.
- Access to the team repo or shared folder.
- The weekly mission card.
- The starter data or scenario files.
- Your AI-use log.
- Your previous defence note.

## How To Use The Course Files

Use these files every week:

- `Mission_Cards.md` tells you the practical mission.
- `Weekly_Case_Packs.md` gives the fuller case story, stakeholder pressure, data context, known traps, and evidence expectations.
- `Student_Workbook.md` explains what to build, break, and submit.
- `Student_Local_Python_Setup.md` helps you prepare local Python, a virtual environment, packages, and setup checks.
- `Exercises/Week_*.md` gives the detailed classroom activities.
- `Prompt_Guidelines_and_Library.md` helps you write better agent instructions.
- `Worked_Examples.md` shows what strong evidence looks like.
- `Starter_Kit/templates/` gives reusable formats for portfolio evidence.

Do not treat the worked examples as scripts to copy. Use them to understand the level of specificity expected in your own evidence.

## How To Work Through A Weekly Case

Before using the agent, pause long enough to answer five questions:

1. Who is the stakeholder?
2. What decision, workflow, or risk does the artefact support?
3. Which definitions or constraints must the agent not invent?
4. What failure would make the output unsafe?
5. What evidence would convince a reviewer that the final claim is scoped correctly?

During the case, keep a small evidence table:

| Claim we want to make | Evidence we have | What could still be wrong |
|---|---|---|
|  |  |  |

This table will make your defence note much easier to write.

## Portfolio Evidence

Your portfolio should contain one bundle per week. Each bundle should answer four questions:

1. What did we build?
2. What failed?
3. What did we change?
4. What evidence supports the final claim?

## AI-Use Rule

You may use an AI agent for drafting, coding, testing, summarising, and debugging. You must not submit agent output that you cannot explain.

For every important agent contribution, log:

- The task you gave the agent.
- The output you accepted.
- The output you rejected or changed.
- The evidence you used to decide.

Use `Starter_Kit/templates/ai_use_log_template.md`.

## Good Evidence Versus Weak Evidence

| Weak evidence | Strong evidence |
|---|---|
| "The agent wrote the script." | "The agent drafted the file-loading structure. We rejected its active-customer calculation because it used recent login instead of paid subscription." |
| "The data was cleaned." | "The row-count bridge shows one subscription customer without product events and one product event outside billing scope." |
| "The model performed well." | "The model was compared with two baselines, leakage columns were excluded, and the threshold was tied to capacity." |
| "The tool works." | "The valid request returns a recommendation, while missing `customer_id` and negative tenure are rejected with clear errors." |
| "The answer has citations." | "Each cited sentence was checked against the source; unsupported causal claims were refused." |

## Week 1 - Reporting Fire Drill

### Situation

The weekly KPI pack is late again. The team needs a repeatable reporting workflow, not another manual copy-paste exercise.

### Your Goal

Create a workflow that turns raw files into a checked KPI output.

### Key Ideas

- The agent is a junior analyst, not the metric owner.
- A metric definition is a contract.
- A smoke test catches obvious wrongness before stakeholders see the result.

### Build Checklist

- Write a work order for the agent.
- Define the key metrics.
- Ask the agent to draft the reporting workflow.
- Run the workflow on the starter data.
- Add at least three smoke checks.

### Break Checklist

- Look for invented metric definitions.
- Check whether the denominator changed.
- Compare output against known totals.

### Submit

- Work order.
- Metric definitions.
- Script, notebook, or spreadsheet.
- Smoke-test output.
- AI-use-log entry.
- Defence note: "I trust this KPI pack because..."

## Week 2 - The Board Number Is Wrong

### Situation

Finance and Product report different churn numbers. Both are in draft board materials.

### Your Goal

Reconcile the number and build a gate that reduces the chance of the same error recurring.

### Key Ideas

- A trusted number needs a row-count story.
- Joins can hide missing records.
- Quarantine tables are better than silent deletion.

### Build Checklist

- Profile each source file.
- Count rows before transformation.
- Join the sources.
- Report matched, unmatched, and ambiguous records.
- Document the churn definition.

### Break Checklist

- Check whether an inner join removed valid customers.
- Check whether dates use different business meanings.
- Check how nulls were handled.

### Submit

- Reconciliation report.
- Row-count bridge.
- Quarantine table.
- Validation checks.
- Trusted-number note.

## Week 3 - Limited Retention Budget

### Situation

The business can afford only a limited number of retention offers.

### Your Goal

Build a decision model or scoring rule that helps choose who receives an offer.

### Key Ideas

- A high model score is not a decision.
- A model must beat a simple baseline.
- Leakage makes a model look better than it is.
- A threshold is a business policy.

### Build Checklist

- Define the action and capacity limit.
- Create at least one simple baseline.
- Ask the agent to build a candidate model or scoring rule.
- Check for leakage.
- Choose a threshold using cost, capacity, or expected value.

### Break Checklist

- Remove any feature that would not exist at decision time.
- Compare with a simple rule.
- Check whether class imbalance makes accuracy misleading.

### Submit

- Baseline comparison.
- Leakage audit.
- Threshold rationale.
- Decision memo.

## Week 4 - From Notebook to Tool

### Situation

Operations likes the analysis but will not run a notebook.

### Your Goal

Turn the analysis into a small internal tool with clear inputs, outputs, tests, and operating notes.

### Key Ideas

- A notebook is a thinking space; a tool is an operating surface.
- Input contracts protect users from bad outputs.
- A runbook helps someone else operate the system.

### Build Checklist

- Define the input contract.
- Create a valid request and invalid requests.
- Ask the agent to scaffold an API, command-line tool, dashboard, or spreadsheet tool.
- Add tests or checks.
- Write a runbook entry.

### Break Checklist

- Send malformed input.
- Remove a required field.
- Try a value outside the expected range.
- Start the tool from a clean environment.

### Submit

- Tool artefact.
- Input contract.
- Good-input and bad-input evidence.
- Test output.
- Runbook entry.

## Week 5 - The Executive Question

### Situation

The CEO asks why churn changed. A fluent answer is not enough.

### Your Goal

Build or simulate an analyst agent that answers with evidence, uncertainty, and appropriate refusals.

### Key Ideas

- A grounded answer cites evidence that actually supports the claim.
- Correlation is not causation.
- An analyst agent must know when not to answer.
- Evaluation cases test behaviour before deployment.

### Build Checklist

- Write five evaluation questions.
- Mark which questions should be answered and which should be refused.
- Ask the agent to answer using approved sources.
- Check whether each citation supports the sentence.
- Revise the answer and refusal behaviour.

### Break Checklist

- Ask for a causal explanation not supported by the data.
- Ask an out-of-scope policy question.
- Check whether the source contradicts the answer.

### Submit

- Evaluation cases.
- Before-and-after answer.
- Citation checks.
- Refusal case.
- Defence note.

## Week 6 - Launch Review

### Situation

The launch committee asks whether the system can go live.

### Your Goal

Defend a launch recommendation using your portfolio evidence.

### Key Ideas

- A launch decision is not a feature tour.
- Shipping means scope, owners, monitoring, rollback, and no-ship conditions are clear.
- Incident response should use evidence, not improvisation.

### Build Checklist

- Assemble your weekly evidence.
- Create an evidence map.
- Write a launch checklist.
- Prepare a five-minute demo.
- Prepare for incident questions.

### Break Checklist

- Respond to a drift alert.
- Respond to bad input.
- Refuse stakeholder pressure to overclaim.

### Submit

- Evidence map.
- Launch checklist.
- Incident timeline.
- Final defence script.
- Ship / no-ship recommendation.

## Glossary

**Agent work order:** A structured instruction that defines the goal, inputs, acceptance criteria, and limits for an AI agent.

**AI-use log:** A record of important agent contributions and how you verified or changed them.

**Baseline:** A simple method used as a comparison point before claiming a model is useful.

**Defence note:** A short evidence-linked explanation of what you trust, what you reject, and what remains risky.

**Evaluation case:** A test question or scenario used to check whether an agent behaves acceptably.

**Input contract:** A definition of required fields, accepted values, and expected output for a tool.

**Leakage:** Use of information that would not be available at the time of decision.

**Quarantine table:** A table of records that require review instead of being silently dropped.

**Runbook:** A practical guide for operating, testing, recovering, and escalating a tool.

**Smoke test:** A small check that catches obvious errors quickly.
