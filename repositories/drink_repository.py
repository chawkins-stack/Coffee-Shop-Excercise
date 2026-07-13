from models.drink import Drink

class DrinkRepository:
    def __init__(self):
        self._drinks: list[Drink] = []
    
    def get_all(self) -> list[Drink]:
        return self._drinks
    
    def get_by_id(self, name: str) -> Drink | None:
        return next((d for d in self._drinks if d.name == name), None)

    def add(self, drink: Drink) -> Drink:
        self._drinks.append(drink)
        return drink
    
    def update(self, name: str, drink: Drink) -> Drink | None:
        self._drinks[name] = drink
        return drink

    def delete(self, name: str) -> bool:
        self._drinks.remove(name)
        return True