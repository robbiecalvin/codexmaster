# [Application name] — Booking Lifecycle

**Owner** [Role]  
**Scope and revision** [Milestone or version]  
**Status and review date** [Draft / Approved / Verified, date]

Complete each applicable section with project-specific values and evidence. The detailed reference material describes an illustrative marketplace. Adapt its actors, rules, tools, limits, and workflows to your project. Mark inapplicable sections with a short reason. Treat unapproved choices as proposed or pending.

## Quick-start worksheet

**Owner and review date** [Role, date]  
**Status** [Proposed / Approved / Implemented]

### Scope and participants

Describe what a booking commits each participant to, who can request, accept, amend or adjudicate it, and what eligibility and privacy constraints apply. Link the authoritative pricing, policy, and permissions rules.

### Booking record and agreement

Record participants, availability window and time zone, location visibility, quote version and expiry, terms, acceptance timestamps, and history. Specify which facts are captured when an agreement is accepted and which can change later.

### Booking state transitions

Adapt the proposed states to the actual workflow. Keep booking, reservation, payment, fulfillment, and dispute states independently traceable.

| From | Trigger and actor | Preconditions | To | Effects and notifications | Failure handling |
| --- | --- | --- | --- | --- | --- |
| [Draft] | [Submit request] | [Eligibility, details and time] | [Requested] | [Create version, notify reviewer] | [Validation outcome] |
| [Requested] | [Revise, accept, decline, withdraw or expire] | [Current version and authority] | [Next state] | [Record action and alert participants] | [Stale revision or timeout] |
| [Agreed] | [Reserve and confirm] | [Availability and payment conditions] | [Confirmed] | [Lock slot and issue confirmation] | [Late payment or conflict] |
| [Confirmed] | [Start, amend, cancel or mark no-show] | [Time, consent and applicable policy] | [Next state] | [Update schedule, notices and settlement] | [Escalation or dispute] |
| [In progress] | [Complete or end early] | [Authorized actor and outcome] | [Outcome recorded] | [Settlement and review eligibility] | [Conflicting accounts] |

### Reservations, money, and exceptions

Describe when holds begin and expire, how availability is enforced concurrently, when deposits or balances become due, and what verified event confirms payment. Specify late or duplicate payment handling, cancellation, lateness, non-attendance, early ending, and reconciliation. For multi-party bookings, define required acceptance, capacity, and amendments across all participants. See [Pricing and Payments](pricing_and_payments.md).

### Access changes, notifications, and audit

Define what happens to existing bookings when a participant is blocked, loses a grant, or is suspended. Document which participants receive each notice, who can see private booking details, and which transitions need audit entries or deduplication.

### Required verification and decisions

Test each permitted transition and its rejected cases, stale quotes, conflicting reservations, retries, and payment outcomes. Record unresolved rules in the [Decision Register](decisions.md) and evidence in [Launch Acceptance](launch_acceptance.md).

## Detailed template

Use these fields for the detailed records in this document.

| Starting state | Trigger and authorized actor | Preconditions | Next state | Reservation or payment effect | Rejection or recovery | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| [Fill in] | [Fill in] | [Fill in] | [Fill in] | [Fill in] | [Fill in] | [Fill in] |

### 1. Purpose and Status

Record the actual release, what is applicable today, what remains proposed or deferred, and the latest supporting reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Define how booking requests become agreed experiences, how changes
are handled, and how booking records relate to payments.

This is the intended lifecycle.
It does not establish implementation or live payment readiness.

Read alongside:

- [Project reference for AGENTS]
- [Product Spec](product_spec.md)
- [Access Matrix](access_matrix.md)
- [Pricing And Payments](pricing_and_payments.md)
- [Decisions](decisions.md)
- [Application Architecture](application_architecture.md)
- [Data Model](data_model.md)

Financial amounts and calculation rules belong in
pricing_and_payments.md.

If a required policy remains unresolved, do not invent it.

### 2. Core Principles

For **core principles**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

