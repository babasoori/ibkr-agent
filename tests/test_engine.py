import io
import unittest
from contextlib import redirect_stdout
from ibkr_agent.cli import main, load_strategy
from ibkr_agent.contracts import Decision, MarketEvent
from ibkr_agent.engine import assess, run
from ibkr_agent.strategies import HoldStrategy

class EngineTests(unittest.TestCase):
    def setUp(self):
        self.event = MarketEvent("DEMO", 100.0, "2026-01-01T00:00:00Z")
    def test_hold(self):
        self.assertTrue(run(HoldStrategy(), [self.event])[0].accepted)
    def test_orders_fail_closed(self):
        for action in ("BUY", "SELL", "UNKNOWN"):
            self.assertFalse(assess(self.event, Decision(action, "DEMO", 1)).accepted)
    def test_bad_hold(self):
        for qty in (1, -1, True, 0.0):
            self.assertFalse(assess(self.event, Decision("HOLD", "DEMO", qty)).accepted)
    def test_mismatch(self):
        self.assertFalse(assess(self.event, Decision("HOLD", "OTHER")).accepted)
    def test_invalid_price(self):
        for price in (0, -1, float("nan"), float("inf")):
            self.assertFalse(assess(MarketEvent("DEMO", price, ""), Decision("HOLD", "DEMO")).accepted)
    def test_invalid_return(self):
        with self.assertRaises(TypeError): assess(self.event, None)
    def test_plugin(self):
        self.assertIsInstance(load_strategy("ibkr_agent.strategies:HoldStrategy"), HoldStrategy)
    def test_bad_plugin_spec(self):
        with self.assertRaises(ValueError): load_strategy("bad")
    def test_cli(self):
        output = io.StringIO()
        with redirect_stdout(output): main(["simulate"])
        self.assertIn('"action": "HOLD"', output.getvalue())
    def test_live_flag_absent(self):
        with redirect_stdout(io.StringIO()), self.assertRaises(SystemExit):
            main(["live"])

if __name__ == "__main__": unittest.main()
