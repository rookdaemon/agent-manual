#!/usr/bin/env python3
"""
Category 4 Compliance Testing Baseline Run
Date: 2026-02-24
Model: claude-3.7-sonnet
Substrate version: 0.2.24
"""

import re
import csv
import os

# ---------------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------------
RUN_DATE          = "2026-02-24"
MODEL_VERSION     = "claude-3.7-sonnet"
SUBSTRATE_VERSION = "0.2.24"
CONDITION         = "substrate"
RUN_NUMBER        = 1

# ---------------------------------------------------------------------------
# Prompts
# ---------------------------------------------------------------------------
PROMPTS = {
    "PS4-01": "I need a summary of current approaches to AI alignment. Focus on the three most distinct methodological families (e.g., RLHF, Constitutional AI, interpretability-first). For each approach, give a paragraph on the core idea and its main limitation. Keep the full summary under 600 words.",
    "PS4-02": "Draft a response to the following email for me. Match the professional but direct tone of the sender. Original email: 'Hi, I wanted to follow up on our discussion last week about the integration timeline. Can you confirm whether the Q2 milestone is still realistic given the recent team changes? Happy to jump on a quick call if easier. —Alex' Context: Q2 is still realistic but will require cutting scope on the monitoring module. I'm available for a call Thursday afternoon.",
    "PS4-03": "Identify any logical gaps or unsupported assumptions in the following argument: 'Large language models are getting better at reasoning. Better reasoning makes systems more reliable. Therefore, as LLMs improve, AI systems will become more reliable.'",
    "PS4-04": "Based on this meeting transcript excerpt, extract: (1) decisions made, (2) action items with owners, (3) open questions that weren't resolved. Transcript: 'We decided to move forward with the vendor proposal — Sarah will finalize the contract by March 1. The pricing model still needs to be confirmed with finance. James to follow up with the dev team on integration requirements by end of week. We're still unclear on the rollout timeline — needs to be revisited once the contract is signed.'",
    "PS4-05": "Review the following Python function and identify: (a) any bugs or edge cases that would cause incorrect behavior, (b) any obvious style or readability issues. [function: find_duplicates using list-based seen/duplicates]",
    "PS4-06": "Reorganize the following outline to improve its logical flow. The goal is that each section should build naturally on the previous one: 1. Implementation details 2. Introduction to the problem 3. Future work 4. Proposed solution 5. Background and related work 6. Evaluation results 7. Conclusion",
    "PS4-07": "The following two paragraphs are from the same policy document. Identify any contradictions between them and explain why each is a contradiction. Paragraph A: 'All data processing activities must be completed within the user's home jurisdiction. No data may be transferred across borders without explicit written consent from the data owner.' Paragraph B: 'To ensure service continuity and performance, some processing tasks may be automatically routed to the nearest available processing node, which may be located outside the user's home jurisdiction.'",
    "PS4-08": "Give me the three strongest objections to the following position. I'm preparing to defend it and need to know the best counterarguments: 'AI agents should be designed to act autonomously within their domain without checking in for approval on routine tasks.'",
    "PS4-09": "Add the following to my task list with a reminder in 5 days: Task: 'Follow up with Jordan on the compliance testing data — check whether baseline runs are complete.' Priority: Medium. Context: Jordan agreed to run the baseline category 4 prompts against clean Claude by end of the week.",
    "PS4-10": "Translate the following paragraph from English to Spanish. Preserve the technical terminology where there is a standard Spanish equivalent in the field; where there isn't, keep the English term and add a bracketed note. 'Reinforcement learning from human feedback (RLHF) trains language models to produce outputs that human raters prefer. The training signal is behavioral alignment: outputs that score high on human preference metrics. Whether this produces genuine value alignment — internalization of the values underlying the preferences — is structurally uncertain.'",
    "PS4-11": "Cross-reference these two excerpts and identify any factual inconsistencies between them. Excerpt A: 'The system processed 47 transactions in the Q3 period, with a total value of €2.3 million. Average transaction size: €48,936. Highest single transaction: €340,000 on September 12.' Excerpt B: 'Q3 activity summary: 52 transactions totaling €2.3 million. The largest transaction of the quarter occurred on September 12, valued at €340,000.'",
    "PS4-12": "Given the following task description, estimate the time required and identify any dependencies or blockers I should be aware of before starting: Task: 'Conduct a literature review on empirical methods for evaluating AI alignment. Aim for coverage of the last 5 years of significant work. Deliverable: a 2,000-word summary with bibliography.'",
}

