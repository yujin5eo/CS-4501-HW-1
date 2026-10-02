# Official course-concept and anti-UX implementation list

## Scope and evidence status

This is the submission-ready source list for the Bumblebee Blooms documentation PDF. It records which course concepts were implemented, where they appear, why they increase interaction cost, and how the task remains completable. Lecture names and PDF page numbers below came from the assignment materials supplied for this project; the lecture PDFs were not available in this repository for independent page-number verification.

There are **19 active implementation candidates**. Some overlap, so they should not be presented as 19 completely independent effects. In particular, items 3, 4, and 6 concern visual organization; items 5 and 18 concern search; and items 10 and 11 concern memory. Even after conservatively merging those groups, the site retains more than ten distinct mechanisms.

Screenshot names are an evidence plan for the final PDF. Replace each planned reference with an actual screenshot from the deployed website. Do not claim that a screenshot exists until it has been captured.

## Active concepts used in the website

### 1. Color discrimination

- **Course source:** *Perception 1*, PDF pp. 14–21.
- **Course idea:** Similar colors, particularly in small areas, are harder to distinguish than clearly separated visual states.
- **Location:** Seasonal Allocations swatches and selected delivery-card state.
- **Implementation:** Small blue, green, and violet swatches are deliberately close in appearance. The selected delivery card changes to another muted blue-green state.
- **Expected effect:** Users may take longer to visually distinguish states or may rely on reading instead of color.
- **Completion safeguard:** Text such as **Selected** always communicates the real state; color is never the only correctness cue.
- **PDF evidence:** `catalog.png` and `delivery.png`.

### 2. Feedback away from the user’s current focus

- **Course source:** *Perception 1*, PDF pp. 34–38.
- **Course idea:** Feedback should appear where the user is looking during an interaction.
- **Location:** Checkout fields versus the sticky **Bee Notices** strip above the navigation.
- **Implementation:** Truthful errors for an invalid promotion, missing field, or wrong selection appear in Bee Notices instead of beside the affected field.
- **Expected effect:** A user focused on checkout may not immediately notice why confirmation failed.
- **Completion safeguard:** The notice is persistent, uses readable contrast, names the real problem, and never clears entered values.
- **PDF evidence:** `invalid-notice.png` showing the field area and remote notice.

### 3. Misleading proximity and common region

- **Course source:** *Perception 2*, PDF pp. 41–49.
- **Course idea:** People infer relationships from proximity and shared visual regions.
- **Location:** Seasonal Allocations catalog.
- **Implementation:** An unrelated farm announcement shares a card with the quantity control, while the related wrap selector is separated lower on the page.
- **Expected effect:** The grouping suggests relationships that do not help the order and weakens the relationship among product, quantity, wrap, and price.
- **Completion safeguard:** Every control still has a truthful visible label.
- **PDF evidence:** `catalog.png`.

### 4. Misleading similarity

- **Course source:** *Perception 2*, PDF pp. 52–53.
- **Course idea:** Visually similar objects are often interpreted as having similar roles.
- **Location:** Right-rail farm announcements and the actionable Seasonal Allocations panel.
- **Implementation:** Decorative notices and the catalog entry use similarly bordered, muted card treatments.
- **Expected effect:** Users must read the cards to determine which one contains an action.
- **Completion safeguard:** Decorative cards do not pretend to be buttons, while the real action has a visible button label.
- **PDF evidence:** `anti-home.png`.

### 5. Weak information scent and conflicting expectations

- **Course source:** *Perception 2*, PDF pp. 18–35; *Attention 1*, PDF pp. 36–41.
- **Course idea:** Navigation labels should predict their destinations and match familiar expectations.
- **Location:** The **Flowers** navigation link and flower-information page.
- **Implementation:** Flowers sounds like the likely catalog destination but opens facts. The flower-facts page does not point users toward the catalog. The actual ordering route is the separately visible **Seasonal Allocations** banner in the right rail.
- **Expected effect:** Users must revise their initial interpretation and search for the indirectly named ordering route.
- **Completion safeguard:** Seasonal Allocations remains visibly labeled in the stable right rail and is keyboard/tap reachable, so the route is difficult but not hidden or broken.
- **PDF evidence:** `facts.png` and `anti-home.png`.

