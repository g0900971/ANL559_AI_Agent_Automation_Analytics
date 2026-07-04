# Portfolio and Assessment Model

This assessment model fits the Studio Refresh version of ANL559. It rewards practical supervision, evidence, and judgement rather than long narrative reporting.

## Portfolio Evidence

Each week contributes one portfolio bundle.

| Week | Portfolio bundle | Minimum evidence |
|---:|---|---|
| 1 | Reporting automation | Work order, metric definitions, reporting script, smoke-test output, AI-use-log entry |
| 2 | Data reconciliation | Row-count bridge, quarantine table, validation tests, trusted-number note |
| 3 | Decision model | Baseline table, leakage audit, threshold rationale, decision memo |
| 4 | Internal analytics product | API or dashboard, bad-input rejection, CI evidence, runbook |
| 5 | Analyst agent | Evaluation set, source-citation checks, refusal cases, before-and-after answer |
| 6 | Launch evidence pack | Launch checklist, incident timeline, evidence map, defence script |

## Suggested Weighting

| Component | Weight | What is assessed |
|---|---:|---|
| Weekly studio artefacts | 30% | Does each artefact run, solve the mission, and include evidence? |
| Group demo | 25% | Can the team operate the system and respond to critique? |
| Individual defence note | 20% | Can the student explain what they accepted, rejected, fixed, and still distrust? |
| AI-use log | 15% | Is agent use specific, honest, and tied to verification? |
| Participation in break/peer review | 10% | Did the student find defects and help improve another team's artefact? |

## Studio Rubric

Use the same four criteria every week.

| Criterion | Excellent | Adequate | Weak |
|---|---|---|---|
| Useful artefact | Runs from a clean checkout and directly solves the mission | Runs with minor setup help or solves part of the mission | Does not run or does not address the mission |
| Agent supervision | Agent output is reviewed, rejected or modified where appropriate, and logged | Agent use is visible but verification is thin | Agent output is accepted with little evidence of judgement |
| Break evidence | Meaningful defect found, reproduced, and prevented from recurring | Defect found and fixed once | No serious defect found, or defect discussed but not reproduced |
| Defence | Claims are specific, evidence-linked, and include limits | Claims are plausible but lightly evidenced | Claims are vague, overconfident, or unsupported |

## Viva Prompts

Use these prompts for individual defence:

1. Show me one place where the agent was wrong.
2. Show me the evidence that changed your mind.
3. What would fail if this system were used by ten times more people?
4. Which claim in your portfolio is strongest, and which is weakest?
5. What should not be shipped yet?

## Marker Guidance

Do not reward polish alone. A clean slide deck with no defect evidence is weaker than a rough artefact with a clear failure, fix, and defence.

The central question is:

> Did the student supervise an AI agent into producing reliable analytics work?