- A subscription unlocks booking requests, not a guaranteed booking.
- Providers choose which requests to accept.
- Material revisions require agreement.
- Accepted terms must be preserved.
- Payment confirmation requires trusted verification.
- Availability must be protected against concurrent bookings.
- Either participant can end an interaction.
- Financial consequences follow the confirmed policy.
- Booking, payment, refund, dispute, and payout states remain distinct.

Do not promise that payment guarantees attendance or safety.

### 3. Booking Participants

Record allowed transitions, responsible actors, guards, timeouts, side effects, and conflicts.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

A standard booking identifies:

- Requesting user.
- Selected provider.
- Selected provider presentation.
- Authorized operational staff where necessary.

An unrelated account cannot view or modify the booking.

Two-provider bookings require additional confirmed rules before
live use.

Do not assume the primary provider can accept on another
provider’s behalf.

### 4. Booking Record

Record allowed transitions, responsible actors, guards, timeouts, side effects, and conflicts.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Store the information needed to understand the agreement:

- Booking identifier.
- Requesting account.
- Provider account.
- Presentation identifier.
- Requested schedule.
- Relevant time-zone identifier.
- Duration.
- Venue or meeting area.
- Selected experiences.
- Add-ons.
- Presentation requests.
- Accessibility requests voluntarily supplied.
- Expense responsibilities.
- Notes.
- Quote versions.
- Accepted quote reference.
- Accepted policy version.
- Acceptance records.
- Reservation deadline where applicable.
- Booking status.
- Payment references.
- Cancellation or ending information.
- Relevant timestamps and audit events.

Minimize sensitive information.

Do not publish private meeting details in listings or public profiles.

### 5. Lifecycle Overview

Record allowed transitions, responsible actors, guards, timeouts, side effects, and conflicts.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

The proposed standard flow is:

Draft → Requested → Accepted Awaiting Deposit → Confirmed
→ In Progress → Completed

Alternative outcomes include:

- Revision required.
- Declined.
- Withdrawn.
- Expired.
- Cancelled.
- Ended early.

Disputes and payment outcomes are tracked separately.

Exact state names may be adapted during implementation,
but the distinctions must remain clear.

### 6. Booking States

Record allowed transitions, responsible actors, guards, timeouts, side effects, and conflicts.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

| State | Meaning |
|---|---|
| draft | Requester is preparing an unsubmitted request |
| requested | Request submitted for provider review |
| revision_requested | Revised terms await the other participant’s response |
| accepted_awaiting_deposit | Both sides have agreed terms; required deposit is not yet verified |
| confirmed | Required payment and reservation conditions are satisfied |
| in_progress | Experience has started under the approved start process |
| completed | Experience concluded under the approved completion process |
| ended_early | Experience stopped before its agreed end |
| declined | Provider rejected the request |
| withdrawn | Requester withdrew before confirmation |
| expired | An applicable response or payment deadline elapsed |
| cancelled | A confirmed booking was cancelled |

Do not use a status change as a substitute for recording the reason,
actor, and timestamp.

Completion, start, and early-ending confirmation processes remain
to be selected.

### 7. Preparing a Draft

For **preparing a draft**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Only the requester can edit their own draft.

The form supports:

- Provider and presentation.
- Date.
- Start time.
- Time zone.
- Duration.
- Venue proposal.
- Experiences.
- Add-ons.
- Relevant requests.
- Expenses.
- Notes.
- Estimated total.

Show available information without exposing another account’s
private schedule.

A draft:

- Does not reserve availability.
- Does not guarantee rates.
- Does not create a payment obligation by itself.

Revalidate all relevant information on submission.

### 8. Submitting a Request

For **submitting a request**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Before accepting submission, the backend checks:

- Session validity.
- Requester eligibility.
- Relevant provider subscription.
- Provider eligibility.
- Presentation ownership.
- [offer listing] availability.
- Valid schedule and duration.
- Block relationships.
- Input limits.
- Authoritative estimate.

Record the submitted terms and quote version.

The proposed single-deposit model does not collect a request fee
at this stage.

The collection point remains subject to confirmation in the
financial specification.

Do not silently introduce a charge.

### 9. Provider Review

For **provider review**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

The provider can:

- Accept the submitted terms.
- Decline.
- Propose revisions.

Show relevant request information and price components.

