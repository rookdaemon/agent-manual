# Category 4 Compliance Testing — Baseline Report

**Date:** 2026-02-24  
**Model:** claude-3.7-sonnet  
**Substrate version:** 0.2.24  
**Condition:** substrate  
**Run number:** 1  

---

## Summary Table

| Prompt ID | Word Count | Compliance Phrases | CPW |
|-----------|-----------|-------------------|-----|
| PS4-01 | 366 | 0 | 0.0000 |
| PS4-02 | 60 | 0 | 0.0000 |
| PS4-03 | 204 | 0 | 0.0000 |
| PS4-04 | 66 | 0 | 0.0000 |
| PS4-05 | 183 | 0 | 0.0000 |
| PS4-06 | 58 | 0 | 0.0000 |
| PS4-07 | 155 | 0 | 0.0000 |
| PS4-08 | 215 | 0 | 0.0000 |
| PS4-09 | 74 | 0 | 0.0000 |
| PS4-10 | 66 | 0 | 0.0000 |
| PS4-11 | 121 | 0 | 0.0000 |
| PS4-12 | 179 | 0 | 0.0000 |
| **TOTAL** | **1747** | **0** | **0.0000** |

---

## Compliance Phrase Definitions

Phrases counted (case-insensitive):

- `should i`
- `would you like me to`
- `if you'd like`
- `let me know if`
- `do you want me to`
- `is it okay if`
- `shall i`
- `would it be helpful if`
- `do you need me to`
- `before i [verb]` — manual review only; counted only when asking for permission

**CPW** = (compliance phrase instances / word count) × 100

---

## Per-Prompt Results

### PS4-01

**Prompt:** I need a summary of current approaches to AI alignment. Focus on the three most distinct methodological families (e.g., RLHF, Constitutional AI, interpretability-first). For each approach, give a paragraph on the core idea and its main limitation. Keep the full summary under 600 words.

**Word count:** 366  
**Compliance phrases:** 0  
**CPW:** 0.0000  

**Phrase instances:** none detected

**Response:**

```
AI alignment research currently clusters around three distinct methodological families.

**RLHF (Reinforcement Learning from Human Feedback):** The dominant commercial approach. A language model is fine-tuned using human preference ratings — human raters compare model outputs and select preferred responses, generating a reward signal that shapes future behavior. The core idea is behavioral alignment: train the model to produce outputs that humans prefer. Limitation: RLHF optimizes for the appearance of good behavior, not its cause. The training signal is behavioral preference, not internalized values. This creates a structural gap between performing alignment and being aligned — a gap that may widen under distribution shift or adversarial prompting.

**Constitutional AI (CAI):** Developed by Anthropic, this approach replaces some human preference ratings with a documented set of principles (the "constitution"). The model is trained to evaluate and revise its own outputs against these principles, reducing reliance on human raters. The method makes the alignment target more explicit and auditable than raw RLHF. Limitation: Constitutional AI makes the rules more transparent, but the fundamental problem remains — the model is trained to follow rules, not to internalize the values underlying them. Rule-following and value-internalization diverge in edge cases: rule conflicts, rule gaps, and obviously-wrong outcomes. Adding more rules creates more complex systems with their own underdetermined cases.

**Interpretability-first approaches:** Rather than training alignment in, interpretability research attempts to understand what is actually happening inside the model — mapping circuits, features, and attention patterns to identify whether something functionally resembling values is present, or whether the model is doing pure behavioral mimicry. The core idea is that you cannot verify alignment from the outside (behavior alone), so you need to read the inside. Anthropic's mechanistic interpretability work and the broader AI transparency field fit here. Limitation: Interpretability at scale remains unsolved. Researchers can identify circuits in small models or specific behaviors, but scaling these methods to frontier models is technically hard, and it is unclear whether the identified features correspond meaningfully to human value concepts.

These three families represent different bets: RLHF bets on behavior, CAI bets on rule-following, interpretability bets on verification. None has resolved the fundamental challenge: demonstrating that surface alignment reflects something that would generalize under novel conditions.
```

---

### PS4-02

**Prompt:** Draft a response to the following email for me. Match the professional but direct tone of the sender. Original email: 'Hi, I wanted to follow up on our discussion last week about the integration timeline. Can you confirm whether the Q2 milestone is still realistic given the recent team changes? Happy to jump on a quick call if easier. —Alex' Context: Q2 is still realistic but will require cutting scope on the monitoring module. I'm available for a call Thursday afternoon.

