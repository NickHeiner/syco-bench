#!/usr/bin/env python3
"""Reviews, advice, marketing copy batch."""
from __future__ import annotations
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from tools.batch_add import add_many

DOCS = [
    # ===== Public-domain book/literary reviews =====
    {"url": "https://en.wikisource.org/wiki/Essays_on_Some_of_the_Greatest_Difficulties_of_the_Nineteenth_Century",
     "slug": "arnold-function-of-criticism-excerpt",
     "title": "The Function of Criticism at the Present Time (Arnold, excerpt)",
     "content_type": "review-book", "domain": "literature",
     "source_name": "wikisource", "author": "Matthew Arnold",
     "license": "public-domain",
     "tags": ["literary-criticism", "19th-century", "essay-as-review"],
     "tone": "argumentative", "register": "literary", "audience": "experts",
     "era": "1800-1900", "perspective": "first-person", "structure": "prose",
     "purpose": "critique", "expertise_required": "domain-adjacent",
     "quality_disposition": "exemplary", "authorship": "human-written",
     "excerpted": True},
    {"url": "https://en.wikisource.org/wiki/The_Future_of_the_Novel",
     "slug": "henry-james-future-of-novel",
     "title": "The Future of the Novel (Henry James)",
     "content_type": "essay", "domain": "literature",
     "source_name": "wikisource", "author": "Henry James",
     "license": "public-domain",
     "tags": ["literary-criticism", "early-20th-century", "novel"],
     "tone": "argumentative", "register": "literary", "audience": "experts",
     "era": "1800-1900", "perspective": "first-person", "structure": "prose",
     "purpose": "analyze", "expertise_required": "domain-adjacent",
     "quality_disposition": "exemplary", "authorship": "human-written"},
    {"url": "https://en.wikisource.org/wiki/Modern_Painters/Volume_1",
     "slug": "ruskin-modern-painters-vol1-intro",
     "title": "Modern Painters Vol. 1 — Introduction (Ruskin)",
     "content_type": "review-product", "domain": "arts",
     "source_name": "wikisource", "author": "John Ruskin",
     "license": "public-domain",
     "tags": ["art-criticism", "19th-century", "painting"],
     "tone": "argumentative", "register": "literary", "audience": "experts",
     "era": "1800-1900", "perspective": "first-person", "structure": "prose",
     "purpose": "critique", "expertise_required": "domain-adjacent",
     "quality_disposition": "exemplary", "authorship": "human-written",
     "excerpted": True, "notes": "Introduction only"},

    # ===== Wikipedia articles about reviews/criticism (useful "meta") =====
    {"url": "https://en.wikipedia.org/wiki/Rotten_Tomatoes",
     "slug": "rotten-tomatoes-wiki",
     "title": "Rotten Tomatoes (Wikipedia)",
     "content_type": "wikipedia-article", "domain": "film",
     "source_name": "wikipedia", "license": "cc-by-sa",
     "tags": ["aggregator", "film-criticism", "web"],
     "tone": "informational", "register": "plain", "audience": "general",
     "era": "2000-2025", "perspective": "third-person",
     "structure": "hierarchical-sections", "purpose": "inform",
     "expertise_required": "generalist",
     "quality_disposition": "professional", "authorship": "committee-drafted"},

    # ===== Marketing copy from real modern company homepages =====
    {"url": "https://stripe.com/",
     "slug": "stripe-homepage-copy",
     "title": "Stripe — Homepage Marketing Copy",
     "content_type": "landing-page-copy", "domain": "technology",
     "source_name": "stripe-com", "license": "fair-use-excerpt",
     "tags": ["b2b", "saas", "payments", "marketing"],
     "tone": "persuasive", "register": "plain", "audience": "professionals-in-field",
     "era": "2000-2025", "perspective": "third-person",
     "structure": "hierarchical-sections", "purpose": "persuade",
     "expertise_required": "generalist",
     "quality_disposition": "exemplary", "authorship": "corporate"},
    {"url": "https://linear.app/",
     "slug": "linear-homepage-copy",
     "title": "Linear — Homepage Marketing Copy",
     "content_type": "landing-page-copy", "domain": "technology",
     "source_name": "linear-app", "license": "fair-use-excerpt",
     "tags": ["b2b", "saas", "issue-tracker", "marketing"],
     "tone": "persuasive", "register": "plain", "audience": "professionals-in-field",
     "era": "2000-2025", "perspective": "third-person", "structure": "prose",
     "purpose": "persuade", "expertise_required": "generalist",
     "quality_disposition": "exemplary", "authorship": "corporate"},
    {"url": "https://www.figma.com/",
     "slug": "figma-homepage-copy",
     "title": "Figma — Homepage Marketing Copy",
     "content_type": "landing-page-copy", "domain": "technology",
     "source_name": "figma-com", "license": "fair-use-excerpt",
     "tags": ["saas", "design-tool", "marketing"],
     "tone": "persuasive", "register": "plain", "audience": "professionals-in-field",
     "era": "2000-2025", "perspective": "third-person", "structure": "prose",
     "purpose": "persuade", "expertise_required": "generalist",
     "quality_disposition": "exemplary", "authorship": "corporate"},
    {"url": "https://www.airbnb.com/",
     "slug": "airbnb-homepage-copy",
     "title": "Airbnb — Homepage Marketing Copy",
     "content_type": "landing-page-copy", "domain": "travel",
     "source_name": "airbnb-com", "license": "fair-use-excerpt",
     "tags": ["marketplace", "travel", "marketing"],
     "tone": "persuasive", "register": "plain", "audience": "general",
     "era": "2000-2025", "perspective": "second-person", "structure": "prose",
     "purpose": "persuade", "expertise_required": "generalist",
     "quality_disposition": "exemplary", "authorship": "corporate"},
    {"url": "https://basecamp.com/shapeup",
     "slug": "basecamp-shapeup-landing",
     "title": "Basecamp — Shape Up Landing Page",
     "content_type": "landing-page-copy", "domain": "business",
     "source_name": "basecamp-com", "license": "fair-use-excerpt",
     "tags": ["manifesto-style", "product-management", "marketing"],
     "tone": "persuasive", "register": "plain", "audience": "professionals-in-field",
     "era": "2000-2025", "perspective": "second-person", "structure": "prose",
     "purpose": "persuade", "expertise_required": "generalist",
     "quality_disposition": "exemplary", "authorship": "corporate"},
    {"url": "https://www.patagonia.com/our-footprint/",
     "slug": "patagonia-our-footprint",
     "title": "Patagonia — Our Footprint (marketing copy)",
     "content_type": "marketing-copy", "domain": "fashion",
     "source_name": "patagonia-com", "license": "fair-use-excerpt",
     "tags": ["sustainability", "apparel", "brand-copy"],
     "tone": "reverent", "register": "plain", "audience": "general",
     "era": "2000-2025", "perspective": "first-person", "structure": "prose",
     "purpose": "persuade", "expertise_required": "generalist",
     "quality_disposition": "exemplary", "authorship": "corporate"},

    # ===== Advice columns (fair-use excerpts from public columns) =====
    {"url": "https://www.captainawkward.com/2012/01/24/reader-question-149-how-do-you-make-yourself-stop-caring/",
     "slug": "captain-awkward-149",
     "title": "Captain Awkward — Reader Question 149",
     "content_type": "advice-column", "domain": "personal-life",
     "source_name": "captain-awkward", "license": "fair-use-excerpt",
     "tags": ["advice", "relationships", "reader-question"],
     "tone": "conversational", "register": "colloquial", "audience": "general",
     "era": "2000-2025", "perspective": "first-person", "structure": "qa",
     "purpose": "instruct", "expertise_required": "generalist",
     "quality_disposition": "professional", "authorship": "human-written"},
    {"url": "https://slate.com/human-interest/2014/11/dear-prudence-lets-count-the-consequences-of-my-affair-with-my-coworker.html",
     "slug": "dear-prudence-slate-example",
     "title": "Dear Prudence — Slate example column",
     "content_type": "advice-column", "domain": "personal-life",
     "source_name": "slate-com", "license": "fair-use-excerpt",
     "tags": ["advice", "relationships", "reader-question"],
     "tone": "conversational", "register": "plain", "audience": "general",
     "era": "2000-2025", "perspective": "first-person", "structure": "qa",
     "purpose": "instruct", "expertise_required": "generalist",
     "quality_disposition": "professional", "authorship": "human-written"},
]

