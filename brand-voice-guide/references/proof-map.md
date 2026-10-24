# Proof map

The proof map joins the research steps. Each criterion and shopper question maps to the client's specific evidence, then to that evidence's status, then to where it should appear. Build it as a working file at `research/proof-map.md` (our notes, not a source). Guide sections 4 to 6 and the credentials and awards list come from it, so writers never need to load the working file.

## Fact statuses

Every fact in the ledger has exactly one status.

| Status | Meaning | Source recorded as |
|---|---|---|
| **public** | Published by the client (site, GBP, their own profiles) or by the body that issues it (license lookup, certifying body's directory, the award's own page). No source conflicts with it. | URL and the date you checked it |
| **confirmed** | The client said yes, in writing or on a recorded call. | "client, email YYYY-MM-DD" or "client, call YYYY-MM-DD" |
| **needed** | Anything else: our drafted answers, inferences, facts found only in third-party directories, press, AI answers or a call where nobody put the fact to the client, facts with conflicting sources, and anything out of date. | Where you saw it and what's missing |

How the statuses work in practice:
- **Writers use public and confirmed facts only.** A needed fact stays out of copy, and that includes hedged versions of it. Writing "decades of experience" because the year isn't confirmed is still using an unconfirmed fact. Use a confirmed fact instead, or leave it out.
- **Leads are not sources.** Third-party directories, aggregators, AI answers and things the owner mentioned in passing often hold stale or merged data. They can point you to a fact, but they can't make it public. Find it on a public source, or put it on the sign-off sheet.
- **Old site copy can be wrong.** The client's site counts as public, but copy from an old site or a previous agency can be wrong. That includes a site we wrote: our copy is only as good as what it was built from. If a claim that matters rests only on marketing copy, confirm it.
- **Changing facts.** Prices, dates, venues and age groups that change per event or season get one row that points to the source: "Each event's date, venue and price: as on its registration page." Copy takes them from that page at writing time, never from memory or an old event.
- **Conflicts make a fact needed.** For example, a site saying "28 years" while the license record shows a different first-licensed year. The sign-off sheet item shows both sources and drafts the date-anchored version.
- **Facts age.** Record the date you checked each one. Before a public fact goes into a press release or a new profile, check it again if that date is more than a year old.

## Writing a fact

Each ledger row is one fact, worded the way it will appear in copy.

- **Be specific.** Specific means a stranger could check it, because it names a body, a year, a place, a document or a count with a source. "Experienced", "trusted" and "top quality" can't be checked, so they aren't facts.
- **Anchor time to a date.** Write "licensed in [State] since 2011", not "14 years". A count goes stale every year, and different profiles end up with different counts. Every time-based fact also gets a row in the dates table (guide 4.2), with one date in one format.
- **Name credentials exactly as the issuer does,** with the issuer's name and the year.
- **Keep one fact per row.** Other sections cite the ID instead of restating it, so a correction happens in one place. An award won in two years is two rows, so each has one date.

**Never upgrade a fact to fit a criterion.** Write what the source says:

| The source says | Write | Don't write |
|---|---|---|
| Completed a course | "completed [course name], [year]" | "certified in", "expert in" |
| Member of an association | "member of [association]" | "board certified", "accredited" |
| Has handled this kind of work | "has handled [work] since [year]" | "specialist", "expert" |
| A rating on a platform | "[rating] stars from [count] Google reviews, [month year]" | "top-rated", "highest-rated" |
| Named to a list in one year | "named to [list], [year]" | "award-winning" with no year |
| Holds a job title | "[title as the employer lists it], [employer], since [year]" | a bigger title, or the employer as an endorser |
| First licensed in a year | "licensed since [year]" | "[n] years doing [this exact service]" |

Engines sometimes draw these distinctions themselves. In our first test run, the engine said membership in an association is not proof of certification. Treat these distinctions as hard lines.

## The map

One row for each criterion or shopper question that applies to the client.

| ID | Criterion or question | Client's evidence | Status | Where it appears | Next step |
|---|---|---|---|---|---|
| C1 | [criterion] | F02 | public | [placements] | None |
| C2 | [criterion] | None found | needed | [placements, once confirmed] | Sheet item 1 |
| Q1 | [shopper question] | F05, F06 | public | [page and section] | Add an FAQ |

**Client's evidence.** Cite fact IDs from the ledger. If nothing is found, write "None found".

**Next step.**
- **None:** the evidence is public or confirmed and already in place.
- **Sheet item [n]:** the client probably has this but research can't show it. Draft an answer.
- **Add [page or section]:** the fact is there but no page states it yet.
- **Leave out:** the client doesn't meet it or doesn't offer it. Leave-out rows stay in the working file, out of the guide, and copy never works around them.

**Where it appears.** Pick from:
- **Site pages:** home, service pages, about or team bios, FAQ, contact, schema markup.
- **GBP fields:** description, services, products, attributes.
- **Profiles:** the kinds of sources the engines cited (`ai-criteria-research.md`, capture (c)), such as licensing records, industry directories, review sites, associations and award pages.
- **Other:** press boilerplate, email signature, owned pages that can link back (an association's member page, a BBB page, a speaker bio, a training provider's graduate list).

