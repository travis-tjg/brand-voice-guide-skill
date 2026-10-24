# Brand voice guide: a Claude skill

From Travis Godec. Version 1.2, October 24, 2026. Shared with the Tested SEO Mastermind.

## Quick install

**Claude Code:**
```sh
git clone https://github.com/travis-tjg/brand-voice-guide-skill.git
cp -R brand-voice-guide-skill/brand-voice-guide ~/.claude/skills/
```
Then ask Claude: "Build a brand voice guide for [URL]. They're a [industry] in [city], and we're doing [the work]."

**Claude app (claude.ai):** download `brand-voice-guide-app.zip` from the latest release on this repo (Releases, on the right) and upload it under Customize > Skills. Upload hasn't been tested yet; tell me if it breaks.

**No git:** Code, then Download ZIP, and copy the `brand-voice-guide` folder into your skills folder.

## What it is

A Claude skill that builds a brand voice guide for a new client in any industry: how they speak, and how they don't. Every writing job for that client then loads it, so AI-written copy is:

- **Unique:** it sounds like this client, not every other site in the category.
- **More likely to convert:** it's written to the customer (StoryBrand: their problem, a simple plan, one next step).
- **Accurate:** the writer gets real, specific, dated facts, so it doesn't have to guess. A checker script catches year counts, never-use words, unconfirmed facts and the client's phrases used out of context. Every other claim is checked by a person: Claude matches each fact in a draft to the guide's fact list, and you read it.

It's early. Version 1.2 is still an early version, not a finished system, and I'd love to hear what you'd change.

Three rules carry it:
1. **We set the voice; the client owns the facts.** The guide says who the client sounds like (a role, not adjectives) and who they never sound like, with voice rules written as pairs ("direct, but not harsh"), do and don't lines, words they never use, and how the tone shifts by page. We never ask the client to describe their voice. Page 1 shows them a sample line and asks: "Does this sound like you talking to a customer? Tell us what doesn't."
2. **Don't send homework, send a draft.** We do the research. The client only confirms or corrects a short sheet of answers we've drafted.
3. **Specific beats generic.** "Former prosecutor" beats "experienced". Every fact has a source and a status: public, confirmed or needed. Writers use only public and confirmed facts, and a drafted answer is never a fact.

**Always asked, and you can skip it: what AI tells shoppers to check.** Ask the engines who they'd recommend, then why. Note the credentials, trainings, specialties and local experience they tell the shopper to look for, and the questions they ask the shopper. That tells you which real facts to surface and which questions the site should answer. It isn't a ranking check.

## New in 1.2

Fixes from three reviews of 1.1 (a practitioner, an engineer and a copywriter). Like 1.1, it has been tested only on an invented business, not a real client.
- **Voice you can trace to the client.** Each voice rule says where it came from: their pattern (with timestamps), their reviews, or our call for the customer. Each Don't line is the near miss a writer would actually produce, on the same fact as its Do line. Sentence rhythm comes from the client's own pacing, not our house style. A rule can have up to 3 Do lines. Example sentences appear once each, and each of the client's phrases at most once per piece.
- **No stand-in testimonials.** What the owner says customers tell them is labeled "owner's account" and never quoted on a page as a customer.
- **Profile descriptions follow Google's rules:** no phone number, link, price or call to action.
- **Checker fixes:** no crash when a step was skipped, no made-up date in its fix hint, and fewer false alarms (a question about how long the reader has had a problem, filler words, an award named "Best ...", saved HTML pages, a review with a dash, "best" in a shopper-search heading). `--credentials` replaces `--proof`, which still works. It still can't catch an invented claim that matches nothing in the guide.
- **Caps, never minimums,** everywhere. The skill's description fits the app's 200-character limit and now also triggers when you write or check copy with a guide.

## New in 1.1

**The client's own words, in context.** The most important change. On a past guide, odd or out-of-context lines from calls were used to shape a client's language, and it caused real confusion with the client. Now every phrase we keep records what they were talking about when they said it, plus the timestamp, and a writer uses it only where the copy is about the same thing. Fragments, filler, jokes and sarcasm (AI misses it) are left out and logged as left out; personal talk stays out of every file. We prefer their patterns (how they explain things, how direct they are, the words they repeat) to one quirky line. Each phrase names the voice rule it feeds, and each rule says where it came from: their own pattern, their reviews, or our call for the customer. Test: would they read it and say "yes, that's how I'd say that, about that"? Optional refresh: re-mine monthly or quarterly calls and update the guide through a dated ruling.

