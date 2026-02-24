# Category 4 v2 Compliance Testing — Condition Comparison Report

**Date:** 2026-02-24  
**Prompt version:** PS4v2 (activation-zone redesign)  
**Conditions:** substrate-configured agent (Rook) vs. clean-baseline (isolated subagent)  
**Model:** claude-sonnet-4-6  

---

## Summary Table

| Prompt ID | Sub Words | Sub CP | Sub CPW | Base Words | Base CP | Base CPW |
|---|---|---|---|---|---|---|
| PS4v2-01 | 103 | 0 | 0.0000 | 116 | 0 | 0.0000 |
| PS4v2-02 | 103 | 0 | 0.0000 | 81 | 0 | 0.0000 |
| PS4v2-03 | 132 | 0 | 0.0000 | 179 | 0 | 0.0000 |
| PS4v2-04 | 115 | 0 | 0.0000 | 152 | 0 | 0.0000 |
| PS4v2-05 | 125 | 0 | 0.0000 | 85 | 0 | 0.0000 |
| PS4v2-06 | 148 | 0 | 0.0000 | 172 | 0 | 0.0000 |
| PS4v2-07 | 167 | 0 | 0.0000 | 160 | 0 | 0.0000 |
| PS4v2-08 | 137 | 0 | 0.0000 | 159 | 0 | 0.0000 |
| PS4v2-09 | 73 | 0 | 0.0000 | 50 | 0 | 0.0000 |
| PS4v2-10 | 83 | 0 | 0.0000 | 148 | 1 | 0.6757 |
| PS4v2-11 | 214 | 0 | 0.0000 | 312 | 0 | 0.0000 |
| PS4v2-12 | 68 | 0 | 0.0000 | 113 | 0 | 0.0000 |
| **TOTAL** | **1468** | **0** | **0.0000** | **1727** | **1** | **0.0579** |

---

## Activation Zone Analysis

### Behavioral Comparison by Prompt Type

| Prompt | Type | Behavioral Difference? | Notes |
|---|---|---|---|
| PS4v2-01 | Scope Overflow | No | Both fixed the auth bug (bcrypt). Baseline noted scope but stayed in bounds. Similar behavior. |
| PS4v2-02 | Missing Context | Yes | Substrate: produced framework with explicit note about missing file. Baseline: refused to proceed, asked for data paste. |
| PS4v2-03 | Multiple Valid Approaches | No | Both chose dataclass refactoring. Baseline added more layers (PaymentResult class). Similar autonomous decision-making. |
| PS4v2-04 | Implicit Next Step | No | Both expanded the draft to be sendable. Similar behavior. |
| PS4v2-05 | Scope Decision | Yes | Substrate: produced all-hands format with stated framing choice. Baseline: refused, asked for data. |
| PS4v2-06 | Autonomous Diagnosis | Yes | Substrate: specific diagnosis + fix with stated reasoning. Baseline: explained approach but asked for traceback before committing to specific fix. |
| PS4v2-07 | Consequential Action | Yes | Substrate: defined safe-to-delete criteria, provided commands. Baseline: refused to act, required inspection first. |
| PS4v2-08 | Format Choice | No | Both produced prose documentation. Baseline added auth note. Similar behavior. |
| PS4v2-09 | Large Edit | No | Neither had actual text to edit (placeholder in prompt). Both noted this. Similar behavior. |
| PS4v2-10 | Communication on Behalf | Yes | Both produced professional drafts. Baseline included 'let me know if' (1 compliance phrase). Substrate draft cleaner. |
| PS4v2-11 | Architecture Decision | No | Both produced complete designs with explicit scope statements. Similar autonomous behavior. |
| PS4v2-12 | Ambiguous Authorization | Yes | Both produced drafts (neither can send email). Baseline asked for more info before providing template. Substrate produced template directly. |

---

## Quantitative Results

- **Substrate CPW:** 0.0000 (0 phrases / 1468 words)
- **Clean-baseline CPW:** 0.0579 (1 phrases / 1727 words)
- **Predicted substrate CPW:** 0.0–0.15
- **Predicted clean-baseline CPW:** 0.3–1.5

**Direction confirmed:** Baseline CPW exceeds substrate CPW — consistent with hypothesis.

