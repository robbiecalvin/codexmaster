# MeetDiscreet — Project Context

## 1. Purpose

This document provides the essential context needed to work on MeetDiscreet.

Read it alongside:

- [Root Instructions](../AGENTS.md)
- [README](../README.md)
- [Next Steps](./next_steps.md)
- [Decisions](./decisions.md)

Detailed requirements belong in their dedicated documents.

This file describes the project direction.
It does not establish implementation, approval, or deployment status.

## 2. Project Identity

- Name: MeetDiscreet.
- Product owner and visual decision-maker: Robbie.
- Product type: Social companion marketplace.
- Current release scope: Paid platonic dates and social experiences.
- Development approach: Page-by-page implementation with ongoing review.
- Primary editor: VS Code.
- Source control: Git and GitHub.

The name does not constitute a guarantee of anonymity, confidentiality,
identity verification, or participant safety.

Do not make unsupported privacy or security claims in product copy.

## 3. Product Goal

Help users discover companions, understand their interests and offerings,
and arrange clearly defined social experiences.

Examples include:

- Coffee and conversation.
- Dinner.
- Concerts and live music.
- Cinema and theatre.
- Cultural outings.
- Sightseeing.
- Shopping.
- Celebrations.
- Formal events.
- Other approved activities.

The platform combines discovery, profiles, subscriptions,
communication, bookings, and advertising.

## 4. Participants

### Visitors

Browse public listings and public profile information after the
entrance age confirmation.

### Registered Users

Create profiles, manage Looking For posts, and purchase optional
memberships or individual companion subscriptions.

### Companions

Create presentations, publish profiles, advertise offerings,
manage availability, communicate, and respond to booking requests.

### Moderators and Administrators

Perform specifically authorized review and operational functions.

Whether one account may act as both user and companion remains
to be confirmed.

## 5. Core Product Structure

### Looking For

Users describe an activity or social experience they want company for.

Posts link to the user’s profile.

### Offering

Companions advertise their experiences and link to their profiles.

Public ads must not expose member-only or subscriber-only information.

### Companion Profiles

Profiles support:

- Public introduction.
- Member-only details.
- Subscriber-only media and experience information.
- Rates.
- Availability.
- Reviews.
- Communication and booking access.

### Two Presentations

A companion may have up to two presentations under one account.

They may differ in content, media, style, offerings, and rates.

They share ownership, publishing association, and enforcement history.

Whether one subscription unlocks both presentations remains
a proposed rule requiring confirmation.

## 6. Commercial Model

MeetDiscreet has separate purchase types:

1. Companion publishing plans.
2. Individual companion subscriptions.
3. Premium user membership.
4. Advertising purchases and upgrades.
5. Booking payments.

These purchases must remain distinguishable in the interface,
backend permissions, and financial records.

Key distinctions:

- Premium user membership provides posting benefits.
- An individual subscription unlocks the specified companion’s access.
- A subscription does not include the separately priced date.
- Publishing enables profile and advertising eligibility.
- No purchase grants administrative privileges.

Authoritative prices and financial rules belong in:

[Pricing and Payments](./product/pricing_and_payments.md)

Do not maintain a competing price list in this document.

## 7. Access Model

The platform distinguishes:

- Public information.
- Registered-member information.
- Subscriber-only information.
- Owner-only management.
- Authorized moderation and administration.

Backend authorization must enforce these boundaries.

Subscription access is companion-specific.

The browser must not receive restricted information merely to conceal
it with interface styling.

Detailed permissions belong in:

[Access Matrix](./product/access_matrix.md)

## 8. Communication and Booking

Individual companion subscriptions are intended to unlock:

- Direct messages.
- Photo and video messages.
- Read receipts and timestamps.
- Audio calls.
- Video calls.
- Booking requests.

Bookings include agreed activities, schedule, duration, venue,
price, and applicable expenses.

The companion can accept, decline, or propose revisions.

The proposed financial interpretation uses one 10% deposit after
acceptance, credited toward the booking total.

That interpretation is not yet confirmed.

Do not assume a separate request fee is also charged.

Detailed rules belong in:

- [Product Specification](./product/product_spec.md)
- [Booking Lifecycle](./product/booking_lifecycle.md)
- [Pricing and Payments](./product/pricing_and_payments.md)

## 9. Design Collaboration

Visual decisions develop during production.

Before building a new page, Codex asks focused questions about
the unresolved choices for that page.

Carry forward existing approved decisions.

Do not:

- Require the entire site to be designed upfront.
- Repeat settled branding questions on every page.
- Force unusual layouts for novelty.
- Treat an approved design as permanently fixed.
- Repeat the full questionnaire for a clear edit request.