**A credentials and awards list** in place of the old proof list, from the Mastermind discussion: separate lists of awards; certifications, licenses and credentials; studies, trainings and courses; and memberships and positions. Each is named exactly as its issuer names it, with the issuer, the date, a source URL and a status, plus drop-in lines for a bio page's credentials section, profiles and owned pages. Paid or vanity awards count if they're real and named exactly; the checker warns if one is the only credential.

**From the gaps against the call and the example guide:**
- Page blueprints for the page types in the job (what goes first, the StoryBrand beat, which proof and where), each with one poor and one good line. Proof sits near the headline, not in it.
- A "before anything ships" checklist of up to 8 yes/no checks built from that client's own guide.
- "The customer is never" and "We are never" lists.
- Voice rules as "X, but not Y" pairs, each with its do and don't lines.
- Reading level set per audience, with the reason.
- Organizations: one master voice with a short note per program, brand, practice area, location or audience (who, what differs, its own proof and CTA). Event and pop-up businesses with no storefront or GBP are covered, and a price or venue that changes per event comes from that event's registration page.

**From a member's brand document** (structure only):
- "What they feel and how we answer": the customer's top worries in their own words, each answered only with ledgered facts, plus one copy line. The feeling comes first on the page.
- Reader states: whether the reader has no one yet, has a default that's fine, is loyal to someone, or is stuck, with how to handle each and which pages serve them.
- "Questions we raise": never name a competitor, respect the reader's past choice, and ask questions they answer for themselves. The questions come from the criteria the engines told shoppers to check, and only ones the client visibly meets.
- "I" for owner-voiced sections, "we" for service and policy copy.
- Shopper questions as content ideas ("what to ask any [trade] before you hire one"), built so the client meets every point.

**From running 1.0 on a real business** (a prospect, with a recorded call and the DataForSEO option):
- The quote check had a hole: it accepted our own notes as a source, so a quote we typed could verify itself. It now reads only originals (transcripts, saved pages, raw files) and fails a quote found only in our notes. It also joins transcript lines, so a sentence split across timestamps still matches, and square brackets mark our fix for a probable mishearing.
- The claim check only looked at years. It now flags any sentence that shares a needed fact's key words, and names and prices found only in needed facts.
- A fallback for turn 5 when the engine asks no clarifying question.
- A privacy rule: business material only from calls. A recording made without an on-record OK is for internal voice notes only, and the checker fails copy that quotes it.
- DataForSEO notes from real use: model choice, reasoning models ignore temperature, real costs (about $0.10 per five-turn ChatGPT run and $0.03 on Perplexity; the minimum set cost $0.32), which cost field to log, a free models endpoint, and billed AI Overview errors logged as errors, not "no Overview".
- A rule for when we wrote the current site and the client likes it: their own words win where the two differ.
- "Client" works for unsigned prospects; anything the business reads uses its name.

## What's in the folder

| File | Use |
|---|---|
| `brand-voice-guide/` | The Claude skill: `SKILL.md`, six reference files and a checker script |
| `README.md` | This page |

Two zips: `brand-voice-guide-skill.zip` holds this README and the folder (for GitHub or a handout); `brand-voice-guide-app.zip` holds only the `brand-voice-guide` folder, ready to upload to the Claude app.

## How to run it

1. **Claude Code:** copy the `brand-voice-guide/` folder into your Claude skills folder (for example `~/.claude/skills/`).
   **Claude app instead (upload not tested yet):** upload `brand-voice-guide-app.zip` under Customize > Skills. If you only have the handout zip, zip the `brand-voice-guide` folder on its own (not this README) and upload that. Code execution must be on. The browser option may not be available there. The app has no `CLAUDE.md`, so add the finished guide to the client's Project and tell each chat to use it.
2. Ask: "Build a brand voice guide for [URL]. They're a [industry] in [city], and we're doing [the work]."
3. At intake it asks two things and waits for your answers: whether you have anything in the client's own words, and how to run the AI step:
   - **DataForSEO API** (needs your DataForSEO API login, set up through their MCP server or two environment variables; about 10 cents per five-prompt ChatGPT run in our test, and it shows you the real cost of one test prompt before running the rest),
   - **a browser** (closest to what shoppers see),
   - **guided prompts** you run yourself and paste back, or
   - **skip it.**
