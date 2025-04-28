```mermaid
classDiagram
    class MealPlan {
        +id: str
        +user_id: str
        +date: date
        +recipe_ids: List[str]
    }

    class MealPlanRepository {
        <<abstract>>
        +save(mealPlan: MealPlan): MealPlan
        +find_by_id(id: str): Optional[MealPlan]
        +find_all(): List[MealPlan]
        +delete_by_id(id: str): None
        +exists_by_id(id: str): bool
        +find_by_user_id(user_id: str): List[MealPlan]
        +find_by_date_range(start_date: date, end_date: date): List[MealPlan]
    }

    class InMemoryMealPlanRepository {
        -_storage: Dict[str, MealPlan]
        +save(mealPlan: MealPlan): MealPlan
        +find_by_id(id: str): Optional[MealPlan]
        +find_all(): List[MealPlan]
        +delete_by_id(id: str): None
        +exists_by_id(id: str): bool
        +find_by_user_id(user_id: str): List[MealPlan]
        +find_by_date_range(start_date: date, end_date: date): List[MealPlan]
    }

    class DatabaseMealPlanRepository {
        -session: DatabaseSession
        +save(mealPlan: MealPlan): MealPlan
        +find_by_id(id: str): Optional[MealPlan]
        +find_all(): List[MealPlan]
        +delete_by_id(id: str): None
        +exists_by_id(id: str): bool
        +find_by_user_id(user_id: str): List[MealPlan]
        +find_by_date_range(start_date: date, end_date: date): List[MealPlan]
    }

    class RepositoryFactory {
        +get_repository(repo_type: str, entity: str): MealPlanRepository | UserRepository
        +get_meal_plan_repository(storage_type: str): MealPlanRepository
    }

    MealPlanRepository <|-- InMemoryMealPlanRepository
    MealPlanRepository <|-- DatabaseMealPlanRepository
    RepositoryFactory --> MealPlanRepository