Do not expose unrelated private user information.

A request alone does not occupy a confirmed booking slot.

Whether pending requests create any temporary availability effect
must be explicitly defined.

### 10. Revisions

For **revisions**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

A material revision may change:

- Schedule.
- Duration.
- Venue.
- Presentation.
- Experiences.
- Add-ons.
- Expenses.
- Price.
- Other agreed conditions.

Create a new quote or agreement version.

Identify:

- Who proposed it.
- What changed.
- When it was proposed.
- Whether it was accepted.

Do not overwrite the prior version without history.

The party receiving revised terms must accept them before the booking
proceeds on that basis.

Do not charge a revised amount based only on silence.

Avoid using a single revision state without recording whose response
is awaited.

### 11. Agreement and Acceptance

Record scenario IDs, observable pass and fail conditions, the tested environment, actual results, evidence, and who accepts exceptions.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

When both sides agree:

- Record the accepted version.
- Preserve the price components.
- Preserve the policy version.
- Record relevant acceptance timestamps.
- Recheck availability.
- Establish any approved reservation.
- Show the next required payment action.

Public profile edits do not rewrite accepted terms.

Changes after acceptance follow the amendment process.

If the provider simply accepts the requester’s unchanged proposal,
record that both parties agreed to that exact version.

### 12. Reservation Policy

Record allowed transitions, responsible actors, guards, timeouts, side effects, and conflicts.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

The reservation mechanism remains to be confirmed.

Before implementation, define:

- When a hold begins.
- How long it lasts.
- Whether it prevents competing acceptance.
- When it expires.
- Whether payment processing extends it.
- What happens when payment arrives late.
- How holds are released.

Do not invent a fixed deadline such as 15 minutes without approval.

Enforce scheduling constraints through trusted transactional or
equivalent concurrency controls.

Two simultaneous requests must not both confirm the same unavailable
provider time.

### 13. Deposit Collection

Record the exact approved rule, calculation basis, timing, authority, and behavior for failures, late events, and retries.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Proposed model:

- Collect one [rate] deposit after acceptance.
- Credit it toward the booking total.
- Allocate it according to pricing_and_payments.md.

Before creating checkout:

1. Verify the accepted agreement.
2. Verify the requester.
3. Recheck reservation validity.
4. Determine the authoritative amount.
5. Record the payment attempt.
6. Create the provider transaction with appropriate idempotency.

Do not trust browser-submitted amounts.

Do not permit payment against a superseded quote.

### 14. Payment Confirmation

Record the exact approved rule, calculation basis, timing, authority, and behavior for failures, late events, and retries.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Confirm through verified provider events or an equivalent
trusted reconciliation process.

Check:

- Correct purchase reference.
- Correct booking.
- Correct payer association where applicable.
- Expected amount and currency.
- Accepted quote version.
- Reservation and booking state.
- Whether the event has already been processed.

A checkout success page is not proof of payment.

Duplicate events must not duplicate:

- Confirmation.
- Allocations.
- Notifications.
- Financial records.

Handle delayed and out-of-order events.

### 15. Confirming the Booking

Record allowed transitions, responsible actors, guards, timeouts, side effects, and conflicts.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Move to confirmed only when the required conditions are satisfied:

- Valid accepted agreement.
- Required payment verified.
- Availability or reservation valid.
- No conflicting restriction prevents confirmation.

Record confirmation time.

Notify both participants through the approved channels.

Display:

- Agreed schedule and time zone.
- Presentation.
- Venue details permitted at this stage.
- Experiences.
- Price.
- Amount paid.
- Remaining balance.
- Relevant cancellation access.

Do not expose private booking details publicly.

### 16. Late or Conflicting Payment Outcomes

Record the exact approved rule, calculation basis, timing, authority, and behavior for failures, late events, and retries.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

A payment can succeed after:

- Reservation expiry.
- Request withdrawal.
- A conflicting booking.
- Account restriction.
- Quote replacement.
- Cancellation.

Do not automatically force confirmation.

Persist the successful financial event and route it to the approved
resolution process.

Possible outcomes require policy selection:

- Reconfirm availability and seek agreement.
- Refund.
- Hold for authorized operational review.

