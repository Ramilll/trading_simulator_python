from utils.action import Action
from typing import Union
from utils.order_book import OrderBook
from utils.definitions import Config
from utils.dir import Dir

class TradingStrategy:
    """
    Trading strategy for a single instrument
    """

    def __init__(self, config: Config) -> None:
        self.hyperparams = config["hyperparams"]
        self.name = config["name"]
        self.model = config["general_model"]

    def step(self, order_book: OrderBook) -> Union[Action, None]:
        """Simulate one step of the trading strategy
        """
        price = order_book.get_price()
        timestamp = order_book.get_timestamp()
        prediction = self.model.predict(timestamp)
        if prediction > self.hyperparams.buy_threshold:
            return Action(dir=Dir.from_meaning("buy"), price=price, amount=1)
        elif prediction < self.hyperparams.sell_threshold:
            return Action(dir=Dir.from_meaning("sell"), price=price, amount=1)
        return None
    