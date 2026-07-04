# Week 2 Exercise Sheet - The Board Number Is Wrong

## Purpose

Students learn how to reconcile conflicting business numbers and how AI-generated joins can hide missing records.

Use this sheet with the Week 2 section of `Weekly_Case_Packs.md`. The case pack gives the fuller board-paper story, data context, intentional defects, and solution guidance.

## Materials

- `Starter_Kit/sample_data/week2_subscriptions.csv`
- `Starter_Kit/sample_data/week2_cancellations.csv`
- `Starter_Kit/sample_data/week2_product_events.csv`
- `Starter_Kit/templates/defence_note_template.md`

Recommended additional template:

- `Starter_Kit/templates/reconciliation_report_template.md`

## Case Setup For Students

Finance and Product have different churn numbers in draft board materials. Finance works from billing subscriptions. Product works from product activity. The board needs one trusted number for the decision being discussed, plus an explanation of why the earlier numbers differed.

Your job is not to make one clean table as quickly as possible. Your job is to show the row-count story from source files to trusted number, and to expose records that should not be silently dropped.

Important note: the sample dataset is a small teaching miniature. It is designed to reveal reconciliation logic and join defects, not to reproduce the illustrative dashboard percentages in the slide story.

## Learning Outcomes

After this exercise, students should be able to:

- Profile sources before joining them.
- Explain how join choice affects the business number.
- Build a quarantine table for unmatched or ambiguous records.
- Define a validation gate that prevents silent data loss.
- Write a trusted-number note with a scoped limitation.

## Studio Flow

| Time | Activity | Concrete output |
|---:|---|---|
| 0-10 | Case briefing and source orientation | Students name the competing definitions and source owners. |
| 10-25 | Exercise 1 | Source profile table. |
| 25-45 | Exercise 2 | Join choice comparison. |
| 45-70 | Exercise 3 | Quarantine table. |
| 70-90 | Exercise 4 | Validation gate. |
| 90-105 | Exercise 5 | Board note. |

For a three-hour seminar, wrap this core with a live inner-join demo, peer review of quarantine tables, and a final defence note.

## Exercise 1 - Source Profile Before Joining

**Time:** 15 minutes

**Student task:** Profile each file before asking the agent to join anything.

Required profile:

| Source file | Row count | Unique customer count | Date fields | Possible data-quality issue |
|---|---:|---:|---|---|
| subscriptions |  |  |  |  |
| cancellations |  |  |  |  |
| product events |  |  |  |  |

**Instructor prompt:** "A join without source counts is a trust fall."

**Look for:** Students should record both row count and unique customer count. If those differ, the group needs to explain duplicates before trusting any rate.

## Exercise 2 - Join Choice Debate

**Time:** 20 minutes

**Student task:** Ask the agent for a join strategy. Before accepting it, compare three choices:

| Join strategy | What it preserves | What it may hide | When it is appropriate |
|---|---|---|---|
| Inner join |  |  |  |
| Left join from subscriptions |  |  |  |
| Full outer review |  |  |  |

**Expected discussion:** The operational source of subscriptions should not lose customers simply because product usage is missing.

**Instructor checkpoint:** Ask students to name which customer IDs each join would hide. This moves the discussion from abstract join types to visible business consequences.

## Exercise 3 - Quarantine Table

**Time:** 25 minutes

**Student task:** Build a quarantine table with records that should not be silently dropped.

Minimum fields:

- `customer_id`
- `source_seen_in`
- `issue_type`
- `why_it_matters`
- `recommended_action`

Starter defects to find:

- `C204` is in subscriptions and cancellations but has no product event.
- `C999` is in product events but not in subscriptions.
- `C204` has a blank cancellation reason.

**Expected evidence:** The quarantine table should explain whether each record affects the billing churn denominator, the product diagnostic view, or follow-up ownership.

## Exercise 4 - Validation Gate

**Time:** 20 minutes

**Student task:** Define a validation gate that should run before the board number is accepted.

Examples:

- Join coverage from subscriptions to product events must be at least a stated threshold.
- All cancelled customers must have billing-end dates.
- All quarantined rows must be reported, not deleted.
- The churn formula must name whether it uses request date or billing-end date.

**Expected evidence:** A test, SQL check, spreadsheet rule, or plain-language validation table.

**Acceptance check:** A peer should be able to say exactly what condition would stop the number from entering the board pack.

## Exercise 5 - Board Note

**Time:** 15 minutes

Write a short board note:

> The number we recommend using is ___ because ___. The previous numbers differed because ___. Remaining limitations are ___.

## End-Of-Class Bundle

Teams should submit or save:

- Source profile table.
- Row-count bridge.
- Quarantine table.
- Validation gate.
- Trusted-number note.
- Defence note or short board-paper paragraph.

## Fallback Routes

If students cannot code:

- Use spreadsheet filters or lookups to compare customer IDs.
- Manually mark `matched`, `subscription_only`, `product_only`, and `needs_review`.
- Write validation gates as plain-language rules with expected evidence.

If students finish early:

- Add a definition-owner table for Finance and Product.
- Add an alert threshold for join coverage.
- Draft a recurring monthly reconciliation checklist.

## Instructor Solution Notes

The important teaching point is not a single perfect churn number. It is the reconciliation logic. Strong teams can explain which rows were lost by an inner join and why a quarantined record is more honest than a silently cleaned table.

Common mistakes:

- Choosing the largest table as the source of truth without business justification.
- Removing unmatched rows to make the result clean.
- Treating missing cancellation reason as a harmless null.
- Failing to distinguish billing churn from product inactivity.

## Extension Options

- Build an automated row-count bridge.
- Add a daily alert when join coverage changes.
- Write a short "definition owner" note naming Finance and Product responsibilities.
