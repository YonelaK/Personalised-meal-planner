from factories.repository_factory import RepositoryFactory
from models.meal_plan import MealPlan

class MealPlanService:
    def __init__(self, storage_type: str = 'memory'):
        self.repository = RepositoryFactory.get_meal_plan_repository(storage_type)
    
    def create_meal_plan(self, user_id: str, date: date, recipes: list[str]) -> MealPlan:
        meal_plan = MealPlan(user_id=user_id, date=date, recipe_ids=recipes)
        return self.repository.save(meal_plan)
    
    def get_user_plans(self, user_id: str) -> list[MealPlan]:
        return self.repository.find_by_user_id(user_id)