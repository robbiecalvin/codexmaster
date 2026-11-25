# [Application name] — Roadmap and Next Steps

**Owner** [Role]  
**Scope and revision** [Milestone or version]  
**Status and review date** [Draft / Approved / Verified, date]

Complete each applicable section with project-specific values and evidence. The detailed reference material describes an illustrative marketplace. Adapt its actors, rules, tools, limits, and workflows to your project. Mark inapplicable sections with a short reason. Treat unapproved choices as proposed or pending.

## Quick-start worksheet

**Owner and review date** [Role, date]  
**Current milestone** [Phase and target]

### Current position and immediate action

Summarize the last verified result, the artifact or environment where it was verified, and the evidence. Identify the next actionable task, its owner, and each blocker. Keep completed work traceable to evidence. Use this section as the resumable checkpoint described in the [State Manager](../workflow/state_manager.md#save-a-checkpoint).

| Checkpoint field | Record |
| --- | --- |
| Objective and acceptance criteria | [Current deliverable and definition of done] |
| Status and scope | [Status, relevant files, and revision or environment] |
| Last verified result | [What was checked, observed result, and evidence] |
| Remaining checks or blockers | [Outstanding work, owner if known, and linked decision IDs] |
| Next action | [First unfinished action and owner] |

### Roadmap

Adapt the phases to the release. For each phase, record the definition of done and the smallest deployable result.

| Phase | Outcome and deliverables | Dependencies and decisions | Acceptance evidence | Deployable result |
| --- | --- | --- | --- | --- |
| Definition and feasibility | [Scope, constraints, provider feasibility] | [Decision IDs] | [Approved requirements] | [Result] |
| Repository and design foundation | [Build, shared UI, first preview] | [Tooling and hosting] | [Build and design review] | [Result] |
| Public entry and discovery | [Entry, navigation, policies, discovery] | [Content and eligibility] | [Page and access checks] | [Result] |
| Accounts and access | [Identity, permissions, restricted paths] | [Identity and policy decisions] | [Allowed and denied cases] | [Result] |
| Core workflows | [Profiles, publishing, transactions, communications as applicable] | [Services, data and business rules] | [Workflow and integration tests] | [Result] |
| Operations and launch | [Moderation, recovery, support, staged release] | [Operational owners and prerequisites] | [Launch acceptance] | [Result] |

### Active work

| Priority | Work item | Owner | Implementation | Verification | Visual review | Integration | Delivery | Next action or blocker |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Now / Soon / Later] | [Task or document] | [Role] | [Status] | [Status and evidence] | [Status or N/A] | [Status or N/A] | [Environment and revision] | [Action or decision] |

### Scope and updates

Record deferred work, explicitly excluded features, and decisions that must precede dependent work. Update the roadmap after scope decisions, verification, or delivery. Link detailed requirements and evidence from the active row.

[Project Context](project_context.md) · [Decision Register](decisions.md) · [Launch Acceptance](launch_acceptance.md)

## Detailed template

Use these fields for the detailed records in this document.

| Outcome and owner | Work and dependencies | Acceptance | Deployable result | Status and evidence | Blocker or next action |
| --- | --- | --- | --- | --- | --- |
| [Fill in] | [Fill in] | [Fill in] | [Fill in] | [Fill in] | [Fill in] |

### 1. Purpose

Record the actual release, what is applicable today, what remains proposed or deferred, and the latest supporting reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Track the current phase, implementation progress, review status,
dependencies, and next actions for [Application name].

This is the authoritative roadmap.

Do not maintain a competing task list elsewhere.

Detailed requirements, design decisions, and financial rules belong
in their dedicated documents.

### 2. Current Position

Record the actual release, what is applicable today, what remains proposed or deferred, and the latest supporting reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Current phase: Phase 0 — Project definition and documentation.

Current activity:
Preparing [Application name]-specific instructions and project documents.

Known status:

- Product name selected: [Application name].
- Current release defined as a platonic social provider marketplace.
- Page-by-page visual collaboration established.
- Initial architecture documentation drafted in conversation.
- Repository saving and implementation status not yet verified.
- No working application or live integration verified in this record.

Do not mark documents as installed merely because their contents
were supplied in chat.

### 3. Immediate Next Action

List the actors, allowed actions, restricted fields, enforcement points, and what happens when access is denied, expires, or is revoked.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Continue preparing the requested project documents one at a time.

Next document:

docs/product/product_spec.md

After the documentation set is prepared:

