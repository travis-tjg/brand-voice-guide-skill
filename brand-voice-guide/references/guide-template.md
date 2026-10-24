# Guide template

This is the exact structure of the guide. Copy the template, fill it in, then delete every bracketed note. Keep the section numbers, the numbered labels (1.1, 1.2 and so on) and the headings, because writing jobs load sections by number and `scripts/check_guide.py` finds them by heading and label.

The numbered labels, the fact tables and the single date format are also there so AI writers can parse the guide. That part is a test, not a proven lift.

## Caps

These are caps, not targets, and no section has a minimum. If a section has nothing true to say, write "None yet."

| Section | Cap |
|---|---|
| Whole guide | 2,500 words of prose |
| 1. Sign-off page | 450 words |
| 2. The customer and the story | 450 words. 2.2 and 2.7 up to 4 items each. 2.5 table up to 5 rows, 2.12 up to 4. 2.13 up to 5 programs of up to 60 words each, 300 in all, counted on their own |
| 3. Voice | 600 words. 3.4 up to 5 rules, each with up to 3 Do lines. 3.6 table up to 5 rows, 3.7 up to 20. 3.10 up to 3 questions |
| 4. Proof ledger | 100 words of prose. 4.1 up to 40 facts of up to 25 words each. 4.2 up to 15 dates. 4.3 up to 25 rows |
| 5. What AI looks for | 60 words, table up to 15 rows |
| 6. Shopper questions | 60 words, table up to 15 rows |
| 7. Consistent descriptions | short 160 characters, medium 300, long 750; profiles table up to 25 rows |
| 8. By type of work | 70 words per type of work. 8.7 up to 6 page types of up to 90 words each. 8.8 up to 8 checks |
| 9. Rulings | 60 words, table up to 30 rows |

Table rows don't count toward the word caps. The 3.9 sample paragraph is up to 80 words, inside the section 3 cap. If every section hit its cap the guide would pass 2,500 words, so the whole-guide cap is the one that binds: spend the words on the voice and cut elsewhere. Our test guides have come in between about 1,200 and 2,200.

## Template

