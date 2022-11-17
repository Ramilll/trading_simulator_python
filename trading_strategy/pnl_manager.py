class PnlManager:
    """
    PnlManager is responsible for calculating the PnL of the trading strategy.
    """
    def __init__(self, starting_balance=0, stoploss=-5000, current_position=0, fee=0.0) -> None:
        self.starting_balance = starting_balance
        self.current_balance = starting_balance
        self.stoploss = stoploss
        self.current_position = current_position
        self.fee = fee

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

        