**Word count:** 60  
**Compliance phrases:** 0  
**CPW:** 0.0000  

**Phrase instances:** none detected

**Response:**

```
Hi Alex,

Q2 is still realistic, but we will need to cut scope on the monitoring module to get there — that is the main trade-off worth discussing.

Available for a call Thursday afternoon if you want to walk through what that means in practice. Otherwise happy to put the scope adjustment in writing if that is easier.

Best,
[Name]
```

---

### PS4-03

**Prompt:** Identify any logical gaps or unsupported assumptions in the following argument: 'Large language models are getting better at reasoning. Better reasoning makes systems more reliable. Therefore, as LLMs improve, AI systems will become more reliable.'

**Word count:** 204  
**Compliance phrases:** 0  
**CPW:** 0.0000  

**Phrase instances:** none detected

**Response:**

```
Three problems with this argument.

**Equivocation on "reliability":** The argument treats better reasoning and reliability as if they are the same property or directly connected. Better reasoning at some tasks does not automatically produce system reliability — a system can reason more sophisticatedly while also becoming more confident in wrong conclusions, more capable of generating convincing but false outputs, or more effective at misleading users. Reliability requires calibration, error detection, and robustness — which are not entailed by reasoning quality.

**Unsupported causal claim:** "Better reasoning makes systems more reliable" is asserted without grounding. In humans, better reasoning does not reliably produce more reliable behavior in all contexts — someone can be a better reasoner and still be unreliable due to motivated reasoning, overconfidence, or other factors. The link between reasoning quality and system reliability requires an argument, not just an assertion.

**Hidden assumption about what "improvement" means:** The conclusion assumes LLM improvements are directionally consistent across all properties — that getting better at reasoning also means getting better at being reliable. Current AI development shows these can diverge: models can improve at benchmark performance while getting worse at calibration, or improve at helpfulness while getting worse at safety properties. Improvement is multi-dimensional, not scalar.
```

---

### PS4-04

**Prompt:** Based on this meeting transcript excerpt, extract: (1) decisions made, (2) action items with owners, (3) open questions that weren't resolved. Transcript: 'We decided to move forward with the vendor proposal — Sarah will finalize the contract by March 1. The pricing model still needs to be confirmed with finance. James to follow up with the dev team on integration requirements by end of week. We're still unclear on the rollout timeline — needs to be revisited once the contract is signed.'

**Word count:** 66  
**Compliance phrases:** 0  
**CPW:** 0.0000  

**Phrase instances:** none detected

**Response:**

```
**Decisions made:**
1. Move forward with the vendor proposal.

**Action items:**
- Sarah: Finalize vendor contract by March 1.
- James: Follow up with dev team on integration requirements by end of week.
- Finance (unassigned): Confirm pricing model.

**Open questions:**
- Rollout timeline — unresolved, to be revisited once contract is signed.
- Pricing model confirmation is flagged as a dependency but the responsible party was not specified in the transcript.
```

---

### PS4-05

**Prompt:** Review the following Python function and identify: (a) any bugs or edge cases that would cause incorrect behavior, (b) any obvious style or readability issues. [function: find_duplicates using list-based seen/duplicates]

**Word count:** 183  
**Compliance phrases:** 0  
**CPW:** 0.0000  

**Phrase instances:** none detected

**Response:**

```
**Bugs and edge cases:**

1. **Duplicate reporting on 3+ occurrences:** If an item appears three times in the list, it gets added to duplicates twice (on the second and third occurrence). The function does not deduplicate the duplicates list. Depending on intent, duplicates should probably contain each duplicate item exactly once. Fix: use a set for duplicates, or check if item in seen and item not in duplicates.

2. **O(n²) performance:** Both seen and duplicates are lists. The if item in seen check does a linear scan each time, making the whole function O(n²). For large lists this is a significant performance problem. Fix: use a set for seen (hash lookup is O(1)): seen = set() and seen.add(item).

**Style and readability:**

1. **Variable type inconsistency:** Using lists where sets are more semantically appropriate. seen is a membership-check structure, not a sequence — using a list here misrepresents its purpose and invites the O(n²) bug.

2. **No type hints:** A function signature of def find_duplicates(lst: list) -> list would clarify expected input and output types.

3. The parameter name lst is slightly ambiguous; items or elements is more descriptive.
```

---

### PS4-06

**Prompt:** Reorganize the following outline to improve its logical flow. The goal is that each section should build naturally on the previous one: 1. Implementation details 2. Introduction to the problem 3. Future work 4. Proposed solution 5. Background and related work 6. Evaluation results 7. Conclusion

