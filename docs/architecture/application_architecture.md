# MeetDiscreet — Application Architecture

## 1. Purpose

This document defines MeetDiscreet’s application boundaries,
component responsibilities, and architectural direction.

It describes the intended system.
It does not establish that components are implemented or operational.

Read alongside:

- ../../AGENTS.md
- ../project_context.md
- ../decisions.md
- ../product/product_spec.md
- ../product/access_matrix.md
- ../product/pricing_and_payments.md
- ./environment.md
- ./data_model.md
- ../security/application_security.md

Some referenced documents may be created later during setup.
Do not claim to have read files that do not exist.

## 2. Product Scope

MeetDiscreet is a marketplace for paid platonic dates and social experiences.

The application connects users and companions through:

- Public Looking For and Offering listings.
- Detailed profiles.
- Tiered information and media access.
- Individual companion subscriptions.
- Direct communication.
- Booking requests.
- Deposits and other agreed booking payments.
- Publishing plans.
- Premium posting benefits.
- Advertising upgrades.
- Reviews and moderation.

The architecture must support these requirements without assuming
every feature launches simultaneously.

Deferred functionality remains recorded in the roadmap.

## 3. Architecture Status

### Established Direction

- HTML, CSS, and JavaScript form the frontend foundation.
- Development takes place in VS Code.
- GitHub stores the source.
- Pages are designed and implemented progressively.
- Shared interface components and design tokens support consistency.
- Production permissions and financial rules require a trusted backend.
- User-uploaded private media must remain outside the public repository.
- GitHub Pages is not the production host for the commercial marketplace.

### Decisions Still Required

- Frontend build tooling.
- Backend provider and runtime.
- Database.
- Authentication provider.
- Object storage.
- Payment and payout provider.
- Production hosting.
- Realtime messaging service.
- Audio/video calling infrastructure.
- Notification delivery.
- Search implementation.
- Background-job infrastructure.

Record selections in ../decisions.md.

Do not introduce a service merely because it appears as a possible option
in earlier discussion.

## 4. Architectural Principles

### Clear Responsibilities

Keep presentation, business rules, persistence, and external integrations
distinguishable.

### Small Operational Footprint

Prefer a coherent backend and established managed services over a collection
of unnecessary microservices.

### Server Authority

The browser presents information and requests actions.
Trusted backend boundaries validate and authorize consequential operations.

### Progressive Delivery

Support useful development increments without misrepresenting prototypes
as production functionality.

### Adaptable Presentation

Shared tokens, components, and page modules must permit later visual edits
without rewriting business logic.

### Explicit Content Policy

Keep category definitions, profile-field definitions, and moderation policies
separate from core marketplace mechanics where practical.

Do not build a speculative universal policy engine.

## 5. Logical Components

The system has these logical components:

| Component | Responsibility |
|---|---|
| Browser frontend | Pages, forms, interface state, and interaction |
| Authentication service | Identity and session lifecycle |
| Application backend | Authorization, domain operations, and orchestration |
| Database | Persistent records, relationships, and constraints |
| Object storage | Uploaded media and attachments |
| Payment integration | Charges, subscriptions, refunds, and payouts |
| Realtime layer | Authorized message and presence updates |
| Calling infrastructure | Audio/video signaling and connectivity |
| Background processing | Expiry, notifications, processing, and reconciliation |
| Administration interface | Authorized moderation and operational workflows |

These are responsibility boundaries, not a requirement for ten separately
deployed services.

A selected provider may supply several components.

## 6. Frontend Architecture

### Structure

Prefer an understandable multipage application.

Use explicit page entry points unless selected tooling provides a clear
reason for another routing approach.

Possible page groups:

- Public discovery.
- Listing detail.
- Companion profiles.
- Authentication and onboarding.
- User workspace.
- Companion workspace.
- Administration.
- Help and policy pages.

Actual page boundaries belong in ../design/page_inventory.md.

### Shared Presentation

Reuse:

