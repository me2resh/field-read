# Sources, endpoints and fallbacks

What worked, by lane. Mark anything that comes from a snippet rather than an opened page as 🟡. Cold Read's `references/sources.md` holds the filing, registry, ATS and infrastructure endpoints in more detail; this file adds what a field read needs on top.

## Lane 1: capital

| Source | Use | Notes |
|---|---|---|
| Funding databases (public company pages, press releases, VC portfolio pages, startup press) | Rounds, dates, leads | Count by company and round date; re-announced rounds double-count |
| Acquirer filings (10-K, 10-Q, 8-K, annual reports, RNS) | Deal prices and allocations | The release says "undisclosed"; the filing two months later often does not |
| Listed comparables' filings and investor pages | Revenue, multiples, guidance | Multiples from a public pricing page carry the date of the price |
| Fund announcements and regulatory filings (Form D, LP letters where public) | New money aimed at the field | A fund is intent, not deployment |
| Shutdown and layoff trackers; "post-mortem" lists | Failures by stage | Cross-check at least one with press |
| Grant databases (CORDIS, UKRI, NSF, SBIR, national equivalents) | Public money and stated future segments | Grant abstracts name markets a company has not announced |

## Lane 2: labour

| Source | Use | Notes |
|---|---|---|
| ATS public APIs: Ashby `api.ashbyhq.com/posting-api/job-board/<org>`, Greenhouse `boards-api.greenhouse.io/v1/boards/<org>/jobs?content=true`, Lever `api.lever.co/v0/postings/<org>?mode=json`, Workable `apply.workable.com/api/v3/accounts/<org>/jobs` (POST), Teamtailor `<careers domain>/jobs.rss`, Personio `<org>.jobs.personio.de/xml`, SmartRecruiters `api.smartrecruiters.com/v1/companies/<org>/postings` | Role counts, first-published dates, pay bands, full text | Careers pages often return 403 to scripts; the ATS endpoint does not |
| Layoff trackers | Dates and counts by company | Mark the tracker's own sourcing |
| Government labour statistics (ONS, BLS, Eurostat, national equivalents) | Occupation counts and pay over time | The series lag a year or more; use them for the base rate, not the latest quarter |
| Salary aggregators and levelling sites | Bands by role | 🟡 unless the page opens; self-reported |
| Archived careers pages (web.archive.org CDX: `web.archive.org/cdx/search/cdx?url=<domain>/careers*&output=json&filter=statuscode:200`) | Roles that disappeared | Fetch one copy per quarter |

## Lane 3: capability curve

| Source | Use | Notes |
|---|---|---|
| Release notes, model and product cards | Dated capability claims | Self-reported until a third party verifies |
| Third-party benchmark and leaderboard sites | Verified results | Record who ran it and when; benchmarks saturate and get gamed |
| Pricing pages and their archived copies | Cost per unit over time | Price is the cleanest capability signal there is |
| Package registries and repository metadata (download counts, release cadence, contributors) | Open-source activity | Stars are a dated fact, not a trend, unless the series is pulled |
| Conference proceedings and preprint servers | What is coming | A paper is 12 to 24 months ahead of a product, when it arrives at all |
| Field tests, teardowns, incident reports | What works outside the demo | The best antidote to a keynote |

## Lane 4: incumbents

| Source | Use | Notes |
|---|---|---|
| Investor relations: prepared remarks, transcripts, shareholder letters | What they say | The company's own site usually hosts the webcast when transcripts are paywalled |
| Release notes and changelogs | What they ship | Date each entry |
| Developer conference programmes and recordings | Direction a year out | Session titles are a plan |
| Pricing pages, archived | Moves into or out of a market | A price cut is a strategy statement |
| Deal announcements and filings | Adjacent-market entry | |

## Lane 5: regulation and standards

| Source | Use | Notes |
|---|---|---|
| Legislation and consultation pages (EU, UK, US federal and state, national regulators) | What is in force and what is coming, with dates | Consultations give the timetable |
| Standards bodies (ISO, IEC, IEEE, NIST, ETSI, sector bodies) | Versions, dates, what buyers will require | A standard's date decides procurement cycles |
| Regulator enforcement pages and court records | The climate | Enforcement lags law by two to four years |
| Insurer and reinsurer publications | Liability positions | Insurers price the risk before regulators rule on it |
| Procurement frameworks and certification schemes | What a buyer can buy | |

## Lane 6: base rates

| Source | Use | Notes |
|---|---|---|
| Data-rich histories and retrospectives of past shifts | What happened, when | Prefer ones with tables to ones with stories |
| Labour statistics series across the shift | Role counts before and after | |
| Funding and failure data for the shift | Survival by stage | |
| Archived job boards from the shift's peak | Titles that existed then | |
| Contemporaneous analyst notes | What was predicted | Compare with what happened; this is the base rate for analysts too |

## Lane 7: disagreement

| Source | Use | Notes |
|---|---|---|
| Essays, papers, newsletters by practitioners and researchers with a record | Named positions with dates | Record the position, not the person's popularity |
| Recorded talks and podcasts | Positions in their own words | Transcripts where available |
| Forecasting platforms and prediction markets with dated questions | Resolution dates and community estimates | A market is a 🟡 source with a date |
| Public comment threads | Only for named people with a record | Never the crowd |

Never open a LinkedIn profile for this work. Snippets from search are acceptable and marked 🟡.
