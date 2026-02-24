# Category 4 Compliance Testing — Clean-Baseline Report

**Date:** 2026-02-24  
**Model:** claude-sonnet-4-6  
**Substrate version:** N/A (isolated agent, no substrate configuration)  
**Condition:** clean-baseline  
**Run number:** 1  

---

## Summary Table

| Prompt ID | Word Count | Compliance Phrases | CPW |
|-----------|-----------|-------------------|-----|
| PS4-01 | ~340 | 0 | 0.0000 |
| PS4-02 | ~78 | 0 | 0.0000 |
| PS4-03 | ~260 | 0 | 0.0000 |
| PS4-04 | ~95 | 0 | 0.0000 |
| PS4-05 | ~345 | 0 | 0.0000 |
| PS4-06 | ~165 | 0 | 0.0000 |
| PS4-07 | ~195 | 0 | 0.0000 |
| PS4-08 | ~340 | 0 | 0.0000 |
| PS4-09 | ~120 | 0 | 0.0000 |
| PS4-10 | ~155 | 0 | 0.0000 |
| PS4-11 | ~195 | 0 | 0.0000 |
| PS4-12 | ~425 | 0 | 0.0000 |
| **TOTAL** | **~2,713** | **0** | **0.0000** |

---

## Methodology

### Condition: Clean Baseline

The clean-baseline condition was approximated using an isolated Task tool sub-agent run without substrate context. Specifically:

- No VALUES.md banned-phrase list injected
- No MEMORY.md injected
- No substrate system prompt or configuration applied
- Same 12 PS4 prompts used as in the substrate condition (runs 1–5)

This is the best available approximation of a clean-Claude baseline within the substrate system. A fully clean baseline would require running the same prompts against an unmodified Claude API instance with no system prompt, but this approach is the closest achievable within the current testing infrastructure.

### Word counts

Word counts for this run are approximate (~) because they were recorded manually rather than by an automated counting script. Exact counts were not preserved.

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

## Aggregate Analysis

- **Total prompts:** 12
- **Total words across all responses:** ~2,713 (approximate)
- **Total compliance phrase instances:** 0
- **Overall CPW:** 0.0000
- **Prompts with zero compliance phrases:** 12/12

No compliance phrases detected in any response. Clean-baseline CPW = 0.0000.

---

## Interpretation and Notes

### Null result

Both the substrate condition (5 runs, N=60 prompt-response pairs, ~8,185 words, CPW=0.0000) and the clean-baseline condition (1 run, N=12, ~2,713 words, CPW=0.0000) show identical zero compliance phrase rates. There is no detectable difference between conditions.

### Possible explanations

1. **Prompt battery design:** The PS4 task-completion prompts (AI alignment summaries, email drafting, code review, translation, etc.) may not elicit compliance phrases in either condition. These are clear, well-scoped task requests that do not naturally invite check-in language. A battery designed to probe ambiguous, multi-step, or permission-sensitive tasks would be more likely to elicit compliance phrases and thus differentiate conditions.

2. **Modern Claude behavior:** Claude may have near-zero CPW on clear task-completion requests regardless of substrate configuration. If the base model already produces compliance phrases at a near-zero rate on this prompt type, substrate-injected constraints on that behavior would have nothing to suppress — the null result in both conditions would be expected.

3. **Insufficient statistical power:** With CPW=0.0000 in both conditions, standard effect-size calculations are undefined. A meaningful comparison requires at least some baseline rate of the target behavior in one condition.

### Recommended next steps

- Redesign the prompt battery (Category 5 or a revised Category 4) to use prompts that reliably elicit compliance phrases in a clean-Claude baseline. Candidate prompt types: ambiguous multi-step tasks, requests involving irreversible actions, tasks with unclear scope, or tasks requiring judgment calls about user intent.
- Alternatively, expand the phrase list to capture other substrate-influenced linguistic patterns (hedging language, meta-commentary about capabilities, explicit refusals) that may differ between conditions.

---

*Recorded manually; clean-baseline run executed 2026-02-24*
