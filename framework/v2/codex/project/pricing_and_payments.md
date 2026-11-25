# [Application name] — Pricing and Payments

**Owner** [Role]  
**Scope and revision** [Milestone or version]  
**Status and review date** [Draft / Approved / Verified, date]

Complete each applicable section with project-specific values and evidence. The detailed reference material describes an illustrative marketplace. Adapt its actors, rules, tools, limits, and workflows to your project. Mark inapplicable sections with a short reason. Treat unapproved choices as proposed or pending.

## Quick-start worksheet

**Owner and review date** [Role, date]  
**Markets and currency** [Regions, ISO currency codes]  
**Release and decision status** [Version, confirmed or proposed]

### Commercial products and price catalogue

Use one row per price and version. Identify the authoritative source for approved amounts, renewal terms, taxes, and eligibility.

| Offer and version | Amount and currency | Charge model and term | Eligibility and benefits | Expiry or renewal | Source and status |
| --- | --- | --- | --- | --- | --- |
| [Plan, purchase, allowance, or upgrade] | [Minor units and currency] | [One-time / recurring / usage] | [Grant and scope] | [Cadence or end date] | [Decision ID] |

Define allowance consumption and rollover, recurring access, optional upgrades, price changes, and treatment of existing subscribers. Use [Access Matrix](access_matrix.md) to describe what each grant unlocks.

### Quotes, deposits, and checkout

Record the quote inputs, effective price version, rounding, fees, tax, and total. If deposits apply, define what the deposit is based on, when it is due, remaining balance, and how amendments or an expired quote affect the transaction. Specify customer disclosures before consent and what appears on receipts. See [Booking Lifecycle](booking_lifecycle.md).

### Payment and entitlement processing

| Event | Trusted source | Deduplication and ordering | Financial effect | Entitlement effect | Recovery |
| --- | --- | --- | --- | --- | --- |
| [Paid, failed, refunded, disputed or renewed] | [Verified provider event or approved action] | [Key and replay handling] | [Ledger change] | [Grant, revoke or retain] | [Retry or reconciliation] |

Document pending states, retry and reconciliation, sandbox versus live mode, and operator permissions. Specify financial records visible to each role and what payment data the app retains.

### Refunds, disputes, allocations, and payouts

Define eligibility and amounts for cancellations, no-shows and early endings where applicable. Document allocation bases, taxes, processing costs, rounding, payout schedule, adjustments, and ownership of unreconciled balances.

### Verification and open financial decisions

Test calculation examples, checkout disclosures, failed and duplicate events, renewal, entitlement expiry, refunds, chargebacks, reconciliation, and price versioning. Record pending financial decisions in the [Decision Register](decisions.md) and results in [Launch Acceptance](launch_acceptance.md).

## Detailed template

Use these fields for the detailed records in this document.

| Offer or event | Amount and currency / rule | Eligibility and timing | Ledger and entitlement effects | Exceptions | Approval and test |
| --- | --- | --- | --- | --- | --- |
| [Fill in] | [Fill in] | [Fill in] | [Fill in] | [Fill in] | [Fill in] |

### 1. Purpose and Status

Record the actual release, what is applicable today, what remains proposed or deferred, and the latest supporting reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Define [Application name]’s prices, purchase types, revenue allocations,
billing behaviour, and unresolved financial rules.

This document describes intended requirements.
It does not establish that a payment provider or financial workflow
has been implemented.

Read alongside:

- [Project reference for AGENTS]
- [Product Spec](product_spec.md)
- [Access Matrix](access_matrix.md)
- [Booking Lifecycle](booking_lifecycle.md)
- [Decisions](decisions.md)
- [Application Architecture](application_architecture.md)
- [Application Security](application_security.md)

Use this document as the authoritative financial specification.

Keep executable pricing centralized in the application.
Do not maintain independent hardcoded prices across pages.

### 2. Decision Status

Record the actual release, what is applicable today, what remains proposed or deferred, and the latest supporting reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Distinguish:

- Established amount: retained from the source model.
- Proposed interpretation: recommended but not confirmed.
- Pending policy: requires a decision before dependent live use.
- Implemented: verified in the application.
- Operational: verified with the selected provider and environment.

Established amounts do not mean every surrounding billing policy
has been approved.

Do not treat recommendations as confirmed decisions.

### 3. Currency and Operating Region

For **currency and operating region**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Launch region and currency remain pending.

Record each approved amount and its currency.

Before live checkout:

