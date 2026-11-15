# MeetDiscreet — Content and Boundaries

## 1. Purpose and Status

Define the content scope, eligibility requirements, participant boundaries,
and policy-placement rules for MeetDiscreet’s current release.

This document guides implementation and moderation.

It is not the final customer-facing legal text.
It does not establish that moderation or verification is operational.

Read alongside:

- ../../AGENTS.md
- ./product_spec.md
- ./access_matrix.md
- ./booking_lifecycle.md
- ./pricing_and_payments.md
- ../design/design_system.md
- ../security/application_security.md
- ../decisions.md

## 2. Current Release Scope

MeetDiscreet supports paid platonic dates and social experiences.

Examples include:

- Coffee and conversation.
- Dinner.
- Concerts.
- Cinema and theatre.
- Museums and galleries.
- Sightseeing.
- Shopping.
- Games.
- Language practice.
- Celebrations.
- Formal events.
- Other approved social activities.

Profiles, listings, media, communication, and bookings must match
the current product scope.

Do not implement unspecified future content categories.

## 3. Positive Product Description

Describe what users can do naturally.

Suitable directions include:

- Find company for your next outing.
- Discover companions with shared interests.
- Plan an experience together.
- Explore profiles and available activities.
- Book time for an agreed social occasion.

Do not make ordinary pages read like repeated explanations of
prohibited conduct.

Do not promise affection, romance, attraction, or guaranteed chemistry.

## 4. Policy Placement

Consolidate detailed eligibility, boundaries, prohibited conduct,
and general safety guidance into one standalone page:

Community Guidelines & Boundaries

Its final URL is selected through the page inventory.

Link to it from:

- The footer.
- Relevant onboarding.
- Relevant booking acceptance.
- Reporting and support flows where useful.

Do not repeat the full page across:

- Homepage sections.
- Profile cards.
- Companion profiles.
- Listing editors.
- Dashboards.
- Message screens.
- Advertising panels.

Keep separate Terms, Privacy, and payment/cancellation documents
focused on their own purposes.

## 5. Concise Contextual Information

Show short, relevant information where a decision requires it.

Examples:

- Entrance age confirmation.
- Subscription price and renewal terms.
- What a subscription unlocks.
- Amount due for a booking.
- Deposit treatment.
- Cancellation terms.
- A linked acceptance checkbox.
- A specific validation error.

A contextual message should explain the immediate action.

Do not use it to repeat the complete guidelines.

Do not hide material transaction information to reduce copy.

## 6. Age Eligibility

The current product direction is for adults aged 18 or older.

Confirm the final eligibility process against the launch region
and actual operating requirements before release.

Do not assume a self-attestation satisfies every age-related obligation.

The approved account-level process must define:

- Information collected.
- Verification, if required.
- Failed or incomplete verification.
- Suspected underage accounts.
- Review and restriction.
- Retention and deletion of verification information.

Collect only information necessary for the selected process.

Do not publish full birth dates or verification documents.

## 7. Entrance Age Gate

Show a concise entrance confirmation before normal browsing.

Provide:

- “I am 18 or older.”
- An exit action.

Requirements:

- Apply to direct page visits.
- Preserve the intended destination.
- Prevent interaction with underlying content while active.
- Support keyboard and screen-reader use.
- Work on mobile.
- Avoid briefly exposing normal page content before activation.
- Use an explicitly selected retention period.

Keep Guidelines, Terms, Privacy, and an appropriate exit route
reachable without false eligibility confirmation.

The gate is self-attestation, not identity verification.

It must not grant roles, paid access, or backend permissions.

## 8. Permitted Profile and Listing Content

Allow content relevant to platonic social experiences:

- Introductions.
- Interests.
- Languages.
- Conversation topics.
- General location.
- Preferred activities.
- Availability.
- Personal style.
- Approved rates.
- Relevant accessibility information voluntarily supplied.
- Boundaries.
- Non-sexual stories about social experiences.

Respect the access tier assigned to each field.

Optional personal attributes must not be interpreted as agreement
to any activity or interaction.

