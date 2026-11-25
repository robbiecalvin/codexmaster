# [Application name] — Decision Register

**Owner** [Role]  
**Scope and revision** [Milestone or version]  
**Status and review date** [Draft / Approved / Verified, date]

Complete each applicable section with project-specific values and evidence. The detailed reference material describes an illustrative marketplace. Adapt its actors, rules, tools, limits, and workflows to your project. Mark inapplicable sections with a short reason. Treat unapproved choices as proposed or pending.

## Quick-start worksheet

### Purpose

Record material decisions and unresolved questions about product scope, design, architecture, access, commercial rules, operations, and release. Link to the authoritative specification and track implementation or verification in [Next Steps](next_steps.md). Link blocked work back to the relevant decision without duplicating its rationale.

### Statuses

- **Confirmed** means the decision owner explicitly selected an option.
- **Proposed** means a recommendation is awaiting a decision.
- **Pending** means the question remains open.
- **Technical constraint** means a documented limitation applies.
- **Superseded** means a later record replaces the decision.

### Decision index

| ID | Topic | Status | Owner | Record or replacement |
| --- | --- | --- | --- | --- |
| [DEC-001] | [Topic] | [Status] | [Role] | [Heading or link] |

### Decision record

Copy this section for every substantial decision. Keep the identifier stable when status changes.

### [DEC-001] [Decision title]

| Field | Value |
| --- | --- |
| Status | [Status] |
| Decision owner | [Person or role] |
| Date | [Known decision date] |
| Scope | [Release, component, or workflow] |
| Dependencies | [Related decisions and prerequisites] |
| Authoritative reference | [Specification or evidence] |
| Replaces or replaced by | [Decision ID when applicable] |

**Question.** [What needs to be decided and why now?]

**Options and tradeoffs.** [Compare feasible choices against cost, risk, constraints, and reversibility.]

**Decision and basis.** [Record the chosen direction or proposal and the evidence behind it.]

**Consequences.** [Identify affected users, data, interfaces, policies, operations, and dependent work.]

**Follow-up and validation.** [Owner, action, and acceptance evidence.]

### Pending questions

| Question | Decision needed by | Owner | Blocked work | Evidence needed |
| --- | --- | --- | --- | --- |
| [Question] | [Date or milestone] | [Role] | [Impact] | [Evidence] |

When resolving a question, record the decision, update the linked specification, and notify affected owners. When replacing a decision, keep the earlier record and link both entries. Log routine local implementation choices with the change unless they create a lasting constraint or tradeoff.

## Detailed template

Use these fields for the detailed records in this document.

| Decision ID and owner | Status | Context and options | Decision and rationale | Dependencies and follow-up | Approval or replacement |
| --- | --- | --- | --- | --- | --- |
| [Fill in] | [Fill in] | [Fill in] | [Fill in] | [Fill in] | [Fill in] |

### 1. Purpose

Record the actual release, what is applicable today, what remains proposed or deferred, and the latest supporting reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Record significant project decisions and unresolved questions.

This register explains which direction currently applies.
It does not establish implementation, testing, or deployment status.

Use alongside:

- [Project reference for AGENTS]
- [Project Context](project_context.md)
- [Next Steps](next_steps.md)
- [Product Spec](product_spec.md)
- [Pricing And Payments](pricing_and_payments.md)
- [Access Matrix](access_matrix.md)
- [Project reference for design system]

Keep detailed rules in their authoritative documents.
Reference them rather than duplicating complete specifications.

### 2. Decision Statuses

Record the actual release, what is applicable today, what remains proposed or deferred, and the latest supporting reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

- Confirmed:
  Explicitly selected by [Decision owner] or retained through an explicit requirement.

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

### 3. Decision Record Format

Record the unresolved question, viable options, decision owner, required evidence, and work blocked by the decision.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

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

### 4. Confirmed Product Direction

#### DEC-001 — Product Name

For **dec-001 — product name**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Status: Confirmed.

Decision:
The product is named [Application name].

Basis:
[Decision owner] explicitly selected the name.

Scope:
Project documentation and future customer-facing branding.

The name does not establish domain ownership, trademark clearance,
or a privacy guarantee.

#### DEC-002 — Current Release Scope

Record the actual release, what is applicable today, what remains proposed or deferred, and the latest supporting reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Status: Confirmed.

Decision:
Build the current release as a marketplace for paid [permitted services]
and social experiences.

Retain the underlying profile, subscription, communication, booking,
publishing, and advertising model.

