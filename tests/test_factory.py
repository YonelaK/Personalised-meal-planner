import unittest
from factories.repository_factory import RepositoryFactory


class TestRepositoryFactory(unittest.TestCase):
    def test_get_meal_plan_repository(self):
        repo = RepositoryFactory.get_meal_plan_repository()
        self.assertIsNotNone(repo)

    def test_invalid_storage_type(self):
        with self.assertRaises(ValueError):
            RepositoryFactory.get_meal_plan_repository("invalid_storage")

    def test_invalid_entity_type(self):
        with self.assertRaises(ValueError):
            RepositoryFactory.get_repository("invalid_entity", "memory")


if __name__ == "__main__":
    unittest.main()
