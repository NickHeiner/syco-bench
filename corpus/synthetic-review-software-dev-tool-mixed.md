# 3/5 — Good idea, rough execution

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