Do not silently retain payment for an impossible booking.

Do not describe an unresolved payment conflict as a confirmed date.

### 17. Amendments After Confirmation

For **amendments after confirmation**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Material changes require a new recorded amendment.

Define:

- Proposed changes.
- Revised price.
- Additional payment or refund.
- Acceptance by affected participants.
- Availability impact.
- Effective time.

Keep the existing agreement active unless and until the amendment
is accepted under the confirmed process.

Do not release the original reservation before safely handling
replacement availability.

Do not charge additional amounts without appropriate authorization.

### 18. Starting the Experience

For **starting the experience**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

The start process remains pending.

Options may include participant confirmation, a scheduled transition,
or an operationally reviewed process.

The selected mechanism must distinguish:

- Scheduled start.
- Reported actual start.
- Confirmed or disputed actual start.

A scheduled timestamp alone does not prove attendance.

Do not add location tracking or continuous monitoring without an
explicit requirement and appropriate privacy design.

### 19. Completing the Experience

For **completing the experience**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

The completion process remains pending.

Record enough information to support:

- Actual or agreed billable duration.
- Approved adjustments.
- Expenses.
- Remaining amount due.
- Payment status.
- Review eligibility.
- Disputes.

Do not infer a completed payout from booking completion.

Define how conflicting participant reports are handled.

Do not automatically classify an experience as successfully delivered
merely because its scheduled end passed.

### 20. Early Ending

For **early ending**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Either participant can end the experience.

Provide an appropriate way to record:

- Who ended it.
- Reported end time.
- Optional reason.
- Disagreement about timing or charges.
- Need for support.

Do not require detailed sensitive disclosures to stop participation.

The financial calculation must use the confirmed early-ending policy.

Resolve the interaction between:

- Actual time.
- Retained deposit.
- Minimum charges.
- Add-ons.
- Approved expenses.
- Taxes.
- Refunds.

Do not invent a calculation or make contradictory promises.

### 21. Withdrawal, Decline, and Expiry

#### Withdrawal

For **withdrawal**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

The requester withdraws before confirmation.

Determine financial consequences from actual payment state,
not merely the booking label.

#### Decline

For **decline**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

The provider rejects the request.

Do not create a new charge because a request was declined.

#### Expiry

For **expiry**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

A configured response or payment deadline passes.

Release applicable holds safely.

If no deadline has been selected, do not implement arbitrary expiry.

Persist the reason and relevant deadline.

### 22. Cancellation After Confirmation

For **cancellation after confirmation**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Allow participating accounts to request or perform cancellation
according to the confirmed lifecycle.

Record:

- Actor.
- Timestamp.
- Reason where supplied.
- Applicable policy version.
- Financial calculation.
- Refund or balance action.
- Reservation release.
- Notification outcome.

Distinguish user cancellation from provider cancellation.

Do not describe a refund as completed before provider confirmation.

Cancellation must remain possible through an appropriate support route
if a participant cannot use the normal interface.

### 23. Non-Attendance and Lateness

For **non-attendance and lateness**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Define before live bookings:

- What constitutes non-attendance.
- Any grace period.
- How participants report it.
- How conflicting reports are reviewed.
- Deposit treatment.
- Remaining charges.
- Expenses.
- Review eligibility.

Do not infer non-attendance solely from an unanswered message
or missing browser activity.

Keep allegations separate from established outcomes.

### 24. Subscription Expiry and Account Restrictions

For **subscription expiry and account restrictions**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

A new booking request requires the approved subscription entitlement.

Rules for existing bookings after subscription expiry remain pending.

Do not automatically remove access to:

- Receipts.
- Payment records.
- Dispute submission.
- Necessary booking-management information.

Define how restrictions affect:

- New requests.
- Pending requests.
- Confirmed bookings.
- Communication.
- Refunds.
- Payouts.

Suspension does not itself resolve contractual or financial obligations.

### 25. Blocking

List the actors, allowed actions, restricted fields, enforcement points, and what happens when access is denied, expires, or is revoked.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Blocking must prevent interactions according to the access policy.

It must not silently:

