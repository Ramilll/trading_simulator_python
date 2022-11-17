from dataclasses import dataclass
from definitions import Price

@dataclass
class OrderBook:
    """Simple version of an order book containing timestamp, and price"""
    price: Price
    timestamp: int