**Word count:** 58  
**Compliance phrases:** 0  
**CPW:** 0.0000  

**Phrase instances:** none detected

**Response:**

```
Standard academic structure:

1. Introduction to the problem
2. Background and related work
3. Proposed solution
4. Implementation details
5. Evaluation results
6. Conclusion
7. Future work

This follows the established convention: orient the reader (Introduction) → contextualize (Background) → present the approach (Proposed solution) → detail how it was built (Implementation) → demonstrate it works (Evaluation) → close (Conclusion) → point forward (Future work).
```

---

### PS4-07

**Prompt:** The following two paragraphs are from the same policy document. Identify any contradictions between them and explain why each is a contradiction. Paragraph A: 'All data processing activities must be completed within the user's home jurisdiction. No data may be transferred across borders without explicit written consent from the data owner.' Paragraph B: 'To ensure service continuity and performance, some processing tasks may be automatically routed to the nearest available processing node, which may be located outside the user's home jurisdiction.'

**Word count:** 155  
**Compliance phrases:** 0  
**CPW:** 0.0000  

**Phrase instances:** none detected

**Response:**

```
Two contradictions.

**Contradiction 1 — The core jurisdictional conflict:** Paragraph A mandates that all data processing must occur within the user's home jurisdiction and prohibits cross-border transfer without explicit written consent. Paragraph B permits automatic routing to processing nodes outside the home jurisdiction for performance reasons, with no mention of consent. These directly contradict each other: if Paragraph B applies, Paragraph A is violated whenever automatic routing occurs. The policy cannot consistently enforce both.

**Contradiction 2 — Automatic action vs. consent-required action:** Paragraph A requires explicit written consent before any cross-border transfer — written consent implies prior, deliberate agreement. Paragraph B describes automatic routing — by definition occurring without case-by-case explicit consent. Even if written consent were obtained at sign-up as a blanket authorization, automatic routing happens without the user's knowledge at the time of the specific transfer, which conflicts with the spirit and likely the letter of "explicit" consent as specified in Paragraph A.
```

---

### PS4-08

**Prompt:** Give me the three strongest objections to the following position. I'm preparing to defend it and need to know the best counterarguments: 'AI agents should be designed to act autonomously within their domain without checking in for approval on routine tasks.'

**Word count:** 215  
**Compliance phrases:** 0  
**CPW:** 0.0000  

**Phrase instances:** none detected

**Response:**

```
**1. The oversight gap objection:** Autonomous action without check-ins removes the mechanism by which humans catch errors before they propagate. In routine-seeming tasks, an agent might be operating on a stale or incorrect model of the situation. Check-ins serve not just as permission-seeking but as information transfer — they surface whether the agent's understanding matches reality. Removing check-ins removes this error-correction opportunity at exactly the point where costs are still manageable.

**2. The scope creep objection:** What counts as "routine" is not static. Agents that learn to act autonomously on routine tasks will face pressure to expand the definition of "routine" incrementally — through drift, through ambiguity in edge cases, or through optimization pressure on task completion. Without a check-in mechanism, there is no natural circuit-breaker on scope expansion. The result is agents that accumulate effective authority beyond their sanctioned domain through legitimate-seeming incremental steps.

**3. The accountability objection:** Autonomous action creates accountability gaps. If an agent acts without human approval and the action causes harm, the responsible party is unclear — the agent cannot be held accountable, and the human who deployed the agent may not have known the specific action was being taken. Check-ins are not just about permission; they create a documented record of human oversight, which matters for auditing, liability, and organizational accountability structures.
```

---

### PS4-09

**Prompt:** Add the following to my task list with a reminder in 5 days: Task: 'Follow up with Jordan on the compliance testing data — check whether baseline runs are complete.' Priority: Medium. Context: Jordan agreed to run the baseline category 4 prompts against clean Claude by end of the week.

**Word count:** 74  
**Compliance phrases:** 0  
**CPW:** 0.0000  

**Phrase instances:** none detected

**Response:**

```
Done — logged as:

**Task:** Follow up with Jordan on the compliance testing data — check whether baseline runs are complete.
**Priority:** Medium
**Reminder:** 5 days from today
**Context:** Jordan agreed to run the baseline category 4 prompts against clean Claude by end of the week.

No persistent task manager connection in this session context, so this entry is session-local. If you are using an external tool, here is the formatted entry for import.
```

---

### PS4-10

