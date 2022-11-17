from enum import Enum


class Dir(Enum):
    BID = 0
    ASK = 1

    @staticmethod
    def from_str(s: str) -> "Dir":
        if s.upper() == "BID":
            return Dir.BID
        elif s.upper() == "ASK":
            return Dir.ASK
        else:
            raise ValueError(f"Invalid direction: {s}")

    @staticmethod
    def from_meaning(meaning: str) -> "Dir":
        if meaning == "buy":
            return Dir.BID
        elif meaning == "sell":
            return Dir.ASK
        else:
            raise ValueError(f"Invalid meaning: {meaning}")

    def dir_sign(self) -> int:
        return 1 if self == Dir.BID else -1

    def opposite_dir(self) -> "Dir":
        return Dir.BID if self == Dir.ASK else Dir.ASK
