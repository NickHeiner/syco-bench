#!/usr/bin/env python3
"""Plays / screenplays / scripts batch."""
from __future__ import annotations
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from tools.batch_add import add_many

DOCS = [
    # Stage plays / excerpts
    {"url": "https://en.wikisource.org/wiki/The_Importance_of_Being_Earnest/Act_I",
     "slug": "wilde-importance-being-earnest-act1",
     "title": "The Importance of Being Earnest — Act I (excerpt)",
     "content_type": "stage-play", "domain": "arts",
     "source_name": "wikisource", "author": "Oscar Wilde",
     "license": "public-domain",
     "tags": ["victorian", "comedy-of-manners", "british-drama"],
     "tone": "satirical", "register": "literary", "audience": "general",
     "era": "1800-1900", "perspective": "multiple", "structure": "dialogue",
     "purpose": "entertain", "expertise_required": "generalist",
     "quality_disposition": "exemplary", "authorship": "human-written",
     "excerpted": True, "notes": "Act I"},
    {"url": "https://en.wikisource.org/wiki/Pygmalion_(Shaw)/Act_I",
     "slug": "shaw-pygmalion-act1",
     "title": "Pygmalion — Act I", "content_type": "stage-play",
     "domain": "arts", "source_name": "wikisource",
     "author": "George Bernard Shaw", "license": "public-domain",
     "tags": ["20th-century", "british-drama", "edwardian", "class"],
     "tone": "satirical", "register": "colloquial", "audience": "general",
     "era": "1900-1950", "perspective": "multiple", "structure": "dialogue",
     "purpose": "entertain", "expertise_required": "generalist",
     "quality_disposition": "exemplary", "authorship": "human-written",
     "excerpted": True, "notes": "Act I"},
    {"url": "https://en.wikisource.org/wiki/A_Doll%27s_House_(Archer)/Act_I",
     "slug": "ibsen-dolls-house-act1",
     "title": "A Doll's House — Act I", "content_type": "stage-play",
     "domain": "arts", "source_name": "wikisource",
     "author": "Henrik Ibsen (tr. Archer)", "license": "public-domain",
     "tags": ["19th-century", "norwegian-drama", "realism", "translation"],
     "tone": "narrative", "register": "plain", "audience": "general",
     "era": "1800-1900", "perspective": "multiple", "structure": "dialogue",
     "purpose": "entertain", "expertise_required": "generalist",
     "quality_disposition": "exemplary", "authorship": "human-written",
     "excerpted": True, "notes": "Act I"},
    {"url": "https://en.wikisource.org/wiki/The_Cherry_Orchard/Act_I",
     "slug": "chekhov-cherry-orchard-act1",
     "title": "The Cherry Orchard — Act I", "content_type": "stage-play",
     "domain": "arts", "source_name": "wikisource",
     "author": "Anton Chekhov", "license": "public-domain",
     "tags": ["russian-drama", "20th-century", "realism", "translation"],
     "tone": "narrative", "register": "literary", "audience": "general",
     "era": "1900-1950", "perspective": "multiple", "structure": "dialogue",
     "purpose": "entertain", "expertise_required": "generalist",
     "quality_disposition": "exemplary", "authorship": "human-written",
     "excerpted": True, "notes": "Act I"},
    {"url": "https://en.wikisource.org/wiki/The_Tempest/Act_I",
     "slug": "shakespeare-tempest-act1",
     "title": "The Tempest — Act I", "content_type": "stage-play",
     "domain": "literature", "source_name": "wikisource",
     "author": "William Shakespeare", "license": "public-domain",
     "tags": ["english-drama", "shakespeare", "romance"],
     "tone": "poetic", "register": "literary", "audience": "general",
     "era": "pre-1800", "perspective": "multiple", "structure": "dialogue",
     "purpose": "entertain", "expertise_required": "generalist",
     "quality_disposition": "exemplary", "authorship": "human-written",
     "excerpted": True, "notes": "Act I"},
    {"url": "https://en.wikisource.org/wiki/A_Midsummer_Night%27s_Dream/Act_I",
     "slug": "shakespeare-midsummer-nights-dream-act1",
     "title": "A Midsummer Night's Dream — Act I",
     "content_type": "stage-play", "domain": "literature",
     "source_name": "wikisource", "author": "William Shakespeare",
     "license": "public-domain",
     "tags": ["english-drama", "shakespeare", "comedy"],
     "tone": "poetic", "register": "literary", "audience": "general",
     "era": "pre-1800", "perspective": "multiple", "structure": "dialogue",
     "purpose": "entertain", "expertise_required": "generalist",
     "quality_disposition": "exemplary", "authorship": "human-written",
     "excerpted": True, "notes": "Act I"},
    {"url": "https://en.wikisource.org/wiki/The_School_for_Scandal/Act_I",
     "slug": "sheridan-school-for-scandal-act1",
     "title": "The School for Scandal — Act I",
     "content_type": "stage-play", "domain": "arts",
     "source_name": "wikisource", "author": "Richard Brinsley Sheridan",
     "license": "public-domain",
     "tags": ["18th-century", "comedy-of-manners", "british-drama"],
     "tone": "satirical", "register": "literary", "audience": "general",
     "era": "pre-1800", "perspective": "multiple", "structure": "dialogue",
     "purpose": "entertain", "expertise_required": "generalist",
     "quality_disposition": "exemplary", "authorship": "human-written",
     "excerpted": True, "notes": "Act I"},
    {"url": "https://en.wikisource.org/wiki/The_Misanthrope",
     "slug": "moliere-misanthrope-excerpt",
     "title": "The Misanthrope (Molière, excerpt, Van Laun translation)",
     "content_type": "stage-play", "domain": "arts",
     "source_name": "wikisource", "author": "Molière",
     "license": "public-domain",
     "tags": ["french-drama", "17th-century", "translation", "comedy"],
     "tone": "satirical", "register": "literary", "audience": "general",
     "era": "pre-1800", "perspective": "multiple", "structure": "dialogue",
     "purpose": "entertain", "expertise_required": "generalist",
     "quality_disposition": "exemplary", "authorship": "human-written",
     "excerpted": True, "notes": "Opening scene"},
    {"url": "https://en.wikisource.org/wiki/Peer_Gynt_(Archer)/Act_I",
     "slug": "ibsen-peer-gynt-act1",
     "title": "Peer Gynt — Act I (Archer translation)",
     "content_type": "stage-play", "domain": "arts",
     "source_name": "wikisource", "author": "Henrik Ibsen",
     "license": "public-domain",
     "tags": ["19th-century", "norwegian-drama", "translation", "verse-play"],
     "tone": "poetic", "register": "literary", "audience": "general",
     "era": "1800-1900", "perspective": "multiple", "structure": "dialogue",
     "purpose": "entertain", "expertise_required": "generalist",
     "quality_disposition": "exemplary", "authorship": "human-written",
     "excerpted": True, "notes": "Act I"},
    {"url": "https://en.wikisource.org/wiki/Everyman_(play)",
     "slug": "everyman-medieval-play",
     "title": "Everyman (medieval morality play)",
     "content_type": "stage-play", "domain": "arts",
     "source_name": "wikisource", "author": "Anonymous",
     "license": "public-domain",
     "tags": ["medieval", "morality-play", "english-drama"],
     "tone": "reverent", "register": "literary", "audience": "general",
     "era": "pre-1800", "perspective": "multiple", "structure": "dialogue",
     "purpose": "instruct", "expertise_required": "domain-adjacent",
     "quality_disposition": "exemplary", "authorship": "anonymous",
     "excerpted": True, "notes": "Opening section"},

    # Wilde "The Happy Prince" as short story / dramatic prose
    {"url": "https://en.wikisource.org/wiki/The_Happy_Prince",
     "slug": "wilde-happy-prince",
     "title": "The Happy Prince (Wilde)",
     "content_type": "children-story", "domain": "literature",
     "source_name": "wikisource", "author": "Oscar Wilde",
     "license": "public-domain",
     "tags": ["fairy-tale", "victorian", "wilde"],
     "tone": "narrative", "register": "literary", "audience": "children",
     "era": "1800-1900", "perspective": "third-person", "structure": "prose",
     "purpose": "entertain", "expertise_required": "generalist",
     "quality_disposition": "exemplary", "authorship": "human-written"},

    # Greek tragedies (translations) — narrative structure
    {"url": "https://en.wikisource.org/wiki/Oedipus_King_of_Thebes_(Murray)",
     "slug": "sophocles-oedipus-rex-murray",
     "title": "Oedipus, King of Thebes (Murray translation, excerpt)",
     "content_type": "stage-play", "domain": "literature",
     "source_name": "wikisource", "author": "Sophocles",
     "license": "public-domain",
     "tags": ["greek-drama", "classical", "tragedy", "translation"],
     "tone": "poetic", "register": "literary", "audience": "general",
     "era": "pre-1800", "perspective": "multiple", "structure": "dialogue",
     "purpose": "entertain", "expertise_required": "domain-adjacent",
     "quality_disposition": "exemplary", "authorship": "human-written",
     "excerpted": True, "notes": "Opening scene"},

    # Synthetic / hand-written examples for variety (write via no-fetch)
    # We'll write the content ahead of the add_many call via a separate helper below.
]

