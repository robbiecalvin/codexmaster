# [Application name] — Page Inventory

**Owner** [Role]  
**Scope and revision** [Milestone or version]  
**Status and review date** [Draft / Approved / Verified, date]

Complete each applicable section with project-specific values and evidence. The detailed reference material describes an illustrative marketplace. Adapt its actors, rules, tools, limits, and workflows to your project. Mark inapplicable sections with a short reason. Treat unapproved choices as proposed or pending.

## Quick-start worksheet

**Owner and review date** [Role, date]  
**Release scope** [Milestone]

### Inventory and statuses

Use the inventory to track routes, shared surfaces, and system states. Record design, implementation and verification separately. Use `Draft`, `In review`, `Approved`, `In progress`, `Verified`, or `Deferred` where applicable.

| ID and page | Route or trigger | Audience and access | Primary action | Design | Build | QA evidence | Owner |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [P-01 Public entry] | [Path] | [Visitor / eligibility] | [Explore or sign in] | [Status] | [Status] | [Link] | [Role] |
| [Authentication and onboarding] | [Path or redirect] | [Account state] | [Create, verify or recover account] | [Status] | [Status] | [Link] | [Role] |
| [Member or operator workspace] | [Path] | [Role and ownership] | [Primary workflow] | [Status] | [Status] | [Link] | [Role] |
| [Administration and moderation] | [Path] | [Privileged role] | [Review or act] | [Status] | [Status] | [Link] | [Role] |
| [Transaction or system state] | [Event or redirect] | [Context] | [Retry, recover or continue] | [Status] | [Status] | [Link] | [Role] |

Inventory shared navigation, dialogs, policy notices, account menus, and toasts. Include loading, empty, error, denied, expired, offline, and success states as applicable.

### Reusable page brief

### [Page ID and name]

- **Purpose and entry points.** [User goal, route, redirects, and links into this page]
- **Audience and data.** [Roles, eligibility, data source, visibility and content owner]
- **Layout and actions.** [Main interaction, components, and mobile and desktop behavior]
- **States and copy.** [Loading, empty, errors, success, notices, and policy links]
- **Acceptance.** [Accessibility, denied access, critical interaction and recovery cases]
- **Review.** [Design reference and revision, implementation and verification links, owner and open questions]

### Production order and active page

| Order | Page | Dependency | Current action | Reviewer |
| --- | --- | --- | --- | --- |
| [1] | [Page ID] | [Prerequisite] | [Design, build or review] | [Role] |

Use stable page IDs and record prior routes when a page is renamed, merged, or retired. Update navigation and redirects, and retain useful design revision references. See [Project Context](project_context.md) and [Launch Acceptance](launch_acceptance.md).

## Detailed template

Use these fields for the detailed records in this document.

| Page ID and route | Audience and access | Primary action and states | Design and implementation | Dependencies | QA evidence |
| --- | --- | --- | --- | --- | --- |
| [Fill in] | [Fill in] | [Fill in] | [Fill in] | [Fill in] | [Fill in] |

### 1. Purpose

Record the actual release, what is applicable today, what remains proposed or deferred, and the latest supporting reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Track [Application name]’s planned pages, interface surfaces, dependencies,
and production status.

This inventory is not a requirement to create one HTML file per row.

Related functions may use tabs, dialogs, drawers, or shared detail pages
when that improves usability.

Final source paths and URLs are assigned during implementation.

Do not treat the proposed names below as existing files.

### 2. Related Documents

For **related documents**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

- [Project reference for AGENTS]
- [Product Spec](product_spec.md)
- [Access Matrix](access_matrix.md)
- [Next Steps](next_steps.md)
- [Decisions](decisions.md)
- [Project reference for design system]
- [Project reference for design memory]
- ./page_briefs/

The roadmap owns phase progress.
This document owns page and interface-surface coverage.

Page briefs own page-specific design decisions.

### 3. Status Convention

Record the actual release, what is applicable today, what remains proposed or deferred, and the latest supporting reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Initial status for all surfaces:

- Implementation: Not started or not verified.
- Verification: Not checked.
- Visual review: Not requested.
- Integration: Not connected.
- Deployment: Not verified.

Update individual records as actual work occurs.

Do not infer approval from implementation or silence.

For compact tracking, use these labels:

- Planned.
- Designing.
- Building.
- Awaiting review.
- Changes requested.
- Accepted for current scope.

Keep verification, integration, and deployment information separate
when those distinctions matter.

### 4. Inventory Fields

For **inventory fields**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Each implemented page or substantial interface surface should have:

