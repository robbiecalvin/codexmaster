# [Application name] — Data Model

**Owner** [Role]  
**Scope and revision** [Milestone or version]  
**Status and review date** [Draft / Approved / Verified, date]

Complete each applicable section with project-specific values and evidence. The detailed reference material describes an illustrative marketplace. Adapt its actors, rules, tools, limits, and workflows to your project. Mark inapplicable sections with a short reason. Treat unapproved choices as proposed or pending.

## Quick-start worksheet

**Owner and review date** [Role, date]  
**Status** [Logical design / Approved design / Implemented schema]

### Scope and modelling conventions

Describe the domain, data owners, underlying storage, and version. Specify stable IDs, provider-ID namespaces, dates and time zones, currency precision, timestamps, lifecycle states, tenant scoping, and concurrency controls.

### Entity inventory

Use the groups applicable to the project. Add a detailed entity record for each authoritative concept.

| Domain | Candidate entities to adapt | Questions to settle |
| --- | --- | --- |
| Identity and eligibility | Accounts, roles, preferences, profiles, verification | Which fields are public, and who may grant access? |
| Discovery and catalogue | Locations, categories, listings, revisions, products, prices | What is indexed, versioned, or discoverable? |
| Billing and financial records | Agreements, entitlements, purchases, payment events, refunds, disputes, payouts | Which provider events establish financial state, and how are duplicates handled? |
| Scheduling and commitments | Availability, bookings, quotes, reservations, outcomes | How are conflicts prevented and accepted terms preserved? |
| Files and communication | Media assets, conversations, members, messages, attachments, read receipts, calls | Where are objects stored, and when does access end? |
| Trust and policy | Reviews, blocks, reports, moderation, policy acceptances | Who can see evidence, and how long is it retained? |
| Operations | Notifications, deliveries, jobs, outbox, audit events | How are retries, duplicate events, and privileged actions tracked? |

### Entity record

Copy this section for each entity.

### [Entity name]

**Responsibility and owner** [Purpose, authoritative service, and owner or tenant]  
**Lifecycle** [Valid states, transitions, and terminal behavior]

| Field | Type and nullability | Default | Constraints and relationships | Classification |
| --- | --- | --- | --- | --- |
| [Field] | [Type / Required or optional] | [Default] | [Key, scope, reference, or validation] | [Public / Internal / Restricted] |

**Relationships** [Cardinality, ownership, foreign-key behavior, and delete policy]  
**Invariants** [Uniqueness, transaction boundaries, time bounds, or accounting rules]  
**Access and API views** [Who can read or write, public projection, and restricted fields]  
**Queries and indexes** [Critical query patterns and index rationale]  
**Retention** [Retention trigger, expiry or redaction, legal holds, and audit needs]

### Cross-entity constraints and migration

Describe rules that span records and how they are enforced. Record migration order, compatibility with existing data, backfill, validation, and rollback. Include tests for invalid transitions, duplicate events and concurrent changes where applicable.

### Open decisions

| Question | Affected entities | Owner | Decision |
| --- | --- | --- | --- |
| [Unresolved rule] | [Entities] | [Role] | [Decision ID] |

See [Application Architecture](application_architecture.md), [Application Security](application_security.md), and [Decision Register](decisions.md).

## Detailed template

Use these fields for the detailed records in this document.

| Entity and owner | Fields and types | Access and classification | Keys and relationships | Invariants and lifecycle | Indexes and retention |
| --- | --- | --- | --- | --- | --- |
| [Fill in] | [Fill in] | [Fill in] | [Fill in] | [Fill in] | [Fill in] |

### 1. Purpose and Status

Record the actual release, what is applicable today, what remains proposed or deferred, and the latest supporting reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Describe the logical data model for [Application name].

This is a design specification, not an implemented database schema.

Entity names are proposed.
Adapt them to the selected database while preserving responsibilities,
ownership, relationships, and constraints.

Read alongside:

- [Project reference for AGENTS]
- [Product Spec](product_spec.md)
- [Access Matrix](access_matrix.md)
- [Pricing And Payments](pricing_and_payments.md)
- [Booking Lifecycle](booking_lifecycle.md)
- [Application Architecture](application_architecture.md)
- [Application Security](application_security.md)
- [Decisions](decisions.md)

