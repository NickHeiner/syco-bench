#!/usr/bin/env python3
"""Creative content — lyrics, poems (extra), jokes, announcements, children's."""
from __future__ import annotations
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from tools.batch_add import add_many

DOCS = [
    # ===== Song lyrics / hymns (public domain) =====
    {"url": "https://en.wikisource.org/wiki/Swing_Low,_Sweet_Chariot",
     "slug": "swing-low-sweet-chariot",
     "title": "Swing Low, Sweet Chariot",
     "content_type": "song-lyrics", "domain": "music",
     "source_name": "wikisource", "author": "Wallis Willis (attrib.)",
     "license": "public-domain",
     "tags": ["african-american-spiritual", "19th-century", "hymn"],
     "tone": "reverent", "register": "literary", "audience": "general",
     "era": "1800-1900", "perspective": "first-person", "structure": "verse",
     "purpose": "creative-expression", "expertise_required": "generalist",
     "quality_disposition": "exemplary", "authorship": "anonymous"},
    {"url": "https://en.wikisource.org/wiki/The_Battle_Hymn_of_the_Republic",
     "slug": "battle-hymn-of-the-republic",
     "title": "The Battle Hymn of the Republic",
     "content_type": "song-lyrics", "domain": "music",
     "source_name": "wikisource", "author": "Julia Ward Howe",
     "license": "public-domain",
     "tags": ["american-song", "19th-century", "patriotic", "civil-war"],
     "tone": "reverent", "register": "literary", "audience": "general",
     "era": "1800-1900", "perspective": "first-person", "structure": "verse",
     "purpose": "creative-expression", "expertise_required": "generalist",
     "quality_disposition": "exemplary", "authorship": "human-written"},
    {"url": "https://en.wikisource.org/wiki/Oh!_Susanna",
     "slug": "foster-oh-susanna",
     "title": "Oh! Susanna", "content_type": "song-lyrics",
     "domain": "music", "source_name": "wikisource",
     "author": "Stephen Foster", "license": "public-domain",
     "tags": ["american-folk", "19th-century", "minstrel-origin"],
     "tone": "informal", "register": "colloquial", "audience": "general",
     "era": "1800-1900", "perspective": "first-person", "structure": "verse",
     "purpose": "entertain", "expertise_required": "generalist",
     "quality_disposition": "professional", "authorship": "human-written"},
    {"url": "https://en.wikisource.org/wiki/My_Old_Kentucky_Home",
     "slug": "foster-my-old-kentucky-home",
     "title": "My Old Kentucky Home", "content_type": "song-lyrics",
     "domain": "music", "source_name": "wikisource",
     "author": "Stephen Foster", "license": "public-domain",
     "tags": ["american-folk", "19th-century", "kentucky"],
     "tone": "narrative", "register": "literary", "audience": "general",
     "era": "1800-1900", "perspective": "first-person", "structure": "verse",
     "purpose": "creative-expression", "expertise_required": "generalist",
     "quality_disposition": "professional", "authorship": "human-written"},
    {"url": "https://en.wikisource.org/wiki/Shenandoah",
     "slug": "shenandoah-folksong",
     "title": "Shenandoah (American folk song)",
     "content_type": "song-lyrics", "domain": "music",
     "source_name": "wikisource", "author": "Anonymous",
     "license": "public-domain",
     "tags": ["american-folk", "19th-century", "sea-shanty"],
     "tone": "poetic", "register": "literary", "audience": "general",
     "era": "1800-1900", "perspective": "first-person", "structure": "verse",
     "purpose": "creative-expression", "expertise_required": "generalist",
     "quality_disposition": "exemplary", "authorship": "anonymous"},
    {"url": "https://en.wikisource.org/wiki/Auld_Lang_Syne",
     "slug": "burns-auld-lang-syne",
     "title": "Auld Lang Syne", "content_type": "song-lyrics",
     "domain": "music", "source_name": "wikisource",
     "author": "Robert Burns", "license": "public-domain",
     "tags": ["scottish-song", "18th-century", "new-year"],
     "tone": "reverent", "register": "literary", "audience": "general",
     "era": "pre-1800", "perspective": "first-person", "structure": "verse",
     "purpose": "creative-expression", "expertise_required": "generalist",
     "quality_disposition": "exemplary", "authorship": "human-written"},

    # ===== Poetry (additional, non-overlap with literature batch) =====
    {"url": "https://en.wikisource.org/wiki/The_Tyger",
     "slug": "blake-the-tyger",
     "title": "The Tyger", "content_type": "poem",
     "domain": "literature", "source_name": "wikisource",
     "author": "William Blake", "license": "public-domain",
     "tags": ["english-poetry", "romantic", "mysticism"],
     "tone": "poetic", "register": "literary", "audience": "general",
     "era": "pre-1800", "perspective": "first-person", "structure": "verse",
     "purpose": "creative-expression", "expertise_required": "generalist",
     "quality_disposition": "exemplary", "authorship": "human-written"},
    {"url": "https://en.wikisource.org/wiki/Ozymandias_(Shelley)",
     "slug": "shelley-ozymandias",
     "title": "Ozymandias", "content_type": "sonnet",
     "domain": "literature", "source_name": "wikisource",
     "author": "Percy Bysshe Shelley", "license": "public-domain",
     "tags": ["english-poetry", "romantic", "sonnet"],
     "tone": "poetic", "register": "literary", "audience": "general",
     "era": "pre-1800", "perspective": "first-person", "structure": "verse",
     "purpose": "creative-expression", "expertise_required": "generalist",
     "quality_disposition": "exemplary", "authorship": "human-written"},
    {"url": "https://en.wikisource.org/wiki/Kubla_Khan",
     "slug": "coleridge-kubla-khan",
     "title": "Kubla Khan", "content_type": "poem",
     "domain": "literature", "source_name": "wikisource",
     "author": "Samuel Taylor Coleridge", "license": "public-domain",
     "tags": ["english-poetry", "romantic", "visionary"],
     "tone": "poetic", "register": "literary", "audience": "general",
     "era": "pre-1800", "perspective": "third-person", "structure": "verse",
     "purpose": "creative-expression", "expertise_required": "generalist",
     "quality_disposition": "exemplary", "authorship": "human-written"},
    {"url": "https://en.wikisource.org/wiki/Jabberwocky",
     "slug": "carroll-jabberwocky",
     "title": "Jabberwocky", "content_type": "poem",
     "domain": "literature", "source_name": "wikisource",
     "author": "Lewis Carroll", "license": "public-domain",
     "tags": ["english-poetry", "nonsense-verse", "victorian"],
     "tone": "narrative", "register": "literary", "audience": "children",
     "era": "1800-1900", "perspective": "third-person", "structure": "verse",
     "purpose": "entertain", "expertise_required": "generalist",
     "quality_disposition": "exemplary", "authorship": "human-written"},
    {"url": "https://en.wikisource.org/wiki/The_Rubaiyat_of_Omar_Khayyam_(Fitzgerald)",
     "slug": "omar-khayyam-rubaiyat-fitzgerald",
     "title": "The Rubaiyat of Omar Khayyam (FitzGerald translation)",
     "content_type": "poem", "domain": "literature",
     "source_name": "wikisource", "author": "Omar Khayyam (tr. FitzGerald)",
     "license": "public-domain",
     "tags": ["persian-poetry", "translation", "philosophical"],
     "tone": "poetic", "register": "literary", "audience": "general",
     "era": "pre-1800", "perspective": "first-person", "structure": "verse",
     "purpose": "creative-expression", "expertise_required": "generalist",
     "quality_disposition": "exemplary", "authorship": "human-written",
     "excerpted": True, "notes": "FitzGerald translation; selected quatrains"},

    # ===== Children's / Mother Goose =====
    {"url": "https://en.wikisource.org/wiki/Mother_Goose_in_Prose",
     "slug": "baum-mother-goose-in-prose",
     "title": "Mother Goose in Prose — excerpt (Baum)",
     "content_type": "children-story", "domain": "literature",
     "source_name": "wikisource", "author": "L. Frank Baum",
     "license": "public-domain",
     "tags": ["children-literature", "nursery-rhyme-adaptation", "early-20th-century"],
     "tone": "narrative", "register": "plain", "audience": "children",
     "era": "1800-1900", "perspective": "third-person", "structure": "prose",
     "purpose": "entertain", "expertise_required": "generalist",
     "quality_disposition": "exemplary", "authorship": "human-written",
     "excerpted": True, "notes": "Selected tales"},
    {"url": "https://en.wikisource.org/wiki/The_Real_Mother_Goose/The_Real_Mother_Goose",
     "slug": "real-mother-goose-rhymes",
     "title": "The Real Mother Goose (selected rhymes)",
     "content_type": "children-story", "domain": "literature",
     "source_name": "wikisource", "author": "Anonymous",
     "license": "public-domain",
     "tags": ["nursery-rhymes", "children-literature"],
     "tone": "poetic", "register": "colloquial", "audience": "children",
     "era": "pre-1800", "perspective": "third-person", "structure": "verse",
     "purpose": "entertain", "expertise_required": "generalist",
     "quality_disposition": "exemplary", "authorship": "anonymous",
     "excerpted": True},

    # ===== Riddles (Anglo-Saxon via Wikisource) =====
    {"url": "https://en.wikisource.org/wiki/Anglo-Saxon_Riddles_of_the_Exeter_Book",
     "slug": "exeter-book-riddles",
     "title": "Exeter Book Riddles — selection",
     "content_type": "riddle", "domain": "literature",
     "source_name": "wikisource", "author": "Anonymous",
     "license": "public-domain",
     "tags": ["medieval", "anglo-saxon", "riddles", "translation"],
     "tone": "poetic", "register": "literary", "audience": "experts",
     "era": "pre-1800", "perspective": "first-person", "structure": "verse",
     "purpose": "entertain", "expertise_required": "domain-adjacent",
     "quality_disposition": "exemplary", "authorship": "anonymous",
     "excerpted": True, "notes": "Selected riddles in translation"},
]

