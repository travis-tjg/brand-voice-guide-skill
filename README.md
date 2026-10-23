# Brand voice guide: a Claude skill

From Travis Godec. Version 1.0, October 23, 2026. Shared with the Tested SEO Mastermind.

## Quick install

**Claude Code:**
```sh
git clone https://github.com/travis-tjg/brand-voice-guide-skill.git
cp -R brand-voice-guide-skill/brand-voice-guide ~/.claude/skills/
```
Then ask Claude: "Build a brand voice guide for [URL]. They're a [industry] in [city], and we're doing [the work]."

**Claude app (claude.ai):** click Code, then Download ZIP on this page. Unzip it, then zip just the `brand-voice-guide` folder on its own and upload that under Settings, Capabilities, Skills.

**No git:** Code, then Download ZIP, and copy the `brand-voice-guide` folder into your skills folder.

## What it is

A Claude skill that builds a brand voice guide for a new client in any industry: how they speak, and how they don't. Every writing job for that client then loads it, so AI-written copy is:

- **Unique:** it sounds like this client, not every other site in the category.
- **More likely to convert:** it's written to the customer (StoryBrand: their problem, a simple plan, one next step).
- **Accurate:** the writer gets real, specific, dated facts, so it doesn't have to guess, and every claim in a draft is checked against them.

It's early. Version 1.0 is just the first one we're sharing, not a finished system, and I'd love to hear what you'd change.

Three rules carry it:
1. **We set the voice; the client owns the facts.** The guide says who the client sounds like (a role, not adjectives) and who they never sound like, with do and don't lines, words they never use, and how the tone shifts by page. We never ask the client to describe their voice. Page 1 shows them a sample line to approve.
2. **Don't send homework, send a draft.** We do the research. The client only confirms or corrects a short sheet of answers we've drafted.
3. **Specific beats generic.** "Former prosecutor" beats "experienced". Every fact has a source and a status: public, confirmed or needed. Writers use only public and confirmed facts, and a drafted answer is never a fact.

**Always asked, and you can skip it: what AI tells shoppers to check.** Ask the engines who they'd recommend, then why. Note the credentials, trainings, specialties and local experience they tell the shopper to look for, and the questions they ask the shopper. That tells you which real facts to surface and which questions the site should answer. It isn't a ranking check.

## New in 1.0

From the Mastermind discussion:
- **The client's own words.** Optional: a recorded 20-minute call where they just talk (Fathom, Fireflies or Zoom, with their OK to record), plus their videos, emails and review replies. The skill mines them for phrases, pacing and how they explain things, and quotes only what's in the transcript. We still draft; they react.
- **A dates table.** One date per time-based fact (licensed, founded, certified), in one format everywhere. The checker fails "over 20 years" and "20+ years" in drafts. If you take it to the site, keep each page's date matching its schema, sitemap and RSS dates.
- **A proof list.** Awards, credentials, trainings, studies and memberships, each with its source and status, as its own file for copy, profiles, citations, owned backlinks and schema.
- **First pieces and rulings.** The client approves the first 3 to 5 pieces, and each edit they make goes back into the guide as a dated ruling.
- **Structure for AI parsing.** Numbered sections (1.1, 1.2), fact tables and one date format. This is a test, not a proven lift.

From three critics' reviews: the voice section now has "We never sound like", "Tone by page", the client's own words and a sample paragraph; the DataForSEO setup is spelled out; and the skill prepares everything for you to send but never contacts the client itself.

## What's in the folder

| File | Use |
|---|---|
| `brand-voice-guide/` | The Claude skill: `SKILL.md`, six reference files and a checker script |
| `README.md` | This page |

## How to run it

1. **Claude Code:** copy the `brand-voice-guide/` folder into your Claude skills folder (for example `~/.claude/skills/`).
   **Claude app instead:** zip just the `brand-voice-guide` folder (not this README) and upload it under Customize > Skills. Code execution must be on. The browser option may not be available there.
2. Ask: "Build a brand voice guide for [URL]. They're a [industry] in [city], and we're doing [the work]."
3. At intake it asks two things and waits for your answers: whether you have anything in the client's own words, and how to run the AI step:
   - **DataForSEO API** (needs your DataForSEO API login, set up through their MCP server or two environment variables; roughly 20 cents per five-prompt run with web search on, and it shows you the real cost of one test prompt before running the rest),
   - **a browser** (closest to what shoppers see),
   - **guided prompts** you run yourself and paste back, or
   - **skip it.**
4. It researches the client's site, profile, reviews and credentials, then drafts the guide, a short confirm-or-correct sheet and the proof list, and checks them with `scripts/check_guide.py` (Python 3, nothing to install).
5. It hands you page 1, the sheet and a draft email. You send it; the skill never emails or books anything with the client.
6. Make every writing job load the guide. In Claude Code, add a line like this to your project's `CLAUDE.md`: "Before writing any copy for a client, read `<client-folder>/brand/voice-guide.md` and load the sections its section 8 lists for the job. If there's no guide, stop and ask for one."

**You get:** one guide with a one-page sign-off section on top and a cap on every section, a confirm-or-correct sheet for the client, a proof list, and your research files. When they conflict, the facts win, then your SEO brief's headings and terms. The voice carries the rest of the copy.

**Outside Claude Code (untested):** the guide is plain markdown, and its section 8 says which sections each type of job loads. Paste those sections into the system prompt of a Make or n8n step, a Claude Project or a custom GPT, send your SEO brief as the user message, and run the claim check as a second step.

## What's tested and what isn't

**Working for us:** copy built on a client's specific, accurate facts reads like the client, not like AI. Our evidence is how clients have reacted, not a measurement.

**Tested so far:** in Claude, on invented businesses, plus real AI research runs on DUI lawyer searches (ChatGPT and Google). Version 1.0 was run end to end once, on an invented electrician with an invented interview transcript and the AI step skipped. The checker passed the guide, proof list and sign-off sheet, passed a sample paragraph (with a warning for "best" inside the shopper's question), and failed a planted bad paragraph on eight counts, including "over 15 years". Not yet run end to end on a real client. The DataForSEO notes come from DataForSEO's docs, checked October 23, 2026; that option hasn't been run through the skill yet.

**Learned the hard way:**
- Questionnaires have had mixed results, and clients often don't understand what the guide is for.
- A guide too long for the client to review doesn't get reviewed.
- What clients do approve is what a live job needs (for us, the profile descriptions). So every sheet item says what it's needed for.
- A guide only helps the jobs it's attached to. In one audit of our own, 7 of 23 writing jobs had been given the guide.

**Testing, because it makes sense:** surfacing the client's real proof for the things AI tells shoppers to check, and stating it the same way on the site and every profile ("building consensus"). Also the numbered sections, fact tables and single date format. We haven't measured any lift in AI inclusion from either yet. The test is to re-run the same prompts once the facts are live and see whether the engines repeat them.

**Not claimed:** any ranking lift from guides. This isn't a ranking tool, and it never records who ranks where.

**Credits:** StoryBrand is Donald Miller's framework. The who-what-where description format comes from local SEO practice. The dates table, the proof list, the client interview and the first-pieces approval came from the Tested SEO Mastermind discussion on October 23, 2026. Thank you.

## License

MIT. Use it, change it, share it. If you improve it, I would love to hear what you changed.
