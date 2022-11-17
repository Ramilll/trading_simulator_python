from dataclasses import dataclass
from utils.dir import Dir 
from definitions import Price


@dataclass
class Action:
    dir: Dir
    price: Price
    amount: int