# Output specification

The layout is fixed. A reader who has seen one Field Read note can find anything in the next one without reading it through, and a script can check that nothing was dropped. Do not reorder, rename, merge or omit sections. Where a section has nothing, write the heading and one line: "Not found after looking at <what was looked at>."

Run `python3 scripts/check_read.py <note.md>` before finishing. It fails on a missing or misordered section, a ✅ without evidence, a dangling or unused footnote, a missing header line, a scenario without a killing signal, or a comparison without the criteria table.

## 1. File and header

File name: `YYYY-MM-DD-<field>-<lens>.md` for one field, `YYYY-MM-DD-<field-a>-vs-<field-b>-<lens>.md` for a comparison; lens one of `career`, `build`, `invest`, `position`. Lane files sit beside it as `lane-1-capital.md` through `lane-7-disagreement.md` (with `-A`, `-B` suffixes in a comparison), raw material in `raw/`.

Every note starts with exactly these lines (a YAML front matter block before them is allowed for notes kept in a vault; the checker skips it):

```
# <Title in sentence case>

Read on <D Month YYYY>. Horizon <n> years. Public record only. No LinkedIn profile was opened.
Legend: ✅ cited to a source read that day and linked; 🟡 inferred from the record, or from a snippet that could not be opened; ❔ not found after looking.
Sources: <N> footnotes across <L> lanes.
```

A comparison adds one line after the horizon line: `Fields: A = <field a>; B = <field b>. Depth: equal.` (or `Depth: A fuller than B, because <reason>.`).

The title names the field and the question, never the lens word: "Software engineering leadership as coding agents mature: a field read", not "Career read".

## 2. Marks and citations

- Every sentence that states a fact about the field ends with a mark. A paragraph of facts carries a mark per sentence, not one at the end.
- ✅ is always followed by its evidence: an inline link `([short label](url))`, a footnote `[^s<lane>-<n>]`, or both. Both for a number that matters. A ✅ with neither is an error.
- 🟡 carries its reasoning in the same sentence or names the ✅ facts it rests on. Probabilities are ranges, marked 🟡.
- ❔ says what was looked at.
- Footnote ids are `s<lane>-<n>` for one field and `<A|B|C>s<lane>-<n>` for a comparison: `[^Bs2-4]` is the fourth source in lane 2 for field B. Footnotes are defined in "Sources by lane", grouped under a heading per lane (and per field), in id order, each as `[^s1-4]: <what it is, date> <url>`.
- A number is never bare. Amount, count, date, multiple, percentage: each carries a mark and a source. A market-size figure also names who published it and who paid for it.
- Quotes are verbatim, in double quotes, with speaker, occasion and date.
- Dates are `D Month YYYY` in prose and `YYYY-MM-DD` in tables.

## 3. Skeleton A: one field

```
## 1. The answer in one paragraph
## 2. Where the field is today
### 2a. Capital
### 2b. Labour
### 2c. The capability curve
### 2d. Incumbents, says and does
### 2e. Regulation and standards
## 3. The base rate
## 4. Three scenarios, dated
### 4a. Base
### 4b. Fast
### 4c. Stall
## 5. Roles and company types
### 5a. Ten that gain
### 5b. Ten that lose
## 6. Where credible people disagree
## 7. What it means for the reader
## 8. Signals to watch, dated
## 9. Sources by lane
```

Fixed tables, exact columns:

- §2a: `Quarter | Rounds | Amount | Notable | Mark`, last 12 quarters; then `Company | Revenue | Multiple | Change over 24 months | Mark` for listed comparables.
- §2b: `Company | Open roles | Engineering | Management | Product | Operations | Other | Locations | Board read on`; then `Role | Appeared or disappeared | Since | Evidence | Mark`.
- §2c: `Date | Release | What it can now do | Verified by | Mark`; then `Unit | Cost then | Cost now | Dates | Mark`.
- §2d: `Date | Who, where | Quote | Then what happened | Mark`.
- §2e: `Constraint | Market | Status | Date | Effect on timing | Mark`.
- §3: one table per shift, `What was predicted | What happened | Time taken | Mark`; then `Role before | Outcome (kept, renamed, merged, gone) | New role | Shift | Mark`; then the base-rate paragraph.
- §4a to §4c: each a short narrative, then `Probability (range) 🟡: <range>, because <one line>`, then `Confirming signals: <signal>, visible by <date>; <signal>, visible by <date>`, then `Killing signal: <signal>`.
- §5a and §5b: numbered lists of ten, each "Role or company type: why, and which lane says so."
- §6: `Dispute | Position A (who, when) | Position B (who, when) | What would settle it | When`.
- §7: exists in the working copy only; the shareable copy keeps the heading with "Removed from the shareable copy." For the career lens it ends with the three questions the reader should be able to answer before moving.
- §8: `Signal | Where to check | By | Confirms scenario | Mark`, every row dated inside the horizon.

## 4. Skeleton B: a comparison of two or three fields

```
## 1. The answer in one paragraph
## 2. The criteria
## 3. The fields today, side by side
### 3a. Capital
### 3b. Labour
### 3c. The capability curve
### 3d. Incumbents, says and does
### 3e. Regulation and standards
## 4. The base rates
## 5. Scenarios, per field
### 5a. <Field A>
### 5b. <Field B>
## 6. Roles and company types, side by side
## 7. The criteria table
## 8. Switching cost and option value
## 9. Where credible people disagree
## 10. What it means for the reader
## 11. Decision points, dated
## 12. Sources by lane and field
```

Fixed tables, exact columns:

- §2: `# | Criterion | How it is measured | Weight (reader's own) | Written on`; five to eight rows, written before the lanes run, with the date. The weights are the reader's and are marked as such; the note never invents them.
- §3a to §3e: the same tables as Skeleton A §2a to §2e, with one column block per field, or two tables stacked with the field named in the caption. Equal depth is the rule; where a side is thinner, say so in the row.
- §4: the Skeleton A §3 tables once per field, then one paragraph that says whether the two fields are in the same phase of their shift.
- §5a, §5b: three scenarios per field as in Skeleton A §4, each with probability range, confirming signals dated, killing signal.
- §6: `Role or company type | Field A: gains or loses | Field B: gains or loses | Why | Mark`.
- §7: `Criterion | <Field A> | <Field B> | Which wins | Mark`; one row per criterion from §2; each cell carries a mark and rests on a lane; the "Which wins" column may say "turns on <signal>" instead of a name.
- §8: four fixed paragraphs headed `Cost of moving A to B`, `Cost of moving B to A`, `Option value kept by each`, `Sequencing`; each 🟡 with the facts it rests on.
- §10: as Skeleton A §7, plus the three questions.
- §11: `Date | What becomes known | Which criterion it settles | Source`.

## 5. Things the checker looks for

- The header lines, including the horizon and, for a comparison, the fields line.
- Every section of the skeleton, in order.
- Each scenario has a `Probability (range)` line, at least two `visible by` dates and one `Killing signal` line.
- The criteria table has one row per criterion in §2.
- Every ✅ has a link or footnote on the same line; every footnote used is defined and every footnote defined is used; ids match the lane pattern; the header counts are true.
- Figures on a line with no mark are warned.
- Quotes without a year on the line are warned.
- A single-field read usually needs 50 or more footnotes across six or more lanes; a comparison, 80 or more across both fields. Fewer is a warning, not a failure.
