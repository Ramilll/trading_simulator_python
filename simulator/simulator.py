from trading_strategy.pnl_manager import PnlManager
from trading_strategy.strategy import TradingStrategy
from utils.order_book import OrderBook
from utils.config import JsonConfig
from utils.definitions import Config
from typing import List
import pandas as pd


class Simulator:
    """Simulator for a trading strategy in python containing pnl_manager and trading_strategy"""

    def __init__(self, config: JsonConfig) -> None:
        general_config = config.get_dict()
        self.pnl_manager = PnlManager(general_config["pnl_manager"])
        self.trading_strategy = TradingStrategy(general_config["strategy"])

    def get_order_books(self) -> List[OrderBook]:
        """Get the order books"""
        pass

    def step(self, order_book: OrderBook) -> None:
        """Simulate one step of the trading strategy"""
        self.pnl_manager.update(order_book)
        action = self.trading_strategy.step(order_book)

    def simulate(self, prices: list) -> None:
        """Run the simulation"""
        for price in prices:
            self.step(price)
        print(self.pnl_manager.pnl)