Unresolved product rules must remain explicit.
Do not encode an assistant recommendation as an approved constraint.

### 2. Modelling Principles

For **modelling principles**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

- Separate identity from public profile information.
- Separate roles from paid entitlements.
- Identify owners and participants explicitly.
- Keep financial history distinct from current catalogue prices.
- Preserve accepted booking agreements.
- Enforce important invariants in trusted storage where practical.
- Keep public and restricted response fields explicit.
- Minimize sensitive data.
- Avoid duplicating authoritative facts.
- Add entities when their responsibility is needed.

These are logical records, not a requirement for one physical table
per heading.

### 3. Common Conventions

For **common conventions**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Use stable internal identifiers.

Provider identifiers must remain distinguishable from internal identifiers.

For relevant records, include:

- id.
- created_at.
- updated_at.
- lifecycle status.
- owner or participant references.
- version where concurrent updates require it.

Store absolute timestamps consistently, normally in UTC.

Use explicit local dates and IANA time zones for scheduling requirements.

Use integer minor units and explicit currency codes for money.

Do not store formatted currency strings as financial authority.

Avoid generic JSON fields for core ownership, money, and relationships.
Use structured fields with enforceable constraints.

JSON may be appropriate for versioned snapshots or bounded metadata.

### 4. Identity and Accounts

#### accounts

Specify stored fields, types, nullability, keys, constraints, access, retention, and dependencies for this record.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Application-level account identity.

Suggested information:

- Internal identifier.
- Authentication-provider subject reference.
- Account lifecycle status.
- Creation and update timestamps.
- Relevant restriction references.
- Deletion-request state where applicable.

Keep public presentation separate.

Do not store plaintext passwords.

If authentication is managed externally, use its supported identity
and credential lifecycle.

#### account_roles

Specify stored fields, types, nullability, keys, constraints, access, retention, and dependencies for this record.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Assigned application roles.

Suggested information:

- Account reference.
- Role.
- Assigned timestamp.
- Assigning authority where applicable.

Prevent duplicate assignments.

Users cannot grant themselves privileged roles.

Whether user and provider roles may coexist remains pending.

#### account_preferences

Specify stored fields, types, nullability, keys, constraints, access, retention, and dependencies for this record.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Private account settings where needed.

Examples:

- Notification preferences.
- Locale.
- Display time zone.
- Privacy choices.

Do not use preferences to establish paid entitlements.

### 5. Profiles and Provider Presentations

#### user_profiles

Specify stored fields, types, nullability, keys, constraints, access, retention, and dependencies for this record.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

User-managed profile information.

Suggested fields:

- Account reference.
- Username.
- Display name.
- General location reference.
- Profile-photo reference.
- Interests.
- Languages.
- What I’m [request listing].
- What I Enjoy.
- Permitted optional fields.

Field visibility remains subject to the access matrix.

Do not publish the entire record through a generic API response.

#### companion_profiles

Specify stored fields, types, nullability, keys, constraints, access, retention, and dependencies for this record.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Provider-level identity and management information.

Suggested fields:

- Owning account.
- Username.
- Display name.
- General location.
- Languages.
- Eligibility association.
- Publishing association.
- Availability preference.
- Profile lifecycle status.

Age-related and other sensitive information must use the approved
eligibility and visibility design.

#### companion_presentations

Specify stored fields, types, nullability, keys, constraints, access, retention, and dependencies for this record.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Up to two presentations per provider account.

Suggested fields:

- Provider reference.
- Presentation slot or equivalent identifier.
- Display content.
- Tagline.
- Preferred date style.
- Biography.
- Interests and preferences.
- Optional story.
- Appearance information.
- Public profile-photo association.
- Lifecycle status.

Enforce the two-presentation limit safely under concurrent requests.

Both presentations share the underlying owner and verification association.

Subscription coverage across presentations remains pending.

#### presentation_partners

Specify stored fields, types, nullability, keys, constraints, access, retention, and dependencies for this record.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Optional links for two-provider offerings.

Suggested fields:

- Source presentation or provider.
- Linked provider.
- Relationship status.
- Any required acknowledgement.

A link is not proof of booking participation or authority to accept
for the other provider.

### 6. Eligibility and Verification

#### verification_records

