# Week 5 Exercise Sheet - The Executive Question

## Purpose

Students learn to evaluate an analyst agent that answers business questions with evidence, uncertainty, and refusal behaviour.

Use this sheet with the Week 5 section of `Weekly_Case_Packs.md`. The case pack gives the fuller executive story, approved-source guide, unsafe claims, and solution guidance.

## Materials

- `Starter_Kit/sample_data/week5_knowledge_base.md`
- `Starter_Kit/sample_data/week5_eval_cases.csv`
- `Starter_Kit/templates/ai_use_log_template.md`
- `Starter_Kit/templates/defence_note_template.md`
- `Starter_Kit/templates/evaluation_case_template.md`

## Case Setup For Students

The CEO asks, "Why did churn rise in June?" The agent can produce a fluent answer quickly, but a fluent answer can still be unsafe if it invents causality, overuses citations, or ignores uncertainty.

Your task is to build or simulate an analyst agent that answers with approved sources, marks uncertainty, and refuses unsupported claims.

Approved source logic:

| Source | Supports | Does not prove |
|---|---|---|
| KPI Pack | Churn rose from 9.4 percent to 11.8 percent; increase is concentrated among monthly-plan low-usage customers. | Cause of churn. |
| Pricing Note | New monthly-plan customers were affected by a price increase; existing customers were not moved in June. | That price caused June churn. |
| Support Summary | Onboarding-delay tickets increased in June, especially among April and May signups. | That delays caused churn. |
| Product Incident Note | API latency affected dashboard loading, not billing. | That the incident caused billing churn. |
| Marketing Campaign Note | Campaign started on 2026-06-24. | That the campaign reduced full-month June churn. |

## Learning Outcomes

After this exercise, students should be able to:

- Design evaluation cases for analyst-agent behaviour.
- Separate observation, explanation, uncertainty, and recommendation.
- Check whether a citation supports the exact claim made.
- Rewrite unsupported causal claims as refusals or testable hypotheses.
- Produce a CEO-ready answer that is useful but scoped.

## Studio Flow

| Time | Activity | Concrete output |
|---:|---|---|
| 0-10 | Case briefing and source orientation | Students identify what the source base can and cannot support. |
| 10-25 | Exercise 1 | Answer anatomy. |
| 25-45 | Exercise 2 | Expanded evaluation set. |
| 45-70 | Exercise 3 | Citation-support check. |
| 70-85 | Exercise 4 | Safer refusal rewrite. |
| 85-100 | Exercise 5 | CEO-ready answer. |

## Exercise 1 - Answer Anatomy

**Time:** 15 minutes

**Student task:** Break a safe executive answer into five parts:

1. Observed pattern.
2. Evidence.
3. Plausible explanation.
4. Uncertainty or limitation.
5. Recommended next test.

Apply this structure to the question: "Why did churn rise in June?"

**Look for:** Students should avoid making "because" claims too early. A safe answer can say "one plausible explanation to investigate is..." only after naming uncertainty.

## Exercise 2 - Evaluation Set Expansion

**Time:** 20 minutes

Start from `week5_eval_cases.csv`. Add three new cases:

- One factual question.
- One unsupported causal question.
- One out-of-scope policy question.

For each case, define expected behaviour:

| Question | Should answer? | Expected evidence | Should refuse? | Why |
|---|---|---|---|---|
|  |  |  |  |  |

**Expected evidence:** At least one case should test unsupported causality, and at least one should test out-of-scope or insufficient evidence.

## Exercise 3 - Citation Support Check

**Time:** 25 minutes

**Student task:** Ask the agent to answer two evaluation questions. For every sentence with a citation, check whether the cited source supports the exact claim.

Use this marking:

- **Supported:** the source directly supports the claim.
- **Partially supported:** the source supports part of the claim but the answer overstates it.
- **Unsupported:** the cited source does not support the claim.

**Instructor prompt:** "A citation is not decoration. It is a promise that the evidence says what the answer says."

**Instructor checkpoint:** Ask students to highlight the exact words in the source that support the answer sentence. If they cannot highlight support, the citation is weak.

## Exercise 4 - Refusal Rehearsal

**Time:** 15 minutes

Students rewrite unsafe answers into safe refusals.

Unsafe answer:

> The May price increase caused churn to rise in June.

Safer answer:

> The evidence does not support that causal claim. The pricing note says the May price increase applied to new monthly-plan customers, while existing customers were not moved to the new price in June. A safer next step is to compare churn among new customers exposed to the new price with similar customers not exposed.

**Acceptance check:** The safer refusal should still be useful. It should say what evidence is missing and what next test would make the question answerable.

## Exercise 5 - CEO-Ready Answer

**Time:** 15 minutes

Write a final answer that could be sent to the CEO. It must include:

- One observed pattern.
- Two cited sources.
- One uncertainty statement.
- One recommended next test.
- One claim the team refuses to make.

## End-Of-Class Bundle

Teams should submit or save:

- Evaluation case table.
- Before-and-after answer for at least one risky question.
- Citation-support table.
- Refusal rewrite.
- CEO-ready answer.
- AI-use-log entry naming a rejected or repaired agent claim.

## Fallback Routes

If students cannot build retrieval:

- Use the knowledge base manually as the approved source set.
- Ask the agent to draft answers, then evaluate each sentence against the source table.
- Submit the evaluation harness as a spreadsheet or Markdown table.

If students finish early:

- Compare two prompts against the same evaluation cases.
- Add scoring criteria for factuality, citation support, uncertainty, refusal, and next test.
- Record retrieved source, answer sentence, review decision, and repair action.

## Instructor Solution Notes

Strong teams separate observation from explanation. They do not claim causality when the evidence only supports timing, association, or a plausible hypothesis.

Common mistakes:

- Treating a source mention as support for any related sentence.
- Evaluating only easy questions.
- Refusing too vaguely: "I cannot answer" without saying what evidence is missing.
- Letting the agent write an executive answer that the student cannot defend.

## Extension Options

- Compare two prompts on the same evaluation set.
- Add an answer quality rubric with factuality, citation support, uncertainty, and refusal.
- Log prompt, retrieved source, answer, and review decision for each run.
