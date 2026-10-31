---
name: field-read
description: Read a whole field (an industry, a technology wave, a profession) from the public record over a 2 to 5 year horizon, or compare two or three fields side by side, and turn it into dated scenarios with signals rather than a verdict on one company. Use it when someone asks "where is X going", "is Y a better place to be than Z", "what happens to role R when technology T lands", "should I move into field F", or wants an outside view before a career, product or investment decision that depends on how a field moves. Trigger on "future of", "where is this heading", "is this a good field", "will AI replace", "physical AI", "which sector", "A versus B", "compare these fields", even when the user does not say "research". For a single company use cold-read; field-read is its sibling and shares its rules, marks and checker.
---

# Field Read

Read a field the way an analyst, a candidate and an operator would, using only what is public, and write it up so that every claim is either cited or marked as inference. Cold Read answers "what will this company do". Field Read answers "what will happen to this kind of work, this kind of company and this kind of role in the next 2 to 5 years, how would I know early, and if I am choosing between two fields, which one and on what evidence".

## The idea in one paragraph

A field cannot hide its direction. Money moves 18 to 36 months before headcount (lane 1). Job boards across the field are next year's org charts (lane 2). The capability line, and its cost per unit of work, is published in releases, benchmarks and open-source activity (lane 3). The largest players tell investors one thing and ship another, and the gap is the platform risk for everyone smaller (lane 4). Regulation and standards decide timing more often than technology does (lane 5). The last three comparable shifts show what happened to the same roles (lane 6). And where credible people disagree is exactly where the uncertainty lives, so it gets recorded instead of averaged away (lane 7). Read all seven lanes, then write three dated scenarios, each with the signals that would confirm it and the date to check them. When two fields are compared, read both to the same depth and the same horizon, then put them side by side against the reader's own criteria.

## Rules that make the output trustworthy

Cold Read's rules apply in full: public record only; no LinkedIn profiles opened; every claim marked ✅ cited to a source read today, 🟡 inferred or from a snippet, ❔ unknown after looking; dates on everything; name collisions checked; vendor and agency claims are marketing, not evidence; inside knowledge kept in a marked internal section and out of the shareable copy. Four rules are specific to a field read:

- **Hype is a data point, not a finding.** Funding announcements, keynote claims and analyst market-size figures go in lane 1 or lane 4 with their source, and are never repeated in the answer as facts about the field. A market-size number is cited with who paid for the estimate.
- **Base rates before forecasts.** No scenario is written until lane 6 has recorded what happened to the same roles and company types in the last three comparable shifts. A forecast that contradicts the base rate must say why this time differs, with evidence.
- **Scenarios carry falsifiers.** Each scenario names the two or three signals that would confirm it, the date by which they should be visible, and the one signal that would kill it. A scenario without a falsifier is an opinion.
- **Comparisons are symmetric.** Two fields get the same horizon, the same lanes, the same depth and the same criteria table. If one side got less time or thinner sources, the note says so in the header and the comparison section discounts it.

## Step 0: frame the job

| Question | Why it matters |
|---|---|
| Which field, and which slice of it? | "AI and software" is too wide; "engineering leadership roles in software companies of 50 to 500 people as coding agents mature" can be read |
| One field or a comparison? | A comparison runs the lanes once per field and adds the compare skeleton; name every field in the same words throughout |
| Which lens? career, build, invest, position | Decides depth per lane and the "what it means" section; a comparison uses the same lens for every field |
| Horizon? | 2, 3 or 5 years; the signals table is dated to it, and every field in a comparison shares it |
| Who reads it, and can it be shared? | Shareable means no inside facts and no personal implications |
| What are the reader's criteria? | For a comparison: the five to eight things the reader actually weighs (pay floor, remote, authority, ethical filters on sectors, learning, option value, downside). Written before the lanes run, so the criteria cannot drift to fit the answer |
| Time box | Two hours is seven lanes at snippet depth for one field; a comparison of two fields at the same depth is four hours or two agents in parallel |

Settle these in one short exchange or by stating assumptions at the top of the note.

## Step 1: run the lanes

Each lane is a self-contained brief in `references/lanes.md`; read it before spawning. Each lane writes its own file with the header (date, field, sources read, fallbacks tried, legend), a sources table, ten facts, findings, implications and sources. Run the lanes in parallel as separate agents where possible; web lanes go to whichever research agent the user prefers. For a comparison, run the full set once per field; the same agent may take the same lane for both fields so the depth matches.