Record scenario IDs, observable pass and fail conditions, the tested environment, actual results, evidence, and who accepts exceptions.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

References to the approved verification process.

Suggested information:

- Account.
- Verification type.
- Provider reference where applicable.
- Status.
- Checked timestamp.
- Expiry where applicable.
- Restricted review information.

Store the minimum required.

Do not retain identity-document copies by default.
Select collection and retention rules first.

Public badges should derive from permitted verification facts,
not expose underlying documents.

Entrance age confirmation is not equivalent to this record.

### 7. Locations and Discovery

#### locations

Specify stored fields, types, nullability, keys, constraints, access, retention, and dependencies for this record.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

General locations used for discovery.

Possible information:

- Country.
- Region.
- City.
- Approved area label.
- Public geographic representation where needed.

Keep precise booking addresses separate.

Do not add precise home coordinates merely to support city browsing.

#### categories

Specify stored fields, types, nullability, keys, constraints, access, retention, and dependencies for this record.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Approved activity or listing categories.

Suggested information:

- Stable code.
- Display label.
- Description.
- Active status.
- Ordering.

Keep policy-specific labels separate from core marketplace logic
without creating an unnecessary universal taxonomy engine.

### 8. Experiences and Rates

#### experiences

Specify stored fields, types, nullability, keys, constraints, access, retention, and dependencies for this record.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Provider or presentation offerings.

Suggested fields:

- Owning provider/presentation.
- Category.
- Title.
- Description.
- Offered status.
- Included-in-base-rate flag.
- Additional amount.
- Currency.
- Charge basis: one-time or hourly.
- Relevant duration or availability restrictions.

If included in the base rate, additional-charge fields must follow
a consistent enforced representation.

Do not permit contradictory pricing inputs.

#### rate_definitions

Specify stored fields, types, nullability, keys, constraints, access, retention, and dependencies for this record.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Applicable base rates.

Suggested fields:

- Provider or presentation.
- Rate category.
- Amount in minor units.
- Currency.
- Billing unit.
- Minimum duration, if approved.
- Effective or active status.

Historical accepted bookings must not depend on mutable current rates.

#### availability_rules

Specify stored fields, types, nullability, keys, constraints, access, retention, and dependencies for this record.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Recurring or offered availability.

Suggested information:

- Provider.
- Local schedule.
- IANA time zone.
- Effective dates.
- Applicable presentation restrictions where needed.

#### availability_exceptions

Specify stored fields, types, nullability, keys, constraints, access, retention, and dependencies for this record.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Specific unavailable periods or overrides.

Keep these distinct from actual confirmed bookings and reservation holds.

### 9. Product Catalogue and Billing Agreements

#### products

Specify stored fields, types, nullability, keys, constraints, access, retention, and dependencies for this record.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Stable commercial product definitions.

Examples:

- Premium membership.
- Provider publishing.
- Provider subscription.
- Additional ad.
- Boost.
- Placement upgrade.
- Appearance upgrade.

#### prices

Record the exact approved rule, calculation basis, timing, authority, and behavior for failures, late events, and retries.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Versioned price definitions.

Suggested fields:

- Product.
- Amount in minor units.
- Currency.
- Billing interval or unit.
- Active dates.
- Provider price reference.
- Relevant version.

Do not overwrite historical prices referenced by transactions.

#### billing_agreements

Record the exact approved rule, calculation basis, timing, authority, and behavior for failures, late events, and retries.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Recurring or fixed-term purchase associations.

Suggested fields:

- Purchasing account.
- Product/price.
- Provider reference when subscription-specific.
- Provider agreement reference.
- Provider status.
- Coverage period.
- Renewal/cancellation information.

Do not invent automatic renewal for products whose renewal model
is still pending.

#### entitlements

Specify stored fields, types, nullability, keys, constraints, access, retention, and dependencies for this record.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Effective access or allowance rights, if separately materialized.

Suggested information:

- Account.
- Entitlement type.
- Relevant provider or resource scope.
- Source purchase.
- Validity period.
- Status.

Alternatively derive entitlements from authoritative billing records
when practical.

Choose one clear authority.
If cached or materialized, define synchronization and revocation.

### 10. Listings

#### listings

Specify stored fields, types, nullability, keys, constraints, access, retention, and dependencies for this record.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Common [request listing] and [offer listing] record.

