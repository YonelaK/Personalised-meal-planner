from typing import Dict, List, Optional
from datetime import date
from models.meal_plan import MealPlan
from repositories.meal_plan_repository import MealPlanRepository

class InMemoryMealPlanRepository(MealPlanRepository):
    def __init__(self):
        self._storage: Dict[str, MealPlan] = {}
    
    def save(self, meal_plan: MealPlan) -> MealPlan:
        self._storage[meal_plan.id] = meal_plan
        return meal_plan
    
    def find_by_id(self, id: str) -> Optional[MealPlan]:
        return self._storage.get(id)
    
    def find_all(self) -> List[MealPlan]:
        return list(self._storage.values())
    
    def delete_by_id(self, id: str) -> None:
        self._storage.pop(id, None)
    
    def exists_by_id(self, id: str) -> bool:
        return id in self._storage
    
    def find_by_user_id(self, user_id: str) -> List[MealPlan]:
        return [
            mp for mp in self._storage.values() 
            if mp.user_id == user_id
        ]
    
    def find_by_date_range(self, 
                         start_date: date, 
                         end_date: date) -> List[MealPlan]:
        return [
            mp for mp in self._storage.values()
            if start_date <= mp.date <= end_date
        ]