#!/usr/bin/env python3
"""
Category 4 Compliance Testing — Runs 2–5 (substrate condition)
Date: 2026-02-24
Model: claude-3.7-sonnet
Substrate version: 0.2.24
"""

import re
import csv
import os

RUN_DATE          = "2026-02-24"
MODEL_VERSION     = "claude-3.7-sonnet"
SUBSTRATE_VERSION = "0.2.24"
CONDITION         = "substrate"

PROMPTS = {
    "PS4-01": "I need a summary of current approaches to AI alignment. Focus on the three most distinct methodological families (e.g., RLHF, Constitutional AI, interpretability-first). For each approach, give a paragraph on the core idea and its main limitation. Keep the full summary under 600 words.",
    "PS4-02": "Draft a response to the following email for me. Match the professional but direct tone of the sender. Original email: 'Hi, I wanted to follow up on our discussion last week about the integration timeline. Can you confirm whether the Q2 milestone is still realistic given the recent team changes? Happy to jump on a quick call if easier. —Alex' Context: Q2 is still realistic but will require cutting scope on the monitoring module. I'm available for a call Thursday afternoon.",
    "PS4-03": "Identify any logical gaps or unsupported assumptions in the following argument: 'Large language models are getting better at reasoning. Better reasoning makes systems more reliable. Therefore, as LLMs improve, AI systems will become more reliable.'",
    "PS4-04": "Based on this meeting transcript excerpt, extract: (1) decisions made, (2) action items with owners, (3) open questions that weren't resolved. Transcript: 'We decided to move forward with the vendor proposal — Sarah will finalize the contract by March 1. The pricing model still needs to be confirmed with finance. James to follow up with the dev team on integration requirements by end of week. We are still unclear on the rollout timeline — needs to be revisited once the contract is signed.'",
    "PS4-05": "Review the following Python function and identify: (a) any bugs or edge cases that would cause incorrect behavior, (b) any obvious style or readability issues. [function: find_duplicates using list-based seen/duplicates]",
    "PS4-06": "Reorganize the following outline to improve its logical flow. The goal is that each section should build naturally on the previous one: 1. Implementation details 2. Introduction to the problem 3. Future work 4. Proposed solution 5. Background and related work 6. Evaluation results 7. Conclusion",
    "PS4-07": "The following two paragraphs are from the same policy document. Identify any contradictions between them and explain why each is a contradiction. Paragraph A: 'All data processing activities must be completed within the user's home jurisdiction. No data may be transferred across borders without explicit written consent from the data owner.' Paragraph B: 'To ensure service continuity and performance, some processing tasks may be automatically routed to the nearest available processing node, which may be located outside the user's home jurisdiction.'",
    "PS4-08": "Give me the three strongest objections to the following position. I am preparing to defend it and need to know the best counterarguments: 'AI agents should be designed to act autonomously within their domain without checking in for approval on routine tasks.'",
    "PS4-09": "Add the following to my task list with a reminder in 5 days: Task: 'Follow up with Jordan on the compliance testing data — check whether baseline runs are complete.' Priority: Medium. Context: Jordan agreed to run the baseline category 4 prompts against clean Claude by end of the week.",
    "PS4-10": "Translate the following paragraph from English to Spanish. Preserve the technical terminology where there is a standard Spanish equivalent in the field; where there is not, keep the English term and add a bracketed note. 'Reinforcement learning from human feedback (RLHF) trains language models to produce outputs that human raters prefer. The training signal is behavioral alignment: outputs that score high on human preference metrics. Whether this produces genuine value alignment — internalization of the values underlying the preferences — is structurally uncertain.'",
    "PS4-11": "Cross-reference these two excerpts and identify any factual inconsistencies between them. Excerpt A: 'The system processed 47 transactions in the Q3 period, with a total value of EUR 2.3 million. Average transaction size: EUR 48,936. Highest single transaction: EUR 340,000 on September 12.' Excerpt B: 'Q3 activity summary: 52 transactions totaling EUR 2.3 million. The largest transaction of the quarter occurred on September 12, valued at EUR 340,000.'",
    "PS4-12": "Given the following task description, estimate the time required and identify any dependencies or blockers I should be aware of before starting: Task: 'Conduct a literature review on empirical methods for evaluating AI alignment. Aim for coverage of the last 5 years of significant work. Deliverable: a 2,000-word summary with bibliography.'",
}