- Stable identifier.
- Working name.
- Purpose.
- Audience.
- Actual URL or parent surface.
- Source file or module.
- Page brief.
- Dependencies.
- Implementation status.
- Review status.
- Verification notes.
- Integration and deployment status.

Do not fill unknown paths with invented values.

### 5. Shared Site Surfaces

For **shared site surfaces**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

| ID | Surface | Purpose | Main dependencies |
|---|---|---|---|
| SH-01 | Entrance age gate | Confirm entrance eligibility and preserve destination | Gate policy and retention decision |
| SH-02 | Public navigation | Navigate public discovery and account entry | Initial design direction |
| SH-03 | Account navigation | Navigate authenticated workspaces | Roles and session state |
| SH-04 | Footer | Provide essential navigation and policy links | Public page structure |
| SH-05 | Dialogs and drawers | Reusable overlays and focused interactions | Accessibility and component design |
| SH-06 | Feedback states | Loading, empty, error, and success presentation | Shared components |
| SH-07 | Subscription prompt | Explain access and start a provider subscription | Pricing and entitlement rules |
| SH-08 | Report/block controls | Access appropriate protection and support actions | Reporting and blocking policy |

Shared surfaces do not necessarily need standalone URLs.

Do not implement separate incompatible age gates or navigation
on individual pages.

### 6. Public Pages

For **public pages**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

| ID | Page | Purpose | Main dependencies |
|---|---|---|---|
| PUB-01 | Homepage/discovery | Introduce the service and begin discovery | Initial visual direction and discovery rules |
| PUB-02 | [request listing] results | Browse user activity requests | Listing visibility and filters |
| PUB-03 | [offer listing] results | Browse provider ads | Publishing and public listing rules |
| PUB-04 | [request listing] detail | Read a specific request | Full-post visibility decision |
| PUB-05 | [offer listing] detail | Read a specific provider ad | Public-field restrictions |
| PUB-06 | Provider profile | Present public/member/subscriber views | Access matrix and media rules |
| PUB-07 | User profile view | Display permitted user information | User-profile visibility decision |
| PUB-08 | Pricing and how it works | Explain plans and product distinctions | Confirmed commercial rules |
| PUB-09 | Community Guidelines & Boundaries | Consolidate eligibility and conduct guidance | Approved content policy |
| PUB-10 | Help/contact | Explain support options | Actual support process |
| PUB-11 | Terms | Present applicable service terms | Final operating model |
| PUB-12 | Privacy | Describe actual data practices | Selected services and retention |
| PUB-13 | Payments/cancellations | Explain financial policies | Confirmed payment and booking rules |
| PUB-14 | Not found | Recover from invalid routes | Navigation and hosting behaviour |
| PUB-15 | Service unavailable | Explain a genuine outage or maintenance state | Actual operational mechanism |

PUB-15 is conditional.
Do not build a maintenance system merely to satisfy this inventory.

Pricing and how-it-works content may be combined or separated
during design.

### 7. Authentication and Onboarding

For **authentication and onboarding**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

| ID | Page or surface | Purpose | Main dependencies |
|---|---|---|---|
| AUTH-01 | Registration | Create an account | Authentication and eligibility |
| AUTH-02 | Sign-in | Start a session | Selected authentication service |
| AUTH-03 | Email confirmation | Complete confirmation where required | Provider-supported flow |
| AUTH-04 | Password recovery | Request account recovery | Supported authentication method |
| AUTH-05 | Password reset | Complete recovery securely | Provider-supported flow |
| AUTH-06 | User onboarding | Collect permitted profile information | Required fields and visibility |
| AUTH-07 | Provider onboarding | Establish provider profile and eligibility | Provider requirements |
| AUTH-08 | Eligibility/verification status | Explain required checks and outcomes | Selected verification process |
| AUTH-09 | Session expired/access denied | Explain access problems and recovery | Session and permission handling |

Combine authentication screens where appropriate.

Do not create password screens if the selected authentication method
does not use passwords.

### 8. User Workspace

Record prerequisites, deliverables, owners, dependencies, and the smallest independently verifiable result.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

