from random import random


class HitRateSimulator:
    def __init__(self, hit_rate):
        self.hit_rate = hit_rate

    def is_filled(self):
        return random() < self.hit_rate
