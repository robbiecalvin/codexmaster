# MeetDiscreet — Data Model

## 1. Purpose and Status

Describe the logical data model for MeetDiscreet.

This is a design specification, not an implemented database schema.

Entity names are proposed.
Adapt them to the selected database while preserving responsibilities,
ownership, relationships, and constraints.

Read alongside:

- ../../AGENTS.md
- ../product/product_spec.md
- ../product/access_matrix.md
- ../product/pricing_and_payments.md
- ../product/booking_lifecycle.md
- ./application_architecture.md
- ../security/application_security.md
- ../decisions.md

Unresolved product rules must remain explicit.
Do not encode an assistant recommendation as an approved constraint.

## 2. Modelling Principles

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

## 3. Common Conventions

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

## 4. Identity and Accounts

### accounts

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

### account_roles

Assigned application roles.

Suggested information:

- Account reference.
- Role.
- Assigned timestamp.
- Assigning authority where applicable.

Prevent duplicate assignments.

Users cannot grant themselves privileged roles.

Whether user and companion roles may coexist remains pending.

### account_preferences

Private account settings where needed.

Examples:

- Notification preferences.
- Locale.
- Display time zone.
- Privacy choices.

Do not use preferences to establish paid entitlements.

## 5. Profiles and Companion Presentations

### user_profiles

User-managed profile information.

Suggested fields:

- Account reference.
- Username.
- Display name.
- General location reference.
- Profile-photo reference.
- Interests.
- Languages.
- What I’m Looking For.
- What I Enjoy.
- Permitted optional fields.

Field visibility remains subject to the access matrix.

Do not publish the entire record through a generic API response.

### companion_profiles

Companion-level identity and management information.

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

### companion_presentations

Up to two presentations per companion account.

Suggested fields:

- Companion reference.
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

### presentation_partners

Optional links for two-companion offerings.

Suggested fields:

- Source presentation or companion.
- Linked companion.
- Relationship status.
- Any required acknowledgement.

A link is not proof of booking participation or authority to accept
for the other companion.

## 6. Eligibility and Verification

### verification_records

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

## 7. Locations and Discovery

### locations

General locations used for discovery.

Possible information:

- Country.
- Region.
- City.
- Approved area label.
- Public geographic representation where needed.

Keep precise booking addresses separate.

Do not add precise home coordinates merely to support city browsing.

### categories

Approved activity or listing categories.

Suggested information:

- Stable code.
- Display label.
- Description.
- Active status.
- Ordering.

Keep policy-specific labels separate from core marketplace logic
without creating an unnecessary universal taxonomy engine.

## 8. Experiences and Rates

### experiences

Companion or presentation offerings.

Suggested fields:

- Owning companion/presentation.
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

### rate_definitions

Applicable base rates.

Suggested fields:

- Companion or presentation.
- Rate category.
- Amount in minor units.
- Currency.
- Billing unit.
- Minimum duration, if approved.
- Effective or active status.

Historical accepted bookings must not depend on mutable current rates.

### availability_rules

Recurring or offered availability.

Suggested information:

- Companion.
- Local schedule.
- IANA time zone.
- Effective dates.
- Applicable presentation restrictions where needed.

### availability_exceptions

Specific unavailable periods or overrides.

Keep these distinct from actual confirmed bookings and reservation holds.

## 9. Product Catalogue and Billing Agreements

### products

Stable commercial product definitions.

Examples:

- Premium membership.
- Companion publishing.
- Companion subscription.
- Additional ad.
- Boost.
- Placement upgrade.
- Appearance upgrade.

### prices

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

### billing_agreements

Recurring or fixed-term purchase associations.

Suggested fields:

- Purchasing account.
- Product/price.
- Companion reference when subscription-specific.
- Provider agreement reference.
- Provider status.
- Coverage period.
- Renewal/cancellation information.

Do not invent automatic renewal for products whose renewal model
is still pending.

### entitlements

Effective access or allowance rights, if separately materialized.

Suggested information:

