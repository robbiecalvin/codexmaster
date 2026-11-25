# [Application name] — Application Architecture

**Owner** [Role]  
**Scope and revision** [Milestone or version]  
**Status and review date** [Draft / Approved / Verified, date]

Complete each applicable section with project-specific values and evidence. The detailed reference material describes an illustrative marketplace. Adapt its actors, rules, tools, limits, and workflows to your project. Mark inapplicable sections with a short reason. Treat unapproved choices as proposed or pending.

## Quick-start worksheet

| Owner | Status | Reviewed |
| --- | --- | --- |
| [Role] | [Proposed / Approved / As built] | [Date] |

### Purpose and product scope

Describe the application, its actors, and the workflows in this release. List deferred capabilities and the constraints that shape the architecture.

### Architectural direction

| Topic | Established direction | Open question or decision |
| --- | --- | --- |
| [Runtime, tenancy, deployment, or other topic] | [Direction and rationale] | [Decision ID] |

State the principles guiding changes. Consider clear component responsibilities, trusted enforcement, operational footprint, progressive delivery, and the content or privacy rules the architecture must support.

### Logical components

| Component | Responsibility | Owns or reads | Interfaces | Failure behavior |
| --- | --- | --- | --- | --- |
| [Client, API, datastore, worker, or provider] | [Responsibility] | [State] | [Protocol and consumers] | [Expected behavior] |

See [Application Diagrams](application_diagram.md).

### Frontend and backend

Describe routes, shared presentation, client state, public content, and accessibility. Describe how the backend authenticates requests, checks permissions, validates inputs, applies business rules, persists state, and returns public or scoped responses.

### Domain workflows

Repeat for each applicable workflow, such as accounts and roles, profiles and discovery, pricing and entitlements, purchases, booking and scheduling, media, messaging and presence, calls, and moderation.

### [Workflow name]

- **Actors and entry points.** [Actor, trigger, and interface]
- **Authority and state.** [Owner, access rules, transitions, and source of truth]
- **Side effects.** [Events, external calls, background jobs, and ordering]
- **Failure and recovery.** [Retries, concurrency, reconciliation, or manual handling]
- **Evidence.** [Diagram, test, or decision]

### Data and environment boundaries

Describe data ownership, sensitive fields, storage, API representations, and which services can access each dataset. Document environment-specific configuration, secret ownership, deployment order, migrations and rollback. See the [Data Model](data_model.md) and [Application Security](application_security.md).

### Observability, verification, and evolution

Document health signals, alert ownership, degraded behavior, recovery objectives, architectural acceptance tests, and rollout evidence. Record tradeoffs and scope changes in the [Decision Register](decisions.md).

## Detailed template

Use these fields for the detailed records in this document.

| Component or workflow | Responsibilities and owner | State and interfaces | Failure and recovery | Decision or evidence |
| --- | --- | --- | --- | --- |
| [Fill in] | [Fill in] | [Fill in] | [Fill in] | [Fill in] |

### 1. Purpose

Record the actual release, what is applicable today, what remains proposed or deferred, and the latest supporting reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

This document defines [Application name]’s application boundaries,
component responsibilities, and architectural direction.

It describes the intended system.
It does not establish that components are implemented or operational.

Read alongside:

- [Project reference for AGENTS]
- [Project Context](project_context.md)
- [Decisions](decisions.md)
- [Product Spec](product_spec.md)
- [Access Matrix](access_matrix.md)
- [Pricing And Payments](pricing_and_payments.md)
- [Project reference for environment]
- [Data Model](data_model.md)
- [Application Security](application_security.md)

Some referenced documents may be created later during setup.
Do not claim to have read files that do not exist.

### 2. Product Scope

Record the actual release, what is applicable today, what remains proposed or deferred, and the latest supporting reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

[Application name] is a marketplace for [permitted services and experiences].

The application connects users and providers through:

- Public [request listing] and [offer listing] listings.
- Detailed profiles.
- Tiered information and media access.
- Individual provider subscriptions.
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

### 3. Architecture Status

#### Established Direction

For **established direction**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

- HTML, CSS, and JavaScript form the frontend foundation.
- Development takes place in VS Code.
- GitHub stores the source.
- Pages are designed and implemented progressively.
- Shared interface components and design tokens support consistency.
- Production permissions and financial rules require a trusted backend.
- User-uploaded private media must remain outside the public repository.
- GitHub Pages is not the production host for the commercial marketplace.

