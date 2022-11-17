from utils.definitions import Config
class PnlManager:
    """
    PnlManager is responsible for calculating the PnL of the trading strategy.
    """
    def __init__(self, config: Config) -> None:
        self.starting_balance = config["starting_balance"]
        self.current_balance = config["starting_balance"]
        self.stoploss = config["stoploss"]
        self.current_position = config["current_position"]
        self.percentage_fee = config["percentage_fee"]

    def update(self, order_book) -> None:
        """Update the PnL of the trading strategy
        """
        self.last_order_book = order_book
        self.last_price = order_book.price

    @property
    def pnl(self) -> float:
        """Return the PnL of the trading strategy
        """
        return self.current_balance - self.starting_balance

        