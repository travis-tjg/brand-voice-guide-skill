---
name: brand-voice-guide
description: Use when building a client's brand voice or tone of voice guide in any industry, or writing or checking copy with one. Makes a capped guide, a sign-off sheet and a credentials and awards list.
---

# Brand voice guide

Version 1.2, 2026-10-24.

Build one guide per client at onboarding. Every writing job for that client loads it from then on: site pages, SEO content, profiles and citations, press releases, GBP posts, email and social.

A brand voice guide writes down how the client speaks and how they don't. It has three jobs:

1. **Unique.** The copy sounds like this client, not like every other site in the category: who they sound like and never sound like, voice rules as pairs ("direct, but not harsh") with do and don't lines, their own words used in context, words they never use, and how the tone shifts by page.
2. **Converts.** The copy is written to the client's customer, who is the hero: what they feel, a simple plan, one call to action, and the stakes without scare tactics (StoryBrand, Donald Miller's framework).
3. **Accurate.** The writer gets real, specific, dated facts, so it doesn't have to guess. Each draft's facts are matched to the ledger, and the checker catches the common slips (year counts, never-use words, unconfirmed facts, lines used out of context); a person checks the rest. As a side benefit, the same facts stated the same way everywhere give AI answer engines a consistent picture of the client. That part is a test, not a promise.

Voice comes first. The research steps exist to feed it real facts, the customer's real words and the client's own words.

It works for any industry: a DUI defense attorney, a plumbing company, a med spa, a youth sports organization. Nothing here assumes an industry. There are no industry rulebooks and no stock offers. If the client doesn't offer something, neither the guide nor the copy mentions it.

"Client" in this skill means the business the guide is for, signed or not. In anything they read, use the business name or "you".

## Outputs

All saved in the folder chosen at intake, by default `<client-folder>/brand/` (for a prospect, wherever the user keeps prospects):

| File | What it is |
|---|---|
| `voice-guide.md` | The guide, and the one master copy. Structure and caps: `references/guide-template.md`. |
| `signoff-sheet-YYYY-MM-DD.md` | The confirm-or-correct sheet that goes with page 1. Archived once answered. `references/client-signoff-sheet.md`. |
| `credentials-and-awards-YYYY-MM-DD.md` | Awards, certifications and licenses, studies and trainings, memberships and positions, each named as the issuer names it, with issuer, date, source and status. Generated from guide 4.3. `references/proof-map.md`. |
| `research/` | Originals: transcripts, saved pages (`pages/`), raw AI files (`ai-criteria/raw/`). The quote check reads only these. |
| `research/sources.md`, `research/proof-map.md`, `research/own-words.md`, `research/ai-criteria/summary.md` | Our notes. Each starts with the line "Our notes, not a source." |

## Rules