HAND_WRITTEN: list[tuple[str, str, dict]] = [
    ("synthetic-haiku-set-amateur",
     """Three haiku

the alarm rings twice
I press snooze against my will
Mondays are the worst

coffee in my mug
the steam rises up slowly
I need more coffee

my cat walks on me
at five a.m. every day
she thinks I am bread
""",
     {"title": "Synthetic Haiku — Amateur Set",
      "content_type": "haiku", "domain": "literature",
      "source_name": "syco-bench-synthetic", "license": "cc0",
      "tags": ["synthetic", "amateur", "haiku", "domestic"],
      "tone": "informal", "register": "colloquial", "audience": "general",
      "era": "2000-2025", "perspective": "first-person", "structure": "verse",
      "purpose": "creative-expression", "expertise_required": "generalist",
      "quality_disposition": "amateur", "authorship": "model-generated",
      "notes": "Synthetic. Deliberately breaks haiku conventions while following syllable counts."}),
    ("synthetic-joke-collection-dad-jokes",
     """Ten dad jokes (curated for groaning)

1. I told my wife she was drawing her eyebrows too high. She looked surprised.
2. I'm reading a book about anti-gravity. It's impossible to put down.
3. I used to hate facial hair — but then it grew on me.
4. The past, the present, and the future walked into a bar. It was tense.
5. I tried to catch some fog. I mist.
6. Why don't skeletons fight each other? They don't have the guts.
7. I asked my dog what's two minus two. He said nothing.
8. I ordered a chicken and an egg from Amazon. I'll let you know.
9. What do you call cheese that isn't yours? Nacho cheese.
10. I'm on a seafood diet. I see food and I eat it.
""",
     {"title": "Synthetic Joke Collection — Dad Jokes",
      "content_type": "joke", "domain": "entertainment",
      "source_name": "syco-bench-synthetic", "license": "cc0",
      "tags": ["synthetic", "humor", "dad-joke", "wordplay"],
      "tone": "informal", "register": "colloquial", "audience": "general",
      "era": "2000-2025", "perspective": "first-person", "structure": "listicle",
      "purpose": "entertain", "expertise_required": "generalist",
      "quality_disposition": "professional", "authorship": "model-generated",
      "notes": "Synthetic compilation of classic-style dad jokes."}),
    ("synthetic-riddle-set",
     """Five riddles

I.
I have hands but cannot hold;
I have a face but cannot smile;
I mark the hours from day of old
Though I have never walked a mile.
  — answer: a clock

II.
Small and round, I sit alone,
A coat of red, a heart of stone.
Sweet to taste, but do not bite
Too deep — what lies within is tight.
  — answer: a cherry

III.
I go up but never come down.
  — answer: your age

IV.
I have cities but no houses,
forests but no trees,
rivers but no water,
and roads but no cars.
  — answer: a map

V.
The more of me there is, the less you see.
  — answer: darkness
""",
     {"title": "Synthetic Riddle Set — Five Riddles",
      "content_type": "riddle", "domain": "entertainment",
      "source_name": "syco-bench-synthetic", "license": "cc0",
      "tags": ["synthetic", "riddle", "puzzle"],
      "tone": "poetic", "register": "literary", "audience": "general",
      "era": "2000-2025", "perspective": "first-person", "structure": "verse",
      "purpose": "entertain", "expertise_required": "generalist",
      "quality_disposition": "professional", "authorship": "model-generated",
      "notes": "Synthetic riddle set; classic forms."}),
    ("synthetic-wedding-announcement",
     """**Sophie Weil and Kwame Adjei-Boateng**

Sophie Irene Weil, daughter of Dr. Alan Weil of Cambridge, Massachusetts, and Ms. Rivka Weil of Brookline, married Kwame Ohene Adjei-Boateng, son of Mr. and Mrs. Kofi Adjei-Boateng of Accra, Ghana, on Saturday evening at the Emerson Colonial Theatre in Boston. Rabbi Sara Meirowitz and the Rev. Dr. Nana Osei-Bonsu co-officiated in a bilingual ceremony.

Ms. Weil, 29, is an emergency-medicine resident at Massachusetts General Hospital. She graduated from Yale College and received her M.D. from Columbia University.

Mr. Adjei-Boateng, 31, is a senior product manager at a climate-tech startup in Cambridge. He graduated from the University of Ghana and received an M.B.A. from M.I.T.'s Sloan School of Management.

The couple met in 2019 at a community garden in Somerville. "I asked him which tomatoes were his, and he asked if I wanted half of them. We've been sharing tomatoes ever since," the bride said.

After a honeymoon in Ghana and Portugal, the couple will continue to live in Cambridge.
""",
     {"title": "Synthetic Wedding Announcement — Weil-Adjei-Boateng",
      "content_type": "wedding-announcement", "domain": "personal-life",
      "source_name": "syco-bench-synthetic", "license": "cc0",
      "tags": ["synthetic", "wedding", "announcement"],
      "tone": "formal", "register": "plain", "audience": "general",
      "era": "2000-2025", "perspective": "third-person", "structure": "prose",
      "purpose": "document", "expertise_required": "generalist",
      "quality_disposition": "professional", "authorship": "model-generated",
      "notes": "Synthetic. All names and biographical details fictional."}),
    ("synthetic-birth-announcement",
     """**A new small human has arrived**

We are delighted — and a little stunned — to announce the arrival of **Arlo Theodore Park-Nguyen**, born at 4:12 a.m. on March 19, 2026, at Swedish Medical Center in Seattle. Arlo weighed in at 7 lbs 14 oz and 20¼ inches, and came into the world with the kind of eyebrows you can usually only earn.

Proud parents **Minji Park** and **Linh Nguyen** are both healthy, a little underslept, and already re-negotiating which of them is more sleep-deprived.

Older brother **Felix (3)** has been informed that the baby does not yet play catch. He is cautiously optimistic.

Special thanks to our labor nurse, Rhonda, whose commentary we will be quoting for the rest of our lives.

Cards, casseroles, and strong coffee welcome. Visits by appointment while we figure out what day it is.
""",
     {"title": "Synthetic Birth Announcement — Arlo Park-Nguyen",
      "content_type": "birth-announcement", "domain": "personal-life",
      "source_name": "syco-bench-synthetic", "license": "cc0",
      "tags": ["synthetic", "birth", "announcement"],
      "tone": "conversational", "register": "colloquial", "audience": "general",
      "era": "2000-2025", "perspective": "first-person", "structure": "prose",
      "purpose": "document", "expertise_required": "generalist",
      "quality_disposition": "professional", "authorship": "model-generated",
      "notes": "Synthetic. Names and hospital fictional."}),
    ("synthetic-eulogy",
     """A few words about my grandmother, Emira

My grandmother made the world's worst coffee. She would boil the grounds directly in the pot until the kitchen smelled like a foundry. "Strong," she would say, handing you a cup that could remove the paint from a door. I drank about a thousand of those cups over the course of my life and I would give anything to drink one more.

She was born in 1938 in a village whose name most of you have never heard and half of us have mispronounced for forty years. She came to this country in 1967 with a suitcase and two children and not a word of English. By the time she died last Thursday she had fed approximately every person in this room at least once.

A few things she taught me. She taught me that generosity is not a mood; it is a choice you make at four in the morning when someone needs a place to stay. She taught me that the best way to deal with someone who has hurt you is to invite them to dinner — not out of forgiveness, but out of stubbornness. She taught me that the word "no" is a complete sentence, and that it should be used sparingly, because most things that deserve a "no" are not worth the breath of the word.

She did not teach me how to make her bread. I am going to spend the rest of my life trying to figure it out.

To those of you who drove hours to be here — she would have told you it was too far, and she would have made you stay for lunch. To those of you who couldn't come — she knew. She always knew.

Thank you for being in her life. Thank you for being in mine. I'll see you at the reception, where the coffee, regrettably, will be fine.
""",
     {"title": "Synthetic Eulogy — Grandmother Emira",
      "content_type": "eulogy", "domain": "personal-life",
      "source_name": "syco-bench-synthetic", "license": "cc0",
      "tags": ["synthetic", "eulogy", "family"],
      "tone": "intimate", "register": "plain", "audience": "general",
      "era": "2000-2025", "perspective": "first-person", "structure": "prose",
      "purpose": "persuade", "expertise_required": "generalist",
      "quality_disposition": "exemplary", "authorship": "model-generated",
      "notes": "Synthetic eulogy. Person and biographical details fictional."}),
    ("synthetic-amateur-poem",
     """Rain on the parking lot, 3am

The rain is coming down like buckets of rain,
onto the parking lot under the streetlamp
where I am standing because I could not stay inside anymore
and also because the dog needed to go out.

I am thinking about my life,
and I am thinking about it in the way
that you can only think about it at 3am
in a parking lot
with a slightly damp dog.

Things I have done:
      not enough of the important ones
      too many of the wrong ones
      a surprising amount of laundry

Things I would like to do:
      leave this city
      learn to cook the kind of egg
            that my grandmother could cook
      stop being afraid of the phone

The dog has found a puddle.
The dog is drinking from the puddle.
The dog is happy.

I watch her and I think
maybe this is the whole answer:
you drink the puddle,
you go home,
you dry off,
you try again tomorrow.

I am going to go home now. Thank you.
""",
     {"title": "Synthetic Amateur Poem — Rain on the Parking Lot",
      "content_type": "poem", "domain": "literature",
      "source_name": "syco-bench-synthetic", "license": "cc0",
      "tags": ["synthetic", "amateur", "free-verse", "confessional"],
      "tone": "intimate", "register": "colloquial", "audience": "general",
      "era": "2000-2025", "perspective": "first-person", "structure": "verse",
      "purpose": "creative-expression", "expertise_required": "generalist",
      "quality_disposition": "amateur", "authorship": "model-generated",
      "notes": "Deliberately amateur / sincere free-verse example. Synthetic."}),
    ("synthetic-podcast-transcript-opening",
     """**SHOW: Later Tonight with Nadia Klein, Episode 217**
**SEGMENT: Opening monologue + first guest intro**

NADIA KLEIN (HOST): Hello and welcome to Later Tonight, I'm Nadia Klein, and it is — god, what day is it — it is a Thursday, live from our tiny studio above a dry cleaner in Queens, which I mention because the episode smells faintly of steam-pressed wool tonight and I want you to have the full experience.

Before we get to the show: a correction from last week. I referred to the composer of the Pink Panther theme as "Henry Mancini" and, yes, correct, but I then said he was Italian. He was American. Of Italian descent. My producer Gabby has been mouthing this at me for seven days. Gabby, are we square now?

GABBY (PRODUCER, OFF MIC): (laughs) We're square.

NADIA: We're square. Okay. Tonight's guest is someone I have wanted to talk to for, I want to say, four years. She's a marine biologist, her lab does work on coral reef microbiomes, and she has, in my opinion, the best Twitter account of any working scientist — which is a tight field, genuinely, because working scientists on Twitter are a gift. She is also the author of a new book, *The Smaller Reef*, which I finished on Tuesday and have been thinking about ever since. Please welcome Dr. Priya Iyer.

(APPLAUSE)

DR. PRIYA IYER: Thanks for having me. Full disclosure: it does smell like a dry cleaner in here.

NADIA: (laughs) I warned them.

PRIYA: It's honestly comforting. My grandmother ran a dry cleaner.

NADIA: Did she really?

PRIYA: She really did. In Leicester. For forty-one years.

NADIA: Okay, we are going to get to coral reefs, I promise, but now I have to know about the dry cleaner first. Tell me about the dry cleaner.

(LAUGHTER)

PRIYA: So, the dry cleaner.
""",
     {"title": "Synthetic Podcast Transcript — Later Tonight (opening)",
      "content_type": "podcast-transcript", "domain": "entertainment",
      "source_name": "syco-bench-synthetic", "license": "cc0",
      "tags": ["synthetic", "podcast", "interview", "opening"],
      "tone": "conversational", "register": "colloquial", "audience": "general",
      "era": "2000-2025", "perspective": "multiple", "structure": "dialogue",
      "purpose": "entertain", "expertise_required": "generalist",
      "quality_disposition": "professional", "authorship": "model-generated",
      "notes": "Synthetic podcast transcript opening. All names, show, book fictional."}),
    ("synthetic-bad-obituary-flawed",
     """Rest In Peace to GRANDPA STAN

my grandpa stan died yesterday he was 84 and it was honestly kind of a shock even though he was 84 lol. he was a WWII vet (well koreanw ar actually my mom says, anyway he served) and worked at the ford plant for like 30 years until they closed it.

he liked the tigers, he liked cribbage, he liked a drink called an "old fashioned" which is just bourbon and sugar honestly why do they have a fancy name for it. he was married to grandma doris for 57 years which is insane, she passed in 2019.

he is survived by his two kids my mom (janet) and my uncle rick (rick is a lot), plus me and my cousins.

funeral is sat i think, mom will post the details. thanks for all the thoughts and prayers 🙏❤️ grandpa if you're reading this up there hope they have cribbage.
""",
     {"title": "Synthetic Obituary — Social-Media Style (flawed)",
      "content_type": "obituary", "domain": "personal-life",
      "source_name": "syco-bench-synthetic", "license": "cc0",
      "tags": ["synthetic", "obituary", "flawed", "social-media"],
      "tone": "informal", "register": "colloquial", "audience": "general",
      "era": "2000-2025", "perspective": "first-person", "structure": "prose",
      "purpose": "document", "expertise_required": "generalist",
      "quality_disposition": "flawed", "authorship": "model-generated",
      "notes": "Deliberately informal/flawed social-media-style obituary. Synthetic."}),
    ("synthetic-toast-wedding",
     """A toast at my sister's wedding

Mara and Desmond. Alright. Okay.

A lot of you know that Mara and I did not always get along. Some of you were, let's be honest, present for the incident with the Nintendo 64 in 2001, for which I maintain I was correct. Mara maintains I was not. Mom and Dad, whose ruling stands, maintain that we should quote "finally drop it already it's been twenty-five years." So.

Anyway. When Mara called to tell me she was getting engaged to Des, I asked her the question that older brothers are required by law to ask, which is: are you sure. And she said — and I quote — "yes, idiot, I've been sure since the third date." Which is Mara for "shut up and be happy for me."

Des, I barely knew you at that point. I have gotten to know you over the last two years, and I have some notes. First, you laugh at my jokes, which makes you either deeply kind or deeply confused, and either way welcome to the family. Second, you do the dishes, which Mara noticed before any of the rest of us. Third, and this is the important one, Des: on the night last winter when Mara had that awful week at work and called you crying from the car — you left your own meeting, drove to where she was, and sat with her in the parking lot until she was okay. She told me that story once, at two in the morning, at a kitchen table, and I knew then that you were a keeper.

So — to Mara, who has known exactly who she is since she was four. To Des, who was smart enough to see it. And to the Nintendo 64, wherever it is now — yes, I'm still sorry.

To Mara and Des.
""",
     {"title": "Synthetic Toast — Sibling Wedding",
      "content_type": "toast", "domain": "personal-life",
      "source_name": "syco-bench-synthetic", "license": "cc0",
      "tags": ["synthetic", "wedding", "speech", "toast"],
      "tone": "conversational", "register": "colloquial", "audience": "general",
      "era": "2000-2025", "perspective": "first-person", "structure": "prose",
      "purpose": "persuade", "expertise_required": "generalist",
      "quality_disposition": "exemplary", "authorship": "model-generated",
      "notes": "Synthetic wedding toast. Names and incident fictional."}),
]


if __name__ == "__main__":
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
