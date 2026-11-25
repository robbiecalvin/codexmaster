# Installation Guide 1.0.0
Install the framework only after inspecting the target environment and obtaining authorization for writes. This package is documentation and a read-only verifier, not the final distribution or an installer.

## Start
1. Read INSTALL.md and choose a host guide in hosts/.
2. Stage the assembled framework in an isolated directory. The final master package is a later deliverable.
3. Run `python3 tests/check_installation.py /path/to/framework` from this guide directory.
4. Follow the host guide and smoke tests; record observed evidence using templates/installation-record.json.
5. Review maintenance.md before upgrading or rolling back.

Static checks do not establish runtime behavior. No credentials are required by the verifier.
