# CLAUDE.md — オープンキャンパス模擬授業 (`jb-open-campus`)

A Quarto book in **Japanese** for high-school students: the material for the
mock lectures (模擬授業) given at Hosei University's open campus, one chapter
per lecture. Author: Ziang Liu (劉子昂), Hosei University.
Published at <https://zi-ang-liu.github.io/jb-open-campus/>.

The `jb-` in the repo name is a leftover from the Jupyter Book (MyST) version
this replaced in September 2026. Nothing here is Jupyter Book any more.

## Read first

Writing conventions are **not** in this file. They are shared with the five
lecture-note books:

    ~/Github/quarto-lecture-notes/CONVENTION.md

Which block to use, callout titling rules, and the `，．` punctuation rule all
live there. Check compliance:

```bash
python3 ~/Github/quarto-lecture-notes/scripts/lint-conventions.py ~/Github
```

Design (colours, fonts, theme) comes from the `lecture` extension in that repo,
installed here at `_extensions/zi-ang-liu/lecture/`. **Never restyle by editing
this book** — edit `_brand.yml` in the hub instead.

## How to work here

- **Edit `.qmd` source only.** Never `_book/`, `_freeze/`, or `*_files/`.
- **Minimal, surgical changes.** Preserve the author's wording and voice.
- **One concern per commit.**
- **Adding a lecture:** copy the shape of `search.qmd` — `## 学習目標` first,
  `## まとめ` last — then add the file to `chapters:` in `_quarto.yml` and a
  line to the list in `index.qmd`.

## Verify before claiming done

```bash
QUARTO_PYTHON=/opt/miniconda3/envs/quarto-book/bin/python quarto render --to lecture-html
```

The system `python3` has no jupyter; renders that execute code fail without
that env var. A local render can reuse a cached compiled stylesheet after a
theme change — `rm -rf .quarto`, then render.

## Facts about this book — decisions, not omissions

- **Audience is high-school students, so there are no theorem-type
  environments.** The MyST original marked its example and algorithm blocks
  `:nonumber:`; a numbered 例 1.1 / Algorithm 1.1 reads as too formal here, the
  same call computer-literacy-book made. Boxes are titled callouts; the quiz
  answer is a `collapse="true"` callout, which is what the original's
  `hide-cell` toggle did.
- **Code is hidden.** `execute: echo: false` in `_quarto.yml`: the figures are
  drawn by Python the students never see. Code that *is* the content (the `bfs`
  function) is a plain ```` ```python ```` block — never executed, always shown.
- **Figures register the bundled font.** The first cell of `search.qmd` adds
  `fonts/NotoSansJP-Regular.ttf` to matplotlib, so Japanese labels render the
  same on macOS and on CI's Ubuntu without installing a font. The original
  asked for `Noto Sans CJK JP`, which exists on neither.
- **The blockquote in `## 経営システム工学って何？` keeps `、。`.** It is
  verbatim from the department website (CONVENTION §5, quotations); the linter
  skips blockquotes for that reason.
- **HTML only, because the remote images are hot-linked** as in the original
  (Wikimedia, Elsevier). Fine for HTML — the browser fetches them — but a PDF
  needs pandoc to download them at render time, and Wikimedia rate-limits that
  (HTTP 429), so `_quarto.yml` declares no `lecture-pdf`. To add one, copy the
  images into `images/` first; the licences (CC0, CC BY-SA, CC BY-NC-ND) allow
  it and the captions already credit the authors.
- Python at render time: matplotlib, networkx (`requirements.txt`, same pins as
  or-book). `_freeze/` is committed, so CI executes nothing unless a chapter's
  source changed since its freeze.
- CI is the hub's reusable workflow (`.github/workflows/publish.yml`), which
  publishes to the `gh-pages` branch. The repo's Pages source must be that
  branch, not "GitHub Actions" — the MyST setup used the latter.
