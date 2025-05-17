# test_factory_method.py
import unittest
from factories.factory_method import MealFactory
from src.vegetarian_meal import VegetarianMeal
from src.non_vegetarian_meal import NonVegetarianMeal


class TestFactoryMethod(unittest.TestCase):

    def setUp(self):
        self.factory = MealFactory()

    def test_create_vegetarian_meal(self):
        meal = self.factory.create_meal("vegetarian")
        self.assertIsInstance(meal, VegetarianMeal)

    def test_create_non_vegetarian_meal(self):
        meal = self.factory.create_meal("non_vegetarian")
        self.assertIsInstance(meal, NonVegetarianMeal)

    def test_invalid_meal_type(self):
        with self.assertRaises(ValueError):
            self.factory.create_meal("vegan")


if __name__ == "__main__":
    unittest.main()
