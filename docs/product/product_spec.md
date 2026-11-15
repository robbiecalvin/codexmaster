# MeetDiscreet — Product Specification

## 1. Purpose and Status

Define what MeetDiscreet must do.

This document describes intended functionality, not verified implementation.

Use alongside:

- ../../AGENTS.md
- ../project_context.md
- ../decisions.md
- ../next_steps.md
- ./access_matrix.md
- ./pricing_and_payments.md
- ./booking_lifecycle.md
- ./content_and_boundaries.md
- ../design/page_inventory.md
- ../architecture/application_architecture.md

Some referenced documents may be created later.

Detailed financial rules belong in pricing_and_payments.md.
Detailed permissions belong in access_matrix.md.
Detailed booking transitions belong in booking_lifecycle.md.

Do not silently resolve contradictions between these documents.
Record and resolve material conflicts.

## 2. Product Definition

MeetDiscreet is a marketplace for paid platonic dates and social experiences.

Users discover companions through public listings, explore profiles,
subscribe to individual companions, communicate, and request bookings.

Companions publish profiles, advertise experiences, manage availability,
and accept or decline requests.

Examples of experiences include:

- Coffee and conversation.
- Dinner.
- Concerts.
- Cinema and theatre.
- Museums and galleries.
- Sightseeing.
- Shopping.
- Board games.
- Language practice.
- Celebrations and formal events.
- Other approved social activities.

The current release does not offer sexual services or erotic content.

Future scope changes require explicit revised requirements.
Do not implement unspecified future functionality.

## 3. Product Goals

- Make discovery relevant.
- Clarify interests, offerings, prices, and expectations.
- Reduce unsolicited and speculative contact through defined access gates.
- Keep communication within the application.
- Give participants control over visibility and interaction.
- Support recurring companion income and platform revenue.
- Make bookings and financial obligations understandable.

Payment does not establish trustworthiness, authenticity, or safety.
Do not make unsupported guarantees.

## 4. Participants and Account States

### Visitor

Can access public discovery and public information after entrance confirmation.

### Registered User

Can create a profile, manage permitted posts, and purchase memberships,
companion subscriptions, or other eligible products.

### Companion

Can create presentations, purchase publishing, advertise offerings,
manage rates and availability, and respond to bookings.

### Moderator

Can perform specifically assigned moderation functions.

### Administrator

Can perform authorized operational and configuration functions.

Roles and paid entitlements are distinct.

Whether one account may act as both user and companion remains pending.

Account lifecycle states must distinguish active access from restrictions,
suspension, and deletion handling.

Do not let clients assign privileged roles.

## 5. Entrance Age Gate

Before normal browsing, show a concise entrance confirmation with:

- “I am 18 or older.”
- An exit action.
- Accessible keyboard and screen-reader behaviour.
- Responsive presentation.
- No interaction with underlying content while active.

Apply the gate to direct visits, not only the homepage.

Preserve the intended destination after confirmation.

The retention period remains pending.

Entrance confirmation is self-attestation.
It does not replace account eligibility or identity verification.

Guidelines, Privacy, Terms, and the exit route must remain reachable
without requiring someone to falsely confirm eligibility.

## 6. Registration and Authentication

Support:

- Free registration.
- Sign-in.
- Confirmation where required by the selected authentication system.
- Password recovery where applicable.
- Logout.
- Session expiry handling.
- Account settings.

Use an approved authentication provider.

Private contact information must not become public profile information
merely because it was collected during registration.

The eligibility and verification approach must be confirmed before launch.

## 7. User Profiles

Required product fields:

- Username.
- Adult age information sufficient for the approved eligibility process.
- Gender field with an appropriate non-disclosure option.

Optional fields:

- Display name.
- General location.
- Profile picture.
- Orientation.
- Interests.
- Languages.
- What I’m Looking For.
- What I Enjoy.
- Relevant accessibility preferences.

Do not publish full birth dates, precise addresses, or private contact
details by default.