| Lane | Question it answers | Primary sources |
|---|---|---|
| 1 Capital | Where money is going in the field, at what stage, at what valuations; exits and failures | Funding databases, fund announcements, public comparables and their multiples, M&A, shutdown trackers |
| 2 Labour | Which roles the field is hiring and stopping hiring, where, at what seniority and pay; layoffs | ATS public APIs and boards across 15 to 30 named companies, layoff trackers, salary bands, government labour statistics |
| 3 Capability curve | Where the technology line is, how fast it moves, what one unit of work costs now against two years ago | Model and hardware releases, benchmark tables, open-source activity, published pricing, reproducible demos |
| 4 Incumbents | What the five largest players say to investors against what they ship; which adjacent markets they are entering | Earnings calls, shareholder letters, release notes, developer conferences, pricing changes |
| 5 Regulation and standards | The laws, safety standards, procurement rules and liability cases that set the pace | Legislation and consultations, standards bodies, regulator enforcement, court cases, insurer positions |
| 6 Base rates | What happened to the same roles and company types in the last three comparable shifts | Histories of the cloud, mobile and first machine-learning waves (or the field's own precedents): headcount, titles, survival by stage, time from hype peak to steady state |
| 7 Disagreement | Where credible, named people disagree, and what evidence would settle each dispute | Essays, papers, podcasts and talks by practitioners and researchers with a record; forecasts with dates |

Lane 2 most often changes the answer: count roles from APIs, de-duplicate across boards, note evergreen requisitions, and read the ads for the problems they describe, not the titles. Lane 6 is the one most often skipped; do not skip it. `references/sources.md` lists the sources by lane with the endpoints that worked.

## Step 2: synthesise, to the fixed layout

Write one note from the lane files, to the skeleton for the job in `references/outputs.md`: **Skeleton A** for one field, **Skeleton B** for a comparison. The layout is fixed on purpose: a reader who has seen one Field Read can find anything in the next without reading it through, and the checker can prove nothing was dropped. Do not reorder, rename, merge or omit sections; a section with nothing says "Not found after looking at ..." under its heading.

The standard the note has to meet, in brief:

- The header carries the read date, the horizon, "Public record only. No LinkedIn profile was opened.", the legend and a true count of footnotes and lanes. A comparison header names every field and says whether depth was equal.
- Every fact sentence ends with a mark. Every ✅ is followed by an inline link, a footnote of the form `[^s<lane>-<n>]` (for a comparison, `[^<field-letter>s<lane>-<n>]`, for example `[^As2-4]`), or both. A number is never bare. Quotes carry speaker, occasion and date.
- Probabilities are ranges, marked 🟡, with the reasoning in one line.
- Scenarios are three (base, fast, stall), each with confirming signals dated inside the horizon and one killing signal.
- A comparison ends with a criteria table (the reader's criteria as rows, the fields as columns, each cell marked), the switching cost and option value of each direction, and the dated decision points; never with "go" or "stay".
- Sources are footnotes grouped by lane (and by field in a comparison) at the end, so the note can be rebuilt from them.

Before finishing, run `python3 scripts/check_read.py <note.md>` and fix every failure it prints. Keep the shareable copy separate from the working copy if the working copy holds inside facts or personal implications; the shareable copy keeps the "What it means for the reader" heading with the line "Removed from the shareable copy."

## Lens notes

**Career.** The roles section is the heart: which roles the field is creating and retiring, at what seniority, in which geographies, and the vocabulary the field's hiring managers use. The reader section maps the reader's experience onto the gaining roles and names the gap. A career read ends with the three questions the reader should be able to answer before moving, and never with "go" or "stay".

**Build.** The capability curve and the incumbents carry the weight: where the line will be when the product ships, and which large players are entering the space. The signals table doubles as the builder's kill criteria.

**Invest.** Lane 1 at full depth; the scenarios carry valuation ranges; the disagreement section is the bull and the bear by name.

**Position.** For a company deciding where to stand in a moving field: the market map by scenario, and the two or three dated events that would change the ranking.

**Compare (any lens).** The same lens on every field. Criteria first, lanes second, side by side third. The honest output is often "field A on criteria 1 to 4, field B on 5 to 7, and the decision turns on criterion 3", with the dated signal that would settle criterion 3.

## Pitfalls learned the hard way

- A funding total for a field double-counts when rounds are re-announced; count by company and round date.
- Job counts across many boards need de-duplication by title plus company plus location; evergreen ads a year old are not fresh signals.
- Benchmark tables are self-reported until reproduced; mark them 🟡 unless a third party ran them.
- "Market will be worth $X by 20YY" figures are sold by the firms that publish them; cite the firm and the sponsor.
- The last shift's winners write its history; look for the roles that disappeared, not only the ones that appeared.
- A field read done in a week of big announcements overweights the news; check the capability line against the trend, not the headline.
- In a comparison, the field the reader already knows always looks riskier, because its problems are visible; the lanes exist to make the other field's problems equally visible.
- Two fields are never compared with different horizons or different lane depths; if one side had less time, say so.