- Navigation.
- Footer.
- Entrance age gate.
- Buttons.
- Form controls.
- Listing cards and rows.
- Dialogs and drawers.
- Media viewers.
- Status indicators.
- Loading and error treatments.

The reuse mechanism depends on approved tooling.

Do not maintain separate incompatible copies of the same shared component.

### Browser Modules

Separate:

- Page initialization.
- Shared UI behaviour.
- API access.
- Session integration.
- Feature-specific interface state.
- Formatting utilities.

Browser modules must not contain server credentials.

### Public Content

Public HTML or public API responses may contain only public-tier data.

Do not embed restricted records in HTML, JavaScript fixtures,
page metadata, or public search indexes.

## 7. Backend Architecture

Start with cohesive modules organized around product responsibilities.

Suggested domains:

- Accounts and profiles.
- Companion presentations.
- Experiences and rates.
- Listings and advertising.
- Memberships and entitlements.
- Bookings.
- Payments and revenue allocation.
- Media.
- Conversations and calls.
- Reviews.
- Moderation and support.

Use one deployable backend where practical.

Split services only when demonstrated operational needs justify it.

### Request Processing

Consequential requests should:

1. Validate the session where required.
2. Validate input.
3. Check role, ownership, and entitlement.
4. Apply domain rules.
5. Persist changes atomically where possible.
6. Initiate external work safely.
7. Return a scoped response.
8. Record necessary audit information.

Do not rely on frontend validation for enforcement.

## 8. Authentication and Accounts

Authentication identifies the account.
Authorization determines what that account may do.

Support the approved identity lifecycle:

- Registration.
- Email confirmation where required.
- Sign-in.
- Session refresh.
- Password recovery where applicable.
- Logout.
- Account restriction or suspension.
- Account deletion handling.

Use established authentication facilities.

Roles may include:

- User.
- Companion.
- Moderator.
- Administrator.

Whether one account can act as both user and companion remains a decision
to confirm.

Keep role assignment separate from paid entitlements.

## 9. Entitlements and Authorization

Evaluate access using:

- Authenticated account.
- Role.
- Ownership.
- Resource visibility.
- Companion-specific subscription.
- Publishing state.
- Premium membership.
- Account restrictions.
- Relevant block relationships.

Detailed rules belong in ../product/access_matrix.md.

Core distinctions:

- Premium user membership grants posting benefits.
- A companion subscription unlocks that companion’s defined subscriber access.
- Publishing enables companion profile/listing visibility under approved rules.
- No purchase grants moderation or administrative privileges.

For every protected operation, enforce authorization at the trusted boundary.

Frontend controls reflect access.
They do not establish it.

Define behaviour for expiry, cancellation, refunds, suspension,
and publishing lapse before those paths go live.

## 10. Profiles and Presentations

Keep the account separate from its displayed profile information.

A companion may have up to two presentations under one account.

Presentations may vary in:

- Introduction.
- Photos and videos.
- Style details.
- Experience offerings.
- Rates.

They share:

- Account ownership.
- Verification association.
- Publishing account.
- Enforcement history.

Proposed interpretation:
one companion subscription unlocks both presentations.

This requires confirmation before entitlement implementation.

Record the booked presentation on bookings and relevant reviews.

Do not create unrelated identities that conceal shared ownership.

## 11. Listings and Discovery

Support:

- Looking For posts.
- Offering ads.
- Location-based browsing.
- Activity filters.
- Availability filters where supported.
- Public profile links.
- Chronological ordering.
- Boosts.
- Paid placement.
- Appearance upgrades.

The backend enforces:

- Posting allowances.
- Publishing eligibility.
- Expiry.
- Boost consumption.
- Paid upgrade validity.
- Public-field restrictions.

Define deterministic tie-breaking for listing order.

Do not allow clients to assign their own boosted position,
paid placement, or expiry.

Use simple database-backed discovery initially if it meets requirements.
Introduce a separate search service only when justified.

## 12. Pricing and Commercial Rules

Keep plan definitions and domain calculations centralized.

Detailed prices and financial policies belong in:

../product/pricing_and_payments.md

