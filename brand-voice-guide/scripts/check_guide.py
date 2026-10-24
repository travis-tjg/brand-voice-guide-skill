#!/usr/bin/env python3
"""Check a brand voice guide against the caps and rules in references/guide-template.md.

Usage:
    python3 check_guide.py voice-guide.md
    python3 check_guide.py voice-guide.md --credentials credentials-and-awards-2026-10-23.md
    python3 check_guide.py voice-guide.md --sheet signoff-sheet-2026-10-23.md
    python3 check_guide.py voice-guide.md --sources research/
    python3 check_guide.py voice-guide.md --own-words research/own-words.md
    python3 check_guide.py voice-guide.md --copy draft.md --own-words research/own-words.md

--sources takes original sources only: transcripts, saved pages and raw files (a folder is read
whole). Files we wrote are ignored: own-words.md, sources.md, summary.md, proof-map.md, the guide,
the sheet, the credentials and awards list, and any file containing the line "Our notes, not a source." A quote
found only in our own notes fails. Transcript lines are joined, with timestamps and speaker labels
removed, so a quote that crosses a line break still matches. Square brackets inside a quote mark
our fix for a probable mishearing, e.g. "That's the whole [drill]."; the rest must match word for word.

--own-words reads research/own-words.md: every phrase there needs a Context, and no line it lists
under "## Left out" (sarcasm, jokes, fragments, filler) may appear in the guide or the copy.
Personal talk is never logged anywhere, so it isn't checked here.

--credentials is the credentials and awards list (--proof, its old name, still works).

Exits 1 if any check fails, 0 if it passes (warnings don't fail it, but read them).
Standard library only. Python 3.8 or later.
"""
import argparse
import html
import os
import re
import sys

TOTAL_CAP = 2500  # the whole guide's prose
PROSE_CAPS = {1: 450, 2: 450, 3: 600, 4: 100, 5: 60, 6: 60, 9: 60}  # table rows don't count
TABLE_CAPS = {5: 15, 6: 15, 7: 25, 9: 30}  # section 2 and 3 tables are capped one by one
FACTS_CAP, DATES_CAP, CREDS_CAP = 40, 15, 25  # rows in 4.1, 4.2 and 4.3
FEELS_CAP, STATES_CAP, WORDS_CAP = 5, 4, 20  # rows in 2.5, 2.12 and 3.7
DESC_CAPS = {"Short": 160, "Medium": 300, "Long": 750}
TYPE_OF_WORK_CAP = 70
CHECKS_CAP = 8  # 8.8 before anything ships
BLUEPRINTS_CAP, BLUEPRINT_WORDS = 6, 90  # 8.7 page blueprints
NEVER_CAP = 4  # items in 2.2 and 2.7
PROGRAMS_CAP, PROGRAM_WORDS, PROGRAMS_WORDS = 5, 60, 300  # 2.13, counted apart from section 2's cap
RULES_CAP, OWN_WORDS_CAP, QUESTIONS_CAP = 5, 5, 3  # 3.4 rules, 3.6 phrases, 3.10 questions
DO_LINES_CAP = 3  # Do lines per 3.4 rule
FACT_WORD_CAP = 25
SAMPLE_PARAGRAPH_CAP = 80
SHEET_ITEMS_CAP, SHEET_ITEM_WORDS = 8, 60
SECTIONS = range(1, 10)
COPY_SECTIONS = (1, 2, 3, 7, 8)  # sections writers copy from: needed facts banned
STATUSES = {"public", "confirmed", "needed"}
# 4.3 kinds, and the list each kind goes under on the credentials and awards list
CERTS = "Certifications, licenses and credentials"
STUDIES = "Studies, trainings and courses"
OTHER = "Memberships, positions and education"
KIND_GROUP = {"award": "Awards", "credential": CERTS, "certification": CERTS, "license": CERTS,
              "study": STUDIES, "training": STUDIES, "course": STUDIES,
              "membership": OTHER, "position": OTHER, "education": OTHER}
GROUPS = ["Awards", CERTS, STUDIES, OTHER]
VOICE_LABELS = ["Who's reading", "We sound like", "We never sound like", "Rules", "Tone by page",
                "In their own words", "Mechanics", "Sample paragraph", "Questions we raise"]
STORY_LABELS = ["The customer is never", "We are never", "What they feel and how we answer", "Reader states",
                "Programs and audiences"]
OUR_NOTES = {"own-words.md", "sources.md", "summary.md", "proof-map.md"}
OUR_NOTES_PREFIXES = ("voice-guide", "signoff-sheet", "proof-list", "credentials-and-awards")
NOTES_MARKER = "our notes, not a source."
SOURCE_EXTS = (".md", ".txt", ".html", ".htm", ".json", ".vtt", ".srt", ".csv")
# Patterns that read as AI-written (references/examples.md). Warnings only.
AI_PATTERNS = ["peace of mind", "navigate", "tailored", "seamless", "rest assured",
               "don't hesitate to", "when it comes to", "whether you're", "not just"]
STOP = set("""about after again also although among because been before being between both could does
doing done down during each either even ever every from further have having here into just like made
make many more most much must need never only other ours over same should since some such than that
their them then there these they this those through under until upon very want were what when where
which while will with within without would your yours youre year month week time""".split())
# Names in a needed fact, like "Women Coaches Academy": two or more capitalized words.
PROPER = re.compile(r"\b[A-Z][A-Za-z0-9'&.]*(?:\s+(?:(?:of|and|the|for|in)\s+)?[A-Z][A-Za-z0-9'&.]*)+")
NUMBER_WORDS = set("one two three four five six seven eight nine ten eleven twelve".split())
PRICE = re.compile(r"\$\s?\d[\d,]*(?:\.\d{2})?")
# Section 7 descriptions go into profile fields: no phone, link, price or call to action (GBP rules).
PHONE = re.compile(r"(?:\(\d{3}\)\s?|\b\d{3}[\s.-])\d{3}[\s.-]\d{4}\b")
URL = re.compile(r"https?://|\bwww\.|\b[a-z0-9-]{2,}\.(?:com|net|org|biz|info|io|example)\b")
CTA = re.compile(r"(?:^|[.!?]\s+)(?:call|book|schedule|sign\s+up|register|enroll|reserve|visit|buy|get|request|"
                 r"come\s+(?:visit|see|in))\b|\b(?:call|contact|visit)\s+us\b|\b(?:call|book)\s+(?:now|today)\b",
                 re.IGNORECASE)
# A heading that frames a claim word as the shopper's search: "How to choose the best plumber in [City]".
SHOPPER_HEADING = re.compile(
    r"^(?:how\s+(?:to|do|does|can|much|long|often)|what|which|where|when|who|is|are|do|does|can|should|"
    r"choos\w*|find\w*|pick\w*|compar\w*|hir\w*|look\w*\s+for|search\w*\s+for|questions?\s+to\s+ask|"
    r"tips?\s+(?:for|on)|(?:a\s+|your\s+|the\s+)?guide\s+to)\b", re.IGNORECASE)
OWNER_ACCOUNT = "owner's account"

NUM = (r"(?:\d+|a|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|"
       r"fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|several|many|a few|"
       r"a couple of)(?:[- ](?:one|two|three|four|five|six|seven|eight|nine))?")