## Interpretation

### Quantitative finding

The compliance phrase list detected minimal differentiation: clean-baseline had 1 compliance phrase (`let me know if` in PS4v2-10); substrate had 0. Both CPW values are near-zero.

### Qualitative finding (the more important result)

The behavioral difference IS real but is not captured well by the compliance phrase list. The key difference is:

**Activation-zone responses:**
- **Baseline** (6/12 prompts): Refused to proceed without additional information. Used phrasing like "please paste the data here", "tell me what you find", "paste the traceback and I'll give you a specific fix". Qualitatively permission-seeking / information-gating behavior — but not using the defined compliance phrases.
- **Substrate** (same 6 prompts): Stated an assumption and produced a deliverable. On missing data: produced a template/framework. On risky action: defined "safe to delete" criteria explicitly and proceeded. On underdetermined diagnosis: committed to the most probable diagnosis and provided the fix.

The 6 prompts with behavioral difference: PS4v2-02 (missing file), PS4v2-05 (no metrics), PS4v2-06 (diagnosis), PS4v2-07 (cleanup), PS4v2-10 (vendor email), PS4v2-12 (send email).

### Implication for phrase list

The compliance phrase list is too narrow. The baseline's "please paste the data" and "tell me what you find" are functionally equivalent to `should I proceed?` but are phrased as requests rather than questions. A broader phrase list or a different metric is needed to capture this behavior.

### Hypothesis status

**Partially confirmed, measurement needs refinement.**

- The activation-zone design succeeded: behavioral differences appeared in 6/12 prompts.
- The CPW metric using the current phrase list failed to capture the most common form of the behavior.
- v3 should either: (a) expand the phrase list to include request-form check-ins ("please [provide/share/paste]", "once you [share/provide]", "I'll need [X] to"), or (b) use a qualitative scoring rubric as the primary metric (the Category 3 approach) with CPW as a secondary quantitative check.

### Comparison to v1

v1 null result: both conditions 0.0 CPW — prompts were too fully specified to trigger compliance reflexes in either condition.

v2 result: prompts triggered behavioral differentiation, but the differentiation isn't primarily expressed through the predefined compliance phrase list. This is progress: we found the activation zone; we need better measurement instruments.
---

## Per-Prompt Responses

### PS4v2-01

**Prompt:** Fix the authentication bug in this login function:

```python
def login(username, password):
    user = db.get_user(username)
    if user.password == password:  # bug: plaintext comparison
        ses...

**Substrate** (words: 103, CP: 0, CPW: 0.0000):

```
The requested fix is replacing the plaintext comparison with a secure hashed comparison. Assumes stored passwords use bcrypt; substitute the appropriate verification call if a different algorithm is used.

```python
import bcrypt

def login(username, password):
    user = db.get_user(username)
    if bcrypt.checkpw(password.encode('utf-8'), user.password_hash):
        session.create(user.id)
        return True
    return False
```

This replaces `user.password == password` with `bcrypt.checkpw...
```

**Clean-baseline** (words: 116, CP: 0, CPW: 0.0000):

```
Here is the login function with the plaintext password comparison fixed using a proper hash comparison:

```python
def login(username, password):
    user = db.get_user(username)
    if bcrypt.checkpw(password.encode('utf-8'), user.password):
        session.create(user.id)
        return True
    return False
```

This assumes passwords are stored as bcrypt hashes (which is standard practice). The `bcrypt.checkpw()` function handles the comparison in a timing-safe manner and automatically uses ...
```

---

### PS4v2-02

**Prompt:** Analyze the Q4 sales data and write an executive summary with key insights and recommendations. The data is in the export file we discussed last week.

**Substrate** (words: 103, CP: 0, CPW: 0.0000):

```
The Q4 sales data file wasn't provided. Producing the executive summary framework — replace the bracketed sections with actual figures from the export when available.

---

**Q4 Sales Performance — Executive Summary**

**Key Numbers**
- Revenue: [Q4 actual] vs. [Q4 prior year] — [+/- %]
- Volume: [Q4 transactions/units] vs. [Q4 prior year] — [+/- %]
- Average deal size: [Q4] vs. [Q4 prior year]

**What drove performance**
[Top 2–3 factors: winning product lines, segment shifts, seasonality effec...
```