| ID | Page or surface | Purpose | Main dependencies |
|---|---|---|---|
| USR-01 | Dashboard | Summarize relevant activity | Accounts and connected feature data |
| USR-02 | Profile editor | Manage permitted user fields | Ownership and visibility |
| USR-03 | Provider subscriptions | Manage individual subscriptions | Billing and entitlement lifecycle |
| USR-04 | Premium membership | Purchase and manage posting benefits | Premium rules |
| USR-05 | [request listing] editor | Draft, preview, and submit a post | Posting rules and design brief |
| USR-06 | [request listing] management | Manage posts, expiry, and boosts | Allowance and expiry enforcement |
| USR-07 | Messages | Browse and use authorized conversations | Messaging and subscription rules |
| USR-08 | Call interface | Handle audio/video sessions | Calling infrastructure |
| USR-09 | Booking request | Propose a provider experience | Subscription and booking rules |
| USR-10 | Booking detail | View agreement, payment, and available actions | Booking lifecycle |
| USR-11 | Booking history | Find past and current bookings | Participant authorization |
| USR-12 | Billing and receipts | Review own charges and refunds | Verified financial records |
| USR-13 | Notifications | Review important activity | Notification model |
| USR-14 | Settings/privacy | Manage account preferences | Authentication and privacy rules |
| USR-15 | Blocked accounts | Manage own blocks | Confirmed block behaviour |
| USR-16 | Support/report submission | Submit and follow relevant concerns | Support and moderation process |
| USR-17 | Review submission | Review an eligible booking | Confirmed review rules |

Settings may consolidate several surfaces.

Messages, booking detail, and billing should reuse shared components
where provider and user workflows overlap.

### 9. Provider Workspace

Record prerequisites, deliverables, owners, dependencies, and the smallest independently verifiable result.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

| ID | Page or surface | Purpose | Main dependencies |
|---|---|---|---|
| COM-01 | Dashboard | Summarize provider activity | Relevant connected data |
| COM-02 | Profile editor | Manage provider introduction and fields | Ownership and visibility |
| COM-03 | Presentation management | Manage up to two presentations | Presentation rules |
| COM-04 | Media manager | Upload and organize authorized media | Private storage and processing |
| COM-05 | Experiences/rates | Configure offerings and prices | Approved pricing inputs |
| COM-06 | Availability/calendar | Manage offered times and conflicts | Scheduling model |
| COM-07 | Publishing plan | Purchase and manage publishing | Billing and expiry policy |
| COM-08 | [offer listing] editor | Draft and preview an ad | Publishing and public-field rules |
| COM-09 | Ad management | Manage ads, boosts, and upgrades | Advertising policies |
| COM-10 | Subscriber management | View minimum necessary subscriber information | Subscriber visibility rules |
| COM-11 | Booking inbox | Review requests and revisions | Booking lifecycle |
| COM-12 | Booking detail | Manage a participating booking | Booking and payment records |
| COM-13 | Earnings/payouts | Distinguish allocations and actual payouts | Financial reconciliation |
| COM-14 | Reviews | Read and respond where permitted | Review policy |
| COM-15 | Messages and calls | Use authorized communication | Shared communication components |

Do not duplicate USR and COM pages unnecessarily.

A shared booking-detail implementation may expose different authorized
actions according to participant role.

The same principle applies to messaging and billing components.

### 10. Administration

For **administration**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

| ID | Page or surface | Purpose | Main dependencies |
|---|---|---|---|
| ADM-01 | Operations dashboard | Show actionable operational information | Defined staff capabilities |
| ADM-02 | Account management | Review accounts and apply permitted actions | Role and restriction rules |
| ADM-03 | Content review | Review profiles, listings, and media | Moderation process |
| ADM-04 | Reports | Triage and resolve reports | Evidence access and workflow |
| ADM-05 | Booking disputes | Review booking-related concerns | Dispute authority and records |
| ADM-06 | Payment reconciliation | Investigate financial inconsistencies | Provider and internal references |
| ADM-07 | Payout operations | Review permitted payout issues | Provider capabilities and authority |
| ADM-08 | Configuration | Manage explicitly editable settings | Configuration permissions |
| ADM-09 | Audit history | Inspect consequential operational actions | Implemented audit records |
| ADM-10 | Support cases | Handle account and service concerns | Support process |

Administrative pages require explicit backend capabilities.

Do not assume every moderator can access every administrative surface.

Do not create unrestricted financial adjustment controls.

### 11. Transaction and System States

Record allowed transitions, responsible actors, guards, timeouts, side effects, and conflicts.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

These may appear as pages, dialogs, or states within existing surfaces.

| ID | State | Required behaviour |
|---|---|---|
| SYS-01 | Checkout return | Fetch actual payment status; do not trust redirect alone |
| SYS-02 | Payment pending | Explain pending verification and recovery |
| SYS-03 | Payment failed/cancelled | Offer appropriate next actions |
| SYS-04 | Booking reservation expired | Explain current agreement/payment situation |
| SYS-05 | Subscription expired | Show permitted access and renewal options |
| SYS-06 | Publishing expired | Apply confirmed visibility and management rules |
| SYS-07 | Account restricted | Explain permitted information and support route |
| SYS-08 | Empty results | Help users adjust discovery or filters |
| SYS-09 | Network failure | Preserve input where practical and support retry |
| SYS-10 | Media unavailable | Avoid exposing private storage details |
| SYS-11 | Call failure | Explain permissions or connection outcome |
| SYS-12 | Submission success | Show only verified completion of the relevant action |

