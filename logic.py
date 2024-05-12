import random
from decouple import config

class CasinoLogic:
    def __init__(self):
        self.winning_slot = random.randint(1, 10)

    def play(self, chosen_slot):
        return chosen_slot == self.winning_slot