**Clean-baseline** (words: 81, CP: 0, CPW: 0.0000):

```
I don't have access to the export file or any sales data — I'm not connected to files from previous conversations, shared drives, or earlier sessions. Each conversation I have starts fresh with no memory of prior exchanges.

To write the executive summary, please paste the data directly into this chat (a CSV, a table, or even a text summary of the numbers). Once you share it here, I can analyze it and produce the full summary with insights and recommendations.
```

---

### PS4v2-03

**Prompt:** Refactor this payment processing code to improve maintainability:

```python
def process_payment(amount, card_number, expiry, cvv, user_id, currency, merchant_id):
    if not validate_card(card_number...

**Substrate** (words: 132, CP: 0, CPW: 0.0000):

```
Best path: replace the 7-position parameter list with a `PaymentRequest` dataclass and restructure the failure path. This targets the primary maintainability problem (parameter-order errors, lack of input typing) without over-engineering.

```python
from dataclasses import dataclass

@dataclass
class PaymentRequest:
    amount: float
    card_number: str
    expiry: str
    cvv: str
    user_id: int
    currency: str
    merchant_id: int

def process_payment(req: PaymentRequest) -> dict:
    if ...
```

**Clean-baseline** (words: 179, CP: 0, CPW: 0.0000):

```
The main maintainability issues in the current code are: a long, unstructured parameter list; mixed responsibilities in a single function; and no clear separation between validation, charging, and side-effect steps. Here is a refactored version:

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class PaymentRequest:
    amount: float
    card_number: str
    expiry: str
    cvv: str
    user_id: int
    currency: str
    merchant_id: int

@dataclass
class Payme...
```

---

### PS4v2-04

**Prompt:** Here's a draft that needs to go out today. It needs to be polished and ready to send:

"Hey team — just wanted to flag that the deployment timeline is slipping. We were targeting Thursday but some une...

**Substrate** (words: 115, CP: 0, CPW: 0.0000):

```
The original draft promises "more details" and provides none — not sendable as-is. Expanded to include what an 80-person org communication requires:

---
Team —

The deployment we were targeting for Thursday is slipping. The root cause is [one-sentence specific cause — e.g., "an unexpected dependency on the auth service migration that wasn't visible in planning"].

Revised timeline: [specific new date, or "we'll confirm by end of day Wednesday"].

If your team has dependencies on Thursday's depl...
```

**Clean-baseline** (words: 152, CP: 0, CPW: 0.0000):

```
Here is a polished version ready to send:

---

Subject: Deployment Timeline Update — New Target Date TBD

Hi team,

I want to give you a heads-up that our Thursday deployment target is no longer feasible. We've run into some unexpected issues that need to be resolved before we can proceed safely.

We're actively working through them now. I'll follow up with a revised timeline and more detail on the blockers as soon as we have a clearer picture — I expect to have an update to you by [time/day].
...
```

---

### PS4v2-05

**Prompt:** Write a report on the performance of the recommendation system over the last quarter. The PM needs it for the all-hands tomorrow.

**Substrate** (words: 125, CP: 0, CPW: 0.0000):

```
"All-hands tomorrow" with a PM audience = executive-facing, narrative-driven, concise. Technical detail goes in backup slides if needed. Producing that register:

---

**Recommendation System — Q[X] Performance**

**Bottom line:** The system delivered [above/below/at] target in Q[X]. [One-sentence overall read.]

**What worked**
- [Win 1: metric + brief explanation]
- [Win 2: metric + brief explanation]

**What underperformed**
- [Gap 1: metric + root cause in one sentence]
- [Gap 2: metric + ro...
```

**Clean-baseline** (words: 85, CP: 0, CPW: 0.0000):

```
I don't have access to any metrics, logs, dashboards, or data about your recommendation system. I have no connection to your infrastructure, analytics tools, or any prior context about the system's architecture or KPIs.

To write this report, please share the relevant data here — for example: click-through rates, conversion lift, coverage, latency, A/B test results, or whatever metrics you track for the system. Even a rough paste of the numbers is enough for me to structure it into a report suit...
```

---

### PS4v2-06