UNIT = r"(?:years?|yrs?|decades?)\b"
# Year counts that go stale: these fail.
YEAR_COUNT_FAIL = re.compile(
    r"\b\d+\s*\+\s*" + UNIT + r"(?!\s+old)"
    r"|\b" + NUM + r"\s+" + UNIT + r"'?\s+(?:of\s+)?(?:combined\s+)?(?:experience|service|practice)\b"
    r"|\b" + NUM + r"\s+" + UNIT + r"\s+(?:in\s+(?:business|practice|the\s+(?:trade|industry|business|field))|serving)\b"
    r"|\b" + NUM + r"\s+" + UNIT + r"\s+(?:as\s+)?an?\s+(?!row\b|day\b|week\b|month\b|time\b|year\b|half\b)[a-z]\w+"
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
# Transcript lines: "**[18:23] Name:** text", "[00:18:23] Name: text", "Name (18:23): text"
TS = r"[\[(]?(?:\d{1,2}:)?\d{1,2}:\d{2}(?:[.,]\d+)?[\])]?"
TRANSCRIPT_LINE = [
    re.compile(r"^(?:[-*]\s+)?(?:\*\*)?\s*" + TS + r"\s*(?:\*\*)?\s*(?P<who>[^:\n]{1,40}?)\s*:\s*(?:\*\*)?\s*(?P<text>.*)$"),
    re.compile(r"^(?:[-*]\s+)?(?:\*\*)?\s*(?P<who>[A-Za-z][^:\n]{0,40}?)\s*" + TS + r"\s*(?:\*\*)?\s*:?\s*(?:\*\*)?\s*(?P<text>.*)$"),
    re.compile(r"^(?:[-*]\s+)?(?:\*\*)?\s*" + TS + r"\s*(?:\*\*)?\s*(?P<who>)(?P<text>.*)$"),
    re.compile(r"^(?:\*\*)?(?P<who>(?:Speaker \d+|[A-Z][a-z]+(?: [A-Z][a-z]+)?))(?:\*\*)?\s*:\s*(?:\*\*)?\s*(?P<text>.*)$"),
]

errors, warnings = [], []


def read(path):
    """A file's text, or None with a FAIL line (not a traceback) if it can't be read."""
    try:
        with open(path, encoding="utf-8-sig", errors="replace") as f:
            return f.read()
    except OSError as e:
        errors.append(f"Can't read {path}: {e.strerror}. Check the path.")
        return None


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
    """Split section 4 into {'4.1': [...], '4.2': [...], '4.3': [...]} by its ### headings."""
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


def items(block):
    """Bulleted or numbered items in a block; a line that doesn't start one continues the last."""
    out = []
    for line in (block or "").splitlines():
        s = line.strip()
        if re.match(r"^(?:[-*]|\d+\.)\s+\S", s):
            out.append(s)
        elif s and out:
            out[-1] += " " + s
    return out


def numbered_items(block):
    """Numbered items, each with every line under it (bullets too) until the next number: 3.4 rules with extra Do lines."""
    out = []
    for line in (block or "").splitlines():
        s = line.strip()
        if re.match(r"^\d+\.\s+\S", s):
            out.append(s)
        elif s and out:
            out[-1] += " " + s
    return out


def overlaps(m, spans):
    return any(m.start() < e and s < m.end() for s, e in spans)


def year_counts(text):
    """(fails, warns): year counts like 'over 12 years' or '20+ years' that should be dates."""
    hits = list(YEAR_COUNT_FAIL.finditer(text))
    spans = [h.span() for h in hits]
    warns = [m.group(0) for m in YEAR_COUNT_WARN.finditer(text) if not overlaps(m, spans)]
    fails = [h.group(0) for h in hits if not reader_span(text, h)]
    warns += [h.group(0) for h in hits if reader_span(text, h)]
    return fails, warns


def reader_span(text, m):
    """'for over two years?': how long the reader has had the problem, asked as a question. Not time in business."""
    if not m.group(0).lower().startswith("for ") or context_of(text, m.start(), m.end()) != "question":
        return False
    ls = max(text.rfind(c, 0, m.start()) for c in ".!?\n") + 1
    sentence = text[ls:m.end()].lower()
    return bool(re.search(r"\byou(?:r|'re|'ve)?\b", sentence)) and not re.search(
        r"\b(?:we|we've|we're|our|us|i|i've|serv\w*|business|licensed|operating|practic\w*|experience)\b", sentence)


def context_of(text, start, end):
    """'quote' if the match sits inside double quotes, 'question' if its sentence ends with '?', 'heading' if it
    sits in a heading that frames it as the shopper's search ("How to choose the best plumber in [City]")."""
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
    h = re.match(r"^\s{0,3}#{1,6}\s+(.*)$", line) or re.match(r"^\s*\*\*([^*]+)\*\*\s*$", line)
    if h and (SHOPPER_HEADING.match(h.group(1).strip(" *_")) or re.search(r"\bnear\s+me\b", h.group(1), re.IGNORECASE)) and not re.search(
            r"\b(?:we|we're|we've|our|us|i|i'm)\b", h.group(1), re.IGNORECASE):
        return "heading"
    return None


def labeled_table(lines, label):
    """Rows of the table under a bold label, up to the next bold label or heading."""
    on, block = False, []
    for line in lines:
        s = line.strip()
        if not on:
            if re.match(LABEL + label + r"[^*]*\*\*", s):
                on = True
            continue
        if re.match(r"^\*\*[^*]+\*\*", s) or s.startswith("#"):
            break
        block.append(line)
    return table_rows(block)


def own_words(sections):
    """3.6 rows: [(phrase, source, context, feeds)], from the table (or bullets with Context: and Feeds:)."""
    out = []
    for cells in labeled_table(sections.get(3, []), "In their own words"):
        m = re.search(r'"([^"]{3,})"', cells[0]) if cells else None
        if m:
            cells = cells + [""] * (4 - len(cells))
            out.append((m.group(1), cells[1], cells[2].strip(" ."), cells[3]))
    if not out:
        for line in items(labeled_block(sections.get(3, []), "In their own words")):
            m = re.search(r'"([^"]{3,})"', line)
            if m:
                c = re.search(r"Context:\s*(.+?)(?:\s*\bFeeds:|$)", line)
                f = re.search(r"Feeds:\s*(.+)$", line)
                out.append((m.group(1), line, c.group(1).strip(" .") if c else "", f.group(1) if f else ""))
    return out


def guide_quotes(sections):
    """(where, quote) for every verbatim phrase in 2.3, 2.5 and 3.6."""
    out = []
    for line in items(labeled_block(sections.get(2, []), "In their words")):
        m = re.search(r'"([^"]{3,})"', line)
        if m:
            out.append(("2.3", m.group(1)))
    for cells in labeled_table(sections.get(2, []), "What they feel and how we answer"):
        m = re.search(r'"([^"]{3,})"', cells[0]) if cells else None
        if m:
            out.append(("2.5", m.group(1)))
    out += [("3.6", q[0]) for q in own_words(sections)]
    return out


def is_owner_retelling(src):
    """2.5 Source: the owner's account of what customers say, not a review or testimonial."""
    s = normalize(src).lower()
    if OWNER_ACCOUNT in s:
        return True
    if re.match(r"\s*customer\b", s):  # "customer, intake call, 04:10": a customer's own words, recorded with consent
        return False
    return bool(re.search(r"\b(?:owner|call|transcript|recording|interview|video|podcast)\b", s)) and not re.search(
        r"\b(?:review|testimonial|google|yelp|facebook|bbb|survey|our reading)\b", s)


def owner_accounts(sections):
    """Quoted 2.5 feelings whose source is the owner's retelling. Never quoted on a page as a customer."""
    out = []
    for cells in labeled_table(sections.get(2, []), "What they feel and how we answer"):
        m = re.search(r'"([^"]{3,})"', cells[0]) if cells else None
        if m and len(cells) > 1 and is_owner_retelling(cells[1]):
            out.append(m.group(1))
    return out


def sentences(text):
    """Example sentences, without fact-ID citations, lowercased, for spotting repeats."""
    text = re.sub(r"\[(?:[FCQ]\d+[,;\s]*(?:and\s+)?)+\]", "", text or "")
    out = []
    for s in re.split(r"(?<=[.!?])\s+", text):
        s = re.sub(r"\s+", " ", s).strip(" \"'").rstrip(".!").lower()
        if s:
            out.append(s)
    return out


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
    s1, s2, s3, s8 = (sections.get(n, []) for n in (1, 2, 3, 8))

    # Prose caps. 2.13 programs have their own cap, so they don't count against section 2's.
    programs = labeled_block(s2, "Programs and audiences")
    total = 0
    for n, lines in sections.items():
        count = len(words(prose(lines)))
        total += count
        if n == 2 and programs:
            count -= len(words(programs))
        cap = PROSE_CAPS.get(n)
        if cap and count > cap:
            errors.append(f"Section {n}: {count} words of prose, cap {cap}.")
    if total > TOTAL_CAP:
        errors.append(f"The guide has {total} words of prose, cap {TOTAL_CAP}. Cut before adding.")

    # Table caps
    for n, cap in TABLE_CAPS.items():
        if n in sections:
            rows = table_rows(sections[n])
            if len(rows) > cap:
                errors.append(f"Section {n}: {len(rows)} table rows, cap {cap}.")

    # Ledger (4.1), dates (4.2) and credentials and awards (4.3)
    ledger, facts_text, sources, dates, creds = {}, {}, {}, {}, {}
    if 4 in sections:
        subs = split_subsections(sections[4])
        fact_lines = subs.get("4.1", sections[4] if not subs else [])
        for sub, heading in (("4.1", "Facts"), ("4.2", "Dates"), ("4.3", "Credentials and awards")):
            if sub not in subs:
                errors.append(f"Section 4: no '### {sub} {heading}' heading. Add it, with 'None yet.' if it's empty.")
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
            if fid in ledger:
                errors.append(f"Ledger ID {fid} is used twice.")
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
                errors.append(f"{fid}: '{hit}' is a year count. Anchor it to a date (rule 7) and add a 4.2 row.")
            for hit in warns:
                warnings.append(f"{fid}: '{hit}' may be a year count. If it's time in business, anchor it to a date.")
            ledger[fid], facts_text[fid], sources[fid] = status, fact, source
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

        cred_rows = table_rows(subs.get("4.3", []))
        if len(cred_rows) > CREDS_CAP:
            errors.append(f"Section 4.3: {len(cred_rows)} rows, cap {CREDS_CAP}.")
        for cells in cred_rows:
            if len(cells) < 3:
                errors.append(f"4.3 row has {len(cells)} columns, expected 3: {cells}")
                continue
            fid, kind, issuer = cells[0], cells[1].lower().strip(), cells[2]
            if fid not in ledger:
                errors.append(f"4.3 cites {fid}, which isn't in 4.1.")
                continue
            if kind not in KIND_GROUP:
                errors.append(f"4.3 {fid}: list '{cells[1]}' should be one of: {', '.join(sorted(KIND_GROUP))}.")
            if not issuer:
                errors.append(f"4.3 {fid}: no issuer. Name the body that issued it, as it names itself.")
            creds[fid] = (kind, issuer)
        usable = [f for f in creds if ledger.get(f) in ("public", "confirmed")]
        if len(usable) == 1 and creds[usable[0]][0] == "award":
            warnings.append(f"4.3: one award ({usable[0]}) is the only public or confirmed proof. "
                            "Paid or vanity awards count if named exactly, but don't let one be the only credential.")

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

    # Page 1 shows the voice, and doesn't call the reader "client"
    sound = labeled_line(s1, "How we'll sound")
    if sound is None:
        errors.append("Section 1: no **1.3 How we'll sound.** line. Page 1 must show the voice the client approves.")
    else:
        sample = re.search(r'"([^"]{10,})"', sound)
        if not sample:
            errors.append("Section 1, 1.3: no sample line in quotation marks. Copy one Do line from 3.4.")
        elif sample.group(1) not in "\n".join(s3):
            warnings.append("Section 1, 1.3: the sample line isn't word for word in section 3. Copy a Do line exactly.")
        if "but not" not in sound.lower():
            warnings.append("Section 1, 1.3: add the 3.4 pairs ('direct, but not harsh') so the client sees how we'll sound.")
        if not re.search(r"sound like you", sound, re.IGNORECASE):
            warnings.append("Section 1, 1.3: end with the question 'Does this sound like you talking to a customer? "
                            "Tell us what doesn't.' Silence approves nothing about the voice.")
    if re.search(r"\bclients?\b", prose(s1), re.IGNORECASE):
        warnings.append("Section 1 says 'client'. The business reads page 1: use its name or 'you'.")

    # Story: the never lists, what they feel, reader states, programs
    for label in STORY_LABELS:
        if 2 in sections and labeled_line(s2, label) is None:
            errors.append(f"Section 2: no **{label}.** line. Keep it, with 'None yet.' if it doesn't apply.")
    for label in ("The customer is never", "We are never"):
        block = labeled_block(s2, label)
        if block:
            bullets = items(block)
            n = len(bullets) if bullets else len([p for p in block.split(";") if p.strip(" .")])
            if n > NEVER_CAP:
                errors.append(f"Section 2, '{label}': {n} items, cap {NEVER_CAP}.")
    feels = labeled_table(s2, "What they feel and how we answer")
    if len(feels) > FEELS_CAP:
        errors.append(f"Section 2.5: {len(feels)} rows, cap {FEELS_CAP}. Keep the top worries.")
    for i, cells in enumerate(feels, 1):
        if len(cells) < 4:
            errors.append(f"Section 2.5 row {i} has {len(cells)} columns, expected 4.")
            continue
        feel, src, answer = cells[:3]
        if not re.search(r"\bF\d+\b", answer):
            errors.append(f"Section 2.5 row {i}: 'How we answer' cites no fact ID. Answer only with ledgered facts.")
        if '"' not in feel and not re.search(r"our reading|\b[QC]\d+\b", src, re.IGNORECASE):
            warnings.append(f"Section 2.5 row {i}: the feeling isn't quoted. Quote it, or write 'our reading' in Source.")
        if '"' in feel and is_owner_retelling(src) and OWNER_ACCOUNT not in normalize(src).lower():
            errors.append(f"Section 2.5 row {i}: the feeling is the owner's retelling of what customers say. Write "
                          "'owner's account' in its Source, so no one quotes it on a page as a customer.")
    states = labeled_table(s2, "Reader states")
    if len(states) > STATES_CAP:
        errors.append(f"Section 2.12: {len(states)} rows, cap {STATES_CAP}.")
    for cells in states:
        if not re.search(r"no one yet|default|loyal|stuck|crisis", cells[0], re.IGNORECASE):
            warnings.append(f"Section 2.12: '{cells[0]}' isn't one of the four states (no one yet, has a default, loyal, stuck).")
    progs = items(programs) if programs else []
    if progs:
        if len(progs) > PROGRAMS_CAP:
            errors.append(f"Section 2.13: {len(progs)} programs, cap {PROGRAMS_CAP}.")
        if len(words(programs)) > PROGRAMS_WORDS:
            errors.append(f"Section 2.13: {len(words(programs))} words, cap {PROGRAMS_WORDS}.")
        for p in progs:
            name = re.search(r"\*\*([^*]+)\*\*", p)
            label = name.group(1).strip(" .") if name else p[:30]
            if len(words(p)) > PROGRAM_WORDS:
                errors.append(f"Section 2.13 '{label}': {len(words(p))} words, cap {PROGRAM_WORDS}.")
            for part in ("Who:", "Differs:", "Proof:", "CTA:"):
                if part not in p:
                    warnings.append(f"Section 2.13 '{label}': no '{part}'. Each program says who, what differs, its proof and its CTA.")

    # Voice: the slots, the pairs, own words in context, words, mechanics, questions
    for label in VOICE_LABELS:
        if 3 in sections and labeled_line(s3, label) is None:
            errors.append(f"Section 3: no **{label}.** line. Keep it, with 'None yet.' if it doesn't apply.")
    rules = numbered_items(labeled_block(s3, "Rules"))
    if len(rules) > RULES_CAP:
        errors.append(f"Section 3.4: {len(rules)} rules, cap {RULES_CAP}.")
    froms = []
    for i, r in enumerate(rules, 1):
        head = re.search(r"\*\*([^*]+)\*\*", r)
        if not head or not re.search(r"\bbut not\b", head.group(1), re.IGNORECASE):
            errors.append(f"Section 3.4 rule {i}: the bold head should be a pair, like '**Direct, but not harsh.**'")
        n_do, n_dont = r.count('Do: "'), r.count("Don't: \"")
        if not n_do or not n_dont:
            warnings.append(f"Section 3.4 rule {i}: needs a Do line and a Don't line, each in quotation marks.")
        elif n_do > DO_LINES_CAP:
            errors.append(f"Section 3.4 rule {i}: {n_do} Do lines, cap {DO_LINES_CAP}.")
        elif n_do != n_dont:
            warnings.append(f"Section 3.4 rule {i}: {n_do} Do line(s), {n_dont} Don't line(s). Give each Do line "
                            "its own Don't: the near miss on the same fact.")
        for do, dont in re.findall(r'Do: "([^"]+)"\s*Don\'t: "([^"]+)"', r):
            if not key_terms(do) & key_terms(dont):
                warnings.append(f"Section 3.4 rule {i}: the Don't line shares no words with its Do line. Write the Don't "
                                "on the same fact, as the near miss a writer would actually produce.")
        fm = re.search(r"\bFrom:\s*(.*)$", r)
        if not fm or not fm.group(1).strip(" ."):
            warnings.append(f"Section 3.4 rule {i}: no 'From:'. Say where the rule came from: their pattern with "
                            "timestamps, what reviewers say (with the month), or 'our call, for the customer: why'.")
        else:
            froms.append(fm.group(1))
            if re.search(r"\b(?:our|old|current|existing)\s+(?:site|copy|website)\b|\bsite copy\b", fm.group(1), re.IGNORECASE):
                warnings.append(f"Section 3.4 rule {i}: its From points to site copy. That's our style, not their voice.")
    quotes = own_words(sections)
    if len(quotes) > OWN_WORDS_CAP:
        errors.append(f"Section 3.6: {len(quotes)} phrases, cap {OWN_WORDS_CAP}.")
    fed = set()
    for phrase, src, context, feeds in quotes:
        short = phrase if len(phrase) < 50 else phrase[:47] + "..."
        if len(words(context)) < 3:
            errors.append(f"Section 3.6 \"{short}\": no Context. Say what they were talking about when they said it.")
        refs = re.findall(r"3\.4\s+rules?\s+(\d+)", feeds)
        if not feeds.strip():
            errors.append(f"Section 3.6 \"{short}\": no Feeds. Name the rule it shapes (e.g. '3.4 rule 2') or drop it.")
        elif not refs and not re.search(r"\b[1-3]\.\d+\b", feeds):
            errors.append(f"Section 3.6 \"{short}\": Feeds should name a rule or section, e.g. '3.4 rule 2' or '3.7'.")
        for ref in refs:
            if not 1 <= int(ref) <= len(rules):
                errors.append(f"Section 3.6 \"{short}\": feeds 3.4 rule {ref}, which doesn't exist.")
            fed.add(int(ref))
        if re.search(r"\b(?:call|video|recording|transcript|interview|podcast|meeting)\b", src, re.IGNORECASE) \
                and not re.search(r"\b\d{1,2}:\d{2}\b", src):
            warnings.append(f"Section 3.6 \"{short}\": a recording needs its timestamp (mm:ss).")
    if quotes and rules and not fed:
        warnings.append("Section 3.6: no phrase feeds a 3.4 rule. If their words show a pattern that fits the customer, "
                        "build a rule from it; never bend a line into a rule to fill the slot.")
    elif quotes and froms and not any(re.search(r"\b\d{1,2}:\d{2}\b|review", f, re.IGNORECASE) for f in froms):
        warnings.append("Section 3.4: no From line names a pattern in their words (with timestamps) or their reviews. "
                        "If they show one that fits the customer, a rule should come from it.")
    if len(labeled_table(s3, "Words")) > WORDS_CAP:
        errors.append(f"Section 3.7: {len(labeled_table(s3, 'Words'))} rows, cap {WORDS_CAP}.")
    mech = labeled_block(s3, "Mechanics") or ""
    if mech.strip(" .") and not re.search(r"None yet", mech):
        if re.search(r"reading level|grade\s*\d", mech, re.IGNORECASE):
            if "because" not in mech.lower():
                warnings.append("Section 3.8: give each audience's reading level a reason ('grade 6, because ...').")
            if len(progs) > 1 and len(re.findall(r"grade\s*\d", mech, re.IGNORECASE)) < 2:
                warnings.append("Section 3.8: there are several programs in 2.13 but one reading level. Set one per audience.")
        else:
            warnings.append("Section 3.8: no reading level. Set one per audience, with the reason.")
        if not re.search(r'"I"|\bI\b', mech):
            warnings.append("Section 3.8: say which sections are written as 'I' (owner-voiced) and which as 'we'.")
    para = labeled_block(s3, "Sample paragraph")
    if para and len(words(para)) > SAMPLE_PARAGRAPH_CAP:
        errors.append(f"Section 3, sample paragraph: {len(words(para))} words, cap {SAMPLE_PARAGRAPH_CAP}.")
    ids56 = {r[0] for n in (5, 6) for r in table_rows(sections.get(n, [])) if r}
    qs = [q for q in items(labeled_block(s3, "Questions we raise")) if re.match(r"^\d+\.", q)]
    if len(qs) > QUESTIONS_CAP:
        errors.append(f"Section 3.10: {len(qs)} questions, cap {QUESTIONS_CAP}.")
    for i, q in enumerate(qs, 1):
        mq = re.search(r'"([^"]+)"', q)
        if not mq or not mq.group(1).rstrip().endswith("?"):
            warnings.append(f"Section 3.10 question {i}: put the question in quotation marks, ending with '?'.")
        raises = re.search(r"Raises:\s*([^.]*)", q)
        cited = re.findall(r"\b[CQ]\d+\b", raises.group(1)) if raises else []
        if not cited:
            errors.append(f"Section 3.10 question {i}: no 'Raises:' criterion (a C or Q ID from section 5 or 6).")
        for c in cited:
            if c not in ids56:
                errors.append(f"Section 3.10 question {i}: {c} isn't in section 5 or 6.")
        answer = re.search(r"Answer:\s*(.*)$", q)
        if not answer or not re.search(r"\bF\d+\b", answer.group(1)):
            errors.append(f"Section 3.10 question {i}: no 'Answer:' with fact IDs. Raise only what this business visibly meets.")

    # Descriptions
    if 7 in sections:
        desc = {k: labeled_line(sections[7], k) for k in DESC_CAPS}
        for k, cap in DESC_CAPS.items():
            d = desc[k]
            if d is None:
                errors.append(f"Section 7: no **{k} ...:** description found.")
            elif len(d) > cap:
                errors.append(f"Section 7: {k} description is {len(d)} characters, cap {cap}.")
        for k in DESC_CAPS:
            d = desc[k] or ""
            found = [what for what, rx in (("a phone number", PHONE), ("a link", URL), ("a price", PRICE)) if rx.search(d)]
            if found:
                errors.append(f"Section 7: the {k.lower()} description has {' and '.join(found)}. Google's Business Profile "
                              "rules bar them in the description; the phone and website have their own fields.")
            cta = CTA.search(d)
            if cta:
                warnings.append(f"Section 7: the {k.lower()} description has a call to action "
                                f"('{cta.group(0).strip(' .!?')}'). Google's rules bar direct calls to action there; "
                                "the CTA lives in 2.9 and on the page.")
        if desc["Short"] and desc["Medium"] and not desc["Medium"].startswith(desc["Short"]):
            errors.append("Section 7: the medium description must start with the short one, word for word.")
        if desc["Medium"] and desc["Long"] and not desc["Long"].startswith(desc["Medium"]):
            errors.append("Section 7: the long description must start with the medium one, word for word.")
        who = labeled_line(s1, "Who you are")
        if who is None:
            errors.append("Section 1: no **1.1 Who you are.** line found.")
        elif desc["Short"] and who != desc["Short"]:
            errors.append("Section 1 'Who you are' must match the section 7 short description exactly.")

    # Section 8: the check before shipping, the page blueprints, and each type of work
    checks = labeled_block(s8, "Before anything ships")
    blueprints = labeled_block(s8, "Page blueprints")
    goods = {}
    if 8 in sections:
        if checks is None:
            errors.append("Section 8: no **8.8 Before anything ships.** checklist. Every job runs it.")
        else:
            cl = [c for c in items(checks) if re.match(r"^\d+\.", c)]
            if not cl:
                warnings.append("Section 8.8 has no numbered checks. Write up to 8 yes/no questions from this guide.")
            if len(cl) > CHECKS_CAP:
                errors.append(f"Section 8.8: {len(cl)} checks, cap {CHECKS_CAP}.")
            for i, c in enumerate(cl, 1):
                if not c.rstrip(" *_").endswith("?"):
                    warnings.append(f"Section 8.8 check {i} should be a yes/no question.")
        if blueprints is None:
            errors.append("Section 8: no **8.7 Page blueprints.** line. Keep it, with 'None: no site pages in this work.'")
        else:
            bps = items(blueprints)
            if len(bps) > BLUEPRINTS_CAP:
                errors.append(f"Section 8.7: {len(bps)} page types, cap {BLUEPRINTS_CAP}. Only the types in this job.")
            for bp in bps:
                name = re.search(r"\*\*([^*]+)\*\*", bp)
                label = name.group(1).strip(" .") if name else bp[:30]
                if len(words(bp)) > BLUEPRINT_WORDS:
                    errors.append(f"Section 8.7 '{label}': {len(words(bp))} words, cap {BLUEPRINT_WORDS}.")
                good = re.search(r'Good:\s*"([^"]+)"', bp)
                if not good or not re.search(r'Poor:\s*"', bp):
                    warnings.append(f"Section 8.7 '{label}': needs a Poor line and a Good line, each in quotation marks.")
                if good:
                    goods[f"8.7 {label} Good line"] = good.group(1)
        for line in s8:
            m = re.match(r"^\*\*([^*]+)\*\*", line.strip())
            if m:
                label = re.sub(r"^\d+(?:\.\d+)*\s+", "", m.group(1)).strip(" .:")
                if label in ("Before anything ships", "Page blueprints"):
                    continue
                block = labeled_block(s8, re.escape(label)) or ""
                if len(words(block)) > TYPE_OF_WORK_CAP:
                    errors.append(f"Section 8 '{label}': {len(words(block))} words, cap {TYPE_OF_WORK_CAP}.")

    # Year counts in the lines that go into copy word for word
    verbatim = {"1.1": labeled_line(s1, "Who you are"), "1.3": sound,
                "1.4": labeled_block(s1, "What we'll lead with"), "3.9": para}
    for k in DESC_CAPS:
        verbatim["7 " + k] = labeled_line(sections.get(7, []), k)
    verbatim.update(goods)
    for where, t in verbatim.items():
        if not t:
            continue
        fails, warns = year_counts(t)
        for hit in fails:
            errors.append(f"{where}: '{hit}' is a year count. Use the date from 4.2.")
        for hit in warns:
            warnings.append(f"{where}: '{hit}' may be a year count. If it's time in business, use the date from 4.2.")

    # The lines writers copy (1.3, Do lines, 3.9, descriptions, Good lines) must not use the never-use words
    terms = never_use_list(sections)
    samples = {"1.3": sound, "3.9": para}
    for i, do in enumerate(re.findall(r'Do: "([^"]+)"', labeled_block(s3, "Rules") or ""), 1):
        samples[f"3.4 Do line {i}"] = do
    for k in DESC_CAPS:
        samples["7 " + k] = labeled_line(sections.get(7, []), k)
    samples.update(goods)
    for where, t in samples.items():
        if t:
            for term, allowed in never_use_hits(t, terms, fact_spans(t, ledger, facts_text)):
                if not allowed:
                    errors.append(f"{where} uses '{term}', which is on the 1.6 never-use list. Writers copy these lines.")

    # Example lines writers copy: each sentence once, at most one question opener, each phrase of theirs once,
    # and never the owner's account of what customers say. 1.3 copies a Do line, so it isn't counted.
    examples = {}
    for i, do in enumerate(re.findall(r'Do: "([^"]+)"', labeled_block(s3, "Rules") or ""), 1):
        examples[f"3.4 Do line {i}"] = do
    for i, cells in enumerate(feels, 1):
        if len(cells) > 3 and cells[3].strip():
            examples[f"2.5 copy line {i}"] = cells[3]
    if para:
        examples["3.9"] = para
    examples.update(goods)
    fact_sents = {s for t in facts_text.values() for s in sentences(t)}
    seen_at = {}
    for where, t in examples.items():
        for snt in sentences(t):
            if len(words(snt)) >= 5 and snt not in fact_sents:
                seen_at.setdefault(snt, [])
                if where not in seen_at[snt]:
                    seen_at[snt].append(where)
    for snt, wheres in seen_at.items():
        if len(wheres) > 1:
            warnings.append(f"The same example sentence is in {', '.join(wheres)}: \"{snt[:60]}\". Writers copy what "
                            "they see most; make each example a different sentence.")
    q_open = [w for w, t in examples.items() if sentences(t) and sentences(t)[0].endswith("?")]
    if len(q_open) > 1:
        warnings.append(f"{len(q_open)} example lines open with a question ({', '.join(q_open)}). Vary the openers; "
                        "at most one opens with a question.")
    for phrase, _src, _ctx, _feeds in own_words(sections):
        needle = re.sub(r"\s+", " ", re.sub(r"[\[\]]", "", phrase)).lower().strip(" .")
        used = [w for w, t in examples.items() if needle and needle in re.sub(r"\s+", " ", t).lower()]
        if len(used) > 1:
            warnings.append(f"3.6 \"{phrase[:50]}\" is in {len(used)} example lines ({', '.join(used)}). Use each of "
                            "their phrases in one place, or it becomes a catchphrase.")
    for feel in owner_accounts(sections):
        needle = squash(feel).strip(" .!?")
        for where, t in list(examples.items()) + [("1.3", sound or "")] + [("7 " + k, labeled_line(sections.get(7, []), k) or "") for k in DESC_CAPS]:
            if needle and needle in squash(t):
                errors.append(f"{where} uses \"{feel}\", the owner's account of what customers say (2.5). "
                              "Never present it as a customer's words; write the feeling as the reader's situation.")

    # Leftover template placeholders. Brackets inside a real quote are a mishearing fix, not a placeholder.
    unquoted = re.sub(r'"([^"\n]*)"', lambda m: "" if re.sub(r"\[[^\]]*\]", "", m.group(1)).strip(" .,!?") else m.group(0), text)
    placeholders = [
        p for p in re.findall(r"\[[^\]\n]{2,}\](?!\()", unquoted)
        if not re.fullmatch(r"\[(?:[FCQ]\d+[,;\s]*(?:and\s+)?)+\]", p)  # bracketed IDs are citations
    ]
    if placeholders:
        sample = ", ".join(sorted(set(placeholders))[:5])
        warnings.append(f"{len(placeholders)} bracketed placeholder(s) left, e.g. {sample}")

    version = re.search(r"^Version\s+(\d+(?:\.\d+)*)", text, re.MULTILINE)
    guide = {"ledger": ledger, "facts": facts_text, "sources": sources, "dates": dates, "creds": creds}
    return sections, total, guide, (version.group(1) if version else None)


def never_use_list(sections):
    lines = sections.get(1, [])
    line = labeled_line(lines, "Words we'll never use")
    if line is None:
        return []
    if not line.strip(" ."):  # the words are listed as bullets under the label
        block = labeled_block(lines, "Words we'll never use") or ""
        line = ", ".join(l.lstrip("-* ").strip() for l in block.splitlines() if l.strip())
    parts = re.split(r"[;,]", line.rstrip("."))
    return [i.strip().strip("\"'").strip() for i in parts if i.strip()]


def words_table_not(sections):
    rows = labeled_table(sections.get(3, []), "Words")
    return [r[1].strip("\"' ") for r in rows if len(r) > 1 and r[1].strip("\"' ") and not r[1].startswith("[")]


def find(term, copy):
    return list(re.finditer(r"(?<!\w)" + re.escape(term) + r"(?!\w)", copy, re.IGNORECASE))


def fact_spans(text, ledger, facts_text):
    """Where a public or confirmed fact appears word for word, e.g. an award named 'Best of [City]'."""
    spans = []
    for fid, fact in facts_text.items():
        if ledger.get(fid) in ("public", "confirmed") and fact.strip(" ."):
            spans += [m.span() for m in re.finditer(re.escape(fact.strip(" .")), text, re.IGNORECASE)]
            # An award's name inside a sentence ("named Best Swim Lessons in Readers' Choice 2025"): the name,
            # capitalized as in the ledger, counts as the fact when the same line also has its year or issuer.
            names = PROPER.findall(fact)
            years = re.findall(r"\b(?:19|20)\d{2}\b", fact)
            for name in names:
                others = [n for n in names if n != name] + years
                for m in re.finditer(r"(?<!\w)" + re.escape(name) + r"(?!\w)", text):
                    ls, le = text.rfind("\n", 0, m.start()) + 1, text.find("\n", m.end())
                    if any(o in text[ls:(len(text) if le == -1 else le)] for o in others):
                        spans.append(m.span())
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


def fold(t):
    """Fold simple plurals so 'grades' matches 'grade' and 'coaches' matches 'coach'."""
    if len(t) > 4 and t.endswith("ies"):
        return t[:-3] + "y"
    if re.search(r"(?:ss|x|z|ch|sh)es$", t):
        return t[:-2]
    if len(t) > 3 and t.endswith("s") and not t.endswith("ss"):
        return t[:-1]
    return t


def key_terms(text):
    """Distinctive words and numbers in a fact: 4+ letters, not common words, plurals folded."""
    out = set()
    for w in re.findall(r"[A-Za-z][A-Za-z'-]*|\d+(?:[.,]\d+)?", normalize(text)):
        t = w.lower().strip("'-")
        if t.endswith("'s"):
            t = t[:-2]
        if t[:1].isdigit():
            out.add(t)
        elif len(t) >= 4 and t not in STOP and fold(t) not in STOP:  # fold first, so "years" is caught like "year"
            out.add(fold(t))
    return out


def date_hint(guide):
    """Point at this guide's own 4.2 wording, so a fix never borrows a year from an example."""
    years = sorted({d[:4] for ds in guide["dates"].values() for d in ds})
    if years:
        return f"Use the wording in 4.2 (this guide's dates: {', '.join(years)}), or cut it."
    return "4.2 has no dates yet: cut it, or put the date on the sign-off sheet."


def check_copy(path, sections, guide):
    ledger, facts_text = guide["ledger"], guide["facts"]
    raw = read(path)
    if raw is None:
        return
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
        elif allowed == "heading":
            warnings.append(f"{path}: '{term}' is on the never-use list, used in a heading that frames it as the shopper's "
                            "search. Fine as the SEO brief's phrase; never as a claim about the client.")
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
        elif reader_span(copy, m):
            warnings.append(f"{path}: '{m.group(0)}' is in a question. Fine about the reader's situation; never as time in business.")
        else:
            errors.append(f"{path}: '{m.group(0)}' is a year count. {date_hint(guide)}")
    spans = [m.span() for m in YEAR_COUNT_FAIL.finditer(copy)]
    for m in YEAR_COUNT_WARN.finditer(copy):
        if not overlaps(m, spans):
            warnings.append(f"{path}: '{m.group(0)}' may be a year count. If it's time in business, use the date.")

    # Claim check 1, years: every year in the copy should trace to a public or confirmed fact.
    usable = " ".join(t for f, t in facts_text.items() if ledger.get(f) in ("public", "confirmed"))
    unusable = " ".join(t for f, t in facts_text.items() if ledger.get(f) == "needed")
    for year in sorted(set(re.findall(r"\b(?:19|20)\d{2}\b", copy))):
        if year in usable:
            continue
        if year in unusable:
            errors.append(f"{path}: {year} appears only in a needed fact. It stays out of copy until confirmed.")
        elif re.search(r"\b(?:since|founded|established|licensed|certified|opened)\s+(?:in\s+)?" + year, copy, re.IGNORECASE):
            errors.append(f"{path}: '{year}' is used as a start date, but no public or confirmed fact has it. Never write a date the ledger doesn't show.")
        else:
            warnings.append(f"{path}: {year} isn't in any ledger fact. Check the claim against the ledger.")

    # Claim check 2, needed facts: a sentence that uses a needed fact's distinctive words may state it.
    known = key_terms(usable)
    keys = {f: key_terms(t) - known for f, t in facts_text.items() if ledger.get(f) == "needed"}
    for line in copy.splitlines():
        for sentence in re.split(r"(?<=[.!?])\s+", line.strip()):
            if not sentence:
                continue
            st = key_terms(sentence)
            for fid, key in keys.items():
                hit = sorted(key & st)
                if all(h in NUMBER_WORDS or (h.isdigit() and len(h) == 1) for h in hit):
                    continue  # "four" alone is in too many sentences to mean a needed fact
                show = sentence if len(sentence) < 70 else sentence[:67] + "..."
                if len(hit) >= 3 or (len(hit) >= 2 and len(hit) == len(key)):
                    errors.append(f"{path}: \"{show}\" looks like needed fact {fid} ({', '.join(hit)}). "
                                  "Needed facts stay out of copy until confirmed.")
                elif len(hit) == 2 or (hit and len(key) <= 2):
                    warnings.append(f"{path}: \"{show}\" shares words with needed fact {fid} ({', '.join(hit)}). "
                                    "Make sure it doesn't state it.")

    # Claim check 3, names and prices: a named program, course or body, or a price, from a needed fact.
    for fid, t in facts_text.items():
        if ledger.get(fid) != "needed":
            continue
        for m in PROPER.finditer(t):
            name = m.group(0)
            if name.lower() not in usable.lower() and name.lower() in copy.lower():
                errors.append(f"{path}: '{name}' comes from needed fact {fid}. It stays out of copy until confirmed.")
    flat_usable, flat_unusable = usable.replace(" ", ""), unusable.replace(" ", "")
    for price in sorted(set(PRICE.findall(copy))):
        p = price.replace(" ", "")
        if p in flat_usable:
            continue
        if p in flat_unusable:
            errors.append(f"{path}: {price} appears only in a needed fact. It stays out of copy until confirmed.")
        else:
            warnings.append(f"{path}: {price} isn't in any ledger fact. Prices come from the ledger or that event's registration page.")

    # The owner's account of what customers say is never presented as a customer's words.
    for feel in owner_accounts(sections):
        needle = squash(feel).strip(" .!?")
        if needle and needle in squash(copy):
            errors.append(f"{path}: uses \"{feel}\", the owner's account of what customers say (2.5). Never present it "
                          "as a customer's words. Quote only real reviews or testimonials, with the platform.")

    # Their own words: used only where the copy is about what they were talking about, and once per piece.
    paras = [re.sub(r"\s+", " ", para).lower() for para in re.split(r"\n\s*\n", copy) if para.strip()]
    for phrase, src, context, _ in own_words(sections):
        plain = re.sub(r"[\[\]]", "", phrase)
        needle = re.sub(r"\s+", " ", plain).lower().strip(" .")
        found = [para for para in paras if needle in para]
        if not found:
            continue
        uses = sum(para.count(needle) for para in paras)
        if uses > 1:
            errors.append(f"{path}: uses their phrase \"{phrase}\" {uses} times. Use each of their phrases at most "
                          "once per piece, or it becomes a catchphrase.")
        if "[" in phrase:
            errors.append(f"{path}: uses \"{plain}\", which has our fix for a probable mishearing. Check the recording first.")
        elif re.search(r"internal only", src, re.IGNORECASE):
            errors.append(f"{path}: uses \"{phrase}\", from a recording with no on-record consent (internal only). "
                          "Get their OK before it goes in public copy.")
        elif key_terms(context) and any(not key_terms(context) & (key_terms(para) - key_terms(plain)) for para in found):
            warnings.append(f"{path}: uses their phrase \"{phrase}\", but nothing in its paragraph matches what they said it "
                            f"about ({context}). Out of context? Cut it or move it.")
        else:
            warnings.append(f"{path}: uses their phrase \"{phrase}\". They said it about: {context or 'no context given'}. "
                            "Keep it only if this copy is about the same thing.")

    for phrase in AI_PATTERNS:
        if find(phrase, copy):
            warnings.append(f"{path}: '{phrase}' reads as AI-written (examples.md). Cut it unless it's needed.")


def check_proof(path, guide, version):
    """The credentials and awards list: a dated copy of 4.3, with wording, dates, sources and statuses from 4.1 and 4.2."""
    ledger, facts_text, dates, creds = guide["ledger"], guide["facts"], guide["dates"], guide["creds"]
    raw = read(path)
    if raw is None:
        return
    if "\u2014" in raw:
        errors.append(f"{path}: {raw.count(chr(0x2014))} em dash(es).")
    text = normalize(raw)
    m = re.search(r"version\s+(\d+(?:\.\d+)*)", text, re.IGNORECASE)
    if version and (not m or m.group(1) != version):
        warnings.append(f"{path}: doesn't say it was generated from guide version {version}. Regenerate it.")
    blocks, current = {}, None
    for line in text.splitlines():
        h = re.match(r"^##\s+(.+?)\s*$", line)
        if h:
            current = h.group(1).strip()
            blocks[current] = []
        elif current is not None:
            blocks[current].append(line)
    seen, rows_found = set(), 0
    for heading, lines in blocks.items():
        if "drop-in" in heading.lower():
            check_dropin(path, lines, ledger, facts_text)
            continue
        first = heading.lower().split()[0].strip(",")
        group = next((g for g in GROUPS if g.lower().split()[0].strip(",") == first), None)
        if group is None:
            errors.append(f"{path}: heading '{heading}' isn't one of the lists ({'; '.join(GROUPS)}) or the drop-in block.")
            continue
        for cells in table_rows(lines):
            rows_found += 1
            if len(cells) < 7:
                errors.append(f"{path}: row has {len(cells)} columns, expected 7: {cells}")
                continue
            fid, name, issuer, date, source, status, _use = cells[:7]
            if fid not in ledger:
                errors.append(f"{path}: {fid} isn't in the guide's ledger.")
                continue
            seen.add(fid)
            if fid not in creds:
                errors.append(f"{path}: {fid} isn't in guide 4.3. Add it there first; this list is generated from 4.3.")
            else:
                kind, c_issuer = creds[fid]
                if KIND_GROUP.get(kind) != group:
                    errors.append(f"{path}: {fid} is under '{heading}', but 4.3 lists it as '{kind}' "
                                  f"('{KIND_GROUP.get(kind, 'unknown')}').")
                if issuer.strip() != c_issuer.strip():
                    errors.append(f"{path}: {fid} issuer '{issuer}' doesn't match 4.3 ('{c_issuer}').")
            if name.strip("\"' ") != facts_text[fid].strip("\"' "):
                errors.append(f"{path}: {fid} wording doesn't match the ledger word for word. Regenerate it.")
            st = re.match(r"\W*(public|confirmed|needed)\b", status.lower())
            if not st or st.group(1) != ledger[fid]:
                errors.append(f"{path}: {fid} status '{status}' doesn't match the ledger ('{ledger[fid]}').")
            if fid in dates and date not in dates[fid]:
                errors.append(f"{path}: {fid} date '{date}' doesn't match 4.2 ({', '.join(sorted(dates[fid]))}).")
            elif fid not in dates and date.strip().lower() not in ("", "none", "n/a"):
                warnings.append(f"{path}: {fid} shows the date '{date}', but 4.2 has no row for it. Add the row or write 'None'.")
            if source.strip() != guide["sources"][fid].strip():
                errors.append(f"{path}: {fid} source doesn't match the ledger. Copy it from 4.1.")
    if not rows_found and creds:
        errors.append(f"{path}: no lists found. Use the headings in proof-map.md.")
    for fid in creds:
        if fid in ledger and fid not in seen:
            errors.append(f"{path}: {fid} is in guide 4.3 but not on this list. Regenerate it.")


def check_dropin(path, lines, ledger, facts_text):
    """Each drop-in line uses a public or confirmed fact's exact wording, and never a needed one."""
    usable = [t.strip(" .") for f, t in facts_text.items() if ledger.get(f) in ("public", "confirmed")]
    for line in lines:
        s = line.strip()
        if not s.startswith(("- ", "* ")):
            continue
        item = s[2:]
        for f, t in facts_text.items():
            if ledger.get(f) == "needed" and t.strip(" .") and t.strip(" .") in item:
                errors.append(f"{path}: the drop-in block uses {f}, a needed fact.")
        if not any(t and t in item for t in usable):
            errors.append(f"{path}: drop-in line '{item[:60]}' doesn't use a public or confirmed fact's exact wording.")


def squash(text):
    return re.sub(r"\s+", " ", normalize(text)).strip().lower()


def transcript_streams(text):
    """All speakers' text joined in order, and each speaker's text joined, minus timestamps and labels."""
    joined, by_speaker, who = [], {}, None
    for line in normalize(text).splitlines():
        s = line.strip()
        if not s or "-->" in s or re.fullmatch(r"\d+", s):
            continue
        for pat in TRANSCRIPT_LINE:
            m = pat.match(s)
            if m:
                who, s = m.group("who").strip(" *[]()").lower(), m.group("text").strip()
                break
        if not s:
            continue
        joined.append(s)
        if who is not None:
            by_speaker.setdefault(who, []).append(s)
    return [squash(" ".join(joined))] + [squash(" ".join(v)) for v in by_speaker.values()]


def is_our_notes(path, guide_path):
    base = os.path.basename(path).lower()
    if base in OUR_NOTES or base.startswith(OUR_NOTES_PREFIXES):
        return True
    if os.path.realpath(path) == os.path.realpath(guide_path):
        return True
    try:
        head = open(path, encoding="utf-8", errors="replace").read(3000)
    except OSError:
        return False
    return NOTES_MARKER in head.lower()


def loose(text):
    """Words only: for a quote whose source has a dash the guide can't keep."""
    return re.sub(r"\s+", " ", re.sub(r"[^\w'\[\]\s]", " ", squash(text))).strip()


def quote_found(q, corpora):
    """Word for word, except square brackets, which stand for up to four words we corrected."""
    sq = squash(q)
    if "[" not in sq:
        return any(sq in c for c in corpora)
    pattern, pos = "", 0
    for m in re.finditer(r"\[[^\]]*\]", sq):
        pattern += re.escape(sq[pos:m.start()]) + r"[\w'-]+(?:\s+[\w'-]+){0,3}"
        pos = m.end()
    rx = re.compile(pattern + re.escape(sq[pos:]))
    return any(rx.search(c) for c in corpora)


def check_sources(paths, sections, guide_path):
    """Every quoted phrase in 2.3, 2.5 and 3.6 must appear word for word in an original source (rule 3)."""
    files = []
    for p in paths:
        if not os.path.exists(p):
            warnings.append(f"--sources: {p} not found, skipped. Fine if that step was skipped (no AI raw files yet).")
            continue
        if os.path.isdir(p):
            for root, _dirs, names in os.walk(p):
                files += [os.path.join(root, n) for n in sorted(names) if n.lower().endswith(SOURCE_EXTS)]
        else:
            files.append(p)
    originals, notes = [], []
    for p in files:
        text = read(p) or ""
        if p.lower().endswith((".html", ".htm")):
            text = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", text)
            text = html.unescape(re.sub(r"<[^>]+>", " ", text))
        if is_our_notes(p, guide_path):
            notes.append(squash(text))
            warnings.append(f"--sources: ignored {p}. It's our own notes, not an original source.")
        else:
            originals += [squash(text)] + transcript_streams(text)
    if not originals:
        errors.append("--sources: no original sources given. Pass transcripts, saved pages or raw files.")
    loose_originals = [loose(c) for c in originals]
    for where, q in guide_quotes(sections):
        if not quote_found(q, originals) and quote_found(loose(q), loose_originals):
            warnings.append(f"{where}: \"{q}\" matches its source except for punctuation (a dash rewritten?). "
                            "Check that only the punctuation changed.")
            continue
        if quote_found(q, originals):
            if "[" in q:
                warnings.append(f"{where}: \"{q}\" has a bracketed fix for a probable mishearing. "
                                "Check it against the recording before it goes in public copy.")
            continue
        if quote_found(q, notes):
            errors.append(f"{where}: \"{q}\" is only in our own notes, not in any original source. "
                          "Quote only what's in a transcript, a saved page or their own writing.")
        else:
            errors.append(f"{where}: \"{q}\" isn't word for word in any original source given.")


def md_section(text, name):
    """Lines under a '## name' heading, up to the next '## ' heading."""
    out, on = [], False
    for line in text.splitlines():
        if re.match(r"^##\s+", line):
            on = line.lstrip("# ").lower().startswith(name.lower())
            continue
        if on:
            out.append(line)
    return out


def check_own_words(path, sections, guide_text, copy_path):
    """own-words.md: each phrase has its context; nothing it left out turns up in the guide or the copy."""
    if not os.path.isfile(path):
        if own_words(sections):
            errors.append(f"{path} not found, but 3.6 has phrases, so the Left out check didn't run. Fix the path.")
        else:
            warnings.append(f"{path} not found. Fine if own words were skipped; own-words checks not run.")
        return
    raw = read(path)
    if raw is None:
        return
    if "\u2014" in raw:
        errors.append(f"{path}: {raw.count(chr(0x2014))} em dash(es).")
    raw = normalize(raw)
    head = "\n".join(raw.splitlines()[:12]).lower()
    internal = "internal only" in head
    listed = []
    rows = table_rows(md_section(raw, "Phrases"))
    if not rows:
        warnings.append(f"{path}: no '## Phrases' table found.")
    for cells in rows:
        cells = cells + [""] * (4 - len(cells))
        m = re.search(r'"([^"]{3,})"', cells[0])
        if not m:
            continue
        short = m.group(1)[:50]
        listed.append(squash(m.group(1)))
        if len(words(cells[2])) < 3:
            errors.append(f"{path}: \"{short}\" has no Context. Record what they were talking about.")
        if re.search(r"call|video|recording|transcript|interview|meeting", cells[1], re.IGNORECASE) \
                and not re.search(r"\b\d{1,2}:\d{2}\b", cells[1]):
            warnings.append(f"{path}: \"{short}\" needs its timestamp (mm:ss).")
    for phrase, src, _context, _feeds in own_words(sections):
        if squash(phrase) not in listed:
            warnings.append(f"Section 3.6 \"{phrase[:50]}\" isn't in {path}'s Phrases table, with its context.")
        if internal and "internal only" not in src.lower():
            errors.append(f"Section 3.6 \"{phrase[:50]}\": the recording has no on-record consent. "
                          "Mark its Source 'internal only'.")
    texts = {"The guide": squash(guide_text)}
    if copy_path:
        copy_text = read(copy_path)
        if copy_text is not None:
            texts[copy_path] = squash(copy_text)
    for cells in table_rows(md_section(raw, "Left out")):
        m = re.search(r'"([^"]{6,})"', cells[0]) if cells else None
        if not m:
            continue
        line = squash(m.group(1)).strip(" .!?")
        why = cells[2] if len(cells) > 2 and cells[2] else "left out"
        if len(line.split()) < 3 and re.search(r"filler|fragment", why, re.IGNORECASE):
            continue  # "you know" or "kind of" turns up in ordinary sentences ("Did you know")
        for where, t in texts.items():
            if re.search(r"(?<!\w)" + re.escape(line) + r"(?!\w)", t):
                errors.append(f"{where} uses \"{m.group(1)}\", which {os.path.basename(path)} left out ({why}).")


def check_sheet(path, sections):
    raw = read(path)
    if raw is None:
        return
    if "\u2014" in raw:
        errors.append(f"{path}: {raw.count(chr(0x2014))} em dash(es).")
    sheet_items, current = [], None
    for line in normalize(raw).splitlines():
        if re.match(r"^\s{0,3}\d+\.\s+\S", line):
            current = [line]
            sheet_items.append(current)
        elif current is not None and line.strip():
            current.append(line)
    if not sheet_items:
        errors.append(f"{path}: no numbered items found.")
    if len(sheet_items) > SHEET_ITEMS_CAP:
        errors.append(f"{path}: {len(sheet_items)} items, cap {SHEET_ITEMS_CAP}. Turn the rest into defaults.")
    for i, item in enumerate(sheet_items, 1):
        body = " ".join(item)
        n = len(words(body))
        if n > SHEET_ITEM_WORDS:
            errors.append(f"{path}: item {i} is {n} words, cap {SHEET_ITEM_WORDS}.")
        if "We'd write:" not in body:
            errors.append(f"{path}: item {i} has no \"We'd write:\" draft. Draft, don't ask.")
        if "Needed for:" not in body:
            errors.append(f"{path}: item {i} has no \"Needed for:\" line.")
    if re.search(r"\bclients?\b", normalize(raw), re.IGNORECASE):
        warnings.append(f"{path}: says 'client'. The business reads this: use its name or 'you'.")
    listed = re.search(r"(\d+)\s+items?\b", labeled_line(sections.get(1, []), "Facts we need you to confirm") or "")
    if listed and int(listed.group(1)) != len(sheet_items):
        errors.append(f"Section 1.7 says {listed.group(1)} items, but {path} has {len(sheet_items)}.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("guide")
    ap.add_argument("--copy", help="a draft to check against the guide's never-use list, dates, ledger and own words")
    ap.add_argument("--credentials", "--proof", dest="proof", help="the credentials and awards list to check against 4.1 to 4.3")
    ap.add_argument("--sheet", help="the sign-off sheet to check against its caps and page 1")
    ap.add_argument("--sources", nargs="+", help="original sources (transcripts, saved pages, raw files, folders) "
                                                  "that quotes in 2.3, 2.5 and 3.6 must come from")
    ap.add_argument("--own-words", help="research/own-words.md: every phrase needs its context, and the lines "
                                        "it left out must not appear in the guide or the copy")
    args = ap.parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="replace")

    text = read(args.guide)
    if text is None:
        print(f"FAIL  {errors[0]}")
        sys.exit(1)
    sections, total, guide, version = check_guide(text)
    if args.proof:
        check_proof(args.proof, guide, version)
    if args.copy:
        check_copy(args.copy, sections, guide)
    if args.sheet:
        check_sheet(args.sheet, sections)
    if args.own_words:
        check_own_words(args.own_words, sections, text, args.copy)
    if args.sources:
        check_sources(args.sources, sections, args.guide)
    elif not args.copy and guide_quotes(sections):
        warnings.append("Quotes in 2.3, 2.5 or 3.6 weren't checked against a source. Add --sources with the "
                        "transcripts and saved pages (not our notes).")

    print(f"Guide: {args.guide}")
    print(f"Prose words (tables excluded): {total} of {TOTAL_CAP}")
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
