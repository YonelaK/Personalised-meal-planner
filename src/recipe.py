class Recipe:
    def __init__(self, id, name, instructions):
        self._id = id
        self._name = name
        self._instructions = instructions
        self._ingredients = []

    def calculate_nutrition(self):
        return NutritionalInfo(self._id)

    def list_ingredients(self):
        return self._ingredients