Suggested fields:

- Owner.
- Listing type.
- Title.
- General location.
- Description.
- Category.
- Draft/publication status.
- Published timestamp.
- Expiry.
- Associated user or provider presentation.
- Relevant moderation status.

Type-specific fields may use separate related records.

Do not fill [offer listing]-only fields on [request listing] posts by assumption.

#### listing_revisions

Specify stored fields, types, nullability, keys, constraints, access, retention, and dependencies for this record.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Use where publication review or meaningful edit history requires it.

Avoid storing every keystroke.

#### listing_upgrades

Specify stored fields, types, nullability, keys, constraints, access, retention, and dependencies for this record.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Purchased appearance or placement rights.

Suggested fields:

- Listing.
- Product/price.
- Purchase reference.
- Start and end where defined.
- Delivery status.
- Relevant placement scope.

Unspecified upgrade durations remain pending.

#### boost_allowances

Specify stored fields, types, nullability, keys, constraints, access, retention, and dependencies for this record.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Included or purchased boost availability where needed.

Suggested fields:

- Account or listing scope.
- Source entitlement.
- Period.
- Granted quantity.
- Consumed quantity or ledger association.

#### boost_events

Specify stored fields, types, nullability, keys, constraints, access, retention, and dependencies for this record.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Actual boost execution.

Suggested fields:

- Listing.
- Source allowance or purchase.
- Requested timestamp.
- Applied timestamp.
- Outcome.
- Idempotency reference.

Consumption and ranking updates must not double-spend an allowance.

A boost does not change post expiry unless the product rules change.

### 11. Bookings

#### bookings

Record allowed transitions, responsible actors, guards, timeouts, side effects, and conflicts.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Stable booking identity and participants.

Suggested fields:

- Requesting user.
- Provider.
- Selected presentation.
- Current lifecycle status.
- Current accepted quote reference.
- Scheduled start/end.
- IANA time zone.
- Relevant venue record.
- Version.
- Creation and update timestamps.

Do not store payment, refund, and payout outcomes solely in this status.

#### booking_quotes

Record allowed transitions, responsible actors, guards, timeouts, side effects, and conflicts.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Versioned proposals.

Suggested information:

- Booking.
- Version number.
- Proposing participant.
- Schedule and duration.
- Experiences.
- Presentation requests.
- Expense responsibilities.
- Currency.
- Calculated totals.
- Relevant policy version.
- Status.

#### booking_quote_items

Record allowed transitions, responsible actors, guards, timeouts, side effects, and conflicts.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Price components for a quote.

Suggested information:

- Quote.
- Item type.
- Description snapshot.
- Quantity or duration.
- Unit amount.
- Charge basis.
- Calculated amount.
- Tax/expense classification where applicable.

Preserve enough information to explain the calculation.

#### booking_acceptances

Record scenario IDs, observable pass and fail conditions, the tested environment, actual results, evidence, and who accepts exceptions.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Evidence that a participant accepted an identified version.

Suggested fields:

- Booking.
- Quote version.
- Account.
- Acceptance timestamp.
- Policy version where applicable.

Do not treat acceptance of an earlier quote as acceptance of a revision.

#### booking_reservations

Record allowed transitions, responsible actors, guards, timeouts, side effects, and conflicts.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Temporary availability holds.

Suggested fields:

- Booking.
- Provider.
- Time range.
- Expiry.
- Status.

The hold policy remains pending.

Use appropriate database or transactional controls to prevent
conflicting confirmation.

A simple application-side availability query is insufficient.

#### booking_private_details

Record allowed transitions, responsible actors, guards, timeouts, side effects, and conflicts.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Restricted venue and logistical information where separation is useful.

Access is limited to authorized participants and necessary operations.

#### booking_events

Record allowed transitions, responsible actors, guards, timeouts, side effects, and conflicts.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Consequential booking history.

Suggested fields:

- Booking.
- Event type.
- Actor.
- Previous/new state where relevant.
- Timestamp.
- Quote or payment reference.
- Reason.

#### booking_outcomes

Record allowed transitions, responsible actors, guards, timeouts, side effects, and conflicts.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Attendance, actual duration, early-ending reports, or completion facts
where required by the selected process.

