from src.recipe import Recipe
from src.ingredient import Ingredient
from src.meal_plan import MealPlan
from datetime import date

class SimpleFactory:
    @staticmethod
    def create_recipe(id, name, instructions):
        return Recipe(id=id, name=name, instructions=instructions)

    @staticmethod
    def create_ingredient(id, name, quantity, unit):
        return Ingredient(id=id, name=name, quantity=quantity, unit=unit)

    @staticmethod
    def create_meal_plan(id, title, start_date, end_date):
        return MealPlan(id=id, title=title, startDate=start_date, endDate=end_date)
