#!/usr/bin/env python3
"""Check a brand voice guide against the caps and rules in references/guide-template.md.

Usage:
    python3 check_guide.py voice-guide.md
    python3 check_guide.py voice-guide.md --proof proof-list-2026-10-23.md   # also check the proof list
    python3 check_guide.py voice-guide.md --copy draft.md                     # also check a piece of copy
    python3 check_guide.py voice-guide.md --sheet signoff-sheet-2026-10-23.md # also check the sign-off sheet
    python3 check_guide.py voice-guide.md --sources research/*.md transcript.md  # quotes must be in a source

Exits 1 if any check fails, 0 if it passes (warnings don't fail it, but read them).
Standard library only. Python 3.8 or later.
"""
import argparse
import re
import sys

# Word caps for each section's prose. Table rows don't count.
PROSE_CAPS = {1: 450, 2: 400, 3: 450, 4: 80, 5: 60, 6: 60, 9: 60}
TABLE_CAPS = {3: 20, 5: 15, 6: 15, 7: 25, 9: 30}
FACTS_CAP, DATES_CAP = 40, 15  # section 4.1 and 4.2 table rows
DESC_CAPS = {"Short": 160, "Medium": 300, "Long": 750}
TYPE_OF_WORK_CAP = 70
FACT_WORD_CAP = 25
SAMPLE_PARAGRAPH_CAP = 80
SHEET_ITEMS_CAP, SHEET_ITEM_WORDS = 8, 60
SECTIONS = range(1, 10)
COPY_SECTIONS = (1, 2, 3, 7, 8)  # sections writers copy from: needed facts banned
STATUSES = {"public", "confirmed", "needed"}
PROOF_KINDS = {"award", "credential", "training", "study", "membership", "education"}
VOICE_LABELS = ["We sound like", "We never sound like", "Tone by page", "Sample paragraph"]
# Patterns that read as AI-written (references/examples.md). Warnings only.
AI_PATTERNS = ["peace of mind", "navigate", "tailored", "seamless", "rest assured",
               "don't hesitate to", "when it comes to", "whether you're", "not just"]

NUM = (r"(?:\d+|a|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|fifteen|"
       r"twenty|thirty|forty|fifty|several|many|a few|a couple of)(?:[- ](?:one|two|three|four|five|six|seven|eight|nine))?")
UNIT = r"(?:years?|yrs?|decades?)\b"
# Year counts that go stale: these fail.
YEAR_COUNT_FAIL = re.compile(
    r"\b\d+\s*\+\s*" + UNIT + r"(?!\s+old)"
    r"|\b" + NUM + r"\s+" + UNIT + r"\s+(?:of\s+(?:combined\s+)?(?:experience|service|practice)"
    r"|in\s+(?:business|practice|the\s+(?:trade|industry|business|field))|serving)\b"
    r"|\bdecades\s+of\s+(?:combined\s+)?experience\b"
    r"|\b(?:for|with)\s+(?:over|more\s+than|nearly|almost|well\s+over|close\s+to)\s+" + NUM + r"\s+" + UNIT + r"(?!\s+old)"
    r"|\b(?:serving|served|in\s+business|licensed|operating|practicing|working)\b[^.?!\n]{0,40}?\bfor\s+" + NUM + r"\s+" + UNIT + r"\b"
    r"|\b\d+-year\s+(?:veteran|history|track\s+record|career)\b",
    re.IGNORECASE)
# Softer: may be a count of years in business, may be something else (a panel's age). These warn.
YEAR_COUNT_WARN = re.compile(
    r"\b(?:over|more\s+than|nearly|almost|well\s+over|close\s+to)\s+" + NUM + r"\s+" + UNIT + r"(?!\s+old)"
    r"|\bfor\s+(?:the\s+(?:last|past)\s+)?" + NUM + r"\s+" + UNIT + r"(?!\s+old)",
    re.IGNORECASE)

errors, warnings = [], []


def normalize(text):
    """Curly quotes from Google Docs or Word become straight, so labels and words still match."""
    return (text.replace("\u2018", "'").replace("\u2019", "'")
                .replace("\u201c", '"').replace("\u201d", '"'))


