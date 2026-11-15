# MeetDiscreet — Access Matrix

## 1. Purpose

Define visibility, ownership, roles, and paid entitlements for MeetDiscreet.

This document describes intended permissions.
It does not establish that authorization is implemented.

Read alongside:

- ../../AGENTS.md
- ./product_spec.md
- ./pricing_and_payments.md
- ./booking_lifecycle.md
- ../architecture/application_architecture.md
- ../security/application_security.md
- ../decisions.md

If a permission remains unresolved, do not silently grant access.

Continue independent implementation where possible.
Resolve the rule before releasing the dependent feature.

## 2. Permission Model

Evaluate access using the relevant combination of:

- Identity.
- Account status.
- Role.
- Resource ownership.
- Resource visibility.
- Companion-specific subscription.
- Premium user membership.
- Companion publishing status.
- Conversation membership.
- Booking participation.
- Block relationships.
- Moderation assignments.

Roles and paid entitlements are separate.

A user may hold several entitlements without receiving additional
administrative privileges.

Whether one account may hold both user and companion roles remains pending.

## 3. Matrix Legend

- Allowed: permitted subject to applicable account and resource rules.
- Own: limited to resources owned by the account.
- Participating: limited to the relevant booking, conversation, or transaction.
- Assigned: limited to explicitly authorized operational duties.
- Pending: requires a confirmed product decision.
- Denied: not permitted through this role or entitlement.

“All subscribers” does not mean every subscriber to the platform.

A companion-specific entitlement applies only to the relevant companion.

## 4. General Enforcement Rules

- Public resources may allow anonymous access.
- Protected resources require trusted authorization.
- Clients cannot assign their own roles or paid status.
- Ownership must be checked on every relevant operation.
- Resource identifiers do not constitute authorization.
- UI visibility does not enforce backend access.
- APIs must return only permitted fields.
- Realtime channels and attachments require their own access checks.
- Administrative access must be explicitly assigned.

A suspended or restricted account may lose otherwise available actions
according to the defined restriction.

Exact restriction effects must be specified before release.

## 5. Public Access

| Resource or action | Visitor |
|---|---|
| View public homepage and discovery | Allowed after entrance confirmation |
| Browse public Offering ads | Allowed after entrance confirmation |
| View public companion profile fields | Allowed after entrance confirmation |
| View public general rates | Allowed after entrance confirmation |
| View published public reviews | Allowed after entrance confirmation |
| Browse public Looking For summaries | Allowed after entrance confirmation |
| View full Looking For post | Pending |
| View linked user-profile details | Pending |
| View member-only fields | Denied |
| Retrieve subscriber media | Denied |
| Send messages or initiate calls | Denied |
| Submit booking request | Denied |
| Create posts or profiles | Denied |
| Access Guidelines, Terms, Privacy, or exit route | Allowed without eligibility confirmation |
| Access an appropriate public support/report route | Allowed; abuse controls required |

The entrance gate is a presentation and eligibility step.
It is not authentication or proof of age.

## 6. Companion Profile Visibility

| Information | Visitor | Registered member | Active subscriber to that companion |
|---|---|---|---|
| Display name and username | Allowed | Allowed | Allowed |
| General location | Allowed | Allowed | Allowed |
| Profile picture | Allowed | Allowed | Allowed |
| Tagline and preferred date style | Allowed | Allowed | Allowed |
| Optional zodiac sign | Allowed | Allowed | Allowed |
| Public age and gender information | Allowed | Allowed | Allowed |
| General rates | Allowed | Allowed | Allowed |
| Published public reviews | Allowed | Allowed | Allowed |
| Bio, interests, and conversation topics | Denied | Allowed | Allowed |
| What I Enjoy | Denied | Allowed | Allowed |
| What Doesn’t Work for Me | Denied | Allowed | Allowed |
| Ideal activities and stated boundaries | Denied | Allowed | Allowed |
| Optional orientation | Denied | Allowed | Allowed |
| Optional A Date to Remember story | Denied | Allowed | Allowed |
| Up to three additional member-visible photos | Denied | Allowed | Allowed |
| Permitted member-level appearance fields | Denied | Allowed | Allowed |
| Further gallery photos | Denied | Denied | Allowed |
| Uploaded profile videos | Denied | Denied | Allowed |
| Detailed experience catalogue | Denied | Denied | Allowed |
| Add-on prices | Denied | Denied | Allowed |
| Subscriber presentation options | Denied | Denied | Allowed |
| Linked two-companion availability information | Denied | Allowed | Allowed |
| Owner editing controls | Denied | Denied | Denied |