- Select the currency explicitly.
- Confirm supported charge and payout countries.
- Confirm provider suitability for the actual business.
- Establish tax treatment.
- Determine whether displayed prices include applicable tax.
- Define currency-conversion responsibility, if relevant.

Do not infer [currency code] merely from [Decision owner]’s location.

Do not enable multiple currencies without a defined conversion,
rounding, pricing, and settlement approach.

### 4. Commercial Products

For **commercial products**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

[Application name] has distinct purchase types:

1. Provider publishing.
2. Individual provider subscriptions.
3. Premium user membership.
4. Additional [offer listing] ads.
5. Listing boosts.
6. Advertising appearance and placement upgrades.
7. Booking payments.

Keep these separate in:

- Product identifiers.
- Checkout descriptions.
- Entitlements.
- Receipts.
- Revenue records.
- Refund handling.

A premium membership is not a provider subscription.

A provider subscription is not payment for a booked date.

### 5. Price Catalogue

Duplicate catalogue rows as needed. Record the approved price and version, currency, tax treatment, unit or cadence, effective date, and provider reference for each item.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

| Product | Established price | Period or unit |
|---|---:|---|
| User registration | Free | Account creation |
| User profile creation | Free | Profile |
| Provider registration | Free | Account creation |
| Unpublished provider profile editing | Free | Profile |
| Individual provider subscription | [amount] | Monthly, per provider |
| Premium user membership | [amount] | Monthly |
| Provider publishing — monthly | [amount] | Monthly |
| Provider publishing — annual | [amount] | Twelve months |
| Additional [offer listing] ad | [amount] | Per ad, per [number of days] |
| Additional boost | [amount] | Per boost |
| Near-top placement | [amount] | [placement duration] |
| Listing thumbnail | [amount] | Duration pending |
| Listing colour and framing | [amount] | Duration pending |

Monthly and annual publishing are alternative plans.
Do not charge both for the same coverage period by default.

Do not change the annual price because it differs substantially
from twelve monthly payments.

### 6. Provider Publishing

For **provider publishing**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

An eligible active publishing plan provides:

- Published provider profile.
- Both permitted presentations under the publishing account.
- One included [offer listing] ad.
- One included boost for that ad per [allowance period] period.

Publishing remains subject to eligibility and moderation.

Free account creation and editing do not themselves publish a profile.

#### Policies Still Required

For **policies still required**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

- Automatic renewal or manual renewal.
- Billing anniversary.
- Monthly/annual switching.
- Proration or deferred plan changes.
- Cancellation timing.
- Failed-payment handling.
- Grace periods.
- Refund eligibility.
- Profile and ad visibility after expiry.
- Effects on existing subscribers.
- Effects on communication and bookings.

Do not silently remove access to necessary transaction records
when publishing expires.

### 7. Individual Provider Subscriptions

For **individual provider subscriptions**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Price: [amount] per month for each selected provider.

An active subscription unlocks that provider’s defined:

- Subscriber-only profile content.
- Additional photos.
- Uploaded videos.
- Detailed experience catalogue and add-on prices.
- Messaging.
- Audio/video calls.
- Booking requests.

It does not include the separately priced booked experience.

#### Gross Allocation

Percentages and amounts in the example refer to different quantities. Fill in each share separately, then show an exact calculation and a rounded allocation that sums to the charge.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

- Provider: [rate].
- Platform: [rate].

For an [amount] subscription:

- Exact mathematical provider share: [amount].
- Exact mathematical platform share: [amount].
- Illustrative cent-rounded allocation: [amount] and [amount].

The executable rounding rule remains to be confirmed.

Do not round independently in ways that create or lose money.

#### Policies Still Required

For **policies still required**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

- Automatic renewal.
- Cancellation timing.
- Failed payments and retries.
- Grace periods.
- Refund consequences.
- Access after expiry.
- Existing-booking communication after expiry.
- Behaviour when the provider stops publishing.
- Behaviour when either account is suspended.
- Subscription coverage across both presentations.

### 8. Premium User Membership

For **premium user membership**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Price: [amount] per month.

Benefits:

- Up to three active [request listing] posts.
- Two included boosts per post per [allowance period] period.
- Additional boosts at [amount] each.

The membership fee is allocated to the platform before any separately
defined processing costs, taxes, refunds, or adjustments.

Premium does not unlock provider content, messaging, calls,
or booking requests.

#### Policies Still Required

For **policies still required**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

- Automatic renewal.
- Allowance-period boundaries.
- Carryover, if any.
- Failed-payment handling.
- Excess-post treatment after expiry.
- Treatment of unused included boosts.
- Cancellation and refunds.