1. **Don't send homework, send a draft.** Research first. Ask the client only what research can't find, and give every question our drafted answer to confirm or correct.
2. **Every fact has a status: public, confirmed or needed.** Definitions are in `references/proof-map.md`. Writers use public and confirmed facts only. A drafted answer isn't a fact until the client confirms it, and silence confirms nothing.
3. **Never invent.** That covers facts, credentials, quotes, reviews, numbers, offers, search results and AI answers. Quotation marks mean verbatim and sourced, and the client is quoted only from a transcript, a recording or their own writing. A quote that exists only in our notes is invented. What the owner says customers tell them is the owner's account: label it so, and never quote it on a page as a customer. Only real reviews and testimonials are quoted as customers.
4. **Their words, in context.** Use the client's tones and sayings only where the copy's subject matches what they were talking about when they said it. Skip fragments, filler, jokes, sarcasm, personal talk and anything that only makes sense mid-conversation. Prefer their patterns to one quirky line, and use each phrase at most once per piece. Procedure: `references/client-own-words.md`.
5. **Specific beats generic.** Write "former prosecutor", not "experienced". Specific means checkable: a stranger could verify it. This is not a hunt for differentiators.
6. **Never upgrade a fact to fit a criterion.** Trained isn't certified, a member isn't board certified, and having handled something doesn't make you an expert. Name every credential and award exactly as its issuer does.
7. **One date per fact, in one format.** Write "licensed since 2009", not "15 years". Each time-based fact gets one date in the dates table (4.2), and every page, profile and schema block uses it.
8. **Offers are a whitelist.** The copy offers only what the ledger lists: services, hours, prices, guarantees, consultations and areas. A price or date that changes per event comes from that event's registration page, never from memory. Nothing else gets offered, so the guide never needs to say what the client doesn't do.
9. **It isn't a ranking check.** Never record who ranks where. Business names in AI answers matter only for the kinds of facts the engine repeated about them.
10. **Caps, not minimums.** Every section has a cap and nothing has a minimum. A guide the client won't read is as good as none.
11. **One master copy.** The credentials and awards list, a client-facing doc or a dashboard view is generated from the master and labeled as a dated copy. Never edit a copy.
12. **Regulated industries get no rulebook.** Flag any claim that is a result, rating, comparison or specialist title for the client to approve. Don't quote rules from memory.
13. **Privacy.** Use only business material from calls. Personal talk stays out of every file we write, and isn't logged under "Left out" either. A recording without an on-record OK is for internal voice notes only and is never quoted publicly without the client's OK.
14. **You prepare, the user sends.** Never email, message, call or book anything with the client yourself, even if you have the tools. Hand the user drafts to send.

## Procedure

### 1. Intake
Collect six things: the client URL, the industry, the service area, the services, the work we're hired for, and where to save. Choose the main service and city for step 3. Ask the user whether we know this industry well; if we only know part of it (homes yes, commercial work no), treat the part we don't know as unknown. Where we don't, the client gets more say over who their customer is, through the sign-off sheet.

Note the shape of the business: one program or several (programs, brands, practice areas, locations or audiences under one organization), and whether it has a storefront (an address, a GBP) or runs events and pop-ups with no fixed place. Both change the template (2.13 and 7.1).

Then ask the two questions the run depends on, word for word, and wait for both answers: the own-words question below and the AI research question in step 3.

> "Do you have anything where the client talks or writes in their own words: a recorded call, videos, emails, newsletters, replies to reviews? If not, I can give you an outline for a 20-minute recorded call where they just talk about their work (with their OK to record). Or we skip it and work from public sources."

### 2. Research the client (no client time)
Log every fact in `research/sources.md` with its URL and the date you checked it, and save the page itself in `research/pages/`:
- **The site:** home, about, team and bio pages, service or program pages, FAQ, contact, registration pages.
- **Google Business Profile:** categories, description, services, hours, attributes, and the owner's replies to reviews. Event and mobile businesses often have none; record that.
- **Reviews:** what customers praise and the words they use for their problem, verbatim with the source.
- **How the client comes across:** what reviewers say about how they talk and treat people, and the owner's own words in replies, videos or posts. Raw material for the voice; we still set it.
- **Their own words:** transcripts, videos or writing the user shared. Follow `references/client-own-words.md`.
- **Credentials and awards:** the industry's license lookup, board or certifying body directory, employer bio pages, and each award on the issuer's own page.
- **Other mentions:** associations, press and directories.

Google Maps listings and reviews often come back empty through a plain web fetch. If they do, ask the user to paste them, use a browser tool, or use DataForSEO's Maps endpoint if option 1 is set up; don't carry on as if there were none. Record every conflict; a conflicting fact stays needed until the client settles it.

### 3. Check what AI tells shoppers to look for (always ask; the user can skip it)
This step finds which facts are worth surfacing and which questions the site should answer. It feeds the Accurate goal and the 3.10 questions; it doesn't set the voice. Follow `references/ai-criteria-research.md`.

Ask this at intake. If it wasn't asked, ask it now, exactly as written, then wait. Never skip it or pick an option for the user. First check what this session has (DataForSEO MCP tools or environment variables, a browser tool) and add "(not set up here)" after any option that's missing, but keep all four.