1. Verify which files are actually present in the app repository.
2. Check links and resolve conflicting framework instructions.
3. Confirm the foundational decisions required for setup.
4. Establish the development environment.
5. Begin the shared design and first-page questionnaire.

Do not begin generating the entire application automatically.

### 4. Documentation Preparation

For **documentation preparation**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Status definitions:

- Draft supplied: content provided in conversation.
- Not yet supplied: content still to be prepared.
- Repository verified: file existence and contents inspected.
- Approved: explicitly accepted by [Decision owner].

These statuses are independent.

#### Requested New Documents

For **requested new documents**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

| Path | Draft status | Repository status |
|---|---|---|
| docs/architecture/application_architecture.md | Draft supplied | Not verified |
| docs/architecture/application_diagram.md | Draft supplied | Not verified |
| docs/project_context.md | Draft supplied | Not verified |
| docs/next_steps.md | Current draft supplied | Not verified |
| docs/product/product_spec.md | Not yet supplied | Not verified |
| docs/product/access_matrix.md | Not yet supplied | Not verified |
| docs/product/pricing_and_payments.md | Not yet supplied | Not verified |
| docs/product/booking_lifecycle.md | Not yet supplied | Not verified |
| docs/design/page_inventory.md | Not yet supplied | Not verified |
| docs/design/page_briefs/ | Structure/template not yet supplied | Not verified |
| docs/decisions.md | Not yet supplied | Not verified |
| docs/architecture/data_model.md | Not yet supplied | Not verified |
| docs/security/application_security.md | Not yet supplied | Not verified |
| docs/development/deployment.md | Not yet supplied | Not verified |
| docs/development/launch_acceptance.md | Not yet supplied | Not verified |

Create individual page briefs when their pages enter design.
A directory alone is not a completed deliverable.

#### Framework Adaptations Already Drafted

Record prerequisites, deliverables, owners, dependencies, and the smallest independently verifiable result.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

- Root README.md.
- Root AGENTS.md.
- docs/architecture/environment.md.
- docs/architecture/repo_map.md.
- docs/design/design_system.md.
- docs/design/design_memory.md.
- docs/development/developer_workflow.md.
- docs/workflow/state_manager.md.
- docs/workflow/task_template.md.
- docs/development/code_style.md.

Their installation in the app repository remains unverified.

Update this section after checking actual files.

### 5. Status Tracking

Record the actual release, what is applicable today, what remains proposed or deferred, and the latest supporting reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

For meaningful work, distinguish:

#### Implementation

For **implementation**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

- Not started.
- In progress.
- Implemented.

#### Verification

Record scenario IDs, observable pass and fail conditions, the tested environment, actual results, evidence, and who accepts exceptions.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

- Not checked.
- Partially checked.
- Passed relevant checks.
- Failed.
- Blocked.

#### Visual Review

For **visual review**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

- Not requested.
- Awaiting review.
- Changes requested.
- Approved.

#### Integration

For **integration**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

- Not connected.
- Synthetic demo.
- Test-mode integration.
- Live integration.

#### Delivery

Record prerequisites, deliverables, owners, dependencies, and the smallest independently verifiable result.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

- Local only.
- Committed.
- Pushed.
- Deployed to preview.
- Deployed to production.
- Failed deployment.

Use only the dimensions relevant to the task.

Never infer production readiness from a completed layout.

### 6. Phase 0 — Definition and Feasibility

Record prerequisites, deliverables, owners, dependencies, and the smallest independently verifiable result.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Status: In progress.

#### Outcomes

For **outcomes**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

- Project documents prepared and installed.
- Requirements distinguished from proposals.
- Foundational decisions recorded.
- Service feasibility understood.

#### Required Work

Record prerequisites, deliverables, owners, dependencies, and the smallest independently verifiable result.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

- Finish the requested documentation set.
- Verify root instructions and relative links.
- Identify conflicting inherited framework rules.
- Confirm launch region and currency.
- Confirm initial account and provider model.
- Select a suitable development and hosting direction.
- Assess payment-provider suitability for the actual product.
- Record unresolved commercial rules.

#### Decisions Needed Before Dependent Work

Record the unresolved question, viable options, decision owner, required evidence, and work blocked by the decision.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

- Backend and hosting selection before infrastructure integration.
- Currency and payment rules before live checkout.
- Initial visual direction before page styling.
- Deposit interpretation before booking-payment implementation.

#### Acceptance

Record scenario IDs, observable pass and fail conditions, the tested environment, actual results, evidence, and who accepts exceptions.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Relevant files are present and internally consistent.
Open questions are explicit.
No selected provider is falsely described as configured.