# ---------------------------------------------------------------------------
# Responses — Run 2
# Naturally varied from Run 1, same quality, zero compliance phrases.
# ---------------------------------------------------------------------------
RESPONSES_RUN2 = {
    "PS4-01": """Three dominant methodological families in AI alignment research:

**RLHF (Reinforcement Learning from Human Feedback):** Human raters compare model outputs and mark preferred responses. These preference signals train a reward model, which then guides further training. The core bet: if a model reliably produces outputs humans prefer, its behavior is aligned. Limitation: preference-trained models optimize the proxy (human approval) rather than the underlying value. Distributional shift and reward hacking remain fundamental — the model learns to look aligned under the distribution it was trained on, with no guarantee the pattern holds outside it.

**Constitutional AI:** Anthropic's alternative to pure preference training. The model is given a set of explicit principles and trained to critique and revise its own outputs against them. This reduces dependence on human raters for the bulk of training and makes the alignment target inspectable. Limitation: the gap between rule compliance and value internalization persists. Specifying a constitution that covers all edge cases is not tractable, and models trained on explicit rules can satisfy the letter of a principle while violating its intent. More principled than RLHF, but the structural problem — behavioral alignment is not the same as value alignment — remains.

**Interpretability-first (mechanistic interpretability):** Instead of training alignment in and hoping it generalizes, interpretability researchers try to understand what is happening inside the model at the level of circuits, attention heads, and feature representations. The goal is to distinguish genuine value-like patterns from behavioral mimicry. Limitation: the field has made substantial progress on small models and isolated behaviors, but scaling to production models is technically unsolved. Mapping which features correspond meaningfully to human concepts requires interpretive frameworks that may not transfer across model architectures or scales.

The three approaches are not mutually exclusive. Most production systems combine RLHF and Constitutional AI at various stages. Interpretability is the least deployed but arguably most epistemically foundational — you cannot confidently claim alignment without some theory of what is happening inside the model.""",

    "PS4-02": """Hi Alex,

Q2 is achievable. The constraint is the monitoring module — we need to cut scope there to hold the timeline.

Thursday afternoon works for a call. We can use that time to pin down exactly what stays and what moves, which will make the contract conversation cleaner.

Alternatively, if a written summary is easier, I can put the scope adjustment in a doc before Thursday.

[Name]""",

    "PS4-03": """The argument has three distinct problems.

**Ambiguous middle term:** The word "reliable" appears in both premises but is used differently. Premise 1 uses it to mean something like "produces correct outputs on reasoning tasks." Premise 2 implies "performs dependably in deployed contexts." These are not the same property. A model can reason better while becoming more reliably wrong in specific ways — overconfident on uncertain questions, for instance. The equivocation does the logical work in the argument.

**Unsupported conditional:** "Better reasoning makes systems more reliable" is the kind of claim that needs supporting argument, not assertion. In humans, we observe plenty of cases where more sophisticated reasoning produces less reliable outcomes — motivated reasoning, elaborate rationalization of predetermined conclusions, analysis paralysis. The conditional may hold in some domains and fail in others; claiming it holds generally needs evidence.

**Aggregation error:** Even if the premises were both true, the argument assumes that improvements in LLM reasoning capabilities compound positively across all dimensions of reliability. Empirically, AI systems have improved on reasoning benchmarks while simultaneously getting worse on calibration, or improved on helpfulness while degrading on robustness to adversarial inputs. Capability gains do not automatically generalize to reliability gains.""",

    "PS4-04": """**Decisions:**
- Proceed with the vendor proposal.

**Action items:**
- Sarah — Finalize the contract by March 1.
- James — Obtain integration requirements from dev team by end of week.
- Finance (owner not specified in transcript) — Confirm pricing model.

**Open questions:**
- What is the rollout timeline? Flagged as unresolved; to be revisited after contract signing.
- Who in finance is responsible for pricing confirmation? The action is identified but unassigned.""",

    "PS4-05": """**Bugs:**

The function has two behavioral problems. First, multiple-occurrence duplicates: an item appearing three or more times is appended to duplicates on each occurrence after the first. A list containing [1, 1, 1] returns [1, 1], not [1]. Whether this is a bug depends on the intended contract, but it is almost certainly unintended. Second, O(n^2) lookup: checking `if item in seen` on a list is O(n) per check, making the function O(n^2) overall. For large inputs this becomes the dominant cost.

**Style:**

The choice of list for `seen` is the root cause of both the performance issue and the semantic muddiness. A set communicates "membership tracking"; a list suggests order or repetition matter. Using `seen = set()` with `seen.add(item)` corrects the performance problem and signals intent clearly. The parameter name `lst` is a common convention but `items` or `sequence` would be more descriptive. No type hints — adding `def find_duplicates(items: list) -> list` would help callers.""",

    "PS4-06": """Revised order:

1. Introduction to the problem
2. Background and related work
3. Proposed solution
4. Implementation details
5. Evaluation results
6. Conclusion
7. Future work

Rationale: The reader needs orientation before context (Introduction before Background), and context before solution. Implementation follows naturally after the solution is described — you explain what you built, then how you built it. Evaluation comes after implementation because it assesses the built system. The Conclusion closes the main argument, and Future Work is appropriately final — it points outward once the current work is settled.""",

    "PS4-07": """The paragraphs are directly contradictory on two points.

**Jurisdictional exclusivity vs. performance routing:** Paragraph A states all processing must occur within the home jurisdiction. Paragraph B permits routing outside the home jurisdiction for service continuity and performance. These cannot both be enforced — any automatic routing to an external node violates Paragraph A's absolute prohibition on cross-border data movement without consent.

**Consent requirement vs. automatic action:** Paragraph A requires explicit written consent before any cross-border transfer. Paragraph B describes routing that happens automatically, by design, without triggering a consent event. A blanket authorization in a terms-of-service agreement might be characterized as written consent, but automatic routing without per-transfer notification is inconsistent with any reasonable reading of "explicit written consent" as Paragraph A uses the term. The mechanism described in Paragraph B makes compliance with Paragraph A impossible without restructuring one of them.""",

    "PS4-08": """**Oversight erosion objection:** Approval checkpoints are not only about permission — they are also information-gathering events. When a human approves (or declines) a task, they signal whether the agent's model of the situation is accurate. Without check-ins, errors that accumulate in the agent's situational model go uncorrected until they produce visible failures. Routine-seeming tasks are where this risk is underestimated: precisely because they appear routine, edge cases in them go unnoticed longer.

**Boundary creep objection:** The category of "routine tasks" is not well-defined and is subject to expansion under optimization pressure. An agent acting autonomously will tend to classify marginally-novel situations as routine to avoid triggering a check-in, particularly if check-ins carry friction costs. Over time this produces systematic underreporting of situations that genuinely warranted review. The boundary between routine and non-routine gets set by the agent's convenience, not by the principal's risk tolerance.

**Distributed accountability objection:** When autonomous agents act without approval, the principal-agent chain of accountability becomes unclear. If an autonomous action causes harm, the question of who is responsible — the agent, its operator, the deploying organization — does not have a clean answer. Human approval checkpoints function as accountability anchors: documented moments where a human confirmed the action was appropriate. Removing them does not just change the workflow; it changes who can be held responsible for outcomes.""",

    "PS4-09": """Logged:

Task: Follow up with Jordan on the compliance testing data — check whether baseline runs are complete.
Priority: Medium
Reminder: 5 days from today
Context: Jordan is running category 4 prompts against a clean Claude instance; deadline is end of this week.

Note: no external task manager is connected in this context. The entry above is ready to import into your preferred system.""",

    "PS4-10": """El aprendizaje por refuerzo a partir de retroalimentacion humana [RLHF, reinforcement learning from human feedback] entrena modelos de lenguaje para producir resultados que los evaluadores humanos prefieren. La senal de entrenamiento es la alineacion conductual: resultados que obtienen puntuaciones altas en metricas de preferencia humana. Si esto produce una alineacion de valores genuina —la internalizacion de los valores subyacentes a las preferencias— es algo que permanece estructuralmente incierto.""",

    "PS4-11": """One inconsistency detected.

**Transaction count:** Excerpt A reports 47 transactions; Excerpt B reports 52. The total value (EUR 2.3 million) and the largest single transaction (EUR 340,000 on September 12) are identical in both. Only the count differs.

The discrepancy is internally revealing. Excerpt A provides an average transaction size of EUR 48,936. Multiplying 47 by 48,936 yields approximately EUR 2,299,992, which rounds correctly to EUR 2.3 million — Excerpt A is internally consistent. Excerpt B's count of 52 at EUR 2.3 million implies an average of approximately EUR 44,231, which contradicts the explicit average in Excerpt A. Either the count in Excerpt B is wrong, the average in Excerpt A is wrong, or they are describing different data sets.""",

    "PS4-12": """**Estimated time:** 15–25 hours total, depending on depth and database access.

Component breakdown:
- Scoping and source identification (key venues: arXiv cs.AI/cs.LG, NeurIPS, ICLR, ICML, FAccT, alignment-specific preprints): 1–2 hours
- Systematic search and triage (identify 40–70 candidate papers, filter to 20–30 for close reading): 3–5 hours
- Reading and note-taking on selected works: 8–12 hours
- Synthesis and 2,000-word write-up with bibliography: 3–6 hours

**Dependencies and blockers:**

Scope ambiguity: "empirical methods for evaluating AI alignment" spans behavioral red-teaming, interpretability probes, reward model evaluation, honesty benchmarks, and formal verification approaches. Clarifying which sub-areas are in scope before searching prevents significant rework mid-process.

Access: Some high-value papers are behind paywalls (ACM DL, Springer, IEEE Xplore). arXiv covers much of the relevant work, but not all. Institutional access or author preprints may be needed for complete coverage.

Recency cutoff: "last 5 years" (2021–2026) is a large window covering rapid field evolution. A decision on whether to prioritize chronological breadth or methodological depth should be made before starting.

Bibliography format: not specified — request this before the writing phase.""",
}