Companion owners manage their own profiles through separate ownership
permissions.

Optional fields need not be populated.

Restrictions and publishing-state rules may affect visibility.

## 7. Subscriber Isolation

An active subscription to Companion A must not unlock:

- Companion B’s restricted profile fields.
- Companion B’s protected media.
- Messaging with Companion B.
- Calls with Companion B.
- Booking requests to Companion B.

Premium user membership does not alter this rule.

If a profile links to another companion, the link does not transfer access.

Whether one subscription unlocks both presentations of the same companion
remains pending confirmation.

Two-companion booking subscription requirements also remain pending.

## 8. Account and User Profile Ownership

| Action or information | Account owner | Other member | Moderator | Administrator |
|---|---|---|---|---|
| Edit permitted personal profile fields | Own | Denied | Assigned | Assigned |
| View private login/contact details | Own | Denied | Assigned only when necessary | Assigned only when necessary |
| Change password through supported process | Own | Denied | Denied | No direct password access |
| Manage notification preferences | Own | Denied | Denied | Assigned support capability only |
| View another user’s profile fields | Not applicable | Pending field visibility | Assigned | Assigned |
| Change own account role | Denied | Denied | Denied unless expressly assigned | Assigned |
| Set own verification status | Denied | Denied | Assigned | Assigned |
| Set own payment or subscription status | Denied | Denied | Denied | Controlled operational process |
| Request account deletion | Own | Denied | Assigned support handling | Assigned |

Administrators must not be able to read passwords.

Administrative recovery or support actions must use supported,
audited mechanisms.

## 9. Companion Management

| Action | Companion owner | Other user or companion | Operational staff |
|---|---|---|---|
| Create/edit own unpublished profile | Own | Denied | Assigned |
| Manage own presentations | Own, up to approved limit | Denied | Assigned |
| Upload and organize own profile media | Own | Denied | Assigned |
| Edit own experiences and rates | Own | Denied | Assigned |
| Manage own availability | Own | Denied | Assigned |
| Request publishing | Own, subject to eligibility | Denied | Assigned |
| Override publishing payment status | Denied | Denied | Controlled operational process |
| Bypass moderation | Denied | Denied | Denied |
| View another companion’s earnings | Denied | Denied | Assigned financial duties only |
| View subscriber management information | Own, minimum necessary fields | Denied | Assigned |

Subscriber management does not grant access to private user records,
unrelated purchases, or credentials.

Define its exact fields before implementation.

## 10. Looking For Posts

| Action | Registered user | Premium user | Other account | Operational staff |
|---|---|---|---|---|
| Create a draft | Own | Own | Denied for another owner | Assigned |
| Preview own draft | Own | Own | Denied | Assigned |
| Publish within confirmed allowance | Own | Own | Denied | Assigned |
| Edit own post | Own | Own | Denied | Assigned |
| Remove own post from public display | Own | Own | Denied | Assigned |
| Use included premium boosts | Denied | Own, subject to allowance | Denied | Assigned adjustment only |
| Purchase eligible additional boosts | Own | Own | Denied | Assigned |
| Set arbitrary boost balance or ranking | Denied | Denied | Denied | Controlled operational process |
| View another account’s draft | Denied | Denied | Denied | Assigned |

Proposed allowances:

- Free: one active post.
- Premium: up to three active posts.
- Premium: two included boosts per post per 30-day period.

The free active-post interpretation remains pending.

Define premium-expiry consequences before release.

## 11. Offering Ads

| Action | Companion owner | Other account | Operational staff |
|---|---|---|---|
| Create/edit own Offering draft | Own | Denied | Assigned |
| Publish Offering ad | Own with eligible publishing status | Denied | Assigned |
| Manage included ad | Own | Denied | Assigned |
| Purchase additional ads | Own with required eligibility | Denied | Assigned |
| Use available boosts | Own | Denied | Assigned adjustment only |
| Purchase eligible upgrades | Own | Denied | Assigned |
| Expose member/subscriber fields in public ad | Denied | Denied | Denied |
| Mark an unpaid upgrade as paid | Denied | Denied | Controlled operational process |