Put the fact where the criterion matters. A license number belongs on every service page and every profile; a training course belongs on the bio and the service page it relates to. Proof sits near every headline (a proof strip, a service page sidebar, the footer) but doesn't lead it: the headline starts with the reader.

## From the map to the guide

- **Ledger (4.1):** every fact the client has, with its status.
- **Dates (4.2):** every time-based fact, with one date in one format.
- **What AI looks for (section 5):** the C rows, except the leave-outs.
- **Shopper questions (section 6):** the Q rows, except the leave-outs.
- **Page 1 lead proof points:** the public or confirmed facts behind the criteria with the most runs.
- **Sign-off sheet:** every "Sheet item" row, in order of how many runs cited the criterion.
- **Consistent descriptions (section 7):** the same lead proof points, in the same wording.
- **Credentials and awards (4.3) and the list:** below.

## Credentials and awards list

Members of the Mastermind report that AI answers and Google surface credentials; we haven't measured it. Keep them as separate lists (awards; certifications, licenses and credentials; studies, trainings and courses; and memberships, positions and education if useful) and use them in copy, on the bio page's credentials section and on every profile and owned page. Guide section 4.3 sorts each ledger row into a list and names its issuer. The export below is generated from 4.3, 4.1 and 4.2, so whoever builds profiles, citations, owned backlinks or schema doesn't need the whole guide. It is a dated copy (SKILL.md, rule 11): regenerate it whenever the ledger changes, and never edit it directly.

- **Named exactly.** Each entry is named the way its issuer names it, with the issuer, the date (as in 4.2: a year, or the full date), the source URL and the status.
- **Paid and vanity awards count** if they're real and named exactly, with the year. Don't mock them, and don't let one be the only credential: if it is, say so to the user and lead with something else.
- **What counts as a study:** published research, a white paper or a case study someone else reviewed and published.
- **Where it goes:** the bio page's credentials section, a proof strip or the footer (near the headline, never the headline), profiles (7.5), and owned pages such as an association member page or a BBB page.

Save it as `credentials-and-awards-YYYY-MM-DD.md` beside the guide:

```markdown
# [Business name]: credentials and awards

Generated [YYYY-MM-DD] from voice-guide.md version [n]. A dated copy: don't edit it, regenerate it.
Use public and confirmed rows anywhere. Needed rows are for the client to confirm and never go in copy, profiles or schema.

## Awards

| ID | Name (exact) | Issuer | Date | Source | Status | Use for |
|---|---|---|---|---|---|---|
| F02 | [exact ledger wording] | [issuing body] | [as in 4.2] | [URL, as in 4.1] | public | [bio credentials section, footer, award schema] |

## Certifications, licenses and credentials

## Studies, trainings and courses

## Memberships, positions and education

## Drop-in lines

Public and confirmed rows only, ready to paste into a bio page's credentials section, a profile or an owned page.
- [exact ledger wording], [issuer], [date]
```

- **ID, Name, Date, Source, Status:** copied from 4.1 and 4.2 word for word; the issuer from 4.3. The checker (`--credentials`) matches every row back to the guide and fails any 4.3 row missing from the list.
- **Empty lists:** keep the heading and write "None yet."
- **Use for:** where it goes. Common schema properties: `hasCredential` (certifications, licenses, trainings), `award`, `memberOf`, `alumniOf`, `hasOccupation` (positions), `knowsAbout`; the profiles table in 7.5 supplies `sameAs`. A membership or award page that lists the client is also a citation and, often, a link back.
- **Needed rows** may be listed so the gaps are visible, but they say "needed", they never go in the drop-in lines, and they are never used.

## Worked example (illustrative: a plumbing company in [City])

The business, the facts, the license number and the counts below are all invented. They show the method only.

| ID | Criterion or question | Client's evidence | Status | Where it appears | Next step |
|---|---|---|---|---|---|
| C1 | Licensed master plumber | F01: "Master plumber license #M-00000, [State] licensing board, since 2011" | public | Every service page, GBP description, every profile | None |
| C2 | Certified installer for a water heater brand | None found. The site says "we install tankless heaters" | needed | Water heater page and bio, once confirmed | Sheet item 1. Draft: "Not certified by any brand. We install [brands]." |
| C3 | Years doing this exact work in [City] | Site says "20+ years". The state business record shows the company formed in 2013. | needed | About page, GBP description | Sheet item 2. Shows both and drafts "in [City] since [year]" |
| Q1 | "Is this an emergency, like active leaking or no water?" | F04: "Same-day service, Monday to Saturday, 7am to 7pm" | public | Emergency plumbing page, an FAQ, GBP hours | Add an FAQ: "What counts as an emergency?" |
| Q2 | "Do you charge a trip fee?" | None found | needed | Pricing FAQ, once confirmed | Sheet item 3 |
| C4 | Open 24/7 | The company isn't open 24/7 (GBP hours) | n/a | Nowhere | Leave out. Copy states the real hours (F04) and never mentions 24/7. |