- Account.
- Entitlement type.
- Relevant companion or resource scope.
- Source purchase.
- Validity period.
- Status.

Alternatively derive entitlements from authoritative billing records
when practical.

Choose one clear authority.
If cached or materialized, define synchronization and revocation.

## 10. Listings

### listings

Common Looking For and Offering record.

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
- Associated user or companion presentation.
- Relevant moderation status.

Type-specific fields may use separate related records.

Do not fill Offering-only fields on Looking For posts by assumption.

### listing_revisions

Use where publication review or meaningful edit history requires it.

Avoid storing every keystroke.

### listing_upgrades

Purchased appearance or placement rights.

Suggested fields:

- Listing.
- Product/price.
- Purchase reference.
- Start and end where defined.
- Delivery status.
- Relevant placement scope.

Unspecified upgrade durations remain pending.

### boost_allowances

Included or purchased boost availability where needed.

Suggested fields:

- Account or listing scope.
- Source entitlement.
- Period.
- Granted quantity.
- Consumed quantity or ledger association.

### boost_events

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

## 11. Bookings

### bookings

Stable booking identity and participants.

Suggested fields:

- Requesting user.
- Companion.
- Selected presentation.
- Current lifecycle status.
- Current accepted quote reference.
- Scheduled start/end.
- IANA time zone.
- Relevant venue record.
- Version.
- Creation and update timestamps.

Do not store payment, refund, and payout outcomes solely in this status.

### booking_quotes

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

### booking_quote_items

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

### booking_acceptances

Evidence that a participant accepted an identified version.

Suggested fields:

- Booking.
- Quote version.
- Account.
- Acceptance timestamp.
- Policy version where applicable.

Do not treat acceptance of an earlier quote as acceptance of a revision.

### booking_reservations

Temporary availability holds.

Suggested fields:

- Booking.
- Companion.
- Time range.
- Expiry.
- Status.

The hold policy remains pending.

Use appropriate database or transactional controls to prevent
conflicting confirmation.

A simple application-side availability query is insufficient.

### booking_private_details

Restricted venue and logistical information where separation is useful.

Access is limited to authorized participants and necessary operations.

### booking_events

Consequential booking history.

Suggested fields:

- Booking.
- Event type.
- Actor.
- Previous/new state where relevant.
- Timestamp.
- Quote or payment reference.
- Reason.

### booking_outcomes

Attendance, actual duration, early-ending reports, or completion facts
where required by the selected process.

Distinguish reported facts from agreed or operationally resolved outcomes.

The confirmation process remains pending.

## 12. Financial Records

### purchases

Internal purchase intent and product association.

Suggested fields:

- Purchaser.
- Product/price.
- Scope: companion, listing, or booking.
- Expected amount and currency.
- Status.
- Idempotency reference.
- Provider checkout association.

### payment_attempts

Individual attempts associated with a purchase.

Distinguish failed attempts from successful collected amounts.

### payments

Provider-confirmed payment records.

Suggested fields:

- Purchase.
- Provider reference.
- Amount.
- Currency.
- Provider status.
- Confirmed timestamps.
- Related booking or billing agreement where applicable.

### payment_events

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

### revenue_allocations

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

### refunds

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

### disputes

Payment or service dispute records.

Separate allegations, evidence, operational decisions,
and provider-side outcomes.

### payouts

Actual transfer attempts and confirmed outcomes.

Suggested fields:

- Companion recipient.
- Provider reference.
- Amount and currency.
- Included allocations or settlement association.
- Status.
- Failure or reversal information.

Payout eligibility and timing remain pending.

Use an auditable ledger or equivalent balanced financial design
appropriate to the selected provider and funds flow.

Do not implement an informal editable balance as the financial authority.

## 13. Media

### media_assets

Stored objects and processing state.

Suggested information:

- Owner.
- Storage reference.
- Media type.
- Size and relevant dimensions/duration.
- Processing status.
- Moderation status.
- Creation/deletion state.

### profile_media

Media placement and access associations.

Suggested fields:

- Asset.
- Companion presentation or user profile.
- Visibility tier.
- Gallery order.
- Profile-photo role.
- Safe-preview reference where applicable.