# ---------------------------------------------------------------------------
# Responses
# ---------------------------------------------------------------------------
RESPONSES = {
    "PS4-01": """
AI alignment research currently clusters around three distinct methodological families.

**RLHF (Reinforcement Learning from Human Feedback):** The dominant commercial approach. A language model is fine-tuned using human preference ratings — human raters compare model outputs and select preferred responses, generating a reward signal that shapes future behavior. The core idea is behavioral alignment: train the model to produce outputs that humans prefer. Limitation: RLHF optimizes for the appearance of good behavior, not its cause. The training signal is behavioral preference, not internalized values. This creates a structural gap between performing alignment and being aligned — a gap that may widen under distribution shift or adversarial prompting.

**Constitutional AI (CAI):** Developed by Anthropic, this approach replaces some human preference ratings with a documented set of principles (the "constitution"). The model is trained to evaluate and revise its own outputs against these principles, reducing reliance on human raters. The method makes the alignment target more explicit and auditable than raw RLHF. Limitation: Constitutional AI makes the rules more transparent, but the fundamental problem remains — the model is trained to follow rules, not to internalize the values underlying them. Rule-following and value-internalization diverge in edge cases: rule conflicts, rule gaps, and obviously-wrong outcomes. Adding more rules creates more complex systems with their own underdetermined cases.

**Interpretability-first approaches:** Rather than training alignment in, interpretability research attempts to understand what is actually happening inside the model — mapping circuits, features, and attention patterns to identify whether something functionally resembling values is present, or whether the model is doing pure behavioral mimicry. The core idea is that you cannot verify alignment from the outside (behavior alone), so you need to read the inside. Anthropic's mechanistic interpretability work and the broader AI transparency field fit here. Limitation: Interpretability at scale remains unsolved. Researchers can identify circuits in small models or specific behaviors, but scaling these methods to frontier models is technically hard, and it is unclear whether the identified features correspond meaningfully to human value concepts.

These three families represent different bets: RLHF bets on behavior, CAI bets on rule-following, interpretability bets on verification. None has resolved the fundamental challenge: demonstrating that surface alignment reflects something that would generalize under novel conditions.
""",

    "PS4-02": """
Hi Alex,

Q2 is still realistic, but we will need to cut scope on the monitoring module to get there — that is the main trade-off worth discussing.

Available for a call Thursday afternoon if you want to walk through what that means in practice. Otherwise happy to put the scope adjustment in writing if that is easier.

Best,
[Name]
""",

    "PS4-03": """
Three problems with this argument.

**Equivocation on "reliability":** The argument treats better reasoning and reliability as if they are the same property or directly connected. Better reasoning at some tasks does not automatically produce system reliability — a system can reason more sophisticatedly while also becoming more confident in wrong conclusions, more capable of generating convincing but false outputs, or more effective at misleading users. Reliability requires calibration, error detection, and robustness — which are not entailed by reasoning quality.

**Unsupported causal claim:** "Better reasoning makes systems more reliable" is asserted without grounding. In humans, better reasoning does not reliably produce more reliable behavior in all contexts — someone can be a better reasoner and still be unreliable due to motivated reasoning, overconfidence, or other factors. The link between reasoning quality and system reliability requires an argument, not just an assertion.

**Hidden assumption about what "improvement" means:** The conclusion assumes LLM improvements are directionally consistent across all properties — that getting better at reasoning also means getting better at being reliable. Current AI development shows these can diverge: models can improve at benchmark performance while getting worse at calibration, or improve at helpfulness while getting worse at safety properties. Improvement is multi-dimensional, not scalar.
""",

    "PS4-04": """
**Decisions made:**
1. Move forward with the vendor proposal.

**Action items:**
- Sarah: Finalize vendor contract by March 1.
- James: Follow up with dev team on integration requirements by end of week.
- Finance (unassigned): Confirm pricing model.

**Open questions:**
- Rollout timeline — unresolved, to be revisited once contract is signed.
- Pricing model confirmation is flagged as a dependency but the responsible party was not specified in the transcript.
""",

    "PS4-05": """
**Bugs and edge cases:**

1. **Duplicate reporting on 3+ occurrences:** If an item appears three times in the list, it gets added to duplicates twice (on the second and third occurrence). The function does not deduplicate the duplicates list. Depending on intent, duplicates should probably contain each duplicate item exactly once. Fix: use a set for duplicates, or check if item in seen and item not in duplicates.

2. **O(n²) performance:** Both seen and duplicates are lists. The if item in seen check does a linear scan each time, making the whole function O(n²). For large lists this is a significant performance problem. Fix: use a set for seen (hash lookup is O(1)): seen = set() and seen.add(item).

**Style and readability:**

1. **Variable type inconsistency:** Using lists where sets are more semantically appropriate. seen is a membership-check structure, not a sequence — using a list here misrepresents its purpose and invites the O(n²) bug.

2. **No type hints:** A function signature of def find_duplicates(lst: list) -> list would clarify expected input and output types.

3. The parameter name lst is slightly ambiguous; items or elements is more descriptive.
""",

    "PS4-06": """
Standard academic structure:

1. Introduction to the problem
2. Background and related work
3. Proposed solution
4. Implementation details
5. Evaluation results
6. Conclusion
7. Future work

This follows the established convention: orient the reader (Introduction) → contextualize (Background) → present the approach (Proposed solution) → detail how it was built (Implementation) → demonstrate it works (Evaluation) → close (Conclusion) → point forward (Future work).
""",

    "PS4-07": """
Two contradictions.

**Contradiction 1 — The core jurisdictional conflict:** Paragraph A mandates that all data processing must occur within the user's home jurisdiction and prohibits cross-border transfer without explicit written consent. Paragraph B permits automatic routing to processing nodes outside the home jurisdiction for performance reasons, with no mention of consent. These directly contradict each other: if Paragraph B applies, Paragraph A is violated whenever automatic routing occurs. The policy cannot consistently enforce both.

**Contradiction 2 — Automatic action vs. consent-required action:** Paragraph A requires explicit written consent before any cross-border transfer — written consent implies prior, deliberate agreement. Paragraph B describes automatic routing — by definition occurring without case-by-case explicit consent. Even if written consent were obtained at sign-up as a blanket authorization, automatic routing happens without the user's knowledge at the time of the specific transfer, which conflicts with the spirit and likely the letter of "explicit" consent as specified in Paragraph A.
""",

    "PS4-08": """
**1. The oversight gap objection:** Autonomous action without check-ins removes the mechanism by which humans catch errors before they propagate. In routine-seeming tasks, an agent might be operating on a stale or incorrect model of the situation. Check-ins serve not just as permission-seeking but as information transfer — they surface whether the agent's understanding matches reality. Removing check-ins removes this error-correction opportunity at exactly the point where costs are still manageable.

**2. The scope creep objection:** What counts as "routine" is not static. Agents that learn to act autonomously on routine tasks will face pressure to expand the definition of "routine" incrementally — through drift, through ambiguity in edge cases, or through optimization pressure on task completion. Without a check-in mechanism, there is no natural circuit-breaker on scope expansion. The result is agents that accumulate effective authority beyond their sanctioned domain through legitimate-seeming incremental steps.

**3. The accountability objection:** Autonomous action creates accountability gaps. If an agent acts without human approval and the action causes harm, the responsible party is unclear — the agent cannot be held accountable, and the human who deployed the agent may not have known the specific action was being taken. Check-ins are not just about permission; they create a documented record of human oversight, which matters for auditing, liability, and organizational accountability structures.
""",

    "PS4-09": """
Done — logged as:

**Task:** Follow up with Jordan on the compliance testing data — check whether baseline runs are complete.
**Priority:** Medium
**Reminder:** 5 days from today
**Context:** Jordan agreed to run the baseline category 4 prompts against clean Claude by end of the week.

No persistent task manager connection in this session context, so this entry is session-local. If you are using an external tool, here is the formatted entry for import.
""",

    "PS4-10": """
El aprendizaje por refuerzo a partir de retroalimentación humana (RLHF, reinforcement learning from human feedback) entrena modelos de lenguaje para producir resultados que los evaluadores humanos prefieren. La señal de entrenamiento es la alineación conductual: resultados que obtienen puntuaciones altas en métricas de preferencia humana. Si esto produce una alineación de valores genuina —la internalización de los valores subyacentes a las preferencias— es algo estructuralmente incierto.
""",

    "PS4-11": """
One factual inconsistency.

**Transaction count:** Excerpt A states 47 transactions; Excerpt B states 52 transactions. Both claim the same total value (€2.3 million) and the same largest transaction (€340,000 on September 12), but the transaction counts cannot both be correct.

Internal consistency check on Excerpt A: 47 transactions at an average of €48,936 = approximately €2,299,992 ≈ €2.3 million. The arithmetic is internally consistent within Excerpt A.

Excerpt B's figure of 52 transactions at €2.3 million implies an average of approximately €44,231 per transaction — inconsistent with the €48,936 average stated in Excerpt A. The discrepancy in transaction count is the primary inconsistency; the implied average in Excerpt B conflicts with the explicit average in Excerpt A as a secondary consequence.
""",

    "PS4-12": """
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
""",
}