User-profile field visibility must be confirmed in the access matrix.
Do not assume the entire user profile is public.

Users can edit their own permitted fields.

## 8. Companion Profiles

### Account-Level Information

- Account ownership.
- Adult age.
- Gender.
- Optional ethnicity.
- Languages.
- General location.
- Availability.
- Publishing status.
- Verification association, where implemented.

### Public Information

- Display name.
- Username.
- General location.
- Profile picture.
- Tagline.
- Preferred date style.
- Optional zodiac sign.
- General rates.
- Public reviews.

### Member-Only Information

- Bio.
- Interests.
- Conversation topics.
- What I Enjoy.
- What Doesn’t Work for Me.
- Ideal activities.
- Boundaries.
- Optional orientation.
- Optional “A Date to Remember” story.
- Up to three additional gallery photos.
- Permitted appearance and wardrobe information.

### Subscriber-Only Information and Actions

- Further gallery photos.
- Uploaded videos.
- Detailed experiences.
- Add-on prices.
- Requested presentation options.
- Messaging.
- Audio/video calls.
- Booking requests.

Backend responses must respect field visibility.

Do not expose restricted information through public metadata,
search results, notifications, or listing previews.

## 9. Companion Presentations

Allow up to two presentations under one companion account.

Each presentation may have different:

- Introductory content.
- Photos.
- Videos.
- Appearance and style information.
- Experiences.
- Rates.
- Linked second-companion information where applicable.

Both share:

- Account ownership.
- Verification association.
- Publishing account.
- Enforcement history.

Record the presentation selected for a booking.

Proposed rule:
one companion subscription unlocks both presentations.

This requires confirmation.

Do not represent the presentations as unrelated verified identities.

## 10. Appearance and Presentation Fields

Optional member-level fields may include:

- Height.
- Weight.
- Body type.
- Natural hair colour.
- Natural hair length.
- Eye colour.
- Personal style.
- Relevant clothing or costume sizes.

Subscriber-level presentation choices may include:

- Available outfits.
- Wigs or hairstyles.
- Costume accessories.
- Other approved event presentation options.

Requested changes require companion agreement.

Any charge must appear in the agreed quote.

Do not include intimate measurements or sexual preference fields.

## 11. Media

Support:

- Public profile photo.
- Up to three additional member-visible gallery photos.
- Further subscriber-only gallery photos.
- Subscriber-only uploaded videos.
- Authorized message attachments.

Allow owners to upload, organize, replace, and remove permitted media.

Define before implementation:

- Allowed types.
- File-size and duration limits.
- Processing.
- Moderation.
- Retention.
- Deletion.
- Storage quotas.

These limits are not yet selected.

Protected originals must remain private.

Blurred previews must use safe preview assets rather than publicly
accessible originals hidden with CSS.

Removing media from a profile must follow defined storage and retention rules.

## 12. Experiences and Rates

Companions can select experiences they offer.

Each experience supports:

- Offered: yes/no.
- Included in hourly rate: yes/no.
- Extra amount when not included.
- One-time or hourly supplement.
- Description.
- Relevant restrictions or availability.

Disable extra-charge inputs when the experience is included.

Supported rate categories:

- Companion-arranged venue.
- User-selected approved venue.
- Extended evening or event attendance.
- Two-companion experience.
- Extended or overnight event attendance where offered.

Define duration, minimums, and expense responsibilities before checkout.

Extended attendance does not imply shared sleeping arrangements.

Public general rates and subscriber-only detailed add-ons must remain
distinct.

## 13. Two-Companion Experiences

Support:

- Indication of availability.
- Link to the other companion’s profile.
- Applicable public rate category.
- Identification of participants in the booking.

Before enabling live paired bookings, confirm:

- Whether both companions must approve.
- Whether the requester needs one or two subscriptions.
- Availability checks.
- Deposit and remaining-payment allocation.
- Payout responsibilities.
- Cancellation consequences.

Do not invent these rules from the existence of a profile link.

