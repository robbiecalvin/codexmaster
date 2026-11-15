# MeetDiscreet — Application Diagrams

## 1. Purpose

These diagrams describe MeetDiscreet’s intended application structure
and critical interaction flows.

They show logical responsibilities, not selected providers or
verified deployments.

Read alongside:

- [Application Architecture](./application_architecture.md)
- [Environment](./environment.md)
- [Data Model](./data_model.md)
- [Access Matrix](../product/access_matrix.md)
- [Pricing and Payments](../product/pricing_and_payments.md)
- [Booking Lifecycle](../product/booking_lifecycle.md)

Some referenced documents may be created later.

## 2. Diagram Status

Current status: proposed architecture.

Not yet established:

- Backend provider.
- Database and storage services.
- Authentication provider.
- Payment provider.
- Realtime service.
- Calling infrastructure.
- Production hosting.

A diagram does not establish that a feature works.

Update these diagrams when implementation decisions change.
Keep vendor names out until providers are selected.

## 3. Application Topology

```mermaid
flowchart TD
    Browser["Browser frontend"]
    Host["Frontend hosting"]
    Auth["Authentication"]
    API["Trusted application backend"]
    DB["Database"]
    Storage["Media storage"]
    Payments["Payment provider"]
    Realtime["Realtime service"]
    Calls["Calling infrastructure"]
    Jobs["Background processing"]

    Host -->|"HTML, CSS, JavaScript"| Browser
    Browser <-->|"Session lifecycle"| Auth
    Browser -->|"Authenticated requests"| API
    API -->|"Session validation"| Auth
    API <-->|"Records and constraints"| DB
    API -->|"Authorize media access"| Storage
    Browser <-->|"Scoped media delivery"| Storage
    API <-->|"Payments and verified events"| Payments
    API -->|"Scoped connection authorization"| Realtime
    Browser <-->|"Authorized updates"| Realtime
    API -->|"Scoped call authorization"| Calls
    Browser <-->|"Signaling and media"| Calls
    Jobs <-->|"Pending work and results"| DB
    Jobs -->|"Authorized service operations"| API
```

These components may be supplied by a small number of services.

The diagram does not require separate deployments for every box.

Provider-specific implementations may support direct browser-to-data
requests when trusted server-side policies enforce equivalent permissions.

Document the chosen implementation before introducing that path.

## 4. Trust Boundaries

| Boundary | Responsibility |
|---|---|
| Browser | Display information, collect input, request actions |
| Authentication | Establish identity and session validity |
| Application backend | Validate input, authorize actions, enforce domain rules |
| Database | Persist records and enforce appropriate constraints and policies |
| Storage | Deliver only media permitted by storage policy or scoped access |
| External services | Perform supported payment, messaging, or calling operations |
| Administration | Perform explicitly authorized operational actions |

Anything received from the browser is untrusted.

Client-supplied roles, prices, ownership claims, and entitlement flags
must not establish authority.

## 5. Protected Resource Access

```mermaid
flowchart TD
    Request["Resource request"]
    Identity["Validate session"]
    Rules["Evaluate resource access"]
    Allowed{"Authorized?"}
    Deliver["Return permitted data or scoped access"]
    Deny["Return appropriate denial"]

    Request --> Identity
    Identity --> Rules
    Rules --> Allowed
    Allowed -->|"Yes"| Deliver
    Allowed -->|"No"| Deny
```

Public resources may permit anonymous access.

For restricted resources, evaluate applicable:

- Role.
- Ownership.
- Visibility tier.
- Companion-specific subscription.
- Publishing status.
- Account restrictions.
- Block relationships.

Return only permitted fields.

Do not return restricted content and rely on the frontend to hide it.

## 6. Subscription and Purchase Flow

