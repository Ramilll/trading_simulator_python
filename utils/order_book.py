from dataclasses import dataclass
from definitions import Price

@dataclass
class OrderBook:
    """Simple version of an order book containing timestamp, and price"""
    price: Price
    timestamp: int

    def get_price(self) -> Price:
        return self.price
    
    def get_timestamp(self) -> int:
        return self.timestamp