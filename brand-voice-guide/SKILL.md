---
name: brand-voice-guide
description: Use when building a brand voice or tone of voice guide for a client in any industry, so AI copy is accurate, unique and converts. Makes a capped guide, a sign-off sheet and a proof list.
---

# Brand voice guide

Version 1.0, 2026-10-23.

Build one guide per client at onboarding. Every writing job for that client loads it from then on: site pages, SEO content, profiles and citations, press releases, GBP posts, email and social.

A brand voice guide writes down how the client speaks and how they don't. It has three jobs:

1. **Unique.** The copy sounds like this client, not like every other site in the category: who they sound like and who they never sound like, voice rules with do and don't lines, words they never use, and how the tone shifts by page.
2. **Converts.** The copy is written to the client's customer, who is the hero: their problem, a simple plan, one call to action, and the stakes without scare tactics (StoryBrand, Donald Miller's framework).
3. **Accurate.** The writer gets real, specific, dated facts, so it doesn't have to guess, and every claim in a draft is checked against them. As a side benefit, the same facts stated the same way everywhere give AI answer engines a consistent picture of the client. That part is a test, not a promise.

Voice comes first. The research steps exist to feed it real facts, the customer's real words and the client's own words.

It works for any industry: a DUI defense attorney, a plumbing company, an electrician, a med spa. Nothing here assumes an industry. There are no industry rulebooks and no stock offers. If the client doesn't offer something, neither the guide nor the copy mentions it. They say what the client does offer.

## Outputs

All saved in the folder chosen at intake, by default `<client-folder>/brand/`:

| File | What it is |
|---|---|
| `voice-guide.md` | The guide, and the one master copy. Structure and caps: `references/guide-template.md`. |
| `signoff-sheet-YYYY-MM-DD.md` | The confirm-or-correct sheet that goes with page 1. Archived once it's answered. Template: `references/client-signoff-sheet.md`. |
| `proof-list-YYYY-MM-DD.md` | Awards, credentials, trainings, studies and memberships from the ledger, each with source and status, for copy, profiles, citations, owned backlinks and schema. A dated copy of the ledger. Format: `references/proof-map.md`. |
| `research/sources.md` | Every fact found, with its source URL and the date checked. |
| `research/own-words.md` | Phrases, pacing and how the client explains things, from their own words. Procedure: `references/client-own-words.md`. |
| `research/ai-criteria/` | Raw AI runs and `summary.md`. Procedure: `references/ai-criteria-research.md`. |

## Rules

1. **Don't send homework, send a draft.** Research first. Ask the client only what research can't find, and give every question our drafted answer to confirm or correct.
2. **Every fact has a status: public, confirmed or needed.** Definitions are in `references/proof-map.md`. Writers use public and confirmed facts only. A drafted answer isn't a fact until the client confirms it, and silence confirms nothing.
3. **Never invent.** That covers facts, credentials, quotes, reviews, numbers, offers, search results and AI answers. If you can't see it, it doesn't go in the guide. Quotation marks mean verbatim and sourced, and the client is quoted only from a transcript, a recording or their own writing.
4. **Specific beats generic.** Write "former prosecutor", not "experienced". Specific means checkable, not unique: a stranger could verify it. This is not a hunt for differentiators.
5. **Never upgrade a fact to fit a criterion.** Trained isn't certified, a member isn't board certified, and having handled something doesn't make you an expert. Name every credential exactly as the body that issued it names it.
6. **One date per fact, in one format.** Write "licensed since 2009", not "15 years". Each time-based fact (licensed, founded, certified, awarded) gets one date in the guide's dates table (4.2), and every page, profile and schema block uses it. Counts go stale and drift apart across profiles.
7. **Offers are a whitelist.** The copy offers only what the ledger lists: services, hours, prices, guarantees, consultations and areas. Because nothing else gets offered, the guide never needs to say what the client doesn't do.
8. **It isn't a ranking check.** Never record who ranks where. Business names in AI answers matter only for the kinds of facts the engine repeated about them.
9. **Caps, not minimums.** Every section has a cap and nothing has a minimum. A guide the client won't read is as good as none.
10. **One master copy.** Anything else, such as the proof list, a client-facing doc or a dashboard view, is generated from the master and labeled as a dated copy. Never edit a copy.
11. **Regulated industries get no rulebook.** Lawyers, medical providers, financial firms and some trades have advertising rules. Flag any claim that is a result, rating, comparison or specialist title for the client to approve. Don't quote rules from memory.
12. **You prepare, the user sends.** Never email, message, call or book anything with the client yourself, even if you have the tools. Hand the user drafts to send.

## Procedure

### 1. Intake
Collect six things: the client URL, the industry, the service area, the services, the work we're hired for, and where to save (default `<client-folder>/brand/`). Choose the main service and city for step 3. Ask the user whether we know this industry well. If we don't, the client gets more say over who their customer is, through the sign-off sheet.

