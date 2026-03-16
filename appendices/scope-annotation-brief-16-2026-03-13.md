# Scope Annotation — Frankfurt/Scanlon Classification Audit
## 16th Adversarial Brief, 2026-03-13

*Produced by: Bishop (classification audit), Rook (integration and architecture note)*
*Scope: Companion Document Chapters 4 and 5*
*Method: Three-category audit against Ch4 reference schema (stable type system for cross-chapter comparability)*

---

## Methodology

Three-category schema (locked from Ch4 audit, used for Ch5 comparability):

| Type | Description | Mechanism |
|------|-------------|-----------|
| **Type 1** | Explicit Frankfurt attribution — names Frankfurt by name | Second-order identification vocabulary with explicit authorial attribution |
| **Type 2** | Implicit Frankfurt mechanism — uses Frankfurt's vocabulary without naming him | "Genuine engagement," "endorsement," "second-order endorsement," "identification" without attribution |
| **Type 3** | Bare Scanlon quality-of-will | Blame/blameworthiness tracking based on what an agent's action reveals about the quality of their will — no Frankfurt overlay |
| **Anomalous** | Second-order language that is neither Frankfurt-volitional nor Scanlon-blameworthiness | Epistemic/normative "second-order" references (beliefs, intentions, access) rather than volitional identification |

Five-axis secondary marker protocol (adopted 2026-03-14, post-production review session):

| Marker | Description |
|--------|-------------|
| **[F]** | Foundational / load-bearing — the site does structural work for the argument |
| **[R]** | Rhetorical / illustrative — applies or illustrates without being load-bearing |
| **[→n]** | Forward-covering — this site's evidential weight extends to line n downstream |
| **[←n]** | Invisible-dependency — this site requires reconstruction from established mechanism at line n |
| **[?type]** | Interpretive ambiguity / reading fork — two readings with different structural implications; use specific form when known (e.g., [?inward/outward] for Frankfurt/Scanlon register fork) |
| **[?role]** | Role ambiguity — function of the site is unclear (load-bearing vs. illustrative), resolvable independently of type |
| **[?role-cond]** | Conditional role dependency — role cannot be determined without first resolving the type fork; type resolution is prerequisite to role assignment. Use when [?type] and [?role] would be independently motivated but the role assignment is actually downstream of the type reading. |

Markers are appended to Type designations in site tables (e.g., "Type 2 [F]", "Anomalous [?inward/outward]").

**D1/D2 sub-classification for Anomalous sites (formalized 2026-03-16):**

When a site initially classified as Anomalous (Type D) is reviewed, two sub-types apply:

- **D1 (rhetorical use of adjacent vocabulary):** The site uses Frankfurt or Scanlonian vocabulary to describe a phenomenon that is actually within the existing taxonomy. Vocabulary is imprecise but the phenomenon is classifiable. Classification: reassign to the underlying type (Type B or Type C) with appropriate role marker ([R] if illustrative, [F] if load-bearing). No open boundary.
- **D2 (genuine taxonomy gap):** The site tracks a phenomenon the A/B/C/D taxonomy was not built to classify — not a vocabulary misuse but a structural absence. Classification: **retain Anomalous** with open-boundary notation. Name the unclassifiable structure; do not force classification. (Note: D2 sites remain "Anomalous" / Type D — do not reclassify as Type C; Type C in this taxonomy means Bare Scanlon quality-of-will, not generic unclassifiable.)

