# Week 6 Exercise Sheet - Launch Review

## Purpose

Students learn to defend a launch decision using evidence from the full portfolio. The final session tests operational judgement, not just presentation polish.

Use this sheet with the Week 6 section of `Weekly_Case_Packs.md`. The case pack gives the fuller launch-committee story, recommendation options, incident injects, and solution guidance.

## Materials

- Weekly artefacts from Weeks 1-5.
- `Starter_Kit/templates/evidence_map_template.md`
- `Starter_Kit/templates/launch_checklist_template.md`
- `Portfolio_and_Assessment_Model.md`
- `Sample_Data_and_Scenarios.md` Week 6 incident injects.

## Case Setup For Students

The launch committee does not want a feature tour. It wants a decision: what can go live, in what scope, with which evidence, with which owners, and under what no-ship conditions.

Your team may recommend full launch, limited pilot, or no ship. A limited pilot or no-ship recommendation can be strong if it is honest, evidence-linked, and operationally clear.

Decision options:

| Recommendation | When it is appropriate |
|---|---|
| Full launch | Every critical claim has evidence, owner, monitoring, and rollback. |
| Limited pilot | The system works in a controlled scope but has unresolved scale, impact, monitoring, or ownership risk. |
| No ship | Critical evidence is missing or incident response is not credible. |

## Learning Outcomes

After this exercise, students should be able to:

- Convert weekly artefacts into launch evidence.
- Distinguish what evidence proves from what it does not prove.
- Respond to incident pressure using checks, owners, and rollback.
- Defend a scoped ship, limited-pilot, or no-ship recommendation.
- Answer viva questions about agent failures and residual risk.

## Studio Flow

| Time | Activity | Concrete output |
|---:|---|---|
| 0-10 | Launch committee briefing | Teams state provisional recommendation. |
| 10-35 | Exercise 1 | Evidence map. |
| 35-55 | Exercise 2 | Launch checklist. |
| 55-85 | Exercise 3 | Incident drill. |
| 85-105 | Exercise 4 | Viva circle. |
| 105-120 | Exercise 5 | Final recommendation. |

## Exercise 1 - Evidence Map

**Time:** 25 minutes

**Student task:** Map each launch claim to evidence.

| Launch claim | Evidence | What it proves | What it does not prove | Owner |
|---|---|---|---|---|
| KPI pack can be rerun |  |  |  |  |
| Churn number is reconciled |  |  |  |  |
| Decision model avoids leakage |  |  |  |  |
| Tool rejects bad input |  |  |  |  |
| Analyst answer is source-grounded |  |  |  |  |

**Instructor prompt:** "A claim without an evidence link is a hope, not a launch argument."

**Look for:** Strong teams write both "what it proves" and "what it does not prove." This keeps the launch claim scoped.

## Exercise 2 - Launch Checklist

**Time:** 20 minutes

Students complete a launch checklist:

- Scope of use.
- No-ship conditions.
- Required evidence.
- Monitoring owner.
- Support owner.
- Rollback path.
- Known limitations.

**Expected evidence:** The checklist should name at least one no-ship condition and at least one human owner. The agent cannot be the owner.

## Exercise 3 - Incident Drill

**Time:** 30 minutes

The instructor gives one inject during each team's demo.

Inject examples:

- The active customer count is outside the expected range.
- A user sends a request with missing fields.
- A stakeholder asks the team to claim the campaign caused churn reduction.
- The latest data-quality gate failed.
- No one knows who monitors the next run.

Student response must include:

1. What pauses or stops.
2. Which evidence or check is used.
3. Who owns the next action.
4. What is communicated to stakeholders.

**Instructor checkpoint:** If a team continues the launch unchanged after a failed gate, ask which evidence says that is safe. Usually the right response is to pause or narrow scope.

## Exercise 4 - Viva Circle

**Time:** 20 minutes

Students answer individual questions in rotating pairs:

- Show one place where the agent was wrong.
- Show evidence that changed your mind.
- What would fail at ten times the volume?
- Which portfolio claim is weakest?
- What should not be shipped yet?

Peer listener records one follow-up question.

**Expected evidence:** Each student should answer from their own understanding, not by reading a group script. The purpose is individual defence of supervised agent work.

## Exercise 5 - Final Recommendation

**Time:** 15 minutes

Students write the final recommendation:

> We recommend ship / limited pilot / no ship because ___. The strongest evidence is ___. The main residual risk is ___. The next owner is ___.

## End-Of-Class Bundle

Teams should submit or save:

- Evidence map.
- Launch checklist.
- Incident response note or timeline.
- Final recommendation.
- Individual viva notes.
- Updated portfolio index.

## Fallback Routes

If some weekly artefacts are incomplete:

- Mark missing evidence honestly in the evidence map.
- Recommend limited pilot or no ship for unsupported claims.
- Use the gap as the basis for no-ship conditions and next owner actions.

If teams finish early:

- Run a cross-team red-team review.
- Add a post-launch monitoring table.
- Record a two-minute executive launch recommendation.

## Instructor Solution Notes

Strong final demos are specific about scope. A team can receive a high mark with a "limited pilot" or "no ship yet" recommendation if the evidence and ownership logic are strong.

Common mistakes:

- Turning the final demo into a feature tour.
- Hiding weaknesses instead of owning residual risk.
- Making a broad launch claim from narrow evidence.
- Saying "the agent will monitor it" without naming a human owner.

## Extension Options

- Run a cross-team red-team review.
- Record a two-minute executive launch recommendation.
- Add a post-launch monitoring dashboard design.
