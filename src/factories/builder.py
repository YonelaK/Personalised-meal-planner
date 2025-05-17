# builder.py


class Meal:
    def __init__(self):
        self.main = None
        self.side = None
        self.drink = None

    def __str__(self):
        return f"Main: {self.main}, Side: {self.side}, Drink: {self.drink}"


class MealBuilder:
    def __init__(self):
        self.meal = Meal()

    def add_main(self, main):
        self.meal.main = main
        return self

    def add_side(self, side):
        self.meal.side = side
        return self

    def add_drink(self, drink):
        self.meal.drink = drink
        return self

    def build(self):
        return self.meal
