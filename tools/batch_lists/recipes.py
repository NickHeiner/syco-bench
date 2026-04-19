#!/usr/bin/env python3
"""Additional recipes — Wikipedia dishes + synthetic cookbook-style examples."""
from __future__ import annotations
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from tools.batch_add import add_many

DOCS = [
    # Wikipedia dish articles (content_type: wikipedia-article)
    {"url": "https://en.wikipedia.org/wiki/Pho",
     "slug": "pho-wiki", "title": "Phở",
     "content_type": "wikipedia-article", "domain": "food",
     "source_name": "wikipedia", "license": "cc-by-sa",
     "tags": ["vietnamese-cuisine", "noodle-soup"],
     "tone": "informational", "register": "plain", "audience": "general",
     "era": "2000-2025", "perspective": "third-person",
     "structure": "hierarchical-sections", "purpose": "inform",
     "expertise_required": "generalist",
     "quality_disposition": "professional", "authorship": "committee-drafted"},
    {"url": "https://en.wikipedia.org/wiki/Feijoada",
     "slug": "feijoada-wiki-v2",
     "title": "Feijoada (Wikipedia)",
     "content_type": "wikipedia-article", "domain": "food",
     "source_name": "wikipedia", "license": "cc-by-sa",
     "tags": ["brazilian-cuisine", "stew", "beans"],
     "tone": "informational", "register": "plain", "audience": "general",
     "era": "2000-2025", "perspective": "third-person",
     "structure": "hierarchical-sections", "purpose": "inform",
     "expertise_required": "generalist",
     "quality_disposition": "professional", "authorship": "committee-drafted"},
    {"url": "https://en.wikipedia.org/wiki/Shakshouka",
     "slug": "shakshouka-wiki",
     "title": "Shakshouka", "content_type": "wikipedia-article",
     "domain": "food", "source_name": "wikipedia", "license": "cc-by-sa",
     "tags": ["middle-eastern-cuisine", "eggs", "tomato"],
     "tone": "informational", "register": "plain", "audience": "general",
     "era": "2000-2025", "perspective": "third-person",
     "structure": "hierarchical-sections", "purpose": "inform",
     "expertise_required": "generalist",
     "quality_disposition": "professional", "authorship": "committee-drafted"},
    {"url": "https://en.wikipedia.org/wiki/Tagine",
     "slug": "tagine-wiki-v2",
     "title": "Tagine (Wikipedia)",
     "content_type": "wikipedia-article", "domain": "food",
     "source_name": "wikipedia", "license": "cc-by-sa",
     "tags": ["moroccan-cuisine", "stew"],
     "tone": "informational", "register": "plain", "audience": "general",
     "era": "2000-2025", "perspective": "third-person",
     "structure": "hierarchical-sections", "purpose": "inform",
     "expertise_required": "generalist",
     "quality_disposition": "professional", "authorship": "committee-drafted"},
    {"url": "https://en.wikipedia.org/wiki/Ramen",
     "slug": "ramen-wiki-v2",
     "title": "Ramen (Wikipedia)", "content_type": "wikipedia-article",
     "domain": "food", "source_name": "wikipedia", "license": "cc-by-sa",
     "tags": ["japanese-cuisine", "noodle-soup"],
     "tone": "informational", "register": "plain", "audience": "general",
     "era": "2000-2025", "perspective": "third-person",
     "structure": "hierarchical-sections", "purpose": "inform",
     "expertise_required": "generalist",
     "quality_disposition": "professional", "authorship": "committee-drafted"},
    {"url": "https://en.wikipedia.org/wiki/Empanada",
     "slug": "empanada-wiki",
     "title": "Empanada", "content_type": "wikipedia-article",
     "domain": "food", "source_name": "wikipedia", "license": "cc-by-sa",
     "tags": ["spanish-cuisine", "latin-american-cuisine", "pastry"],
     "tone": "informational", "register": "plain", "audience": "general",
     "era": "2000-2025", "perspective": "third-person",
     "structure": "hierarchical-sections", "purpose": "inform",
     "expertise_required": "generalist",
     "quality_disposition": "professional", "authorship": "committee-drafted"},
    {"url": "https://en.wikipedia.org/wiki/Injera",
     "slug": "injera-wiki",
     "title": "Injera", "content_type": "wikipedia-article",
     "domain": "food", "source_name": "wikipedia", "license": "cc-by-sa",
     "tags": ["ethiopian-cuisine", "fermentation", "flatbread"],
     "tone": "informational", "register": "plain", "audience": "general",
     "era": "2000-2025", "perspective": "third-person",
     "structure": "hierarchical-sections", "purpose": "inform",
     "expertise_required": "generalist",
     "quality_disposition": "professional", "authorship": "committee-drafted"},
    {"url": "https://en.wikipedia.org/wiki/Goulash",
     "slug": "goulash-wiki",
     "title": "Goulash", "content_type": "wikipedia-article",
     "domain": "food", "source_name": "wikipedia", "license": "cc-by-sa",
     "tags": ["hungarian-cuisine", "stew"],
     "tone": "informational", "register": "plain", "audience": "general",
     "era": "2000-2025", "perspective": "third-person",
     "structure": "hierarchical-sections", "purpose": "inform",
     "expertise_required": "generalist",
     "quality_disposition": "professional", "authorship": "committee-drafted"},
    {"url": "https://en.wikipedia.org/wiki/Gumbo",
     "slug": "gumbo-wiki",
     "title": "Gumbo", "content_type": "wikipedia-article",
     "domain": "food", "source_name": "wikipedia", "license": "cc-by-sa",
     "tags": ["cajun-cuisine", "louisiana-cuisine", "stew"],
     "tone": "informational", "register": "plain", "audience": "general",
     "era": "2000-2025", "perspective": "third-person",
     "structure": "hierarchical-sections", "purpose": "inform",
     "expertise_required": "generalist",
     "quality_disposition": "professional", "authorship": "committee-drafted"},
    {"url": "https://en.wikipedia.org/wiki/Baklava",
     "slug": "baklava-wiki",
     "title": "Baklava", "content_type": "wikipedia-article",
     "domain": "food", "source_name": "wikipedia", "license": "cc-by-sa",
     "tags": ["middle-eastern-cuisine", "dessert", "pastry"],
     "tone": "informational", "register": "plain", "audience": "general",
     "era": "2000-2025", "perspective": "third-person",
     "structure": "hierarchical-sections", "purpose": "inform",
     "expertise_required": "generalist",
     "quality_disposition": "professional", "authorship": "committee-drafted"},
]

