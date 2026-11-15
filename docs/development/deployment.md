# MeetDiscreet — Deployment Guide

## 1. Purpose and Status

Define how MeetDiscreet moves from local development to preview
and production.

This is the deployment specification.
It is not evidence that infrastructure or a pipeline exists.

Current provider selections, commands, and deployment URLs remain
unverified until recorded and tested.

Read alongside:

- ../../AGENTS.md
- ../architecture/environment.md
- ../architecture/application_architecture.md
- ../architecture/repo_map.md
- ../security/application_security.md
- ./launch_acceptance.md
- ../decisions.md
- ../next_steps.md

## 2. Deployment Direction

Develop in VS Code.
Maintain source in GitHub.
Deploy through an appropriate GitHub-connected hosting workflow.

The intended process is:

Edit → Preview locally → Check → Commit → Push → Deploy → Verify

GitHub Pages is not the production host for the commercial marketplace.

Select hosting appropriate to the actual product and backend requirements.

Do not assume pushing to GitHub automatically deploys the application.

## 3. Initial Configuration Register

Complete this register when selections are made.

| Item | Current status |
|---|---|
| Application repository | Not verified |
| Default branch | Not verified |
| Frontend host | Pending |
| Backend host/runtime | Pending |
| Database | Pending |
| Authentication provider | Pending |
| Media storage | Pending |
| Payment provider | Pending |
| Realtime/calling services | Pending |
| Production domain | Pending |
| Local preview command | Not established |
| Build command | Not established |
| Build output directory | Not established |
| Test commands | Not established |
| Preview URL | Not established |
| Production URL | Not established |

Replace pending entries with actual verified values.

Do not include secret values in this document.

## 4. Environments

### Local Development

Purpose:

- Implement pages and features.
- Use synthetic fixtures.
- Run focused tests.
- Integrate approved local or isolated test services.

Do not require production credentials for routine development.

### Preview or Staging

Purpose:

- Review changes.
- Test connected features.
- Validate deployment configuration.
- Exercise payment-provider test mode.

Restrict access where appropriate.

Do not use production customer records in an unrestricted preview.

### Production

Purpose:

- Serve real participants.
- Use approved live services.
- Process live transactions only after readiness and authorization.

Maintain appropriate monitoring, recovery, and support processes.

## 5. Required Separation

Each environment must have appropriate separate configuration for:

- Frontend origin.
- Backend endpoints.
- Database resources.
- Authentication redirects.
- Storage.
- Payment mode.
- Webhooks.
- Realtime/calling credentials.
- Notification delivery.
- Logging.

Do not allow a preview build to use privileged production credentials.

A public client identifier does not replace backend access controls.

## 6. Local Setup

After tooling selection:

1. Document the required runtime.
2. Install declared dependencies.
3. Create local configuration from the safe example.
4. Start the documented HTTP development server.
5. Open the actual local preview URL.
6. Verify representative pages.
7. Run relevant checks.

If npm is selected, use the committed package and lockfile configuration.

Do not list scripts as available until they exist and have been run.

Do not rely on file:// previews for application functionality.

## 7. Source Preparation

Before committing or releasing:

- Inspect repository status.
- Review the diff.
- Preserve unrelated changes.
- Confirm the intended scope.
- Check for secrets and private data.
- Run relevant checks.
- Update affected documentation.

Use focused commits.

Do not commit:

- Credentials.
- Local secret-bearing configuration.
- Private user media.
- Real customer datasets.
- Unnecessary generated files.

A build artifact may be committed only when the approved deployment
process requires it.

## 8. Frontend Hosting

Configure the selected host using verified values:

- Repository.
- Deployment branch or trigger.
- Runtime version where required.
- Install command.
- Build command, if any.
- Output directory.
- Public configuration.
- Preview behaviour.
- Domain.
- HTTPS.
- Routing and not-found behaviour.
- Security headers.

For a static frontend, hosting does not execute backend functions
unless a separate supported runtime is configured.

Do not assume server code runs because it is present in the repository.

## 9. Routing and Assets

