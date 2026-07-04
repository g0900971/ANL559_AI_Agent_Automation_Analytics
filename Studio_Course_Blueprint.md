# ANL559 Studio Course Blueprint

## Course Premise

Students are placed in a fictional analytics automation studio. Each week they receive a practical mission from a business stakeholder. Their job is to use an AI agent to build the first draft, then make it reliable enough to defend.

The course avoids starting with a framework. Instead, students repeatedly experience the same pattern:

1. **Build** - use the agent to create a useful artefact quickly.
2. **Break** - stress it with bad data, edge cases, ambiguous prompts, or user misuse.
3. **Defend** - write the evidence that proves what is safe, what is risky, and what must happen next.

The package is self-contained: `Weekly_Case_Packs.md` gives the detailed case-study layer, `Instructor_Delivery_Notes.md` gives the teaching detail, `Student_Workbook.md` gives student context and checklists, `Sample_Data_and_Scenarios.md` explains the fictional company and data defects, and `Starter_Kit/` supplies templates plus sample data.

## Six-Week Arc

| Week | Studio mission | Main artefact | Break moment | Defence evidence |
|---:|---|---|---|---|
| 1 | The Monday KPI pack is late again. Automate the recurring reporting workflow. | Repo, agent work order, reporting script, smoke tests | Agent invents a metric definition and silently changes a denominator | Metric-definition note, test output, AI-use log |
| 2 | Two dashboards disagree. Find the truth before the board meeting. | Data reconciliation pipeline and quality gates | Agent inner-joins away missing records and calls the result clean | Reconciliation report, quarantine table, contract tests |
| 3 | Retention budget is limited. Decide who should receive an offer. | Baseline model, cost-aware threshold, decision memo | Agent leaks the answer through a post-outcome feature | Leakage audit, baseline comparison, cost rationale |
| 4 | Operations wants a tool, not a notebook. Make the model usable. | Internal analytics product: API or lightweight dashboard | Agent ships a tool that works locally but fails on invalid input | Contract-bound service, CI checks, runbook |
| 5 | The CEO asks: "Why did churn change?" Build an analyst agent that can answer with sources. | Tool-using analyst agent and evaluation set | Agent gives a fluent answer with unsupported causal claims | Evaluation harness, citation checks, refusal cases |
| 6 | Launch review. Can the team ship and defend the system? | Portfolio evidence pack and live demo | Incident drill: metric drift, bad input, and stakeholder pressure | Launch checklist, incident timeline, defence script |

## Standard 180-Minute Seminar Shape

| Time | Block | Teaching purpose |
|---:|---|---|
| 0-5 | Retrieval link | What did we build, break, and defend last week? |
| 5-15 | Cold open | A short business scene that creates urgency. |
| 15-25 | Demo target | Show the kind of artefact students will build by the end. |
| 25-45 | Concept burst | Only the ideas needed for today's build. |
| 45-80 | Studio sprint A | Students build the first version with the agent. |
| 80-95 | Break it | Instructor releases failure cards; students try to expose defects. |
| 95-135 | Studio sprint B | Students fix the defects and add evidence. |
| 135-160 | Peer demo | Pairs demo artefacts and critique evidence. |
| 160-175 | Defence note | Students write the claim they can defend. |
| 175-180 | Exit ticket | One sentence: what they trusted, what they rejected, what they changed. |

The exact minute marks can flex, but the sequence should not: retrieval, motivation, build, break, repair, defend.

## Assessment Shape

The refreshed version favours a portfolio of working artefacts over long reports.

| Evidence | What markers look for |
|---|---|
| Working artefact | Does it run? Does it solve the mission? |
| Break evidence | Did the student find agent failure, edge cases, or bad assumptions? |
| Defence note | Can the student explain the decision, risk, and remaining limits? |
| AI-use log | Did the student supervise the agent rather than merely accept output? |
| Demo | Can the student operate and explain the artefact under questioning? |

## Alignment Logic

Every week uses the same alignment chain:

1. **Mission:** a realistic analytics automation problem.
2. **Artefact:** the professional object students must produce.
3. **Failure:** the agent or workflow defect students must expose.
4. **Evidence:** tests, traces, notes, or demos proving the repair.
5. **Defence:** a short explanation of what can and cannot be trusted.

This keeps learning activities, assessment evidence, and final viva preparation aligned.

## Course Tone

The course should feel like a professional studio, not a theory survey. Students should leave every week with something they can show, run, critique, and reuse.
