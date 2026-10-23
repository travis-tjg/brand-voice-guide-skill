# The client's own words

An optional step, and the best voice source there is. Two clients with the same ideal customer still say things differently, and that difference lives in how they talk: the phrases they reach for, how fast they get to the point, how they explain the work. This file covers collecting what the client has already said and mining it for the voice.

It stays "not homework". We draft, they react. The client never writes anything for this step and never describes their own voice.

## What to collect

Use whatever already exists, in this order:
1. **A recorded call where they just talk.** 20 minutes, with the outline below. Meeting recorders such as Fathom, Fireflies or Zoom's own recording give you a transcript.
2. **Their videos:** YouTube, Facebook, a talk, a local news segment. Use the platform's transcript if there is one, and note that auto transcripts mishear words.
3. **Their writing:** emails to customers, newsletters, replies to reviews, social posts they wrote themselves.
4. **Old sales or intake calls**, if the client already records them and says we can use them.

Old site copy doesn't count; someone else often wrote it.

## Consent

Get the client's OK to record before the call starts, and have them say yes on the recording. Some states require everyone on a call to agree to the recording. Use existing recordings only with the client's OK, and only the client's own voice: never mine their customers' words from a recorded call without the customer's consent.

## The 20-minute call

The user runs it; you prepare the outline and the email asking for the time. Never book it yourself. The point is to get them talking the way they talk to a customer, not to ask about their brand. Ask the questions below, in any order, and let them run long.

1. "Walk me through a job you did last week, from the first call to when you left."
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
# Own words: [client]

Sources: [file, kind, date, consent noted: yes]

## Phrases they use (verbatim, with source and timestamp)
- "[phrase]" ([source], [YYYY-MM-DD], [mm:ss])

## How they explain things
- [pattern, e.g. "starts with what the customer sees, then the cause, then the fix"] (example at [source, mm:ss])

## Pacing and register
- [e.g. "short answers, then a story when asked why"; "says 'I', not 'we'"; "names prices plainly"]

## Words they avoid or correct
- [e.g. "says 'panel', corrects 'fuse box' gently"]

## Facts they mentioned (go to sources.md as needed until checked)
- [fact] ([source], [mm:ss])
```

Rules for mining:
- **Never quote anything that isn't in the transcript or source.** Copy phrases exactly, with the source and the timestamp or date. Don't tidy a quote. If the transcript is garbled at that spot, leave it out.
- **A quote isn't a fact.** "Nine times out of ten it's a loose connection" shows how they talk. The ratio inside it still needs a ledger row before copy states it.
- **Patterns are ours, quotes are theirs.** "Explains the cause before the fix" is our reading and is labeled as such. Only verbatim text goes in quotation marks.
- **Facts from a call are leads.** A year, a credential or a count the owner mentions goes into `research/sources.md` as needed until a public source or a confirmed answer backs it. A recorded call can confirm a fact only when the fact was put to the client and they said yes, which is what the sign-off sheet's fallback call does.
- **Keep what helps the customer, drop what doesn't.** If the owner talks in trade jargon or runs hot, we don't copy it. We keep how they explain things and the phrases a customer would understand.

## How it feeds the guide

- **3.2 We sound like:** the role often comes straight from how they explain things.
- **3.4 Rules:** turn each pattern into a rule with a Do line. A Do line can borrow their phrasing, but it's still a line we wrote, not a quote.
- **3.6 In their own words:** up to 5 phrases, verbatim, with the source.
- **3.7 Words:** words they use next to the trade's word.
- **1.5 How working with you goes:** the steps they described in the job walkthrough.
- **Section 6:** the questions they say they get asked most, labeled as coming from the client.