def words(text):
    return [w for w in text.split() if re.search(r"[A-Za-z0-9]", w)]


def split_sections(text):
    sections, current = {}, None
    for line in text.splitlines():
        m = re.match(r"^##\s+(\d)\.\s", line)
        if m:
            current = int(m.group(1))
            sections[current] = []
            continue
        if current is not None:
            sections[current].append(line)
    return sections


def split_subsections(lines):
    """Split section 4 into {'4.1': [...], '4.2': [...]} by its ### headings."""
    subs, current = {}, None
    for line in lines:
        m = re.match(r"^###\s+(\d\.\d)\b", line)
        if m:
            current = m.group(1)
            subs[current] = []
            continue
        if current is not None:
            subs[current].append(line)
    return subs


def table_rows(lines):
    """Return data rows (lists of cells) of every markdown table in lines, minus headers."""
    rows, in_table, header_seen = [], False, False
    for line in lines:
        s = line.strip()
        if s.startswith("|"):
            cells = [c.strip() for c in s.strip("|").split("|")]
            if not in_table:
                in_table, header_seen = True, False
                continue  # header row
            if not header_seen and all(re.fullmatch(r":?-{3,}:?", c) for c in cells if c):
                header_seen = True
                continue
            rows.append(cells)
        else:
            in_table = False
    return rows


def prose(lines):
    return "\n".join(l for l in lines if not l.strip().startswith("|"))


LABEL = r"^\*\*(?:\d+(?:\.\d+)*\s+)?"  # optional number like 1.3 before a bold label


def labeled_line(lines, label):
    """Text after a bold label like **1.1 Who you are.** or **7.2 Short (up to 160 characters):**"""
    for line in lines:
        m = re.match(LABEL + label + r"[^*]*\*\*\s*(.*)$", line.strip())
        if m:
            return m.group(1).strip()
    return None


def labeled_block(lines, label):
    """The labeled line plus the lines under it, up to the next bold label, heading or table."""
    out, on = [], False
    for line in lines:
        s = line.strip()
        m = re.match(LABEL + label + r"[^*]*\*\*\s*(.*)$", s)
        if m and not on:
            on = True
            out.append(m.group(1))
            continue
        if on:
            if re.match(r"^\*\*[^*]+\*\*", s) or s.startswith("#") or s.startswith("|"):
                break
            out.append(s)
    return "\n".join(out).strip() if on else None


def overlaps(m, spans):
    return any(m.start() < e and s < m.end() for s, e in spans)


def year_counts(text):
    """(fails, warns): year counts like 'over 12 years' or '20+ years' that should be dates."""
    hits = list(YEAR_COUNT_FAIL.finditer(text))
    spans = [h.span() for h in hits]
    warns = [m.group(0) for m in YEAR_COUNT_WARN.finditer(text) if not overlaps(m, spans)]
    return [h.group(0) for h in hits], warns


def context_of(text, start, end):
    """'quote' if the match sits inside double quotes, 'question' if its sentence ends with '?'."""
    ls = text.rfind("\n", 0, start) + 1
    le = text.find("\n", end)
    line = text[ls:(len(text) if le == -1 else le)]
    pos = start - ls
    if line[:pos].count('"') % 2 == 1:
        return "quote"
    m = re.search(r"[.!?](?=[\s*\")_]|$)", line[pos:])
    if m and m.group(0) == "?":
        return "question"
    if not m and line.rstrip(" *_#").endswith("?"):
        return "question"
    return None