Basis:
[Decision owner] explicitly requested conversion of the original app model.

Authoritative document:
./product/product_spec.md

#### DEC-003 — Future Scope Adaptability

Record the actual release, what is applicable today, what remains proposed or deferred, and the latest supporting reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Status: Confirmed direction.

Decision:
Keep content definitions and policies reasonably separate from
core marketplace mechanics.

[Decision owner] may independently change the product scope later.

Limits:
This is not authorization to implement unspecified future features.
It does not establish future provider eligibility.

Authoritative documents:
./project_context.md
[Product Specification](product_spec.md)

### 5. Confirmed Design Workflow

#### DEC-004 — Progressive Page Design

Record the actual release, what is applicable today, what remains proposed or deferred, and the latest supporting reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Status: Confirmed.

Decision:
Design and build the application page by page.

Codex asks focused visual questions before implementing an undesigned page.

Do not require every page to be designed upfront.

Authoritative documents:
./design/design_system.md
./development/developer_workflow.md

#### DEC-005 — Revisions Remain Available

For **dec-005 — revisions remain available**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Status: Confirmed.

Decision:
[Decision owner] may revisit and edit any page after it is built or approved.

Earlier approval supplies the current direction.
It does not freeze the design.

#### DEC-006 — Consolidated Boundaries Page

For **dec-006 — consolidated boundaries page**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Status: Confirmed.

Decision:
Keep detailed eligibility and content-boundary explanations
on one standalone Community Guidelines & Boundaries page.

Do not repeat lengthy disclaimers across normal interfaces.

Necessary concise transaction disclosures remain at the relevant action.

Authoritative document:
[Product Specification](product_spec.md)

#### DEC-007 — Entrance Age Gate

For **dec-007 — entrance age gate**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Status: Confirmed requirement.

Decision:
Provide an age gate at the start of normal browsing.

Working implementation direction:
An “I am 18 or older” confirmation with an exit action,
including direct-link coverage and destination preservation.

Still pending:
Retention period and account-level verification process.

### 6. Development Direction

#### DEC-008 — Frontend Foundation

For **dec-008 — frontend foundation**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Status: Confirmed direction.

Decision:
Use HTML, CSS, and JavaScript as the frontend foundation.

Additional tooling may be selected when justified.

Do not assume a large frontend framework is approved.

#### DEC-009 — Editor and Source Control

For **dec-009 — editor and source control**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Status: Confirmed.

Decision:
Support development in VS Code with source maintained in GitHub.

A GitHub repository, local setup, or deployment must not be described
as configured until verified.

#### DEC-010 — Production Hosting

For **dec-010 — production hosting**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Status: Technical constraint; provider selection pending.

Constraint:
GitHub Pages is not the production hosting target for this paid marketplace.

Basis:
GitHub’s documented Pages restrictions on sites primarily facilitating
commercial transactions.

Source:
[Hosting provider policy reference]

Next decision:
Select an appropriate production host supporting the actual application.

Do not infer that a particular alternative host has been approved.

#### DEC-011 — Backend Required

For **dec-011 — backend required**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Status: Technical requirement.

Decision:
Production accounts, permissions, private media, payments, bookings,
and communication require trusted backend services.

Browser state is not authoritative for financial or protected access.

Provider selection remains pending.

### 7. Commercial Model Baseline

#### DEC-012 — Preserve Source Prices

Record the exact approved rule, calculation basis, timing, authority, and behavior for failures, late events, and retries.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Status: Established baseline under the feature-preservation requirement.

Decision:
Retain the source model’s listed amounts unless [Decision owner] explicitly changes them.

Authoritative document:
./product/pricing_and_payments.md

This does not confirm unresolved renewal, refund, tax, or payout policies.

#### DEC-013 — Separate Commercial Products

For **dec-013 — separate commercial products**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Status: Established product requirement.

Decision:
Keep these distinct:

- Provider publishing.
- Individual provider subscriptions.
- Premium user posting membership.
- Advertising purchases.
- Booking payments.

Premium membership does not replace provider subscriptions.
A provider subscription does not include the booked date.

### 8. Proposed Interpretations

#### PROP-001 — Single Booking Deposit

Record the exact approved rule, calculation basis, timing, authority, and behavior for failures, late events, and retries.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Status: Proposed.

Proposal:
Use one [rate] booking deposit after acceptance, credited toward the total.

Allocate:

- [rate] of the deposit to the platform.
- [rate] of the deposit to the provider.

