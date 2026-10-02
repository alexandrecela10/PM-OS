---
name: portfolio-case-study
description: Turn a finished project into a public case study page (portfolio hub on GitHub Pages) plus a LinkedIn project entry, for a private capital audience. Top of page = the private capital problem, the player it's for, and an interactive demo. Details = value equation per persona, sub-problems, one hypothesis per tackled sub-problem, scope, non-goals, success tracking, limits, trade-offs, PM OS lifecycle. Minimal factual tone. Runs /name-audit first and checks every claim against code, logs and tests.
user-invocable: true
disable-model-invocation: false
---

# /portfolio-case-study

Input: a project folder or repo path. Output: `outputs/portfolio/<slug>/` with `index.html`, `linkedin.md`, `name-audit.md`, plus a goals file and a state file (see CLAUDE.md).

## Steps

1. **Read the source, then the code and its outputs.** README, demo script, decks, code, logs, test suite, generated files. Keep observed numbers only.
2. **Check claims.** Every README or deck claim is checked against code, logs or tests. Example: a README said "no LLM call"; the log showed one. Wrong claims are corrected, not repeated.
3. **Map sub-problems to code.** For each sub-problem: tackled, partial or not tackled, with the file or function that proves it.
4. **Run `/name-audit`.** No repo edit before the PM approves its list.
5. **Draft from `template.html`** (in this folder). Same order in `index.html` and `linkedin.md`.
6. **Check links.** Every link returns 200. A sibling page that doesn't exist yet reads "case study coming", with no link.
7. **Checks.** Tone rules in CLAUDE.md (minimal factual, no em dashes, banned words, factual over persuasive). LinkedIn description 2,000 characters or fewer (`wc -m`). Every number traces to a source or reads "unobserved".
8. **Goals + state files.** Wait for PM approval before any repo edit, push or publish.

## Page structure

**Top (above the fold). Answers three questions in under 30 seconds:**

| Block | Content |
|---|---|
| Name | Punchy, says what it does. One-line description under it |
| Problem | The private capital problem, one bold sentence. States the cost, not the symptoms |
| For | The private capital player (e.g. early-stage VC fund) and the personas: user + buyer, with the decision each owns |
| User stories | 2-3 stories, "As a ..., I want ..., so that ...". The demo, sub-problems and hypotheses are organised around them. Anything that serves no story goes to non-goals or details |
| Try it | The interactive demo, or its link, with 3 numbered steps a visitor follows. Label real vs sample data |

**Details (below, in collapsible sections):**

| Section | Content |
|---|---|
| Value equation | Hormozi: value = (outcome × likelihood) / (time delay × effort & sacrifice). One card per persona: outcome, likelihood, delay, effort, sacrifice. Sacrifice = what the persona gives up (control, habit, data, privacy). Verdict: weakest factor + cheapest fix, each fix explained on the page. Outcome in the persona's words; likelihood stays honest; mark unproven causal links as hypotheses |
| Sub-problems | Numbered, one line each, bold label. End with "This build tackles N to M" |
| How it works | Numbered steps, input → process → output |
| Hypotheses | One card per tackled sub-problem, in order: before → after, "If X, then Y, because Z", metric (direction, baseline or "unobserved"), test. Guardrail metric on card 1. Define any ambiguous term |
| Scope / non-goals | Non-goals list every untackled or partial sub-problem and what's missing |
| Success tracking | Leading and lagging metrics, which hypothesis each tests, how it would be measured |
| Observed | Numbers from the build, logs or tests. Say which hypothesis each supports |
| Limits + trade-offs | Synthetic data, untested with users, unmeasured accuracy, assumptions a hypothesis depends on. Trade-offs table: chose, over, gain, cost |
| PM OS lifecycle | The stages this project went through and the artifact at each: discovery, opportunity, PRD, build, evaluation. Only stages with a real artifact |
| Other side | Sibling project and a shared funnel dream, if any |
| Links | Demo, repo, video. Live links only |
| PM OS skills used | Last. If the build sessions weren't logged, map each lifecycle stage to the skill that produces its artifact, and say on the page that the skills are mapped. The point is to show repeatable PM work |

## Writing style

Follow **Minimal factual** in CLAUDE.md for every section. Tables and lists for parallel items, sentences for reasoning.

## Page design

Copy `template.html` from this folder. Navy background, blue accent, Lato: matches the LinkedIn banner. Headings use `display:table` so each sits on its own line. Persona and hypothesis blocks use the card grid, stacked on mobile. Ratings (LOW / MEDIUM / HIGH) in heavy white. Details use `<details>` so the top stays short.

## LinkedIn entry

Same order, compressed. Name, one line, problem, player, demo link, then one line per hypothesis. 2,000 characters max.
