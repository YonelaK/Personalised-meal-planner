# test_prototype.py

import unittest
from creational_patterns.prototype import VegMeal, NonVegMeal


class TestPrototype(unittest.TestCase):
    def test_clone_meal(self):
        veg_meal = VegMeal()
        cloned_meal = veg_meal.clone()
        self.assertEqual(str(cloned_meal), str(veg_meal))
        self.assertIsNot(cloned_meal, veg_meal)  # Different instances


if __name__ == "__main__":
    unittest.main()
