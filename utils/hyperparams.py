from utils.definitions import Config


class Hyperparams:
    def __init__(self, config: Config):
        self.buy_threshold = config["buy_threshold"]
        self.sell_threshold = config["sell_threshold"]
        self.pose_slope = config["pose_slope"]
