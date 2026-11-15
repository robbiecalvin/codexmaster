# MeetDiscreet — Application Security

## 1. Purpose and Status

Define the security requirements for MeetDiscreet’s accounts,
private information, media, payments, bookings, and operations.

This is a security specification.
It does not establish that controls have been implemented or verified.

Read alongside:

- ../../AGENTS.md
- ../architecture/application_architecture.md
- ../architecture/environment.md
- ../architecture/data_model.md
- ../product/access_matrix.md
- ../product/pricing_and_payments.md
- ../product/booking_lifecycle.md
- ../product/content_and_boundaries.md
- ../development/launch_acceptance.md

Provider-specific configuration must be confirmed against the
selected services and actual deployment.

## 2. Security Objectives

Protect:

- Account ownership.
- Private profile information.
- Subscriber-only media.
- Private conversations and attachments.
- Booking locations and agreements.
- Financial records.
- Administrative capabilities.
- Verification information.
- System integrity and availability.

Do not promise absolute security, anonymity, or participant safety.

Describe only controls that actually exist.

## 3. Threat Model

Assess relevant threats including:

- Account takeover.
- Unauthorized record access.
- Cross-companion subscription bypass.
- Public leakage of restricted media.
- Stored or reflected script injection.
- Malicious uploads.
- Payment-event forgery or replay.
- Price manipulation.
- Double spending of allowances.
- Concurrent booking conflicts.
- Spam and harassment.
- Scraping of sensitive information.
- Administrative misuse.
- Secret exposure.
- Dependency compromise.
- Misconfigured preview environments.

Update the assessment when architecture or product scope changes.

## 4. Trust Boundaries

Treat these as distinct boundaries:

- Browser and user input.
- Authentication service.
- Application API.
- Database.
- Object storage.
- Payment provider.
- Realtime infrastructure.
- Calling service.
- Background processing.
- Administrative interface.

Validate identity, input, and authorization at the relevant trusted boundary.

Do not assume a request is legitimate because it originated from
the intended interface.

## 5. Authentication

Use an established authentication implementation.

Verify relevant:

- Registration.
- Sign-in.
- Confirmation.
- Recovery.
- Session refresh.
- Logout.
- Account restriction.
- Credential changes.

Prevent account enumeration where practical.

Apply appropriate protection against repeated authentication attempts.

Do not:

- Store plaintext passwords.
- Log credentials.
- expose recovery tokens.
- Build custom password cryptography.
- Treat a frontend account object as proof of identity.

Configure authentication redirects explicitly for each environment.

Do not accept arbitrary redirect destinations.

## 6. Sessions

Use the selected provider’s supported session mechanism.

Define:

- Token or cookie storage.
- Session lifetime.
- Refresh behaviour.
- Logout and revocation.
- Compromised-account handling.
- Multiple-device behaviour.

Where cookies are used, configure appropriate security attributes
and CSRF protection.

Where bearer tokens are used, minimize exposure and account for
the consequences of script injection.

Do not assume one session-storage approach is universally correct.

Sensitive actions may require recent authentication according
to the approved risk model.

## 7. Authorization

Enforce:

- Role.
- Ownership.
- Visibility.
- Companion-specific subscription.
- Publishing eligibility.
- Premium allowances.
- Conversation membership.
- Booking participation.
- Account restrictions.
- Applicable blocking rules.

Reject unauthorized requests even when the caller knows a valid record ID.

Do not rely on:

- Hidden buttons.
- Disabled inputs.
- Frontend route guards.
- Browser storage flags.
- Unpredictable URLs.
- Client-supplied role claims.

Use the access matrix as the detailed permission specification.

Deny unassigned privileged capabilities.

## 8. Database Permissions

Implement authorization through trusted backend logic,
database policies, or an explicitly designed combination.

Verify that direct service access cannot bypass intended restrictions.

Apply appropriate:

- Row ownership.
- Field exposure.
- Write permissions.
- Constraints.
- Transaction controls.
- Service-role restrictions.

Never expose privileged database credentials in browser code.

Do not allow account owners to modify their own:

- Roles.
- Verification.
- Payment state.
- Entitlements.
- Financial balances.
- Boost grants.

Administrative overrides require explicit authority and auditability.

## 9. Public and Restricted Responses

Construct API responses deliberately.

Public responses must not contain restricted fields merely because
the interface does not display them.

Check:

- Profile responses.
- Listing results.
- Search indexes.
- Page metadata.
- Structured data.
- Notifications.
- Error messages.
- Export files.
- Browser fixtures.

Do not expose full records through generic serialization.

Precise meeting locations and private account details require
appropriate participant or operational access.

## 10. Frontend Injection Protection

Render user-provided plain text using safe text APIs.

Do not insert untrusted content into:

- innerHTML.
- Script blocks.
- Event-handler attributes.
- Styles.
- Unvalidated URLs.

