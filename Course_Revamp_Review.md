# Course Revamp Review

Review date: 2026-07-04

Course package: ANL559 - AI Agents for Analytics Automation

## Review Summary

The course has a strong central design: students repeatedly build, break, and defend analytics automation artefacts with an AI agent. The strongest existing elements are the six-week arc, the portfolio assessment model, the starter templates, and the worked examples.

The main usability gap was practical detail. The previous materials explained the course concept well, but each weekly case could still feel under-specified for a new instructor or student team. In particular, the exercise sheets needed richer stakeholder context, clearer expected outputs, more explicit failure modes, and stronger fallback paths for non-coding students.

## Strengths Found

| Strength | Evidence in package |
|---|---|
| Clear course identity | The Build / Break / Defend rhythm is consistent across guides, slides, workbook, and assessment. |
| Authentic artefacts | Students produce work orders, reconciliation reports, leakage audits, tools, evaluation cases, and launch checklists. |
| Practical AI-agent framing | The course rewards supervision, verification, and rejected output rather than passive AI use. |
| Reusable support files | `Starter_Kit/templates/`, sample data, and worked examples make the course self-contained. |
| Assessment alignment | `Portfolio_and_Assessment_Model.md` maps weekly evidence to marking criteria and viva prompts. |

## Gaps Found

| Gap | Why it matters | Revamp response |
|---|---|---|
| Weekly case studies were too brief | Students may not understand stakeholder pressure, data meaning, or why the failure matters. | Added `Weekly_Case_Packs.md` with detailed weekly case briefs, data context, traps, expected evidence, and solution guidance. |
| Exercise sheets were activity lists more than lesson guides | New instructors would need to improvise setup, flow, checkpoints, and fallback routes. | Expanded all six exercise sheets with case setup, learning outcomes, studio flow, evidence bundles, checkpoints, and fallback routes. |
| Student path through the package was unclear | Students could see many files but not know when to use each one. | Updated `Student_Workbook.md` with a weekly case workflow and added `Weekly_Case_Packs.md` to the use sequence. |
| Instructor preparation sequence missed the detailed case layer | Instructors might rely on decks without enough case substance. | Updated `Instructor_Delivery_Notes.md` and `Complete_Instructor_Guide.md` to use the case pack before teaching. |
| README referenced a missing slide-generation script | This creates maintenance confusion for future slide refreshes. | Revised the README to treat Markdown guides as the current source of truth and note that slide/PDF exports may need separate refresh. |
| Sample data are intentionally small but this was not always explicit | Students may expect full realism or exact dashboard percentages. | Added notes in the Week 2 case and exercises that the data are teaching miniatures used to reveal reconciliation logic. |

## Files Updated Or Added

| File | Change |
|---|---|
| `Weekly_Case_Packs.md` | New detailed case-study layer for all six weeks. |
| `Exercises/Week_1_Reporting_Fire_Drill.md` | Added case setup, learning outcomes, studio flow, checkpoints, evidence bundle, and fallback routes. |
| `Exercises/Week_2_Board_Number.md` | Added richer board-number context, reconciliation guidance, row-count expectations, and fallback routes. |
| `Exercises/Week_3_Retention_Decision.md` | Added decision assumptions, leakage framing, top-N guidance, studio flow, and fallback routes. |
| `Exercises/Week_4_Notebook_to_Tool.md` | Added operations context, suggested request/output fields, tool boundary guidance, and handoff evidence. |
| `Exercises/Week_5_Executive_Question.md` | Added source-support guide, evaluation behaviour expectations, refusal guidance, and fallback routes. |
| `Exercises/Week_6_Launch_Review.md` | Added launch decision options, incident-response expectations, viva guidance, and fallback routes. |
| `README.md` | Added the new case-pack and review files; clarified that slides/PDFs may need separate refresh. |
| `Student_Workbook.md` | Added the case-pack reference and a five-question workflow for weekly cases. |
| `Instructor_Delivery_Notes.md` | Added the case pack as a core level of seminar support. |
| `Complete_Instructor_Guide.md` | Added the case pack to the package map and preparation sequence. |
| `Studio_Course_Blueprint.md` | Added the case pack to the self-contained package description. |

## Remaining Recommendations

These were not changed in this pass:

1. Refresh the PowerPoint decks and PDFs so distributed versions match the updated Markdown source.
2. Add instructor demo artefacts for each week, such as a flawed KPI script, flawed join output, leaky model transcript, and unsafe analyst-agent answer.
3. Consider adding a small `scripts/` folder if slide or PDF generation should be reproducible.
4. Create one completed exemplar portfolio bundle for a fictional team, separate from student-facing worked examples.
5. Add optional expanded datasets for advanced cohorts while keeping the current small datasets for classroom teaching.

## Recommended Teaching Workflow After Revamp

Before each seminar:

1. Read the relevant section of `Weekly_Case_Packs.md`.
2. Open the matching exercise sheet in `Exercises/`.
3. Choose one worked example from `Worked_Examples.md` or `Starter_Kit/examples/`.
4. Select two or three failure cards from the case pack.
5. Confirm the relevant sample data and templates are available.

During the seminar:

1. Start with the mission card.
2. Use the case brief to explain stakeholder pressure and data meaning.
3. Run the exercise sheet as the activity guide.
4. Use the case-pack solution guidance when coaching teams.
5. End with the evidence bundle and defence note.

