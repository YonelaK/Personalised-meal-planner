# test_builder.py

import unittest
from creational_patterns.builder import MealBuilder

class TestBuilder(unittest.TestCase):
    def test_meal_builder(self):
        builder = MealBuilder()
        meal = builder.add_main("Burger").add_side("Fries").add_drink("Cola").build()
        self.assertEqual(meal.main, "Burger")
        self.assertEqual(meal.side, "Fries")
        self.assertEqual(meal.drink, "Cola")

if __name__ == "__main__":
    unittest.main()