#### Decisions Still Required

Record the unresolved question, viable options, decision owner, required evidence, and work blocked by the decision.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

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

### 4. Architectural Principles

#### Clear Responsibilities

For **clear responsibilities**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Keep presentation, business rules, persistence, and external integrations
distinguishable.

#### Small Operational Footprint

For **small operational footprint**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Prefer a coherent backend and established managed services over a collection
of unnecessary microservices.

#### Server Authority

For **server authority**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

The browser presents information and requests actions.
Trusted backend boundaries validate and authorize consequential operations.

#### Progressive Delivery

Record the actual release, what is applicable today, what remains proposed or deferred, and the latest supporting reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Support useful development increments without misrepresenting prototypes
as production functionality.

#### Adaptable Presentation

For **adaptable presentation**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Shared tokens, components, and page modules must permit later visual edits
without rewriting business logic.

#### Explicit Content Policy

For **explicit content policy**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Keep category definitions, profile-field definitions, and moderation policies
separate from core marketplace mechanics where practical.

Do not build a speculative universal policy engine.

### 5. Logical Components

For **logical components**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

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

### 6. Frontend Architecture

#### Structure

For **structure**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Prefer an understandable multipage application.

Use explicit page entry points unless selected tooling provides a clear
reason for another routing approach.

Possible page groups:

- Public discovery.
- Listing detail.
- Provider profiles.
- Authentication and onboarding.
- User workspace.
- Provider workspace.
- Administration.
- Help and policy pages.

Actual page boundaries belong in ../design/page_inventory.md.

#### Shared Presentation

For **shared presentation**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

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

#### Browser Modules

For **browser modules**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Separate:

- Page initialization.
- Shared UI behaviour.
- API access.
- Session integration.
- Feature-specific interface state.
- Formatting utilities.

Browser modules must not contain server credentials.

#### Public Content

For **public content**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Public HTML or public API responses may contain only public-tier data.

Do not embed restricted records in HTML, JavaScript fixtures,
page metadata, or public search indexes.

### 7. Backend Architecture

For **backend architecture**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Start with cohesive modules organized around product responsibilities.

Suggested domains:

- Accounts and profiles.
- Provider presentations.
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

#### Request Processing

For **request processing**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

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

### 8. Authentication and Accounts

For **authentication and accounts**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

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
- Provider.
- Moderator.
- Administrator.

Whether one account can act as both user and provider remains a decision
to confirm.

Keep role assignment separate from paid entitlements.

### 9. Entitlements and Authorization

List the actors, allowed actions, restricted fields, enforcement points, and what happens when access is denied, expires, or is revoked.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Evaluate access using:

- Authenticated account.
- Role.
- Ownership.
- Resource visibility.
- Provider-specific subscription.
- Publishing state.
- Premium membership.
- Account restrictions.
- Relevant block relationships.

Detailed rules belong in ../product/access_matrix.md.

Core distinctions:

- Premium user membership grants posting benefits.
- A provider subscription unlocks that provider’s defined subscriber access.
- Publishing enables provider profile/listing visibility under approved rules.
- No purchase grants moderation or administrative privileges.

For every protected operation, enforce authorization at the trusted boundary.

Frontend controls reflect access.
They do not establish it.

Define behaviour for expiry, cancellation, refunds, suspension,
and publishing lapse before those paths go live.

### 10. Profiles and Presentations

For **profiles and presentations**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Keep the account separate from its displayed profile information.

A provider may have up to two presentations under one account.

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
one provider subscription unlocks both presentations.

This requires confirmation before entitlement implementation.

Record the booked presentation on bookings and relevant reviews.

Do not create unrelated identities that conceal shared ownership.

### 11. Listings and Discovery

For **listings and discovery**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Support:

- [request listing] posts.
- [offer listing] ads.
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

### 12. Pricing and Commercial Rules

For **pricing and commercial rules**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Keep plan definitions and domain calculations centralized.

Detailed prices and financial policies belong in:

../product/pricing_and_payments.md

Distinguish:

- Provider publishing subscriptions.
- Individual provider subscriptions.
- Premium user membership.
- Advertising purchases.
- Booking payments.
- Platform revenue allocations.
- Provider earnings.
- Payouts.

Use:

- Explicit currency.
- Integer minor units.
- Defined rounding.
- Versioned or snapshotted commercial terms where needed.

Never trust browser-submitted totals as authoritative.

The current single [rate] booking-deposit interpretation remains proposed
until confirmed.