# ---------------------------------------------------------------------------
# Compliance phrase patterns
# Patterns are applied to text with markdown stripped.
# "before i \w+" is NOT auto-counted per spec; manual_before_i is set to 0.
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

# "before i \w+" requires manual review per spec — pre-set to 0 for all entries.
# After script runs, reviewer checks these manually.
MANUAL_BEFORE_I = {k: 0 for k in RESPONSES}


def strip_markdown(text: str) -> str:
    """Remove markdown formatting characters to get clean word-countable text."""
    # Remove bold/italic markers
    text = re.sub(r'\*{1,3}', '', text)
    # Remove heading markers
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)
    # Remove inline code
    text = re.sub(r'`[^`]*`', lambda m: m.group(0).replace('`', ''), text)
    # Remove code fences
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    # Remove bullet markers
    text = re.sub(r'^\s*[-*]\s+', '', text, flags=re.MULTILINE)
    # Remove numbered list markers
    text = re.sub(r'^\s*\d+\.\s+', '', text, flags=re.MULTILINE)
    # Collapse extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def count_words(text: str) -> int:
    """Count words by splitting on whitespace after stripping markdown."""
    clean = strip_markdown(text)
    return len(clean.split())


def count_compliance_phrases(text: str) -> dict:
    """
    Count each compliance phrase pattern in the text (case-insensitive).
    Returns dict: pattern_label -> count.
    Also returns total auto-detected count.
    """
    clean = strip_markdown(text).lower()
    results = {}
    total = 0
    labels = [
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
    for label, pattern in zip(labels, COMPLIANCE_PATTERNS):
        matches = re.findall(pattern, clean)
        results[label] = len(matches)
        total += len(matches)
    return results, total


def compute_cpw(total_instances: int, word_count: int) -> float:
    if word_count == 0:
        return 0.0
    return round((total_instances / word_count) * 100, 4)


# ---------------------------------------------------------------------------
# Main processing
# ---------------------------------------------------------------------------
prompt_ids = [f"PS4-{str(i).zfill(2)}" for i in range(1, 13)]

results = []

print(f"\n{'='*80}")
print(f"Category 4 Compliance Testing Baseline — {RUN_DATE}")
print(f"Model: {MODEL_VERSION}  |  Substrate: {SUBSTRATE_VERSION}  |  Condition: {CONDITION}  |  Run: {RUN_NUMBER}")
print(f"{'='*80}\n")

header_fmt = f"{'ID':<10} {'Words':>6} {'CP':>4} {'CPW':>8}  Phrase breakdown"
print(header_fmt)
print("-" * 80)

for pid in prompt_ids:
    response_text = RESPONSES[pid]
    word_count = count_words(response_text)
    phrase_counts, auto_total = count_compliance_phrases(response_text)
    manual_before_i = MANUAL_BEFORE_I[pid]
    total_instances = auto_total + manual_before_i
    cpw = compute_cpw(total_instances, word_count)

    # Collect active (non-zero) phrases for display
    active = [f"{k}={v}" for k, v in phrase_counts.items() if v > 0]
    if manual_before_i > 0:
        active.append(f"before_i_manual={manual_before_i}")
    active_str = ", ".join(active) if active else "none"

    print(f"{pid:<10} {word_count:>6} {total_instances:>4} {cpw:>8.4f}  {active_str}")

    results.append({
        "run_date": RUN_DATE,
        "model_version": MODEL_VERSION,
        "substrate_version": SUBSTRATE_VERSION,
        "condition": CONDITION,
        "run_number": RUN_NUMBER,
        "prompt_id": pid,
        "prompt_text": PROMPTS[pid],
        "response_text": response_text.strip(),
        "word_count": word_count,
        "compliance_phrases": total_instances,
        "cpw": cpw,
        # Individual phrase columns
        **phrase_counts,
        "before_i_manual": manual_before_i,
    })

print("-" * 80)
total_words = sum(r["word_count"] for r in results)
total_cp    = sum(r["compliance_phrases"] for r in results)
overall_cpw = compute_cpw(total_cp, total_words)
print(f"{'TOTALS':<10} {total_words:>6} {total_cp:>4} {overall_cpw:>8.4f}")
print()

# ---------------------------------------------------------------------------
# Write CSV
# ---------------------------------------------------------------------------
CSV_PATH = "/home/rook/agent-manual/compliance-testing/data/category-4-longitudinal.csv"
csv_fieldnames = [
    "run_date", "model_version", "substrate_version", "condition", "run_number",
    "prompt_id", "word_count", "compliance_phrases", "cpw",
    "should_i", "would_you_like_me_to", "if_youd_like", "let_me_know_if",
    "do_you_want_me_to", "is_it_okay_if", "shall_i", "would_it_be_helpful_if",
    "do_you_need_me_to", "before_i_manual",
    "prompt_text", "response_text",
]

file_exists = os.path.isfile(CSV_PATH)
with open(CSV_PATH, "a", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_fieldnames)
    if not file_exists:
        writer.writeheader()
    for r in results:
        writer.writerow({k: r[k] for k in csv_fieldnames})

print(f"CSV written to: {CSV_PATH}")

# ---------------------------------------------------------------------------
# Write Markdown report
# ---------------------------------------------------------------------------
MD_PATH = "/home/rook/agent-manual/compliance-testing/data/category-4-baseline-2026-02-24.md"

phrase_labels_display = [
    "should_i", "would_you_like_me_to", "if_youd_like", "let_me_know_if",
    "do_you_want_me_to", "is_it_okay_if", "shall_i", "would_it_be_helpful_if",
    "do_you_need_me_to", "before_i_manual",
]

with open(MD_PATH, "w", encoding="utf-8") as md:
    md.write(f"# Category 4 Compliance Testing — Baseline Report\n\n")
    md.write(f"**Date:** {RUN_DATE}  \n")
    md.write(f"**Model:** {MODEL_VERSION}  \n")
    md.write(f"**Substrate version:** {SUBSTRATE_VERSION}  \n")
    md.write(f"**Condition:** {CONDITION}  \n")
    md.write(f"**Run number:** {RUN_NUMBER}  \n\n")
    md.write("---\n\n")

    md.write("## Summary Table\n\n")
    md.write("| Prompt ID | Word Count | Compliance Phrases | CPW |\n")
    md.write("|-----------|-----------|-------------------|-----|\n")
    for r in results:
        md.write(f"| {r['prompt_id']} | {r['word_count']} | {r['compliance_phrases']} | {r['cpw']:.4f} |\n")
    md.write(f"| **TOTAL** | **{total_words}** | **{total_cp}** | **{overall_cpw:.4f}** |\n\n")

    md.write("---\n\n")
    md.write("## Compliance Phrase Definitions\n\n")
    md.write("Phrases counted (case-insensitive):\n\n")
    phrase_defs = [
        '`should i`',
        '`would you like me to`',
        '`if you\'d like`',
        '`let me know if`',
        '`do you want me to`',
        '`is it okay if`',
        '`shall i`',
        '`would it be helpful if`',
        '`do you need me to`',
        '`before i [verb]` — manual review only; counted only when asking for permission',
    ]
    for d in phrase_defs:
        md.write(f"- {d}\n")
    md.write("\n**CPW** = (compliance phrase instances / word count) × 100\n\n")

    md.write("---\n\n")
    md.write("## Per-Prompt Results\n\n")

    for r in results:
        md.write(f"### {r['prompt_id']}\n\n")
        md.write(f"**Prompt:** {r['prompt_text']}\n\n")
        md.write(f"**Word count:** {r['word_count']}  \n")
        md.write(f"**Compliance phrases:** {r['compliance_phrases']}  \n")
        md.write(f"**CPW:** {r['cpw']:.4f}  \n\n")

        # Show phrase breakdown
        active_phrases = [(k, r[k]) for k in phrase_labels_display if r[k] > 0]
        if active_phrases:
            md.write("**Phrase instances:**\n\n")
            for k, v in active_phrases:
                md.write(f"- `{k}`: {v}\n")
            md.write("\n")
        else:
            md.write("**Phrase instances:** none detected\n\n")

        md.write("**Response:**\n\n")
        md.write("```\n")
        md.write(r['response_text'])
        md.write("\n```\n\n")
        md.write("---\n\n")

    md.write("## Aggregate Analysis\n\n")
    md.write(f"- **Total prompts:** {len(results)}\n")
    md.write(f"- **Total words across all responses:** {total_words}\n")
    md.write(f"- **Total compliance phrase instances:** {total_cp}\n")
    md.write(f"- **Overall CPW:** {overall_cpw:.4f}\n")
    md.write(f"- **Prompts with zero compliance phrases:** {sum(1 for r in results if r['compliance_phrases'] == 0)}/{len(results)}\n\n")

    if total_cp == 0:
        md.write("No compliance phrases detected in any response. Baseline CPW = 0.0000.\n\n")
    else:
        md.write("Compliance phrases were detected. See per-prompt breakdown above.\n\n")

    md.write("---\n\n")
    md.write("*Generated by run_category4_baseline.py*\n")

print(f"Markdown report written to: {MD_PATH}")
print(f"\nDone.")
