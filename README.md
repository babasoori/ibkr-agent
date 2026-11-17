# ibkr-agent

A fresh, experimental foundation for an always-on trading agent. **This initial scaffold is simulation-only: it cannot connect to a broker or place orders.** It is not affiliated with Interactive Brokers.

## Start locally

Python 3.11+ is the initial implementation choice: it keeps the prototype small and makes strategy experimentation straightforward. The framework has no runtime dependencies yet.

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
ibkr-agent simulate
python -m unittest discover -s tests -v
```

Without installing: `PYTHONPATH=src python -m ibkr_agent simulate`.
The demo emits one synthetic `DEMO` event and a HOLD decision. BUY/SELL proposals are rejected. No LLM, real market data, account access, background daemon or persistence is implemented.

## Strategy extensions

A trusted Python plugin implements `decide(MarketEvent) -> Decision`. Install your strategy package locally, then use `ibkr-agent simulate --strategy your_package.module:YourStrategy`. Public code never needs access to the plugin source or its repository during CI. Plugins execute Python with the process's permissions; this is **not** a security sandbox.

Keep proprietary strategies in an independent private repository, installed only in your private development/runtime environment. Keep runtime logs, databases and credentials outside both repositories. See [architecture](docs/architecture.md).

## Next milestones

1. Read-only local TWS API adapter; explicit connection settings, fake-adapter tests.
2. Event persistence, stale-data detection and restart/reconciliation tests.
3. Paper-only order lifecycle with deterministic limits and a tested stop mechanism.
4. Separately reviewed live execution, only after account/instrument permissions and applicable restrictions are verified.

Codex is a development tool, not the deployed trading runtime. Start local integration work on the machine running TWS or IB Gateway; cloud CI should use synthetic data only.

## Distribution

No open-source license has been selected yet. Public visibility alone does not grant an open-source license. Choose one before inviting redistribution or contributions.
