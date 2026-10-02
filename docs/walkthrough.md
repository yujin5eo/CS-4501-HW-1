# Tested completion walkthrough

## Anti-UX (`index.html`)

1. Read the task brief and press **Start task**. Normal links record a practice run. Participant-test links are available only on `review.html`. Timing starts when Start task is pressed after the brief has been displayed.
2. Use the right-rail banner **Seasonal Allocations → Enter allocations**. (**Flowers** intentionally opens facts, whose text points to Seasonal Allocations.)
3. On **Bumblebee flowers**, press **Choose flower**. The remote header becomes `Ledger marks: 1`; there is deliberately no local confirmation.
4. Set quantity to `12`.
5. Open **Old Hive Files → Grower Cabinet → Grower Notes** (hover, focus, or tap/click works). The mapping is `WG17 — Ivory Garden Wrap`. Return through **Harvest Talk** or the Seasonal Allocations banner and choose `WG17`.
6. Proceed to Flight. Open delivery cards until finding **Morning Flight**, window `09:00–11:00`, charge `$24.00`; select it. Other options fail the time constraint or (Queen's Reserve) the $295 budget.
7. Open **Wedding Circular**, select/copy or note `741906283517`, then open **Ledger**.
8. Enter promotion `741906283517`, date `2026-10-24`, recipient `Turnipseed Wedding`, venue `Meadow Hall`, email `planner@example.com`, and payment `Demo invoice`.
9. Review `$300.00 − $30.00 + $24.00 = $294.00`; press **Confirm order**.
10. Verify the explicit receipt includes an order ID, Bumblebee flowers, 12 bouquets, Ivory Garden Wrap (WG17), October 24, 2026, Morning Flight 09:00–11:00, recipient, venue, email, promotion/discount, Demo invoice, and `$294.00`. Timing stops only now.

If validation fails, all valid input remains stored. Read the persistent **Bee Notices** strip at the page top, correct the named issue, and reconfirm. The task card can be reopened without resetting.

## Baseline (`baseline.html`)

Open the normal baseline link for a practice run, then start the task; the form already presents the same task and data clearly. Choose Bumblebee flowers, 12, Ivory Garden Wrap; select Morning Flight from the 18-row comparison; use **Copy promotion**; keep the supplied delivery fields; review the running total; confirm. Validation and receipt requirements are shared with the anti-UX version.

## Arithmetic

Integer cents are used: `12 × 2500 = 30000`; promotion `30000 × 10 / 100 = 3000`; delivery `2400`; final `30000 − 3000 + 2400 = 29400` cents. The discount is derived once from the current valid code, so repeated review/confirmation cannot stack it.