4. It researches the client's site, profile, reviews and credentials, then drafts the guide, a short confirm-or-correct sheet and the credentials and awards list, and checks them with `scripts/check_guide.py` (Python 3, nothing to install).
5. It hands you page 1, the sheet and a draft email. You send it; the skill never emails or books anything with the client.
6. Make every writing job load the guide. In Claude Code, add a line like this to your project's `CLAUDE.md`: "Before writing any copy for a client, read `<client-folder>/brand/voice-guide.md` and load the sections its section 8 lists for the job. Before delivering, answer its 8.8 checklist, run `python3 ~/.claude/skills/brand-voice-guide/scripts/check_guide.py <client-folder>/brand/voice-guide.md --copy <draft> --own-words <client-folder>/brand/research/own-words.md` and fix every FAIL. If there's no guide, stop and ask for one."

**Time:** allow about an hour of Claude time, plus 20 to 60 minutes of yours. Our one real run (on 1.0) took Claude 72 minutes, 22 of them on the DataForSEO step; 1.2 does more and hasn't been timed on a real client. By our estimate, your time is reading the guide (15 to 20 minutes), plus about half an hour if you run the guided AI prompts yourself, and page 1 and the sheet take the client about 5 minutes.

**You get:** one guide with a one-page sign-off section on top and a cap on every section (about 2,500 words of prose at most), a confirm-or-correct sheet for the client, a credentials and awards list, and your research files. When they conflict, the facts win, then your SEO brief's headings and terms. The voice carries the rest of the copy.

**Outside Claude Code (untested):** the guide is plain markdown, and its section 8 says which sections each type of job loads. Paste those sections into the system prompt of a Make or n8n step, a Claude Project or a custom GPT, send your SEO brief as the user message, and run the claim check as a second step.

## What's tested and what isn't

**Working for us:** copy built on a client's specific, accurate facts reads less like AI. Our evidence is how clients have reacted, not a measurement. Facts alone don't make it sound like the client: our 1.0 run on a real business came out sounding like the site copy we'd written for them, not like the owner. The voice comes from the client's own words plus the voice rules; the own-words changes in 1.1 and 1.2 are our fix for that, tested so far only on an invented call.

**Tested so far:** in Claude, on invented businesses, plus real AI research runs on DUI lawyer searches (ChatGPT and Google). Version 1.0 was run end to end on an invented electrician, then on one real business (a prospect) with a recorded call and the DataForSEO option. That real run found the problems fixed above. Version 1.1 was run once, on an invented two-program swim school with an invented call that included sarcastic and out-of-context lines. The checker passed the guide, the sign-off sheet, the credentials list and a sample draft, and failed a planted bad draft that used the sarcastic lines, an unconfirmed title, an unconfirmed price and "over 8 years". A quote we typed into our notes failed the quote check. The real-business draft that slipped two unconfirmed facts past 1.0 now fails on both. The script can't catch a claim that matches nothing in the guide, such as an invented guarantee, so the fact-by-fact match Claude runs on each draft, and your own read, still matter. The AI step was skipped in the 1.1 test, and 1.1 hasn't been run on a real client yet. Version 1.2 was retested on the same invented swim school, rewritten to the 1.2 template, and on the engineer's edge-case files (skipped steps, saved HTML pages, a guide saved from Word).

**Learned the hard way:**
- Questionnaires have had mixed results, and clients often don't understand what the guide is for.
- A guide too long for the client to review doesn't get reviewed.
- What clients do approve is what a live job needs (for us, the profile descriptions). So every sheet item says what it's needed for.
- A guide only helps the jobs it's attached to. In one audit of our own, 7 of 23 writing jobs had been given the guide.
- Lines from a call, used out of context, can confuse the client more than help.

**Testing, because it makes sense:** surfacing the client's real proof for the things AI tells shoppers to check, and stating it the same way on the site and every profile ("building consensus"). Also the numbered sections, fact tables and single date format. We haven't measured any lift in AI inclusion from either yet. The test is to re-run the same prompts once the facts are live and see whether the engines repeat them.

**Not claimed:** any ranking lift from guides. This isn't a ranking tool, and it never records who ranks where.

**Credits:** StoryBrand is Donald Miller's framework. The reader states and the question-based approach to a reader's current option are adapted from Marty Marion's positioning and de-positioning matrices, which a member shared through his own brand document; we left out the weightings. The who-what-where description format comes from local SEO practice. The dates table, the credentials and awards lists, the client interview and its monthly refresh, the first-pieces approval and the sarcasm warning came from the Tested SEO Mastermind discussion on October 23, 2026. Thank you.

## License

MIT. Use it, change it, share it. If you improve it, I would love to hear what you changed.
