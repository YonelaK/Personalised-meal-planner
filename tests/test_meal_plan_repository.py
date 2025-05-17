import unittest
from datetime import date, timedelta
from models.meal_plan import MealPlan
from repositories.inmemory.in_memory_meal_plan_repository import (
    InMemoryMealPlanRepository,
)


class TestInMemoryMealPlanRepository(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryMealPlanRepository()
        self.today = date.today()
        self.meal_plan = MealPlan(
            user_id="user1", date=self.today, recipe_ids=["recipe1", "recipe2"]
        )

    def test_save_and_retrieve(self):
        # Test creation
        saved = self.repo.save(self.meal_plan)
        self.assertIsNotNone(saved.id)

        # Test retrieval
        retrieved = self.repo.find_by_id(saved.id)
        self.assertEqual(saved, retrieved)

    def test_find_all(self):
        self.repo.save(self.meal_plan)
        self.assertEqual(1, len(self.repo.find_all()))

    def test_delete(self):
        saved = self.repo.save(self.meal_plan)
        self.repo.delete_by_id(saved.id)
        self.assertFalse(self.repo.exists_by_id(saved.id))

    def test_find_by_user(self):
        self.repo.save(self.meal_plan)
        self.repo.save(MealPlan(user_id="user2", date=self.today, recipe_ids=["r3"]))

        user_plans = self.repo.find_by_user_id("user1")
        self.assertEqual(1, len(user_plans))
        self.assertEqual("user1", user_plans[0].user_id)

    def test_find_by_date_range(self):
        yesterday = self.today - timedelta(days=1)
        tomorrow = self.today + timedelta(days=1)

        self.repo.save(self.meal_plan)
        self.repo.save(MealPlan(user_id="user1", date=yesterday, recipe_ids=["r4"]))

        plans = self.repo.find_by_date_range(self.today, tomorrow)
        self.assertEqual(1, len(plans))
        self.assertEqual(self.today, plans[0].date)


if __name__ == "__main__":
    unittest.main()
