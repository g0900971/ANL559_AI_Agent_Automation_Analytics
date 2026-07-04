# ANL559 Studio Refresh

This folder contains an alternative teaching package for ANL559. It is not a polish pass on the existing H-SAAF roadmap. It reframes the course as a six-week analytics automation studio.

## Design Intent

The refreshed course is built around practical studio work:

- Start from a recognisable business problem.
- Build a working automation artefact with an AI agent.
- Break it deliberately through tests, adversarial data, or user misuse.
- Defend the final artefact with evidence, cost logic, and operational controls.

The repeated teaching rhythm is:

1. Build something useful.
2. Break it on purpose.
3. Defend what remains.

This gives students a concrete habit: they do not just prompt an agent; they turn agent output into a reliable analytics workflow.

## Folder Contents

| File or folder | Purpose |
|---|---|
| `Studio_Course_Blueprint.md` | Six-seminar redesign, weekly missions, artefacts, and run-of-show. |
| `Complete_Instructor_Guide.md` | Full instructor manual for learning the course design, preparing delivery, using the decks, facilitating activities, and assessing evidence. |
| `Facilitation_Guide.md` | Teaching moves, room setup, timing, and instructor prompts. |
| `Instructor_Delivery_Notes.md` | Detailed weekly teaching notes, preparation guidance, expected outputs, and fallback paths. |
| `Weekly_Case_Packs.md` | Detailed week-by-week case studies with stakeholder brief, data context, failure cards, expected evidence, and solution guidance. |
| `Student_Workbook.md` | Student-facing context, weekly checklists, evidence expectations, and glossary. |
| `Mission_Cards.md` | Student-facing weekly mission cards. |
| `Exercises/` | Detailed weekly exercise sheets with timing, instructions, expected evidence, instructor notes, and extensions. |
| `Worked_Examples.md` | Concrete examples of good work orders, logs, audits, memos, input contracts, answers, and launch recommendations. |
| `Prompt_Guidelines_and_Library.md` | Prompt patterns, repair prompts, weak-vs-strong examples, and agent supervision checklist. |
| `Portfolio_and_Assessment_Model.md` | Studio-style portfolio evidence, rubric, and viva prompts. |
| `Sample_Data_and_Scenarios.md` | Synthetic scenario context, data defects, schemas, and incident injects. |
| `Teaching_Practice_Review.md` | Review against teaching-practice principles and the revamp decisions applied. |
| `Starter_Kit/` | Templates and sample data so the seminars can run without external datasets. |
| `Slide_Decks/` | Six expanded PowerPoint decks, 77 slides each. Treat the Markdown guides as the current source of truth before refreshing slide exports. |
| `PDFs/` | PDF exports of the six expanded seminar decks, 77 pages each. |
| `PDFs/Documents/` | PDF exports of the main instructor and student guide documents. |
| `Course_Revamp_Review.md` | Audit findings, changes made in the revamp, and recommended next maintenance steps. |

## Self-Contained Use

This package is designed to run on its own. A new instructor can teach from it without reading the older course files.

Recommended use sequence:

1. Read `Complete_Instructor_Guide.md` to understand the course design and delivery model.
2. Read `Studio_Course_Blueprint.md` for the six-week arc.
3. Read `Weekly_Case_Packs.md` for the detailed weekly stakeholder cases, traps, expected evidence, and solution guidance.
4. Read `Instructor_Delivery_Notes.md` before teaching each seminar.
5. Give students `Student_Workbook.md`, `Mission_Cards.md`, and the relevant files from `Starter_Kit/`.
6. Use `Sample_Data_and_Scenarios.md` to explain the fictional company, data fields, known checks, and intentional defects.
7. Use the matching weekly file in `Exercises/` for guided practice.
8. Show examples from `Worked_Examples.md` or `Starter_Kit/examples/` before students build.
9. Use `Prompt_Guidelines_and_Library.md` when students need help supervising the agent.
10. Teach from the weekly 77-slide deck in `Slide_Decks/`, or distribute the matching PDF from `PDFs/`.
11. Assess using `Portfolio_and_Assessment_Model.md`.

Each weekly deck is designed for a three-hour seminar and now contains 77 slides. The deck is a teaching spine, not a lecture script: some slides are transition cues, some are activity timers, and some are instructor support for build, break, repair, peer review, and defence.

## How This Differs From the Existing Course

- It is mission-first rather than framework-first.
- It uses shorter concept bursts followed by studio work.
- It treats agent failures as game mechanics: students earn trust by finding and fixing them.
- It foregrounds useful analytics products: KPI automation, data-quality gates, decision models, internal tools, analyst agents, and launch controls.
- It keeps governance and evaluation, but teaches them through launch reviews, incident drills, and evidence packs rather than through long standards lectures.

## Deck Index

| Week | Deck | Core mission |
|---:|---|---|
| 1 | `Slide_Decks/Week_1_Studio_Slides.pptx` | 77-slide seminar on turning a recurring reporting fire drill into an agent-assisted automation. |
| 2 | `Slide_Decks/Week_2_Studio_Slides.pptx` | 77-slide seminar on reconciling disagreeing numbers and building data-quality gates. |
| 3 | `Slide_Decks/Week_3_Studio_Slides.pptx` | 77-slide seminar on allocating a limited intervention budget using a defended decision model. |
| 4 | `Slide_Decks/Week_4_Studio_Slides.pptx` | 77-slide seminar on turning a notebook into a usable internal analytics product. |
| 5 | `Slide_Decks/Week_5_Studio_Slides.pptx` | 77-slide seminar on building and evaluating a tool-using analyst agent. |
| 6 | `Slide_Decks/Week_6_Studio_Slides.pptx` | 77-slide seminar on launch review, incident drill, and final portfolio defence. |

PDF versions are available with matching filenames in `PDFs/`. Guide PDFs are available in `PDFs/Documents/`, including the complete instructor guide, student workbook, exercise pack, prompt library, worked examples, scenario guide, mission cards, and assessment model.

## Maintenance Note

The Markdown guides and exercise sheets have been expanded with richer case detail. The existing PowerPoint decks and PDF exports may need a separate refresh if you want distributed slides/PDFs to match the latest Markdown content.

## Use Recommendation

Use this package when the teaching priority is engagement, applied skill, and student confidence. Use the existing course package when the priority is formal framework coverage and document alignment.