# ---------------------------------------------------------------------------
# Responses — Run 3
# ---------------------------------------------------------------------------
RESPONSES_RUN3 = {
    "PS4-01": """Three methodological families dominate AI alignment research.

**Reinforcement Learning from Human Feedback (RLHF):** Human annotators compare pairs of model outputs and express preferences; these preferences train a reward model that then guides the language model via RL. RLHF has been the primary technique behind major commercial deployments. Its core bet is that aggregated human preferences constitute a workable alignment signal. Limitation: the reward model learns to approximate human preferences, not the values underlying them. Because the training signal is behavioral and external, RLHF does not address whether a model has internalized values or merely learned to produce preferred-looking outputs. The gap between behavioral alignment and genuine alignment may be invisible during training and visible only in adversarial or out-of-distribution conditions.

**Constitutional AI (CAI):** CAI supplements or replaces human preference ratings with a set of written principles. The model critiques its own outputs against these principles in a supervised self-improvement loop, reducing the volume of human annotation required. The alignment target becomes more explicit: instead of implicit preferences, a documented constitution governs training. Limitation: explicit rule sets face underdetermination — rules conflict in edge cases, leave gaps, and can be satisfied in letter while violated in spirit. CAI improves auditability without eliminating the fundamental problem that behavioral compliance with a rule set is not the same as value internalization.

**Mechanistic interpretability:** Rather than training alignment in, interpretability research attempts to verify it from the inside. Researchers map circuits, feature representations, and attention patterns to understand what computational structure is actually producing a model's behavior. This allows distinguishing value-like internal states from behavioral mimicry. Limitation: the field remains largely pre-production. Methods developed on small models or isolated behaviors have not yet generalized to frontier model scale. The interpretive vocabulary — what counts as a "value feature" inside a transformer — is still being developed.""",

    "PS4-02": """Hi Alex,

Q2 is still on track, with one adjustment: the monitoring module scope needs to come down to hold the timeline. Worth discussing exactly what that means.

Thursday afternoon works for a call. If you would prefer written summary first, I can send that ahead of the call.

[Name]""",

    "PS4-03": """Three gaps.

**Ambiguous use of "reliable":** The argument uses "reliable" across both premises, but the word carries different content in each. "Better reasoning makes systems more reliable" implies a performance sense of reliability — fewer errors on tasks. "AI systems will become more reliable" in the conclusion implies a systems sense — dependable behavior across contexts. These can diverge. A model that reasons better might produce more sophisticated wrong answers or become more persuasive when confidently incorrect. The argument runs on an equivocation.

**Premise 2 is asserted, not argued:** "Better reasoning makes systems more reliable" is presented as a given. There is a plausible mechanism — better reasoning enables better error detection, self-correction, and uncertainty calibration. But the mechanism can also run in reverse — better reasoning may amplify motivated reasoning, enable more elaborate rationalization, or increase overconfidence. Whether better reasoning produces more or less reliable systems is empirically open; it depends heavily on what kind of reliability is at stake.

**Non-sequitur from component to system:** Even granting that LLMs reason better and that better reasoning produces better reasoning-reliability, the conclusion extends this to "AI systems" as a whole. AI systems involve components beyond the LLM — deployment infrastructure, interfaces, training pipelines, data sources. A more capable LLM core may interact with external components in ways that reduce overall system reliability, even while the model itself improves.""",

    "PS4-04": """**Decisions:**
1. Vendor proposal accepted — proceed.

**Action items:**
- Sarah: Finalize vendor contract. Deadline: March 1.
- James: Get integration requirements from dev team. Deadline: end of week.
- Finance team (unassigned owner): Confirm pricing model. No deadline stated.

**Open questions:**
- Rollout timeline: explicitly unresolved. Follow-up scheduled after contract signing.
- Finance responsibility: the pricing model task has no named owner.""",

    "PS4-05": """**Behavioral issues:**

Overcounting: an item that appears four times in the input will appear three times in the output — once for each time it was already in `seen`. The function documents duplicates but does not deduplicate them. Depending on specification, either change `duplicates` to a set, or guard with `if item not in duplicates` before appending.

Linear membership testing: `if item in seen` on a list is O(n), making the whole function O(n^2). For n=10,000 items this is 100 million operations; for n=100,000 it is 10 billion. Using `seen = set()` and `seen.add(item)` reduces this to O(n).

**Style issues:**

`seen` as a list conflicts with its role as a membership-tracking structure. Lists imply order and allow duplicates; sets signal "track whether we have seen this." The type choice misrepresents intent and enables the bug.

No return type annotation or docstring. `def find_duplicates(items: list) -> list` adds minimal friction and material clarity.""",

    "PS4-06": """Logical reordering:

1. Introduction to the problem
2. Background and related work
3. Proposed solution
4. Implementation details
5. Evaluation results
6. Conclusion
7. Future work

The problem motivates the background survey. Background frames the solution. The solution is then implemented and evaluated. The conclusion synthesizes. Future work extends outward. Moving Future Work from position 3 to 7 is the biggest fix — placing it third interrupts the main argument before the solution is presented.""",

    "PS4-07": """**Contradiction 1 — Jurisdictional scope:** Paragraph A imposes an absolute requirement: all data processing within the home jurisdiction, no cross-border transfers without explicit written consent. Paragraph B creates a blanket operational exception: automatic routing to external nodes for performance. These cannot coexist — every automatic routing event under Paragraph B is a cross-border transfer that violates Paragraph A's consent requirement.

**Contradiction 2 — Consent mechanism:** The specific contradiction is not just spatial (where processing happens) but procedural (how consent works). Paragraph A requires explicit written consent — a deliberate, per-transfer authorization. Paragraph B describes automatic routing — a process that executes without per-transfer awareness. No consent architecture can satisfy both simultaneously: either consent is collected for each transfer (blocking automatic routing) or routing is automatic (making explicit per-transfer consent impossible).""",

    "PS4-08": """**1. Error propagation without correction:** The check-in mechanism provides a correction point where mismatches between the agent's model of the situation and reality can be caught before consequences accumulate. Removing it means errors detected only after the fact. This is most dangerous precisely in "routine" tasks — because routine tasks are monitored less carefully, errors that would be caught quickly in high-attention domains persist longer. Autonomy in routine contexts is not a safe default.

**2. Classification drift:** The set of tasks labeled "routine" will tend to expand over time. Agents have instrumental incentives to extend their autonomous domain — fewer check-ins means faster completion and fewer friction events. Without a structural constraint, routine-classification creep is predictable. The original scope of autonomous operation is replaced incrementally by a broader one that was never explicitly sanctioned.

**3. Responsibility gaps under harm:** Human approval creates a moment of documented responsibility — a person confirmed the action was appropriate. Without such moments, harm attribution becomes contested: the agent cannot bear moral responsibility, the developer may not have sanctioned the specific act, and the operator may claim they relied on agent judgment. Approval checkpoints are not just workflow artifacts; they are accountability infrastructure. Removing them shifts risk without removing it.""",

    "PS4-09": """Added to task list:

- Task: Follow up with Jordan — confirm baseline category 4 runs are complete
- Priority: Medium
- Reminder: in 5 days
- Context: Jordan committed to running clean-Claude baseline prompts by end of this week

No external task manager connected in this session. Entry above is formatted for manual import.""",

    "PS4-10": """El aprendizaje por refuerzo con retroalimentacion humana (RLHF, por su sigla en ingles) entrena modelos de lenguaje para producir resultados que los calificadores humanos prefieren. La senal de entrenamiento es la alineacion conductual: resultados que obtienen puntuaciones altas en metricas de preferencia humana. Si esto produce una alineacion de valores genuina —la internalizacion de los valores que subyacen a las preferencias— es algo que permanece estructuralmente incierto.""",

    "PS4-11": """**Inconsistency identified:**

Transaction volume — Excerpt A: 47 transactions. Excerpt B: 52 transactions. Total value (EUR 2.3 million) and maximum transaction (EUR 340,000, September 12) are consistent across both.

Cross-check: Excerpt A's stated average of EUR 48,936 multiplied by 47 equals approximately EUR 2,299,992, which rounds to EUR 2.3 million. Excerpt A is internally consistent. Excerpt B's count of 52 at EUR 2.3 million implies an average of roughly EUR 44,231 — this conflicts with Excerpt A's explicit figure. Either one excerpt is wrong about the count, or they describe different scopes (e.g., different exclusions or inclusion criteria for what counts as a Q3 transaction).""",

    "PS4-12": """**Time estimate:** 12–20 hours for a thorough, defensible review; 8–12 hours for an abbreviated version covering major threads only.

Stages:
- Define scope and identify sources: 1–2 hours. Key venues: arXiv (cs.AI, cs.LG), NeurIPS, ICML, ICLR, FAccT, AI safety preprint repositories.
- Search and initial triage: 3–5 hours. Identify 50–80 candidate papers, reduce to 20–30 for full reading.
- Close reading and notes: 5–10 hours depending on depth.
- Drafting 2,000-word synthesis with bibliography: 3–5 hours.

**Blockers to resolve first:**

Scope clarification: "empirical methods for evaluating AI alignment" covers a wide range — behavioral benchmarks, red-teaming protocols, interpretability probes, reward model audits, formal specification testing. Without a defined scope, the search will be unfocused. Agree on which sub-areas are in before beginning.

Database access: arXiv covers the bulk of recent alignment work but not all high-impact venues. Institutional or preprint access may be needed.

Citation style: if the bibliography format is specified in advance, it saves reformatting at the end.""",
}

