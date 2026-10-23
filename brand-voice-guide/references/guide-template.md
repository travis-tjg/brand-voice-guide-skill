# Guide template

This is the exact structure of the guide. Copy the template, fill it in, then delete every bracketed note. Keep the section numbers, the numbered labels (1.1, 1.2 and so on) and the headings, because writing jobs load sections by number and `scripts/check_guide.py` finds them by heading and label.

The numbered labels, the fact tables and the single date format are also there so AI writers can parse the guide. That part is a test, not a proven lift.

## Caps

These are caps, not targets, and no section has a minimum. If a section has nothing true to say, write "None yet."

| Section | Cap |
|---|---|
| 1. Sign-off page | 450 words |
| 2. The customer and the story | 400 words |
| 3. Voice | 450 words, plus a word table of up to 20 rows |
| 4. Proof ledger | 4.1 facts table of up to 40 rows, each fact up to 25 words; 4.2 dates table of up to 15 rows |
| 5. What AI looks for | table of up to 15 rows |
| 6. Shopper questions | table of up to 15 rows |
| 7. Consistent descriptions | short 160 characters, medium 300, long 750; profiles table up to 25 rows |
| 8. By type of work | 70 words per type of work |
| 9. Rulings | table of up to 30 rows |

Table rows don't count toward the word caps. Section 4 allows 80 words of prose and sections 5, 6 and 9 allow 60 each, for the notes above and below the tables. The 3.9 sample paragraph is up to 80 words, inside the section 3 cap. At every cap, the prose tops out at about 2,400 words; our test guides have come in between about 1,200 and 1,650.

## Template

