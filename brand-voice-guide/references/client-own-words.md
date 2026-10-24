# The client's own words

An optional step, and the best voice source there is. Two businesses with the same customer still say things differently, and that difference lives in how they talk: the phrases they reach for, how fast they get to the point, how they explain the work. This file covers collecting what they've already said, mining it, and turning it into voice rules.

It stays "not homework". We draft, they react. They never write anything for this step and never describe their own voice.

## The rule: their words, in context

Use their tones and sayings, but only in context and only where they fit.

We learned this the hard way. On a past guide, odd or out-of-context lines from calls were used to shape a client's language, and it caused real problems and confusion with the client. A line that was natural in the middle of a call can read as strange, or as a joke at their expense, once it's on a page about something else.

So:
- **Record the context.** Every phrase we keep records what they were talking about when they said it, plus the timestamp.
- **Match the subject.** A phrase is used only where the copy's subject matches its context. A line about a stubborn drain doesn't go on the pricing page.
- **Skip what doesn't travel:** fragments, filler ("you know", "kind of"), throwaway lines, jokes, sarcasm (AI misses it), and anything that only makes sense mid-conversation. Log each one under "Left out" so nobody picks it up later. Personal talk and venting are different: skip them without logging (see Consent and privacy).
- **Prefer patterns to quirks.** How they explain things, how direct they are and the words they repeat are worth more than one quirky line. A pattern that shows up three times is a rule; a line said once is a phrase at most, used once per piece at most.
- **The test:** would they read it and say "yes, that's how I'd say that, about that"? If you aren't sure, leave it out.
- **Own words must feed the rules.** Every phrase in guide 3.6 names the 3.4 rule or section it shapes (the Feeds column). A phrase that shapes nothing comes out. In one of our test runs, five quotes were captured and then ignored, and the voice ended up sounding like our old site copy instead of the owner. The opposite fails too: never bend a line into a rule to fill the slot. A planning or sales call may hold nothing that travels (venues, logistics, tech questions). Then guide 3.6 says "None yet", the rules say "From: our call", and the user gets the 20-minute call outline below.

## What to collect

Use whatever already exists, in this order:
1. **A recorded call where they just talk.** 20 minutes, with the outline below. Meeting recorders such as Fathom, Fireflies or Zoom's own recording give you a transcript.
2. **Their videos:** YouTube, Facebook, a talk, a local news segment. Use the platform's transcript if there is one, and note that auto transcripts mishear words.
3. **Their writing:** emails to customers, newsletters, replies to reviews, social posts they wrote themselves.
4. **Old sales or intake calls**, if they already record them and say we can use them.

Old site copy doesn't count; someone else often wrote it. If we wrote it and they like it, see SKILL.md step 6.

Save each original (transcript, saved page, exported email) in `research/`. The quote check reads the originals, never our notes.

## Consent and privacy

- **Consent first.** Get their OK to record before the call starts, and have them say yes on the recording. Some states require everyone on a call to agree to the recording.
- **A recording made without an on-record OK** (an earlier call, a sales call): use it only for internal voice notes, meaning patterns, pacing and word choice. Write "Consent: none on record. Internal only." at the top of `own-words.md`, and mark each 3.6 phrase's Source "internal only". Never quote it in public copy until they say yes; the user can ask, and a sign-off sheet item is fine. The checker fails copy that uses an internal-only phrase.
- **Business material only.** Calls drift into family, health, money, other people and venting. Leave all of it out of every file we write, including `own-words.md` and `sources.md`. Don't log it under "Left out" either; just skip it.
- **Only their voice.** Never mine their customers' words from a recorded call without the customer's consent.

## The 20-minute call

The user runs it; you prepare the outline and the email asking for the time. Never book it yourself. The point is to get them talking the way they talk to a customer, not to ask about their brand. Ask the questions below, in any order, and let them run long.

1. "Walk me through a job you did last week, from the moment they called to when you left."
2. "What do customers usually get wrong before they call you?"
3. "What's the question you get asked most? How do you answer it?"
4. "How do you explain your prices to someone who thinks it's too much?"
5. "What made you start doing this work?"
6. "What do you tell a customer when the news is bad?"
7. "If a friend asked you how to pick someone in your trade, what would you tell them?"

