# MeetDiscreet — Roadmap and Next Steps

## 1. Purpose

Track the current phase, implementation progress, review status,
dependencies, and next actions for MeetDiscreet.

This is the authoritative roadmap.

Do not maintain a competing task list elsewhere.

Detailed requirements, design decisions, and financial rules belong
in their dedicated documents.

## 2. Current Position

Current phase: Phase 0 — Project definition and documentation.

Current activity:
Preparing MeetDiscreet-specific instructions and project documents.

Known status:

- Product name selected: MeetDiscreet.
- Current release defined as a platonic social companion marketplace.
- Page-by-page visual collaboration established.
- Initial architecture documentation drafted in conversation.
- Repository saving and implementation status not yet verified.
- No working application or live integration verified in this record.

Do not mark documents as installed merely because their contents
were supplied in chat.

## 3. Immediate Next Action

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

## 4. Documentation Preparation

Status definitions:

- Draft supplied: content provided in conversation.
- Not yet supplied: content still to be prepared.
- Repository verified: file existence and contents inspected.
- Approved: explicitly accepted by Robbie.

These statuses are independent.

### Requested New Documents

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
| docs/product/content_and_boundaries.md | Not yet supplied | Not verified |
| docs/design/page_inventory.md | Not yet supplied | Not verified |
| docs/design/page_briefs/ | Structure/template not yet supplied | Not verified |
| docs/decisions.md | Not yet supplied | Not verified |
| docs/architecture/data_model.md | Not yet supplied | Not verified |
| docs/security/application_security.md | Not yet supplied | Not verified |
| docs/development/deployment.md | Not yet supplied | Not verified |
| docs/development/launch_acceptance.md | Not yet supplied | Not verified |

Create individual page briefs when their pages enter design.
A directory alone is not a completed deliverable.

### Framework Adaptations Already Drafted

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

## 5. Status Tracking

For meaningful work, distinguish:

### Implementation

- Not started.
- In progress.
- Implemented.

### Verification

- Not checked.
- Partially checked.
- Passed relevant checks.
- Failed.
- Blocked.

### Visual Review

- Not requested.
- Awaiting review.
- Changes requested.
- Approved.

### Integration

- Not connected.
- Synthetic demo.
- Test-mode integration.
- Live integration.

### Delivery

- Local only.
- Committed.
- Pushed.
- Deployed to preview.
- Deployed to production.
- Failed deployment.

Use only the dimensions relevant to the task.

Never infer production readiness from a completed layout.

## 6. Phase 0 — Definition and Feasibility

Status: In progress.

### Outcomes

- Project documents prepared and installed.
- Requirements distinguished from proposals.
- Foundational decisions recorded.
- Service feasibility understood.

### Required Work

- Finish the requested documentation set.
- Verify root instructions and relative links.
- Identify conflicting inherited framework rules.
- Confirm launch region and currency.
- Confirm initial account and companion model.
- Select a suitable development and hosting direction.
- Assess payment-provider suitability for the actual product.
- Record unresolved commercial rules.

### Decisions Needed Before Dependent Work

- Backend and hosting selection before infrastructure integration.
- Currency and payment rules before live checkout.
- Initial visual direction before page styling.
- Deposit interpretation before booking-payment implementation.

### Acceptance

Relevant files are present and internally consistent.
Open questions are explicit.
No selected provider is falsely described as configured.

### Deployable Result

Documentation only.
No production functionality implied.

## 7. Phase 1 — Repository and Design Foundation

Status: Not started.

Dependencies: Relevant Phase 0 decisions.

### Deliverables

- Understandable application structure.
- Verified local preview process.
- Selected runtime/tooling configuration.
- Shared design tokens.
- Reusable navigation and footer foundation.
- Environment configuration templates.
- Relevant automated checks.
- Deployment configuration where selected.

### Visual Process

Ask only the initial shared questions needed to start:

- Colour direction.
- Typography.
- Navigation.
- Content density.
- Brand assets.
- Mobile priorities.

Provisional decisions are permitted when Robbie delegates them.

### Acceptance

The project runs through documented commands.
Shared components render.
Secrets are excluded.
The initial frontend can be reviewed.

### Deployable Result

A frontend foundation in an appropriate preview environment.
No real accounts or payments unless separately implemented.

## 8. Phase 2 — Entrance and Public Discovery

Status: Not started.

Dependencies: Shared foundation and relevant page briefs.

### Deliverables

- Entrance age gate.
- Homepage/discovery.
- Looking For results.
- Offering results.
- Listing detail pages.
- Public companion profile presentation.
- Community Guidelines & Boundaries page.
- Essential navigation and not-found handling.

### Requirements

- Ask visual questions before each undesigned page.
- Preserve direct-link destinations through the entrance gate.
- Use clearly identified synthetic fixtures until data is connected.
- Keep restricted information out of public responses.
- Avoid repeated disclaimer sections.

### Acceptance

Public navigation and filters behave as implemented.
Responsive layouts are inspected.
Age-gate behaviour is checked.
Demo content is not presented as real marketplace activity.

### Deployable Result

A clearly scoped public prototype or preview.
Not a working paid marketplace.

## 9. Phase 3 — Accounts and Access Boundaries

Status: Not started.

Dependencies: Selected backend, data model, and access rules.

### Deliverables

- Registration and sign-in.
- Confirmation and recovery flows where applicable.
- Onboarding.
- Roles and ownership.
- Account settings.
- Member-tier access.
- Backend permissions.
- Initial administrator access controls.

### Acceptance

