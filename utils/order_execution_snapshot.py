from dataclasses import dataclass
from utils.dir import Dir
from utils.definitions import Price


@dataclass
class OrderExecutionSnapshot:
    dir: Dir
    price: Price
    amount: int
