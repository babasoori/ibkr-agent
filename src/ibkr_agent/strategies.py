from .contracts import Decision, MarketEvent

class HoldStrategy:
    """Non-trading demonstration; not an investment strategy."""
    def decide(self, event: MarketEvent) -> Decision:
        return Decision("HOLD", event.symbol)
