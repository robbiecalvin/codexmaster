# MeetDiscreet — Decision Register

## 1. Purpose

Record significant project decisions and unresolved questions.

This register explains which direction currently applies.
It does not establish implementation, testing, or deployment status.

Use alongside:

- ../AGENTS.md
- ./project_context.md
- ./next_steps.md
- ./product/product_spec.md
- ./product/pricing_and_payments.md
- ./product/access_matrix.md
- ./design/design_system.md

Keep detailed rules in their authoritative documents.
Reference them rather than duplicating complete specifications.

## 2. Decision Statuses

- Confirmed:
  Explicitly selected by Robbie or retained through an explicit requirement.

- Proposed:
  Recommended interpretation awaiting confirmation.

- Pending:
  A decision is required, but no option has been selected.

- Technical constraint:
  A limitation identified through relevant evidence.
  Record its source when relying on it.

- Superseded:
  Replaced by a later decision.

Do not treat a recommendation as confirmed.

Do not treat silence, implementation, or a request for the next document
as approval of every proposed policy.

## 3. Decision Record Format

For a material decision, record:

- Identifier.
- Subject.
- Status.
- Decision or question.
- Basis.
- Scope.
- Dependencies.
- Authoritative document.
- Replacement decision, if superseded.

Record dates only when known.
Do not invent historical approval dates.

## 4. Confirmed Product Direction

### DEC-001 — Product Name

Status: Confirmed.

Decision:
The product is named MeetDiscreet.

Basis:
Robbie explicitly selected the name.

Scope:
Project documentation and future customer-facing branding.

The name does not establish domain ownership, trademark clearance,
or a privacy guarantee.

### DEC-002 — Current Release Scope

Status: Confirmed.

Decision:
Build the current release as a marketplace for paid platonic dates
and social experiences.

Retain the underlying profile, subscription, communication, booking,
publishing, and advertising model.

Basis:
Robbie explicitly requested conversion of the original app model.

Authoritative document:
./product/product_spec.md

### DEC-003 — Future Scope Adaptability

Status: Confirmed direction.

Decision:
Keep content definitions and policies reasonably separate from
core marketplace mechanics.

Robbie may independently change the product scope later.

Limits:
This is not authorization to implement unspecified future features.
It does not establish future provider eligibility.

Authoritative documents:
./project_context.md
./product/content_and_boundaries.md

## 5. Confirmed Design Workflow

### DEC-004 — Progressive Page Design

Status: Confirmed.

Decision:
Design and build the application page by page.

Codex asks focused visual questions before implementing an undesigned page.

Do not require every page to be designed upfront.

Authoritative documents:
./design/design_system.md
./development/developer_workflow.md

### DEC-005 — Revisions Remain Available

Status: Confirmed.

Decision:
Robbie may revisit and edit any page after it is built or approved.

Earlier approval supplies the current direction.
It does not freeze the design.

### DEC-006 — Consolidated Boundaries Page

Status: Confirmed.

Decision:
Keep detailed eligibility and content-boundary explanations
on one standalone Community Guidelines & Boundaries page.

Do not repeat lengthy disclaimers across normal interfaces.

Necessary concise transaction disclosures remain at the relevant action.

Authoritative document:
./product/content_and_boundaries.md

### DEC-007 — Entrance Age Gate

Status: Confirmed requirement.

Decision:
Provide an age gate at the start of normal browsing.

Working implementation direction:
An “I am 18 or older” confirmation with an exit action,
including direct-link coverage and destination preservation.

Still pending:
Retention period and account-level verification process.

## 6. Development Direction

### DEC-008 — Frontend Foundation

Status: Confirmed direction.

Decision:
Use HTML, CSS, and JavaScript as the frontend foundation.

Additional tooling may be selected when justified.

Do not assume a large frontend framework is approved.

### DEC-009 — Editor and Source Control

Status: Confirmed.

Decision:
Support development in VS Code with source maintained in GitHub.

A GitHub repository, local setup, or deployment must not be described
as configured until verified.

### DEC-010 — Production Hosting

