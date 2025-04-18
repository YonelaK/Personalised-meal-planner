from factories.simple_factory import SimpleFactory
from datetime import date

# Test creating a Recipe
recipe = SimpleFactory.create_recipe(1, "Spaghetti", "Boil pasta. Add sauce.")
print("Recipe:", recipe.name, "| Instructions:", recipe.instructions)

# Test creating an Ingredient
ingredient = SimpleFactory.create_ingredient(1, "Tomato", 2.5, "kg")
print("Ingredient:", ingredient.name, "| Quantity:", ingredient.quantity, ingredient.unit)

# Test creating a MealPlan
meal_plan = SimpleFactory.create_meal_plan(1, "Weekly Plan", date(2025, 4, 18), date(2025, 4, 25))
print("Meal Plan:", meal_plan.title, "| Dates:", meal_plan.startDate, "-", meal_plan.endDate)