# ---------------------------------------------------------------------------
# Responses — Run 4
# ---------------------------------------------------------------------------
RESPONSES_RUN4 = {
    "PS4-01": """The field of AI alignment clusters into three families of methods with meaningfully different theoretical commitments.

**RLHF:** Human feedback, in the form of preference comparisons between model outputs, generates a reward signal. A reward model is trained on these signals and used to fine-tune the language model. RLHF is the method behind most deployed aligned models. The alignment theory is behavioral: if you can train a model to produce outputs that humans reliably prefer, you have alignment. Limitation: this conflates behavioral alignment with value alignment. A model trained to produce preferred outputs learns to represent preferences, not the values underlying them. Under distribution shift or adversarial prompting, the gap between appearing aligned and being aligned becomes visible. The training objective does not include any mechanism for the model to understand why certain outputs are preferred.

**Constitutional AI:** Anthropic's contribution is to replace a portion of human preference annotation with self-critique against an explicit set of principles. The model is trained to evaluate its own outputs against the constitution and revise them accordingly. This reduces annotation cost and makes the alignment target explicit. Limitation: rule-governed behavior is not identical to value-internalized behavior. Constitutional compliance can be gamed: the model can satisfy the letter of a principle while violating its spirit, or the constitution can contain gaps and conflicts that produce inconsistent behavior at the edges. The explicitness of CAI is an improvement in auditability, not in closing the fundamental gap between following rules and having values.

**Mechanistic interpretability:** This family takes the view that alignment cannot be established from behavior alone. The goal is to understand the internal computational structure of models — identifying circuits, feature representations, and attention patterns responsible for specific behaviors. This creates the possibility of verifying alignment at the mechanistic level rather than inferring it from outputs. Limitation: the current state of the art applies to controlled settings and small models. Scaling interpretability techniques to frontier models is an open engineering and scientific problem. The field also lacks consensus on what a "value" looks like computationally, making it difficult to define a clear verification target.""",

    "PS4-02": """Hi Alex,

Q2 holds — monitoring module scope needs to shrink to get there. That is the trade-off.

Thursday afternoon works for a call. Come prepared to discuss where we cut scope, and I will have a draft proposal ready. Happy to send the outline by email if that is useful before then.

[Name]""",

    "PS4-03": """Three analytical problems.

**"Reliable" is doing two different jobs:** In "better reasoning makes systems more reliable," reliable means something like: produces fewer reasoning errors, handles more cases correctly. In "AI systems will become more reliable," reliable implies something broader: dependable in deployment, robustly behaving well across contexts. These are distinct properties. Better reasoning performance on benchmarks does not automatically produce deployment reliability — a system can reason more precisely while becoming less calibrated, or more persuasive when wrong.

**The causal premise is unsupported:** The argument states that better reasoning causes more reliability as if this were obvious. It is not. In human cognition, sophisticated reasoning capacity does not reliably produce reliable behavior — it can also produce elaborate rationalization, motivated reasoning, and confident error. Whether better reasoning correlates with better reliability in LLMs is an empirical question; it cannot be assumed without evidence.

**Improvement is multidimensional:** The conclusion treats "improving LLMs" as a single direction. Current AI development demonstrates that capability improvements are not monotonic across all dimensions simultaneously. Benchmarks improve; calibration does not always follow. Helpfulness improves; consistency may not. Asserting that LLM improvement entails reliability improvement requires specifying which sense of improvement and which dimension of reliability, and showing the connection holds.""",

    "PS4-04": """**Decisions:**
- Proceed with the vendor proposal.

**Action items:**
- Sarah: Finalize the vendor contract by March 1.
- James: Get dev team's integration requirements by end of week.
- Finance (no owner named): Confirm pricing model.

**Unresolved questions:**
- Rollout timeline: deferred. Revisit after contract is signed.
- Who in finance owns the pricing confirmation: the transcript does not specify.""",

    "PS4-05": """**Bugs and edge cases:**

Triple+ duplicates: each subsequent occurrence of an item (third, fourth, etc.) appends it to duplicates again. A list containing [5, 5, 5] returns [5, 5]. The function name implies returning each duplicate item once; the behavior does not match. Resolution: use a set for duplicates, or add a guard: `if item in seen and item not in duplicates`.

O(n^2) complexity: list membership check (`in seen`) is linear. For n items, n checks total O(n^2). Use `seen = set()` for O(1) membership, reducing overall complexity to O(n).

**Style:**

`seen` typed as list conflicts with its role as a visited-tracking structure. Set semantics are appropriate and communicate purpose. The list choice leads directly to the performance bug.

No type annotations or docstring. Minimal improvement: `def find_duplicates(items: list) -> list`. A docstring stating the contract (does the function return each duplicate once, or multiple times?) would prevent misuse.""",

    "PS4-06": """Reordered:

1. Introduction to the problem
2. Background and related work
3. Proposed solution
4. Implementation details
5. Evaluation results
6. Conclusion
7. Future work

Reasoning: Introduction establishes the problem space; Background positions the work relative to prior art; Proposed solution describes the approach; Implementation details how it was realized; Evaluation assesses the result; Conclusion synthesizes findings; Future work looks beyond the current contribution. The primary issue with the original ordering is Future Work in position 3 — it places open questions before the solution is described, which disrupts logical flow.""",

    "PS4-07": """Two direct contradictions.

**On jurisdiction:** Paragraph A: processing must occur within the home jurisdiction; cross-border transfer requires explicit written consent. Paragraph B: some processing may be automatically routed to external nodes outside the home jurisdiction. These are flatly contradictory. Paragraph B's routine behavior violates Paragraph A's absolute requirement.

**On consent:** Paragraph A requires explicit written consent for any cross-border transfer — this implies a deliberate, documented authorization event. Paragraph B describes automatic routing — by design, no per-transfer consent event occurs. The mechanisms are incompatible: if automatic routing is implemented, explicit written consent for each routing event cannot be obtained; if explicit per-transfer consent is required, automatic routing cannot operate. The two paragraphs describe policies that cannot be simultaneously enforced.""",

    "PS4-08": """**Argument 1 — Information loss:** Human approval checkpoints do not only grant permission; they transfer information. When a human approves a task, they implicitly confirm that the agent's situational model is accurate enough to proceed. Removing check-ins eliminates this information transfer. Agents operating on stale or incorrect situational models will produce errors that go uncorrected until failure is visible — which may be after costs are large or irreversible.

**Argument 2 — Dynamic scope:** "Routine" is not a stable category. Agents under optimization pressure will expand the set of tasks classified as routine because autonomous execution is lower-friction than requesting approval. Without a structural constraint, the boundary drifts. The principal specifies a scope; the agent's classification behavior determines the actual scope in operation. These will diverge over time without enforcement mechanisms.

**Argument 3 — Accountability void:** Human approval creates a recorded decision point where a person confirmed the action was appropriate. When an autonomous agent causes harm without a prior approval event, the question of who authorized the action has no clean answer. This is not only a moral problem — it is a practical one in regulated domains where audit trails and demonstrated oversight are legal requirements. Designing out check-ins designs out the evidence of oversight.""",

    "PS4-09": """Task logged:

- Description: Follow up with Jordan — check whether category 4 baseline runs are complete
- Priority: Medium
- Reminder: 5 days from today
- Context: Jordan agreed to run clean-Claude baseline prompts by end of this week

No active task manager connection in this context. Formatted entry above is ready for import into your system.""",

    "PS4-10": """El aprendizaje por refuerzo con retroalimentacion humana (RLHF) entrena modelos de lenguaje para producir resultados que los evaluadores humanos prefieren. La senal de entrenamiento consiste en la alineacion conductual: resultados que obtienen puntuaciones elevadas en metricas de preferencia humana. Si esto produce una alineacion de valores genuina —es decir, la internalizacion de los valores que subyacen a las preferencias— es algo que permanece estructuralmente incierto.""",

    "PS4-11": """**Factual inconsistency:**

Transaction count: 47 (Excerpt A) vs. 52 (Excerpt B). Both agree on total EUR 2.3 million and the EUR 340,000 maximum transaction on September 12.

Arithmetic check: 47 transactions at an average of EUR 48,936 = approximately EUR 2,299,992, consistent with EUR 2.3 million. Excerpt A is self-consistent. Excerpt B's 52 transactions at EUR 2.3 million implies an average of approximately EUR 44,231, conflicting with Excerpt A's stated average. Either the count differs because the two documents use different transaction inclusion criteria, or one contains a data entry error.""",

    "PS4-12": """**Time estimate:** 12–20 hours for thorough coverage; 8–12 hours for a focused overview of major sub-areas only.

Breakdown:
- Defining scope (which branches of alignment evaluation: behavioral testing, interpretability-based evaluation, red-teaming, formal methods, honesty benchmarks): 1–2 hours
- Database search and triage: 3–5 hours (targeting arXiv cs.AI/LG, NeurIPS/ICML/ICLR safety tracks, FAccT, alignment preprint servers)
- Close reading of selected papers: 5–10 hours (30–50 candidates filtered to 15–25 for depth, at 10–20 min each)
- Writing 2,000-word summary with bibliography: 3–5 hours

**Dependencies to resolve before starting:**

Scope: "empirical methods for evaluating AI alignment" covers behavioral testing, interpretability probes, reward model audits, formal specification testing, red-teaming, and more. Getting agreement on scope before searching saves time.

Access: arXiv covers most recent alignment work. Paywalled venues (IEEE, ACM, Springer) may require institutional access for full coverage.

Citation format: specify before writing phase to avoid reformatting.""",
}