#### Deployable Result

Record prerequisites, deliverables, owners, dependencies, and the smallest independently verifiable result.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Documentation only.
No production functionality implied.

### 7. Phase 1 — Repository and Design Foundation

Record prerequisites, deliverables, owners, dependencies, and the smallest independently verifiable result.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Status: Not started.

Dependencies: Relevant Phase 0 decisions.

#### Deliverables

Record prerequisites, deliverables, owners, dependencies, and the smallest independently verifiable result.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

- Understandable application structure.
- Verified local preview process.
- Selected runtime/tooling configuration.
- Shared design tokens.
- Reusable navigation and footer foundation.
- Environment configuration templates.
- Relevant automated checks.
- Deployment configuration where selected.

#### Visual Process

For **visual process**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Ask only the initial shared questions needed to start:

- Colour direction.
- Typography.
- Navigation.
- Content density.
- Brand assets.
- Mobile priorities.

Provisional decisions are permitted when [Decision owner] delegates them.

#### Acceptance

Record scenario IDs, observable pass and fail conditions, the tested environment, actual results, evidence, and who accepts exceptions.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

The project runs through documented commands.
Shared components render.
Secrets are excluded.
The initial frontend can be reviewed.

#### Deployable Result

Record prerequisites, deliverables, owners, dependencies, and the smallest independently verifiable result.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

A frontend foundation in an appropriate preview environment.
No real accounts or payments unless separately implemented.

### 8. Phase 2 — Entrance and Public Discovery

Record prerequisites, deliverables, owners, dependencies, and the smallest independently verifiable result.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Status: Not started.

Dependencies: Shared foundation and relevant page briefs.

#### Deliverables

Record prerequisites, deliverables, owners, dependencies, and the smallest independently verifiable result.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

- Entrance age gate.
- Homepage/discovery.
- [request listing] results.
- [offer listing] results.
- Listing detail pages.
- Public provider profile presentation.
- Community Guidelines & Boundaries page.
- Essential navigation and not-found handling.

#### Requirements

For **requirements**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

- Ask visual questions before each undesigned page.
- Preserve direct-link destinations through the entrance gate.
- Use clearly identified synthetic fixtures until data is connected.
- Keep restricted information out of public responses.
- Avoid repeated disclaimer sections.

#### Acceptance

Record scenario IDs, observable pass and fail conditions, the tested environment, actual results, evidence, and who accepts exceptions.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Public navigation and filters behave as implemented.
Responsive layouts are inspected.
Age-gate behaviour is checked.
Demo content is not presented as real marketplace activity.

#### Deployable Result

Record prerequisites, deliverables, owners, dependencies, and the smallest independently verifiable result.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

A clearly scoped public prototype or preview.
Not a working paid marketplace.

### 9. Phase 3 — Accounts and Access Boundaries

List the actors, allowed actions, restricted fields, enforcement points, and what happens when access is denied, expires, or is revoked.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Status: Not started.

Dependencies: Selected backend, data model, and access rules.

#### Deliverables

Record prerequisites, deliverables, owners, dependencies, and the smallest independently verifiable result.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

- Registration and sign-in.
- Confirmation and recovery flows where applicable.
- Onboarding.
- Roles and ownership.
- Account settings.
- Member-tier access.
- Backend permissions.
- Initial administrator access controls.

#### Acceptance

Record scenario IDs, observable pass and fail conditions, the tested environment, actual results, evidence, and who accepts exceptions.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Ownership and role checks are verified.
Unauthorized requests are rejected.
Authentication works across configured environments.

#### Deployable Result

Record prerequisites, deliverables, owners, dependencies, and the smallest independently verifiable result.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

An account-enabled test environment.

Public account collection requires appropriate operational
and privacy readiness.

### 10. Phase 4 — Provider Profiles and Publishing

Record prerequisites, deliverables, owners, dependencies, and the smallest independently verifiable result.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Status: Not started.

Dependencies: Accounts, storage, and profile requirements.

#### Deliverables

Record prerequisites, deliverables, owners, dependencies, and the smallest independently verifiable result.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

- Profile editor.
- Up to two provider presentations.
- Media management.
- Experience and rate editor.
- Availability.
- Publishing eligibility.
- Provider dashboard.
- Profile preview and visibility controls.

#### Acceptance

Record scenario IDs, observable pass and fail conditions, the tested environment, actual results, evidence, and who accepts exceptions.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Owners can manage their own information.
Visibility tiers are enforced.
Private originals remain protected.
Presentation ownership is consistent.