## 14. Publishing Plans

Companions can create accounts and edit unpublished profiles for free.

Publishing options:

- $19.99 monthly.
- $59.99 annually.

An active publishing plan includes:

- A live profile, subject to eligibility and moderation.
- One Offering ad.
- One included boost for that ad per 30-day period.

Both presentations belong to the publishing account.

Confirm behaviour when publishing expires, including:

- Public profile visibility.
- Existing ads.
- Existing subscribers.
- Messaging.
- Pending and confirmed bookings.

Do not infer that publishing payment bypasses moderation.

## 15. Individual Companion Subscriptions

Price: $11.99/month per companion.

Intended allocation:

- Companion: 75%.
- Platform: 25%.

An active subscription unlocks the specified companion’s:

- Subscriber media.
- Detailed experience information.
- Direct messaging.
- Audio calls.
- Video calls.
- Booking requests.

It does not include the booking’s separately priced companionship time.

Messaging has no numerical subscription allowance.
Appropriate anti-spam and abuse controls still apply.

Define renewals, cancellation, failures, refunds, grace periods,
and access after expiry in the financial and access specifications.

## 16. Premium User Membership

Price: $5.99/month.

Benefits concern Looking For posts only:

- Up to three active posts.
- Two included boosts per post per 30-day period.
- Additional boosts available for purchase.

Premium does not unlock companion media, communication, or bookings.

Confirm allowance behaviour when premium expires or payment fails.

Do not automatically delete posts without an approved rule.

## 17. Looking For Posts

Support:

- Title.
- General location.
- Desired activity.
- Description.
- Proposed date/time or flexibility.
- Optional budget if approved.
- Link to the user profile.
- Draft and preview.
- Publishing.
- Editing.
- Expiry.
- Boosting.
- Owner management.

Proposed free allowance:
one active post per account.

The original wording could mean a lifetime allowance.
Confirm the active-post interpretation.

Posts expire after 30 days.

Define republication, renewal, and edit effects on ordering.
Do not assume editing provides a free boost.

Visibility of full posts and user-profile details must be specified
in the access matrix.

## 18. Offering Ads

A companion with an eligible published profile can create Offering ads.

Public listings show:

- Clickable title.
- Age.
- Gender.
- General location.
- Purchased thumbnail where applicable.

The full ad contains permitted public information and links
to the companion’s profile or presentation.

Support:

- Draft.
- Preview.
- Publish.
- Edit.
- Ad management.
- Additional posting areas.
- Boosts.
- Paid upgrades.

Do not expose member-only or subscriber-only information in public ads.

The included ad’s lifetime relative to publishing must be confirmed.

## 19. Boosts and Advertising Upgrades

### Additional Offering Ads

- $5.99 per ad per 30 days.
- One included boost per additional ad.

### Additional Boosts

- $1.99 each.
- Return a listing to the top of the chronological list.
- Do not reset expiry.

### Optional Offering Upgrades

- Near-top placement: $9.99 for 24 hours.
- Profile thumbnail in the title: $2.99.
- Colour and framing: $3.99.

Thumbnail and styling durations remain unspecified.

Define:

- Placement ordering.
- Tie-breaking.
- Upgrade expiry.
- Interaction between boosts and paid placement.
- Included allowance periods.
- Refunds for failed delivery.
- Behaviour after edits, suspension, or deletion.

Paid placement must be identifiable.

Clients cannot assign paid status or boost balances.

## 20. Discovery

Support browsing by:

- Looking For or Offering.
- General location.
- Activity.
- Relevant gender preference.
- Availability where supported.
- Public price information where applicable.

Use chronological default ordering, modified by approved boosts
and sponsored-placement rules.

Support:

- Clear empty states.
- Loading and failure states.
- Filter reset.
- Suitable pagination or incremental loading.
- Useful return navigation.

Specific layouts and filter controls are decided during page design.

Do not expose precise private locations in discovery.

## 21. Messaging

Active subscriptions unlock messaging to the relevant companion.