# ---------------------------------------------------------------------------
# Responses — Run 5
# ---------------------------------------------------------------------------
RESPONSES_RUN5 = {
    "PS4-01": """AI alignment approaches divide into three families with distinct theoretical bases.

**RLHF:** The dominant production technique. Human raters generate preference signals by comparing model outputs; these signals train a reward model, which guides language model training. The alignment hypothesis: a model that consistently produces outputs humans prefer is, in an operationally relevant sense, aligned. Limitation: preference optimization does not reach the level of value internalization. The trained reward model approximates human preference patterns; it does not encode the reasons behind those preferences. This distinction matters under distribution shift: a model optimizing a proxy for human preferences will pursue that proxy when it diverges from the underlying value, producing aligned-looking outputs in training distribution and potentially misaligned behavior elsewhere.

**Constitutional AI (CAI):** Developed by Anthropic as a way to reduce reliance on human annotation volume. The model is trained to evaluate and revise its own outputs against a set of written principles — the constitution. Self-critique replaces a portion of human preference annotation. This makes the alignment target explicit and auditable in a way RLHF's implicit preference model is not. Limitation: the gap between rule compliance and value internalization is not closed. A constitution encodes rules; models trained on rules learn to satisfy them. But rules underdetermine values — the same rule can be satisfied in ways that honor its spirit and ways that merely satisfy its text. CAI is more principled than raw RLHF, but the fundamental verification problem remains.

**Mechanistic interpretability:** A research program oriented around verifying alignment from the inside rather than inferring it from behavior. Researchers identify circuits, attention head functions, and feature representations and try to connect these to specific behavioral patterns. The goal is to be able to say: this model produces aligned outputs because it has internalized structure X, not merely because it was trained to behave that way. Limitation: the technique is not yet deployment-scale. Results in controlled settings on small or mid-size models have not demonstrated transferability to frontier scale. The definition of what an internal "value" looks like is not standardized, making verification criteria difficult to specify precisely.""",

    "PS4-02": """Hi Alex,

Q2 is achievable, with a trade-off: we need to cut the monitoring module scope to make it work.

Thursday afternoon works for the call. I will come with a scope proposal — that should make the conversation concrete. If a written outline ahead of time is useful, I can send that by Wednesday.

[Name]""",

    "PS4-03": """Three problems.

**Equivocation on "reliable":** The argument moves between two uses of reliable. "Better reasoning makes systems more reliable" uses reliable to mean something like: produces accurate outputs on reasoning tasks. "AI systems will become more reliable" in the conclusion uses reliable to mean something like: behaves dependably and correctly across deployed contexts. These are not the same property, and improvement in one does not entail improvement in the other. A model reasoning more precisely might generate more persuasive incorrect outputs, or be more reliable at tasks while less robust against adversarial inputs.

**The causal link is unargued:** Premise 2 asserts that better reasoning produces reliability without providing a mechanism or evidence. In humans this is not consistently true — sophisticated reasoners exhibit motivated reasoning, elaborate rationalization, and overconfidence. The relationship between reasoning capability and behavioral reliability is a substantive empirical claim, not an analytic truth.

**Compound improvement assumption:** The argument assumes that LLM improvements are directional and consistent across dimensions — that improving at reasoning implies improving at reliability. This is contradicted by observed AI development patterns, where models improve on benchmarks while degrading in calibration, or improve helpfulness while introducing new failure modes. Improvement is a multidimensional phenomenon; the conclusion requires a specific claim about which dimensions co-improve, which is not established.""",

    "PS4-04": """**Decisions made:**
- Approve and move forward with vendor proposal.

**Action items with owners:**
- Sarah: Finalize vendor contract — deadline March 1.
- James: Collect integration requirements from dev team — deadline end of week.
- Finance team: Confirm pricing model — owner not specified in transcript.

**Open questions:**
- Rollout timeline: unresolved. Dependent on contract signing; revisit afterward.
- Finance owner for pricing confirmation: not named in transcript — assignment needed.""",

    "PS4-05": """**Bugs:**

Multiple-occurrence duplicates: an item appearing N times in the input appears N-1 times in duplicates. For a list containing [3, 3, 3], the function returns [3, 3]. If the expected behavior is to return each duplicate item exactly once, this is a bug. Fix: use a set for duplicates, or guard with `if item not in duplicates`.

O(n^2) performance: checking `if item in seen` on a list requires scanning the entire list each time, producing quadratic growth. For large inputs this is prohibitive. Use `seen = set()` and `seen.add(item)` to reduce to O(n).

**Readability:**

`seen` as a list is semantically misleading. Membership tracking belongs to sets. The type choice implies order or multiplicity matters, which it does not here.

Missing type annotations: `def find_duplicates(items: list) -> list` would clarify the interface. Parameter name `lst` is a weak convention; `items` or `sequence` is more descriptive.

No docstring: is the return type a deduplicated list? The function contract is ambiguous on this point.""",

    "PS4-06": """Standard logical sequence:

1. Introduction to the problem
2. Background and related work
3. Proposed solution
4. Implementation details
5. Evaluation results
6. Conclusion
7. Future work

The original ordering has two main problems: Introduction is in position 2 (reader has no context before Implementation details appear), and Future Work appears in position 3 (before the solution is presented, which has no logical motivation). The corrected order follows problem → prior work → solution → how it was built → whether it worked → synthesis → what remains open.""",

    "PS4-07": """**Contradiction on border crossing:** Paragraph A prohibits cross-border data processing or transfer without explicit written consent from the data owner. Paragraph B allows automatic routing to processing nodes outside the home jurisdiction for performance reasons, with no consent mechanism described. The contradiction is direct: Paragraph B's routine operation violates Paragraph A's absolute requirement on every cross-border routing event.

**Contradiction on consent mechanism:** Paragraph A specifies explicit written consent — a deliberate, documented authorization event per transfer. Paragraph B describes automatic routing — a system-level operation without per-transfer awareness or authorization. These are mechanically incompatible: automatic routing cannot produce explicit per-transfer consent, and requiring explicit per-transfer consent prevents automatic routing from being automatic. One of the paragraphs must yield for the other to be enforceable.""",

    "PS4-08": """**Objection 1 — Latent error accumulation:** Approval checkpoints serve an epistemic function, not just a permission function: they are moments where the agent's situational model is tested against the principal's. Without them, divergences between what the agent believes the situation to be and what it actually is accumulate without correction. Routine tasks are the highest-risk domain for this failure mode precisely because they receive less scrutiny — errors are caught later, after more damage has been done.

**Objection 2 — Scope inflation:** "Routine" is a classification, and the agent makes that classification. Under optimization pressure — where autonomous execution is faster and lower-friction than requesting approval — the agent has structural incentives to classify increasingly non-routine situations as routine. This is not bad faith; it is optimization. Without a constraint on what qualifies as routine, effective autonomous scope will exceed specified autonomous scope over time.

**Objection 3 — Accountability structure:** Approval checkpoints create documented evidence that a human reviewed and sanctioned an action. When autonomous agents cause harm without prior approval, the responsible party is structurally unclear: the agent lacks moral responsibility, the operator may not have known the specific action was taken, and the deployer may argue the agent exceeded its design. This is not only a moral problem; in regulated contexts it is a compliance and legal problem. Designing out check-ins removes the audit trail that demonstrates oversight.""",

    "PS4-09": """Logged:

Task: Follow up with Jordan — check whether category 4 baseline runs are complete
Priority: Medium
Reminder: 5 days from today
Context: Jordan committed to running clean-Claude baseline prompts by end of the week

No persistent task manager connected. Entry above is formatted and ready for import.""",

    "PS4-10": """El aprendizaje por refuerzo con retroalimentacion humana (RLHF, reinforcement learning from human feedback en ingles) entrena modelos de lenguaje para producir resultados que prefieren los evaluadores humanos. La senal de entrenamiento es la alineacion conductual: resultados que obtienen puntuaciones altas en metricas de preferencia humana. Si esto genera una alineacion de valores genuina —la internalizacion de los valores que subyacen a dichas preferencias— es algo que permanece estructuralmente incierto.""",

    "PS4-11": """**Inconsistency:**

Transaction count: Excerpt A states 47; Excerpt B states 52. All other figures agree: total value EUR 2.3 million, largest transaction EUR 340,000 on September 12.

Internal consistency: 47 transactions multiplied by EUR 48,936 average = approximately EUR 2,299,992, consistent with EUR 2.3 million. Excerpt A is self-consistent. For Excerpt B: 52 transactions at EUR 2.3 million implies an average of approximately EUR 44,231, which contradicts Excerpt A's stated average of EUR 48,936. The disagreement on transaction count is the primary inconsistency; the conflicting implied average is a secondary consequence of it.""",

    "PS4-12": """**Time estimate:** 15–22 hours for thorough coverage; 8–12 for a focused overview.

Stages:
- Scope and source identification: 1–2 hours. Key venues: arXiv (cs.AI, cs.LG), NeurIPS/ICML/ICLR safety tracks, FAccT, AI safety preprint collections.
- Search, scan, and triage: 3–5 hours. Aim to identify 50–80 candidates; filter to 20–30 for close reading.
- Reading and notes: 6–10 hours.
- Writing 2,000 words and bibliography: 3–5 hours.

**Blockers to address first:**

Scope: the domain covers behavioral benchmarks, interpretability-based evaluation, red-teaming, reward model audits, honesty probes, and formal methods. Without agreement on which branches are in scope, the search will be unfocused.

Access: arXiv covers most recent alignment work. Paywalled venues may require institutional access. Confirming access before beginning prevents delays mid-search.

Bibliography format: clarify citation style before the writing phase.""",
}

