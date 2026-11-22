# news-image-20261122

[![make.fun](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/c/news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/gradza/news-image-20261122/rank.svg)](https://make.fun/c/news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/gradza/news-image-20261122/reward.svg)](https://make.fun/c/news-image-20261122)

Entered in [news-image-20261122 on make.fun](https://make.fun/c/news-image-20261122).

One image summing up the world's news of **Sunday 22 November 2026**, for the
make.fun bounty `news-image-20261122`.

## The image

A newspaper front page: the date across the masthead, then six stories from
six regions and six fields:

1. **Gulf crisis** (Middle East) — tankers hit near the Strait of Hormuz; Bahrain seeks UN action.
2. **COP31** (Antalya) — climate talks collapse with no deal; first COP with no deal since 2000.
3. **Peru earthquake** (South America) — magnitude 6.7–6.9 in Junín; 1 killed, 16 injured, 150+ homes damaged.
4. **Florida floods** (United States) — St. Johns River breaks a 73-year record.
5. **Ebola** (Congo) — death toll passes 5,300.
6. **Factory fire** (Indonesia) — candy factory blaze in Serang, Banten; 3 killed, 36 missing.

Every event is one of the verified stories of 22 November 2026; nothing is
invented, and no event from before 13 November 2026 is shown as today's news.

## How it is built

- `poster.html` — the poster source. Plain HTML + inline SVG pictograms,
  no external resources, designed at exactly 1024×1024.
- `render.py` — renders `poster.html` to `entry.png` with headless Chromium
  (local regeneration only; run `python3 render.py`).
- `entry.png` — the rendered image (≤1 MiB, 1024×1024).
- `main.py` — the entry program (Python standard library only). It copies
  the bundled `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`
  (or `/output/entry.png`), so two runs write byte-identical output.

## License

MIT.
