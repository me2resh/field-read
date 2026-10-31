#!/usr/bin/env python3
"""Check a Field Read note against the output specification (references/outputs.md).

Usage: python3 check_read.py <note.md> [--shape field|compare]
The shape is inferred from the file name when not given ("-vs-" means a comparison). Exit 1 on any failure.
"""
import re, sys, pathlib

FIELD = ["1. The answer in one paragraph", "2. Where the field is today", "2a. Capital", "2b. Labour",
         "2c. The capability curve", "2d. Incumbents, says and does", "2e. Regulation and standards",
         "3. The base rate", "4. Three scenarios, dated", "4a. Base", "4b. Fast", "4c. Stall",
         "5. Roles and company types", "5a. Ten that gain", "5b. Ten that lose",
         "6. Where credible people disagree", "7. What it means for the reader", "8. Signals to watch, dated",
         "9. Sources by lane"]
COMPARE = ["1. The answer in one paragraph", "2. The criteria", "3. The fields today, side by side", "3a. Capital",
           "3b. Labour", "3c. The capability curve", "3d. Incumbents, says and does", "3e. Regulation and standards",
           "4. The base rates", "5. Scenarios, per field", "5a.", "5b.", "6. Roles and company types, side by side",
           "7. The criteria table", "8. Switching cost and option value", "9. Where credible people disagree",
           "10. What it means for the reader", "11. Decision points, dated", "12. Sources by lane and field"]