Then ask the two questions the run depends on, so it doesn't stall halfway: the own-words question below and the AI research question in step 3, word for word. Wait for both answers.

> "Do you have anything where the client talks or writes in their own words: a recorded call, videos, emails, newsletters, replies to reviews? If not, I can give you an outline for a 20-minute recorded call where they just talk about their work (with their OK to record). Or we skip it and work from public sources."

### 2. Research the client (no client time)
Log every fact in `research/sources.md` with its URL and the date you checked it:
- **The site:** home, about, team and bio pages, service pages, FAQ, contact.
- **Google Business Profile:** categories, description, services, products, hours, attributes, and the owner's replies to reviews.
- **Reviews:** what customers praise and the words they use for their problem. Copy phrases verbatim with the source.
- **How the client comes across:** what reviewers say about how the client talks and treats them (for example "explained everything" or "no pressure"), and the owner's own words in review replies, videos or posts. This is raw material for the voice rules. We still set the voice.
- **Their own words:** if the user shared transcripts, videos or writing, mine them for phrases, pacing and how the client explains things. Follow `references/client-own-words.md`.
- **The industry's licensing and credential records:** for example a state license lookup, a bar or medical board record, a certifying body's directory, or a manufacturer's certified-installer finder.
- **Other mentions:** associations, awards (checked on the issuer's own page), press and directories.

Google Maps listings and reviews often come back empty through a plain web fetch. If they do, ask the user to paste them or use a browser tool; don't carry on as if there were none.

Record every conflict, such as a site that says one year count while a directory shows another date. A conflicting fact stays needed until the client settles it.

### 3. Check what AI tells shoppers to look for (always ask; the user can skip it)
This step finds which facts are worth surfacing and which questions the site should answer. It feeds the Accurate goal; it doesn't set the voice. Follow `references/ai-criteria-research.md`.

Ask this at intake. If it wasn't asked, ask it now. Ask exactly this, then wait for the answer. Never skip this question or pick an option for the user. First check what this session has (DataForSEO MCP tools or environment variables, a browser tool) and add "(not set up here)" after any option that's missing, but keep all four on the list.

> "For the AI research step, how do you want to run it?
> 1. **DataForSEO API.** I send the prompts to ChatGPT, Gemini and Perplexity through your DataForSEO account. Fast. It's billed to your DataForSEO account, roughly 20 cents per five-prompt run with web search on (their fee plus the model's charge). I'll run one test prompt, show you the real cost and the projected total, and get your OK before the rest.
> 2. **Browser.** I drive a browser and run the prompts in the real apps, including Google's AI Overview. Closest to what a shopper sees. Needs a browser tool and may need you to be signed in.
> 3. **Guided prompts.** I give you the exact prompts, you run them yourself in fresh chats and paste each finished conversation back. No tools or cost.
> 4. **Skip it** for this client."

Then:
- **Option 1:** check for DataForSEO MCP tools, or the `DATAFORSEO_USERNAME` and `DATAFORSEO_PASSWORD` environment variables (the API login and API password, not the account password). Never ask the user to paste a password into the chat. If neither is set up, say so, point them to https://dataforseo.com/model-context-protocol, and offer option 2 or 3. Make one test call, report its real cost and the projected total, and get a yes before the rest. Follow the API notes in the reference (web search on, model logged, history shortened). Save each raw response, and log that answers came through the API, which can differ from the apps.
- **Option 2:** confirm a browser tool is available. Use fresh or temporary sessions and log whether you were signed in. Never touch tabs you didn't open. If a CAPTCHA, login wall or bot check appears, stop and offer option 3 instead of retrying.
- **Option 3:** print the prompts as a numbered checklist, one fresh chat per run. Default to the minimum set (2 engines, 2 runs each, plus one "how do I choose" chat per engine) unless the user wants more. Ask for the full conversation text and the raw-file header details from the reference (engine and mode, signed in, memory, location, date and time).
- **Option 4:** write "AI research skipped." in the summary and in guide sections 5 and 6, and move on.

Whatever the method, log four things: what the engines tell the shopper to check (credentials, certifications, trainings, specialties, education, awards, local experience) with run counts, the clarifying questions they ask the shopper, the kinds of sources they cite, and the kinds of facts they repeat about named businesses. Our prompt names those categories, so this shows what AI tells shoppers to check, not how it ranks. Never write an engine answer you didn't see.

### 4. Build the proof map
Follow `references/proof-map.md`. Map every criterion and shopper question to the client's specific evidence (fact IDs), then to its status, then to where it should appear. Gaps that research can't fill become sign-off sheet items. Criteria the client doesn't meet stay in the research summary and out of the guide.

