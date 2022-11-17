from utils.definitions import Config
from utils.order_book import OrderBook
from utils.order_execution_snapshot import OrderExecutionSnapshot


class PnlManager:
    """
    PnlManager is responsible for calculating the PnL of the trading strategy.
    """

    def __init__(self, config: Config) -> None:
        self.starting_balance = config["starting_balance"]
        self.current_balance = config["starting_balance"]
        self.stoploss = config["stoploss"]
        self.current_pose = config["current_pose"]
        self.percentage_fee = config["percentage_fee"]

    def update_on_order_book(self, order_book: OrderBook) -> None:
        """Update the PnL of the trading strategy"""
        self.last_order_book = order_book
        self.last_price = order_book.price

    def update_on_order_execution_snapshot(self, order_execution_snapshot: OrderExecutionSnapshot) -> None:
        """Update the PnL of the trading strategy"""
        self.current_balance -= (
            order_execution_snapshot.amount * order_execution_snapshot.price * (1 + self.percentage_fee)
        )
        self.current_pose += order_execution_snapshot.amount * order_execution_snapshot.dir.dir_sign()
        self.current_balance += self.current_pose * self.last_price * (1 - self.percentage_fee)
        self.current_pose = 0 if abs(self.current_pose) < 1e-6 else self.current_pose

    @property
    def pnl(self) -> float:
        """Return the PnL of the trading strategy"""
        return self.current_balance - self.starting_balance
