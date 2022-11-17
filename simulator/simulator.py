from trading_strategy.pnl_manager import PnlManager
from trading_strategy.strategy import TradingStrategy
from utils.order_book import OrderBook
from utils.config import JsonConfig
from utils.definitions import Config
from typing import List
from hitrate_simulator import HitRateSimulator
from utils.order_execution_snapshot import OrderExecutionSnapshot
from utils.action import Action
import pandas as pd


class Simulator:
    """Simulator for a trading strategy in python containing pnl_manager and trading_strategy"""

    def __init__(self, config: JsonConfig) -> None:
        general_config = config.get_dict()
        simulator_config = general_config["simulator"]
        self.pnl_manager = PnlManager(general_config["pnl_manager"])
        self.trading_strategy = TradingStrategy(general_config["strategy"])

        # simulator
        self.hit_rate = simulator_config["hit_rate"]
        self.data_path = simulator_config["data_path"]
        self.hit_rate_simulator = HitRateSimulator(self.hit_rate)
        self.order_books = self.get_order_books()

    def get_order_books(self) -> List[OrderBook]:
        """Get the order books"""
        df = pd.read_csv(self.data_path)
        timestamps = pd.to_datetime(df["time"]).apply(lambda x: x.value)
        prices = df["market price"]
        return [OrderBook(price, timestamp) for price, timestamp in zip(prices, timestamps)]

    def step(self, order_book: OrderBook) -> None:
        """Simulate one step of the trading strategy"""
        self.pnl_manager.update_on_order_book(order_book)
        action = self.trading_strategy.process_order_book(order_book)
        if action is not None and self.hit_rate_simulator.is_filled():
            order_execution_snapshot = self.execute(action)
            self.pnl_manager.update_on_order_execution_snapshot(order_execution_snapshot)
            self.trading_strategy.process_order_execution_snapshot(order_execution_snapshot)

    def execute(self, action: Action) -> OrderExecutionSnapshot:
        """Execute the simulation"""
        return OrderExecutionSnapshot(action.dir, action.price, action.amount)

    def simulate(self, prices: list) -> None:
        """Run the simulation"""
        for order_book in self.order_books:
            self.step(order_book)