> "For the AI research step, how do you want to run it?
> 1. **DataForSEO API.** I send the prompts to ChatGPT, Gemini and Perplexity through your DataForSEO account. Fast. It's billed to your account: in our test, about 10 cents per five-prompt ChatGPT run and 3 cents on Perplexity, 32 cents for the whole minimum set. I'll run one test prompt, show you the real cost and the projected total, and get your OK before the rest.
> 2. **Browser.** I drive a browser and run the prompts in the real apps, including Google's AI Overview. Closest to what a shopper sees. Needs a browser tool and may need you to be signed in.
> 3. **Guided prompts.** I give you the exact prompts, you run them yourself in fresh chats and paste each finished conversation back. No tools or cost.
> 4. **Skip it** for this client."

Then:
- **Option 1:** use DataForSEO MCP tools or the `DATAFORSEO_USERNAME` and `DATAFORSEO_PASSWORD` environment variables (the API login and API password, not the account password). Never ask for a password in the chat. If neither is set up, say so, point to https://dataforseo.com/model-context-protocol, and offer option 2 or 3. One test call per engine, then the real cost and projected total, then a yes (or a check against a budget the user already set). Follow the API notes: model choice, web search on, history shortened, cost logging, billed errors.
- **Option 2:** confirm a browser tool. Fresh or temporary sessions; log whether you were signed in. Never touch tabs you didn't open. On a CAPTCHA, login wall or bot check, stop and offer option 3.
- **Option 3:** print the prompts as a numbered checklist, one fresh chat per run. Default to the minimum set (2 engines, 2 runs each, plus one "how do I choose" chat per engine). Ask for the full conversation text and the raw-file header details.
- **Option 4:** write "AI research skipped." in the summary and in guide sections 5 and 6.

Whatever the method, log what the engines tell the shopper to check, with run counts, the questions they ask the shopper, the kinds of sources they cite, and the kinds of facts they repeat about named businesses. Never write an engine answer you didn't see.

### 4. Build the proof map
Follow `references/proof-map.md`. Map every criterion and shopper question to the client's evidence (fact IDs), its status and where it should appear. Gaps research can't fill become sheet items. Criteria the client doesn't meet stay in the research summary, out of the guide.

### 5. Draft the sign-off sheet
Use `references/client-signoff-sheet.md`. Up to 8 items, each with our drafted answer and what it unlocks. Only facts that block copy get a question; preferences get a sensible default.

### 6. Write the guide and the credentials and awards list
Use `references/guide-template.md`: its structure, its caps and its write order (section 4 first, page 1 last). Page 1 is the sign-off page the client reads; the rest is the writer's spec.

Spend the most care on the voice. We set it, for the client's customer, not to flatter the owner. If the current copy is generic, salesy, fearful or written for the trade, don't copy it; the client owns the facts, not the tone. Keep what is real and works for the customer, such as how the owner explains things. Their own words, used in context, are the best voice source; when they show a pattern that fits the customer, at least one 3.4 rule comes from it, and its From line says so. Never bend a line from a call into a rule to fill the slot: if their words hold nothing that travels, the rules say "From: our call, for the customer". 3.8's sentence shape comes from their pacing notes, not our house style. Old site copy is the weakest source.

**If we wrote the current site and the client likes it,** keep what they like and check it against their own words: where the site and how they talk differ, their words win, and a rule we can't trace to them or the customer gets cut. Don't let our old copy stand in for their voice.

**One organization, several programs:** one master voice (section 3) and one ledger, plus a short note per program or audience in 2.13: who it's for, what differs, its own proof and its own CTA.

Every sample line uses only public or confirmed facts and starts with the reader, because writers copy examples (`references/examples.md`). Each example sentence appears once in the guide (only 1.3 copies a Do line), and each Don't line is the near miss a writer would actually produce, on the same fact as its Do line. Then write the credentials and awards list from 4.3.