## 9. Media Standards

Profile and subscriber media may include:

- Portraits.
- Introductions.
- Hobbies.
- Outfit previews.
- Event presentation options.
- Activity highlights.
- Non-sexual videos.
- Other approved material matching the service.

Subscriber payment does not unlock a different content standard.

For the current release, do not permit:

- Explicit nudity.
- Sexual acts.
- Erotic performances.
- Sexual-service advertising.
- Sexualized content involving minors.
- Content shared without necessary permission.
- Material that violates another person’s privacy.

Do not describe a moderation process as automated or comprehensive
unless that capability exists.

## 10. Prohibited Offers and Requests

The current release does not permit:

- Sexual services.
- Erotic add-ons.
- Negotiating sexual services through messages or bookings.
- Prices tied to intimate contact.
- Coercive or exploitative arrangements.
- Requests involving minors.
- Threats or intimidation.
- Nonconsensual recording.
- Stolen or impersonated profiles.
- Fraudulent payment requests.
- Requests to commit crimes.
- Publication of private identifying information without authorization.

Apply rules to conduct and context.

A keyword alone is not sufficient proof of a violation.
Do not make an unexplained word blacklist the sole moderation system.

## 11. Participant Boundaries

Participants control their own involvement.

A payment, subscription, booking, or prior meeting does not create
entitlement to:

- Physical contact.
- Affection.
- Romance.
- Intimate access.
- Continuous replies.
- Personal contact details.
- Continued participation.

Either participant may decline a request or end an interaction.

The financial outcome follows the confirmed booking policy.

Do not imply that ending participation automatically resolves
every charge or refund.

## 12. Activities, Venues, and Presentation Requests

Companions choose which activities they offer and accept.

Requests for changes to:

- Venue.
- Schedule.
- Duration.
- Outfit or presentation.
- Activities.
- Expenses.

must be agreed through the relevant booking process.

A profile preference does not constitute acceptance of every
request matching that preference.

Extended or overnight event attendance refers to agreed duration
and logistics.

It does not imply shared sleeping arrangements.

Venue restrictions and any prohibited activity categories remain
to be explicitly defined before affected bookings are enabled.

## 13. Messaging and Calls

Communication must remain within the current service scope.

Prohibit:

- Harassment.
- Threats.
- Repeated unwanted contact.
- Coercion.
- Sexual-service negotiation.
- Nonconsensual sexual material.
- Attempts to bypass another person’s block.
- Impersonation.
- Fraud.

Unlimited subscription messaging means no numerical plan allowance.
It does not require continuous availability or replies.

No call recording is enabled by default.

Any later recording feature requires a separate explicit specification
for consent, storage, access, and retention.

## 14. Privacy and Public Information

Use general locations in public discovery.

Do not publish by default:

- Precise home addresses.
- Private meeting details.
- Login email addresses.
- Phone numbers.
- Identity documents.
- Payment credentials.
- Private messages.
- Restricted media originals.

Define when booking participants receive necessary venue information.

Do not promise complete anonymity or confidentiality merely because
the product is named MeetDiscreet.

Privacy claims must match actual implementation.

## 15. Identity and Authenticity

Accounts must not misrepresent another person.

Define appropriate handling for:

- Stolen photographs.
- Impersonation.
- Misleading age claims.
- False verification claims.
- Unauthorized account control.
- Misrepresented presentations or experiences.

Two companion presentations share the same underlying account.

Do not present them as separately verified unrelated identities.

Verification badges must describe what was actually checked.
They must not imply a guarantee of safety or trustworthiness.

## 16. Reviews and Public Feedback

Reviews must follow confirmed eligibility rules.

Do not permit:

- Fabricated booking claims.
- Threats.
- Doxxing.
- Publication of sensitive private details.
- Payment demands in exchange for removing a review.
- Impersonated feedback.

Distinguish criticism from prohibited conduct.

A negative review is not automatically abusive.

Moderation must not silently rewrite a reviewer’s meaning
to protect a commercial relationship.

