from trading_strategy.pnl_manager import PnlManager
from trading_strategy.strategy import TradingStrategy
from utils.order_book import OrderBook

class Simulator:
    """Simulator for a trading strategy in python
    """
    def __init__(self, pnl_manager: PnlManager, trading_strategy: TradingStrategy) -> None:
        self.pnl_manager = pnl_manager
        self.trading_strategy = trading_strategy

    def step(self, order_book: OrderBook) -> None:
        """Simulate one step of the trading strategy
        """
        self.pnl_manager.update(order_book)
        action = self.trading_strategy.step(order_book)

    def run(self, prices: list) -> None:
        """Run the simulation
        """
        for price in prices:
            self.step(price)
        print(self.pnl_manager.pnl)