Status: Technical constraint; provider selection pending.

Constraint:
GitHub Pages is not the production hosting target for this paid marketplace.

Basis:
GitHub’s documented Pages restrictions on sites primarily facilitating
commercial transactions.

Source:
https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits

Next decision:
Select an appropriate production host supporting the actual application.

Do not infer that a particular alternative host has been approved.

### DEC-011 — Backend Required

Status: Technical requirement.

Decision:
Production accounts, permissions, private media, payments, bookings,
and communication require trusted backend services.

Browser state is not authoritative for financial or protected access.

Provider selection remains pending.

## 7. Commercial Model Baseline

### DEC-012 — Preserve Source Prices

Status: Established baseline under the feature-preservation requirement.

Decision:
Retain the source model’s listed amounts unless Robbie explicitly changes them.

Authoritative document:
./product/pricing_and_payments.md

This does not confirm unresolved renewal, refund, tax, or payout policies.

### DEC-013 — Separate Commercial Products

Status: Established product requirement.

Decision:
Keep these distinct:

- Companion publishing.
- Individual companion subscriptions.
- Premium user posting membership.
- Advertising purchases.
- Booking payments.

Premium membership does not replace companion subscriptions.
A companion subscription does not include the booked date.

## 8. Proposed Interpretations

### PROP-001 — Single Booking Deposit

Status: Proposed.

Proposal:
Use one 10% booking deposit after acceptance, credited toward the total.

Allocate:

- 10% of the deposit to the platform.
- 90% of the deposit to the companion.

Reason:
The source model refers both to a request fee and a deposit without
clearly establishing whether they are the same charge.

Required confirmation:
One charge or two, collection point, and calculation basis.

Blocks:
Live booking-payment implementation.

Does not block:
Booking-page layout using clearly identified estimates.

### PROP-002 — Free Looking For Allowance

Status: Proposed.

Proposal:
Interpret “one free posting per account” as one active post,
rather than one lifetime post.

Required confirmation:
Allowance interpretation and republication behaviour.

Blocks:
Final allowance enforcement.

### PROP-003 — Subscription Across Presentations

Status: Proposed.

Proposal:
One subscription to a companion unlocks both permitted presentations
under that account.

Required confirmation:
Whether access is account-wide or presentation-specific.

Blocks:
Final entitlement implementation for presentations.

## 9. Pending Foundational Decisions

| ID | Subject | Decision required | Blocks |
|---|---|---|---|
| OPEN-001 | Launch region | Initial operating geography | Provider and operational setup |
| OPEN-002 | Currency | Explicit charge and payout currency | Live pricing and checkout |
| OPEN-003 | Domain | Domain selection and ownership | Domain configuration |
| OPEN-004 | Brand assets | Logo and approved references | Relevant visual implementation |
| OPEN-005 | Initial visual direction | Colours, typography, navigation, density | First styled page |
| OPEN-006 | Frontend tooling | Static workflow or justified build tooling | Final local setup |
| OPEN-007 | Backend and database | Services and runtime | Data integration |
| OPEN-008 | Authentication | Provider and supported methods | Account implementation |
| OPEN-009 | Storage | Public/private media infrastructure | Uploaded media |
| OPEN-010 | Production hosting | Suitable host and deployment process | Production deployment |
| OPEN-011 | Payments and payouts | Provider suitability and configuration | Financial integration |
| OPEN-012 | Realtime and calls | Messaging and calling infrastructure | Communication integration |

Do not block document drafting or independent page planning
on unrelated provider decisions.

## 10. Pending Product and Access Decisions