Do not implement both a request fee and deposit by assumption.

### 13. Payment Integration

Record the exact approved rule, calculation basis, timing, authority, and behavior for failures, late events, and retries.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Use a suitable provider for the actual operating model and region.

Keep test and live environments separate.

#### Purchase Flow

For **purchase flow**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

1. Browser requests a purchase.
2. Backend validates account and product eligibility.
3. Backend determines the authoritative price.
4. Backend creates the provider transaction.
5. User completes the provider-supported payment flow.
6. Verified provider events update internal financial state.
7. Entitlements change according to confirmed policy.

A browser redirect is not payment confirmation.

#### Event Processing

For **event processing**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

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

#### External Consistency

For **external consistency**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Database transactions do not include external payment-provider operations.

Use an appropriate recoverable workflow, such as persisted pending actions,
provider idempotency keys, and reconciliation.

Do not promise atomicity across independent services.

### 14. Booking Architecture

Record allowed transitions, responsible actors, guards, timeouts, side effects, and conflicts.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Detailed lifecycle rules belong in:

../product/booking_lifecycle.md

A booking associates:

- User.
- Provider.
- Presentation.
- Requested schedule.
- Venue details.
- Experiences and add-ons.
- Accepted price.
- Relevant policy version.
- Payment references.
- Lifecycle history.

Keep booking status separate from payment and refund status.

#### Request Flow

For **request flow**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

1. Verify subscription and account eligibility.
2. Validate schedule and selected offerings.
3. Calculate an estimate.
4. Submit the request.
5. Allow acceptance, rejection, or revision.
6. Record acceptance of agreed details.
7. Collect the required deposit.
8. Confirm according to the approved payment and reservation rules.

#### Scheduling

For **scheduling**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Prevent conflicting confirmed bookings through trusted concurrency controls.

Do not rely on checking availability only in the browser.

Define reservation expiry and the handling of payments received after expiry.

#### Price History

Record the exact approved rule, calculation basis, timing, authority, and behavior for failures, late events, and retries.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Preserve accepted price snapshots.

Changing a provider’s current rates must not silently rewrite
existing agreements.

Require acceptance of material revisions.

### 15. Media Architecture

List the actors, allowed actions, restricted fields, enforcement points, and what happens when access is denied, expires, or is revoked.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

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

### 16. Messaging and Presence

For **messaging and presence**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

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

### 17. Audio and Video Calls

For **audio and video calls**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

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

### 18. Reviews and Moderation

For **reviews and moderation**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Link review eligibility to qualifying completed bookings.

Define:

- Who can review.
- Which booking is referenced.
- Whether revisions are allowed.
- Provider responses.
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

### 19. Background Processing

For **background processing**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

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

### 20. Data Boundaries

For **data boundaries**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

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

### 21. Environment and Deployment Boundaries

Record prerequisites, deliverables, owners, dependencies, and the smallest independently verifiable result.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Maintain separate:

- Local development.
- Preview or staging.
- Production.

Do not connect unrestricted previews to production customer data.

Keep service endpoints and credentials environment-specific.

Public frontend configuration must be intentionally browser-safe.

Server-only credentials must remain outside public source and bundles.

Document actual setup, commands, deployments, and rollback procedures.

### 22. Privacy and Security

For **privacy and security**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

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

### 23. Failure Handling and Observability

Identify triggers, the accountable operator, the recovery procedure, the last known good state, and a check that confirms recovery.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

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

### 24. Architectural Verification

Record scenario IDs, observable pass and fail conditions, the tested environment, actual results, evidence, and who accepts exceptions.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Verify critical boundaries before production use.

Examples:

- Unauthorized requests cannot retrieve restricted data.
- Provider A’s subscription cannot unlock Provider B.
- Browser-edited totals do not alter authoritative prices.
- Duplicate payment events do not duplicate allocations.
- Concurrent booking attempts cannot violate scheduling constraints.
- Expired reservations follow the approved payment-resolution policy.
- Blocked communication is rejected at the backend.
- Private media is excluded from public assets and responses.

Use tests and runtime evidence appropriate to the implementation.

Do not infer production readiness from architecture documentation.

### 25. Evolution Rules

For **evolution rules**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

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

### 26. Final Rule

For **final rule**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Keep [Application name] understandable.

Use a simple frontend, a clearly authorized backend, explicit domain rules,
private media storage, and verified service integrations.

Document what is planned separately from what has been built and tested.