Publishing or upgrade payment does not override content restrictions.

## 12. Plans and Billing

| Action or information | Purchaser | Companion receiving allocation | Operational staff |
|---|---|---|---|
| Purchase eligible plan or upgrade | Own | Not applicable | Assigned support only |
| View own subscription status | Own | Limited subscriber-management view | Assigned |
| Cancel own eligible renewal | Own | Denied for another purchaser | Assigned support process |
| View purchaser receipt | Own | Denied unless separately required | Assigned financial duties |
| View allocated companion earnings | Denied for another account | Own | Assigned financial duties |
| View full payment credentials | Denied | Denied | Denied through application |
| Set own financial balance | Denied | Denied | Controlled operational process |
| Request refund or raise dispute | Own transaction | Participating where relevant | Assigned |
| Approve financial adjustment | Denied | Denied unless confirmed policy permits | Assigned with audit |

Use provider-supported payment interfaces.

Do not expose payment secrets or unnecessary billing details
to companions or moderators.

## 13. Booking Requests

| Action | Requesting user | Selected companion | Unrelated account | Operational staff |
|---|---|---|---|---|
| Open new request form | Active subscription required | Own management interface | Denied | Assigned |
| Submit new request | Active subscription and eligibility required | Not applicable | Denied | Assigned |
| View own submitted request | Participating | Participating | Denied | Assigned |
| Accept or decline request | Denied | Participating | Denied | Assigned intervention only |
| Propose revised details | According to lifecycle | According to lifecycle | Denied | Assigned |
| Accept material companion revision | Participating requester | Denied on requester’s behalf | Denied | No silent acceptance |
| Pay required booking amount | Participating purchaser | Denied on purchaser’s behalf | Denied | Assigned support process |
| Change accepted price unilaterally | Denied | Denied | Denied | Denied outside explicit adjustment process |
| Cancel booking | Participating, subject to lifecycle | Participating, subject to lifecycle | Denied | Assigned |
| View private venue details | Participating, when permitted | Participating, when permitted | Denied | Assigned when necessary |
| Raise booking concern | Participating | Participating | Denied | Assigned |
| Retrieve another booking by changing its ID | Denied | Denied | Denied | Assigned resource access only |

Retention of booking-management access after subscription expiry
must be defined.

Do not remove access to receipts, dispute routes, or necessary
transaction records merely because a subscription expires.

## 14. Messages and Attachments

| Action | Authorized participant | Unrelated account | Operational staff |
|---|---|---|---|
| Initiate subscriber-gated conversation | Active relevant entitlement required | Denied | Assigned support route only |
| Send message | Membership, entitlement, and block checks required | Denied | No impersonation |
| Read conversation history | Participating; expiry rule pending | Denied | Assigned, necessary review only |
| Upload attachment | Authorized conversation participant | Denied | Assigned |
| Retrieve attachment | Authorized access required | Denied | Assigned |
| Update own read receipt | Participating | Denied | Denied |
| Modify another participant’s receipt | Denied | Denied | Denied |
| Subscribe to realtime channel | Authorized membership required | Denied | Assigned |

Subscription alone does not grant access to unrelated conversations.

Moderation access to private communication must have a defined purpose,
scope, and audit trail.

Historical message access after expiry remains pending.

## 15. Calls

| Action | Caller | Recipient | Unrelated account |
|---|---|---|---|
| Initiate call | Relevant entitlement and eligibility required | Not applicable | Denied |
| Receive invitation | Authorized intended recipient | Authorized intended recipient | Denied |
| Accept invitation | Denied on another person’s behalf | Intended recipient only | Denied |
| Retrieve connection credentials | Authorized session participant | Authorized session participant | Denied |
| Control microphone/camera | Own device/session | Own device/session | Denied |
| End call | Participating | Participating | Denied |
| Access recordings | Not available by default | Not available by default | Denied |

Validate permissions at relevant call actions.

Do not assume administrative status authorizes joining private calls.

## 16. Reviews

