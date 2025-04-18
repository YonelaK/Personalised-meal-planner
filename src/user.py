class User:
    def __init__(self, id, name, email):
        self._id = id
        self._name = name
        self._email = email

    def create_meal_plan(self):
        return MealPlan(self._id)

    def view_shopping_list(self):
        return ShoppingList(self._id)

