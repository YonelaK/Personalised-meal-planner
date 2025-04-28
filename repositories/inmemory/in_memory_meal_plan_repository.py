from typing import Dict, List, Optional
from datetime import date
import uuid
from models.meal_plan import MealPlan
from repositories.meal_plan_repository import MealPlanRepository

class InMemoryMealPlanRepository(MealPlanRepository):
    def __init__(self):
        self._storage: Dict[str, MealPlan] = {}
    
    def save(self, meal_plan: MealPlan) -> MealPlan:
        """Create or update a meal plan"""
        if not meal_plan.id:
            meal_plan.id = str(uuid.uuid4())
        self._storage[meal_plan.id] = meal_plan
        return meal_plan
    
    def find_by_id(self, id: str) -> Optional[MealPlan]:
        """Find by ID or return None if not found"""
        return self._storage.get(id)
    
    def find_all(self) -> List[MealPlan]:
        """Return all meal plans"""
        return list(self._storage.values())
    
    def delete_by_id(self, id: str) -> None:
        """Delete a meal plan by ID"""
        self._storage.pop(id, None)
    
    def exists_by_id(self, id: str) -> bool:
        """Check if a meal plan exists"""
        return id in self._storage
    
    def find_by_user_id(self, user_id: str) -> List[MealPlan]:
        """Find all meal plans for a specific user"""
        return [
            mp for mp in self._storage.values() 
            if mp.user_id == user_id
        ]
    
    def find_by_date_range(self, 
                         start_date: date, 
                         end_date: date) -> List[MealPlan]:
        """Find meal plans within a date range (inclusive)"""
        return [
            mp for mp in self._storage.values()
            if start_date <= mp.date <= end_date
        ]