```mermaid
sequenceDiagram
    participant User as Browser
    participant API as Backend
    participant Pay as Payment provider
    participant DB as Database

    User->>API: Request purchase of identified product
    API->>API: Validate eligibility and determine price
    API->>DB: Record pending purchase
    API->>Pay: Create checkout using idempotency controls
    Pay-->>API: Return checkout reference
    API-->>User: Return checkout destination
    User->>Pay: Complete supported checkout
    Pay->>API: Deliver payment event
    API->>API: Verify authenticity and event relevance
    API->>DB: Record event and apply valid state transition
    User->>API: Request current purchase status
    API->>DB: Read authoritative application state
    API-->>User: Return confirmed or pending result
```

The browser’s return from checkout is not proof of payment.

Event handling must account for:

- Duplicate delivery.
- Out-of-order events.
- Delayed confirmation.
- Failed payments.
- Refunds and disputes.
- Interrupted processing.

Persist enough information to reconcile incomplete operations.

Do not grant entitlements twice when the same event is retried.

## 7. Separate Commercial Entitlements

```mermaid
flowchart TD
    Account["Account"]
    Premium["User premium membership"]
    Subscription["Subscription to a specific companion"]
    Publishing["Companion publishing plan"]

    Account --> Premium
    Account --> Subscription
    Account --> Publishing

    Premium --> Posting["Additional posting and boost benefits"]
    Subscription --> Access["That companion's subscriber access"]
    Publishing --> Visibility["Publishing and Offering eligibility"]
```

These purchases serve different purposes.

Premium user membership does not unlock companion communication.

A companion subscription does not grant access to every companion.

Publishing does not grant administrative permissions.

Treatment of access after publishing expiry remains subject to
the confirmed product rules.

## 8. Booking and Deposit Flow

```mermaid
flowchart TD
    Request["Submit booking request"]
    Review["Companion reviews request"]
    Decision{"Response"}
    Revision["Propose revised details"]
    UserReview{"User accepts revision?"}
    Accepted["Record accepted terms"]
    Payment["Await verified deposit"]
    Confirm["Confirm booking"]
    Closed["Close request"]
    Resolution["Resolve expiry or payment conflict"]

    Request --> Review
    Review --> Decision
    Decision -->|"Decline"| Closed
    Decision -->|"Revise"| Revision
    Decision -->|"Accept"| Accepted
    Revision --> UserReview
    UserReview -->|"Yes"| Accepted
    UserReview -->|"No"| Closed
    Accepted --> Payment
    Payment -->|"Paid and reservation valid"| Confirm
    Payment -->|"Expired or conflicting outcome"| Resolution
```

This is a proposed interaction flow.

The detailed lifecycle must define:

- Reservation creation and expiry.
- Availability checks.
- Concurrent acceptance.
- Material revisions.
- Deposit collection.
- Late payment.
- Cancellation.
- Remaining balance.
- Refunds.
- Early endings.

The proposed single 10% deposit remains pending confirmation.

Do not infer a second booking-request charge from this diagram.

## 9. Booking State and Financial State

Keep these records related but distinct.

| Record | Examples of state |
|---|---|
| Booking | Requested, awaiting acceptance, confirmed, completed, cancelled |
| Payment | Pending, succeeded, failed |
| Refund | Requested, processing, completed, failed |
| Payout | Pending, eligible, paid, held |

Exact state names belong in the booking and payment specifications.

A cancelled booking does not prove a refund completed.

A successful payment does not automatically resolve an expired reservation.

A completed booking does not prove a payout was made.

## 10. Restricted Media Delivery

```mermaid
sequenceDiagram
    participant Browser
    participant API as Backend
    participant DB as Database
    participant Store as Private storage

    Browser->>API: Request protected media
    API->>DB: Check resource, ownership, and access
    DB-->>API: Return applicable access facts
    alt Access permitted
        API->>Store: Obtain scoped delivery access
        Store-->>API: Return delivery reference
        API-->>Browser: Return permitted media access
        Browser->>Store: Retrieve authorized media
        Store-->>Browser: Deliver permitted object
    else Access denied
        API-->>Browser: Return access denial
    end
```

Temporary access may remain usable until expiry, depending on the
selected storage mechanism.

Choose access duration and revocation behaviour deliberately.