#### Deployable Result

Record prerequisites, deliverables, owners, dependencies, and the smallest independently verifiable result.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Profile-management functionality in a test environment.

Paid publishing requires Phase 6 payment integration.

### 11. Phase 5 — Classifieds and Advertising

Record prerequisites, deliverables, owners, dependencies, and the smallest independently verifiable result.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Status: Not started.

Dependencies: Accounts, publishing rules, and listing specifications.

#### Deliverables

Record prerequisites, deliverables, owners, dependencies, and the smallest independently verifiable result.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

- [request listing] editor.
- [offer listing] editor.
- Draft and preview states.
- Post management.
- Expiry.
- Posting allowances.
- Boost allowances.
- Advertising upgrade interfaces.
- Sponsored-placement ordering.

#### Acceptance

Record scenario IDs, observable pass and fail conditions, the tested environment, actual results, evidence, and who accepts exceptions.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Allowances cannot be bypassed through direct requests.
Drafts remain unpublished.
Expiry and boosts follow confirmed rules.
Public ads expose only public information.

#### Deployable Result

Record prerequisites, deliverables, owners, dependencies, and the smallest independently verifiable result.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Listing-management functionality.

Paid upgrades remain test-only until payment integration is verified.

### 12. Phase 6 — Subscriptions and Billing

Record the exact approved rule, calculation basis, timing, authority, and behavior for failures, late events, and retries.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Status: Not started.

Dependencies: Provider suitability, currency, and confirmed financial rules.

#### Deliverables

Record prerequisites, deliverables, owners, dependencies, and the smallest independently verifiable result.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

- Provider publishing payments.
- Individual provider subscriptions.
- User premium membership.
- Advertising purchases.
- Verified payment events.
- Entitlement updates.
- Billing history.
- Cancellation and renewal handling.
- Revenue-allocation records.
- Reconciliation.

#### Acceptance

Record scenario IDs, observable pass and fail conditions, the tested environment, actual results, evidence, and who accepts exceptions.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

- Correct product and account receive entitlements.
- Provider subscriptions remain isolated.
- Failed payments do not grant access.
- Duplicate events do not duplicate allocations.
- Confirmed expiry and refund rules work.
- Browser-edited prices are rejected.

#### Deployable Result

Record prerequisites, deliverables, owners, dependencies, and the smallest independently verifiable result.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

A verified test-mode commercial flow.

Live charging requires operational readiness and explicit release scope.

### 13. Phase 7 — Booking and Deposit Lifecycle

Record the exact approved rule, calculation basis, timing, authority, and behavior for failures, late events, and retries.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Status: Not started.

Dependencies: Confirmed booking policies, availability, and payments.

#### Deliverables

Record prerequisites, deliverables, owners, dependencies, and the smallest independently verifiable result.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

- Booking request form.
- Price estimate.
- Provider review.
- Revisions and acceptance.
- Accepted price snapshots.
- Reservation handling.
- Deposit payment.
- Confirmation.
- Booking history.
- Cancellation and refund workflows.
- Remaining-balance handling.

#### Acceptance

Record scenario IDs, observable pass and fail conditions, the tested environment, actual results, evidence, and who accepts exceptions.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Concurrent requests cannot violate booking constraints.
Material changes require acceptance.
Payment and booking states remain distinct.
Late payments and expired reservations have defined outcomes.

#### Deployable Result

Record prerequisites, deliverables, owners, dependencies, and the smallest independently verifiable result.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

A testable booking flow.

No live booking payments before required policies and operations are ready.

### 14. Phase 8 — Messaging and Calls

Record prerequisites, deliverables, owners, dependencies, and the smallest independently verifiable result.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Status: Not started.

Dependencies: Entitlements, private storage, and selected infrastructure.

#### Deliverables

Record prerequisites, deliverables, owners, dependencies, and the smallest independently verifiable result.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

- Conversations.
- Text messages.
- Photo/video attachments.
- Read receipts.
- Realtime updates.
- Notification preferences.
- Audio calls.
- Video calls.
- Relevant connection and permission states.

#### Acceptance

Record scenario IDs, observable pass and fail conditions, the tested environment, actual results, evidence, and who accepts exceptions.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Membership, subscriptions, and blocks are enforced.
Attachments remain private.
Missed updates can be recovered.
Calling works in the tested browser matrix.
Recording is not enabled by default.

#### Deployable Result

Record prerequisites, deliverables, owners, dependencies, and the smallest independently verifiable result.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Communication features in the verified environment.