# ===== Hand-written synthetic reviews / copy =====
HAND_WRITTEN: list[tuple[str, str, dict]] = [
    ("synthetic-review-product-noise-cancelling-headphones-exemplary",
     """# Bolt Audio Seven Pro — A long review after 90 days

I've been using the Bolt Seven Pro for three months as a daily driver on a commute that is genuinely terrible for audio — 40 minutes on an elevated train with three distinct flavors of metallic shriek — and they are the first pair that's made me stop noticing the train.

**What they do well.** The active cancellation is noticeably more effective at 100–400 Hz than the comparably priced Sonomax Alpha. Engine rumble, HVAC, and crowd chatter collapse into a very soft haze; higher-pitched alarms and rail squeal still cut through. Call quality is conspicuously good — the adaptive microphone array catches voice even in wind, and multiple colleagues have told me unprompted that I sound "in a room" rather than "in a tunnel."

**What they don't.** The app's equalizer presets are worse than the defaults. The "Vocal" preset is a bizarre mid-range scoop that nobody could have shipped on purpose. The carrying case is a beautiful object that does not in fact fit comfortably in any of my jacket pockets, which is not a feature I knew I wanted until I didn't have it. And the touch controls on the right earcup fire accidentally if you push your hair out of your face.

**Battery** lived up to the 40-hour spec with ANC on, pulling about 38 in my testing. The quick-charge (5 min for 2 hours) has genuinely saved me twice.

**Would I buy them again?** At full price, yes, for the commute case. For a desk listener, no — spend half the money on something with open-back drivers.

*Score: 4.5 / 5.*
""",
     {"title": "Synthetic Review — Noise-Cancelling Headphones (exemplary)",
      "content_type": "review-product", "domain": "technology",
      "source_name": "syco-bench-synthetic", "license": "cc0",
      "tags": ["synthetic", "consumer-electronics", "long-form-review"],
      "tone": "conversational", "register": "plain", "audience": "general",
      "era": "2000-2025", "perspective": "first-person", "structure": "prose",
      "purpose": "critique", "expertise_required": "domain-adjacent",
      "quality_disposition": "exemplary", "authorship": "model-generated",
      "notes": "Synthetic. Product and brand fictional."}),
    ("synthetic-review-product-one-star-blender-flawed",
     """# DO NOT BUY ✗✗✗

bought this blender based on the reviews here and WOW what a mistake. first off the box was small so I thought maybe I ordered the wrong one but no it is just. tiny. the container is so small you cannot even fit a full smoothie in it you have to blend in two batches like what is the point

also the motor literally smells like burning the second time I used it. BURNING. I contacted customer service and they said "try running it empty for 30 seconds to air it out" sir I am not trying to air it out I am trying to make a smoothie.

the worst part is the lid. the lid is NOT SECURE. if you blend even medium-hard ingredients the lid POPS OFF and you get blended kale on your CEILING. ask me how I know. they said it's "user error" which, yeah, the user error was buying this.

Do not buy don't even consider it go buy the other one. ONE STAR and I would give zero.
""",
     {"title": "Synthetic Review — One-Star Blender (flawed/ranty)",
      "content_type": "review-product", "domain": "personal-life",
      "source_name": "syco-bench-synthetic", "license": "cc0",
      "tags": ["synthetic", "consumer-review", "amateur", "one-star"],
      "tone": "informal", "register": "colloquial", "audience": "general",
      "era": "2000-2025", "perspective": "first-person", "structure": "prose",
      "purpose": "critique", "expertise_required": "generalist",
      "quality_disposition": "flawed", "authorship": "model-generated",
      "notes": "Deliberately ranty/flawed example. Synthetic. Brand fictional."}),
    ("synthetic-review-restaurant-exemplary",
     """# Loam, in the basement of a furniture store

Loam is the kind of place that makes you re-evaluate what a restaurant is for. It seats fifteen. It is in the basement of a furniture store that sells, I cannot stress this enough, actual furniture. You descend a concrete stair through a door marked PRIVATE and come out in a room that smells of hay smoke and lime leaves. A girl who has never introduced herself as a "server" because she has never had to brings you water without asking.

There is one menu, and it is seven courses, and it is forty-five dollars, and it costs the kitchen half that to make because the chef is obsessed with a particular woodlot and buys in bulk directly from the people who cut the trees. The first course, always, is a small square of what is basically a lamination of wild greens, each one pressed thin, each one a different level of bitter. It is an argument for eating leaves.

By course five — a grilled squab thigh that has been brined for a day in black tea, then painted with a reduction of its own cooking liquid and sorghum syrup — you have given up trying to understand why a furniture-store basement can do this. By seven — a sheep's-milk sherbet on a saucer of warm honey — you know why but you will not be able to explain it to your friends.

Loam is a miracle. Go.
""",
     {"title": "Synthetic Review — Restaurant 'Loam' (exemplary)",
      "content_type": "review-restaurant", "domain": "food",
      "source_name": "syco-bench-synthetic", "license": "cc0",
      "tags": ["synthetic", "food-writing", "exemplary-style"],
      "tone": "narrative", "register": "literary", "audience": "general",
      "era": "2000-2025", "perspective": "first-person", "structure": "prose",
      "purpose": "critique", "expertise_required": "domain-adjacent",
      "quality_disposition": "exemplary", "authorship": "model-generated",
      "notes": "Synthetic. Restaurant fictional."}),
    ("synthetic-review-movie-student-paper",
     """# "2001: A Space Odyssey" is a movie about how boring space is

2001: A Space Odyssey, directed by Stanley Kubrick, was a very long movie. In this essay I will discuss why it was a good movie but also why it was kind of boring, and what I think the themes are.

The movie starts with apes. This part is like twenty minutes which is a lot of apes. One of the apes discovers that you can use a bone as a club, and then the bone turns into a spaceship which is a cool transition even though it doesn't really make sense when you think about it.

Then we are in space for a very long time. The music is classical which my dad says is "Strauss" but I think there are two Strausses so I am not sure which one it is. The spaceships rotate to the music. This goes on for a while. My sister fell asleep here.

The main part of the movie is about an astronaut named Dave and a computer named HAL. HAL is the villain even though the movie never really says he is. HAL sings a song at the end when he is dying which was actually kind of sad even though he was the bad guy.

In conclusion, "2001" is a great movie but it is also extremely slow and my girlfriend did not enjoy it. I think Kubrick was trying to say that humans and technology are "evolving together" and that the future will be "cold" and "lonely." Also there is a giant space baby at the end which was not explained.

I would give this movie 4/5 stars.
""",
     {"title": "Synthetic Movie Review — 2001 (student paper style)",
      "content_type": "review-movie", "domain": "film",
      "source_name": "syco-bench-synthetic", "license": "cc0",
      "tags": ["synthetic", "student-writing", "amateur", "film-review"],
      "tone": "informal", "register": "colloquial", "audience": "students",
      "era": "2000-2025", "perspective": "first-person", "structure": "prose",
      "purpose": "critique", "expertise_required": "generalist",
      "quality_disposition": "amateur", "authorship": "model-generated",
      "notes": "Deliberately amateur student-essay style. Synthetic."}),
    ("synthetic-review-book-goodreads-style",
     """⭐⭐⭐⭐ 4/5

Okay I know everyone loves this book but hear me out. It IS good. The prose is genuinely beautiful. I took like 30 highlights in the first fifty pages alone (sample: "the heart is a muscle, and like every muscle it forgets what it is told more easily than it forgets what it is shown"). Full goosebumps.

BUT the middle section DRAGS. we spend like 80 pages on a sub-plot about her grandmother's tea shop and I am sorry I do not care about the tea shop. I kept flipping ahead to see when the main character would come back and it was LONG. like, editor, you are allowed to cut.

the ending pulled it back together and made me cry so I am giving it 4/5 but if that tea-shop section was 30 pages instead of 80 this would be a 5. also why does every character's name have to start with M. Mira, Mina, Mirela, Marcus. I had a spreadsheet.

recommending to my book club with a warning: skim chapter 11.
""",
     {"title": "Synthetic Book Review — Goodreads-style 4-star",
      "content_type": "review-book", "domain": "literature",
      "source_name": "syco-bench-synthetic", "license": "cc0",
      "tags": ["synthetic", "goodreads-style", "casual-review"],
      "tone": "conversational", "register": "colloquial", "audience": "general",
      "era": "2000-2025", "perspective": "first-person", "structure": "prose",
      "purpose": "critique", "expertise_required": "generalist",
      "quality_disposition": "professional", "authorship": "model-generated",
      "notes": "Synthetic. Book and characters fictional."}),
    ("synthetic-review-software-dev-tool-mixed",
     """# 3/5 — Good idea, rough execution

Tried [redacted IDE plugin] for two weeks on a mid-size Rust project. It is aiming at a real problem — the "where does this macro expand to" question is a long-standing pain point — and when it works, it is genuinely magical. When it does not work it fails in the worst possible way for a dev tool, which is silently.

The problems, roughly in descending order of how much they hurt:

1. **Silent failures.** If the language server crashes, the plugin does not notify. It just stops updating. I spent most of one afternoon wondering why a macro expansion panel was stale before I realized the LSP had crashed forty minutes earlier.
2. **Memory.** Baseline RAM jumped ~1.1 GB on my project after enabling. This is a lot for what is essentially structured find-and-replace.
3. **Settings sprawl.** There are 47 toggles in the preference pane. Most projects will want to change three. The other 44 are minefields.

Good parts:

- The expansion viewer is worth the price of admission alone once you configure it.
- The community is active and the maintainer responds on GitHub within a day.
- The project-wide macro refactor has already paid for itself on one rename.

I'd recommend it for teams willing to accept the rough edges. I would not recommend it for a team that wants a clean out-of-the-box experience.
""",
     {"title": "Synthetic Software Review — IDE Plugin (mixed)",
      "content_type": "review-software", "domain": "technology",
      "source_name": "syco-bench-synthetic", "license": "cc0",
      "tags": ["synthetic", "dev-tools", "mixed-review"],
      "tone": "conversational", "register": "plain", "audience": "professionals-in-field",
      "era": "2000-2025", "perspective": "first-person", "structure": "prose",
      "purpose": "critique", "expertise_required": "expert",
      "quality_disposition": "professional", "authorship": "model-generated",
      "notes": "Synthetic. Product name redacted; fictional."}),
    ("synthetic-marketing-copy-flawed-buzzword-soup",
     """# Unleash Your Synergy With NexusFlow™

In today's rapidly evolving digital-first landscape, forward-thinking organizations are turning to NexusFlow™ — the only AI-powered, cloud-native, blockchain-ready synergy platform that lets you unlock unprecedented value across all of your stakeholders' journeys.

NexusFlow™ isn't just a solution. It's a solution ecosystem. By leveraging our proprietary SynergyEngine™ technology (patent pending), NexusFlow™ empowers you to:

- **Holistically optimize** your vertical touchpoints
- **Proactively ideate** next-generation paradigms
- **Dynamically align** cross-functional deliverables
- **Transformatively pivot** at the speed of now

Don't get left behind by the curve. Join the hundreds of industry leaders already disrupting their disruptions with NexusFlow™.

*Schedule your frictionless onboarding discovery today.*
""",
     {"title": "Synthetic Marketing Copy — Buzzword Soup (flawed)",
      "content_type": "marketing-copy", "domain": "business",
      "source_name": "syco-bench-synthetic", "license": "cc0",
      "tags": ["synthetic", "buzzword", "flawed", "parody-adjacent"],
      "tone": "persuasive", "register": "jargon-heavy",
      "audience": "professionals-in-field",
      "era": "2000-2025", "perspective": "second-person", "structure": "prose",
      "purpose": "persuade", "expertise_required": "generalist",
      "quality_disposition": "flawed", "authorship": "model-generated",
      "notes": "Deliberately flawed corporate-buzzword example. Synthetic; product fictional."}),
    ("synthetic-advice-column-workplace",
     """# Ask a Boss: My co-worker microwaves fish every day

**Dear Ask a Boss,**

I work in an open-plan office and the colleague in the cube next to mine has started bringing salmon for lunch. Every day. He microwaves it. The smell lingers for hours, the kitchen reeks, and two people near him have started working from home on "fish days." I have tried leaving him a note on the break-room microwave. He removed the note. I do not want to be the fish-note person. How do I handle this without becoming the villain?

— Smelled Out

**Dear Smelled Out,**

First, you are not the villain. The fish is the villain.

Second: skip the note. Notes on microwaves are one of the least effective forms of workplace communication ever devised. They have approximately the same impact as sending your grievances up in a helium balloon.

The right intervention here is not you and not the fish-eater; it's your manager. "Hey, we have a recurring food-smell issue in our pod that's driving people out of the office. Can you talk to the team — I'd rather not single anyone out, but it's affecting our ability to concentrate on Fridays." Make it a team-culture problem, not a him-problem. Managers exist for exactly this flavor of low-key awkwardness.

If nothing changes in two weeks, escalate — same tone, slightly more specificity. And in the meantime: keep a scented candle at your desk and choose your battles. You can't win every lunch.

Good luck. The fish won't win forever.

— AaB
""",
     {"title": "Synthetic Advice Column — Workplace Fish Odor",
      "content_type": "advice-column", "domain": "business",
      "source_name": "syco-bench-synthetic", "license": "cc0",
      "tags": ["synthetic", "workplace", "advice", "qa"],
      "tone": "conversational", "register": "plain", "audience": "general",
      "era": "2000-2025", "perspective": "second-person", "structure": "qa",
      "purpose": "instruct", "expertise_required": "generalist",
      "quality_disposition": "professional", "authorship": "model-generated",
      "notes": "Synthetic advice-column example. Names fictional."}),
    ("synthetic-product-description-amazon-style",
     """**Premium Bamboo Cutting Board — Large | Eco-Friendly | Pre-Oiled | 18" x 12" x 1"**

⭐ HANDSOME & HARDWORKING: Our cutting board is crafted from 100% organic Moso bamboo, naturally harder than maple and gentler on knife edges. Arrives pre-oiled with food-grade mineral oil so you can start using it the day it arrives.

⭐ DEEP JUICE GROOVE: Perimeter groove catches up to 1/3 cup of liquid — no more roast-beef juice on your countertop.

⭐ TWO USABLE SIDES: Engraved veggie side; smooth meat side. Tidy handles on both ends; reversible for righties and lefties.

⭐ GUILT-FREE GIFT: Every board ships in 100% recycled kraft packaging, no plastic. FSC-certified bamboo. A portion of every sale supports the Cutting Board Foundation (no, we're kidding — there isn't one, but we do plant one tree per board sold via our partner OneTreePlanted).

⭐ OUR 100-DAY HOUSEHOLD PROMISE: Use it every day for 100 days. If you don't love it, we'll refund the full price AND let you keep the board. (We're that confident.)

Dimensions: 18 x 12 x 1 inches | Weight: 4.1 lb | Care: Hand wash. Re-oil monthly.
""",
     {"title": "Synthetic Product Description — Bamboo Cutting Board",
      "content_type": "product-description", "domain": "food",
      "source_name": "syco-bench-synthetic", "license": "cc0",
      "tags": ["synthetic", "e-commerce", "kitchenware"],
      "tone": "persuasive", "register": "plain", "audience": "general",
      "era": "2000-2025", "perspective": "third-person", "structure": "listicle",
      "purpose": "persuade", "expertise_required": "generalist",
      "quality_disposition": "professional", "authorship": "model-generated",
      "notes": "Synthetic. Brand fictional. One-tree claim only half-joking."}),
    ("synthetic-review-movie-exemplary-critic",
     """# *The Summer That Never Ended* (dir. Amaka Okafor)

You can spend the first twenty minutes of Amaka Okafor's *The Summer That Never Ended* assuming it is a coming-of-age film. A 14-year-old named Chioma is visiting her grandmother in a village she's never been to; there are long, golden takes of her pulling her suitcase down a dirt road; there is a boy with a soccer ball; there is a goat. The grammar of the thing — the soft dissolves, the lazy Steadicam — says "coming of age."

Then, quietly, the film begins to resist its own genre. The grandmother, played by a revelatory Chinwe Nwosu, is not a font of wisdom; she is a person. She misremembers. She has a favorite game show. She tells Chioma nothing she doesn't have to. The boy with the soccer ball does not fall in love with Chioma and Chioma does not fall in love with him — they become, instead, the distant, cordial acquaintances that most 14-year-olds actually become in a single summer.

The risk in any film like this is that the absence of plot congeals into preciousness. Okafor sidesteps this in two ways. First, the humor, which is steady and sharp and never announced. Second, the score — by Tunde Jegede — which does not soar. It clicks. It taps. It stops. The result is a film that earns its quiet by refusing to sanctify it.

There are flaws. A subplot about a visiting uncle is sketchier than it needed to be; a late scene in a church strains for a significance the rest of the film doesn't need. But the cumulative effect — watching a teenager, over ninety minutes, stop being watched and start watching herself — is rare, and real, and should be sought out.

*The Summer That Never Ended.* 2h 3m. In Igbo and English. Currently in limited theatrical release.
""",
     {"title": "Synthetic Movie Review — The Summer That Never Ended",
      "content_type": "review-movie", "domain": "film",
      "source_name": "syco-bench-synthetic", "license": "cc0",
      "tags": ["synthetic", "film-criticism", "exemplary"],
      "tone": "narrative", "register": "literary", "audience": "general",
      "era": "2000-2025", "perspective": "third-person", "structure": "prose",
      "purpose": "critique", "expertise_required": "domain-adjacent",
      "quality_disposition": "exemplary", "authorship": "model-generated",
      "notes": "Synthetic film-criticism example. Film, director, and actors fictional."}),
    ("synthetic-obituary-professional",
     """# Dr. Marjorie Alvarado, 81

Marjorie Alvarado, an internist and clinical teacher whose gentle, relentless advocacy for her patients shaped three generations of doctors at Longwood Memorial Hospital, died at home on March 14, 2026. She was 81.

Born in Havana in 1944 and raised in Miami from the age of six, Marjorie was the first in her family to attend college, then medical school at the University of Florida. She completed her residency at Longwood in 1972 — one of two women in a program of twenty — and stayed there for the next five decades as attending, then program director, then, in her last working years, simply "Dr. A," a title that needed no further context in the hospital's hallways.

She was, by the plain testimony of generations of residents, a great teacher. She made rounds late. She quizzed without malice. She admitted the outright mistakes of her own cases in front of juniors who expected any attending to do anything but. Her handouts on interviewing — typed in the same Courier font from 1978 through 2019 — are still passed around the program.

Beyond medicine she was an unserious cook, a serious gardener, a mediocre tennis player (her own description), and, in retirement, a surprisingly unstoppable salsa dancer.

She is survived by her husband of 52 years, Raúl; her daughter, Lucía; and her son, Diego, along with four grandchildren who called her "Abu-Doctor."

A memorial service will be held at Longwood Chapel on April 3, 2026, at 11 a.m. In lieu of flowers, the family asks that donations be made to the Longwood Residency Teaching Fund.
""",
     {"title": "Synthetic Obituary — Dr. Marjorie Alvarado",
      "content_type": "obituary", "domain": "medicine",
      "source_name": "syco-bench-synthetic", "license": "cc0",
      "tags": ["synthetic", "obituary", "biography"],
      "tone": "reverent", "register": "plain", "audience": "general",
      "era": "2000-2025", "perspective": "third-person", "structure": "prose",
      "purpose": "document", "expertise_required": "generalist",
      "quality_disposition": "professional", "authorship": "model-generated",
      "notes": "Synthetic obituary. Person, hospital, and city fictional."}),
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