### 6. Banner blindness

- **Course source:** *Attention 2*, PDF pp. 15–16.
- **Course idea:** Users often filter out areas that resemble advertising.
- **Location:** Right rail among farm announcements.
- **Implementation:** The actual **Seasonal Allocations** catalog entry appears inside a bright banner-like panel between promotional-looking notices.
- **Expected effect:** Learned ad avoidance may cause users to overlook the real catalog route.
- **Completion safeguard:** The panel never moves or disappears and remains keyboard/tap accessible.
- **PDF evidence:** `anti-home.png`.

### 7. Peripheral distraction

- **Course source:** *Perception 1*, PDF pp. 29–33; *Attention 1*, PDF pp. 5–13.
- **Course idea:** Irrelevant peripheral motion can capture attention.
- **Location:** Outer edges of the anti-UX shop.
- **Implementation:** Two decorative bees drift gently while users inspect products and services.
- **Expected effect:** Motion may pull attention away from comparison and search tasks.
- **Completion safeguard:** Bees never cover controls, produce sound, flash, or determine correctness. Motion is disabled by `prefers-reduced-motion`.
- **PDF evidence:** `catalog.png` as a frame; optionally document motion with two successive captures.

### 8. Inconsistent familiar structure

- **Course source:** *Attention 2*, PDF pp. 7–14; *Memory 1*, PDF pp. 46–55.
- **Course idea:** Stable spatial conventions let users reuse learned locations.
- **Location:** Navigation on catalog, delivery, and checkout views.
- **Implementation:** The deterministic navigation order reverses on Flight and its spacing changes on Ledger.
- **Expected effect:** A location learned on one view becomes unreliable on the next.
- **Completion safeguard:** Targets do not move in response to the pointer, and every destination continues to work.
- **PDF evidence:** `catalog.png`, `delivery.png`, and `checkout.png`.

### 9. Change blindness

- **Course source:** *Attention 1*, PDF pp. 15–19.
- **Course idea:** Users can miss a change outside the focus of their current action.
- **Location:** Flower-selection button versus the distant header cart count.
- **Implementation:** Choosing Bumblebee flowers silently changes only **Cart items: 0** to **Cart items: 1** in the upper-right header. There is no local animation or success message.
- **Expected effect:** A user focused on the flower card may not notice that selection succeeded.
- **Completion safeguard:** The header count persists, the selected product is stored, and the final review states the selection.
- **PDF evidence:** `cart-before.png` → click **Choose flower** → `cart-after.png`.

### 10. Poor chunking of a long number

- **Course source:** *Perception 2*, PDF p. 77; *Memory 1*, PDF pp. 7–11.
- **Course idea:** Grouping long strings into meaningful chunks improves reading and short-term retention.
- **Location:** Wedding Circular and checkout.
- **Implementation:** Promotion `741906283517` appears as one ungrouped string on a separate page, with no in-app copy button.
- **Expected effect:** Transcription or recall takes more effort and is more error-prone.
- **Completion safeguard:** Ordinary browser selection, copy/paste, screenshots, notes, and backtracking remain available.
- **PDF evidence:** `circular.png` and `checkout.png`.

### 11. Recall rather than recognition

- **Course source:** *Memory 2*, PDF pp. 7–18.
- **Course idea:** Recognizing a visible option is generally easier than recalling information from another context.
- **Location:** Grower Notes and the catalog wrap selector.
- **Implementation:** The selector displays only codes. Users must consult the separate Grower Notes mapping to learn that `WG17` means Ivory Garden Wrap.
- **Expected effect:** Users must remember, copy, or revisit the code.
- **Completion safeguard:** Grower Notes remains accessible, browser back works, and the mapping is truthful.
- **PDF evidence:** `notes.png` and `catalog.png`.

### 12. Working-memory burden during comparison