Ownership and role checks are verified.
Unauthorized requests are rejected.
Authentication works across configured environments.

### Deployable Result

An account-enabled test environment.

Public account collection requires appropriate operational
and privacy readiness.

## 10. Phase 4 — Companion Profiles and Publishing

Status: Not started.

Dependencies: Accounts, storage, and profile requirements.

### Deliverables

- Profile editor.
- Up to two companion presentations.
- Media management.
- Experience and rate editor.
- Availability.
- Publishing eligibility.
- Companion dashboard.
- Profile preview and visibility controls.

### Acceptance

Owners can manage their own information.
Visibility tiers are enforced.
Private originals remain protected.
Presentation ownership is consistent.

### Deployable Result

Profile-management functionality in a test environment.

Paid publishing requires Phase 6 payment integration.

## 11. Phase 5 — Classifieds and Advertising

Status: Not started.

Dependencies: Accounts, publishing rules, and listing specifications.

### Deliverables

- Looking For editor.
- Offering editor.
- Draft and preview states.
- Post management.
- Expiry.
- Posting allowances.
- Boost allowances.
- Advertising upgrade interfaces.
- Sponsored-placement ordering.

### Acceptance

Allowances cannot be bypassed through direct requests.
Drafts remain unpublished.
Expiry and boosts follow confirmed rules.
Public ads expose only public information.

### Deployable Result

Listing-management functionality.

Paid upgrades remain test-only until payment integration is verified.

## 12. Phase 6 — Subscriptions and Billing

Status: Not started.

Dependencies: Provider suitability, currency, and confirmed financial rules.

### Deliverables

- Companion publishing payments.
- Individual companion subscriptions.
- User premium membership.
- Advertising purchases.
- Verified payment events.
- Entitlement updates.
- Billing history.
- Cancellation and renewal handling.
- Revenue-allocation records.
- Reconciliation.

### Acceptance

- Correct product and account receive entitlements.
- Companion subscriptions remain isolated.
- Failed payments do not grant access.
- Duplicate events do not duplicate allocations.
- Confirmed expiry and refund rules work.
- Browser-edited prices are rejected.

### Deployable Result

A verified test-mode commercial flow.

Live charging requires operational readiness and explicit release scope.

## 13. Phase 7 — Booking and Deposit Lifecycle

Status: Not started.

Dependencies: Confirmed booking policies, availability, and payments.

### Deliverables

- Booking request form.
- Price estimate.
- Companion review.
- Revisions and acceptance.
- Accepted price snapshots.
- Reservation handling.
- Deposit payment.
- Confirmation.
- Booking history.
- Cancellation and refund workflows.
- Remaining-balance handling.

### Acceptance

Concurrent requests cannot violate booking constraints.
Material changes require acceptance.
Payment and booking states remain distinct.
Late payments and expired reservations have defined outcomes.

### Deployable Result

A testable booking flow.

No live booking payments before required policies and operations are ready.

## 14. Phase 8 — Messaging and Calls

Status: Not started.

Dependencies: Entitlements, private storage, and selected infrastructure.

### Deliverables

- Conversations.
- Text messages.
- Photo/video attachments.
- Read receipts.
- Realtime updates.
- Notification preferences.
- Audio calls.
- Video calls.
- Relevant connection and permission states.

### Acceptance

Membership, subscriptions, and blocks are enforced.
Attachments remain private.
Missed updates can be recovered.
Calling works in the tested browser matrix.
Recording is not enabled by default.

### Deployable Result

Communication features in the verified environment.

Do not describe decorative controls as implemented communication.

## 15. Phase 9 — Reviews and Operations

Status: Not started.

Dependencies: Accounts and relevant transaction records.

### Deliverables

- Booking-linked reviews.
- Reporting.
- Blocking.
- Moderation queue.
- Content and account actions.
- Dispute workflows.
- Earnings and payout visibility.
- Audit records.
- Support tools.

### Acceptance

Review eligibility is enforced.
Operational permissions are limited appropriately.
Reports do not automatically establish misconduct.
Financial and moderation actions are auditable.

### Dependency Note

Basic reporting, blocking, and moderation must be available before
affected features are opened to real users.

Do not postpone essential protections merely because their full
administration interface appears in this phase.

### Deployable Result

Operational workflows supporting the approved release.

## 16. Phase 10 — Production Readiness

Status: Not started.

Dependencies: A defined launch scope and completed prerequisite work.

### Deliverables

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

### Acceptance

All launch-blocking requirements for the selected release are satisfied
with recorded evidence.

Unresolved limitations are explicit.
Robbie controls the release decision.

### Deployable Result

Only the verified and authorized production release.

## 17. Dependency and Scope Rules

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

## 18. Current Work Snapshot

- Objective: Prepare the MeetDiscreet documentation set.
- Active document: docs/next_steps.md.
- Implementation status: No application implementation verified.
- Visual review: Global visual direction remains undecided.
- Integration status: No integration verified.
- Delivery status: Draft supplied in conversation; repository status unknown.

### Last Verified Result

No application tests, local preview, or deployment checks have been
recorded for the MeetDiscreet build.

### Next Action

Prepare docs/product/product_spec.md.

### Current Blockers

No blocker prevents continuing the documentation drafts.

Provider and business-rule decisions block dependent implementation,
not the preparation of unrelated documents.

## 19. Updating This Roadmap

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

## 20. Final Rule

Keep this roadmap aligned with reality.

The next person or session should be able to identify:

- What is happening now.
- What has actually been completed.
- What still needs review.
- What is blocked.
- What can proceed.
- What should happen next.