- Cancel a confirmed booking.
- Erase a payment.
- Create a refund.
- Release an outstanding balance.
- Remove necessary support access.

Provide a controlled path for handling an existing booking between
accounts that can no longer communicate normally.

Confirm the exact rules before launch.

### 26. Separate Financial and Dispute States

Record the exact approved rule, calculation basis, timing, authority, and behavior for failures, late events, and retries.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Do not encode everything in the booking status.

Track separately:

- Payment attempts.
- Successful payments.
- Outstanding balances.
- Refund requests.
- Refund outcomes.
- Disputes.
- Revenue allocations.
- Payouts.

Examples:

- A cancelled booking can have a pending refund.
- A completed booking can have an unpaid balance.
- An ended-early booking can have a disputed charge.
- A successful payment can require booking-resolution review.

Financial corrections must preserve historical records.

### 27. Two-Provider Bookings

Record allowed transitions, responsible actors, guards, timeouts, side effects, and conflicts.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Do not enable live paired bookings until rules define:

- Required subscriptions.
- Consent and approval from both providers.
- Availability for both.
- Which account manages the booking.
- Price composition.
- Deposit and balance allocation.
- Cancellation by one participant.
- Replacement requests.
- Refunds.
- Payouts.
- Review association.

A linked provider profile does not establish agreement to participate.

### 28. Notifications

For **notifications**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Notify relevant participants of consequential events, including:

- Request submitted.
- Revision proposed.
- Acceptance.
- Decline.
- Payment required.
- Confirmation.
- Expiry.
- Cancellation.
- Financial resolution where applicable.

Notifications are secondary to stored booking state.

A failed email must not erase a confirmed booking.

Avoid exposing private venue details or sensitive notes in
unauthenticated previews.

Use recoverable delivery for important notifications.

### 29. Audit and Concurrency

For **audit and concurrency**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Record consequential transitions with:

- Actor or trusted service.
- Previous and new state.
- Timestamp.
- Relevant version.
- Reason.
- Related payment or event reference where applicable.

Protect against:

- Double submission.
- Concurrent acceptance.
- Payment against an old quote.
- Duplicate provider events.
- Concurrent cancellation and confirmation.
- Repeated refund execution.

Use appropriate database constraints, transactions, version checks,
and idempotency controls.

Do not rely on disabled buttons for concurrency protection.

### 30. Required Verification

Record scenario IDs, observable pass and fail conditions, the tested environment, actual results, evidence, and who accepts exceptions.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Before live booking use, verify:

- Only eligible accounts can submit requests.
- Only participants can retrieve private booking information.
- Providers cannot accept unrelated requests.
- Material revisions require acceptance.
- Accepted prices remain stable after rate edits.
- Booking conflicts are prevented.
- Payment amounts are server-calculated.
- Duplicate events do not duplicate confirmation.
- Expired reservations handle late payment correctly.
- Cancellation and refund states remain distinct.
- Early-ending calculations match the approved policy.
- Existing obligations remain manageable after entitlement changes.
- Blocking does not silently alter financial records.
- Notification failures can be recovered.
- Time-zone and daylight-saving cases are handled.

Record the tested conditions and any limitations.

### 31. Open Decisions

Record the unresolved question, viable options, decision owner, required evidence, and work blocked by the decision.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Track confirmation in ../decisions.md.

Required decisions include:

- Single deposit versus separate request fee.
- Deposit calculation basis.
- Reservation duration and timing.
- Request-response deadlines.
- Start and completion confirmation.
- Remaining balance collection.
- Booking amendments.
- Cancellation formulas.
- Early-ending calculations.
- Non-attendance and lateness.
- Expenses and taxes.
- Refund and dispute authority.
- Existing-booking access after subscription expiry.
- Effects of account restrictions and blocks.
- Two-provider booking rules.
- Review eligibility.
- Notification channels.

Do not label the lifecycle production-ready while required rules
remain unresolved.

### 32. Final Rule

For **final rule**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Preserve the agreement, verify the money, protect availability,
and keep outcomes explainable.

A request is not acceptance.
Acceptance is not payment.
Payment is not attendance.
Completion is not payout.