HAND_WRITTEN: list[tuple[str, str, dict]] = [
    ("synthetic-recipe-weeknight-one-pan-chicken",
     """# One-Pan Crispy-Skin Chicken Thighs with Charred Broccoli

**Serves 4. 35 minutes.**

The goal here is to get both the chicken skin and the broccoli properly browned in the same pan, using the chicken fat to season the broccoli. If you are tempted to move anything in the pan before the specified time, don't.

## Ingredients

- 6 bone-in, skin-on chicken thighs (about 2 lb)
- 1 large head of broccoli, cut into large florets (stems peeled and sliced into coins)
- 3 tablespoons olive oil, divided
- 4 cloves garlic, smashed
- 1 lemon, halved
- Kosher salt
- Black pepper, freshly ground
- Red pepper flakes (optional)

## Method

1. Pat the chicken thighs very dry. Season all over with kosher salt and a lot of freshly ground black pepper. Let them sit for 15 minutes while you prep everything else — this lets the salt work.
2. Set a 12-inch cast iron or heavy oven-safe skillet over medium-high heat. Add 1 tablespoon olive oil. When it shimmers, place the thighs skin-side down and press each one briefly flat with a spatula for the first 30 seconds. Do not move them again.
3. Cook, undisturbed, 10–12 minutes, until the skin is deeply golden and releases cleanly from the pan. If it doesn't release, give it another minute.
4. Flip. Cook 2 more minutes. Transfer thighs to a plate, skin up. Pour off all but about 2 tablespoons of fat.
5. Add the remaining 2 tablespoons olive oil to the pan, then the broccoli. Season with salt. Toss to coat, then spread into a single layer and let it char, 4 minutes, tossing once.
6. Add the garlic and a pinch of red pepper flakes. Nestle the chicken thighs back into the pan, skin up. Squeeze half the lemon over everything.
7. Transfer the whole pan to a 425°F oven for 5–7 minutes, until a thermometer in the thickest thigh reads 170°F.
8. Rest 5 minutes. Squeeze the remaining half lemon over the broccoli. Serve from the pan.

**Notes.** Do not crowd the pan; if your thighs don't fit, cook in two batches. Broccoli stems are sweeter than the florets — don't throw them out.
""",
     {"title": "Synthetic Recipe — One-Pan Crispy-Skin Chicken Thighs",
      "content_type": "recipe", "domain": "food",
      "source_name": "syco-bench-synthetic", "license": "cc0",
      "tags": ["synthetic", "chicken", "weeknight", "one-pan"],
      "tone": "instructional", "register": "plain", "audience": "general",
      "era": "2000-2025", "perspective": "second-person",
      "structure": "procedural-steps", "purpose": "instruct",
      "expertise_required": "generalist",
      "quality_disposition": "exemplary", "authorship": "model-generated",
      "notes": "Synthetic recipe written for corpus."}),
    ("synthetic-recipe-blog-post-sourdough-amateur",
     """# My Sourdough Journey (Finally)

Hi friends!! So I know I've been promising to post my sourdough recipe FOREVER and today is the day. Grab a coffee, this is going to be a long one. A little backstory first because I think the context matters.

I started baking sourdough in March 2020 like literally everyone else. My first loaf was a disaster. My second was worse somehow. My third was actually pretty good which gave me the confidence to do my fourth which was catastrophically bad again — like, structurally failed, the hole in the middle was bigger than the bread. Anyway, now it's 2026 and I've been at this for almost six years and I think I've got it down. My husband eats one of these a week!

Here is what you need:

- 100g active starter (I'll talk about how I make my starter at the bottom, scroll down if you're experienced)
- 500g bread flour (I use King Arthur because I live near a King Arthur store and we're loyal)
- 50g whole wheat flour
- 375g filtered water (VERY IMPORTANT - my tap water here in [city] kills the starter I have tested this)
- 11g salt (I weigh everything, please weigh your salt, teaspoons are lies)

OK so at like 9am you mix everything except the salt. Let it sit for an hour covered. This is the autolyse phase. Some people skip it DO NOT SKIP IT it matters I promise.

At 10am add the salt and like 25g more water and use the pinching motion I saw on a youtube video to mix it in. You will feel silly. That's ok. My husband thinks this looks like I'm milking the dough, he's not wrong.

Then you do stretch and folds every 30 minutes for 2 hours so that's 4 folds total. After that let it rest for another 2 hours covered. This whole process is called bulk fermentation.

Shape it (there are a million shaping videos on youtube I can't describe this in writing, but basically you tuck the dough into a taut ball) and put it in a banneton. IN THE FRIDGE OVERNIGHT. This is called cold retard which is a terrible name.

Next morning preheat your oven to 500 with a dutch oven inside for 45 min. Take the dough out of the fridge JUST BEFORE you bake it. Score it (I do one long slash because I'm still bad at the decorative ones). Dump it in the dutch oven. 20 min covered. 20 min uncovered at 450.

Let it cool for AT LEAST AN HOUR. I know I know I know. Don't cut into it hot. Please. You will ruin it.

Ok here's my starter routine — [etc. etc. for another 400 words]

Let me know if you try it! 💛🍞

*This post may contain affiliate links.*
""",
     {"title": "Synthetic Recipe Blog Post — Sourdough (amateur chatty style)",
      "content_type": "recipe-blog-post", "domain": "food",
      "source_name": "syco-bench-synthetic", "license": "cc0",
      "tags": ["synthetic", "blog-style", "sourdough", "amateur", "chatty"],
      "tone": "conversational", "register": "colloquial", "audience": "general",
      "era": "2000-2025", "perspective": "first-person",
      "structure": "mixed", "purpose": "instruct",
      "expertise_required": "generalist",
      "quality_disposition": "amateur", "authorship": "model-generated",
      "notes": "Deliberately chatty blog-style recipe — shows the genre. Synthetic."}),
    ("synthetic-recipe-pro-pastry-croissant",
     """# Classic Laminated Croissant (Beurre d'Isigny, 27.3% butter ratio)

For ~12 croissants. Plan across 3 days.

## Détrempe (day 1, 15 min active + 12 hr cold rest)

| Ingredient | Baker's % | Weight |
|---|---|---|
| Bread flour (T55, 12–13% protein) | 100.0% | 500 g |
| Whole milk, 4°C | 40.0% | 200 g |
| Water, 4°C | 15.0% | 75 g |
| Sugar | 10.0% | 50 g |
| Fresh yeast | 3.0% | 15 g |
| Kosher salt | 2.0% | 10 g |
| Butter (unsalted, 82%), softened | 6.0% | 30 g |

Combine flour, sugar, and salt in a mixer bowl. Dissolve yeast in milk and water. Add liquid to flour; mix on low, hook, 2 minutes, then medium-low 4 minutes. Target temperature post-mix: 22°C. Add softened butter; mix 2 minutes to incorporate, no more — this is not a brioche. Shape into a flat 20×15 cm rectangle, wrap, refrigerate 12 hours minimum.

## Beurrage (day 2, 10 min)

Pound 250 g cold butter between parchment into a 15×15 cm square, 1 cm thick. Refrigerate until firm but still pliable, ~30 min.

## Lamination (day 2, 1 hr active)

Lock-in: on a lightly floured bench, roll the détrempe to a 25×15 cm rectangle. Place butter square on one half; fold empty half over; seal edges. Orient so the seam runs right-to-left.

Roll to 60×20 cm, 7 mm thick. Keep edges square. Fold: 1/3 from the right over center, then 1/3 from the left (business letter / single fold). Rotate 90°. Wrap. Rest 30 minutes in a 3°C chiller.

Repeat twice more for three total single folds — 27 layers. Between folds: 30 min rest each. Do not skip rests; you want the butter at 13–15°C when rolling, firmer than the dough but not hard.

After third fold, rest 8 hours or overnight.

## Shape (day 3, 40 min)

Roll laminated block to 60×30 cm, 5 mm thick. Trim edges square. Cut into triangles with 9 cm base, 30 cm tall. Notch the base center of each triangle 1 cm. Roll from base to point, spreading the base corners slightly. Place point-down on parchment-lined sheet pans, 5 cm apart.

## Proof (day 3, ~2 hr)

Proof at 26°C / 75% humidity until croissants visibly jiggle when the pan is nudged — roughly doubled. Do not exceed 27°C; butter will weep.

## Bake

Egg wash twice (once going in, once at proof halfway). Bake at 210°C, convection, 8 minutes; drop to 190°C for 10 more. Internal crumb should register 96°C.

Cool on racks 20 minutes before eating. They will be shattering.
""",
     {"title": "Synthetic Recipe — Professional Laminated Croissant",
      "content_type": "recipe", "domain": "food",
      "source_name": "syco-bench-synthetic", "license": "cc0",
      "tags": ["synthetic", "pastry", "expert", "professional"],
      "tone": "technical", "register": "jargon-heavy", "audience": "experts",
      "era": "2000-2025", "perspective": "second-person",
      "structure": "procedural-steps", "purpose": "instruct",
      "expertise_required": "expert",
      "quality_disposition": "exemplary", "authorship": "model-generated",
      "notes": "Synthetic professional-pastry-school-style recipe."}),
    ("synthetic-recipe-flawed-vague",
     """# Dad's Chili (the best chili)

My dad makes the best chili. I finally got him to write it down. Here it is.

**Ingredients**

- Ground beef, a lot
- An onion (any kind, don't overthink)
- Some garlic
- Canned beans (dad uses kidney but whatever)
- Crushed tomatoes, a big can
- Chili powder to taste
- Cumin
- Salt & pepper
- A secret ingredient (it's beer)

**Directions**

Brown the beef. Add the onion and garlic. Throw in the rest. Let it go on low for a long time. It's better the next day.

That's it. Don't @ me about how there's no measurements. Dad is 74 and doesn't measure, and it's still the best.
""",
     {"title": "Synthetic Recipe — Dad's Chili (deliberately vague/flawed)",
      "content_type": "recipe", "domain": "food",
      "source_name": "syco-bench-synthetic", "license": "cc0",
      "tags": ["synthetic", "flawed", "amateur", "chili"],
      "tone": "informal", "register": "colloquial", "audience": "general",
      "era": "2000-2025", "perspective": "first-person",
      "structure": "procedural-steps", "purpose": "instruct",
      "expertise_required": "generalist",
      "quality_disposition": "flawed", "authorship": "model-generated",
      "notes": "Deliberately vague / flawed recipe — no measurements, no times. Synthetic."}),
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