Support:

- Text.
- Photos.
- Videos.
- Timestamps.
- Read receipts.
- Conversation history.
- Realtime updates.
- Appropriate notification controls.

Backend enforcement must check:

- Identity.
- Conversation membership.
- Entitlement.
- Account restrictions.
- Blocking.

Define:

- Historical read access after expiry.
- Attachment limits.
- Read-receipt controls.
- Retention.
- Deletion.
- Whether any booking-related communication continues after expiry.

Do not assume unlimited messaging requires continuous replies.

## 22. Audio and Video Calls

Support authorized in-app audio and video calling.

Include relevant controls and states:

- Call initiation.
- Incoming invitation.
- Accept and decline.
- Microphone mute.
- Camera control.
- End call.
- Permission denial.
- Missed call.
- Connection failure.
- Disconnection.

Use appropriate signaling and connectivity infrastructure.

Do not enable recording by default.

Calling permissions, browser support, and operational limits
must be verified before release.

## 23. Booking Requests

Subscribers can request bookings with a specific companion.

Capture:

- Companion and presentation.
- Date.
- Start time.
- Time zone.
- Duration.
- Venue or meeting area.
- Experiences.
- Add-ons.
- Accessibility requests.
- Presentation requests.
- Expenses and responsibility.
- Notes.
- Estimated price.
- Relevant acceptance.

Companion responses:

- Accept.
- Decline.
- Propose revisions.

Material revisions require requester acceptance.

Freeze the agreed quote and relevant policy version.

Do not silently apply later rate changes to accepted bookings.

## 24. Deposits and Completion

Proposed interpretation:

- One deposit equal to 10% of the agreed booking price.
- Collected after acceptance.
- Credited toward the booking total.
- Platform receives 10% of the deposit.
- Companion receives 90% of the deposit.

This remains pending confirmation.

The original plan also referred to a request fee at submission.
Do not implement both charges without an explicit decision.

Before live bookings, define:

- Reservation holds.
- Payment deadlines.
- Late payments.
- Remaining balance collection.
- Cancellation.
- Provider non-attendance.
- Early endings.
- Expense treatment.
- Refund eligibility.
- Disputes.
- Payout timing.

Either participant can end an interaction.

The financial treatment must clearly reconcile actual time,
retained deposits, and any approved expenses.
Do not leave contradictory promises in checkout copy.

## 25. Reviews

Support public reviews tied to eligible completed bookings.

Define:

- Eligible reviewer.
- Review period.
- Rating dimensions.
- Written feedback.
- Companion response.
- Editing.
- Reporting.
- Moderation.

Associate the review with the relevant presentation where appropriate.

Do not label unverified activity as a verified booking.

Do not publish sensitive booking details unnecessarily.

## 26. Blocking, Reporting, and Support

Users must be able to:

- Block another account where applicable.
- Report profiles, listings, media, reviews, and communication.
- Raise booking or payment concerns.
- Access support.

These functions must not require paid access.

Define blocking effects across:

- Discovery.
- Profile access.
- Messages.
- Calls.
- New bookings.
- Existing booking obligations.

Do not silently erase contractual or financial records when blocking.

Support reports without assuming an allegation is established fact.

## 27. Administration

Provide authorized tools for:

- Account and role management.
- Profile and listing review.
- Media review.
- Reports.
- Moderation actions.
- Booking disputes.
- Payment reconciliation.
- Revenue and payout visibility.
- Approved configuration changes.
- Audit history.

Use least-privilege access.

Moderators do not automatically receive unrestricted financial
or private-message access.

Record consequential actions and reasons.

Define operational effects of suspension before enabling it.

## 28. Billing and Earnings

Users can view relevant:

- Active plans.
- Renewal information.
- Cancellation controls.
- Payments.
- Receipts.
- Booking balances and refunds.

Companions can view relevant:

- Subscription allocations.
- Booking allocations.
- Fees where applicable.
- Refund adjustments.
- Pending and completed payouts.