## 17. Reporting and Blocking

Provide reporting and blocking without paid access.

Support reports concerning:

- Accounts.
- Profiles.
- Listings.
- Media.
- Messages and calls.
- Reviews.
- Bookings.
- Payments.

Provide an appropriate support route when normal account access
is unavailable.

Define how blocking affects each feature.

Blocking must not silently erase bookings, payments, or disputes.

Do not disclose reporter identity automatically to the reported account.

Apply appropriate abuse controls to public reporting routes.

## 18. Moderation Process

Define an operational process before affected features launch.

It should identify:

- Report intake.
- Prioritization.
- Evidence access.
- Authorized reviewers.
- Interim restrictions where appropriate.
- Decision recording.
- Participant notification.
- Review or appeal route.
- Relevant retention.

Possible actions may include:

- Requesting clarification.
- Removing content from display.
- Restricting features.
- Suspending an account.
- Ending account access.

Exact actions and authority require confirmation.

A report is an allegation, not an established finding.

Use necessary evidence and record reasons for consequential actions.

## 19. Financial Consequences of Enforcement

Content removal or account restriction may affect:

- Publishing.
- Ads.
- Subscriber access.
- Pending bookings.
- Confirmed bookings.
- Refunds.
- Payouts.

Do not invent automatic forfeiture rules.

Define financial consequences in the payment specification
and operational procedures.

Preserve necessary transaction and dispute records.

## 20. Policy Acceptance and Versioning

Where acceptance is required, record:

- Account.
- Policy identifier.
- Policy version.
- Acceptance time.
- Relevant booking or transaction where applicable.

Do not precheck an acceptance box by assumption.

Define how material policy updates are communicated and accepted.

Preserve the policy version relevant to an existing agreement.

Do not silently rewrite historical acceptance records.

## 21. Content Configuration

Keep reasonably separate:

- Category definitions.
- Profile-field definitions.
- Visibility tiers.
- Permitted media types.
- Moderation rules.
- Customer-facing policy text.

Do not scatter conflicting copies across page scripts.

Do not build a universal policy engine without a concrete need.

Changes to content policy must be reflected in relevant validation,
moderation, documentation, and interface controls.

## 22. Future Scope Changes

Robbie has indicated that the platform’s scope may change later.

That intention does not alter the current release.

Before implementing a different scope:

1. Define the revised requirements explicitly.
2. Reassess provider suitability.
3. Reassess eligibility and verification.
4. Update moderation and operational processes.
5. Update data and access rules.
6. Update customer-facing policies.
7. Verify the changed implementation.

Do not disguise the business model to retain provider approval.

Do not enable an alternative service through hidden configuration
without an approved implementation plan.

## 23. Required Verification

Before releasing affected features, verify:

- Entrance confirmation covers direct navigation.
- Policy and exit routes remain accessible.
- Browser confirmation cannot grant backend permissions.
- Public listings do not leak restricted information.
- Protected originals remain private.
- Reporting does not require payment.
- Blocking is enforced beyond interface visibility.
- Verification labels match actual checks.
- Policy acceptance records identify the correct version.
- Moderation access is appropriately restricted.
- Enforcement consequences follow confirmed rules.
- Normal pages do not repeat lengthy disclaimer content.

Do not claim that tests guarantee all prohibited behaviour is prevented.

## 24. Open Decisions

Track confirmations in ../decisions.md.

Outstanding decisions include:

- Final launch eligibility requirements.
- Age and identity verification process.
- Age-gate retention.
- Venue restrictions.
- Media limits and review process.
- Moderation roles and response priorities.
- Appeals or review process.
- Blocking consequences.
- Financial effects of enforcement.
- Policy-update acceptance.
- Evidence retention.
- Final customer-facing policy wording.

Resolve relevant decisions before dependent live functionality.

## 25. Final Rule

Keep the current service scope clear and enforceable.

Put detailed boundaries on their designated page.
Keep ordinary interfaces focused and useful.
Protect privacy.
Record moderation decisions fairly.
Make no guarantees the application cannot support.