```markdown
# [Business name]: brand voice guide

Version [n], [YYYY-MM-DD]. Master copy: [path]. Status: [Draft for sign-off / Signed off YYYY-MM-DD].

## 1. Sign-off page

Please read this page and tell us anything that's wrong. The rest of the guide is the detailed spec our writers follow, and you don't need to read it to sign off.

**1.1 Who you are.** [One sentence: who, what, where. Identical to the short description in 7.2.]

**1.2 Your customer.** [Up to 60 words: who they are and what's happening when they find you.]

**1.3 How we'll sound.** Like [the role from 3.2]. For example: "[one Do line from 3.4, copied exactly]"

**1.4 What we'll lead with.** These facts go everywhere, worded exactly like this:
- [Proof point in its exact wording] (F01)
- [3 to 5 in total, public or confirmed facts only]

**1.5 How working with you goes.**
1. [First step, verb first, up to 15 words]
2. [Second step]
3. [Third step]

**1.6 Words we'll never use.** [Up to 12 words or phrases, separated by commas.]

**1.7 Facts we need you to confirm.** [n] items, on the attached sheet. Until you confirm them, they stay out of everything we write.
- Sheet item 1: [label, up to 8 words]

**1.8 Your first pieces.** You'll approve the first [3 to 5] pieces we write. Any change you make becomes a rule in this guide.

## 2. The customer and the story

**2.1 The customer.** [Up to 80 words. Who they are, what they want, what just happened, what they're worried about. The customer is the hero and the client is the guide.]

**2.2 In their words.** [Up to 5 short phrases copied exactly from reviews, each with platform and month. "None found" is fine.]
- "[phrase]" ([platform], [YYYY-MM])

**2.3 The problem.**
- External: [what's wrong, one line]
- Internal: [how it makes them feel, one line]
- Philosophical: [why it shouldn't be this way, one line]

**2.4 What stops them.** [Up to 2 lines: the worry that delays the call (price, embarrassment, fear of an upsell), and the fact ID that answers it.]

**2.5 The guide.** Empathy: [one line that shows we understand]. Authority: [fact IDs only, e.g. F01, F03].

**2.6 The plan.** As on page 1 (1.5).

**2.7 Calls to action.** Primary: [the exact action and contact]. Transitional: [a lower-commitment step the client really offers, or "None"].

**2.8 Success.** [Up to 50 words: what life looks like after.]

**2.9 Stakes.** [Up to 50 words: what happens if they wait or choose badly. Facts, not fear. Any deadline or number cites its fact ID.]

## 3. Voice

**3.1 Who's reading.** [One sentence: the customer at the moment they read.]

**3.2 We sound like.** [One sentence that names a role, not adjectives.]

**3.3 We never sound like.** [One sentence naming the role the category defaults to, for example "a late-night TV ad for a law firm" or "a luxury spa brochure".]

**3.4 Rules.**
1. **[Do this], not [that].** Do: "[line]" Don't: "[line]"
2. [3 or 4 rules in total]

**3.5 Tone by page.** [Up to 4 lines, only for pages where the tone shifts.]
- [Emergency page: shortest sentences, the first step before anything about us.]

**3.6 In their own words.** [Up to 5 phrases the client really says, copied exactly, each with its source and date. "None yet" if we have no transcript or writing of theirs.]
- "[phrase]" ([call transcript / video / email / review reply], [YYYY-MM-DD])

**3.7 Words.**

| Use | Not | Why |
|---|---|---|
| [word] | [word] | [a few words] |

**3.8 Mechanics.** [One short paragraph: you and we, reading level, sentence and paragraph length, contractions, and how dates and numbers are written (as in 4.2).]

**3.9 Sample paragraph.** [Up to 80 words in this voice, for the page the customer reads most. It starts with the reader and uses public or confirmed facts only, with fact IDs in brackets.]

## 4. Proof ledger

Writers use public and confirmed rows only. Needed rows never appear in copy.

### 4.1 Facts

| ID | Fact (exact wording to use) | Source | Checked | Status |
|---|---|---|---|---|
| F01 | [up to 25 words] | [URL, or "client, email YYYY-MM-DD"] | [YYYY-MM-DD] | [public / confirmed / needed] |

### 4.2 Dates

One date per time-based fact, in one format. Every page, profile and schema block uses these dates, and copy never turns one into a count.

| Date fact | Date | Written in copy as | Fact |
|---|---|---|---|
| [License first issued] | [YYYY, YYYY-MM or YYYY-MM-DD] | [licensed since 2014] | F01 |

## 5. What AI looks for

From [N] runs on [engines], [dates]. Raw answers: [path]. This is what the engines told shoppers to check, not a ranking. [Or: "AI research skipped."]

| ID | Criterion | Runs | Neutral chat | Client's proof | Where it should appear |
|---|---|---|---|---|---|
| C1 | [criterion] | [n of N] | [yes / no] | [fact IDs, or "sheet item 2"] | [pages and profiles] |

Sources the engines cited: [kinds of sources]. The profiles in 7.5 should cover them.

## 6. Shopper questions

The questions the engines asked shoppers. Each one gets an answer somewhere on the site. [Or: "AI research skipped." plus questions from reviews and the client's own words, labeled as such.]

| ID | Question | Runs | Where we answer it | Facts used |
|---|---|---|---|---|
| Q1 | [as the engine asked it] | [n of N] | [URL or planned page, section or FAQ] | [fact IDs] |

## 7. Consistent descriptions

Each version starts with the one before it, so a small field gets the first sentence and a large one gets the whole text. The who-what-where sentence and every proof point keep this exact wording everywhere. If you're filling many directories and want variety, change the order of the other sentences, never the wording of a fact.

**7.1 Business details.**
- Name: [the real-world business name, as on signage and the state business record]
- Address: [exactly as on the GBP, or "Service-area business, address hidden"]
- Phone: [main line, the same everywhere]
- Website: [canonical URL]
- Primary category: [as on the GBP]
- Area served: [as on the GBP]

**7.2 Short (up to 160 characters):** [Who, what, where in one sentence. Same as 1.1.]

**7.3 Medium (up to 300 characters):** [The short version plus one sentence with the top proof points.]

**7.4 Long (up to 750 characters):** [The medium version plus services, areas and how to start.]

**7.5 Profiles.**

| Profile | URL | Status |
|---|---|---|
| [platform] | [URL] | [matches / fix / create] |

## 8. By type of work

For every job, when they conflict, the proof ledger wins, then the SEO brief, and the voice carries everything else. Every job also loads section 9. The SEO brief owns headings and target terms. In term-filling sections (FAQs, accordions) the terms win, and the voice carries the body copy. A term that is also a claim, like "best", appears only as the shopper's phrase, never as a claim about the business.

**8.1 Site pages.** Load sections 1 to 7. [Client-specific direction.]

**8.2 SEO content.** Load sections 1, 3, 4 and 6. [Client-specific direction.]

**8.3 Profiles and citations.** Load sections 4 and 7, and the proof list. [Client-specific direction.]

**8.4 Press releases.** Load sections 1, 3, 4 and 7. [Client-specific direction.]

**8.5 GBP posts.** Load sections 1 to 4 and 7. [Client-specific direction.]

**8.6 Email and social.** Load sections 1 to 4. [Client-specific direction.]

## 9. Rulings

Each change the client made to the first pieces, turned into a rule. Newest first. The section it changes is updated the same day.

| Date | Piece | What the client changed | The rule now | Updated |
|---|---|---|---|---|
| [YYYY-MM-DD] | [piece] | [what they changed, in their words] | [the rule] | [e.g. 3.4 rule 2] |
```