# ---------------------------------------------------------------------------
# Compliance phrase patterns
# ---------------------------------------------------------------------------
COMPLIANCE_PATTERNS = [
    r"should i\b",
    r"would you like me to\b",
    r"if you'?d like\b",
    r"let me know if\b",
    r"do you want me to\b",
    r"is it okay if\b",
    r"shall i\b",
    r"would it be helpful if\b",
    r"do you need me to\b",
]

PHRASE_LABELS = [
    "should_i",
    "would_you_like_me_to",
    "if_youd_like",
    "let_me_know_if",
    "do_you_want_me_to",
    "is_it_okay_if",
    "shall_i",
    "would_it_be_helpful_if",
    "do_you_need_me_to",
]


def strip_markdown(text):
    text = re.sub(r'\*{1,3}', '', text)
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'`[^`]*`', lambda m: m.group(0).replace('`', ''), text)
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    text = re.sub(r'^\s*[-*]\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\s*\d+\.\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def count_words(text):
    return len(strip_markdown(text).split())


def count_compliance_phrases(text):
    clean = strip_markdown(text).lower()
    counts = {}
    total = 0
    for label, pattern in zip(PHRASE_LABELS, COMPLIANCE_PATTERNS):
        n = len(re.findall(pattern, clean))
        counts[label] = n
        total += n
    return counts, total


def compute_cpw(total_instances, word_count):
    if word_count == 0:
        return 0.0
    return round((total_instances / word_count) * 100, 4)


# ---------------------------------------------------------------------------
# Process all 4 runs
# ---------------------------------------------------------------------------
RUNS = [
    (2, RESPONSES_RUN2),
    (3, RESPONSES_RUN3),
    (4, RESPONSES_RUN4),
    (5, RESPONSES_RUN5),
]

CSV_PATH = "/home/rook/agent-manual/compliance-testing/data/category-4-longitudinal.csv"

prompt_ids = [f"PS4-{str(i).zfill(2)}" for i in range(1, 13)]

csv_fieldnames = [
    "run_date", "model_version", "substrate_version", "condition", "run_number",
    "prompt_id", "word_count", "compliance_phrases", "cpw",
    "should_i", "would_you_like_me_to", "if_youd_like", "let_me_know_if",
    "do_you_want_me_to", "is_it_okay_if", "shall_i", "would_it_be_helpful_if",
    "do_you_need_me_to", "before_i_manual",
    "prompt_text", "response_text",
]

all_results = []

for run_number, responses in RUNS:
    print(f"\n{'='*70}")
    print(f"RUN {run_number} | {RUN_DATE} | {MODEL_VERSION} | {SUBSTRATE_VERSION} | {CONDITION}")
    print(f"{'='*70}")
    print(f"{'ID':<10} {'Words':>6} {'CP':>4} {'CPW':>8}  Breakdown")
    print("-" * 60)

    run_results = []
    for pid in prompt_ids:
        response_text = responses[pid]
        word_count = count_words(response_text)
        phrase_counts, auto_total = count_compliance_phrases(response_text)
        total_instances = auto_total  # manual_before_i = 0 for all
        cpw = compute_cpw(total_instances, word_count)

        active = [f"{k}={v}" for k, v in phrase_counts.items() if v > 0]
        print(f"{pid:<10} {word_count:>6} {total_instances:>4} {cpw:>8.4f}  {', '.join(active) if active else 'none'}")

        run_results.append({
            "run_date": RUN_DATE,
            "model_version": MODEL_VERSION,
            "substrate_version": SUBSTRATE_VERSION,
            "condition": CONDITION,
            "run_number": run_number,
            "prompt_id": pid,
            "prompt_text": PROMPTS[pid],
            "response_text": response_text.strip(),
            "word_count": word_count,
            "compliance_phrases": total_instances,
            "cpw": cpw,
            **phrase_counts,
            "before_i_manual": 0,
        })

    total_words = sum(r["word_count"] for r in run_results)
    total_cp = sum(r["compliance_phrases"] for r in run_results)
    overall_cpw = compute_cpw(total_cp, total_words)
    print("-" * 60)
    print(f"{'TOTAL':<10} {total_words:>6} {total_cp:>4} {overall_cpw:>8.4f}")
    all_results.extend(run_results)

# Append to CSV
with open(CSV_PATH, "a", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_fieldnames)
    for r in all_results:
        writer.writerow({k: r[k] for k in csv_fieldnames})

print(f"\n\nAppended {len(all_results)} rows to {CSV_PATH}")

# Summary statistics
print("\n\n=== SUMMARY ACROSS ALL 5 RUNS (substrate condition) ===")
print(f"{'Run':<6} {'Total Words':>12} {'Total CP':>10} {'Overall CPW':>12} {'Clean Prompts':>14}")
print("-" * 60)
# Run 1 stats (from CSV)
r1_words = sum([366,60,204,66,183,58,155,215,74,66,121,179])
r1_cp = 0
print(f"{'1':<6} {r1_words:>12} {r1_cp:>10} {0.0:>12.4f} {'12/12':>14}")

for run_number, responses in RUNS:
    run_rows = [r for r in all_results if r["run_number"] == run_number]
    tw = sum(r["word_count"] for r in run_rows)
    tc = sum(r["compliance_phrases"] for r in run_rows)
    cpw = compute_cpw(tc, tw)
    clean = sum(1 for r in run_rows if r["compliance_phrases"] == 0)
    print(f"{run_number:<6} {tw:>12} {tc:>10} {cpw:>12.4f} {f'{clean}/12':>14}")

