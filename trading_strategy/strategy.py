from utils.action import Action
from typing import Union
from utils.order_book import OrderBook
from utils.definitions import Config

class TradingStrategy:
    """
    Trading strategy for a single instrument
    """

    def __init__(self, config: Config) -> None:
        pass

    def step(self, order_book: OrderBook) -> Union[Action, None]:
        """Simulate one step of the trading strategy
        """
        return None
    