Verify:

- Homepage.
- Direct page visits.
- Refresh on nested routes.
- Not-found behaviour.
- Relative links.
- Base-path handling.
- Stylesheets and modules.
- Images and fonts.
- Authentication callbacks.
- Checkout return routes.

Use rewrites only when the actual routing architecture requires them.

Do not route every missing asset to HTML and treat the resulting
response as success.

Check filename casing against the deployed filesystem.

The entrance gate must preserve the intended destination.

## 10. Backend Deployment

Document the selected backend’s actual process.

Verify:

- Runtime compatibility.
- Function or server entry points.
- Required configuration.
- Authentication validation.
- Authorization.
- Allowed origins.
- Request limits.
- Storage permissions.
- Service integrations.
- Logging.
- Health or smoke-check mechanism.

Do not expose service-role credentials to the frontend.

Backend deployment success does not prove domain rules work.
Run relevant functional checks.

## 11. Database Changes

Use versioned migrations.

Before applying a migration:

1. Review its effect.
2. Identify application compatibility requirements.
3. Test against an appropriate nonproduction environment.
4. Assess data loss, locking, and operational impact.
5. Verify backup/recovery readiness where relevant.
6. Establish a recovery approach.

Prefer backward-compatible changes when they support safer rollout.

Do not assume every migration can be reversed safely.

Destructive changes require explicit authorization.

Do not automatically run production seed data intended for development.

## 12. Authentication Configuration

For each environment, verify:

- Allowed application origins.
- Sign-in redirects.
- Confirmation links.
- Recovery links.
- Logout behaviour.
- Session refresh.
- Cookie settings where relevant.
- Restricted-account handling.

Avoid broad redirect wildcards without a justified design.

Do not put production recovery tokens in documentation or logs.

Test deployed callbacks rather than assuming local success transfers
to production.

## 13. Storage and Media

Verify:

- Public versus private containers.
- Upload permissions.
- Read permissions.
- Processing workflow.
- Temporary delivery access.
- Preview generation.
- CORS where needed.
- Deletion and cleanup.
- Backup scope where applicable.

Confirm private originals cannot be retrieved anonymously.

Check that build output contains no restricted uploads.

Do not make storage public to solve an integration error.

## 14. Payment Configuration

Use provider test mode in preview/staging.

Before live configuration:

- Confirm provider suitability.
- Confirm operating region and currency.
- Confirm required recipient onboarding.
- Finalize relevant financial policies.
- Verify product and price references.
- Configure live secrets securely.
- Configure the correct webhook destination.
- Verify event authenticity.
- Verify idempotency and reconciliation.
- Verify cancellation and refund routes.

Keep test and live identifiers clearly separated.

Do not grant access based only on checkout redirects.

Do not enable live charges through a routine visual deployment
unless live payment release is authorized.

## 15. Messaging and Calls

Verify the actual configured:

- Realtime endpoint.
- Channel permissions.
- Subscription checks.
- Attachment access.
- Call signaling.
- Connection credentials.
- Relay or managed connectivity.
- Credential expiry.
- Camera/microphone behaviour.
- Supported browser operation.

Check deployed secure-context requirements.

Do not assume calls work because the interface renders.

No recording is enabled by default.

## 16. Background Jobs

Document actual scheduling and execution for:

- Listing expiry.
- Reservation expiry.
- Notifications.
- Media processing.
- Payment reconciliation.
- Other approved work.

Verify:

- Jobs are registered.
- Required credentials exist.
- Retry behaviour is bounded and safe.
- Duplicate execution is handled.
- Failures are observable.
- Time-zone assumptions are explicit.

A function file does not establish that a scheduler invokes it.

## 17. CI and Deployment Permissions

Use least-privilege workflow credentials.

Keep secrets in the approved secure configuration system.

Do not expose privileged deployment credentials to untrusted
pull-request code.

Review third-party workflow dependencies and permissions.

Document:

- Which events run checks.
- Which events deploy previews.
- Which events deploy production.
- Required checks.
- Environment protections.
- Who can release.