def check_guide(text):
    if "\u2014" in text:
        errors.append(f"{text.count(chr(0x2014))} em dash(es) found. Rewrite the sentence instead.")
    if "\u2013" in text:
        warnings.append("En dash found. Prefer 'to' for ranges (2004 to 2010).")
    text = normalize(text)

    sections = split_sections(text)
    missing = [n for n in SECTIONS if n not in sections]
    if missing:
        errors.append(f"Missing section(s): {missing}. Keep the template's '## N.' headings.")

    # Prose caps
    total = 0
    for n, lines in sections.items():
        count = len(words(prose(lines)))
        total += count
        cap = PROSE_CAPS.get(n)
        if cap and count > cap:
            errors.append(f"Section {n}: {count} words of prose, cap {cap}.")

    # Table caps
    for n, cap in TABLE_CAPS.items():
        if n in sections:
            rows = table_rows(sections[n])
            if len(rows) > cap:
                errors.append(f"Section {n}: {len(rows)} table rows, cap {cap}.")

    # Ledger (4.1) and dates (4.2)
    ledger, facts_text, dates = {}, {}, {}
    if 4 in sections:
        subs = split_subsections(sections[4])
        fact_lines = subs.get("4.1", sections[4] if not subs else [])
        if "4.1" not in subs:
            errors.append("Section 4: no '### 4.1 Facts' heading.")
        if "4.2" not in subs:
            errors.append("Section 4: no '### 4.2 Dates' heading. Add it, with 'None yet.' if there are no dates.")
        fact_rows = table_rows(fact_lines)
        if len(fact_rows) > FACTS_CAP:
            errors.append(f"Section 4.1: {len(fact_rows)} facts, cap {FACTS_CAP}.")
        for cells in fact_rows:
            if len(cells) < 5:
                errors.append(f"Ledger row has {len(cells)} columns, expected 5: {cells}")
                continue
            fid, fact, source, checked, raw_status = cells[:5]
            m = re.match(r"\W*(public|confirmed|needed)\b", raw_status.lower())
            status = m.group(1) if m else raw_status.lower().strip()
            if not re.fullmatch(r"F\d+", fid):
                errors.append(f"Ledger ID '{fid}' should look like F01.")
            if status not in STATUSES:
                errors.append(f"{fid}: status '{raw_status}' must be public, confirmed or needed.")
            elif raw_status.strip().lower() != status:
                warnings.append(f"{fid}: status '{raw_status}' read as '{status}'. Put notes in the Source column.")
            if len(words(fact)) > FACT_WORD_CAP:
                errors.append(f"{fid}: fact is {len(words(fact))} words, cap {FACT_WORD_CAP}.")
            if not source:
                errors.append(f"{fid}: no source.")
            if not re.search(r"\d{4}-\d{2}-\d{2}", checked):
                warnings.append(f"{fid}: 'Checked' should be a date (YYYY-MM-DD).")
            if status == "confirmed" and "client" not in source.lower():
                warnings.append(f"{fid}: confirmed, but the source doesn't say how the client confirmed it.")
            fails, warns = year_counts(fact)
            for hit in fails:
                errors.append(f"{fid}: '{hit}' is a year count. Anchor it to a date (rule 6) and add a 4.2 row.")
            for hit in warns:
                warnings.append(f"{fid}: '{hit}' may be a year count. If it's time in business, anchor it to a date.")
            ledger[fid] = status
            facts_text[fid] = fact
        if not ledger:
            warnings.append("Section 4: the ledger is empty.")

        date_rows = table_rows(subs.get("4.2", []))
        if len(date_rows) > DATES_CAP:
            errors.append(f"Section 4.2: {len(date_rows)} dates, cap {DATES_CAP}.")
        for cells in date_rows:
            if len(cells) < 4:
                errors.append(f"Dates row has {len(cells)} columns, expected 4: {cells}")
                continue
            label, date, written, fid = cells[:4]
            if not re.fullmatch(r"\d{4}(?:-\d{2}(?:-\d{2})?)?", date):
                errors.append(f"4.2 '{label}': '{date}' should be YYYY, YYYY-MM or YYYY-MM-DD, the one format.")
                continue
            if fid not in ledger:
                errors.append(f"4.2 '{label}' cites {fid}, which isn't in 4.1.")
                continue
            if ledger[fid] == "needed":
                errors.append(f"4.2 '{label}' uses {fid}, a needed fact. Dates rows must be public or confirmed; "
                              "the date stays on the sign-off sheet until confirmed.")
            if date[:4] not in facts_text.get(fid, ""):
                errors.append(f"4.2 '{label}' says {date[:4]}, but {fid}'s wording in 4.1 doesn't. One date per fact.")
            if date[:4] not in written:
                warnings.append(f"4.2 '{label}': 'Written in copy as' doesn't show the year {date[:4]}.")
            if any(year_counts(written)):
                errors.append(f"4.2 '{label}': '{written}' is a count. Write it from the date ('since {date[:4]}').")
            dates.setdefault(fid, set()).add(date)
        for fid, fact in facts_text.items():
            if ledger.get(fid) in ("public", "confirmed") and re.search(r"\bsince\s+(?:19|20)\d{2}\b", fact) and fid not in dates:
                warnings.append(f"{fid} has a 'since' year but no row in 4.2 dates.")

    # Fact IDs cited: needed facts banned from copy sections, unknown IDs flagged
    needed = {fid for fid, st in ledger.items() if st == "needed"}
    for n, lines in sections.items():
        if n == 4:
            continue
        cited = set(re.findall(r"\bF\d+\b", "\n".join(lines)))
        for fid in sorted(cited - set(ledger)):
            errors.append(f"Section {n} cites {fid}, which isn't in the ledger.")
        bad = sorted(cited & needed)
        if bad and n in COPY_SECTIONS:
            errors.append(f"Section {n} uses needed fact(s) {bad}. Writers may use public or confirmed facts only.")
        elif bad and n == 6:
            warnings.append(f"Section 6 plans answers with needed fact(s) {bad}. Confirm them before writing.")

    # Page 1 shows the voice, and section 3 has the voice slots
    s1, s3 = sections.get(1, []), sections.get(3, [])
    sound = labeled_line(s1, "How we'll sound")
    if sound is None:
        errors.append("Section 1: no **1.3 How we'll sound.** line. Page 1 must show the voice the client approves.")
    else:
        sample = re.search(r'"([^"]{10,})"', sound)
        if not sample:
            errors.append("Section 1, 1.3: no sample line in quotation marks. Copy one Do line from 3.4.")
        elif sample.group(1) not in "\n".join(s3):
            warnings.append("Section 1, 1.3: the sample line isn't word for word in section 3. Copy a Do line exactly.")
    for label in VOICE_LABELS:
        if 3 in sections and labeled_line(s3, label) is None:
            errors.append(f"Section 3: no **{label}.** line. Keep it, with 'None yet.' if it doesn't apply.")
    para = labeled_block(s3, "Sample paragraph")
    if para and len(words(para)) > SAMPLE_PARAGRAPH_CAP:
        errors.append(f"Section 3, sample paragraph: {len(words(para))} words, cap {SAMPLE_PARAGRAPH_CAP}.")

    # Descriptions
    if 7 in sections:
        desc = {k: labeled_line(sections[7], k) for k in DESC_CAPS}
        for k, cap in DESC_CAPS.items():
            d = desc[k]
            if d is None:
                errors.append(f"Section 7: no **{k} ...:** description found.")
            elif len(d) > cap:
                errors.append(f"Section 7: {k} description is {len(d)} characters, cap {cap}.")
        if desc["Short"] and desc["Medium"] and not desc["Medium"].startswith(desc["Short"]):
            errors.append("Section 7: the medium description must start with the short one, word for word.")
        if desc["Medium"] and desc["Long"] and not desc["Long"].startswith(desc["Medium"]):
            errors.append("Section 7: the long description must start with the medium one, word for word.")
        who = labeled_line(s1, "Who you are")
        if who is None:
            errors.append("Section 1: no **1.1 Who you are.** line found.")
        elif desc["Short"] and who != desc["Short"]:
            errors.append("Section 1 'Who you are' must match the section 7 short description exactly.")

    # Year counts in the lines that go into copy word for word
    verbatim = {"1.1": labeled_line(s1, "Who you are"), "1.3": sound,
                "1.4": labeled_block(s1, "What we'll lead with"), "3.9": para}
    for k in DESC_CAPS:
        verbatim["7 " + k] = labeled_line(sections.get(7, []), k)
    for where, t in verbatim.items():
        if not t:
            continue
        fails, warns = year_counts(t)
        for hit in fails:
            errors.append(f"{where}: '{hit}' is a year count. Use the date from 4.2.")
        for hit in warns:
            warnings.append(f"{where}: '{hit}' may be a year count. If it's time in business, use the date from 4.2.")

    # By type of work: count the whole block under each label
    if 8 in sections:
        for line in sections[8]:
            m = re.match(r"^\*\*([^*]+)\*\*", line.strip())
            if m:
                label = re.sub(r"^\d+(?:\.\d+)*\s+", "", m.group(1)).strip(" .:")
                block = labeled_block(sections[8], re.escape(label)) or ""
                if len(words(block)) > TYPE_OF_WORK_CAP:
                    errors.append(f"Section 8 '{label}': {len(words(block))} words, cap {TYPE_OF_WORK_CAP}.")

    # The lines writers copy (1.3, Do lines, 3.9, descriptions) must not use the never-use words themselves
    terms = never_use_list(sections)
    samples = {"1.3": sound, "3.9": para}
    for i, do in enumerate(re.findall(r'Do: "([^"]+)"', labeled_block(s3, "Rules") or ""), 1):
        samples[f"3.4 Do line {i}"] = do
    for k in DESC_CAPS:
        samples["7 " + k] = labeled_line(sections.get(7, []), k)
    for where, t in samples.items():
        if t:
            for term, allowed in never_use_hits(t, terms, fact_spans(t, ledger, facts_text)):
                if not allowed:
                    errors.append(f"{where} uses '{term}', which is on the 1.6 never-use list. Writers copy these lines.")

    # Leftover template placeholders
    placeholders = [
        p for p in re.findall(r"\[[^\]\n]{2,}\](?!\()", text)
        if not re.fullmatch(r"\[(?:[FCQ]\d+[,;\s]*(?:and\s+)?)+\]", p)  # bracketed IDs are citations, not placeholders
    ]
    if placeholders:
        sample = ", ".join(sorted(set(placeholders))[:5])
        warnings.append(f"{len(placeholders)} bracketed placeholder(s) left, e.g. {sample}")

    version = re.search(r"^Version\s+(\d+(?:\.\d+)*)", text, re.MULTILINE)
    return sections, total, ledger, facts_text, dates, (version.group(1) if version else None)


