# agent-system adapter

Host must wire routing, stage events, state storage, permissions and test execution. Use task ID and route revision to reject stale events; deduplicate repeated events and reconcile concurrent writes. No runtime hooks are installed by this package.
