# Security guidance

## Reporting a vulnerability

Use GitHub private vulnerability reporting if enabled for this repository. Otherwise contact the repository owner privately through the contact information on the [GitHub profile](https://github.com/robbiecalvin). Do not include credentials, personal data or exploit details in public issues.

Include the affected revision, environment, observed behavior, expected behavior and a minimal sanitized reproduction. Avoid testing against systems or accounts without authorization.

## Development safeguards

- Keep credentials in local environment variables or an appropriate secret store.
- Use synthetic fixtures and disposable test environments.
- Review dependency updates and authorization boundaries before release.
- Revoke exposed credentials; removing them from the latest revision is not sufficient.

## Support status

This policy describes reporting and development practices. It does not promise a response SLA, supported release window, completed security audit or production certification.