def never_use_list(sections):
    lines = sections.get(1, [])
    line = labeled_line(lines, "Words we'll never use")
    if line is None:
        return []
    if not line.strip(" ."):  # the words are listed as bullets under the label
        block = labeled_block(lines, "Words we'll never use") or ""
        line = ", ".join(l.lstrip("-* ").strip() for l in block.splitlines() if l.strip())
    items = re.split(r"[;,]", line.rstrip("."))
    return [i.strip().strip("\"'").strip() for i in items if i.strip()]


def words_table_not(sections):
    rows = table_rows(sections.get(3, []))
    return [r[1].strip("\"' ") for r in rows if len(r) > 1 and r[1].strip("\"' ") and not r[1].startswith("[")]


def find(term, copy):
    return list(re.finditer(r"(?<!\w)" + re.escape(term) + r"(?!\w)", copy, re.IGNORECASE))


def fact_spans(text, ledger, facts_text):
    """Where a public or confirmed fact appears word for word, e.g. an award named 'Best of [City]'."""
    spans = []
    for fid, fact in facts_text.items():
        if ledger.get(fid) in ("public", "confirmed") and fact.strip(" ."):
            spans += [m.span() for m in re.finditer(re.escape(fact.strip(" .")), text, re.IGNORECASE)]
    return spans