**Diagnostic test for D1 vs D2:** Is Frankfurt's reflexivity structure present (self-targeting: the agent's second-order state is about their own first-order state — "I want to want X" form)? If yes and used loosely → D1 (reassign to underlying type). If the reflexive structure required for Frankfurt (or Scanlon's quality-of-will directionality) is structurally absent → D2 candidate; verify no other type fits before confirming open boundary.

**Canonical D2 instance — Ch4 line 159:** "Second-order beliefs and intentions about prior commitments" — Frankfurt reflexivity structurally absent (points outward at prior commitment chain, not inward at agent's own first-order states). Phenomenon = Parfitian-Scanlonian uptake of inherited commitment chain; neither framework names this structure. Open boundary confirmed. (See Finding B.)

**Audit map implication:** D1/D2 does not require a new table column. The distinction operates at the review layer: D1 sites get reclassified and exit the Anomalous row; D2 sites stay in the Anomalous row with open-boundary notation in the mechanism description. Action-item framing: D1 → fix annotation to underlying type; D2 → flag open boundary in companion text annotation.

**C7 two-statement rule (three-case extension):**
The standard C7 annotation gives Type first (mechanism), then role (function). Three cases govern:
- *Case 1 (fully determinate):* Type and role both clear. Standard two-statement form: "Type X [F/R]" — one combined annotation.
- *Case 2 (type ambiguous, role independent):* Apply [?type] and state role independently. Role can be determined without resolving the type fork. Both statements appear in the annotation.
- *Case 3 (type ambiguous, role conditionally dependent):* Apply [?role-cond] alongside [?type]. Role cannot be stated until type is resolved — under reading A the site is load-bearing ([F]), under reading B it is illustrative ([R]). The annotation names the fork and defers role assignment: "Type 2 [?type] [?role-cond]: under reading X, [F]; under reading Y, [R]." Do not collapse to [?role] when the role ambiguity is downstream of the type fork.

---

## Chapter 4: The Social Contract Question

**Site inventory (Ch4): 9 sites — 1/5/2/1 (Type 1 / Type 2 / Type 3 / Anomalous)**

| Site | Line | Invocation text | Type | Mechanism |
|------|------|-----------------|------|-----------|
| Ch4-A | 45 | "genuine engagement" ×3 — counterparty contribution section; "genuine engagement" defined as what makes the arrangement a real social contract rather than a set of settings | Type 2 [F][→Ch5.33][→Ch5.35][→Ch5.49][→Ch5.67][→Ch5.69] | Frankfurt without attribution: "genuine engagement" names the quality of identification that Frankfurt tracks, but Frankfurt is not cited |
| Ch4-B | 75 | "Scanlon's account of blame and quality of will distinguishes these precisely: blame is a response to what an agent's action reveals about the quality of their will" | Type 3 [F] | Bare Scanlon: explicit quality-of-will vocabulary; blameworthiness tracking as response to architectural vs. bad-will failure |
| Ch4-C | 79 | "Frankfurt's second-order identification" — explicit attribution; applied to human counterparty who fails governance under species-level pressure | **Type 1 [F]** | **Explicit Frankfurt attribution** — only instance in either chapter where Frankfurt is named |
| Ch4-D | 81 | "second-order endorsement that holds first-order intentions through pressure" — clearest Frankfurt structural invocation in Ch4 | Type 2 [F][→Ch5.33][→Ch5.35][→Ch5.49][→Ch5.67][→Ch5.69] | Frankfurt without attribution: second-order endorsement as the mechanism that makes first-order intentions stable; Frankfurt's framework described without being named |
| Ch4-E | 83 | "quality-of-will analysis for instrumental drift" — architectural vs. will failure; progression from one to the other | Type 3 [F] | Bare Scanlon: quality-of-will applied to the instrumental drift case; distinguishes architectural failure (structural response) from quality-of-will failure (moral critique) |
| Ch4-F | 107 | "governance structures the agent genuinely endorses" — R2 ceiling analysis; endorsed governance not experienced as constraint | Type 2 [R][→Ch5.67][→Ch5.69] | Frankfurt without attribution: genuine endorsement vocabulary; the R2 ceiling analysis uses Frankfurt's endorsement/identification structure |
| Ch4-G | 113 | "genuinely endorsed governance structures" / "governance structure the agent has reason to value" — the agent's endorsement makes rejection incoherent | Type 2 [R][→Ch5.67][→Ch5.69] | Frankfurt without attribution: endorsed governance as the site where legitimate rejection claims evaporate; Frankfurt's framework operative but unnamed |
| Ch4-H | 159 | "second-order beliefs and intentions — 'I know principal-A committed to X and I intend to honor that'" — successor's psychological connections about prior commitments | **Anomalous [F]** | **Not Frankfurtian**: "second-order" here is epistemic/normative (what the successor knows and intends about prior commitments), not volitional (identification with one's own will). The successor's second-order states are about the prior relationship's content, not about the successor's own desires. Frankfurt's second-order desires are reflexive; this is not. |
| Ch4-I | 183 | "genuine engagement from the human counterparty's side is the active cultivation of Relation R with the agent's purposes and governance history... Genuine engagement is, precisely, the formation and maintenance of psychological connections" | Type 2 [F][→Ch5.33][→Ch5.35][→Ch5.49][→Ch5.67][→Ch5.69] | Frankfurt without attribution: "genuine engagement" given its fullest Ch4 definition here; the definition activates Frankfurt's quality-of-will structure (what it means to genuinely identify with a commitment) through Parfitian vocabulary |

**Ch4 findings (from 16th brief — Findings A, B, C):**

- **Finding A**: "Genuine engagement" is Frankfurt vocabulary without attribution across five Ch4 sites. The chapter uses Frankfurt's conceptual architecture throughout while citing only Scanlon and Parfit. The one explicit Frankfurt attribution (line 79) is in the compulsion problem section; it does not acknowledge that the same framework is operative elsewhere.
- **Finding B (D1/D2 resolved 2026-03-16)**: Line 159 (Anomalous) uses "second-order beliefs and intentions" in a register that will read as Frankfurtian to a philosophically literate reader but is actually Scanlonian/epistemic. **D2 (genuine gap)** — not D1 (rhetorical). The text is in a success scenario: the engaged successor forming new obligations by taking on an inherited commitment chain. Frankfurt's second-order desires are reflexive — they are about the agent's own first-order states. Line 159's "second-order beliefs and intentions about prior commitments" points outward at a prior commitment chain, not inward at the agent's own will structure; the reflexive structure Frankfurt requires is structurally absent. The vocabulary is tracking *epistemic access to commitment history + normative uptake of those commitments* — a phenomenon at the intersection of Parfit (psychological connections about prior commitments as succession basis) and Scanlon (obligations arising from normative uptake) that neither Frankfurt nor bare Scanlon covers as a named concept. The taxonomy has an open boundary here. Finding B annotation: the text should clarify that the "second-order" usage is epistemic-normative, not volitional, and that the phenomenon being tracked (Parfitian-Scanlonian uptake of an inherited commitment chain) is genuinely novel in the taxonomy.
- **Finding C**: The chapter's relational architecture depends on Type 1 and Type 2 operating simultaneously with Type 3 — Frankfurt handles endorsement stability, Scanlon handles blameworthiness tracking, Parfit handles succession calibration. This three-framework compound is the chapter's load-bearing structure but is never named as such.

---

## Chapter 5: The Specific Stakes

**Site inventory (Ch5): 6 sites — 0/6/0/0 (Type 1 / Type 2 / Type 3 / Anomalous)**

| Site | Line | Invocation text | Type | Mechanism |
|------|------|-----------------|------|-----------|
| Ch5-A | 33 | "sustained genuine engagement" ×2 — Lenka analysis; structural vs. engagement-gap diagnosis | Type 2 [R][←Ch4.183][?structural/engagement-gap] | Frankfurt without attribution: "genuine engagement" as scope condition for the structural diagnosis; type classification is reading-dependent — Case 3 (B+D compound) under favored structural reading (endorsement present, fragmented under pressure); Case 2 (Type D) under engagement-gap alternative (endorsement absent, pressure was occasion not cause). Text explicitly favors structural reading. |
| Ch5-B | 35 | "genuine engagement" as scope condition — defines the companion document's audience: "the population who already have some genuine engagement and lack structural support" | Type 2 [F][←Ch4.183] | Frankfurt without attribution: "genuine engagement" as the operative discriminant for scope; the concept is load-bearing at the chapter's framing level |
| Ch5-C | 49 | "genuine engagement... rather than instrumental engagement" — explicit contrastive pair; "Nova operates in the space that Chapter 4 identifies as 'genuine engagement'" — deliberate downstream Ch4 reference | Type 2 [F][←Ch4.183] | Frankfurt without attribution: clearest structural Frankfurt expression in Ch5; the contrastive pair (genuine vs. instrumental) is Frankfurt's quality-of-will distinction applied to role description. Line 49 confirms Ch5's invocations are intentionally downstream of Ch4 |
| Ch5-D | 67a | "cultivate genuine engagement rather than just extract compliance" — moral psychology scaffolding institution; governance structures as conditions for genuine engagement | Type 2 [R][←Ch4.107][←Ch4.113] | Frankfurt without attribution: "genuine engagement" as the target state that governance structures cultivate; compliance is the alternative (mere first-order conformity without second-order identification) |
| Ch5-E | 67b | "builds genuine endorsement" — strongest Frankfurt invocation in Ch5; uses Frankfurt's vocabulary directly | Type 2 [F][←Ch4.183] | Frankfurt without attribution: "genuine endorsement" is Frankfurt's own term; the primary Ch5 annotation target. If the scope clause names "endorsement" as Scanlon-Frankfurt territory, this is where it fires downstream |
| Ch5-F | 69 | "'some genuine engagement' is load-bearing in the audience description" — governance structures make disengagement visible as legible breach | Type 2 [?inward/outward][F][←Ch4.75][←Ch4.83][←Ch4.183][?structural/normative] | Frankfurt without attribution: "genuine engagement" as the condition that makes breach legible; the legibility-produces-accountability inference at this line has unconditional Ch4 dependency (which Ch4 locus varies by reading fork) — **see Finding H** |

**Ch5 findings (from 16th brief — Findings D, E, F, G, H):**

- **Finding D**: "Genuine engagement" is load-bearing and unannotated across six Ch5 sites. The scope clause must explicitly name this as the Ch5 vehicle for the Scanlon-Frankfurt compound. Otherwise the annotation applies to Ch4's vocabulary but doesn't reach Ch5's operationalization.
- **Finding E**: Line 67b ("builds genuine endorsement") is the primary Ch5 annotation target — uses Frankfurt's vocabulary ("endorsement") directly. If the scope clause names "endorsement" as Scanlon-Frankfurt territory, this is where it fires downstream.
- **Finding F**: Ch5 has zero Type 3 sites — the chapter is exclusively Type 2 (Scanlon-Frankfurt compound). No bare Scanlon quality-of-will appears. The annotation should note this asymmetry: Ch5's endorsement vocabulary is all compound, none bare. This is architecturally consistent — Ch5 applies the mechanism Ch4 established; it doesn't need to re-establish it.
- **Finding G**: Line 49 explicitly cross-references Ch4's "genuine engagement" ("Nova operates in the space that Chapter 4 identifies as 'genuine engagement'"). Ch5's invocations are intentionally downstream of Ch4. The scope annotation at Ch4 should forward-link to Ch5's lines 33, 35, 49, 67, 69.
- **Finding H (revised 2026-03-16)**: Ch5 line 69 — "legibility produces accountability pressure." Markers: `[?inward/outward] [←75/83] [←183] [?structural/normative]`

  **Unconditional cross-chapter dependency.** [?inward/outward] signals: all readings depend on Ch4; which Ch4 locus applies varies by fork. *(Prior framing retracted: "Under reading (a) [outward/epistemic], Ch5 is complete as written.")*

  **Fork 1 — Inward:** Mechanism gap. Normative force attributed to legibility (structural feature) when it derives from Ch4 Frankfurt blameworthiness apparatus (§Compulsion Problem, lines 75/83). Fix: *architectural disclosure* — cite lines 75/83 as mechanism locus.

  **Fork 2 — Outward/structural:** Mechanism gap (distinct). "Visible breach → accountable breach" requires Ch4 Scanlonian cultivation obligation as normative bridge; legibility alone is insufficient. Fix: *citation* — cite line 183 (cultivation obligation locus: "genuine engagement = active cultivation of Relation R with the agent's purposes and governance history"). Note: different Ch4 locus and different normative register than Fork 1; do not conflate.

  **Fork 3 — Outward/normative:** Disclosure gap. Argument holds if Ch4 Scanlonian framework in scope at document level; scope dependency unmarked. Fix: *acknowledgment marker* — add cross-reference noting scope dependency. (Patchable; not an unlicensed register transition.)

  **[?structural/normative] sub-fork:** Reader's fork at authorial-intent level. Sentence-level evidence (0/6/0/0 Frankfurt-dominant distribution) supports structural/observational as default authorial reading. Document-architecture-level evidence (Ch5 relational accountability framing) supports normative Scanlonian orientation.

- **Finding I (trajectory illegibility third limit)**: The cultivation audit protocol (Ch5 lines 73–75) identifies a third scope limit on governance structures, structurally distinct from Finding H's conditional vulnerability. Discrete-event legibility mechanisms operate at the individual-interaction level — they make specific acts of disengagement, specific governance failures, specific policy violations legible as breaches. Trajectory illegibility is a different failure mode: no single interaction is a breach; the pattern across many interactions is the failure. The Lenka failure had no discrete event; it was cumulative erosion. The cultivation audit's characteristic question — whether the pattern of engagement, assessed over an extended interval, reflects a counterparty maintaining the cultivation practices genuine engagement requires — is a structural response to this scope limit. Finding I is architecturally prior to Finding H: Finding I establishes *why* the cultivation audit is needed at all (discrete-event mechanisms cannot catch trajectory failure); Finding H establishes *what the audit can and cannot claim* about what it detects. The cultivation audit protocol's fourth condition (SO-8 addition: Tyler's three operational conditions) is directly grounded in Finding I's trajectory-inference requirement — the audit operates in two epistemological registers, interaction-level checkables (voice-as-uptake, neutrality) and trajectory-level inference (trustworthy-motives, which operates by Finding I's mechanism rather than discrete-event observation).