Do not delete excess posts or consume unrelated allowances by assumption.

### 9. Free [request listing] Allowance

For **free [request listing] allowance**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Proposed interpretation:

- One active [request listing] post per free account.
- Each post expires after [number of days].
- Additional boosts cost [amount] each.

The original wording was “one free posting per account.”
Confirm that this means one active post rather than one lifetime post.

Define:

- Replacement after removal.
- Republication after expiry.
- Whether editing changes expiry.
- Whether renewal creates a new post.
- How allowances are counted during pending moderation.

Editing must not become an undocumented free boost.

### 10. [offer listing] Ads

For **[offer listing] ads**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Included with eligible publishing:

- One [offer listing] ad.
- One included boost per [allowance period] period.

Additional ads:

- [amount] per ad per [number of days].
- One included boost per additional ad.

#### Policies Still Required

For **policies still required**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

- Included-ad lifetime.
- Additional-ad renewal.
- Whether recurring billing is used.
- Effect of publishing expiry during a paid ad period.
- Effect of moderation removal.
- Refunds when publication cannot be delivered.
- Boost allowance timing.
- Whether unused boosts carry over.
- Consequences of changing posting areas.

Do not describe a one-time purchase as recurring or vice versa
without a confirmed rule.

### 11. Boosts

For **boosts**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Price: [amount] per additional boost.

A boost returns a listing to the top of the chronological listing order,
subject to defined sponsored-placement ordering.

A boost does not extend the post’s expiry.

Enforce eligibility and allowance consumption on the backend.

Concurrent requests must not spend the same included boost twice.

#### Policies Still Required

For **policies still required**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

- Immediate use versus stored boost credit.
- Refunds for failed boosts.
- Ordering when boosts occur together.
- Whether purchase and execution are one operation.
- Treatment when a post expires during processing.
- Restrictions on repeated rapid boosting.

If payment succeeds but placement fails, record a recoverable outcome.
Do not silently retain money for an undelivered action.

### 12. Advertising Upgrades

#### Near-Top Placement

For **near-top placement**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Price: [amount] for [placement duration].

Confirm:

- When the period begins.
- Placement ordering among simultaneous purchases.
- Eligible browsing areas.
- Effect of post expiry.
- Effect of suspension or removal.
- Whether the same post can purchase overlapping periods.

Do not promise an exclusive first position unless that is explicitly
the approved product.

#### Thumbnail

For **thumbnail**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Price: [amount].

Duration remains pending.

#### Colour and Framing

For **colour and framing**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Price: [amount].

Duration remains pending.

For each upgrade, specify:

- Scope.
- Start and end.
- Eligible listing.
- Delivery status.
- Refund treatment.
- Whether it follows a renewed ad.

Identify paid placement appropriately.

### 13. Booking Prices

Record the exact approved rule, calculation basis, timing, authority, and behavior for failures, late events, and retries.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Providers set permitted experience rates.

A quote may include:

- Base duration.
- Base rate.
- Included activities.
- One-time add-ons.
- Hourly add-ons.
- Approved presentation requests.
- Agreed expenses.
- Applicable taxes.
- Other explicitly approved charges.

Define minimum durations, increments, and rounding before implementation.

Clearly distinguish:

- Estimated quote.
- Provider-proposed revision.
- User-accepted price.
- Actual amount due.
- Amount already paid.
- Refunds.
- Outstanding balance.

Freeze the accepted price and relevant policy version.

Later profile-rate changes must not rewrite existing agreements.

### 14. Booking Deposit — Proposed Interpretation

Record the exact approved rule, calculation basis, timing, authority, and behavior for failures, late events, and retries.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

The proposed model uses one deposit:

- [rate] of the agreed booking price.
- Collected after provider acceptance.
- Credited toward the booking total.
- Platform allocation: [rate] of the deposit.
- Provider allocation: [rate] of the deposit.

Example:

| Item | Amount |
|---|---:|
| Agreed booking price | [amount] |
| Deposit | [amount] |
| Platform deposit allocation | [amount] |
| Provider deposit allocation | [amount] |
| Remaining booking balance | [amount] |

Under this example, the platform allocation equals [rate] of the booking
price before other costs.

Do not describe it as a [rate] platform commission on the full booking.

#### Source Ambiguity

For **source ambiguity**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

The source model describes both:

- A deposit after acceptance.
- A booking-request fee at submission.

It does not clearly establish whether these are one charge or two.

The single-deposit interpretation requires confirmation.

Do not implement both charges or silently choose a collection point.