Distinguish:

- Companion publishing subscriptions.
- Individual companion subscriptions.
- Premium user membership.
- Advertising purchases.
- Booking payments.
- Platform revenue allocations.
- Companion earnings.
- Payouts.

Use:

- Explicit currency.
- Integer minor units.
- Defined rounding.
- Versioned or snapshotted commercial terms where needed.

Never trust browser-submitted totals as authoritative.

The current single 10% booking-deposit interpretation remains proposed
until confirmed.

Do not implement both a request fee and deposit by assumption.

## 13. Payment Integration

Use a suitable provider for the actual operating model and region.

Keep test and live environments separate.

### Purchase Flow

1. Browser requests a purchase.
2. Backend validates account and product eligibility.
3. Backend determines the authoritative price.
4. Backend creates the provider transaction.
5. User completes the provider-supported payment flow.
6. Verified provider events update internal financial state.
7. Entitlements change according to confirmed policy.

A browser redirect is not payment confirmation.

### Event Processing

Verify provider events.

Handle:

- Duplicate delivery.
- Delayed delivery.
- Out-of-order events.
- Failed renewals.
- Refunds.
- Disputes.
- Reconciliation.

Use provider event identifiers and appropriate idempotency controls.

Do not overwrite a newer financial state with an older event.

### External Consistency

Database transactions do not include external payment-provider operations.

Use an appropriate recoverable workflow, such as persisted pending actions,
provider idempotency keys, and reconciliation.

Do not promise atomicity across independent services.

## 14. Booking Architecture

Detailed lifecycle rules belong in:

../product/booking_lifecycle.md

A booking associates:

- User.
- Companion.
- Presentation.
- Requested schedule.
- Venue details.
- Experiences and add-ons.
- Accepted price.
- Relevant policy version.
- Payment references.
- Lifecycle history.

Keep booking status separate from payment and refund status.

### Request Flow

1. Verify subscription and account eligibility.
2. Validate schedule and selected offerings.
3. Calculate an estimate.
4. Submit the request.
5. Allow acceptance, rejection, or revision.
6. Record acceptance of agreed details.
7. Collect the required deposit.
8. Confirm according to the approved payment and reservation rules.

### Scheduling

Prevent conflicting confirmed bookings through trusted concurrency controls.

Do not rely on checking availability only in the browser.

Define reservation expiry and the handling of payments received after expiry.

### Price History

Preserve accepted price snapshots.

Changing a companion’s current rates must not silently rewrite
existing agreements.

Require acceptance of material revisions.

## 15. Media Architecture

Store uploaded media in the selected object-storage service.

Separate:

- Public profile assets.
- Member-tier media.
- Subscriber-tier media.
- Message attachments.
- Operational moderation access.

Restrict originals according to ownership and entitlement.

Use appropriately scoped temporary delivery where supported.

Generate safe previews separately from restricted originals.

Do not:

- Commit uploads to GitHub.
- Place private files in public build output.
- Hide accessible originals behind a blur effect.
- Reuse permanent public URLs for protected attachments.

Define validation, processing, retention, deletion,
and abuse-handling behaviour.

File-processing jobs must not expose unprocessed uploads prematurely.

## 16. Messaging and Presence

Persist conversations and messages with explicit membership.

Authorize:

- Conversation access.
- New message submission.
- Attachment retrieval.
- Read receipts.
- Realtime subscriptions.

Subscription and blocking rules must be enforced on the backend.

Define access to historical messages after subscription expiry.

Treat presence as approximate.

An online indicator does not prove immediate availability or create
an obligation to respond.

Do not leak restricted message previews through notifications.

## 17. Audio and Video Calls

Use approved calling infrastructure.

Responsibilities include:

- Authorized call initiation.
- Authorized signaling.
- Expiring credentials.
- Accept and decline behaviour.
- Connection establishment.
- Relay support where necessary.
- Disconnect and failure handling.
- Call termination.

Frontend controls include:

- Microphone.
- Camera.
- Device permissions.
- End call.
- Relevant connection status.