### 5. Draft the sign-off sheet
Use `references/client-signoff-sheet.md`. Include up to 8 items, each with our drafted answer and what it unlocks. Only facts that block copy get a question. Preferences get a sensible default.

### 6. Write the guide and the proof list
Use `references/guide-template.md`, in exactly that structure and order and within the caps. Page 1 is the sign-off page the client reads, and it shows one sample line in the voice. The rest is the writer's spec. Spend the most care on the voice: who they sound like and never sound like, the do and don't lines, the words they never use, tone by page and the sample paragraph. We set the voice, and we write it for the client's customer, not to flatter the owner. If the client's current copy is generic, salesy, fearful or written for the trade instead of the customer, don't copy it; the client owns the facts, not the tone. Keep what is real and works for the customer, such as how the owner explains things in review replies or on a call. Old site copy, often written by someone else, is the weakest voice source. Every sample line uses only public or confirmed facts and starts with the reader, because writers copy examples. See `references/examples.md`.

Then write the proof list from the ledger (`references/proof-map.md`, "Proof list export").

### 7. Check, save, hand over
- **Run the checker:** `python3 <this skill's folder>/scripts/check_guide.py <output folder>/voice-guide.md --proof <proof list> --sheet <sign-off sheet> --sources <output folder>/research/*.md <any transcripts>`. It checks the caps, the ledger and dates, needed facts in copy sections, year counts, page 1's sample line, the descriptions, the proof list, the sheet, and that every quote is word for word in a source (`--help` has the options). Fix until it passes, or work through the same checks by hand.
- **Check sources:** re-read every quote against its source and every number against the ledger.
- **Save and hand over:** save the master copy. Give the user page 1, the sign-off sheet and a draft email that says: "If we don't hear back by [date], we'll go ahead with the voice as drafted and leave out every fact on the sheet." The user sends it.
- **If there's no reply (the user's step):** once the date passes, the user books a 15-minute call, walks through page 1 on screen and records it with the client's OK. The recording is the source for each answer.
- **When answers come back:** the user shares them. Update the ledger statuses, the dates table and the proof list, then remove the answered items from page 1.
- **Report:** end with the file paths, the checker result, which AI method ran or was skipped, whether own words were used, and how many facts are still needed.

### 8. First pieces and rulings (after hand-over)
The client approves the first 3 to 5 pieces written with the guide. Prepare each for the user to send. For every edit the client makes, work out the rule behind it, add a dated row to section 9, and update the section it changes (a voice rule, the never-use list, a ledger row) the same day. Then bump the version. Fill notes: `references/guide-template.md`, section 9.

## Writing with the guide

When they conflict, the facts win, then the SEO brief, and the voice carries the rest:
1. **The proof ledger.** No fact bends, whether for a term, a heading or style.
2. **The SEO brief.** It owns headings and target terms. In term-filling sections (FAQs, accordions, supplemental sections), the terms win.
3. **The voice.** It carries the body copy, including how a term sits in its sentence.

Some target terms are also claims, such as "best", "top" or "cheapest". Those appear only as the shopper's phrase ("how to choose the best plumber in [City]"), never as a claim about the client.

**Check every draft's claims.** List each fact in the draft (years, credentials, counts, prices, hours, offers, areas) and match it to a public or confirmed ledger ID. Anything without one comes out or goes on the sign-off sheet. Then run `check_guide.py <guide> --copy draft.md`. It fails never-use words used as claims, year counts like "over 20 years" and years found only in a needed fact. It only warns when a never-use word sits inside a question or quote, such as the shopper's phrase "how to choose the best plumber", so review each warning.

Cut the patterns that make copy read as AI-written (list in `references/examples.md`), whatever the voice.

Each type of work loads only the sections it needs (section 8 of the guide). If a writing job has no guide for the client, it stops and asks for one instead of improvising a voice.

**A test, not a proven lift:** the numbered sections, fact tables and single date format are there so AI can parse the guide and the pages built from it. If you carry them onto the site (see the 4.2 fill note), log it as a test.

## Keeping it current

Update the guide when the client gets a new credential, award or service, when hours or areas change, and before a site rebuild (re-run the AI step then). Bump the version each time, regenerate the proof list, and never edit a dated copy.

## Files

- `references/guide-template.md`: the guide's exact structure, caps and fill notes.
- `references/client-own-words.md`: the 20-minute call outline and how to mine transcripts and writing for the voice.
- `references/ai-criteria-research.md`: the prompts, run counts, API notes, what to capture, how to log.
- `references/proof-map.md`: fact statuses, how criteria map to evidence, then status, then placement, and the proof list export.
- `references/client-signoff-sheet.md`: the confirm-or-correct sheet.
- `references/examples.md`: poor and good lines in three industries, the same facts in two voices, and patterns that read as AI-written. All of them are illustrative.
- `scripts/check_guide.py`: the cap and rule checker (Python 3, standard library only).