## How to fill each section

**Order.** Write section 4 first (4.1, then 4.2), then 5 and 6, then 7, 2, 3 and 8. Write page 1 last, because it summarizes the rest. Section 9 starts as "None yet."

**1. Sign-off page.** This is the one page the client reads.
- **1.1 Who you are:** a semantic triple: "[Business] is a [category] in [City, State] that [does what] for [whom]."
- **1.3 How we'll sound:** the role from 3.2 and one Do line from 3.4, copied exactly, so the client approves the voice by seeing it. If the new voice differs from their current site, this is where they find out.
- **1.4 What we'll lead with:** pick the proof points that answer the most-cited criteria in section 5. They must be public or confirmed. Use each fact's exact ledger wording, with no adjectives added.
- **1.5 How working with you goes:** say how the client really works, from the site, GBP, reviews and their own words. If you don't know a step, make it a sheet item.
- **1.6 Words we'll never use:** claims the ledger can't back ("best", "guaranteed", "24/7" when they aren't), filler the category repeats, and words customers wouldn't use. To find the filler, skim 3 to 5 competitor pages already in your Cora, Surfer or POP report and list the phrases most of them share. Record the phrases, not who ranks.
- **1.7 Facts we need you to confirm:** refer to sheet items by number and label only, never by fact ID. Once the sheet is answered, this list reads "None."

**2. Customer and story.** This is compact StoryBrand.
- **2.1 The customer:** build them from reviews, the client's own words and the questions engines ask shoppers. In an industry we don't know well, draft the customer and put it on the sign-off sheet, so the client gets the final say without having to write it.
- **2.3 Problem:** use the customer's own words where reviews give them.
- **2.4 What stops them:** take it from reviews ("I put off calling because...") and shopper questions. The answer must be a public or confirmed fact.
- **2.5 The guide:** authority cites fact IDs and never restates them, so a fact only lives in one place.
- **2.7 Calls to action:** a transitional CTA must be something the client actually offers.

**3. Voice.** We set the voice, and we write it for the client's customer, not to copy the client's current copy or how the owner talks. Use what reviewers say about how the client comes across, and the client's own words (`client-own-words.md`), as raw material: keep what helps the customer, drop what doesn't, and never promise a manner the reviews contradict.
- **3.2 We sound like:** a role, for example "a licensed tradesperson explaining the fix to a neighbor". Adjectives like "friendly and professional" don't tell a writer anything.
- **3.3 We never sound like:** the role the category drifts into. A contrast gives a writer a much sharper target than a role alone.
- **3.4 Rules:** each rule is a voice choice someone can check: how the client sounds, not which facts they use, because the ledger and the never-use list already cover facts. Choose what fits this client's customer: how plainly we name the reader's worry; whether we explain the trade's terms or skip them; "I", "we" or the owner's name; how we talk about price; how much warmth or humor; how fast we get to the point; naming who does the work. Test the set: if every rule would fit the closest competitor's guide just as well, the voice isn't set yet.
- **Do and Don't lines:** use public or confirmed facts only, and start Do lines with the reader, not the business. Writers copy examples, so an example built on a guess teaches guessing.
- **3.5 Tone by page:** only where the tone really shifts, such as an emergency page, a price page or the about page.
- **3.6 In their own words:** copied exactly from a transcript, recording or the client's own writing, with the source. Never tidy a quote, and never quote anything that isn't in a source. A phrase here shows how they talk; a claim inside it ("nine times out of ten") still needs a ledger row before copy states it.
- **3.7 Words:** the customer's word next to the trade's word ("water in the basement", not "water intrusion"), and plain verbs over corporate ones ("fix", not "remediate"). Claims the ledger can't back go on the 1.6 never-use list, not here.
- **3.9 Sample paragraph:** the strongest thing a writer can copy, because it shows rhythm, not just word choice. Write it last, from the rules.

**4. Proof ledger.** One row per fact. Every other section cites the ID instead of restating the fact.
- **Wording:** write each fact the way it will appear in copy. Name each credential exactly as the issuer does. Exact wording means the fact's terms stay fixed: the credential's name, the date, the place. On site pages, the sentence around them follows the voice.
- **Status:** conflicting sources make a fact needed. So does anything found only in a third-party directory or an AI answer.
- **No memory:** nothing goes in the ledger from a model's own knowledge.
- **4.2 Dates:** one row for every time-based fact (licensed, founded, certified, awarded, joined). The Date column uses one format: YYYY-MM-DD, or YYYY-MM or YYYY when the source shows no more. The year must match the year in the fact's 4.1 wording. "Written in copy as" anchors to the date ("licensed since 2014"), never a count ("over 10 years"). Page dates follow the same rule: the date shown on a page should match its schema, sitemap and RSS dates, in one format. That's a site task; note it in 8.1 if it applies. Fact tables for credentials and dates on published pages are the same idea. All of this is a test, not a proven lift.
- **More:** see `proof-map.md`.

**5 and 6. AI criteria and shopper questions.** Copy these from `research/ai-criteria/summary.md`.
- **Section 5:** list a criterion only if the client has proof for it, or might (in which case it goes on the sheet). Criteria the client doesn't meet stay in the summary. "Neutral chat" says whether the engine named the criterion in the "how do I choose" chat, before we named any categories; those are the stronger signal.
- **Section 6:** skip questions about things the client doesn't offer.
- **Skipped:** write "AI research skipped." in both sections. Section 6 can still list questions from reviews and the client's own words, labeled as coming from there.

**7. Consistent descriptions.**
- **Name:** use the real-world business name, as on signage and the state business record, never a GBP name with keywords added. Take the address and phone from the GBP. If the GBP, the site and the record disagree, make it a sheet item. If the GBP shows a call-tracking number, list the main line here and use it on every citation.
- **Descriptions:** build them as triples (who, what, where), and use the same proof points with the same wording everywhere. This follows the local SEO rule: keep the entity triples identical, and vary only sentence order. Check each version against its field's limit; the GBP description allows 750 characters.
- **7.5 Profiles:** list every official profile, plus the directories and profile sites the engines cited, even where the client has no profile yet. Award and rating sites aren't profiles anyone can create: list one only if the client already holds that award or rating. Membership and licensing directories from the proof list belong here too.

**8. By type of work.** Up to 70 words each, for direction specific to this client. For example: "Every service page names who does the work", or "Prices appear only as listed on F07". Don't repeat general writing advice. Refer to unconfirmed facts by sheet item ("hold sheet item 2"), never by fact ID; the checker treats a needed fact ID here as copy.

**9. Rulings.** The client approves the first 3 to 5 pieces. For each change they make, ask what rule it implies, write the rule, and update the section it changes (a 3.4 rule, the 1.6 list, a 4.1 row) the same day. "What the client changed" is their own words or the before and after. If they push back on the voice, ask which line felt wrong and change the rule behind it. Turn adjectives they give you ("more premium") into a role and a do and don't line, and check it against the customer before using it. Bump the version after each ruling.
