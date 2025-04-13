### Design Decisions Explained
Encapsulation: Private fields (-) for attributes and public methods (+) for actions promote object-oriented design.

Associations:

A User can have multiple MealPlans, Preferences, and DietaryRestrictions.

Each MealPlan must generate one ShoppingList and contain one or more Recipes.

Composition:

ShoppingList is tightly linked to a MealPlan — it wouldn’t exist without it.

Aggregation:

Recipe aggregates Ingredients, meaning they can exist independently but are reused.

NutritionalInfo is tightly bound to a single Recipe.

Methods were added where key operations are performed — such as generating lists or calculating nutritional information.

```mermaid
classDiagram
    class User {
        -id: int
        -name: string
        -email: string
        +createMealPlan(): MealPlan
        +viewShoppingList(): ShoppingList
    }

    class MealPlan {
        -id: int
        -title: string
        -startDate: date
        -endDate: date
        +generateShoppingList(): ShoppingList
        +addRecipe(recipe: Recipe): void
    }

    class Recipe {
        -id: int
        -name: string
        -instructions: string
        +calculateNutrition(): NutritionalInfo
        +listIngredients(): Ingredient[]
    }

    class Ingredient {
        -id: int
        -name: string
        -quantity: float
        -unit: string
    }

    class NutritionalInfo {
        -calories: float
        -protein: float
        -fat: float
        -carbs: float
        +totalMacros(): string
    }

    class ShoppingList {
        -id: int
        +viewItems(): Ingredient[]
    }

    class Preference {
        -foodType: string
        -isPreferred: boolean
    }

    class DietaryRestriction {
        -restrictedItem: string
        -reason: string
    }

    %% Relationships
    User "1" -- "0..*" MealPlan : creates
    User "1" -- "0..*" Preference : sets
    User "1" -- "0..*" DietaryRestriction : sets
    MealPlan "1" -- "1" ShoppingList : generates
    MealPlan "1" -- "1..*" Recipe : includes
    Recipe "1" -- "1" NutritionalInfo : has
    Recipe "1" -- "1..*" Ingredient : uses
    ShoppingList "1" -- "1..*" Ingredient : contains

