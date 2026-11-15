# MeetDiscreet — Booking Lifecycle

## 1. Purpose and Status

Define how booking requests become agreed experiences, how changes
are handled, and how booking records relate to payments.

This is the intended lifecycle.
It does not establish implementation or live payment readiness.

Read alongside:

- ../../AGENTS.md
- ./product_spec.md
- ./access_matrix.md
- ./pricing_and_payments.md
- ../decisions.md
- ../architecture/application_architecture.md
- ../architecture/data_model.md

Financial amounts and calculation rules belong in
pricing_and_payments.md.

If a required policy remains unresolved, do not invent it.

## 2. Core Principles

- A subscription unlocks booking requests, not a guaranteed booking.
- Companions choose which requests to accept.
- Material revisions require agreement.
- Accepted terms must be preserved.
- Payment confirmation requires trusted verification.
- Availability must be protected against concurrent bookings.
- Either participant can end an interaction.
- Financial consequences follow the confirmed policy.
- Booking, payment, refund, dispute, and payout states remain distinct.

Do not promise that payment guarantees attendance or safety.

## 3. Booking Participants

A standard booking identifies:

- Requesting user.
- Selected companion.
- Selected companion presentation.
- Authorized operational staff where necessary.

An unrelated account cannot view or modify the booking.

Two-companion bookings require additional confirmed rules before
live use.

Do not assume the primary companion can accept on another
companion’s behalf.

## 4. Booking Record

Store the information needed to understand the agreement:

- Booking identifier.
- Requesting account.
- Companion account.
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

## 5. Lifecycle Overview

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

## 6. Booking States

| State | Meaning |
|---|---|
| draft | Requester is preparing an unsubmitted request |
| requested | Request submitted for companion review |
| revision_requested | Revised terms await the other participant’s response |
| accepted_awaiting_deposit | Both sides have agreed terms; required deposit is not yet verified |
| confirmed | Required payment and reservation conditions are satisfied |
| in_progress | Experience has started under the approved start process |
| completed | Experience concluded under the approved completion process |
| ended_early | Experience stopped before its agreed end |
| declined | Companion rejected the request |
| withdrawn | Requester withdrew before confirmation |
| expired | An applicable response or payment deadline elapsed |
| cancelled | A confirmed booking was cancelled |

Do not use a status change as a substitute for recording the reason,
actor, and timestamp.

Completion, start, and early-ending confirmation processes remain
to be selected.

## 7. Preparing a Draft

Only the requester can edit their own draft.

The form supports:

- Companion and presentation.
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

## 8. Submitting a Request

Before accepting submission, the backend checks:

- Session validity.
- Requester eligibility.
- Relevant companion subscription.
- Companion eligibility.
- Presentation ownership.
- Offering availability.
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

## 9. Companion Review

The companion can:

- Accept the submitted terms.
- Decline.
- Propose revisions.

Show relevant request information and price components.

Do not expose unrelated private user information.

A request alone does not occupy a confirmed booking slot.

Whether pending requests create any temporary availability effect
must be explicitly defined.

## 10. Revisions

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

## 11. Agreement and Acceptance

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

If the companion simply accepts the requester’s unchanged proposal,
record that both parties agreed to that exact version.

## 12. Reservation Policy

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
companion time.

## 13. Deposit Collection

Proposed model:

- Collect one 10% deposit after acceptance.
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

## 14. Payment Confirmation

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

## 15. Confirming the Booking

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

## 16. Late or Conflicting Payment Outcomes

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

## 17. Amendments After Confirmation

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

## 18. Starting the Experience

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

## 19. Completing the Experience

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

## 20. Early Ending

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

## 21. Withdrawal, Decline, and Expiry

### Withdrawal

The requester withdraws before confirmation.

Determine financial consequences from actual payment state,
not merely the booking label.

### Decline

The companion rejects the request.

Do not create a new charge because a request was declined.

### Expiry

A configured response or payment deadline passes.

Release applicable holds safely.

If no deadline has been selected, do not implement arbitrary expiry.

Persist the reason and relevant deadline.

## 22. Cancellation After Confirmation

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

Distinguish user cancellation from companion cancellation.

Do not describe a refund as completed before provider confirmation.

Cancellation must remain possible through an appropriate support route
if a participant cannot use the normal interface.

## 23. Non-Attendance and Lateness

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

## 24. Subscription Expiry and Account Restrictions

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

## 25. Blocking

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

## 26. Separate Financial and Dispute States

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

## 27. Two-Companion Bookings

Do not enable live paired bookings until rules define:

- Required subscriptions.
- Consent and approval from both companions.
- Availability for both.
- Which account manages the booking.
- Price composition.
- Deposit and balance allocation.
- Cancellation by one participant.
- Replacement requests.
- Refunds.
- Payouts.
- Review association.

A linked companion profile does not establish agreement to participate.

## 28. Notifications

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

## 29. Audit and Concurrency

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

## 30. Required Verification

Before live booking use, verify:

- Only eligible accounts can submit requests.
- Only participants can retrieve private booking information.
- Companions cannot accept unrelated requests.
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

## 31. Open Decisions

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
- Two-companion booking rules.
- Review eligibility.
- Notification channels.

Do not label the lifecycle production-ready while required rules
remain unresolved.

## 32. Final Rule

Preserve the agreement, verify the money, protect availability,
and keep outcomes explainable.

A request is not acceptance.
Acceptance is not payment.
Payment is not attendance.
Completion is not payout.