from dataclasses import dataclass

@dataclass
class Ingredient:
    name: str
    purchasing_cost: float
    marking_percentage: float
    vendor_name: str
    allergens: list[str]
    sales_price: float 
    