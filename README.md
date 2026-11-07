# Field Read

**Read a whole field from the outside before you bet your next five years on it.**

Field Read is an add-on for Claude Code, Codex and Cursor (and anything else that reads the Agent Skills format, with a rule file for GitHub Copilot). Point it at an industry, a technology wave or a profession and it reads seven places in the public record, records the base rate from the last comparable shifts, and writes three dated scenarios with the signals that would confirm or kill each one. Every claim is marked cited, inferred or unknown. Ask it to compare two fields and it reads both to the same depth and puts them side by side against your own criteria.

It is the sibling of [Cold Read](https://github.com/me2resh/cold-read), which reads one company. Field Read reads the field the company sits in.

Site: https://me2resh.github.io/field-read/

## Four uses

| Lens | The question | Output |
|---|---|---|
| Career | Is this a good field to move into, and which roles gain? | Ten roles that gain and ten that lose, the vocabulary, the gap between you and the gaining roles, three questions to answer before moving |
| Build | Where will the capability line be when my product ships, and who is moving in? | The capability curve, the incumbents' says and does, kill criteria as dated signals |
| Invest | Where is the money going, and what does it expect back? | Capital by quarter, comparables and multiples, the bull and the bear by name |
| Position | Where should a company stand in a moving field? | The market map by scenario, the two or three dated events that change the ranking |

Comparison is optional and works with any lens: "A versus B" runs the lanes on both fields, same horizon, same depth, and ends with a criteria table, switching costs and dated decision points.

## The seven lanes

1. **Capital**: funding by quarter, the largest rounds, comparables and multiples, failures. Money moves 18 to 36 months before headcount.
2. **Labour**: job ads across 15 to 30 named companies, counted from the applicant-tracking APIs; roles that appeared and disappeared; layoffs; pay bands.
3. **Capability curve**: releases, verified benchmarks, cost per unit of work over time, open-source activity.
4. **Incumbents**: what the five largest players say to investors against what they ship.
5. **Regulation and standards**: the laws, standards, procurement rules and liability positions that set the pace.
6. **Base rates**: what happened to the same roles and company types in the last three comparable shifts. Written before any scenario.
7. **Disagreement**: where credible, named people disagree, and what evidence would settle it.

## Install

Claude Code, one line:

```
/plugin install field-read --marketplace me2resh/field-read
```

Older Claude Code, two steps: `/plugin marketplace add me2resh/field-read`, then `/plugin install field-read@field-read`. From the shell: `claude plugin install field-read --marketplace me2resh/field-read`. The skill then answers to `/field-read` (or `/field-read:field-read`).

Codex and other agents that read the Agent Skills format: clone the repo and run `./install.sh codex` (copies `skills/field-read/` into `~/.codex/skills/`), or `./install.sh /path/to/your/agent/skills`. Cursor: copy `.cursor/rules/field-read.mdc` into your project. Copilot: copy `.github/copilot-instructions.md`. Anything else: add `AGENTS.md` to its instructions and keep `skills/field-read/` readable.

Then ask: *"Field read industrial robotics software over three years, career lens"* or *"Compare platform engineering with physical AI as a place to spend the next three years."*

## The output is deterministic

Every read follows a fixed skeleton: Skeleton A for one field, Skeleton B for a comparison. Numbered sections in a fixed order, tables with fixed columns, a mark on every claim, probabilities as ranges, three scenarios each with dated confirming signals and one killing signal, footnotes as `[^s<lane>-<n>]` grouped by lane at the end, and a header with a true source count. `skills/field-read/references/outputs.md` is the specification; `skills/field-read/scripts/check_read.py` fails a note that drifts from it, and the skill runs it before finishing.

## Rules the skill enforces

- Public record only. Nothing behind a login, no scraping against terms, no pretexts.
- Every claim marked ✅ cited, 🟡 inferred, ❔ unknown.
- No LinkedIn profile views; snippets, public writing and talks only.
- Hype is a data point, not a finding: a market-size figure names who published it and who paid for it.
- Base rates before forecasts: no scenario is written until lane 6 is.
- Every scenario carries a falsifier.
- Comparisons are symmetric: same horizon, same lanes, same depth, criteria written before the lanes run.
- Inside knowledge stays in a separate, marked section; the shareable copy reconstructs from sources alone.
- Dates on everything.

## Repository

```
.claude-plugin/plugin.json          plugin manifest
.claude-plugin/marketplace.json     this repo is also its own marketplace
skills/field-read/SKILL.md          the skill (Agent Skills format)
skills/field-read/references/       lanes, sources and endpoints, output layouts
skills/field-read/examples/         sample reads (first one to follow)
skills/field-read/scripts/check_read.py   layout and citation checker
docs/build/build_samples.py          renders the samples to docs/samples/*.pdf
AGENTS.md                           generic agent instructions (Codex and others)
.cursor/rules/                      Cursor rule
.github/copilot-instructions.md
docs/                               the website
install.sh                          copies the skill for agents without plugins
```

## Licence

MIT.

---

Part of [me2resh skills](https://github.com/me2resh/skills), free and open source: Cold Read, Field Read, Tayyib and Job Apply. Add them all with `/plugin marketplace add me2resh/skills`.