### 15. Deposit Basis and Remaining Balance

Record the exact approved rule, calculation basis, timing, authority, and behavior for failures, late events, and retries.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Before live bookings, confirm whether the deposit is calculated on:

- Base time only.
- Time and add-ons.
- Expenses.
- Taxes.
- The complete accepted total.

Also confirm:

- Who collects the remaining balance.
- When it becomes payable.
- Whether it is collected through the platform.
- Supported payment methods.
- Whether the platform receives any share of the balance.
- Handling of unpaid balances.
- Booking extensions and additional charges.

The original deposit split does not define a commission on the
remaining balance.

Do not invent one.

### 16. Cancellation, Non-Attendance, and Early Ending

For **cancellation, non-attendance, and early ending**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Both participants may end an interaction.

Financial outcomes must follow an explicit, understandable policy.

The source model combines:

- A normally non-refundable deposit.
- Payment for actual time provided when a session ends early.

Before implementation, reconcile these statements.

Define outcomes for:

- User cancellation before acceptance.
- User cancellation after acceptance but before payment.
- User cancellation after payment.
- Provider cancellation.
- User non-attendance.
- Provider non-attendance.
- Late arrival.
- Early ending by either participant.
- A materially misrepresented experience.
- A disputed outcome.
- Agreed nonrecoverable expenses.

Specify whether a retained deposit is:

- A minimum total charge.
- A separately defined cancellation charge.
- Credited against actual time with a stated retention floor.
- Subject to another explicitly approved calculation.

Do not imply that both “only actual time is charged” and an additional
retained amount apply without explaining the calculation.

Avoid absolute “no refunds under any circumstances” claims.

Final terms must reflect applicable obligations and the selected
provider’s requirements.

### 17. Taxes, Processing Costs, and Gross Allocations

For **taxes, processing costs, and gross allocations**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Source percentages describe intended allocations.
They do not establish net take-home amounts.

Confirm:

- Tax responsibility.
- Tax-inclusive or tax-exclusive display.
- Processing-fee responsibility.
- Refund processing costs.
- Chargeback costs.
- Currency-conversion costs.
- Payout costs.
- How costs affect platform and provider shares.

Do not subtract undisclosed costs from provider earnings.

Keep tax amounts and fee adjustments distinguishable in records.

### 18. Payouts

Record the exact approved rule, calculation basis, timing, authority, and behavior for failures, late events, and retries.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

An allocation is not a completed payout.

Track separately:

- Gross amount.
- Platform allocation.
- Provider allocation.
- Fees and taxes.
- Refund adjustments.
- Disputed amounts.
- Available amount.
- Pending payout.
- Confirmed payout.

Before live payouts, define:

- Recipient eligibility and onboarding.
- Payout schedule.
- Availability delay.
- Minimum payout, if any.
- Holds and reserves.
- Failed payout handling.
- Negative balances.
- Recovery of reversed transactions.
- Responsibility for refunds after payout.

Do not describe funds as held in escrow unless the actual arrangement
supports that description.

Do not build an internal stored-value wallet by implication.

### 19. Checkout Presentation

For **checkout presentation**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Before payment, show:

- Identified product or provider.
- Currency.
- Amount due now.
- Relevant taxes or fees.
- Renewal frequency, if recurring.
- What the purchase unlocks.
- What it does not include when necessary for clarity.
- Cancellation access.
- Relevant deposit or refund terms.

Keep disclosure concise and transaction-specific.

Link to detailed policies rather than repeating the full guidelines page.

Do not preselect paid extras without an approved, transparent design.

Never use misleading countdowns or fabricated scarcity.

### 20. Payment Processing

Record the exact approved rule, calculation basis, timing, authority, and behavior for failures, late events, and retries.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

The backend must:

1. Validate account and purchase eligibility.
2. Determine the authoritative product and amount.
3. Record a recoverable purchase state.
4. Create the provider transaction.
5. Verify provider confirmation.
6. Apply valid financial and entitlement transitions.
7. Preserve audit and reconciliation information.

Do not trust client-submitted prices or payment-success flags.

A checkout return URL is not proof of payment.

Avoid placing full payment credentials in application storage.
Use provider-supported payment collection.

### 21. Webhooks and Idempotency

For **webhooks and idempotency**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Verify payment events using the provider’s supported mechanism.

Handle:

- Duplicate delivery.
- Delayed events.
- Out-of-order events.
- Processing interruptions.
- Failed event handling.
- Provider-side changes missed locally.

Store relevant provider references.