| Action | Eligible booking participant | Companion reviewed | Unrelated account | Operational staff |
|---|---|---|---|---|
| Read published public review | Allowed | Allowed | Allowed | Allowed |
| Submit verified-booking review | Pending exact reviewer rule | Pending | Denied | No fabricated reviews |
| Respond to review | Pending | Own response if approved | Denied | Assigned |
| Edit or remove another person’s review | Denied | Denied | Denied | Assigned moderation |
| Report review | Allowed through appropriate route | Allowed | Allowed through appropriate route | Assigned |
| Mark unverified activity as verified | Denied | Denied | Denied | Denied |

Confirm review eligibility, timing, editing, and response rules.

## 17. Blocking and Reporting

Blocking and reporting must not require a subscription or premium plan.

Registered accounts can manage their own block list.

Define block effects on:

- Discovery.
- Profile visibility.
- Messages.
- Calls.
- New requests.
- Existing bookings.

Do not assume blocking cancels a booking, erases a payment obligation,
or authorizes disclosure of private information.

Reports should be visible to:

- The reporter through an appropriately limited status view.
- Assigned operational staff.
- Other parties only when the review process requires disclosure.

Do not expose reporter identity automatically to the reported account.

Provide a suitable reporting/support route for people unable to sign in,
with appropriate abuse controls.

## 18. Moderator and Administrator Boundaries

Operational roles require explicit capabilities.

Possible capabilities include:

- Review public content.
- Review reported private content when necessary.
- Restrict accounts.
- Remove content from display.
- Handle support cases.
- Review booking disputes.
- Reconcile payments.
- Approve financial adjustments.
- Manage roles.
- Review audit records.

Do not grant all capabilities merely because the interface labels
someone a moderator.

Financial duties and sensitive-content review should be separately scoped.

Use audited support actions rather than silent account impersonation.

## 19. Expiry, Suspension, and Revocation

Document consequences before enabling each transition.

| Event | Required decision |
|---|---|
| Companion subscription expires | Media, messaging, calls, booking initiation, and history access |
| Premium membership expires | Excess posts and unused included boosts |
| Publishing expires | Profile visibility, ads, subscribers, and existing bookings |
| Payment fails | Pending access, grace periods, and retries |
| Payment refunded | Entitlement removal and historical records |
| Account suspended | New activity, existing obligations, communication, and payouts |
| Account deleted | Public removal, retained financial records, and associated media |
| Account blocked | Cross-feature interaction consequences |

Unresolved rules must not result in accidental continued paid access.

At the same time, do not erase necessary transaction records or support
access without an approved policy.

## 20. Media Access

Authorize each requested asset according to:

- Owner.
- Associated profile, presentation, or conversation.
- Visibility tier.
- Relevant entitlement.
- Account restrictions.
- Operational capability, if applicable.

Temporary delivery references may remain valid until expiry.
Select duration and revocation behaviour deliberately.

Do not expose protected originals in public previews, HTML source,
metadata, client fixtures, or public storage paths.

## 21. Required Authorization Checks

Before releasing dependent features, verify:

- Anonymous requests cannot retrieve member-only fields.
- Nonsubscribers cannot retrieve subscriber media.
- Companion A’s subscription does not unlock Companion B.
- Premium membership does not unlock companion communication.
- Changing a resource ID does not bypass ownership.
- Draft posts remain private.
- Direct API requests cannot exceed posting allowances.
- Boost balances cannot be modified by clients.
- Message attachments require conversation authorization.
- Realtime channels reject unrelated accounts.
- Call credentials are scoped to authorized participants.
- Operational access is limited to assigned capabilities.
- Expiry and restrictions follow confirmed rules.
- Reporting and support remain available without paid access.

Test the backend boundary, not merely the visibility of buttons.

## 22. Open Decisions

Track confirmations in ../decisions.md.

Pending permissions include:

- Combined user/companion accounts.
- Full Looking For post visibility.
- User-profile field visibility.
- One subscription covering both presentations.
- Two-companion booking requirements.
- Historical messaging after expiry.
- Booking-management access after expiry.
- Publishing-expiry consequences.
- Premium-expiry consequences.
- Detailed block effects.
- Review eligibility and responses.
- Operational capabilities and sensitive-data access.
- Grace periods and refund-related entitlement changes.

## 23. Final Rule

Grant the minimum access required by confirmed product rules.

Keep roles, ownership, subscriptions, publishing, and premium benefits
distinct.

Enforce permissions at trusted boundaries and return only authorized data.