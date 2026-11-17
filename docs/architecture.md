# Architecture and privacy boundary

Market source -> event loop -> strategy -> deterministic risk gate -> execution adapter.

This scaffold implements only synthetic events, a strategy protocol and a fail-closed assessment. There is deliberately no execution adapter yet. The timestamp is descriptive in this demo; freshness validation must be implemented before real data is used.

Public: generic contracts, adapters, risk machinery, educational examples, synthetic tests.
Private: proprietary strategies and prompts, parameters, research and strategy-specific tests.
Outside Git: credentials, account exports, real trade logs and trading-state databases.

Use independent sibling repositories and separate public/private coding workspaces. Public CI must never fetch private strategies. Do not put private code in public branches, PRs, issue text, build logs, artifacts or container images. Secret scanners do not identify proprietary strategy logic. Hosted-model privacy is a separate question from GitHub repository visibility.

Future always-on operation needs durable state, bounded queues, disconnect handling, reconciliation, idempotency, market-data entitlement handling, session reauthentication alerts and operator controls. Do not equate this finite simulator with a production trading system.