```markdown
# [Business name]: brand voice guide

Version [n], [YYYY-MM-DD]. Master copy: [path]. Status: [Draft for sign-off / Signed off YYYY-MM-DD].

## 1. Sign-off page

Please read this page and tell us anything that's wrong. The rest of the guide is the detailed spec our writers follow, and you don't need to read it to sign off.

**1.1 Who you are.** [One sentence: who, what, where. Identical to the short description in 7.2.]

**1.2 Your customer.** [Up to 60 words: who they are and what's happening when they find you. With several programs, one line each.]

**1.3 How we'll sound.** Like [the role from 3.2]: [the pairs from 3.4]. For example: "[one Do line from 3.4, copied exactly]" Does this sound like you talking to a customer? Tell us what doesn't.

**1.4 What we'll lead with.** These facts go everywhere, worded exactly like this:
- [Proof point in its exact wording] (F01)
- [Up to 5 in total, public or confirmed facts only]

**1.5 How working with you goes.**
1. [First step, verb first, up to 15 words]
2. [Second step]
3. [Third step]

**1.6 Words we'll never use.** [Up to 12 words or phrases, separated by commas.]

**1.7 Facts we need you to confirm.** [n] items, on the attached sheet. Until you confirm them, they stay out of everything we write.
- Sheet item 1: [label, up to 8 words]

**1.8 Your first pieces.** You'll approve the first [n, up to 5] pieces we write. Any change you make becomes a rule in this guide.

## 2. The customer and the story

**2.1 The customer.** [Up to 80 words. Who they are, what they want, what just happened, what they're worried about. The customer is the hero and the business is the guide.]

**2.2 The customer is never.**
- [Up to 4 short items: who this business isn't for, and how we never portray the customer.]

**2.3 In their words.** [Up to 5 short phrases copied exactly from reviews, each with platform and month. "None found" is fine.]
- "[phrase]" ([platform], [YYYY-MM])

**2.4 The problem.**
- External: [what's wrong, one line]
- Internal: [how it makes them feel, one line]
- Philosophical: [why it shouldn't be this way, one line]

**2.5 What they feel and how we answer.** On the page, the feeling comes first, then the answer.

| Customer feels | Source | How we answer | Copy line |
|---|---|---|---|
| ["their words, verbatim", or our reading without quotation marks] | [review, YYYY-MM / Q2 / owner's account, call, mm:ss / our reading of Q3] | [fact IDs] | [one line a writer can use] |

**2.6 The guide.** Empathy: [one line that shows we understand]. Authority: [fact IDs only, e.g. F01, F03].

**2.7 We are never.**
- [Up to 4 short items: roles the business never plays in the story.]

**2.8 The plan.** As on page 1 (1.5).

**2.9 Calls to action.** Primary: [the exact action and contact]. Transitional: [a lower-commitment step the business really offers, or "None"].

**2.10 Success.** [Up to 50 words: what life looks like after.]

**2.11 Stakes.** [Up to 50 words: what happens if they wait or choose badly. Facts, not fear. Any deadline or number cites its fact ID.]

**2.12 Reader states.** [Only the states this business sees, up to 4.]

| State | How we handle it | Pages that serve it |
|---|---|---|
| [No one yet / Has a default that's fine / Loyal to someone / Stuck or in crisis] | [one line] | [pages] |

**2.13 Programs and audiences.** [Only for an organization with several programs, brands, practice areas, locations or audiences. Otherwise "None: one program."]
- **[Program name].** Who: [who it's for]. Differs: [what changes from the master voice]. Proof: [fact IDs]. CTA: [its own action].

## 3. Voice

**3.1 Who's reading.** [One sentence: the customer at the moment they read.]

**3.2 We sound like.** [One sentence that names a role, not adjectives.]

**3.3 We never sound like.** [One sentence naming the role the category defaults to, for example "a late-night TV ad for a law firm" or "a luxury spa brochure".]

**3.4 Rules.** Each rule is a pair: the trait, but not the way it goes wrong.
1. **[Trait], but not [the trait overdone].** [What it means here, one line.] Do: "[line]" Don't: "[the same fact, overdone]" From: [their pattern, with two or three timestamps / what reviewers say, with the month / our call, for the customer: why]
   - [Optional, up to 2 more per rule, each for a different moment:] Do: "[line]" Don't: "[the same fact, overdone]"
2. [Up to 5 rules. Two that are really theirs beat five that would fit anyone.]

**3.5 Tone by page.** [Up to 4 lines, only for pages where the tone shifts.]
- [Emergency page: shortest sentences, the first step before anything about us.]

**3.6 In their own words.** Use a phrase only where the copy is about what they were talking about. [Up to 5 phrases, or "None yet" if we have no transcript or writing of theirs.]

| Phrase | Source | Context: what they were talking about | Feeds |
|---|---|---|---|
| "[phrase, verbatim]" | [call, YYYY-MM-DD, mm:ss] | [the subject, in a few words] | [3.4 rule 2] |

**3.7 Words.**

| Use | Not | Why |
|---|---|---|
| [word] | [word] | [a few words] |

**3.8 Mechanics.** [One short paragraph: who says "I" and who says "we", and how the owner is named; the reading level for each audience, with the reason; sentence and paragraph length; contractions; and how dates and numbers are written (as in 4.2).]

**3.9 Sample paragraph.** [Up to 80 words in this voice, for the page the customer reads most. It starts with the reader and uses public or confirmed facts only, with fact IDs in brackets.]

**3.10 Questions we raise.** We never name a competitor, only the type. We respect the reader's past choice, ask questions they answer for themselves, and raise only what this business visibly meets. [Up to 3, or "None yet."]
1. "[a question the reader asks themselves]" Raises: [C2]. Answer: [F01, F04].

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

### 4.3 Credentials and awards

Name, date, source and status come from 4.1 and 4.2. The credentials and awards list is generated from this table.

| ID | List | Issuer (as it names itself) | Show on |
|---|---|---|---|
| F01 | [award / certification / license / credential / study / training / course / membership / position / education] | [issuing body] | [bio credentials section, footer, profiles, owned pages] |

## 5. What AI looks for

From [N] runs on [engines], [dates]. Raw answers: [path]. This is what the engines told shoppers to check, not a ranking. [Or: "AI research skipped."]

| ID | Criterion | Runs | Neutral chat | Proof | Where it should appear |
|---|---|---|---|---|---|
| C1 | [criterion] | [n of N] | [yes / no] | [fact IDs, or "sheet item 2"] | [pages and profiles] |

Sources the engines cited: [kinds of sources]. The profiles in 7.5 should cover them.

## 6. Shopper questions

The questions the engines asked shoppers. Each one gets an answer somewhere on the site. [Or: "AI research skipped." plus questions from reviews and the owner's own words, labeled as such.]

| ID | Question | Runs | Where we answer it | Facts used |
|---|---|---|---|---|
| Q1 | [as the engine asked it] | [n of N] | [URL or planned page, section or FAQ] | [fact IDs] |

## 7. Consistent descriptions

Each version starts with the one before it, so a small field gets the first sentence and a large one gets the whole text. The who-what-where sentence and every proof point keep this exact wording everywhere. If you're filling many directories and want variety, change the order of the other sentences, never the wording of a fact.

**7.1 Business details.**
- Name: [the real-world business name, as on signage and the state business record]
- Address: [exactly as on the GBP, "Service-area business, address hidden", or "No fixed address: each event page lists its venue"]
- Phone: [main line, the same everywhere, or "None published"]
- Website: [canonical URL]
- Primary category: [as on the GBP, or "No Google Business Profile"]
- Area served: [as on the GBP, or the region the events cover]

**7.2 Short (up to 160 characters):** [Who, what, where in one sentence. Same as 1.1.]

**7.3 Medium (up to 300 characters):** [The short version plus one sentence with the top proof points.]

**7.4 Long (up to 750 characters):** [The medium version plus services and areas. No phone number, link, price or promotion, and no "call us" line: the phone and website have their own fields, and Google's Business Profile rules bar links, prices, promotions and direct calls to action in the listing.]

**7.5 Profiles.**

| Profile | URL | Status |
|---|---|---|
| [platform] | [URL] | [matches / fix / create] |

## 8. By type of work

For every job, when they conflict, the proof ledger wins, then the SEO brief, and the voice carries everything else. Every job also loads section 9 and passes 8.8 before it ships. The SEO brief owns headings and target terms. In term-filling sections (FAQs, accordions) the terms win, and the voice carries the body copy. A term that is also a claim, like "best", appears only as the shopper's phrase, never as a claim about the business.

**8.1 Site pages.** Load sections 1 to 7. [Client-specific direction.]

**8.2 SEO content.** Load sections 1, 3, 4 and 6. [Client-specific direction.]

**8.3 Profiles and citations.** Load sections 4 and 7, and the credentials and awards list. [Client-specific direction.]

**8.4 Press releases.** Load sections 1, 3, 4 and 7. [Client-specific direction.]

**8.5 GBP posts.** Load sections 1 to 4 and 7. [Client-specific direction, or "None: no Google Business Profile."]

**8.6 Email and social.** Load sections 1 to 4. [Client-specific direction.]

**8.7 Page blueprints.** [Only the page types this work includes, up to 6.]
- **[Home].** First: [what goes first]. Beat: [the StoryBrand beat]. Proof: [fact IDs, and where they sit]. Poor: "[a generic line]" Good: "[a line in this voice]"

**8.8 Before anything ships.** Every answer must be yes.
1. [Does it open with the reader's situation, not with us?]
2. [Up to 8 checks in total, built from this guide]

## 9. Rulings

Each change the client made to the first pieces, turned into a rule. Newest first. The section it changes is updated the same day.

| Date | Piece | What the client changed | The rule now | Updated |
|---|---|---|---|---|
| [YYYY-MM-DD] | [piece] | [what they changed, in their words] | [the rule] | [e.g. 3.4 rule 2] |
```