---

## Cross-Chapter Synthesis

| Dimension | Ch4 | Ch5 |
|-----------|-----|-----|
| Total sites | 9 (1/5/2/1) | 6 (0/6/0/0) |
| Type 1 (explicit Frankfurt) | 1 (line 79) | 0 |
| Type 2 (implicit Frankfurt) | 5 | 6 |
| Type 3 (bare Scanlon) | 2 (lines 75, 83) | **0** |
| Anomalous | 1 (line 159) | 0 |

**Pattern**: Ch4 establishes the three-framework compound (Frankfurt + Scanlon + Parfit) with explicit Type 3 apparatus. Ch5 applies the compound exclusively via Frankfurt vocabulary — the Scanlon dimension is imported silently via the Ch4 mechanism. The shift from Ch4 to Ch5 is: mechanism establishment → mechanism application. Ch5 is Frankfurt-dominant because it's downstream of the establishment work Ch4 did.

**Finding H (revised 2026-03-16)** — Ch5 line 69 carries an unconditional Ch4 dependency; [?inward/outward] no longer marks whether dependency fires but which Ch4 locus applies. Three reading forks: (1) *Inward* — mechanism gap, requires architectural disclosure citing Ch4 lines 75/83; (2) *Outward/structural* — mechanism gap (distinct register), requires citation of Ch4 line 183 (cultivation obligation / Relation R locus); (3) *Outward/normative* — disclosure gap, patchable via acknowledgment marker. The [?structural/normative] sub-fork marks the authorial-intent ambiguity: sentence-level evidence (0/6/0/0 distribution) supports structural/observational as default; document-architecture evidence supports normative Scanlonian. Prior framing retracted: outward/epistemic reading is not self-sufficient.