If rich text is required, use an approved sanitization strategy.

Validate link protocols and destinations appropriately.

Use framework or template escaping correctly if such tooling is selected.

Configure suitable browser security headers through the host.

A Content Security Policy can provide defence in depth.
It does not replace safe rendering and authorization.

## 11. Request Security

Validate request shape, types, lengths, and permitted values.

Use parameterized database queries.

Protect state-changing requests against CSRF where the architecture requires it.

Configure CORS for intended origins.

CORS is not authentication or authorization.

Avoid server-side requests to arbitrary user-supplied destinations.
If URL fetching is required, design explicit SSRF protections.

Do not expose internal diagnostics through public errors.

## 12. Upload Security

Before enabling uploads, define:

- Allowed file types.
- Maximum sizes.
- Video-duration limits.
- Processing workflow.
- Storage quotas.
- Content review.
- Malware-handling strategy.
- Failure cleanup.

Do not trust filename extensions or browser-provided MIME types alone.

Use safe generated storage names.

Prevent executable uploads from being served as active application content.

Handle unsupported or failed processing explicitly.

Do not expose an upload publicly before required validation is complete.

Avoid importing remote files from arbitrary URLs without a separate
security design.

## 13. Private Media

Keep protected originals in private storage.

Authorize:

- Upload.
- Attachment.
- Read.
- Replacement.
- Deletion.
- Moderation access.

Use scoped temporary access where appropriate.

Define access duration and revocation limitations.

Do not:

- Put private originals in GitHub.
- Include them in static build output.
- Use permanent public URLs for restricted assets.
- Conceal public originals with CSS blur.
- Log signed access URLs.

Use separate safe previews.

Authorization reduces unauthorized retrieval.
It cannot guarantee that an authorized viewer will not copy content.

Do not advertise technical controls as preventing all redistribution.

## 14. Payments

Use a suitable payment provider and its supported collection methods.

Do not store full payment credentials unnecessarily.

The backend determines:

- Product.
- Eligibility.
- Amount.
- Currency.
- Applicable quote.
- Entitlement consequence.

Reject client-edited financial values.

Use idempotency for consequential provider operations.

A successful checkout redirect does not prove payment.

Keep test and live payment environments separate.

## 15. Payment Events and Reconciliation

Verify provider event authenticity using the supported mechanism.

Check:

- Provider reference.
- Event identity.
- Expected account or purchase association.
- Amount and currency.
- Relevant state.
- Processing history.

Protect against duplicate and out-of-order events.

Record processing outcomes safely.

Provide reconciliation for:

- Missed events.
- Interrupted processing.
- Provider-side changes.
- Refund discrepancies.
- Payout failures.

Do not duplicate allocations or entitlements when events repeat.

Do not log unnecessary raw payment payloads.

## 16. Financial Integrity

Use explicit currency and integer minor units.

Protect:

- Price definitions.
- Accepted quotes.
- Revenue allocations.
- Refund limits.
- Payout records.
- Allowance consumption.

Financial adjustments must be attributable and explainable.

Do not maintain an editable number as the sole balance authority.

Prevent unauthorized staff or account owners from silently rewriting
historical transactions.

Financial-policy decisions belong in pricing_and_payments.md.

## 17. Booking Integrity

Enforce:

- Participant identity.
- Valid state transitions.
- Accepted quote version.
- Availability.
- Reservation validity.
- Payment conditions.
- Amendment acceptance.

Protect against concurrent conflicting confirmations.

Do not trust disabled buttons to prevent duplicate actions.

Preserve accepted terms and relevant policy versions.

Handle late payments and expired reservations through the approved process.

Protect private venue information.

## 18. Messaging and Realtime Access

Authorize:

- Conversation membership.
- Message submission.
- History access.
- Attachments.
- Read receipts.
- Realtime subscriptions.

Do not allow a valid session to subscribe to arbitrary private channels.

Apply subscription and blocking rules at the trusted boundary.

Use bounded request and attachment limits.

Prevent notifications from exposing restricted conversation content.

Define retention and deletion before release.

Do not claim end-to-end encryption unless the implemented protocol
actually provides it and its limitations are understood.

## 19. Calling Security

Use authorized, scoped call sessions.

Protect:

- Invitations.
- Acceptance.
- Signaling.
- Connection credentials.
- Session termination.

Use expiring credentials where supported.

Do not permit unrelated accounts or operational staff to join
private calls merely because they know a call identifier.

Request camera and microphone access only when relevant.

No recording is enabled by default.

Verify the selected service’s actual security properties before
making encryption or confidentiality claims.

## 20. Abuse Prevention

Apply proportionate controls to:

- Registration.
- Sign-in.
- Messaging.
- Calling.
- Posting.
- Boosting.
- Uploads.
- Reports.
- Checkout creation.
- Search and discovery requests.