def never_use_hits(text, terms, spans):
    """[(term, None)] for a claim, [(term, 'question' / 'quote' / 'ledger fact')] for an allowed use."""
    out = []
    for term in terms:
        hits = find(term, text)
        if not hits:
            continue
        bad = [m for m in hits if not overlaps(m, spans) and not context_of(text, m.start(), m.end())]
        if bad:
            out.append((term, None))
        else:
            m = hits[0]
            out.append((term, "ledger fact" if overlaps(m, spans) else context_of(text, m.start(), m.end())))
    return out


def check_copy(path, sections, ledger, facts_text, dates):
    raw = open(path, encoding="utf-8").read()
    if "\u2014" in raw:
        errors.append(f"{path}: {raw.count(chr(0x2014))} em dash(es).")
    if "\u2013" in raw:
        warnings.append(f"{path}: en dash found. Prefer 'to' for ranges.")
    copy = normalize(raw)

    terms = never_use_list(sections)
    if not terms:
        errors.append("Page 1 has no 'Words we'll never use' line in the template's format, "
                      "so the copy was not checked for those words.")
    for term, allowed in never_use_hits(copy, terms, fact_spans(copy, ledger, facts_text)):
        if allowed == "ledger fact":
            warnings.append(f"{path}: '{term}' is on the never-use list, but here it's part of a ledger fact's exact wording.")
        elif allowed:
            warnings.append(f"{path}: '{term}' is on the never-use list, used inside a {allowed}. "
                            "Fine as the shopper's phrase; never as a claim about the client.")
        else:
            errors.append(f"{path}: uses '{term}', which is on the never-use list.")

    for term in words_table_not(sections):
        if term.lower() not in [t.lower() for t in terms] and find(term, copy):
            warnings.append(f"{path}: uses '{term}', which the 3.7 Words table says not to use.")

    for m in YEAR_COUNT_FAIL.finditer(copy):
        if context_of(copy, m.start(), m.end()) == "quote":
            warnings.append(f"{path}: '{m.group(0)}' is a year count inside a quote. Keep it only if it's verbatim.")
        else:
            errors.append(f"{path}: '{m.group(0)}' is a year count. Use the date from 4.2 ('since 2014').")
    spans = [m.span() for m in YEAR_COUNT_FAIL.finditer(copy)]
    for m in YEAR_COUNT_WARN.finditer(copy):
        if not overlaps(m, spans):
            warnings.append(f"{path}: '{m.group(0)}' may be a year count. If it's time in business, use the date.")

    # Claim check, years only: every year in the copy should trace to a public or confirmed fact.
    usable = " ".join(t for f, t in facts_text.items() if ledger.get(f) in ("public", "confirmed"))
    unusable = " ".join(t for f, t in facts_text.items() if ledger.get(f) == "needed")
    for year in sorted(set(re.findall(r"\b(?:19|20)\d{2}\b", copy))):
        if year in usable:
            continue
        if year in unusable:
            errors.append(f"{path}: {year} appears only in a needed fact. It stays out of copy until confirmed.")
        else:
            warnings.append(f"{path}: {year} isn't in any ledger fact. Check the claim against the ledger.")

    for phrase in AI_PATTERNS:
        if find(phrase, copy):
            warnings.append(f"{path}: '{phrase}' reads as AI-written (examples.md). Cut it unless it's needed.")