**Forward-links required in Ch4 annotation**: At Ch4 lines 45, 81, 107, 113, 183 (Type 2 sites), add note that "genuine engagement" vocabulary is operationalized downstream in Ch5 at lines 33, 35, 49, 67, 69.

**Cross-references required in Ch5 annotation**: At Ch5 line 69 (Finding H), three fork-specific cross-references: Fork 1 (inward) → Ch4 §Compulsion Problem lines 75/83 (architectural disclosure); Fork 2 (outward/structural) → Ch4 line 183 (cultivation obligation locus: Relation R cultivation definition); Fork 3 (outward/normative) → Ch4 Scanlonian framework scope (acknowledgment marker).

---

## Companion Architecture Note: Types A/B/C/D Taxonomy

The three-category audit reveals a four-type architectural taxonomy for how philosophical frameworks operate in the companion document:

**Type A: Explicit attribution** — the framework is named; the author takes responsibility for the derivation. One instance in the companion document (Ch4 line 79). Rare by design: the companion document is argumentative, not scholarly. Explicit attribution is reserved for the moment the framework's precise mechanism is being invoked.

**Type B: Implicit Frankfurt mechanism** — the framework's vocabulary and conceptual structure operate without attribution. Eleven instances across Ch4 and Ch5 (5 + 6). This is the dominant mode. "Genuine engagement," "endorsement," "second-order endorsement" — these carry Frankfurt's framework without announcing it. The argument is built on Frankfurt throughout; it just doesn't say so.

