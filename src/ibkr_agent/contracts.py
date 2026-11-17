"""Small versioned boundary between the public engine and strategy plugins."""
from dataclasses import dataclass
from typing import Literal, Protocol

@dataclass(frozen=True)
class MarketEvent:
    symbol: str
    price: float
    timestamp: str

@dataclass(frozen=True)
class Decision:
    action: Literal["HOLD", "BUY", "SELL"]
    symbol: str
    quantity: int = 0

class Strategy(Protocol):
    def decide(self, event: MarketEvent) -> Decision: ...
