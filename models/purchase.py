from dataclasses import dataclass
import datetime
from models.customer import Customer, Ingredient
from models.drink import Drink
from models.baked_good import Ingredient



@dataclass
class Purchase:
    timestamp: datetime
    items: list[Drink, Ingredient]
    total_cost: float
    Customer: Customer
     