Robbie may revisit and revise any page.

Use:

- [Design System](./design/design_system.md)
- [Design Memory](./design/design_memory.md)
- [Page Inventory](./design/page_inventory.md)
- Individual page briefs.

Do not assume previously generated images establish approved
design choices unless Robbie identifies them as the reference.

## 10. Copy and Guidelines Placement

Keep normal pages focused on discovery, people, activities,
subscriptions, and bookings.

Consolidate detailed eligibility, boundaries, prohibited conduct,
and general safety explanations into one standalone page:

Community Guidelines & Boundaries

Do not fill ordinary pages with repeated disclaimers.

Keep necessary transaction-specific information visible,
including prices, renewal terms, subscription scope,
deposit treatment, and cancellation terms.

Separate Terms and Privacy documents may serve their actual purposes
without duplicating the guidelines essay.

## 11. Entrance Age Gate

Show a concise entrance age confirmation before normal browsing.

Requirements include:

- An “I am 18 or older” action.
- An exit action.
- Accessible interaction.
- Direct-link coverage.
- Preservation of the intended destination.
- A retention period still to be selected.

Entrance confirmation is self-attestation.

It does not replace backend eligibility checks or identity verification.
It does not establish authorization for protected features.

## 12. Technical Direction

The approved frontend direction is:

- HTML.
- CSS.
- JavaScript ES modules.
- Shared components.
- Responsive layouts.
- Accessible controls.
- Minimal justified dependencies.

A lightweight build tool may be selected when useful.

Backend functionality is required for accounts, permissions,
private media, payments, bookings, communication, and administration.

No backend provider or runtime is established by this document.

Provider decisions must be recorded explicitly.

See:

- [Application Architecture](./architecture/application_architecture.md)
- [Environment](./architecture/environment.md)
- [Repository Map](./architecture/repo_map.md)

## 13. Source Control and Deployment

The intended workflow is:

VS Code → Local preview → Relevant checks → GitHub → Deployment

GitHub is the source repository host.

GitHub Pages is not the production hosting target for the
commercial marketplace.

Choose an appropriate production host and document its configuration.

Local, preview, and production environments must remain appropriately
separated.

A successful push does not prove deployment succeeded.

## 14. Privacy and Security Constraints

Do not place the following in public source or frontend bundles:

- Secret credentials.
- Private messages.
- Restricted media originals.
- Real customer datasets.
- Administrative tokens.
- Payment secrets.

Enforce ownership, visibility, and entitlements on the backend.

Use synthetic data for development where appropriate.

Do not claim that an account, subscription, payment, or verification badge
guarantees trustworthiness or safety.

Detailed application controls belong in:

[Application Security](./security/application_security.md)

## 15. Future Adaptability

Robbie has indicated that the platform’s content scope may change later.

The current release remains the platonic service described here.

Keep category definitions, profile-field definitions, and content policy
reasonably separate from marketplace mechanics.

Do not:

- Implement unspecified future features.
- Build a hidden alternative service.
- Misrepresent the operating model to providers.
- Assume current provider suitability extends to a changed business.

A future scope change requires explicit revised requirements and
reassessment of affected services and operations.

## 16. Open Decisions

Record detailed status in ./decisions.md.

Current unresolved areas include:

- Launch region and currency.
- Domain and brand assets.
- Global visual direction.
- Backend and hosting providers.
- Payment and payout provider suitability.
- Single-deposit interpretation.
- Remaining booking balance collection.
- Refund and cancellation calculations.
- Taxes, processing costs, and payout timing.
- Account role combinations.
- Subscription access across both presentations.
- Entitlements after publishing expiry.
- Historical message access after subscription expiry.
- Free-post allowance interpretation.
- Unspecified advertising-upgrade durations.
- Age-confirmation retention.
- Verification approach.

Resolve decisions when they affect the next implementation step.

Do not block independent work unnecessarily.

## 17. Current Progress

Implementation and review status belong in:

[Next Steps](./next_steps.md)

Documents drafted in conversation are not proof they have been saved,
committed, or pushed.

Do not claim repository changes occurred without verification.

## 18. Working Priorities

1. Preserve the agreed product and payment-gate structure.
2. Build reviewable increments.
3. Follow Robbie’s visual direction.
4. Keep financial and permission rules explicit.
5. Distinguish prototypes from integrations.
6. Verify consequential behaviour.
7. Maintain accurate progress and decisions.

## 19. Final Rule

Use this document to orient work quickly.

Consult the detailed specification for implementation rules.
Consult the roadmap for actual progress.
Consult Robbie when a material unresolved decision is required.