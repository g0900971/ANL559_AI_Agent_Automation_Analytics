# Mission Cards

These cards are written for students. Each card defines the week's practical mission, the artefact to build, the failure to hunt, and the evidence to submit.

Use these cards with `Student_Workbook.md`, `Weekly_Case_Packs.md`, `Sample_Data_and_Scenarios.md`, and the relevant files in `Starter_Kit/`.

## Week 1 - Reporting Fire Drill

**Scene:** Monday, 8:40 a.m. The COO wants the weekly KPI pack by 10:00. Last week the analyst spent three hours copying numbers between CSV files, Excel, and slides.

**Your mission:** Use an AI agent to turn the recurring KPI pack into a reproducible reporting workflow.

**Build:** A repo with a work order, a reporting script, metric definitions, and smoke tests.

**Starter materials:** `week1_customers.csv`, `week1_sales.csv`, `week1_support.csv`, `week1_metric_definitions.md`, `work_order_template.md`, and `ai_use_log_template.md`.

**Break:** The agent invents one metric definition and changes a denominator.

**Defend:** Show the metric-definition note, the test that catches the issue, and the corrected output.

## Week 2 - The Board Number Is Wrong

**Scene:** Finance says churn is 11.8 percent. Product says it is 9.4 percent. Both dashboards are used in board papers.

**Your mission:** Reconcile the number and build a gate that prevents this disagreement from recurring.

**Build:** A data reconciliation pipeline with source counts, join coverage, quarantine rows, and validation tests.

**Starter materials:** `week2_subscriptions.csv`, `week2_cancellations.csv`, `week2_product_events.csv`, and the Week 2 section of `Sample_Data_and_Scenarios.md`.

**Break:** The agent inner-joins away unmatched records and calls the table clean.

**Defend:** Show the reconciliation report and explain which number is now trusted and why.

## Week 3 - Limited Retention Budget

**Scene:** The business can afford 8,000 retention offers, not 80,000. A model is only useful if it helps choose who receives an offer.

**Your mission:** Build a cost-aware decision model, not just a high-scoring model.

**Build:** Baselines, a candidate model, a threshold rationale, and a one-page decision memo.

**Starter materials:** `week3_retention_training.csv`, the cost assumptions in `Sample_Data_and_Scenarios.md`, and `defence_note_template.md`.

**Break:** The agent includes a post-outcome feature that makes the model look excellent.

**Defend:** Show the leakage audit, baseline comparison, and expected-value calculation.

## Week 4 - From Notebook to Tool

**Scene:** Operations likes the model but will not run a notebook. They need a small internal tool that rejects bad inputs and produces a consistent answer.

**Your mission:** Turn the analysis into a usable analytics product.

**Build:** A contract-bound API or lightweight dashboard, CI checks, and a runbook.

**Starter materials:** Week 3 decision logic, the Week 4 request schema in `Sample_Data_and_Scenarios.md`, `runbook_template.md`, and `peer_demo_review_template.md`.

**Break:** The first version works locally but crashes on missing or malformed inputs.

**Defend:** Show the rejected bad request, the passing CI checks, and the runbook entry.

## Week 5 - The Executive Question

**Scene:** The CEO asks, "Why did churn rise this month?" A fluent answer is not enough. The answer needs sources, uncertainty, and limits.

**Your mission:** Build a tool-using analyst agent that answers business questions with evidence.

**Build:** An analyst-agent workflow, source retrieval, evaluation cases, and refusal tests.

**Starter materials:** `week5_knowledge_base.md`, `week5_eval_cases.csv`, and `ai_use_log_template.md`.

**Break:** The agent gives a confident causal claim without support.

**Defend:** Show the evaluation case that catches the unsupported claim and the corrected answer.

## Week 6 - Launch Review

**Scene:** The launch committee asks: "Can this system go live, and who owns it when something goes wrong?"

**Your mission:** Run a launch review and incident drill for the portfolio system.

**Build:** A launch checklist, evidence pack, live demo, and incident-response timeline.

**Starter materials:** Weekly artefacts from Weeks 1-5, `evidence_map_template.md`, the viva prompts in `Portfolio_and_Assessment_Model.md`, and the Week 6 incident injects in `Sample_Data_and_Scenarios.md`.

**Break:** The instructor injects a drift alert, a bad input, and stakeholder pressure to overclaim.

**Defend:** Show what ships, what does not ship, who owns the next action, and what evidence supports the decision.