def check_proof(path, ledger, facts_text, dates, version):
    raw = open(path, encoding="utf-8").read()
    if "\u2014" in raw:
        errors.append(f"{path}: {raw.count(chr(0x2014))} em dash(es).")
    text = normalize(raw)
    m = re.search(r"version\s+(\d+(?:\.\d+)*)", text, re.IGNORECASE)
    if version and (not m or m.group(1) != version):
        warnings.append(f"{path}: doesn't say it was generated from guide version {version}. Regenerate it.")
    rows = table_rows(text.splitlines())
    if not rows:
        errors.append(f"{path}: no proof table found.")
    for cells in rows:
        if len(cells) < 8:
            errors.append(f"{path}: row has {len(cells)} columns, expected 8: {cells}")
            continue
        fid, kind, proof, issuer, date, source, status, use = cells[:8]
        if fid not in ledger:
            errors.append(f"{path}: {fid} isn't in the guide's ledger.")
            continue
        if kind.lower() not in PROOF_KINDS:
            warnings.append(f"{path}: {fid} kind '{kind}' isn't one of {sorted(PROOF_KINDS)}.")
        if proof.strip("\"' ") != facts_text[fid].strip("\"' "):
            errors.append(f"{path}: {fid} wording doesn't match the ledger word for word. Regenerate it.")
        st = re.match(r"\W*(public|confirmed|needed)\b", status.lower())
        if not st or st.group(1) != ledger[fid]:
            errors.append(f"{path}: {fid} status '{status}' doesn't match the ledger ('{ledger[fid]}').")
        if fid in dates and date not in dates[fid]:
            errors.append(f"{path}: {fid} date '{date}' doesn't match 4.2 ({', '.join(sorted(dates[fid]))}).")
        if not source:
            errors.append(f"{path}: {fid} has no source.")