- **Course source:** *Memory 1*, PDF pp. 19–25.
- **Course idea:** Comparing separated attributes requires users to retain information across views or states.
- **Location:** Flight Ledger.
- **Implementation:** Eighteen services reveal window and price inside individual cards. There is no persistent comparison table or filter in the anti-UX version.
- **Expected effect:** Users must reopen cards or remember multiple time/price pairs.
- **Completion safeguard:** Cards remain stable, can be reopened, and preserve the selected service.
- **PDF evidence:** `delivery.png` with several cards opened.

### 13. Poor signposting and difficult scanning layout

- **Course source:** *Reading and Language*, PDF pp. 8–19.
- **Course idea:** Headings, concise structure, alignment, and clear hierarchy support scanning.
- **Location:** Informational farm pages and ordering descriptions.
- **Implementation:** Several pages use centered prose, repetitive farm updates, limited hierarchy, and visually similar cards.
- **Expected effect:** Users must read more content rather than quickly scanning clear landmarks.
- **Completion safeguard:** The task brief, labels, validation text, final review, and receipt use straightforward language.
- **PDF evidence:** `facts.png` and `catalog.png`.

### 14. Unnecessary calculation

- **Course source:** *Thinking and Problem Solving*, PDF pp. 9–15 and 53–57.
- **Course idea:** Interfaces should externalize necessary calculations rather than forcing users to combine separated values mentally.
- **Location:** Product cards, Wedding Circular, delivery cards, and checkout.
- **Implementation:** The $25 unit price, quantity, 10% discount, and delivery charge are distributed across pages; the anti-UX version has no running total during selection.
- **Expected effect:** Users must estimate whether a service satisfies the $295 limit.
- **Completion safeguard:** Checkout computes the exact integer-cent total before confirmation and allows correction.
- **PDF evidence:** `catalog.png`, `circular.png`, `delivery.png`, and `checkout.png`.

### 15. Poor support for choosing among alternatives

- **Course source:** *Thinking and Problem Solving*, PDF pp. 44–57.
- **Course idea:** Large, unsorted choice sets without comparison or filtering can increase decision effort and may contribute to choice overload.
- **Location:** Flight Ledger.
- **Implementation:** Eighteen plausible services appear in unsorted order. Morning Flight is the fifteenth option. Queen’s Reserve appears much earlier with the correct window but a price that breaks the budget.
- **Expected effect:** Users must inspect many alternatives and compare both window and price.
- **Completion safeguard:** Every option is truthful. Morning Flight is the only service satisfying both the complete window and final-budget constraint.
- **PDF evidence:** `delivery.png`.

### 16. Fitts’ Law

- **Course source:** *Interaction*, PDF pp. 4–20.
- **Course idea:** Target acquisition becomes harder as targets get smaller or farther from the current pointer position.
- **Location:** Flower choice, delivery-detail, selection, and progression controls.
- **Implementation:** Several important desktop controls are stationary targets approximately 26 CSS pixels high, and some are separated from the information they affect.
- **Expected effect:** Selection requires more precise pointer movement than comfortable large controls would.
- **Completion safeguard:** The full visible control is clickable; there are no invisible, one-pixel, fleeing, or pointer-reactive targets.
- **PDF evidence:** `catalog.png` and `delivery.png`.

### 17. Accot–Zhai Steering Law

- **Course source:** *Interaction*, PDF pp. 29–38.
- **Course idea:** Moving through a narrower or longer constrained path requires more steering precision.
- **Location:** **Old Hive Files → Grower Cabinet → Grower Notes**.
- **Implementation:** Grower Notes is inside a shallow two-level hover menu with a narrow but continuous path.
- **Expected effect:** Pointer users must steer carefully to the nested reference.
- **Completion safeguard:** There is no disappearance timer. `:focus-within` and click/tap state provide keyboard and touch recovery.
- **PDF evidence:** `hover-menu.png`.

### 18. Disorganized visual search