### message_attachments

Conversation-specific asset associations.

Authorization must follow the conversation and attachment policy.

Do not expose private storage references through public APIs.

Define cleanup for uploads that are never attached to a valid resource.

## 14. Conversations and Messages

### conversations

Conversation identity.

### conversation_members

Authorized participants.

Include membership state and relevant lifecycle information.

A companion subscription alone must not authorize unrelated
conversation history.

### messages

Suggested fields:

- Conversation.
- Sender.
- Content.
- Creation timestamp.
- Edit/deletion state if supported.
- Client request identifier for duplicate-send handling.

Define retention and editing policies before implementing them.

### read_receipts

Participant-specific read position or receipt records.

Users can update only their own permitted read state.

### call_sessions

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

## 15. Reviews

### reviews

Suggested fields:

- Eligible booking.
- Reviewer.
- Reviewed companion/presentation.
- Rating dimensions.
- Written content.
- Publication/moderation status.
- Creation and permitted edit timestamps.

Enforce confirmed eligibility and duplicate-review rules.

### review_responses

Use if companion responses are approved.

A response must not modify the original review.

## 16. Blocking, Reporting, and Support

### blocks

Suggested fields:

- Blocking account.
- Blocked account.
- Creation timestamp.

Prevent self-blocking and duplicate active relationships.

Cross-feature consequences remain subject to the access specification.

### reports

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

### report_evidence

Restricted references to necessary evidence.

Avoid duplicating private content unnecessarily.

### moderation_actions

Consequential operational actions.

Suggested information:

- Authorized actor.
- Target.
- Action.
- Reason.
- Start/end where applicable.
- Report or case reference.
- Audit association.

### support_cases

Operational support workflow where required.

Keep access limited according to case responsibility.

## 17. Policies and Acceptance

### policy_versions

Suggested fields:

- Policy identifier.
- Version.
- Effective date.
- Immutable content reference.
- Publication status.

### policy_acceptances

Suggested fields:

- Account.
- Policy version.
- Acceptance timestamp.
- Related booking or transaction where relevant.

Do not prepopulate acceptance.

An accepted historical version must remain identifiable after updates.

## 18. Notifications and Background Work

### notifications

Persistent account-visible events where applicable.

Suggested information:

- Recipient.
- Event type.
- Safe content.
- Related record.
- Created/read state.

### notification_deliveries

Channel-specific attempts and outcomes.

A failed delivery does not erase the underlying booking or message.

### background_jobs

Use when the selected infrastructure requires persisted work records.

Track:

- Job type.
- Relevant record.
- Attempts.
- Status.
- Next eligible execution.
- Safe failure information.

### outbox_events

Use an outbox or equivalent recoverable mechanism when a committed
database change must trigger external work reliably.

Do not assume an external notification is atomic with a database write.

## 19. Audit Records

### audit_events

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

## 20. Important Constraints

Enforce relevant invariants through trusted mechanisms:

- Unique normalized usernames under the approved identity design.
- Unique authentication-provider subject association.
- No duplicate role assignments.
- No more than two companion presentations.
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

## 21. Indexing and Query Design

Add indexes for actual query patterns.

Likely areas include:

- Listing type, location, publication, expiry, and ordering.
- Companion lookup.
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

## 22. Deletion and Retention

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

## 23. API Representations

Database records are not automatically safe API responses.

Define explicit representations for:

- Public profile.
- Member profile.
- Subscriber profile.
- Owner editor.
- Booking participant.
- Purchaser billing.
- Companion earnings.
- Moderator case.
- Administrator operation.

Return only required fields.

Do not expose internal notes, provider secrets, private addresses,
or unrestricted storage references through generic serialization.

## 24. Migration and Implementation

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

## 25. Open Decisions

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

## 26. Final Rule

Model ownership, agreements, entitlements, and money explicitly.

Preserve history where required.
Minimize sensitive data.
Enforce important invariants.
Keep the schema aligned with confirmed product rules and actual implementation.