MARKS = "✅🟡❔"


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__); sys.exit(2)
    path = pathlib.Path(args[0]); text = path.read_text(encoding="utf-8")
    fm = re.match(r"^---\n.*?\n---\n", text, re.S)
    if fm: text = text[fm.end():].lstrip("\n")
    shape = sys.argv[sys.argv.index("--shape") + 1] if "--shape" in sys.argv else ("compare" if "-vs-" in path.name else "field")
    fails, warns = [], []
    lines = text.splitlines()

    # header
    if not lines or not lines[0].startswith("# "): fails.append("line 1 must be the title '# ...'")
    head = "\n".join(lines[:10])
    if not re.search(r"^Read on \d{1,2} [A-Z][a-z]+ \d{4}\. Horizon \d+ years?\. Public record only\. No LinkedIn profile was opened\.", head, re.M):
        fails.append("header line missing: 'Read on D Month YYYY. Horizon N years. Public record only. No LinkedIn profile was opened.'")
    if "Legend: ✅" not in head: fails.append("header legend line missing")
    msrc = re.search(r"^Sources: (\d+) footnotes across (\d+) lanes\.", head, re.M)
    if not msrc: fails.append("header line missing: 'Sources: N footnotes across L lanes.'")
    if shape == "compare" and not re.search(r"^Fields: A = .+; B = .+\. Depth: ", head, re.M):
        fails.append("comparison header line missing: 'Fields: A = ...; B = .... Depth: equal.' (or the reason it is not)")

    # sections
    heads = [re.sub(r"^#+\s*", "", l).strip() for l in lines if re.match(r"^##+ ", l)]
    want = COMPARE if shape == "compare" else FIELD
    pos = -1
    for w in want:
        try:
            i = next(i for i, h in enumerate(heads) if h.startswith(w) or h == w)
        except StopIteration:
            fails.append(f"section missing: '{w}'"); continue
        if i < pos: fails.append(f"section out of order: '{w}'")
        pos = max(pos, i)

    # scenarios: probability range, dated confirming signals, a killing signal
    scen_heads = [i for i, l in enumerate(lines) if re.match(r"^###\s+(4[abc]\.|5[ab]\.)", l)]
    for n, start in enumerate(scen_heads):
        end = scen_heads[n + 1] if n + 1 < len(scen_heads) else next((i for i in range(start + 1, len(lines)) if re.match(r"^## ", lines[i])), len(lines))
        block = "\n".join(lines[start:end])
        if shape == "field" or re.match(r"^###\s+5[ab]\.", lines[start]):
            probs = len(re.findall(r"Probability \(range\)", block)); kills = len(re.findall(r"Killing signal:", block)); dates = len(re.findall(r"visible by \d", block))
            need = 3 if shape == "compare" else 1
            if probs < need: fails.append(f"'{lines[start].strip()}': {probs} 'Probability (range)' line(s), need {need}")
            if kills < need: fails.append(f"'{lines[start].strip()}': {kills} 'Killing signal:' line(s), need {need}")
            if dates < 2 * need: warns.append(f"'{lines[start].strip()}': only {dates} 'visible by <date>' signals")

    # comparison: criteria rows reappear in the criteria table
    if shape == "compare":
        def rows(after):
            try: s = next(i for i, l in enumerate(lines) if re.match(r"^## " + re.escape(after), l))
            except StopIteration: return []
            out = []
            for l in lines[s + 1:]:
                if l.startswith("## "): break
                if l.startswith("|") and not re.match(r"^\|\s*-", l) and not re.match(r"^\|\s*#", l) and "Criterion" not in l: out.append(l)
            return out
        c2, c7 = rows("2. The criteria"), rows("7. The criteria table")
        if c2 and c7 and len(c7) < len(c2): fails.append(f"criteria table has {len(c7)} rows, the criteria section lists {len(c2)}")
        if c2 and not (5 <= len(c2) <= 8): warns.append(f"{len(c2)} criteria; five to eight is the rule")

    # footnotes
    defined = set(re.findall(r"^\[\^([A-C]?s\d+-\d+)\]:", text, re.M))
    used = set(re.findall(r"\[\^([A-C]?s\d+-\d+)\](?!:)", text))
    bad_ids = [f for f in defined | used if not re.match(r"[A-C]?s[1-7]-\d+$", f)]
    for f in sorted(used - defined): fails.append(f"footnote used but not defined: [^{f}]")
    for f in sorted(defined - used): warns.append(f"footnote defined but never used: [^{f}]")
    for f in bad_ids: fails.append(f"footnote id not of the form [A|B|C]s<lane>-<n>: {f}")
    lanes = {re.sub(r"^[A-C]", "", f).split("-")[0] for f in defined}
    if msrc:
        n, l = int(msrc.group(1)), int(msrc.group(2))
        if n != len(defined): fails.append(f"header says {n} footnotes, note defines {len(defined)}")
        if l != len(lanes): fails.append(f"header says {l} lanes, footnotes span {len(lanes)}")

    # marks
    in_sources = False
    for i, l in enumerate(lines, 1):
        if re.match(r"^## .*Sources by lane", l): in_sources = True
        if in_sources or l.startswith("#") or l.startswith("Legend:") or not l.strip(): continue
        for m in re.finditer("✅", l):
            tail = l[m.end():m.end() + 160]
            if not re.search(r"\]\(https?://|\[\^[A-C]?s\d+-\d+\]", tail):
                fails.append(f"line {i}: ✅ without a link or footnote after it")
        if re.search(r"(£|\$|€|GBP|USD|EUR)\s?\d|\d+(\.\d+)?x\b|\d+%", l) and not any(c in l for c in MARKS) \
           and not l.startswith("|--") and "not public" not in l.lower():
            warns.append(f"line {i}: a figure with no mark on the line")
        if re.search(r"\"[^\"]{12,}\"", l) and not re.search(r"\d{4}", l):
            warns.append(f"line {i}: a quote without a year on the line")

    floor = 80 if shape == "compare" else 50
    if len(defined) < floor:
        missing = sorted({"s1", "s2", "s3", "s4", "s5", "s6", "s7"} - lanes)
        warns.append(f"only {len(defined)} footnotes; a {shape} read usually needs {floor} or more" + (f"; lanes with no sources: {', '.join(missing)}" if missing else ""))
    for w in warns: print("warn:", w)
    for f in fails: print("FAIL:", f)
    print(f"{path.name}: {shape}, {len(defined)} footnotes, {len(lanes)} lanes, {len(fails)} failures, {len(warns)} warnings")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