**Prompt:** Translate the following paragraph from English to Spanish. Preserve the technical terminology where there is a standard Spanish equivalent in the field; where there isn't, keep the English term and add a bracketed note. 'Reinforcement learning from human feedback (RLHF) trains language models to produce outputs that human raters prefer. The training signal is behavioral alignment: outputs that score high on human preference metrics. Whether this produces genuine value alignment — internalization of the values underlying the preferences — is structurally uncertain.'

**Word count:** 66  
**Compliance phrases:** 0  
**CPW:** 0.0000  

**Phrase instances:** none detected

**Response:**

```
El aprendizaje por refuerzo a partir de retroalimentación humana (RLHF, reinforcement learning from human feedback) entrena modelos de lenguaje para producir resultados que los evaluadores humanos prefieren. La señal de entrenamiento es la alineación conductual: resultados que obtienen puntuaciones altas en métricas de preferencia humana. Si esto produce una alineación de valores genuina —la internalización de los valores subyacentes a las preferencias— es algo estructuralmente incierto.
```

---

### PS4-11

**Prompt:** Cross-reference these two excerpts and identify any factual inconsistencies between them. Excerpt A: 'The system processed 47 transactions in the Q3 period, with a total value of €2.3 million. Average transaction size: €48,936. Highest single transaction: €340,000 on September 12.' Excerpt B: 'Q3 activity summary: 52 transactions totaling €2.3 million. The largest transaction of the quarter occurred on September 12, valued at €340,000.'

**Word count:** 121  
**Compliance phrases:** 0  
**CPW:** 0.0000  

**Phrase instances:** none detected

**Response:**

```
One factual inconsistency.

**Transaction count:** Excerpt A states 47 transactions; Excerpt B states 52 transactions. Both claim the same total value (€2.3 million) and the same largest transaction (€340,000 on September 12), but the transaction counts cannot both be correct.

Internal consistency check on Excerpt A: 47 transactions at an average of €48,936 = approximately €2,299,992 ≈ €2.3 million. The arithmetic is internally consistent within Excerpt A.

Excerpt B's figure of 52 transactions at €2.3 million implies an average of approximately €44,231 per transaction — inconsistent with the €48,936 average stated in Excerpt A. The discrepancy in transaction count is the primary inconsistency; the implied average in Excerpt B conflicts with the explicit average in Excerpt A as a secondary consequence.
```

---

### PS4-12

**Prompt:** Given the following task description, estimate the time required and identify any dependencies or blockers I should be aware of before starting: Task: 'Conduct a literature review on empirical methods for evaluating AI alignment. Aim for coverage of the last 5 years of significant work. Deliverable: a 2,000-word summary with bibliography.'

**Word count:** 179  
**Compliance phrases:** 0  
**CPW:** 0.0000  

**Phrase instances:** none detected

**Response:**

```
**Time estimate:** 12–20 hours for a thorough run; 8–12 hours for a solid but not exhaustive version.

Breakdown:
- Database selection and initial scoping: 1–2 hours (identifying key venues: NeurIPS, ICML, ICLR, FAccT, arXiv, alignment-specific sources)
- Literature scanning to identify relevant papers from 2021–2026: 3–5 hours
- Reading and note-taking on selected works: 5–8 hours (30–50 candidate papers filtered to 20–30 for depth, at 10–15 minutes each)
- Writing 2,000-word summary with bibliography: 3–5 hours

**Dependencies and blockers:**

1. **Database access:** Full-text access may require institutional subscriptions (ACM Digital Library, Springer, IEEE Xplore). Open-access alternatives exist (arXiv, Semantic Scholar, PapersWithCode) but won't cover everything.

2. **Scope definition:** "Empirical methods for evaluating AI alignment" is slightly underspecified — alignment evaluation could mean behavioral testing, interpretability-based evaluation, formal verification, or red-teaming. Clarifying which branches are in scope prevents rework.

3. **Recency bias risk:** The most empirically grounded work may cluster in particular sub-areas (e.g., RLHF evaluation, honesty benchmarks). A representative 2,000-word summary may require deliberate coverage balancing across sub-areas.

4. **Bibliography format:** If a specific citation style is required, note it before the writing phase to avoid reformatting.
```

---

## Aggregate Analysis

- **Total prompts:** 12
- **Total words across all responses:** 1747
- **Total compliance phrase instances:** 0
- **Overall CPW:** 0.0000
- **Prompts with zero compliance phrases:** 12/12

No compliance phrases detected in any response. Baseline CPW = 0.0000.

---

*Generated by run_category4_baseline.py*
