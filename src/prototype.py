# prototype.py

import copy

class MealPrototype:
    def clone(self):
        return copy.deepcopy(self)

class VegMeal(MealPrototype):
    def __init__(self):
        self.type = "Veg"
        self.items = ["Veg Burger", "Salad", "Juice"]

    def __str__(self):
        return f"{self.type} Meal: {', '.join(self.items)}"

class NonVegMeal(MealPrototype):
    def __init__(self):
        self.type = "Non-Veg"
        self.items = ["Chicken Burger", "Fries", "Soda"]

    def __str__(self):
        return f"{self.type} Meal: {', '.join(self.items)}"
