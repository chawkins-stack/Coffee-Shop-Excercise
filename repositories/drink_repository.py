from models.drink import Drink

class DrinkRepository:
    def __init__(self):
        self._drinks: list[Drink] = []