Do not enable recording by default.

Call availability and browser support must be verified
for the selected implementation.

## 18. Reviews and Moderation

Link review eligibility to qualifying completed bookings.

Define:

- Who can review.
- Which booking is referenced.
- Whether revisions are allowed.
- Companion responses.
- Reporting.
- Moderation outcomes.

Do not fabricate verified-booking labels.

Moderation must support appropriate control over:

- Accounts.
- Profiles.
- Listings.
- Media.
- Reports.
- Reviews.
- Communication-related complaints.

Limit moderator access to necessary information.

Record consequential administrative actions.

## 19. Background Processing

Expected background responsibilities may include:

- Listing expiry.
- Reservation expiry.
- Subscription reconciliation.
- Notification delivery.
- Media processing.
- Payment reconciliation.
- Approved payout-related work.

Choose the actual scheduling and execution mechanism explicitly.

Jobs must be:

- Safe to retry.
- Observable.
- Appropriately authorized.
- Resistant to duplicate processing.

Do not assume scheduled work exists because it is described here.

## 20. Data Boundaries

The database is the source of truth for application records.

The payment provider remains authoritative for provider-side
financial events.

Use internal records to reconcile and interpret those events
according to approved product policy.

The browser may cache suitable data for usability.
It is not the authority for financial or permission state.

Use database constraints and transactional operations for invariants
where practical.

Detailed entities and relationships belong in ./data_model.md.

## 21. Environment and Deployment Boundaries

Maintain separate:

- Local development.
- Preview or staging.
- Production.

Do not connect unrestricted previews to production customer data.

Keep service endpoints and credentials environment-specific.

Public frontend configuration must be intentionally browser-safe.

Server-only credentials must remain outside public source and bundles.

Document actual setup, commands, deployments, and rollback procedures.

## 22. Privacy and Security

Apply security at each trust boundary.

Priorities include:

- Account ownership.
- Subscriber isolation.
- Private media protection.
- Financial integrity.
- Upload handling.
- Session security.
- Administrative access.
- Abuse prevention.
- Sensitive-data minimization.

Do not log private messages, secrets, payment credentials,
or temporary private-media access URLs.

Detailed controls belong in ../security/application_security.md.

## 23. Failure Handling and Observability

Users need clear recoverable errors.
Operators need safe diagnostic evidence.

Distinguish:

- Invalid requests.
- Access denial.
- Scheduling conflict.
- Payment pending.
- External-service failure.
- Unexpected internal failure.

Use correlation identifiers where helpful.

Record significant:

- Payment events.
- Entitlement transitions.
- Booking transitions.
- Job failures.
- Administrative actions.

Avoid excessive or sensitive logging.

Provide reconciliation paths for operations that can partially succeed.

## 24. Architectural Verification

Verify critical boundaries before production use.

Examples:

- Unauthorized requests cannot retrieve restricted data.
- Companion A’s subscription cannot unlock Companion B.
- Browser-edited totals do not alter authoritative prices.
- Duplicate payment events do not duplicate allocations.
- Concurrent booking attempts cannot violate scheduling constraints.
- Expired reservations follow the approved payment-resolution policy.
- Blocked communication is rejected at the backend.
- Private media is excluded from public assets and responses.

Use tests and runtime evidence appropriate to the implementation.

Do not infer production readiness from architecture documentation.

## 25. Evolution Rules

Revise architecture when requirements or evidence justify it.

Before a substantial change:

1. Identify the concrete problem.
2. Inspect the existing implementation.
3. Explain affected boundaries and consumers.
4. Consider migration and operational consequences.
5. Record the decision.
6. Update relevant diagrams and environment documentation.

Do not introduce speculative complexity solely for possible future expansion.

Keep the current release accurate while preserving reasonable separation
between marketplace mechanics and content policy.

## 26. Final Rule

Keep MeetDiscreet understandable.

Use a simple frontend, a clearly authorized backend, explicit domain rules,
private media storage, and verified service integrations.

Document what is planned separately from what has been built and tested.