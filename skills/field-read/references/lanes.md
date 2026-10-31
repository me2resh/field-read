# Lane briefs

Each brief is written so it can be handed to a separate agent as its whole prompt, after filling the placeholders in angle brackets. For a comparison, run every lane once per field with the same horizon and the same time box, and name the field in the file name (`lane-2-labour-A.md`, `lane-2-labour-B.md`). Every lane produces one Markdown file with this header:

```
# Lane N: <title>
<Field>, horizon <n> years, read on <date>. Public record only. No LinkedIn profiles opened.
Legend: ✅ cited to a source read today (linked); 🟡 inferred or from a snippet that could not be opened; ❔ unknown after looking.
## Sources and how each was read   (table: source | status | fallbacks tried)
## Ten facts that matter most       (numbered, each with a mark and a link)
## Findings                          (tables by topic)
## What it implies                   (🟡 paragraphs, kept short)
## Sources                           (every URL used)
```

Save raw material (board JSON, benchmark tables, transcript extracts) next to the lane file in `raw/`.

---

## Lane 1: capital

Goal: where the money is going in `<field>` and what it expects back. Funding by stage and by quarter for the last 12 quarters (count by company and round date; de-duplicate re-announced rounds); the ten largest rounds with lead investors; new funds raised to invest in the field; M&A with prices where public; public comparables with revenue multiples and how they moved; shutdowns, down rounds and acqui-hires; government and grant money.

Sources in order: funding databases (public pages and press), fund announcements, acquirer filings for deal prices, listed comparables' filings, shutdown and layoff trackers, grant databases.

Output: a table by quarter (rounds, amount, notable); the ten largest rounds; the comparables table (company, revenue, multiple, change over 24 months); the failures table; ten facts. Every market-size figure carries the firm that published it and who sponsored it.

## Lane 2: labour

Goal: what the field is hiring, and what it has stopped hiring. Pick 15 to 30 named companies across sizes and geographies (`<list>`); pull every open role from each ATS public API where one exists (see sources), else the board page and feed, else aggregator snippets marked 🟡. For each role: title, function, seniority, location, remote or on-site, first-seen date, pay band if shown, the stack and tools named, and the problem the ad describes. Then: counts by function and seniority per company and in total; the roles that appeared in the last six months and the roles that disappeared; evergreen requisitions; the ratio of engineering to management roles; layoffs in the field from trackers with dates and counts; salary bands by role from public sources.

Watch for: a corporate board and a regional board listing the same company; evergreen requisitions; titles that changed meaning (the same title asking for different work than two years ago); ads that describe a problem the company is trying to solve.

Output: the counts table; the new and disappeared roles tables; five ads that matter most, quoted; ten roles that would tell the most if they appeared next; ten facts.

## Lane 3: capability curve

Goal: where the technology line is in `<field>`, how fast it moves, and what one unit of work costs. Releases and their dates for the last 24 months; benchmark results with who ran them (self-reported marked 🟡); published prices per unit (token, inference, robot-hour, device, seat) over time; open-source activity (repositories, stars as a dated fact only, contributors, release cadence); reproducible demonstrations against marketing demonstrations; hardware constraints (compute, sensors, actuators, energy) and their trend.

Sources in order: release notes and model or product cards, third-party benchmark sites, pricing pages and their archived copies, package registries and repository metadata, conference proceedings, teardown and field-test reports.

Output: a dated capability table (date, release, what it can now do, who verified it, mark); a cost-per-unit series; an open-source activity table; ten facts; one 🟡 paragraph on where the line will be at the horizon and why.

## Lane 4: incumbents

Goal: what the five largest players in or next to `<field>` say against what they ship. For each: dated quotes from earnings calls, shareholder letters, keynotes and interviews about the field; against each, what then shipped, was priced, was acquired or was discontinued; adjacent markets they entered; pricing moves; partnerships and exclusivities.

Sources in order: investor relations pages (prepared remarks and transcripts), release notes, developer conference programmes, pricing pages and archived copies, deal announcements.

Output: a says/does table per incumbent (date, who, quote, then what happened, mark); the adjacent-market moves table; ten facts; one 🟡 paragraph on the platform risk this creates for smaller companies and for the roles in lane 2.

## Lane 5: regulation and standards

Goal: the constraints that set the pace in `<field>`. Laws in force and consultations under way in the main markets; safety and technical standards (bodies, versions, dates); procurement rules and certifications buyers require; liability and insurance positions; enforcement actions and court cases with dates; what each constraint does to time-to-market and to which roles it creates (compliance, safety, assurance).

Sources in order: legislation and consultation pages, standards bodies, regulator enforcement pages, court records, insurer and reinsurer publications, procurement frameworks.

Output: a constraints table (constraint, market, status, date, effect, mark); the enforcement list; ten facts; one 🟡 paragraph on timing.

## Lane 6: base rates

Goal: what happened to the same roles and company types in the last three comparable shifts (`<shifts>`, for example the cloud, mobile and the first machine-learning wave, or the field's own precedents). For each shift: the hype peak and the steady state with dates; what happened to the role titles that existed before (kept, renamed, merged, gone); which new titles appeared and when; survival of companies by stage from the peak; time from peak to consolidation; who captured the value (incumbents, new entrants, the picks-and-shovels layer).

Sources in order: histories and retrospectives with data, labour statistics series, funding and failure data for the shift, archived job boards, contemporaneous analyst notes compared with what happened.

Output: one table per shift (what was predicted, what happened, time taken, mark); a roles table across the three shifts; ten facts; the base-rate paragraph that the scenarios must respect or argue with.

## Lane 7: disagreement

Goal: where credible, named people disagree about `<field>`, and what evidence would settle each dispute. Find the three to five live disputes; for each, two or three named people with a record, their position, when they said it, and what they would accept as evidence; dated forecasts with their resolution dates; the quiet consensus nobody argues about.

Sources in order: essays and papers by practitioners and researchers, recorded talks and podcasts, forecasting platforms with dated questions, prediction markets where they exist, the comment threads of the above only for named people.

Output: a disputes table (dispute, position A with name and date, position B with name and date, what would settle it, when); the consensus list; ten facts. No profile pages are opened; a person's public writing and talks are the source.