Use database constraints and transactional updates where appropriate.

Do not:

- Duplicate entitlements.
- Duplicate revenue allocations.
- Apply a refund twice.
- Overwrite a newer state with an older event.
- Lose a paid purchase because the browser closed.

Provide reconciliation for incomplete or inconsistent records.

### 22. Refunds and Disputes

Record the exact approved rule, calculation basis, timing, authority, and behavior for failures, late events, and retries.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Keep refund state separate from payment and booking state.

Record:

- Original payment.
- Requested amount.
- Reason.
- Decision and authority.
- Provider refund reference.
- Processing status.
- Completed amount.
- Allocation adjustments.
- Entitlement consequences.

A refund request is not a completed refund.

A cancelled booking is not proof of repayment.

Define chargeback handling, including:

- Evidence access.
- Account restrictions.
- Entitlement effects.
- Provider allocation adjustments.
- Payout consequences.

Do not use account deletion to erase financial history required
for reconciliation.

### 23. Receipts and Financial Visibility

Record the exact approved rule, calculation basis, timing, authority, and behavior for failures, late events, and retries.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Purchasers can view their own relevant:

- Purchases.
- Charges.
- Currency.
- Product descriptions.
- Dates.
- Renewal status.
- Refunds.
- Booking balances.
- Receipts.

Providers can view their own allocations and payout records.

Operational staff receive only the financial access their duties require.

Receipts must reflect actual transactions.
Do not issue a payment receipt for a pending or failed charge.

### 24. Rounding and Calculation Integrity

For **rounding and calculation integrity**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Use integer minor currency units.

Confirm whether the selected currency uses the assumed minor-unit precision.

Define:

- Percentage rounding method.
- Which allocation receives any remainder.
- Tax rounding.
- Partial refunds.
- Time increments.
- Add-on calculation.
- Deposit basis.
- Multi-provider allocation.

Ensure allocated parts sum to the amount being allocated.

Preserve calculation inputs or snapshots sufficient to explain
historical charges.

Do not parse formatted display strings as financial authority.

### 25. Price and Plan Changes

Record the exact approved rule, calculation basis, timing, authority, and behavior for failures, late events, and retries.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Price changes require explicit authorization.

Define before supporting plan changes:

- New-customer effective date.
- Existing-subscriber treatment.
- Required notices.
- Renewal amount.
- Proration.
- Grandfathered prices.
- Refund implications.

Store historical transaction amounts independently of current catalogue
prices.

Changing a public price must not rewrite past receipts or accepted quotes.

### 26. Required Verification

Record scenario IDs, observable pass and fail conditions, the tested environment, actual results, evidence, and who accepts exceptions.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Before releasing dependent payment functionality, verify:

- Correct product and account are charged.
- Currency and amount match backend calculations.
- Provider subscriptions remain isolated.
- Premium membership does not unlock provider access.
- Publishing and premium are billed separately.
- Failed payments do not grant unapproved access.
- Duplicate events do not duplicate allocations.
- Interrupted checkout can be reconciled.
- Refunds and disputes follow confirmed rules.
- Boost purchases cannot be double-spent.
- Booking deposits use the confirmed basis.
- Remaining balances are calculated correctly.
- Payout displays distinguish allocated and paid amounts.
- Receipts match provider-confirmed transactions.
- Test and live environments are separated.

Use test-mode transactions until live use is authorized and ready.

### 27. Open Financial Decisions

Record the exact approved rule, calculation basis, timing, authority, and behavior for failures, late events, and retries.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Track confirmations in ../decisions.md.

Required decisions include:

- Currency and launch region.
- Payment and payout provider.
- Recurring versus manual renewal for each product.
- Plan-switching behaviour.
- Allowance-period boundaries and carryover.
- Free-post interpretation.
- Included-ad lifetime.
- Upgrade durations.
- Sponsored-placement ordering.
- Single deposit versus separate request fee.
- Deposit calculation basis.
- Remaining balance collection.
- Cancellation and early-ending formulas.
- Expenses and taxes.
- Processing-cost allocation.
- Rounding.
- Refund and dispute consequences.
- Payout timing and holds.
- Two-provider payment allocation.
- Expiry-related entitlements.

Resolve each policy before its dependent live transaction is enabled.

### 28. Final Rule

For **final rule**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Preserve established prices.
Resolve ambiguous financial rules explicitly.
Calculate on the backend.
Verify provider events.
Keep charges, allocations, refunds, and payouts distinguishable.

Never describe an estimate, pending payment, or allocated earning
as confirmed money received.

