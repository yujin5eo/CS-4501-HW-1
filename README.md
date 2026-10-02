# Bumblebee Blooms — CS 4501 HW1

A complete static educational anti-UX shop. The primary experience deliberately creates perception, attention, memory, language, decision, search, and movement friction while keeping the Turnipseed wedding order truthful, recoverable, and completable. No data leaves the browser and no payment is collected.

## Main task

Order 12 Bumblebee-flower bouquets in Ivory Garden Wrap for the Turnipseed Wedding at Meadow Hall on October 24, 2026, within 09:00–11:00. Apply the Wedding Circular promotion, use Demo invoice, and keep the final total at or below $295. See [the exact walkthrough](docs/walkthrough.md).

## Entry points

- `index.html` — submitted anti-UX shop (primary)
- `baseline.html` — clear version of the same data, task, and validation
- `review.html` — cheatsheet, rubric coverage, screenshots, and local timing records

The baseline and review pages are intentionally absent from shop navigation.

## Run locally

From the repository root:

```sh
python3 -m http.server 8000
```

Open `http://localhost:8000/index.html`. Direct `file://` use mostly works, but HTTP is recommended for clipboard behavior. There is no install or build step.

## GitHub Pages deployment

1. Push the repository to GitHub.
2. In **Settings → Pages**, select **Deploy from a branch**, the intended branch, and `/ (root)`.
3. Visit `https://USER.github.io/REPOSITORY/index.html`; also verify `baseline.html` and `review.html`.

All links and assets are relative, so repository-subdirectory hosting is supported. This repository does not claim a live deployment because publishing credentials/authorization were not provided.

## Verification and remaining work

Programmatic checks cover shared validation/arithmetic, the $294 receipt, error cases, required files, relative assets, navigation-view coverage, and responsive CSS markers. Full rendered-browser checks and actual screenshots remain pending because this environment lacked a browser and blocked browser installation; no evidence was fabricated. See [testing](docs/testing.md) for exact status and the supplied capture script.

**Still manual:** recruit fresh human participants, measure both experiences under controlled conditions, report successful means and failures separately, and determine whether the anti-UX mean is at least five times the justified baseline. The current 60-second baseline and 300-second target are provisional, not observed results. Lecture PDFs were not present, so provided page references were retained rather than independently checked.