Never ask "how would you describe your brand voice?" or "what makes you different?" Those are our job.

## Mining the transcript

Read the whole transcript, then fill in `research/own-words.md`:

```markdown
# Own words: [business]

Our notes, not a source.
Sources: [file, kind, date]. Consent: [yes, on the recording at mm:ss / none on record. Internal only.]

## Phrases

| Phrase (verbatim) | Source | Context: what they were talking about | Feeds |
|---|---|---|---|
| "[phrase]" | [call, YYYY-MM-DD, mm:ss] | [the subject, in a few words] | [3.4 rule 2 / 3.7 / none yet] |

## How they explain things (our reading)
- [pattern, e.g. "starts with what the customer sees, then the cause, then the fix"] (examples at mm:ss, mm:ss)

## Pacing and register (our reading)
- [how they open an answer, how long they run, how they finish, with timestamps: e.g. "short answers, then a story when asked why" (04:30, 13:30); "says 'I', not 'we'"; "names prices plainly"]

## Words they use, avoid or correct
- [e.g. "says 'panel', corrects 'fuse box' gently"]

## Business facts they mentioned (leads: go to sources.md as needed until checked)
- [fact] (mm:ss)

## Left out

| Line | Source | Why left out |
|---|---|---|
| "[line]" | [mm:ss] | [sarcasm / joke / fragment / filler / only makes sense mid-call / off-topic] |
```

Rules for mining:
- **Never quote anything that isn't in the transcript or source.** Copy phrases exactly. Don't tidy a quote.
- **Lines break, phrases don't.** Machine transcripts split one sentence across timestamped lines. Copy the phrase as spoken; the checker joins the lines (and drops timestamps and speaker labels) before matching.
- **Probable mishearings.** If one word is clearly misheard, put our correction in square brackets: "We'll [figure] it out." The checker matches the rest and warns, and the phrase stays out of public copy until someone checks the recording. If more than a word or two is garbled, leave it out.
- **A quote isn't a fact.** "Nine times out of ten it's a loose connection" shows how they talk. The ratio inside it still needs a ledger row before copy states it.
- **Patterns are ours, quotes are theirs.** "Explains the cause before the fix" is our reading and is labeled as such. Only verbatim text goes in quotation marks.
- **Facts from a call are leads.** A year, a credential or a count the owner mentions goes into `research/sources.md` as needed until a public source or a confirmed answer backs it. A recorded call confirms a fact only when the fact was put to them and they said yes, which is what the sign-off sheet's fallback call does.
- **Keep what helps the customer, drop what doesn't.** If the owner talks in trade jargon or runs hot, we don't copy it. We keep how they explain things and the phrases a customer would understand.

## How it feeds the guide

- **3.2 We sound like:** the role often comes straight from how they explain things.
- **3.4 Rules:** turn a repeated pattern that fits the customer into a pair with a Do line, and name it in the rule's From line with two or three timestamps. If they talk in short, flat promises, the pair says so; it isn't "calm". A Do line can borrow their phrasing, but it's still a line we wrote, not a quote.
- **3.8 Mechanics:** sentence shape from the Pacing and register notes: how they open an answer, how long they run, how they finish. Not our house defaults.
- **3.6 In their own words:** up to 5 phrases from the Phrases table, each with its source, context and the rule it feeds.
- **3.7 Words:** the words they use next to the trade's word.
- **2.5 What they feel:** what they say customers tell them ("people always ask me if..."), with the timestamp, labeled "owner's account". It shows the worry; it's never quoted on a page as a customer's words.
- **1.5 How working with you goes:** the steps they described in the job walkthrough.
- **Section 6:** the questions they say they get asked most, labeled as coming from them.

Check it: `check_guide.py voice-guide.md --own-words research/own-words.md` fails a phrase with no context, and fails the guide (or a draft, with `--copy`) if it uses a line from "Left out".

## Refresh (optional, recurring)

If the user already records monthly or quarterly calls with the business (with their OK), re-mine them for phrases and patterns. When a new pattern holds across calls, or a 3.6 phrase turns out to be wrong, update the guide through a dated ruling in section 9, then bump the version. Change a rule because of a pattern, never because of one new line.