def squash(text):
    return re.sub(r"\s+", " ", normalize(text)).strip()


def check_sources(paths, sections):
    """Every quoted phrase in 2.2 and 3.6 must appear word for word in a source file (rule 3)."""
    corpus = " ".join(squash(open(p, encoding="utf-8").read()) for p in paths)
    for n, label in ((2, "In their words"), (3, "In their own words")):
        block = labeled_block(sections.get(n, []), label) or ""
        for q in re.findall(r'"([^"]{3,})"', normalize(block)):
            if squash(q) not in corpus:
                errors.append(f"Section {n}, '{label}': \"{q}\" isn't word for word in any source given. "
                              "Quote only what's in a transcript or source.")


def check_sheet(path, sections):
    raw = open(path, encoding="utf-8").read()
    if "\u2014" in raw:
        errors.append(f"{path}: {raw.count(chr(0x2014))} em dash(es).")
    items, current = [], None
    for line in normalize(raw).splitlines():
        if re.match(r"^\s{0,3}\d+\.\s+\S", line):
            current = [line]
            items.append(current)
        elif current is not None and line.strip():
            current.append(line)
    if not items:
        errors.append(f"{path}: no numbered items found.")
    if len(items) > SHEET_ITEMS_CAP:
        errors.append(f"{path}: {len(items)} items, cap {SHEET_ITEMS_CAP}. Turn the rest into defaults.")
    for i, item in enumerate(items, 1):
        body = " ".join(item)
        n = len(words(body))
        if n > SHEET_ITEM_WORDS:
            errors.append(f"{path}: item {i} is {n} words, cap {SHEET_ITEM_WORDS}.")
        if "We'd write:" not in body:
            errors.append(f"{path}: item {i} has no \"We'd write:\" draft. Draft, don't ask.")
        if "Needed for:" not in body:
            errors.append(f"{path}: item {i} has no \"Needed for:\" line.")
    listed = re.search(r"(\d+)\s+items?\b", labeled_line(sections.get(1, []), "Facts we need you to confirm") or "")
    if listed and int(listed.group(1)) != len(items):
        errors.append(f"Section 1.7 says {listed.group(1)} items, but {path} has {len(items)}.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("guide")
    ap.add_argument("--copy", help="a draft to check against the guide's never-use list, dates and ledger")
    ap.add_argument("--proof", help="the proof list export to check against the ledger")
    ap.add_argument("--sheet", help="the sign-off sheet to check against its caps and page 1")
    ap.add_argument("--sources", nargs="+", help="transcripts and research files that quotes in 2.2 and 3.6 must come from")
    args = ap.parse_args()

    text = open(args.guide, encoding="utf-8").read()
    sections, total, ledger, facts_text, dates, version = check_guide(text)
    if args.proof:
        check_proof(args.proof, ledger, facts_text, dates, version)
    if args.copy:
        check_copy(args.copy, sections, ledger, facts_text, dates)
    if args.sheet:
        check_sheet(args.sheet, sections)
    if args.sources:
        check_sources(args.sources, sections)
    elif not args.copy and any(re.search(r'"[^"]{3,}"', labeled_block(sections.get(n, []), l) or "")
             for n, l in ((2, "In their words"), (3, "In their own words"))):
        warnings.append("Quotes in 2.2 or 3.6 weren't checked against a source. Add --sources with the transcripts and research files.")

    print(f"Guide: {args.guide}")
    print(f"Prose words (tables excluded): {total}")
    for n in sorted(sections):
        print(f"  Section {n}: {len(words(prose(sections[n])))} words, {len(table_rows(sections[n]))} table rows")
    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"FAIL  {e}")
    print("PASS" if not errors else f"FAILED: {len(errors)} problem(s)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
