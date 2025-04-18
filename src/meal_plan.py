class MealPlan:
    def __init__(self, id, title, start_date, end_date):
        self._id = id
        self._title = title
        self._start_date = start_date
        self._end_date = end_date
        self._recipes = []

    def generate_shopping_list(self):
        return ShoppingList(self._id)

    def add_recipe(self, recipe):
        self._recipes.append(recipe)
