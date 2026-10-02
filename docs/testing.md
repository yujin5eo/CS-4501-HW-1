# Timing and verification

## Provisional estimate — not a measured result

The provisional normal baseline is **60 seconds**, to validate or replace through human observation: read brief 10 s; choose product/quantity/wrap 10 s; scan/filter the side-by-side delivery table 12 s; copy promotion and verify details 13 s; review and confirm 10 s; receipt check 5 s. This is reasonable for the compact, prefilled, clearly labelled baseline, but it is an estimate—not fabricated participant data. With 60 seconds, the initial five-times target is **at least 300 seconds** for mean successful anti-UX completion.

Automated browser speed does not establish human slowdown. The five-times requirement is **pending human testing**.

## Human study method

1. Recruit friends, family, or out-of-class peers without collecting names or other personal data. Use a fresh browser profile/storage reset for each clean trial.
2. Use the same displayed task, timing boundaries, device, viewport, input method, and assistance policy. Timing starts when the task brief first appears after the participant starts a trial and stops only at the correct receipt. The apps implement these boundaries consistently.
3. Open a **participant test** link from `review.html` for each real volunteer run. The normal shop and baseline links automatically record practice runs. This keeps study data separate without showing a technical selector to customers. Record device conditions, prior exposure, version order, and assistance separately in the table below.
4. Prefer fresh participants. If each participant uses both versions, counterbalance version order. Discuss learning effects because wrap, promotion, and service knowledge may transfer to the second run.
5. Export JSON or CSV from `review.html`. Records contain anonymous random run ID, mode, elapsed seconds, success/abandonment, error attempts, and classification; they remain local.
6. Report failures and abandonments separately. Never transform them into completion times.

| Anonymous run ID | Mode | Successful seconds | Failed/abandoned | Errors | Device/viewport | Prior exposure | Order | Assistance/notes |
|---|---|---:|---|---:|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |

For successful anti-UX trials:

`slowdown ratio = mean successful anti-UX completion seconds ÷ justified baseline seconds`

Report both that ratio and the measured normal-version successful average when available. If the ratio is below 5, strengthen documented cognitive/interaction problems and retest—do not add waiting, break controls, arbitrarily lower the baseline, or substitute violation count for measured slowdown.

## Programmatic verification status

`node tests/core-check.mjs` checks shared data cardinality, the exact correct order, integer-cent arithmetic and `$294.00` receipt, invalid promotion, missing field, wrong delivery, correction without loss, and non-stacking discount. `tests/static-check.py` checks local references, relative paths, required entry points, navigation target/view coverage, and responsive CSS markers.

Full browser automation was unavailable: no browser/runtime was installed, and the environment proxy returned HTTP 403 when Playwright/Chromium installation was attempted. Consequently, interactive browser checks (ordinary clipboard behavior, browser back, pointer corridor, keyboard/tap operation, console errors, rendered desktop/narrow clipping, and actual screenshots) are honestly **pending** rather than invented. `tests/capture.py` is provided for a machine with Selenium and Chromium; it captures the planned evidence from the real pages. Manual human timing remains outstanding. Subjective confirmation that the anti-UX experience is sufficiently difficult, and final inspection on the instructor's device/browser, also remain manual. Lecture PDFs were unavailable in the repository; all lecture/page references in `violations.md` are supplied assignment references, not independently verified.
