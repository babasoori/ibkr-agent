import argparse
from dataclasses import asdict
from importlib import import_module
import json
from .contracts import MarketEvent
from .engine import run
from .strategies import HoldStrategy

def load_strategy(spec: str):
    module, separator, name = spec.partition(":")
    if not separator or not module or not name:
        raise ValueError("Use installed_module:ClassName")
    # Plugins are trusted local Python code, not a sandbox.
    strategy = getattr(import_module(module), name)()
    if not callable(getattr(strategy, "decide", None)):
        raise TypeError("Strategy must implement decide(event)")
    return strategy

def main(argv=None):
    parser = argparse.ArgumentParser(description="Simulation only: no broker connections or orders")
    parser.add_argument("command", choices=["simulate"])
    parser.add_argument("--strategy", help="Trusted installed Python plugin as module:ClassName")
    args = parser.parse_args(argv)
    strategy = load_strategy(args.strategy) if args.strategy else HoldStrategy()
    events = [MarketEvent("DEMO", 100.0, "2026-01-01T00:00:00Z")]
    for result in run(strategy, events):
        print(json.dumps(asdict(result), sort_keys=True))

if __name__ == "__main__":
    main()