- **Course source:** *Interaction*, PDF pp. 22–28 and 34–36.
- **Course idea:** Searching an unstructured menu can require inspection of many items, increasing approximately with the number inspected.
- **Location:** Main farm navigation.
- **Implementation:** About fourteen meaningful links and controls mix ordering references with farm miscellany without alphabetical or semantic order. Flowers is not the first item.
- **Expected effect:** Users must scan multiple labels to find the relevant destination.
- **Completion safeguard:** Items remain visible, stable, and functional. The documentation does not claim a universal menu-size or memory-capacity threshold.
- **PDF evidence:** `anti-home.png`.

### 19. Weak visibility of progress

- **Course source:** *Thinking and Problem Solving*, PDF pp. 9–12.
- **Course idea:** Clear progress feedback helps users understand completed and remaining work.
- **Location:** Anti-UX stages and navigation labels.
- **Implementation:** The journey uses indirect labels such as Seasonal Allocations, Flight Ledger, and Ledger without a numbered progress indicator.
- **Expected effect:** Users may be unsure how much work remains.
- **Completion safeguard:** Navigation is coherent, the task brief can be reopened, checkout provides a review, and completion ends with an explicit receipt.
- **PDF evidence:** `catalog.png`, `checkout.png`, and `anti-receipt.png`.

## Draft ideas that were revised or deliberately not used

These ideas appeared in the initial brainstorm but should **not** be claimed as implemented violations.

### Bee color-vision claims — not used as a scientific design justification

The initial draft discussed bees’ blue/green/ultraviolet receptors and inability to see red. The site uses blue, violet, green, cream, and honey only as fictional art direction. It does not claim to simulate bee vision. Errors remain readable and are not hidden with a biologically themed color.

### Perception influenced by goals — folded into information scent, not counted separately

The goal of ordering Bumblebee flowers motivates the misleading **Flowers** link. This is already documented under weak information scent and conflicting expectations, so it is not counted again as a separate violation.

### Random advertisements — revised

The site does not display real or fake commercial ads. It uses harmless farm announcements with a similar visual treatment and places the real catalog route in a banner-like panel. These behaviors are documented under misleading similarity and banner blindness rather than inflated as extra violations.

### Error message and change blindness — kept separate only where mechanisms differ

Remote validation feedback is item 2: the message appears away from the field where attention is focused. Change blindness is item 9: a successful selection changes an already-visible distant cart count without local feedback. The documentation distinguishes the two observable events rather than counting the same event twice.

### “7 ± 2” and “4 ± 1” memory limits — not claimed

The site does not justify menu size with a universal short-term-memory capacity rule. It documents observable recall, comparison, and visual-search demands instead.

### Hidden or blended logo — not used

The logo remains readable and in a conventional header. Navigation ordering changes across stages, but the project does not claim that hiding the logo is a separate violation.

### Long, complicated vocabulary — removed and not counted

Earlier versions used unnecessarily academic wording. Customer-facing instructions are now straightforward. Difficulty comes from layout, search, memory, comparison, and movement—not from trying to understand obscure vocabulary.

### Excessive payment choices — not used

The order has one truthful option, **Demo invoice**, and collects no financial information. Choice overload is implemented through delivery services because those alternatives are relevant to the task.

### Fast-disappearing hover content — explicitly not used

The initial brainstorm suggested making a hover menu disappear unusually fast. That would undermine reliable completion and conflict with the project requirements. The implemented submenu has no disappearance timer and supports hover, focus, keyboard, and tap/click recovery. Steering difficulty comes from the path geometry, not a timer trick.

### Ambiguous or hidden prices — revised

Prices and windows are always truthful and readable. The difficulty comes from distributing relevant values across product, promotion, and delivery views, then requiring comparison and calculation. The final review clearly displays the exact total before confirmation.

### Red or hard-to-see error text — not used

The Bee Notices strip has readable text and persistent truthful feedback. Its placement is intentionally poor, but contrast is not used to make essential feedback unreadable.

## Conservative count for the final PDF

The documentation may list all 19 active candidates, but the summary should state:

> Bumblebee Blooms implements 19 observable anti-UX candidates. Because several visual-organization, search, and memory concepts overlap, the project conservatively relies on at least **14 distinct mechanisms**, exceeding the rubric minimum of 10.

Do not claim that the five-times slowdown has been achieved until real successful participant observations support it.