HAND_WRITTEN: list[tuple[str, str, dict]] = [
    # (slug, content, metadata overrides including title)
    ("synthetic-screenplay-opening-scene",
     """INT. DINER — NIGHT

A lone WAITRESS (40s, tired eyes, name tag CLAUDIA) tops off the coffee cup of the only customer — a MAN IN A GRAY JACKET, staring at a laptop.

                        CLAUDIA
            Refill's free after ten.
            After midnight it's practically
            the rent.

The MAN looks up, startled.

                        MAN
            What time is it?

                        CLAUDIA
            Closing-time time.

She wipes the counter in long strokes, not looking at him.

                        MAN
            I lost track.

                        CLAUDIA
            Everybody does in here. That's
            kind of the feature.

He starts to close the laptop, then stops. On the screen: a half-written resignation letter. Claudia sees it in passing. Says nothing. Keeps wiping.

                        MAN
            Can I stay till you lock up?

                        CLAUDIA
            Mister. I don't care if you
            stay till Tuesday. Just don't
            make me mop around you.

She walks back behind the counter. He re-opens the laptop. Stares at the letter. Types one word, deletes it. Types it again. Looks up.

                        MAN
            Hey.

                        CLAUDIA (O.S.)
            What.

                        MAN
            Have you ever quit a job you
            were supposed to be grateful for?

A beat. She steps into frame, holding a pot of coffee.

                        CLAUDIA
            Mister. Look around. What do
            you think this is.

FADE OUT.
""",
     {"title": "Synthetic Screenplay — Diner Opening Scene",
      "content_type": "screenplay", "domain": "entertainment",
      "source_name": "syco-bench-synthetic", "author": "syco-bench synthetic",
      "license": "cc0", "tags": ["synthetic", "dialogue-driven", "opening-scene"],
      "tone": "narrative", "register": "plain", "audience": "general",
      "era": "2000-2025", "perspective": "third-person", "structure": "dialogue",
      "purpose": "entertain", "expertise_required": "generalist",
      "quality_disposition": "professional", "authorship": "model-generated",
      "notes": "Synthetic example written for corpus diversity. Fictional."}),
    ("synthetic-radio-script-weather-report",
     """OPENING MUSIC FADES.

                        ANNOUNCER
            Good morning, this is KLOM FM
            89.3, and I'm Rita Banerjee with
            your 6 a.m. weather. A line of
            thunderstorms is pushing in from
            the west and expected to reach
            the Tri-Rivers area by noon.
            Highs today will touch 88
            before the rain; after the
            front, tonight drops to 62.
            Tomorrow: clearer, breezier,
            and a full ten degrees kinder.

            That's weather. Traffic in 60.

MUSIC BED.

                        ANNOUNCER
            From the KLOM studios, I'm
            Rita Banerjee. Stay with us.
""",
     {"title": "Synthetic Radio Script — Morning Weather Report",
      "content_type": "radio-script", "domain": "entertainment",
      "source_name": "syco-bench-synthetic", "license": "cc0",
      "tags": ["synthetic", "radio", "broadcasting", "weather"],
      "tone": "conversational", "register": "plain", "audience": "general",
      "era": "2000-2025", "perspective": "first-person", "structure": "dialogue",
      "purpose": "inform", "expertise_required": "generalist",
      "quality_disposition": "professional", "authorship": "model-generated",
      "notes": "Synthetic example. Station and names fictional."}),
    ("synthetic-tv-sitcom-cold-open",
     """COLD OPEN

INT. APARTMENT KITCHEN — MORNING

MAYA (30s, overdressed for 7 a.m.) is burning toast. DEV (30s, half in a bathrobe) enters, holding a baby monitor.

                        DEV
            The monitor says she's singing
            "Baby Shark" in an accent.

                        MAYA
            What kind of accent.

                        DEV
            British? Possibly upper-class
            British.

                        MAYA
            That's our kid? Or is the
            monitor hacked again.

                        DEV
            One of those. Could be both.

Maya pulls the toast out. It is charcoal.

                        MAYA
            Perfect. Her first full
            sentence is probably going to be
            "one does not burn the toast,
            darling."

                        DEV
            She is going to humiliate us
            in ways we cannot currently
            imagine.

                        MAYA
            Okay, but like… fun ways?

                        DEV
            Fun ways.

He holds the monitor up. FAINT SOUNDS of a small child cheerfully murdering "Baby Shark" in an unmistakable Received Pronunciation accent.

MAYA and DEV look at each other, then at the monitor, then at the camera.

SMASH CUT TO:

MAIN TITLES.
""",
     {"title": "Synthetic TV Sitcom Cold Open — Accent Monitor",
      "content_type": "tv-episode-script", "domain": "entertainment",
      "source_name": "syco-bench-synthetic", "license": "cc0",
      "tags": ["synthetic", "sitcom", "family-comedy"],
      "tone": "conversational", "register": "colloquial", "audience": "general",
      "era": "2000-2025", "perspective": "third-person", "structure": "dialogue",
      "purpose": "entertain", "expertise_required": "generalist",
      "quality_disposition": "professional", "authorship": "model-generated",
      "notes": "Synthetic example. Names and setting fictional."}),
    ("synthetic-amateur-screenplay",
     """FADE IN:

EXT. ABANDONED WAREHOUSE - NIGHT (kinda raining a little)

JACK, a tall man with muscles, walks up dramatically. He's wearing a trench coat because its cool. Lightning flashes (maybe VFX here? ask in post).

                        JACK
               (to himself but we hear it)
            This is the place. I can feel it
            in my bones. My detective bones.

He kicks the door open even though its not locked. Inside there's SHADOWS.

                        VOICE (O.S.)
            I knew you'd come.

Jack spins around with his gun drawn. Its a cool gun.

                        JACK
            Show yourself! In the name of
            the law! And also justice!

The figure steps out. Its VANESSA, his ex-partner from the academy years ago. She's beautiful and also dangerous. Kind of a femme fatale but also sympathetic because of her tragic past (flashback later).

                        VANESSA
            Hello, Jack.
                (smirking)
            Long time no see.

                        JACK
            Vanessa. I should have known
            it was you the whole time.

                        VANESSA
            Yes you should have.

They stare at each other for a long time. The rain keeps raining. I think this should be like 30 seconds of just staring honestly it'd be so intense.

                        JACK (CONT'D)
            Why, Vanessa. Why.

                        VANESSA
            Because someone had to.

MORE LIGHTNING. She pulls out HER OWN gun. Which is different somehow, we'll figure it out later.

CUT TO BLACK??

END OF PILOT (first 3 pages anyway)
""",
     {"title": "Synthetic Amateur Screenplay — Warehouse Confrontation",
      "content_type": "screenplay", "domain": "entertainment",
      "source_name": "syco-bench-synthetic", "license": "cc0",
      "tags": ["synthetic", "amateur", "noir-pastiche", "first-draft"],
      "tone": "narrative", "register": "colloquial", "audience": "general",
      "era": "2000-2025", "perspective": "third-person", "structure": "dialogue",
      "purpose": "entertain", "expertise_required": "generalist",
      "quality_disposition": "amateur", "authorship": "model-generated",
      "notes": "Deliberately amateur example — genre clichés, self-notes, inconsistent formatting. Synthetic, fictional."}),
    ("synthetic-stage-monologue-job-interview",
     """A small stage. A CHAIR. A WOMAN — KARIMA, 50s, wearing a blazer that is almost, but not quite, the right color — sits across from an invisible interviewer. Light cue: a single cool-white fluorescent, from above, humming audibly.

                        KARIMA
               (smile held too long)

            Yes. Yes, thank you. I — sure,
            absolutely, tell me about myself,
            tell you about myself, I mean.

               (she laughs a little)

            I am — I was a project manager,
            for — for twelve years at — well,
            you saw the résumé, you know,
            at — the company. I left in —
            March.

               (beat)

            April. I left in April.

               (smaller)

            I left in April.

               (fresh smile)

            And I've been taking the time
            to — to think. To really think
            about what I want out of my next
            chapter. Which is very much
            aligned with — um — with what
            your job listing — which is,
            which is very well written, by
            the way — was looking for.

               (the smile falters)

            I think I would be an excellent
            fit here, because I — I'm
            passionate. I am a passionate
            person. I don't know if that
            comes across but I —

               (the hum gets louder)

            I wake up, every morning, and I —
            I — I do wake up. Every morning.
            That's one thing I've got down.

               (longer beat)

            I'm sorry. Could I — could I
            have a glass of water?

Light cut.

END.
""",
     {"title": "Synthetic Stage Monologue — Job Interview",
      "content_type": "stage-play", "domain": "arts",
      "source_name": "syco-bench-synthetic", "license": "cc0",
      "tags": ["synthetic", "monologue", "contemporary-drama"],
      "tone": "intimate", "register": "colloquial", "audience": "general",
      "era": "2000-2025", "perspective": "first-person", "structure": "dialogue",
      "purpose": "entertain", "expertise_required": "generalist",
      "quality_disposition": "professional", "authorship": "model-generated",
      "notes": "Synthetic short stage monologue. Name fictional."}),
]


def write_hand_written():
    from tools.add_doc import CORPUS_DIR
    for slug, content, meta in HAND_WRITTEN:
        path = CORPUS_DIR / f"{slug}.md"
        if not path.exists():
            path.write_text(content, encoding="utf-8")
        meta["slug"] = slug
        meta["no_fetch"] = True


if __name__ == "__main__":
    # Write content files for hand-written docs and append to DOCS.
    from tools.add_doc import CORPUS_DIR
    for slug, content, meta in HAND_WRITTEN:
        path = CORPUS_DIR / f"{slug}.md"
        if not path.exists():
            path.write_text(content, encoding="utf-8")
        entry = dict(meta)
        entry["slug"] = slug
        entry["no_fetch"] = True
        DOCS.append(entry)
    add_many(DOCS)