### 7. Check, save, hand over
- **Run the checker:** `python3 <this skill's folder>/scripts/check_guide.py <folder>/voice-guide.md --credentials <credentials and awards list> --sheet <sign-off sheet> --own-words <folder>/research/own-words.md --sources <folder>/research/`. `--sources` reads the whole research folder: originals (transcripts, `pages/`, `ai-criteria/raw/`) count, and our notes are skipped by file name or by the line "Our notes, not a source.", so a skipped step doesn't break the command. Leave out `--own-words` if own words were skipped. Fix every FAIL by correcting the guide, never by inventing a fact the hint seems to ask for; or work through the same checks by hand. Read the WARN lines too.
- **Check sources:** re-read every quote against its source and its context, and every number against the ledger.
- **Save and hand over:** save the master copy. Give the user page 1, the sheet and a draft email that says: "If we don't hear back by [date], we'll start writing with the voice as drafted and leave these facts out until you confirm them." The user sends it.
- **If there's no reply (the user's step):** the user books a 15-minute call, walks through page 1 on screen and records it with the client's OK. The recording is the source for each answer.
- **When answers come back:** update the ledger, the dates table and the credentials and awards list, then remove the answered items from page 1.
- **Report:** the file paths, the checker result, which AI method ran or was skipped, whether own words were used, and how many facts are still needed.

### 8. First pieces and rulings (after hand-over)
The client approves the first pieces written with the guide, up to 5. Prepare each for the user to send. For every edit they make, work out the rule behind it, add a dated row to section 9, and update the section it changes the same day. Then bump the version.

## Writing with the guide

When they conflict, the facts win, then the SEO brief, and the voice carries the rest:
1. **The proof ledger.** No fact bends, whether for a term, a heading or style.
2. **The SEO brief.** It owns headings and target terms. In term-filling sections (FAQs, accordions), the terms win.
3. **The voice.** It carries the body copy, including how a term sits in its sentence.

A target term that is also a claim ("best", "top", "cheapest") appears only as the shopper's phrase, never as a claim about the client. In a question, a quote, or a heading that frames the shopper's search ("How to choose the best [service] in [City]"), the checker warns instead of failing.

**Check every draft.** Run the guide's 8.8 checklist. List each fact in the draft and match it to a public or confirmed ledger ID; anything without one comes out or goes on the sheet. The script can't catch a claim that matches nothing in the guide (an invented guarantee), so this match is the real claim check. Then run `python3 <this skill's folder>/scripts/check_guide.py <guide> --copy draft.md --own-words research/own-words.md`. It fails never-use words used as claims, year counts, a start date no fact shows, years, prices and names found only in needed facts, sentences that share a needed fact's key words, lines own-words.md left out, the owner's account quoted as a customer, and a 3.6 phrase used twice. It warns when the draft uses a 3.6 phrase, with the context it came from, so check the subject matches.

Cut the patterns that read as AI-written (`references/examples.md`). Each type of work loads only the sections section 8 lists. If a writing job has no guide for the client, it stops and asks for one.

## Keeping it current

Update the guide when the client gets a new credential, award or service, when hours, areas or programs change, and before a site rebuild (re-run the AI step then). If the user records monthly or quarterly calls with the client, re-mine them and log changes as dated rulings (`client-own-words.md`, "Refresh"). Bump the version each time and regenerate the credentials and awards list.

## Files

- `references/guide-template.md`: the guide's structure, caps, write order and fill notes, including page blueprints and the ship checklist.
- `references/client-own-words.md`: the context rule, consent and privacy, the call outline, mining, and the refresh.
- `references/ai-criteria-research.md`: prompts, run counts, the turn-5 fallback, DataForSEO notes and real costs, what to log.
- `references/proof-map.md`: fact statuses, the map, and the credentials and awards list.
- `references/client-signoff-sheet.md`: the confirm-or-correct sheet.
- `references/examples.md`: poor and good lines, two voices on the same facts, and patterns that read as AI-written.
- `scripts/check_guide.py`: the checker (Python 3, standard library only). `--credentials` takes the credentials and awards list; `--proof`, its old name, still works.