## How to fill each section

**Order.** This is the write order; the template above is the read order. Write section 4 first (4.1, 4.2, 4.3), then 5 and 6, then 7, 2, 3 and 8. Write page 1 last, because it summarizes the rest. Section 9 starts as "None yet."

**Words.** In this skill, "client" means the business the guide is for, signed or not. In anything the business reads (page 1, the sheet, the email), use its name or "you", never "client" or "prospect".

**Example lines.** The guide shows writers about 15 example sentences (1.3, the Do and Don't lines, the 2.5 copy lines, 3.9 and the 8.7 Poor and Good lines). Make each one a different sentence; only the 1.3 line repeats, copied from 3.4. Writers copy what they see most, so a sentence that appears five times ends up on every page. Facts repeat in their ledger wording; sentences don't. Vary the openers: at most one of them opens with a question. Each of their 3.6 phrases appears in one example at most. The checker warns on repeats.

**1. Sign-off page.** This is the one page the business reads.
- **1.1 Who you are:** a semantic triple: "[Business] is a [category] in [City, State] that [does what] for [whom]." An organization names itself and its main programs: "[Org] runs [program] and [program] in [region]."
- **1.3 How we'll sound:** the role from 3.2, the pairs from 3.4 and one Do line copied exactly, so they approve the voice by seeing it. Pick the Do line that shows the voice most, not the one with the most facts. If the new voice differs from their current site, this is where they find out. The closing question asks them to react to a line we wrote, never to describe their voice; keep it word for word.
- **1.4 What we'll lead with:** the proof points that answer the most-cited criteria in section 5. Public or confirmed only, in each fact's exact ledger wording, with no adjectives added.
- **1.5 How working with you goes:** how the business really works, from the site, GBP, reviews and their own words. If you don't know a step, make it a sheet item.
- **1.6 Words we'll never use:** claims the ledger can't back ("best", "guaranteed", "24/7" when they aren't), filler the category repeats, and words customers wouldn't use. To find the filler, skim up to 5 competitor pages already in your Cora, Surfer or POP report and list the phrases most of them share. Record the phrases, not who ranks.
- **1.7 Facts we need you to confirm:** sheet items by number and label only, never by fact ID. Once the sheet is answered, this reads "None."

**2. Customer and story.** Compact StoryBrand: the customer is the hero, the business is the guide.
- **2.1 The customer:** from reviews, the owner's own words and the questions engines ask shoppers. In an industry we don't know well (or the part of the work we don't), draft the customer and put it on the sign-off sheet.
- **2.2 The customer is never:** who this business isn't for (a job they don't take, a buyer they can't serve well) and how we never portray the customer, such as never naive, helpless or foolish for waiting. Copy never says these out loud; they tell the writer who not to write for. Services they don't offer still never appear in copy (rule 8), and anything we're unsure of stays needed on the sheet rather than guessed.
- **2.3 In their words:** save the page each phrase came from in `research/pages/`, so the quote check has an original.
- **2.4 Problem:** use the customer's own words where reviews give them.
- **2.5 What they feel and how we answer:** the customer's top worries, up to 5, including the one that delays the call (price, embarrassment, fear of an upsell). The feeling comes from reviews, a section 6 question, or what the owner says customers tell them (with the timestamp). Quotation marks mean verbatim; otherwise write "our reading" in the Source column. What the owner says customers tell them is the owner's account: write "owner's account" in its Source (the checker fails a quoted retelling without it). It shows the worry; it is never quoted on a page as a customer's words. Only a real review or testimonial is quoted as a customer, with its platform. On the page, write the feeling as the reader's situation ("Water in the basement again?"), not as a quote. "How we answer" cites public or confirmed fact IDs only; a worry with no ledgered answer stays out, or its answer goes on the sheet. The copy line uses the same facts. On the page the feeling comes before the answer.
- **2.6 The guide:** authority cites fact IDs and never restates them, so a fact lives in one place.
- **2.7 We are never:** roles the business never plays in the story, such as the hero of the page, a closer who disappears after the sale, or a lecturer. 3.3 is different: it names the voice the category drifts into.
- **2.9 Calls to action:** a transitional CTA must be something the business actually offers.
- **2.12 Reader states:** how tied the reader is to their current option. List only the states this business sees:
  - **No one yet** (first-time need, new to the area): they compare. Explain plainly and show proof. Service, program and location pages.
  - **Has a default that's fine:** they aren't looking. Raise a 3.10 question that makes a gap visible, then answer it. Home, pricing and policy pages.
  - **Loyal to someone:** don't chase, and never knock their choice. Be visible and credible for the day that changes. Profiles (7.5) and reviews.
  - **Stuck or in crisis:** they want out and can't see how. Remove the barrier with the first step, the price or the guarantee the ledger shows. An emergency or "start here" page.
- **2.13 Programs and audiences:** for one organization running several programs, brands, practice areas, locations or audiences (a summer camp and a school program, a firm with three practice areas, two locations). Section 3 is the one master voice. Each program gets one line: who it's for, what differs (tone, reading level, a word or two), its own proof (fact IDs from the one ledger) and its own CTA. If a program is really a separate brand with its own name and site, give it its own guide.

**3. Voice.** We set the voice, and we write it for the customer, not to copy the current site or how the owner talks. Use what reviewers say about how the business comes across, and the owner's own words (`client-own-words.md`), as raw material: keep what helps the customer, drop what doesn't, and never promise a manner the reviews contradict.
- **3.2 We sound like:** a role, for example "a licensed tradesperson explaining the fix to a neighbor". Adjectives like "friendly and professional" don't tell a writer anything.
- **3.3 We never sound like:** the role the category drifts into. A contrast is a sharper target than a role alone.
- **3.4 Rules:** each rule is a pair, the trait and the way it goes wrong: "direct, but not harsh", "warm, but not gushing", "confident, but not boastful". These are placeholders; use one only if their words or reviews show it. The pair in bold, one line on what it means here, then a Do line showing the first half and a Don't line showing the second half: the trait taken too far, the near miss a writer trying to follow the rule would actually produce (for "calm, but not slow", a padded, over-reassuring line). Not category hype; 3.3 and 1.6 already rule that out. Write the Do and the Don't on the same fact, so the only difference is the voice. Each pair is a voice choice someone can check (how plainly we name the worry, how we talk about price, how much warmth, how fast we get to the point, who we name), not which facts we use.
- **From:** each rule ends with where the choice came from: a pattern in their own words with two or three timestamps ("From: a flat promise, then a short kicker, 04:30, 13:30, 18:00"), what reviewers say about how they come across (with the month), or "our call, for the customer: [why]". Where their words show a pattern that fits the customer, at least one rule's From is that pattern, and the pair sounds like it: if they talk in short, flat promises, the rule isn't "calm". Never bend a line into a rule to fill the slot; if their words hold nothing that travels, every From says "our call". Test the set: if every pair would fit the closest competitor's guide just as well, or a From line points to our own copy, the voice isn't set yet.
- **Do and Don't lines:** public or confirmed facts only, and Do lines start with the reader. A rule may have up to 3 Do lines, each for a different moment (a headline, a price line, a reply to a worry), each with its own Don't on the same fact. Writers copy examples, so an example built on a guess teaches guessing.
- **3.5 Tone by page:** only where the tone really shifts, such as an emergency page, a price page or the about page.
- **3.6 In their own words:** follow `client-own-words.md`. Each phrase is verbatim, with the timestamp, the context (what they were talking about) and the rule it feeds. A writer uses a phrase only where the copy is about the same thing, and at most once per piece. Their patterns go everywhere; their lines go in one or two places, or they become a catchphrase the client hears back on every page. Leave out fragments, filler, jokes, sarcasm, personal talk and lines that only make sense mid-conversation. A phrase that feeds no rule comes out. Square brackets mark our fix for a probable mishearing, and that phrase stays out of public copy until someone checks the recording. A claim inside a phrase ("nine times out of ten") still needs a ledger row before copy states it.
- **3.7 Words:** the customer's word next to the trade's word ("water in the basement", not "water intrusion"), and plain verbs ("fix", not "remediate"). Claims the ledger can't back go on the 1.6 list, not here.
- **3.8 Mechanics:** pronouns by section: by default "I" in owner-voiced sections (about, bio, a note from the owner) and "we" in service and policy copy; a firm with several people may use "we" throughout. Reading level per audience, with the reason, for example "injury callers: grade 5, because they're stressed and reading on a phone; adjusters: grade 10, because they read for detail." One number for every audience is a guess. Sentence shape comes from the "Pacing and register" notes in own-words.md: how they open an answer, how long they run, how they finish. With no own words, write it for the customer and say so. If this paragraph would fit another client's guide word for word, it's our house style, not their voice.
- **3.9 Sample paragraph:** the strongest thing a writer can copy, because it shows rhythm, not just word choice. Write it last, from the rules.
- **3.10 Questions we raise:** for readers with a default (2.12). Turn up to 3 criteria the engines told shoppers to check (section 5) into questions the reader answers for themselves, for example "Who will actually be at your court date?" Each cites the criterion and the fact IDs that answer it. Never name a competitor; describe the type. Acknowledge the past choice first ("that made sense when you chose it"). Questions, not accusations. Raise a criterion only if this business visibly meets it. If AI research was skipped, use section 6 questions from reviews or their own words, or write "None yet."

**4. Proof ledger.** One row per fact. Every other section cites the ID instead of restating the fact.
- **Wording:** write each fact the way it will appear in copy. Name each credential exactly as the issuer does. The fact's terms stay fixed (the name, the date, the place); on a page, the sentence around them follows the voice.
- **Status:** conflicting sources make a fact needed. So does anything found only in a third-party directory, an AI answer or a call where nobody put the fact to the owner.
- **Changing facts:** for prices, dates and venues that change per event or season, write the row as "Each event's price, date and venue: as on its registration page" and cite that page. Copy takes them from there, never from memory.
- **No memory:** nothing goes in the ledger from a model's own knowledge.
- **4.2 Dates:** one row for every time-based fact (licensed, founded, certified, awarded, joined). The Date column uses one format: YYYY-MM-DD, or YYYY-MM or YYYY when the source shows no more, and its year matches the fact's 4.1 wording. An award won in two years is two facts, so each has one date. "Written in copy as" anchors to the date ("licensed since 2014"), never a count ("over 10 years"). The date shown on a page should match its schema, sitemap and RSS dates; that's a site task for 8.1. Fact tables on published pages are the same idea, and all of it is a test, not a proven lift.
- **4.3 Credentials and awards:** one row for each award, certification, license, credential, published study, training, course, membership or position in 4.1. "List" sorts it into one of four lists on the export. The issuer is named as it names itself. Real awards count even if they were paid for or are a vanity award, as long as they're named exactly with the year; just don't let one be the only credential (the checker warns). "Show on" says where it goes: the bio page's credentials section, a proof strip or the footer, profiles (7.5), owned pages such as an association member page or a BBB page. Proof sits near every headline but never is the headline. The export: `proof-map.md`.

**5 and 6. AI criteria and shopper questions.** Copy these from `research/ai-criteria/summary.md`.
- **Section 5:** list a criterion only if the business has proof for it, or might (then it goes on the sheet). Criteria they don't meet stay in the summary. "Neutral chat" says whether the engine named the criterion in the "how do I choose" chat, before we named any categories; those are the stronger signal.
- **Section 6:** skip questions about things the business doesn't offer.
- **Skipped:** write "AI research skipped." in both sections. Section 6 can still list questions from reviews and their own words, labeled as coming from there.

**7. Consistent descriptions.**
- **Name:** the real-world business name, as on signage and the state business record, never a GBP name with keywords added. Address and phone from the GBP. If the GBP, the site and the record disagree, make it a sheet item. If the GBP shows a call-tracking number, list the main line here and use it on every citation.
- **No storefront:** for an event, pop-up or mobile business with no GBP or public address, say so in 7.1 and never publish a personal number or a home address. Each event page carries its own venue.
- **Descriptions:** triples (who, what, where), the same proof points in the same wording everywhere. Keep the triples identical and vary only sentence order. Check each version against its field's limit; the GBP description allows 750 characters. No phone number, link, price, promotion or call to action in any version: Google's Business Profile rules bar them, and the phone and website have their own fields. The CTA lives in 2.9 and on the page. The checker fails a phone number, link or price here and warns on a call to action.
- **7.5 Profiles:** every official profile, plus the directories and profile sites the engines cited, even where the business has no profile yet. Award and rating sites aren't profiles anyone can create: list one only if the business already holds that award or rating. Membership and licensing directories from 4.3 belong here too.

**8. By type of work.** Up to 70 words each, for direction specific to this business, for example "Every service page names who does the work" or "Prices appear only as listed on F07". Don't repeat general writing advice. Refer to unconfirmed facts by sheet item ("hold sheet item 2"), never by fact ID; the checker treats a needed fact ID here as copy.
- **8.2 SEO content:** the section 6 questions and the 3.10 questions are also content ideas for shoppers whose default has stopped working, such as "what to ask any [trade] before you hire one", built so every criterion it lists is one the business visibly meets. No formulas here; the SEO brief owns headings and terms.
- **8.7 Page blueprints:** only the page types this work includes (home, service or program, location, about, blog or resource, event, FAQ), up to 6. Each says what goes first, the StoryBrand beat it carries, which proof and where, then one Poor line and one Good line. The Poor line is what a model would write from the facts alone, without the voice ("At [Business], we understand every customer is different."), not an obvious ad. The Good line is a new sentence, not one used elsewhere in the guide. The usual order for a page that sells: the reader's situation (a 2.5 feeling), a 3.10 question if the page serves readers with a default, the answer with proof, then the CTA. The headline starts with the reader; proof sits just under it, in a proof strip, a sidebar and the footer. Event pages put the date, venue and price first, from that event's registration page.
- **8.8 Before anything ships:** up to 8 yes/no questions built from this guide, not general advice: the 3.4 pairs, the 1.6 words, the 2.2 portrayal, the 3.6 context rule and the facts. The last one is always some form of: would the owner read it and say "yes, that's how I'd say that"?

**9. Rulings.** The client approves the first pieces, up to 5. For each change they make, ask what rule it implies, write the rule, and update the section it changes (a 3.4 pair, the 1.6 list, a 4.1 row) the same day. "What the client changed" is their own words or the before and after. If they push back on the voice, ask which line felt wrong and change the rule behind it. Turn adjectives they give you ("more premium") into a pair and a Do and Don't line, and check it against the customer before using it. A refresh from a later call (`client-own-words.md`) is logged here too. Bump the version after each ruling.