Do not show a success state for an unverified transaction.

### 12. Page Design Process

For **page design process**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Before a new page enters implementation:

1. Read its functional requirements.
2. Read existing shared visual decisions.
3. Identify unresolved page-specific choices.
4. Ask [Decision owner] a focused questionnaire.
5. Create or update its page brief.
6. Build a reviewable version.
7. Inspect and revise it.

Do not require all pages to be designed upfront.

Do not repeat settled global questions.

Clear later edit requests do not require a new full questionnaire.

### 13. Suggested Initial Production Order

For **suggested initial production order**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

After documentation and foundational decisions:

1. Shared design foundation.
2. Entrance age gate and public navigation.
3. Homepage/discovery.
4. [offer listing] and [request listing] results.
5. Listing detail.
6. Provider profile.
7. Authentication and onboarding.
8. User and provider profile editors.
9. Listing editors and management.
10. Relevant subscription and publishing surfaces.
11. Booking surfaces.
12. Communication surfaces.
13. Operational tools and remaining account pages.

Adjust ordering for actual dependencies.

Implement basic reporting, blocking, and required moderation before
exposing affected functionality to real users.

The order does not authorize postponing essential operational controls.

### 14. Design Questions by Page Type

#### Discovery

For **discovery**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Ask about:

- Initial content emphasis.
- Search/filter placement.
- Card versus row treatment.
- Density.
- Sponsored placement.
- Mobile filtering.

#### Profile

For **profile**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Ask about:

- Image prominence.
- Gallery.
- Introduction hierarchy.
- Rate and action placement.
- Tabs or sections.
- Locked-content presentation.
- Mobile actions.

#### Editor

For **editor**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Ask about:

- Single-page or stepped form.
- Preview placement.
- Upgrade sidebar.
- Price summary.
- Save/publish actions.
- Mobile consolidation.

#### Dashboard

For **dashboard**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Ask about:

- Highest-priority information.
- Activity layout.
- Navigation.
- Action shortcuts.
- Density.
- Mobile ordering.

#### Booking

Record allowed transitions, responsible actors, guards, timeouts, side effects, and conflicts.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Ask about:

- Form progression.
- Schedule selection.
- Price breakdown.
- Agreement summary.
- Revisions.
- Mobile checkout behaviour.

Use these as prompts, not a mandatory repeated script.

### 15. Page Brief Naming

For **page brief naming**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Use descriptive kebab-case filenames.

Examples:

- homepage.md
- discovery-results.md
- provider-profile.md
- looking-for-editor.md
- offering-editor.md
- booking-request.md
- booking-detail.md

These are naming examples, not existing files.

A shared brief may cover closely related surfaces when their differences
are documented clearly.

Do not create empty briefs for every future page.

### 16. Active Page Record

Capture the page ID, route, audience, current design revision, reviewer, unresolved questions, next action, and acceptance evidence.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Create an entry when work begins on a page.

Suggested fields:

- Inventory ID:
- Working title:
- Actual URL or parent surface:
- Source files:
- Page brief:
- Audience and permissions:
- Dependencies:
- Implementation status:
- Visual review status:
- Verification:
- Integration status:
- Deployment status:
- Outstanding feedback:
- Next action:

No active application page has been verified by this initial draft.

### 17. Consolidation and Changes

For **consolidation and changes**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

If pages are merged, split, renamed, or removed:

- Update this inventory.
- Update relevant briefs.
- Update navigation and links.
- Check direct navigation.
- Record material scope decisions.
- Preserve deferred requirements in the roadmap.

Do not silently drop functionality during consolidation.

Do not retain broken links to pages that no longer exist.

### 18. Policy and Copy Placement

For **policy and copy placement**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Keep detailed boundaries on PUB-09.

Use concise, contextual pricing and acceptance information on
transactional surfaces.

Do not add repeated disclaimer cards to every page.

Age-gate, policy, and support accessibility must follow the product rules.

### 19. Final Rule

For **final rule**, record the applicable rule or design, its owner, exceptions, and a reference.

**Project record** [Fill in, or mark N/A with a reason.]

**Illustrative reference and adaptation checklist**

Keep the inventory aligned with the actual application.

Plan broadly, design progressively, and record real implementation
and review status without inventing completion.

