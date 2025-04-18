class NutritionalInfo:
    def __init__(self, calories, protein, fat, carbs):
        self._calories = calories
        self._protein = protein
        self._fat = fat
        self._carbs = carbs

    def total_macros(self):
        return f"Calories: {self._calories}, Protein: {self._protein}, Fat: {self._fat}, Carbs: {self._carbs}"
