from typing import List

import numpy as np

from trading_strategy.single_model import SingleModel
from utils.definitions import Prediction


class Model:
    def __init__(self, config) -> None:
        self.path = config["path"]
        self.model_names = config["model_names"]
        self.models = [SingleModel(self.path, model_name) for model_name in self.model_names]

    def predict(self, timestamp: int) -> Prediction:
        predictions = [model.predict(timestamp) for model in self.models]
        return Prediction(np.mean(predictions))