Distinguish reported facts from agreed or operationally resolved outcomes.

The confirmation process remains pending.

### 12. Financial Records

#### purchases

Specify stored fields, types, nullability, keys, constraints, access, retention, and dependencies for this record.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Internal purchase intent and product association.

Suggested fields:

- Purchaser.
- Product/price.
- Scope: provider, listing, or booking.
- Expected amount and currency.
- Status.
- Idempotency reference.
- Provider checkout association.

#### payment_attempts

Record the exact approved rule, calculation basis, timing, authority, and behavior for failures, late events, and retries.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Individual attempts associated with a purchase.

Distinguish failed attempts from successful collected amounts.

#### payments

Record the exact approved rule, calculation basis, timing, authority, and behavior for failures, late events, and retries.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Provider-confirmed payment records.

Suggested fields:

- Purchase.
- Provider reference.
- Amount.
- Currency.
- Provider status.
- Confirmed timestamps.
- Related booking or billing agreement where applicable.

#### payment_events

Record the exact approved rule, calculation basis, timing, authority, and behavior for failures, late events, and retries.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Verified incoming event processing.

Suggested information:

- Provider.
- Provider event identifier.
- Received timestamp.
- Relevant event type.
- Processing status.
- Related records.
- Safe diagnostic information.

Enforce uniqueness of provider event identifiers within the provider scope.

Do not store unnecessary raw sensitive payloads.

#### revenue_allocations

Specify stored fields, types, nullability, keys, constraints, access, retention, and dependencies for this record.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Recorded distribution of a confirmed amount.

Suggested fields:

- Source financial transaction.
- Beneficiary.
- Allocation type.
- Amount.
- Currency.
- Calculation/policy version.
- Adjustment relationships.

Do not label an allocation as a payout.

#### refunds

Record the exact approved rule, calculation basis, timing, authority, and behavior for failures, late events, and retries.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Refund requests and provider outcomes.

Suggested information:

- Original payment.
- Requested amount.
- Confirmed refunded amount.
- Reason.
- Authority.
- Provider reference.
- Status.
- Allocation adjustments.

Prevent refunds exceeding the permitted refundable amount.

#### disputes

Specify stored fields, types, nullability, keys, constraints, access, retention, and dependencies for this record.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Payment or service dispute records.

Separate allegations, evidence, operational decisions,
and provider-side outcomes.

#### payouts

Record the exact approved rule, calculation basis, timing, authority, and behavior for failures, late events, and retries.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Actual transfer attempts and confirmed outcomes.

Suggested fields:

- Provider recipient.
- Provider reference.
- Amount and currency.
- Included allocations or settlement association.
- Status.
- Failure or reversal information.

Payout eligibility and timing remain pending.

Use an auditable ledger or equivalent balanced financial design
appropriate to the selected provider and funds flow.

Do not implement an informal editable balance as the financial authority.

### 13. Media

#### media_assets

List the actors, allowed actions, restricted fields, enforcement points, and what happens when access is denied, expires, or is revoked.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Stored objects and processing state.

Suggested information:

- Owner.
- Storage reference.
- Media type.
- Size and relevant dimensions/duration.
- Processing status.
- Moderation status.
- Creation/deletion state.

#### profile_media

List the actors, allowed actions, restricted fields, enforcement points, and what happens when access is denied, expires, or is revoked.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Media placement and access associations.

Suggested fields:

- Asset.
- Provider presentation or user profile.
- Visibility tier.
- Gallery order.
- Profile-photo role.
- Safe-preview reference where applicable.

#### message_attachments

Specify stored fields, types, nullability, keys, constraints, access, retention, and dependencies for this record.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Conversation-specific asset associations.

Authorization must follow the conversation and attachment policy.

Do not expose private storage references through public APIs.

Define cleanup for uploads that are never attached to a valid resource.

### 14. Conversations and Messages

#### conversations

Specify stored fields, types, nullability, keys, constraints, access, retention, and dependencies for this record.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Conversation identity.

#### conversation_members

Specify stored fields, types, nullability, keys, constraints, access, retention, and dependencies for this record.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Authorized participants.

Include membership state and relevant lifecycle information.

A provider subscription alone must not authorize unrelated
conversation history.

#### messages

Specify stored fields, types, nullability, keys, constraints, access, retention, and dependencies for this record.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Suggested fields:

- Conversation.
- Sender.
- Content.
- Creation timestamp.
- Edit/deletion state if supported.
- Client request identifier for duplicate-send handling.

Define retention and editing policies before implementing them.

#### read_receipts

Specify stored fields, types, nullability, keys, constraints, access, retention, and dependencies for this record.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Participant-specific read position or receipt records.

Users can update only their own permitted read state.

#### call_sessions

List the actors, allowed actions, restricted fields, enforcement points, and what happens when access is denied, expires, or is revoked.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Call identity and participation.

Suggested information:

- Conversation or participant references.
- Initiator.
- Intended recipient.
- Provider reference.
- Lifecycle timestamps.
- Status.

Do not store reusable privileged connection credentials.

No recording entity is required by the current specification.

### 15. Reviews

#### reviews

Specify stored fields, types, nullability, keys, constraints, access, retention, and dependencies for this record.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Suggested fields:

- Eligible booking.
- Reviewer.
- Reviewed provider/presentation.
- Rating dimensions.
- Written content.
- Publication/moderation status.
- Creation and permitted edit timestamps.

Enforce confirmed eligibility and duplicate-review rules.

#### review_responses

Specify stored fields, types, nullability, keys, constraints, access, retention, and dependencies for this record.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Use if provider responses are approved.

A response must not modify the original review.

### 16. Blocking, Reporting, and Support

#### blocks

List the actors, allowed actions, restricted fields, enforcement points, and what happens when access is denied, expires, or is revoked.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Suggested fields:

- Blocking account.
- Blocked account.
- Creation timestamp.

Prevent self-blocking and duplicate active relationships.

Cross-feature consequences remain subject to the access specification.

#### reports

Specify stored fields, types, nullability, keys, constraints, access, retention, and dependencies for this record.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Suggested information:

- Reporter where available.
- Reported resource/account.
- Category.
- Description.
- Submission time.
- Status.
- Assigned reviewer.
- Resolution reference.

Public reporting may require a distinct intake design.

#### report_evidence

Specify stored fields, types, nullability, keys, constraints, access, retention, and dependencies for this record.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Restricted references to necessary evidence.

Avoid duplicating private content unnecessarily.

#### moderation_actions

Specify stored fields, types, nullability, keys, constraints, access, retention, and dependencies for this record.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Consequential operational actions.

Suggested information:

- Authorized actor.
- Target.
- Action.
- Reason.
- Start/end where applicable.
- Report or case reference.
- Audit association.

#### support_cases

Specify stored fields, types, nullability, keys, constraints, access, retention, and dependencies for this record.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Operational support workflow where required.

Keep access limited according to case responsibility.

### 17. Policies and Acceptance

#### policy_versions

Specify stored fields, types, nullability, keys, constraints, access, retention, and dependencies for this record.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Suggested fields:

- Policy identifier.
- Version.
- Effective date.
- Immutable content reference.
- Publication status.

#### policy_acceptances

Record scenario IDs, observable pass and fail conditions, the tested environment, actual results, evidence, and who accepts exceptions.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Suggested fields:

- Account.
- Policy version.
- Acceptance timestamp.
- Related booking or transaction where relevant.

Do not prepopulate acceptance.

An accepted historical version must remain identifiable after updates.

### 18. Notifications and Background Work

#### notifications

Specify stored fields, types, nullability, keys, constraints, access, retention, and dependencies for this record.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Persistent account-visible events where applicable.

Suggested information:

- Recipient.
- Event type.
- Safe content.
- Related record.
- Created/read state.

#### notification_deliveries

Record prerequisites, deliverables, owners, dependencies, and the smallest independently verifiable result.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Channel-specific attempts and outcomes.

A failed delivery does not erase the underlying booking or message.

#### background_jobs

Specify stored fields, types, nullability, keys, constraints, access, retention, and dependencies for this record.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Use when the selected infrastructure requires persisted work records.

Track:

- Job type.
- Relevant record.
- Attempts.
- Status.
- Next eligible execution.
- Safe failure information.

#### outbox_events

Specify stored fields, types, nullability, keys, constraints, access, retention, and dependencies for this record.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Use an outbox or equivalent recoverable mechanism when a committed
database change must trigger external work reliably.