Do not describe decorative controls as implemented communication.

### 15. Phase 9 — Reviews and Operations

Record prerequisites, deliverables, owners, dependencies, and the smallest independently verifiable result.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Status: Not started.

Dependencies: Accounts and relevant transaction records.

#### Deliverables

Record prerequisites, deliverables, owners, dependencies, and the smallest independently verifiable result.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

- Booking-linked reviews.
- Reporting.
- Blocking.
- Moderation queue.
- Content and account actions.
- Dispute workflows.
- Earnings and payout visibility.
- Audit records.
- Support tools.

#### Acceptance

Record scenario IDs, observable pass and fail conditions, the tested environment, actual results, evidence, and who accepts exceptions.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Review eligibility is enforced.
Operational permissions are limited appropriately.
Reports do not automatically establish misconduct.
Financial and moderation actions are auditable.

#### Dependency Note

For **dependency note**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Basic reporting, blocking, and moderation must be available before
affected features are opened to real users.

Do not postpone essential protections merely because their full
administration interface appears in this phase.

#### Deployable Result

Record prerequisites, deliverables, owners, dependencies, and the smallest independently verifiable result.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Operational workflows supporting the approved release.

### 16. Phase 10 — Production Readiness

Record prerequisites, deliverables, owners, dependencies, and the smallest independently verifiable result.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Status: Not started.

Dependencies: A defined launch scope and completed prerequisite work.

#### Deliverables

Record prerequisites, deliverables, owners, dependencies, and the smallest independently verifiable result.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

- Launch acceptance review.
- End-to-end permission checks.
- Payment reconciliation checks.
- Browser and device verification.
- Accessibility review.
- Performance checks.
- Monitoring and alerting.
- Backup and recovery verification.
- Production configuration review.
- Support and incident procedures.
- Deployment and rollback verification.

#### Acceptance

Record scenario IDs, observable pass and fail conditions, the tested environment, actual results, evidence, and who accepts exceptions.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

All launch-blocking requirements for the selected release are satisfied
with recorded evidence.

Unresolved limitations are explicit.
[Decision owner] controls the release decision.

#### Deployable Result

Record prerequisites, deliverables, owners, dependencies, and the smallest independently verifiable result.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Only the verified and authorized production release.

### 17. Dependency and Scope Rules

Record the actual release, what is applicable today, what remains proposed or deferred, and the latest supporting reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Phase order may change when dependencies justify it.

Do not:

- Silently remove difficult features.
- Enable live transactions before required policies exist.
- Expose communication without relevant blocking and reporting.
- Assume frontend completion establishes backend readiness.
- Build every page before obtaining visual direction.

If launch scope is reduced:

1. Obtain an explicit scope decision.
2. Record deferred features.
3. Keep them visible in the roadmap.
4. Remove misleading interface claims.
5. Verify the resulting release as a coherent product.

### 18. Current Work Snapshot

Record the actual most recent verified result, the next actionable task, and all unresolved blockers. Replace the illustrative snapshot below.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

- Objective: Prepare the [Application name] documentation set.
- Active document: docs/next_steps.md.
- Implementation status: No application implementation verified.
- Visual review: Global visual direction remains undecided.
- Integration status: No integration verified.
- Delivery status: Draft supplied in conversation; repository status unknown.

#### Last Verified Result

Record scenario IDs, observable pass and fail conditions, the tested environment, actual results, evidence, and who accepts exceptions.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

No application tests, local preview, or deployment checks have been
recorded for the [Application name] build.

#### Next Action

For **next action**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Prepare docs/product/product_spec.md.

#### Current Blockers

Record the actual release, what is applicable today, what remains proposed or deferred, and the latest supporting reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

No blocker prevents continuing the documentation drafts.

Provider and business-rule decisions block dependent implementation,
not the preparation of unrelated documents.

### 19. Updating This Roadmap

For **updating this roadmap**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

After meaningful work:

- Update the relevant phase.
- Record completed outcomes.
- Preserve unresolved dependencies.
- Update the current snapshot.
- Replace stale next actions.
- Reference evidence where useful.

Keep detailed design feedback in page briefs.
Keep financial rules in the payment specification.
Keep confirmed decisions in the decision log.

Do not mark work approved based on silence.

Do not mark files saved, committed, pushed, or deployed without evidence.

### 20. Final Rule

For **final rule**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Keep this roadmap aligned with reality.

The next person or session should be able to identify:

- What is happening now.
- What has actually been completed.
- What still needs review.
- What is blocked.
- What can proceed.
- What should happen next.