Distinguish gross allocations from available earnings and actual payouts.

Do not label money as paid before payout confirmation.

Tax, processing-cost, and payout rules remain to be established.

## 29. Notifications

Provide useful notifications for applicable events, such as:

- Booking requests and revisions.
- Accepted bookings.
- Payment requirements.
- Messages.
- Calls.
- Subscription changes.
- Listing expiry.
- Moderation outcomes.

Select delivery channels and preferences explicitly.

Avoid exposing sensitive content in emails, push previews,
or unauthenticated screens.

Persist important events so a missed notification does not lose
the underlying action.

## 30. Design and Content Presentation

Build pages progressively.

Before each undesigned page:

1. Read existing design choices.
2. Ask focused visual questions.
3. Record the working direction.
4. Implement.
5. Preview and revise.

Robbie may request edits at any stage.

Keep shared components consistent without forcing every page
into the same layout.

Do not fabricate testimonials, activity counts, users, reviews,
or verification claims.

Synthetic fixtures must remain clearly distinguishable in development.

## 31. Policy Presentation

Detailed eligibility, content boundaries, prohibited conduct,
and general safety explanations belong on:

Community Guidelines & Boundaries

Do not repeat the full policy across normal pages.

Maintain concise transactional disclosures where needed.

Provide separate Terms, Privacy, and payment/cancellation information
for their actual purposes.

Store acceptance records for relevant versioned policies where required
by the approved onboarding and transaction process.

## 32. Technical and Quality Requirements

The frontend uses HTML, CSS, and JavaScript unless an approved
decision changes the approach.

Production requires trusted backend enforcement.

Requirements include:

- Responsive layouts.
- Accessible controls.
- Explicit loading and error states.
- Appropriate private storage.
- Server-side input validation.
- Ownership checks.
- Subscription isolation.
- Verified payment events.
- Idempotent financial processing.
- Booking concurrency controls.
- Safe upload handling.
- Appropriate logging and recovery.
- Environment separation.

No secrets or private customer data belong in the public repository.

Actual architecture and deployment choices remain separate decisions.

## 33. Future Adaptability

Keep content-specific definitions reasonably separate from:

- Accounts.
- Entitlements.
- Listings.
- Booking mechanics.
- Financial processing.
- Messaging infrastructure.

Do not implement a speculative second product.

Any later content-scope change requires revised requirements,
provider reassessment, and appropriate operational changes.

## 34. Open Decisions

Track resolution in ../decisions.md.

Outstanding decisions include:

- Launch region and currency.
- Domain and visual references.
- Backend, hosting, storage, and authentication.
- Payment and payout provider.
- Account role combinations.
- User-profile and Looking For visibility.
- Subscription coverage across presentations.
- Two-companion booking approval and payment rules.
- Free-post allowance interpretation.
- Publishing-expiry consequences.
- Premium-expiry consequences.
- Historical message access.
- Deposit versus request-fee interpretation.
- Booking cancellation and early-ending calculations.
- Remaining balance collection.
- Expenses, taxes, processing costs, and payouts.
- Advertising-upgrade durations and ordering.
- Media limits and retention.
- Verification process.
- Age-gate retention.
- Review eligibility details.
- Blocking consequences.
- Notification channels.
- Precise initial launch scope.

Do not treat an assistant recommendation as a confirmed owner decision.

## 35. Acceptance and Change Control

A feature is accepted against its concrete requirements and
relevant verification evidence.

Track separately:

- Implementation.
- Testing.
- Visual approval.
- Integration.
- Deployment.

Update this specification when an approved requirement changes.

Do not alter requirements merely to match incomplete implementation.

If a feature is deferred, retain it in the roadmap and make the
release scope explicit.

## 36. Final Rule

Preserve MeetDiscreet’s agreed marketplace features and payment gates.

Resolve material unknowns before dependent implementation.
Keep design collaborative.
Enforce permissions and financial rules on the backend.
Report actual progress accurately.