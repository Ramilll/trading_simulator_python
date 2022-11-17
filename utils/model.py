import pandas as pd
from utils.definitions import Price, Prediction


class Model:
    @staticmethod
    def get_predictions_by_timestamp(path, column_name):
        df = pd.read_csv(path)
        timestamp = pd.to_datetime(df["time"]).apply(lambda x: x.value)
        predictions = df[column_name] - df["market price"]
        return dict(zip(timestamp, predictions))

    def __init__(self, path: str, model_name: str) -> None:
        self.path = path
        self.model_name = model_name
        self.predictions_by_timestamp = self.get_predictions_by_timestamp(self.path, self.model_name)

    def predict(self, timestamp: int) -> Prediction:
        return self.predictions_by_timestamp[timestamp]
