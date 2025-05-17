# factory_method.py
from src.meal import Meal
from src.vegetarian_meal import VegetarianMeal
from src.non_vegetarian_meal import NonVegetarianMeal


class MealFactory:
    def create_meal(self, meal_type: str) -> Meal:
        if meal_type == "vegetarian":
            return VegetarianMeal()
        elif meal_type == "non_vegetarian":
            return NonVegetarianMeal()
        else:
            raise ValueError(f"Unknown meal type: {meal_type}")