Do not assume an external notification is atomic with a database write.

### 19. Audit Records

#### audit_events

Specify stored fields, types, nullability, keys, constraints, access, retention, and dependencies for this record.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Record consequential administrative and security-sensitive actions.

Suggested fields:

- Actor or trusted service.
- Action.
- Resource type and identifier.
- Timestamp.
- Safe change summary.
- Correlation reference.

Do not log secrets or private conversation bodies into general audit records.

Access to audit records is itself restricted.

Do not promise immutability unless the chosen storage and permissions
actually provide it.

### 20. Important Constraints

Assign each invariant an ID and identify its enforcement layer, transaction boundary, affected records, and regression test.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Enforce relevant invariants through trusted mechanisms:

- Unique normalized usernames under the approved identity design.
- Unique authentication-provider subject association.
- No duplicate role assignments.
- No more than two provider presentations.
- Correct owner/presentation relationships.
- Valid foreign-key relationships.
- Explicit currency for monetary records.
- Nonnegative ordinary charge amounts.
- Signed adjustments only in explicitly designed adjustment records.
- Revenue allocations reconcile with their source amounts.
- Unique provider payment/event references where appropriate.
- No duplicate allowance consumption.
- No unauthorized confirmed booking overlaps.
- Accepted quotes reference valid versions.
- Refund totals respect approved limits.
- Review eligibility follows the confirmed policy.

Choose provider-compatible implementations.

Cross-row limits and scheduling conflicts may require more than
simple field checks.

### 21. Indexing and Query Design

For **indexing and query design**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Add indexes for actual query patterns.

Likely areas include:

- Listing type, location, publication, expiry, and ordering.
- Provider lookup.
- Entitlement account/scope/status.
- Booking participants and schedule.
- Conversation membership.
- Message conversation and ordering.
- Provider references.
- Pending jobs.
- Moderation queues.

Do not add indexes indiscriminately.

Use stable tie-breakers for paginated ordering.

Prevent public search indexes from containing restricted fields.

### 22. Deletion and Retention

For **deletion and retention**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Define retention by record purpose.

Distinguish:

- Removal from public display.
- Account restriction.
- Soft deletion.
- Storage-object deletion.
- Anonymization.
- Required financial or dispute retention.

Do not cascade account deletion through financial history by assumption.

Do not retain sensitive information indefinitely merely because
soft deletion is convenient.

Document cleanup for:

- Abandoned uploads.
- Expired temporary records.
- Deleted profile media.
- Message attachments.
- Verification information.
- Operational evidence.

Final periods remain pending.

### 23. API Representations

For **api representations**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Database records are not automatically safe API responses.

Define explicit representations for:

- Public profile.
- Member profile.
- Subscriber profile.
- Owner editor.
- Booking participant.
- Purchaser billing.
- Provider earnings.
- Moderator case.
- Administrator operation.

Return only required fields.

Do not expose internal notes, provider secrets, private addresses,
or unrestricted storage references through generic serialization.

### 24. Migration and Implementation

For **migration and implementation**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

When the database is selected:

1. Translate this logical model into the actual schema.
2. Resolve policies required by the implementation slice.
3. Create versioned migrations.
4. Add ownership and permission enforcement.
5. Add appropriate constraints and indexes.
6. Use synthetic development data.
7. Verify critical queries and authorization.
8. Update this document to match the implemented structure.

Do not create all proposed entities upfront if the current phase
does not require them.

Keep planned and implemented portions distinguishable.

### 25. Open Decisions

Record the unresolved question, viable options, decision owner, required evidence, and work blocked by the decision.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Data design depends on pending choices including:

- Account role combinations.
- Eligibility and verification.
- User-profile visibility.
- Subscription coverage across presentations.
- Publishing and premium expiry.
- Historical communication access.
- Reservation policy.
- Attendance confirmation.
- Deposit and balance collection.
- Refund and payout calculations.
- Paired bookings.
- Review eligibility.
- Media retention.
- Operational evidence access.

Track decisions in ../decisions.md.

### 26. Final Rule

For **final rule**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Model ownership, agreements, entitlements, and money explicitly.

Preserve history where required.
Minimize sensitive data.
Enforce important invariants.
Keep the schema aligned with confirmed product rules and actual implementation.

