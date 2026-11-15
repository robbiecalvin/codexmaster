# MeetDiscreet — Launch Acceptance

## 1. Purpose and Status

Define the evidence required before releasing MeetDiscreet
to real users and enabling live transactions.

This is an acceptance framework, not a completed launch review.

Initial status:

- Production readiness: Not established.
- Release scope: Not confirmed.
- Application implementation: Not verified.
- Integrations: Not verified.
- Deployment: Not verified.

Do not mark this document complete merely because it exists.

## 2. Related Documents

Read alongside:

- ../../AGENTS.md
- ../project_context.md
- ../next_steps.md
- ../decisions.md
- ../product/product_spec.md
- ../product/access_matrix.md
- ../product/pricing_and_payments.md
- ../product/booking_lifecycle.md
- ../product/content_and_boundaries.md
- ../architecture/application_architecture.md
- ../architecture/environment.md
- ../security/application_security.md
- ./deployment.md

Detailed requirements remain in their authoritative documents.

## 3. Release Scope

Before acceptance begins, record:

- Release identifier.
- Source revision.
- Target environment.
- Intended users and operating region.
- Currency, if payments are enabled.
- Included pages.
- Included features.
- Enabled integrations.
- Deferred features.
- Known limitations.
- Responsible release owner.

Robbie controls the production release decision.

Do not assume every planned feature must launch simultaneously.

If scope is reduced:

- Obtain an explicit scope decision.
- Keep deferred requirements in the roadmap.
- Remove misleading claims and inactive production controls.
- Verify that the resulting product is coherent.
- Retain protections required by the enabled features.

A feature hidden in navigation is not necessarily disabled at the backend.

## 4. Acceptance Statuses

Use:

- Not checked.
- Passed.
- Failed.
- Blocked.
- Not applicable.
- Accepted limitation.

For each material check, record:

- Requirement.
- Method.
- Result.
- Environment.
- Source revision or deployment.
- Evidence reference.
- Remaining limitation.
- Responsible reviewer where relevant.

“Not applicable” requires a reason tied to release scope.

An accepted limitation is not equivalent to a passing check.
It cannot override a launch-blocking security or financial defect.

## 5. Evidence Standards

Use evidence appropriate to the claim:

- Automated tests.
- Direct browser inspection.
- Configuration review.
- Provider test records.
- Deployment results.
- Operational exercises.
- Explicit visual approval.

Do not substitute:

- A self-awarded quality score.
- An architecture diagram.
- A successful build alone.
- A successful Git push.
- A button rendering.
- An unverified provider capability.
- Silence from Robbie.

Passing checks apply to the tested revision and conditions.

Reassess affected checks when code, configuration, providers,
or financial policies change.

## 6. Product and Policy Readiness

For enabled functionality, verify:

- Product descriptions match actual behaviour.
- Prices match the approved catalogue.
- Currency is explicit.
- Subscription products are clearly distinguished.
- Unresolved rules are not silently implemented.
- Current policies describe actual operations.
- Relevant acceptance records identify policy versions.
- Terms, Privacy, Guidelines, and payment information are reachable.
- Support routes exist and work.

Do not imply legal review occurred unless it did.

Any applicable eligibility or operating requirements identified
for the launch region must be resolved before dependent release.

## 7. Design and Page Review

For included pages:

- Relevant page briefs reflect the current direction.
- Robbie’s requested edits are addressed or explicitly tracked.
- Shared components are consistent.
- Desktop and mobile layouts are inspected.
- Intermediate widths remain usable.
- Long text and realistic content do not break layouts.
- Empty, loading, error, and restricted states are handled.
- Navigation and return paths work.

Record visual approval separately from functional verification.

An approved screenshot does not establish backend correctness.

Do not require novelty or unusual layouts as a launch criterion.

## 8. Entrance Age Gate

Verify:

- Gate appears before normal browsing.
- Direct links receive the gate.
- Intended destination is preserved.
- Underlying content cannot be interacted with while active.
- Confirmation retention matches the selected rule.
- Exit works.
- Keyboard and screen-reader interaction is usable.
- Policy routes remain reachable without false confirmation.
- Browser confirmation does not grant backend privileges.

Do not describe entrance self-attestation as verified identity or age.

## 9. Accounts and Sessions

For enabled account features, verify:

- Registration.
- Confirmation where applicable.
- Sign-in.
- Recovery.
- Logout.
- Session expiry and refresh.
- Restricted-account handling.
- Correct redirects in production.
- Appropriate account-enumeration protections.
- Private login details are not publicly exposed.

Verify the selected account eligibility process.

Privileged accounts require the approved stronger protections,
including MFA before production operational access.

## 10. Authorization

Verify at trusted boundaries:

- Anonymous access cannot retrieve member-only information.
- Nonsubscribers cannot retrieve subscriber-only information.
- Companion A’s subscription cannot unlock Companion B.
- Premium membership does not unlock companion communication.
- Ownership cannot be bypassed by changing record identifiers.
- Users cannot assign their own roles or verification.
- Users cannot alter entitlement or payment state.
- Drafts and private records remain restricted.
- Realtime and storage access follow the same intended boundaries.
- Operational capabilities are limited to assigned duties.