Possible controls include:

- Rate limits.
- Quotas.
- Duplicate detection.
- Risk-based challenges.
- Account restrictions.

Select controls based on actual threats and usability.

Do not equate all unusual behaviour with abuse.

Provide appropriate reporting and blocking without requiring payment.

## 21. Administrative Access

Use explicit staff capabilities.

Separate where appropriate:

- Content moderation.
- Private-evidence review.
- Account restrictions.
- Financial reconciliation.
- Financial adjustments.
- Role management.
- Audit review.

Require strong authentication, including MFA for privileged accounts
before production operational access.

Apply least privilege.

Avoid silent impersonation.

Record consequential actions with actor, target, reason,
timestamp, and outcome.

Define how privileged access is granted and revoked.

## 22. Privacy and Verification Data

Collect only information needed for the approved product and operations.

Restrict access to:

- Identity verification.
- Precise locations.
- Private requests.
- Support evidence.
- Financial details.

Do not retain document images by default if a provider result
or reference meets the actual requirement.

Define retention and deletion explicitly.

Do not treat the entrance age gate as verified identity or age.

## 23. Logging and Audit

Log useful operational facts without exposing sensitive content.

Appropriate information may include:

- Safe record identifiers.
- Event type.
- State transition.
- Correlation identifier.
- Failure category.
- Authorized actor.

Exclude:

- Passwords.
- Tokens.
- Secret keys.
- Private message bodies.
- Payment credentials.
- Signed media URLs.
- Unnecessary personal details.

Restrict log access and define retention.

Do not claim audit records are immutable unless controls support that claim.

## 24. Environment Separation

Separate local, preview, and production configuration.

Use synthetic data and test accounts outside production.

Do not connect an unrestricted preview to production records.

Protect deployment credentials and CI permissions.

Ensure public build variables contain only browser-safe values.

Do not assume environment variables are private after bundling.

Verify callback URLs, webhook endpoints, and allowed origins
for each environment.

## 25. Dependencies and Source Control

Use maintained dependencies appropriate to the selected environment.

Commit lockfiles where applicable.

Review significant dependency additions.

Run relevant dependency checks once tooling exists.

Keep secrets, private media, and real customer datasets out of Git.

If a secret enters Git history:

- Treat it as exposed.
- Revoke or rotate it.
- Investigate access as appropriate.
- Remove it through an authorized cleanup process.

Deleting a secret from the latest file does not revoke it.

## 26. Backups and Recovery

Define and verify:

- What is backed up.
- Backup frequency.
- Retention.
- Access permissions.
- Restoration process.
- Recovery limitations.

Include database and media relationships where relevant.

A provider’s advertised backup feature is not evidence that
restoration has been tested for MeetDiscreet.

Keep recovery credentials protected.

Record material recovery tests.

## 27. Incident Handling

Before production, establish a practical response process.

It should cover:

- Detection.
- Triage.
- Containment.
- Credential revocation.
- Evidence preservation.
- Service recovery.
- Appropriate participant communication.
- Required external escalation.
- Post-incident corrections.

Do not publish sensitive incident details in public repository issues.

Record actual incidents in an appropriately restricted system.

## 28. Verification Requirements

Verify relevant controls before releasing dependent functionality.

Priority checks:

- Cross-account record access.
- Cross-companion entitlement isolation.
- Public-response field filtering.
- Private-media retrieval.
- Upload processing.
- Session expiry and revocation.
- Role escalation attempts.
- CSRF and CORS configuration where relevant.
- Stored-XSS handling.
- Price manipulation.
- Duplicate payment events.
- Concurrent booking conflicts.
- Realtime channel access.
- Call-session access.
- Blocking enforcement.
- Staff capability restrictions.
- Secret exclusion from builds.
- Recovery procedures.

Use unit, integration, browser, and configuration checks as appropriate.

A passing automated scan does not establish complete security.

Record findings, fixes, and unresolved limitations.

## 29. Launch Blockers

Do not release affected functionality when known issues allow:

- Account takeover.
- Unauthorized private-data access.
- Privilege escalation.
- Unverified financial entitlements.
- Secret exposure.
- Private media in public storage.
- Unauthorized administrative actions.
- Uncontrolled duplicate financial processing.

Assess other findings by concrete impact.

Do not conceal a blocker behind a disclaimer.

## 30. Future Scope Changes

A material change to content, identity handling, funds flow,
or communication may change the threat model.

Before enabling it:

1. Revise requirements.
2. Review provider suitability.
3. Reassess data collection and permissions.
4. Update moderation and operational controls.
5. Verify affected flows.
6. Update security claims.

Do not assume current controls cover an unassessed future product.

## 31. Final Rule

Protect the real trust boundaries.

Use backend authorization, private storage, verified financial events,
limited operational access, and evidence-based checks.

Describe security honestly and keep unresolved risks visible.