Do not claim these protections are active before verifying configuration.

## 18. Preview Deployment

Before creating or updating a preview:

1. Confirm the intended source revision.
2. Use preview-specific configuration.
3. Build and deploy through the selected process.
4. Inspect the actual deployed URL.
5. Verify relevant pages and integrations.
6. Record limitations.

Use synthetic data and test accounts.

Identify demo or test behaviour clearly enough to avoid confusion.

Do not suggest that a preview is ready for public account collection
or live payments merely because it is accessible.

## 19. Production Release

Before release:

1. Define the exact release scope.
2. Complete relevant launch-acceptance checks.
3. Confirm migrations and service compatibility.
4. Confirm production configuration.
5. Identify the source revision.
6. Confirm recovery procedures.
7. Follow the authorization established for production release.
8. Deploy.
9. Perform post-deployment checks.
10. Record the actual outcome.

Do not repeatedly request approval already given for a defined release.

Do not treat an unrelated implementation request as authorization
to enable new live financial functionality.

## 20. Post-Deployment Checks

Check relevant:

- Public pages.
- Direct links.
- Entrance gate.
- Navigation.
- Asset loading.
- Registration and sign-in.
- Account ownership.
- Restricted profile access.
- Private media.
- Listing management.
- Subscription state.
- Booking state.
- Messaging and calls.
- Support/reporting.
- Operational access.
- Background jobs.
- Error monitoring.

Use appropriate test accounts and authorized verification methods.

Do not create unnecessary real charges to test a deployment.

A successful HTTP response is not enough to validate the application.

## 21. Rollback and Recovery

Define recovery separately for:

- Frontend release.
- Backend release.
- Configuration.
- Database changes.
- External-service state.

A source-code rollback does not automatically reverse:

- Database writes.
- Payment events.
- Sent notifications.
- Payouts.
- Uploaded or deleted media.

Prefer a compatible previous release when possible.

If rollback is unsafe, use an appropriate forward correction.

Record:

- Failed release.
- Affected components.
- Recovery action.
- Data implications.
- Verification result.

Do not repeatedly redeploy the same failing revision without new evidence.

## 22. Deployment Record

For meaningful deployments, record:

- Environment.
- Source commit.
- Deployment identifier where available.
- Timestamp.
- Relevant configuration version.
- Migration references.
- Outcome.
- Verification performed.
- Known limitations.
- Recovery reference if needed.

Do not store secrets.

Keep concise progress references in ../next_steps.md.

## 23. Operational Readiness

Before production use, establish:

- Appropriate monitoring.
- Error visibility.
- Payment reconciliation.
- Backup and restoration procedures.
- Support access.
- Incident handling.
- Privileged-account protection.

Do not assume the hosting provider supplies every operational control
the application requires.

## 24. Troubleshooting

Investigate the relevant boundary.

Examples:

| Symptom | Inspect |
|---|---|
| Missing styles or scripts | Output directory, asset paths, filename casing |
| Nested-page refresh fails | Routing and not-found configuration |
| Sign-in returns to wrong URL | Authentication redirect configuration |
| Private media returns access denial | Session, entitlement, storage policy |
| Paid access remains pending | Verified events and reconciliation |
| Calls fail | Permissions, secure context, signaling, connectivity |
| Expiry does not run | Scheduler registration, job credentials, logs |
| Preview exposes production data | Environment configuration and permissions |

Do not weaken security controls merely to remove an error.

## 25. Open Setup Decisions

Complete and record:

- Repository and branches.
- Runtime and tooling.
- Hosting provider.
- Build/output configuration.
- Backend and database.
- Authentication.
- Storage.
- Payment mode and provider.
- Realtime and calling.
- Notification channels.
- Scheduler.
- Domain.
- Release triggers.
- Recovery process.

Update this guide with verified commands and values as selections
are implemented.

## 26. Final Rule

Deploy a known revision with explicit configuration.

Verify the deployed result.
Keep environments separate.
Preserve recovery paths.
Report actual outcomes rather than assuming success from a push.