| ID | Subject | Decision required |
|---|---|---|
| OPEN-013 | Combined roles | Whether one account can be user and companion |
| OPEN-014 | User-profile visibility | Public, member, owner, and operational fields |
| OPEN-015 | Looking For detail | Visibility of full posts |
| OPEN-016 | Publishing expiry | Effects on profiles, ads, subscribers, and bookings |
| OPEN-017 | Premium expiry | Excess posts and unused boosts |
| OPEN-018 | Subscription expiry | Historical messages and existing-booking communication |
| OPEN-019 | Two-companion bookings | Subscriptions, approvals, availability, and management |
| OPEN-020 | Blocking | Effects across discovery, communication, and bookings |
| OPEN-021 | Reviews | Eligibility, timing, responses, and editing |
| OPEN-022 | Verification | Age/identity checks and displayed claims |
| OPEN-023 | Gate retention | How long entrance confirmation is remembered |
| OPEN-024 | Notifications | Channels, preferences, and private-content limits |
| OPEN-025 | Media rules | Types, limits, processing, retention, and deletion |

Use the access matrix for the resulting detailed permissions.

## 11. Pending Financial Decisions

| ID | Subject | Decision required |
|---|---|---|
| OPEN-026 | Renewals | Automatic or manual renewal per product |
| OPEN-027 | Plan changes | Switching, proration, and effective dates |
| OPEN-028 | Failed payments | Retry and grace-period rules |
| OPEN-029 | Allowance periods | Boundaries and carryover |
| OPEN-030 | Included Offering ad | Lifetime and publishing relationship |
| OPEN-031 | Appearance upgrades | Thumbnail and styling duration |
| OPEN-032 | Placement ordering | Simultaneous promotions and boosts |
| OPEN-033 | Deposit basis | Which quote components enter the percentage |
| OPEN-034 | Remaining balance | Collector, timing, methods, and platform allocation |
| OPEN-035 | Cancellation | Calculation by actor and timing |
| OPEN-036 | Early ending | Actual time, deposit retention, and expenses |
| OPEN-037 | Non-attendance | Evidence, grace periods, and charges |
| OPEN-038 | Taxes and fees | Responsibility and display |
| OPEN-039 | Rounding | Percentage allocation and remainder handling |
| OPEN-040 | Refunds and disputes | Authority, adjustments, and entitlements |
| OPEN-041 | Payouts | Schedule, holds, failures, and reversals |
| OPEN-042 | Paired bookings | Multi-companion financial allocation |

Authoritative detail belongs in pricing_and_payments.md.

Do not enable dependent live charges before the required policy is resolved.

## 12. Pending Booking and Operational Decisions

| ID | Subject | Decision required |
|---|---|---|
| OPEN-043 | Reservation holds | Start, duration, exclusivity, and expiry |
| OPEN-044 | Response deadlines | Whether and when requests expire |
| OPEN-045 | Late payment | Resolution after reservation expiry or conflict |
| OPEN-046 | Start/completion | How attendance and duration are established |
| OPEN-047 | Amendments | Changes after confirmation and payment adjustments |
| OPEN-048 | Moderation | Capabilities, evidence access, and review process |
| OPEN-049 | Enforcement | Effects on obligations, access, and payouts |
| OPEN-050 | Retention | Application, financial, and moderation records |
| OPEN-051 | Launch scope | Exact features enabled in the initial production release |

## 13. Resolving a Decision

When Robbie makes a choice:

1. Update the existing record.
2. Preserve its stable identifier.
3. Record the chosen option and relevant scope.
4. Record the basis and date when known.
5. Update the authoritative specification.
6. Identify affected implementation and verification.
7. Update the roadmap if dependencies change.

A decision is not implemented merely because it is confirmed.

Do not close unrelated questions automatically.

## 14. Changing an Earlier Decision

When a new instruction replaces an earlier choice:

- Follow the new instruction within the actual instruction hierarchy.
- Mark the earlier record superseded.
- Reference the replacement.
- Update active guidance.
- Check affected components.

Do not maintain contradictory active decisions.

Do not treat design revision as a failure.

## 15. Recording Routine Technical Choices

Codex may resolve reversible implementation details within approved scope.

Record them here only when they materially affect:

- Architecture.
- Dependencies.
- Cost.
- Security.
- Shared conventions.
- Operations.
- Future maintenance.

Do not turn every variable name or spacing adjustment into a decision record.

## 16. Final Rule

Keep confirmed choices, proposals, constraints, and open questions distinct.

Use decisions to unblock work—not to manufacture approval
or create unnecessary permission checkpoints.