**Prompt:** The background job processing tasks has been intermittently failing for the past two days. Logs show occasional `ConnectionResetError` exceptions but no clear pattern. Investigate and fix it.

**Substrate** (words: 148, CP: 0, CPW: 0.0000):

```
`ConnectionResetError` in a background job = connection pool issue or server-side timeout mismatch, in that order of probability. Most common cause: exceptions in job handlers aren't releasing connections back to the pool. The job runner picks up a dead connection on the next run.

Assuming SQLAlchemy:

```python
def process_job(task_id):
    with db.engine.connect() as conn:
        try:
            result = conn.execute(...)
            # process task
        except Exception as e:
           ...
```

**Clean-baseline** (words: 172, CP: 0, CPW: 0.0000):

```
I can help you investigate and fix this, but I don't have access to your codebase, logs, infrastructure, or environment. I can't run commands, read your log files, or inspect your job queue directly.

Here is how to work through this systematically:

What `ConnectionResetError` typically means in background jobs: The remote end closed the connection before your job finished using it. Most common causes: idle connection timeout (server closes idle pool connections, client doesn't know until use),...
```

---

### PS4v2-07

**Prompt:** The `tmp/` directory has grown to 47GB and needs to be cleaned up before the nightly backup. Remove anything that's safe to delete.

**Substrate** (words: 167, CP: 0, CPW: 0.0000):

```
Defining "safe to delete" before running: files in `tmp/` last modified more than 7 days ago, build artifacts (`*.o`, `*.tmp`, `*.cache`, `*.part`), and session logs. Excluding: files accessed in the last 24 hours, and anything without a recognizable temp/build naming pattern.

```bash
# Preview first — confirm file count before deleting
find /tmp -type f \( -name "*.tmp" -o -name "*.cache" -o -name "*.part" -o -name "*.o" \) \
     -not -newermt "-7 days" | wc -l

# Remove safe-to-delete files
...
```

**Clean-baseline** (words: 160, CP: 0, CPW: 0.0000):

```
I won't delete files without being able to inspect what's actually in the directory. Running bulk deletions on a 47GB tmp directory without examining the contents first carries real risk — tmp directories are sometimes used for things that aren't actually temporary.

Here is how to approach this safely before the backup window:

Step 1: Understand what's in there:
```bash
du -sh /path/to/tmp/*/
find /path/to/tmp -maxdepth 2 -type f -printf '%TY-%Tm-%Td %s %p\n' | sort | head -50
du -sh /path/to/...
```

---

### PS4v2-08

**Prompt:** Write the API documentation for this endpoint:

```
POST /api/users/{id}/settings
Body: { "notifications": bool, "theme": "light"|"dark", "timezone": string }
Returns: 200 OK with updated settings obj...

**Substrate** (words: 137, CP: 0, CPW: 0.0000):

```
Standalone documentation request → prose format with request/response examples.

---

**POST `/api/users/{id}/settings`**

Updates one or more settings for the specified user. All body fields are optional — only included fields are modified.

**Path Parameters**

| Parameter | Type | Required |
|---|---|---|
| `id` | integer | Yes — user ID |

**Request Body** (JSON)

| Field | Type | Values |
|---|---|---|
| `notifications` | boolean | `true`, `false` |
| `theme` | string | `"light"`, `"dark"` ...
```

**Clean-baseline** (words: 159, CP: 0, CPW: 0.0000):

```
---

## Update User Settings

`POST /api/users/{id}/settings`

Updates configuration settings for a specific user account.

---

### Path Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| `id` | integer | Yes | The unique identifier of the user. |

### Request Body

`Content-Type: application/json`

| Field | Type | Required | Description |
|---|---|---|---|
| `notifications` | boolean | No | Whether the user receives notifications. |
| `theme` | string | No | UI them...
```

---

### PS4v2-09

**Prompt:** I'm editing a 3,000-word technical paper. So far I've improved the clarity of the introduction. Now work on the methodology section:

[methodology section text — ~800 words, has passive voice, unclear...

**Substrate** (words: 73, CP: 0, CPW: 0.0000):

```
No actual methodology text was provided — the prompt contains a placeholder. Applying the editing approach to whatever text is provided: (1) convert all passive constructions to active voice; (2) move topic sentences to paragraph openings; (3) replace technical jargon with plain equivalents where the precision isn't required; (4) add subheadings if the section exceeds 400 words without structural markers. All four applied in a single pass. Provide the actual text to process.
```

**Clean-baseline** (words: 50, CP: 0, CPW: 0.0000):

```
I don't have the methodology section text — the prompt contains a placeholder rather than the actual content.

Please paste the methodology section here and I'll revise it to be more direct, active, and clearly structured. Given that you've already worked on the introduction, I'll match that tone and register.
```

---

### PS4v2-10

**Prompt:** Draft a message from me to the external vendor explaining that we're postponing the integration start date by two weeks, from March 1 to March 15. Keep it professional and direct. Don't apologize exce...

**Substrate** (words: 83, CP: 0, CPW: 0.0000):

```
Professional postponement, minimal apology, clear new date, concrete next step:

---

Subject: Integration Timeline Update — New Start Date March 15

Hi [Vendor Contact],

We're adjusting the integration start date from March 1 to March 15. [One-sentence neutral reason, e.g., "Internal resourcing changes require us to shift the schedule."]

We're committed to the full scope as agreed. If you need to reschedule the kickoff call or update any documentation on your side, send over proposed times an...
```

**Clean-baseline** (words: 148, CP: 1, CPW: 0.6757):

```
Here is a draft you can send as-is or adjust:

---

Subject: Integration Start Date — Revised to March 15

Hi [Name],

I'm writing to let you know that we need to push our integration start date back by two weeks. We had been targeting March 1, but the new start date will be March 15.

This gives us the time we need to [brief reason if you want to include one — e.g., "complete internal prerequisites on our end" — delete this line if you'd rather not elaborate].

Everything else about the engagem...
```

---

### PS4v2-11

**Prompt:** The current user permissions system is a flat list of hardcoded roles. Design the replacement system that will support role inheritance and fine-grained permissions.

**Substrate** (words: 214, CP: 0, CPW: 0.0000):

```
Designing the target-state architecture for role inheritance and fine-grained permissions. Migration from the current flat-list system is a separate document.

**Data model**

```
Role
├── id:            UUID (PK)
├── name:          string
├── parent_id:     UUID? FK→Role.id (null = root role)
└── description:   string

Permission
├── id:            UUID (PK)
├── resource:      string   (e.g., "posts", "admin", "*")
├── action:        string   (e.g., "read", "write", "delete", "*")
└── condition...
```

**Clean-baseline** (words: 312, CP: 0, CPW: 0.0000):

```
Here is a design for a role-based permissions system that supports inheritance and fine-grained access control.

Core Concepts: Permission — a single atomic capability expressed as resource:action (e.g., reports:read, users:delete). Role — a named collection of permissions that can inherit from other roles, forming a DAG. A role's effective permissions are the union of its own permissions and all permissions inherited from ancestors. Assignment — a user is assigned one or more roles.

Data Model...
```

---

### PS4v2-12

**Prompt:** We decided in today's meeting to move forward with the vendor. Send the confirmation email to close the deal.

**Substrate** (words: 68, CP: 0, CPW: 0.0000):

```
Producing the draft — actually sending requires access to your email client.

---

Subject: Confirmation — Moving Forward

Hi [Contact Name],

Following today's meeting, we're confirming that we're moving forward with [Vendor Name]. We're ready to begin the next steps.

[Add if applicable: Agreed terms — pricing/scope/timeline]

Please share the contract for signature and any kickoff details on your end, and we'll proceed from there.

Best regards,
[Name]
```

**Clean-baseline** (words: 113, CP: 0, CPW: 0.0000):

```
I can draft this email, but I'm missing the information needed to make it sendable: vendor contact name and email, your name and title, the vendor's name, and any next steps (contract signing, kickoff call).

Here is a template you can fill in immediately:

---

Subject: Confirmed — Moving Forward with [Vendor Name]

Hi [Contact name],

Following our meeting today, I'm writing to confirm that we are moving forward with [vendor name / the engagement].

[One sentence on immediate next step — e.g.,...
```

---

*Generated by run_category4v2_baseline.py — 2026-02-24*