Private originals must not appear in:

- Public repository assets.
- Static build output.
- Public metadata.
- Unrestricted API responses.
- CSS-blurred full-resolution images.

Generate safe previews separately where required.

## 11. Messaging Flow

```mermaid
sequenceDiagram
    participant Sender as Sender browser
    participant API as Backend
    participant DB as Database
    participant RT as Realtime service
    participant Receiver as Recipient browser

    Sender->>API: Submit message
    API->>API: Validate session and message
    API->>DB: Check membership, entitlement, and blocks
    DB-->>API: Return authorization facts
    API->>DB: Persist authorized message
    API-->>Sender: Confirm stored message
    API->>RT: Publish authorized update
    RT-->>Receiver: Deliver update on authorized channel
```

Persisting a message and publishing an update can fail independently.

Use a recoverable delivery mechanism appropriate to the selected service.

The recipient must be able to recover missed messages from stored history.

Apply access controls to:

- Conversation history.
- Attachments.
- Read receipts.
- Realtime channels.
- Notifications.

Historical access after subscription expiry remains a product decision.

## 12. Audio and Video Calling

```mermaid
sequenceDiagram
    participant Caller as Caller browser
    participant API as Backend
    participant Call as Calling infrastructure
    participant Recipient as Recipient browser

    Caller->>API: Request call
    API->>API: Check session, entitlement, and blocks
    API->>Call: Create authorized call session
    Call-->>Recipient: Deliver authorized invitation
    Recipient->>API: Accept call
    API->>API: Validate recipient and current call state
    API->>Call: Authorize accepted connection
    Call-->>Caller: Establish connection
    Call-->>Recipient: Establish connection
```

This diagram abstracts provider-specific signaling and connectivity.

The implementation must handle:

- Permission denial.
- Declined calls.
- Missed calls.
- Expired invitations.
- Disconnects.
- Device changes where supported.
- Session cleanup.

Recheck relevant authorization when actions occur.

No recording is enabled by default.

## 13. Moderation Actions

```mermaid
flowchart TD
    Report["Report submitted"]
    Queue["Authorized moderation queue"]
    Review["Review necessary evidence"]
    Decision{"Outcome"}
    Action["Apply permitted action"]
    Dismiss["Close without action"]
    Audit["Record outcome and audit event"]

    Report --> Queue
    Queue --> Review
    Review --> Decision
    Decision -->|"Action justified"| Action
    Decision -->|"No action"| Dismiss
    Action --> Audit
    Dismiss --> Audit
```

Reports do not automatically establish misconduct.

Limit evidence access to authorized personnel and necessary information.

Suspension and content removal must have defined effects on
existing subscriptions, bookings, and financial obligations.

Do not invent those consequences in implementation.

## 14. Development and Deployment Flow

```mermaid
flowchart TD
    Local["VS Code and local preview"]
    Checks["Relevant checks and diff review"]
    Git["Authorized commit and GitHub push"]
    Deploy["Configured deployment pipeline"]
    Target{"Deployment target"}
    Preview["Preview environment"]
    Production["Production environment"]

    Local --> Checks
    Checks --> Git
    Git --> Deploy
    Deploy --> Target
    Target -->|"Preview configuration"| Preview
    Target -->|"Authorized production release"| Production
```

This diagram describes the intended workflow.

Do not claim a pipeline exists before configuration and verification.

A push does not prove a deployment succeeded.

Production and preview environments require separate appropriate
configuration and data boundaries.

## 15. Documentation Maintenance

Update this file when changes affect:

- Component responsibilities.
- Trust boundaries.
- Payment confirmation.
- Booking transitions.
- Media delivery.
- Realtime communication.
- Deployment topology.

Keep detailed product rules in their authoritative documents.

Do not introduce unsupported vendor-specific behaviour into these diagrams.

## 16. Final Rule

Use diagrams to explain the application clearly.

Keep planned structure separate from implemented infrastructure.
Keep interface access separate from backend authorization.
Keep booking, payment, refund, and payout states distinguishable.