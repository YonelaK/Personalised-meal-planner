from recipe import Recipe


class SimpleFactory:
    @staticmethod
    def create_recipe(recipe_type: str) -> Recipe:
        """Factory method to create a Recipe based on the type."""
        if recipe_type == "vegan":
            return Recipe(name="Vegan Salad", instructions="Mix vegetables.", id=1)
        elif recipe_type == "non-vegan":
            return Recipe(
                name="Chicken Salad", instructions="Mix chicken and vegetables.", id=2
            )
        else:
            raise ValueError("Unknown recipe type")