Reason:
The source model refers both to a request fee and a deposit without
clearly establishing whether they are the same charge.

Required confirmation:
One charge or two, collection point, and calculation basis.

Blocks:
Live booking-payment implementation.

Does not block:
Booking-page layout using clearly identified estimates.

#### PROP-002 — Free [request listing] Allowance

For **prop-002 — free [request listing] allowance**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Status: Proposed.

Proposal:
Interpret “one free posting per account” as one active post,
rather than one lifetime post.

Required confirmation:
Allowance interpretation and republication behaviour.

Blocks:
Final allowance enforcement.

#### PROP-003 — Subscription Across Presentations

For **prop-003 — subscription across presentations**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Status: Proposed.

Proposal:
One subscription to a provider unlocks both permitted presentations
under that account.

Required confirmation:
Whether access is account-wide or presentation-specific.

Blocks:
Final entitlement implementation for presentations.

### 9. Pending Foundational Decisions

Record the unresolved question, viable options, decision owner, required evidence, and work blocked by the decision.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

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

### 10. Pending Product and Access Decisions

List the actors, allowed actions, restricted fields, enforcement points, and what happens when access is denied, expires, or is revoked.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

| ID | Subject | Decision required |
|---|---|---|
| OPEN-013 | Combined roles | Whether one account can be user and provider |
| OPEN-014 | User-profile visibility | Public, member, owner, and operational fields |
| OPEN-015 | [request listing] detail | Visibility of full posts |
| OPEN-016 | Publishing expiry | Effects on profiles, ads, subscribers, and bookings |
| OPEN-017 | Premium expiry | Excess posts and unused boosts |
| OPEN-018 | Subscription expiry | Historical messages and existing-booking communication |
| OPEN-019 | Two-provider bookings | Subscriptions, approvals, availability, and management |
| OPEN-020 | Blocking | Effects across discovery, communication, and bookings |
| OPEN-021 | Reviews | Eligibility, timing, responses, and editing |
| OPEN-022 | Verification | Age/identity checks and displayed claims |
| OPEN-023 | Gate retention | How long entrance confirmation is remembered |
| OPEN-024 | Notifications | Channels, preferences, and private-content limits |
| OPEN-025 | Media rules | Types, limits, processing, retention, and deletion |

Use the access matrix for the resulting detailed permissions.

### 11. Pending Financial Decisions

Record the exact approved rule, calculation basis, timing, authority, and behavior for failures, late events, and retries.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

| ID | Subject | Decision required |
|---|---|---|
| OPEN-026 | Renewals | Automatic or manual renewal per product |
| OPEN-027 | Plan changes | Switching, proration, and effective dates |
| OPEN-028 | Failed payments | Retry and grace-period rules |
| OPEN-029 | Allowance periods | Boundaries and carryover |
| OPEN-030 | Included [offer listing] ad | Lifetime and publishing relationship |
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
| OPEN-042 | Paired bookings | Multi-provider financial allocation |

Authoritative detail belongs in pricing_and_payments.md.

Do not enable dependent live charges before the required policy is resolved.

### 12. Pending Booking and Operational Decisions

Record allowed transitions, responsible actors, guards, timeouts, side effects, and conflicts.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

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

### 13. Resolving a Decision

Record the unresolved question, viable options, decision owner, required evidence, and work blocked by the decision.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

When [Decision owner] makes a choice:

1. Update the existing record.
2. Preserve its stable identifier.
3. Record the chosen option and relevant scope.
4. Record the basis and date when known.
5. Update the authoritative specification.
6. Identify affected implementation and verification.
7. Update the roadmap if dependencies change.

A decision is not implemented merely because it is confirmed.

Do not close unrelated questions automatically.

### 14. Changing an Earlier Decision

Record the unresolved question, viable options, decision owner, required evidence, and work blocked by the decision.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

When a new instruction replaces an earlier choice:

- Follow the new instruction within the actual instruction hierarchy.
- Mark the earlier record superseded.
- Reference the replacement.
- Update active guidance.
- Check affected components.

Do not maintain contradictory active decisions.

Do not treat design revision as a failure.

### 15. Recording Routine Technical Choices

Record the unresolved question, viable options, decision owner, required evidence, and work blocked by the decision.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

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

### 16. Final Rule

For **final rule**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Keep confirmed choices, proposals, constraints, and open questions distinct.

Use decisions to unblock work—not to manufacture approval
or create unnecessary permission checkpoints.

