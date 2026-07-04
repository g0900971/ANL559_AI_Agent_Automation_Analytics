# Prompt Guidelines and Library

This guide helps students use AI agents as supervised workers rather than answer machines.

## Core Prompting Principle

Do not ask the agent to "solve the problem." Ask it to perform a bounded task with inputs, acceptance criteria, and constraints.

Strong prompts include:

- Role or task.
- Business context.
- Input files.
- Definitions.
- Output format.
- Acceptance criteria.
- Things the agent must not do.
- How the output will be checked.

## The Work-Order Pattern

Use this pattern for most course tasks:

```text
You are helping build [artefact] for [stakeholder].

Business goal:
[Decision or workflow this supports.]

Inputs:
[Files, schemas, definitions.]

Task:
[Specific build, analysis, test, or documentation request.]

Acceptance criteria:
[What must be true before we accept the output.]

Constraints:
[Do not invent, drop, infer, use leakage, overclaim, or hide assumptions.]

Output format:
[Table, code, tests, memo, JSON, checklist.]
```

## Prompt Moves By Week

| Week | Good agent task | Bad agent task |
|---:|---|---|
| 1 | "Draft a reporting script using these approved metric definitions and add checks for known totals." | "Make a KPI report." |
| 2 | "Profile these sources and produce a row-count bridge before joining." | "Clean and merge these datasets." |
| 3 | "Label columns by decision-time availability and exclude leakage before modelling." | "Build the best churn model." |
| 4 | "Create input validation for this request schema and tests for bad requests." | "Turn this notebook into an app." |
| 5 | "Answer only with cited support and refuse unsupported causal claims." | "Explain why churn increased." |
| 6 | "Map each launch claim to evidence, remaining limit, and owner." | "Write a launch presentation." |

## Repair Prompts

Use repair prompts when the agent output is plausible but unsafe.

### When The Agent Invents A Definition

```text
Stop. Compare your metric definitions against the approved definitions below.
List every mismatch in a table with: metric, your definition, approved definition, risk, correction.
Do not recalculate until the mismatches are resolved.
```

### When The Agent Drops Rows

```text
Before producing the final table, create a row-count bridge.
Show row counts before and after each join.
List unmatched records in a quarantine table.
Do not silently remove any customer ID.
```

### When The Model Looks Too Good

```text
Audit the feature list for leakage.
For each column, state whether it is available at decision time.
Exclude unavailable columns and rerun the baseline comparison.
Report the performance before and after leakage removal.
```

### When The Tool Only Works On The Happy Path

```text
Add validation for missing, malformed, and out-of-range inputs.
Create tests for one valid request and three invalid requests.
Return clear error messages without crashing.
```

### When The Agent Overclaims

```text
Separate the answer into observed pattern, evidence, plausible explanation, uncertainty, and next test.
Mark any causal claim as supported, partially supported, or unsupported.
Rewrite unsupported claims as refusals or hypotheses.
```

### When The Final Demo Is Too Broad

```text
Turn this launch claim into a scoped recommendation.
For each claim, list evidence, remaining limitation, owner, and no-ship condition.
Do not recommend full launch unless every critical claim has evidence.
```

## Agent Supervision Checklist

Before accepting agent output, students should ask:

- Did the agent use approved definitions?
- Did it name assumptions?
- Did it preserve records that should not disappear?
- Did it use only decision-time information?
- Did it produce checks or tests?
- Did it cite evidence for claims?
- Did it state limits?
- Can I explain this output without the agent?

## Classroom Prompt Exercises

### Prompt Rewrite

Give students a weak prompt and ask them to rewrite it using the work-order pattern. Then compare which version is more likely to produce checkable output.

### Prompt Red-Team

Teams exchange prompts and mark:

- Missing input.
- Missing definition.
- Missing acceptance criterion.
- Hidden assumption.
- Unsafe instruction.

### Prompt Diff Review

Students compare two agent outputs from different prompts and identify which prompt better controlled the failure mode.

## Prompting Norms For Assessment

Students do not need to submit every prompt. They should submit prompts that materially affected the artefact:

- The prompt that scoped the build.
- The prompt that generated or changed a test.
- The prompt that exposed or repaired a defect.
- The prompt that produced a claim later accepted or rejected.

Weak AI-use evidence:

```text
Used AI to write the script.
```

Strong AI-use evidence:

```text
Asked the agent to draft a reporting script with approved metric definitions. Accepted the file-loading structure. Rejected the active-customer calculation because it used recent login instead of paid active subscription. Added smoke test paid_active_accounts == 6.
```
