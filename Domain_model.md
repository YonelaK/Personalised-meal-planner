

## **Domain Model – Personalized Meal Planner System**

| **Entity**            | **Attributes**                                                                 | **Methods**                                      | **Relationships**                                                                                      | **Business Rules**                                                                                     |
|-----------------------|--------------------------------------------------------------------------------|--------------------------------------------------|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| **User**              | id, name, email                                                                | createMealPlan(), viewShoppingList()             | - Has many Meal Plans<br>- Has many Preferences<br>- Has many Dietary Restrictions                      | - A user can have multiple meal plans<br>- A user sets personal dietary preferences and restrictions    |
| **Meal Plan**         | id, title, startDate, endDate                                                  | generateShoppingList(), addRecipe()              | - Belongs to one User<br>- Has many Recipes<br>- Has one Shopping List                                  | - Each meal plan spans a date range and contains one or more recipes                                   |
| **Recipe**            | id, name, instructions                                                         | calculateNutrition(), listIngredients()          | - Belongs to many Meal Plans<br>- Has many Ingredients<br>- Has one NutritionalInfo                     | - Recipes with restricted ingredients are excluded from suggested plans                                |
| **Ingredient**        | id, name, quantity, unit                                                       | none                                             | - Belongs to many Recipes<br>- Belongs to many Shopping Lists                                           | - Ingredients are combined when generating shopping lists if repeated                                  |
| **Nutritional Info**  | calories, protein, fat, carbs                                                  | totalMacros()                                    | - Belongs to one Recipe                                                                                 | - Nutritional values are tracked per recipe and summarized in meal plans                               |
| **Preference**        | foodType, isPreferred                                                          | none                                             | - Belongs to one User                                                                                    | - Preferred food types guide recipe suggestions                                                         |
| **Dietary Restriction**| restrictedItem, reason                                                        | none                                             | - Belongs to one User                                                                                    | - Recipes containing restricted items are filtered out                                                  |

---

### Business Rules Summary:
- A user can have **multiple meal plans**, each covering a different date range.
- A **meal plan must include at least one recipe**.
- A **shopping list is automatically generated** from all ingredients in the plan.
- A **user’s preferences** help **prioritize recipes** during suggestions.
- **Dietary restrictions must be enforced**, e.g., exclude recipes with allergens.




  