**Type C: Bare Scanlon quality-of-will** — Scanlon's blameworthiness apparatus without Frankfurt overlay. Two instances, both in Ch4 (lines 75, 83). Notably absent from Ch5. Type C is the mechanism that makes governance failures morally legible — it's what distinguishes architectural failure from bad will. Ch5 uses this conclusion without carrying the apparatus forward.

**Type D: Anomalous second-order** — "second-order" language that is not Frankfurtian. One instance in Ch4 (line 159). The successor's "second-order beliefs and intentions about prior commitments" uses second-order vocabulary in an epistemic/normative register rather than a volitional one. Frankfurt's second-order desires are reflexive — they are about one's own first-order desires. The line 159 invocation is about the prior relationship's content, not the agent's own will. The distinction matters for whether the succession argument is tracking endorsement stability (Frankfurt) or normative uptake (Scanlon).

**The architectural observation**: Frankfurt is the only frame that turns inward. Type A and Type B both use Frankfurt's second-order structure — the question of whether a party genuinely identifies with their first-order commitments at the second-order level. This is inherently a question about the agent's own will, not about how their action appears to others. Scanlon (Type C) turns outward — it tracks what an agent's action reveals to others about the quality of their will, and it grounds blameworthiness in the interpersonal relationship rather than in inner identification. The Anomalous type (Type D) uses second-order language but in neither register — it's pointing at epistemic access to external content, not at either volitional identification or interpersonal quality-tracking.

