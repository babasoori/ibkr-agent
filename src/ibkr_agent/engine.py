"""Deterministic, finite simulation. Intentionally contains no order-submission API."""
from dataclasses import dataclass
from math import isfinite
from .contracts import Decision, MarketEvent, Strategy

@dataclass(frozen=True)
class Assessment:
    decision: Decision
    accepted: bool
    reason: str

def assess(event: MarketEvent, decision: Decision) -> Assessment:
    # Fail closed. A real risk engine will require substantially more validation.
    if not isinstance(decision, Decision):
        raise TypeError("Strategy must return Decision")
    if not event.symbol or not isfinite(event.price) or event.price <= 0:
        return Assessment(decision, False, "invalid market event")
    if decision.symbol != event.symbol:
        return Assessment(decision, False, "symbol mismatch")
    if decision.action == "HOLD" and type(decision.quantity) is int and decision.quantity == 0:
        return Assessment(decision, True, "no action required")
    return Assessment(decision, False, "order submission is disabled in this scaffold")

def run(strategy: Strategy, events: list[MarketEvent]) -> list[Assessment]:
    return [assess(event, strategy.decide(event)) for event in events]