Test direct requests, not only interface controls.

## 11. Profiles and Presentations

Verify:

- Required fields follow the approved specification.
- Optional fields remain optional.
- Public/member/subscriber responses expose only permitted fields.
- Owners can manage only their own profiles.
- The two-presentation limit is enforced.
- Presentations remain associated with the correct account.
- Subscription coverage follows the confirmed rule.
- Verification labels match actual checks.
- Publishing visibility follows the confirmed lifecycle.

Do not expose precise private locations or identity documents.

## 12. Media and Uploads

Before enabling uploads, verify:

- File-type checks.
- Size and duration limits.
- Processing and review requirements.
- Failed-upload handling.
- Abandoned-upload cleanup.
- Ownership.
- Storage permissions.
- Safe previews.
- Private-original protection.
- Scoped delivery access.
- Retention and deletion behaviour.

Confirm protected originals are absent from:

- Public Git history.
- Frontend assets.
- Build output.
- Public API responses.
- Search indexes.
- Unrestricted storage URLs.

Document delivery-token expiry and revocation limits.

## 13. Listings and Advertising

For enabled listing features, verify:

- Looking For and Offering creation.
- Draft privacy.
- Preview.
- Publication.
- Editing.
- Removal.
- Expiry.
- Correct public-field restrictions.
- Posting allowances.
- Premium-expiry consequences.
- Publishing eligibility.
- Boost allowance consumption.
- Concurrent boost handling.
- Sponsored-placement ordering.
- Upgrade scope and duration.
- Failure/refund handling for undelivered purchases.

Editing must not create an undocumented free boost.

Boosting must not reset expiry unless explicitly approved.

## 14. Subscriptions and Memberships

Verify each enabled commercial product separately:

- Companion publishing.
- Individual companion subscription.
- Premium user membership.
- Additional ads.
- Boosts.
- Appearance or placement upgrades.

For each:

- Correct purchaser.
- Correct product.
- Correct amount and currency.
- Clear renewal model.
- Correct entitlement.
- Failure handling.
- Cancellation.
- Expiry.
- Refund consequences.
- Appropriate receipt.

Do not treat one successful checkout as verification of every product.

## 15. Payment Integrity

Before live charges, verify:

- Provider suitability for the actual business and region.
- Required merchant and recipient setup.
- Server-calculated prices.
- Explicit currency.
- Correct provider product references.
- Secure credential storage.
- Verified provider events.
- Idempotent processing.
- Out-of-order event handling.
- Recovery from interrupted checkout.
- Reconciliation.
- Refund processing.
- Dispute handling.
- Correct rounding and allocation.

A checkout redirect must not grant paid access by itself.

Test and live modes must be clearly separated.

Live configuration requires its own verification;
test-mode success alone does not establish production readiness.

## 16. Booking Readiness

Before enabling real bookings, resolve the relevant pending policies.

Verify:

- Request eligibility.
- Participant access.
- Experience selection.
- Price estimate.
- Companion acceptance, decline, and revisions.
- Acceptance of material changes.
- Accepted price and policy snapshots.
- Reservation handling.
- Concurrent conflict prevention.
- Deposit collection under the confirmed interpretation.
- Late-payment resolution.
- Confirmation.
- Amendments.
- Cancellation.
- Attendance/completion process.
- Early-ending calculations.
- Non-attendance handling.
- Remaining balance.
- Refund and dispute routes.

Do not enable two-companion bookings until their additional
approval, availability, and financial rules are resolved.

## 17. Financial Records and Payouts

Verify:

- Charges are distinguishable from allocations.
- Allocations reconcile to confirmed source amounts.
- Fees and taxes follow confirmed rules.
- Refunds adjust records correctly.
- Available earnings are not confused with pending allocations.
- Payouts are labelled paid only after confirmation.
- Failed or reversed payouts can be handled.
- Operational adjustments require authorization.
- Receipts reflect actual transactions.
- Historical prices and accepted agreements are preserved.

No informal editable balance may serve as the sole financial authority.

## 18. Messaging and Calls

For enabled communication, verify:

- Conversation membership.
- Relevant subscription checks.
- Blocking.
- Historical access rules.
- Message persistence.
- Recovery of missed updates.
- Attachment authorization.
- Read-receipt permissions.
- Rate limits.
- Notification privacy.

For calls, additionally verify:

- Authorized initiation and acceptance.
- Scoped credentials.
- Device permission handling.
- Decline and missed-call states.
- Connection and disconnect handling.
- Tested browser compatibility.
- No recording by default.

Do not launch decorative call controls as functioning calls.

## 19. Reporting, Blocking, and Moderation

Before exposing affected features to real users, verify:

- Reporting works without paid access.
- Appropriate support exists for people unable to sign in.
- Blocking is enforced on the backend.
- Existing obligations remain manageable after blocking.
- Report evidence is restricted appropriately.
- Staff capabilities are assigned.
- Consequential actions are recorded.
- Review or appeal handling is defined where applicable.
- Financial consequences of enforcement are confirmed.
- Reporter identity is not disclosed automatically.

A report must not automatically be treated as an established finding.

## 20. Reviews

If reviews are enabled, verify:

- Eligibility comes from the confirmed booking rule.
- Unrelated accounts cannot submit verified-booking reviews.
- Duplicate-review rules work.
- Presentation association is correct where required.
- Responses and edits follow policy.
- Reporting and moderation work.
- Sensitive booking information is not exposed.

Do not fabricate reviews or verification labels to populate launch pages.

## 21. Accessibility and Browser Coverage

Define the supported browser/device matrix.

Record actual tested versions and conditions.

Check relevant:

- Semantic structure.
- Labels.
- Keyboard navigation.
- Visible focus.
- Dialog focus handling.
- Error associations.
- Contrast.
- Touch interaction.
- Text scaling.
- Reduced motion.
- Media controls.
- Mobile navigation.

Assess intended coverage across desktop browsers, iOS Safari,
and Android Chrome.

Do not claim complete accessibility or universal compatibility
based on a limited inspection.

## 22. Performance and Reliability

Set relevant performance budgets using representative pages,
devices, and network conditions.

Verify:

- Public pages remain usable while loading.
- Images and video previews are appropriately delivered.
- Large galleries do not block the whole interface.
- Queries and pagination are bounded.
- Errors do not create endless retry loops.
- Duplicate submissions are handled.
- External-service failures produce recoverable states.
- Important background work can recover after interruption.

Record observed results rather than invented performance claims.

## 23. Deployment and Configuration

Verify the actual production deployment:

- Correct source revision.
- Correct build output.
- Correct environment configuration.
- HTTPS.
- Domain.
- Direct routes.
- Asset paths.
- Authentication callbacks.
- Backend endpoints.
- Storage policies.
- Payment mode.
- Webhook destinations.
- Realtime/calling configuration.
- Scheduled jobs.
- Relevant security headers.

A successful frontend deployment does not establish integration readiness.

Follow deployment.md for release and recovery procedures.

## 24. Operations and Recovery

Before production, verify:

- Monitoring and error visibility.
- Payment reconciliation responsibility.
- Support ownership.
- Incident response process.
- Privileged-access management.
- Backup coverage.
- Restoration procedure.
- Appropriate recovery exercise.
- Release rollback or forward-correction procedure.

Document who handles failures and how.

Do not claim backups or monitoring exist merely because a provider
offers those features.

## 25. Launch-Blocking Findings

Do not release affected functionality with known defects that allow:

- Account takeover.
- Unauthorized private-data access.
- Privilege escalation.
- Secret exposure.
- Public retrieval of protected media.
- Client-controlled financial authority.
- Duplicate charges or allocations without safe resolution.
- Unverified payment-based entitlements.
- Uncontrolled conflicting booking confirmation.
- Unauthorized operational actions.

Also block dependent features when required financial or access
policies remain unresolved.

Evaluate other findings by concrete impact and release scope.

A disclaimer does not resolve a technical or operational blocker.

## 26. Deferred Features and Accepted Limitations

For each deferred feature, record:

- What is excluded.
- Why.
- Whether the interface exposes it.
- Backend disablement where necessary.
- Dependencies.
- Future roadmap reference.

For each accepted limitation, record:

- Exact limitation.
- User impact.
- Evidence.
- Mitigation.
- Owner.
- Review trigger.

Do not label an essential security requirement optional merely
to meet a release date.

## 27. Release Record

Create a record for each production release.

Suggested format:

- Release:
- Source revision:
- Deployment:
- Environment:
- Scope:
- Review date:
- Product owner:
- Relevant checks passed:
- Failed or blocked checks:
- Deferred features:
- Accepted limitations:
- Recovery approach:
- Release decision:
- Authorization reference:
- Post-deployment result:

Use actual facts.
Do not prepopulate a passing outcome.

## 28. Final Release Decision

Possible outcomes:

- Not ready.
- Ready for restricted preview.
- Ready for explicitly scoped production release.
- Released and awaiting post-deployment verification.
- Released and verified for recorded scope.

Readiness and authorization are separate.

Codex reports the evidence and unresolved issues.
Robbie controls the release decision.

Follow authorization already established for the defined release.
Do not invent unnecessary additional permission checkpoints.

## 29. Post-Launch Review

After release:

- Perform relevant deployed smoke checks.
- Inspect operational failures.
- Reconcile consequential transactions.
- Confirm background jobs run.
- Track support issues.
- Reassess known limitations.
- Update the roadmap with observed work.

Do not invent automatic monitoring or future follow-up.
Only scheduled or implemented processes operate without another task.

## 30. Final Rule

Launch a defined, verified product.

Keep evidence specific to the revision and environment.
Keep unresolved blockers visible.
Distinguish readiness, authorization, deployment, and verification.