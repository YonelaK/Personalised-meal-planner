from datetime import date, timedelta
from models.meal_plan import MealPlan
from repositories.inmemory.in_memory_meal_plan_repository import (
    InMemoryMealPlanRepository,
)

# Initialize repository
repo = InMemoryMealPlanRepository()

# Create sample meal plans
today = date.today()
meal_plan1 = MealPlan(user_id="user1", date=today, recipe_ids=["recipe1", "recipe2"])

meal_plan2 = MealPlan(
    user_id="user1", date=today + timedelta(days=1), recipe_ids=["recipe3"]
)

# Save to repository
repo.save(meal_plan1)
repo.save(meal_plan2)

# Query examples
print(f"All meal plans: {repo.find_all()}")
print(f"Today's plans: {repo.find_by_date_range(today, today)}")
print(f"User1's plans: {repo.find_by_user_id('user1')}")
