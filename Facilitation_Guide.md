# Facilitation Guide

## Instructor Stance

Teach like a studio lead. The room should feel active, practical, and slightly time-pressured. The instructor's job is not to explain every tool in advance; it is to set up the mission, show a credible target, then coach students through agent supervision.

Use this refrain every week:

> Fast first draft. Slow acceptance.

## Room Setup

- Students work in pairs or teams of three.
- Every team has one shared repo.
- Every team uses one agent surface as the primary worker.
- Every mission has a visible timer.
- The instructor keeps a public "defect wall" where teams post failures they found.

## Access and Inclusion

The studio should not reward only the fastest coder. Use multiple roles so every student can contribute:

- **Driver:** operates the repo and agent.
- **Reviewer:** reads diffs, checks evidence, and challenges assumptions.
- **Reporter:** prepares the defence note and demo narrative.

Rotate roles weekly. If a student has tool-access problems, they can still meet the learning objective by reviewing a provided agent transcript, writing acceptance tests, or producing the defence note from a supplied artefact.

Provide materials in multiple forms:

- A short mission card.
- A visible slide target.
- A work-order template.
- A checklist for evidence.
- A sample failure card.

This supports students who need a concrete example before open-ended work.

## Teaching Moves

### Cold Open

Open with a specific business pressure:

- The report is late.
- The board number is wrong.
- The model is too good to be true.
- The notebook works only on one laptop.
- The agent answered confidently without evidence.
- The launch committee asks for proof.

Do not explain the whole theory first. Let the pain create the motivation.

### Demo Target

Show a working but imperfect example:

- A script that runs but has a flawed metric.
- A reconciliation table with quarantined rows.
- A model card with one missing slice.
- An API that rejects bad input.
- An analyst-agent answer with cited sources and refusal behaviour.

Students should know what they are building before concepts are introduced.

### Concept Burst

Limit concept teaching to 15-20 minutes. The rule is: if students do not need the idea to complete today's artefact, move it to notes or later.

### Retrieval Link

Start Weeks 2-6 with a two-minute retrieval link:

- What did you build last week?
- What failed?
- What evidence proved the fix?
- Which habit carries into today's mission?

This turns six separate missions into one portfolio arc.

### Break Cards

Every week has three failure cards. Give them after Sprint A, not before.

Examples:

- A metric name is ambiguous.
- A source table has missing IDs.
- A column is post-outcome leakage.
- A malformed request crashes the service.
- A source document contradicts another source.
- A stakeholder asks for a decision outside the system's scope.

### Defence Note

End each week by making students write a short claim they can defend:

- "I trust this number because..."
- "I reject the agent's output because..."
- "The current artefact is safe for... but not for..."
- "The remaining risk is..."

This note becomes portfolio evidence.

### Feedback Loop

Every studio block should produce feedback before students leave:

- Test feedback from running the artefact.
- Peer feedback from the three-minute demo.
- Instructor feedback from the defect wall.
- Self-feedback through the exit ticket.

Do not let teams leave with only a working artefact. They need an artefact plus a judgement about its limits.

## Handling Tool Problems

If a student's agent or API access fails, keep them in the studio:

- They can act as reviewer for another pair.
- They can write the work order and acceptance tests manually.
- They can audit an agent transcript provided by the instructor.
- They can produce the defence note from a supplied artefact.

No student should lose the learning objective because a vendor login failed.

## Weekly Instructor Checklist

Before class:

- Prepare the mission data or repo.
- Read the relevant section of `Weekly_Case_Packs.md`.
- Prepare three failure cards.
- Prepare one imperfect demo artefact.
- Confirm the agent and Python environment work on a clean machine.
- Open the relevant section of `Instructor_Delivery_Notes.md`.
- Distribute the weekly files from `Starter_Kit/sample_data/` and the templates from `Starter_Kit/templates/`.
- Check `Sample_Data_and_Scenarios.md` for known checks, intentional defects, and incident injects.

During class:

- Keep the concept burst short.
- Force students to run the artefact, not just read it.
- Ask "what did you reject?" at least twice.
- Collect one defect from each team.

After class:

- Ask students to commit the artefact and defence note.
- Remind them to log the agent turn that mattered most.
