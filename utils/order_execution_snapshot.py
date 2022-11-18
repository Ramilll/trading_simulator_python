from dataclasses import dataclass

from utils.definitions import Price
from utils.dir import Dir


@dataclass
class OrderExecutionSnapshot:
    dir: Dir
    price: Price
    amount: int