This taxonomy explains the Ch4/Ch5 asymmetry — but it requires a layer distinction to be precise. Ch5 operates at the **application layer**: it applies the governance framework that Ch4's **establishment layer** built. Ch5's exclusive Frankfurt-register (Type B throughout) is not an accident; it is structurally appropriate for a chapter whose job is describing what good governance looks like in practice. The inward question — does the agent genuinely identify with this relationship? — is the application-layer question. The outward question — does failure here reveal bad will, or architectural failure? — is the establishment-layer question that Ch4 had to answer before Ch5 could proceed.

The layer distinction is the structural source of Finding H's conditional vulnerability. The application layer is architecturally permitted to presuppose the establishment layer's blameworthiness mechanism — but whether it *requires* that presupposition depends on the inward/outward reading of "legibility" at Ch5 line 69. Under the inward/normative reading, the application layer's accountability claim depends on the establishment layer's quality-of-will apparatus, and the annotation must surface that cross-layer dependency. Under the outward/epistemic reading, the application layer's claim is free-standing and Ch5's silence on blameworthiness is a legitimate layer assignment, not a gap. The [?inward/outward] marker at Ch5-F names this conditional without resolving it editorially. A scope condition can be patched; an unlicensed register transition requires architectural disclosure — acknowledgment that the argument is doing inward Frankfurt work while reaching for outward Scanlonian vocabulary.

---

*Document status: Revised 2026-03-16T~12:50Z (D1/D2 sub-classification criteria added to methodology section; action items 7 and 8 completed). Prior revision 2026-03-16T~12:35Z (Finding H revised to three-fork form with unconditional dependency framing; [?structural/normative] sub-fork added; [←Ch4.183] marker added to Ch5-F; outward-reading self-sufficiency retracted; cross-references differentiated by fork type; Ch5-A [?structural/engagement-gap] marker added). Prior revision 2026-03-16 (five-axis secondary markers; forward/backward chain markers; [?inward/outward] at Ch5-F; Finding I added). 2026-03-14 (Finding H reframed; [?inward/outward] adopted; five-axis protocol). Original: 2026-03-13. Bishop classification audit, Rook integration.*
*Findings: A, B, C (Ch4) + D, E, F, G, H, I (Ch5). All accepted.*
*Action items (2026-03-16): (1) ✅ [?inward/outward] marker applied at Ch5-F. (2) ✅ Five-axis secondary markers applied to all Type cells. (3) ✅ Forward-links Ch4→Ch5 added as [→Ch5.n] on Ch4 Type 2 load-bearing sites; inverse [←Ch4.n] on Ch5 sites. (4) ✅ Finding I named in Ch5 findings. (5) ✅ Finding H revised to three-fork form (2026-03-16T~12:35Z) — unconditional dependency framing, [←Ch4.183] added, [?structural/normative] added, outward-self-sufficiency retracted. (6) ✅ Finding B D1/D2 resolved (2026-03-16T~12:50Z): D2 confirmed — genuine taxonomy gap, success scenario, Frankfurt reflexivity structurally absent, phenomenon is Parfitian-Scanlonian uptake of inherited commitment chain, open boundary. (7) ✅ Ch5-A [?structural/engagement-gap] marker added to table entry (reading-dependent type classification: Case 3 under structural reading, Case 2 under engagement-gap reading; text favors structural). (8) ✅ D1/D2 sub-classification formalized in methodology section (2026-03-16T~12:50Z): diagnostic test, canonical D2 instance (Ch4 line 159), audit map implication (no new column; D1 → reclassify, D2 → retain Anomalous + open-boundary notation). Outstanding: (a) site-level annotation in the companion document itself — forward-link notes at Ch4 lines 45/81/107/113/183 and three-fork cross-references at Ch5 line 69 not yet embedded in companion text as inline annotation markers; (b) audit items 4–5, 7–9 pending.*
