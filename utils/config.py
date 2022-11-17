import json


class JsonConfig:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        with open(self.config_file) as f:
            config = json.load(f)
        return config

    def get_dict(self):
        return self.config
