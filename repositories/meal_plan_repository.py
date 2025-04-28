from abc import ABC, abstractmethod
from datetime import date
from typing import List
from models.meal_plan import MealPlan
from repositories.base_repository import Repository

class MealPlanRepository(Repository[MealPlan, str], ABC):
    @abstractmethod
    def find_by_user_id(self, user_id: str) -> List[MealPlan]:
        """Find meal plans by user ID"""
        pass
    
    @abstractmethod
    def find_by_date_range(self, 
                         start_date: date, 
                         end_date: date) -> List[MealPlan]:
        """Find meal plans between dates (inclusive)"""
        pass