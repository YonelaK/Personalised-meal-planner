# Assignment 11
## Meal Planner - Repository Interfaces (Task 1)

## Implementation Details

### Repository Pattern Structure

1. **Base Repository Interface**
   - Generic interface (`Repository[T, ID]`) with common CRUD operations
   - Uses Python's `ABC` for abstract base class
   - Type hints for better code clarity

2. **MealPlan-specific Repository**
   - Extends base repository with `MealPlan`-specific queries
   - Adds methods like `find_by_user_id` and `find_by_date_range`

3. **In-Memory Implementation**
   - HashMap-based storage (`Dict[str, MealPlan]`)
   - Full implementation of all interface methods

### Why This Design?

1. **Generics**: Avoid code duplication across different entity repositories
2. **Separation of Concerns**: Business logic won't depend on storage details
3. **Testability**: Easy to mock or replace implementations
4. **Future Extensibility**: Can add new storage backends without changing interfaces

### How to Use

```python
from repositories.meal_plan_repository import MealPlanRepository
from repositories.inmemory.in_memory_meal_plan_repository import InMemoryMealPlanRepository

# Use the interface type for variables
repo: MealPlanRepository = InMemoryMealPlanRepository()

# All operations work through the interface
meal_plan = MealPlan(user_id="user1", date=date.today(), recipe_ids=["r1"])
saved = repo.save(meal_plan)
found = repo.find_by_id(saved.id)

## Task 2: In-Memory Implementation
- Completed HashMap-based storage
- Test coverage for all CRUD operations
- Type hints maintained

## Task 3: Storage Abstraction

### Factory Pattern Implementation
- **`RepositoryFactory`**: Centralized creation of repositories
  - Currently supports: `'memory'` storage
  - Easy to extend with `'database'` or `'filesystem'` later
- **Decoupled architecture**:
  ```python
  # Business logic doesn't know about storage details
  repo = RepositoryFactory.get_meal_plan_repository()

## Task 4: Future-Proofing

### Added Database Support Stub
- Created `DatabaseMealPlanRepository` with method stubs
- Ready for implementation with:
  - SQLAlchemy (for SQL databases)
  - Motor (for MongoDB)
  - Firebase/Firestore

### Factory Updates
- Added 'database' storage type option
- Prepared database configuration hook

### How to Extend:
1. Implement database methods in `DatabaseMealPlanRepository`
2. Add connection pooling
3. Implement migrations (e.g., using Alembic)

### Class Diagram
See [docs/class_diagram.md](docs/class_diagram.md)

# Personalised Meal Planner

[Short project description]

## Getting Started

[Setup instructions, prerequisites, installation, how to run]

## Features for Contribution

| Feature              | Description                         | Difficulty          | Labels            |
|----------------------|-----------------------------------|---------------------|-------------------|
| User Authentication  | Implement login/logout system      | Medium              | good-first-issue  |
| Meal Preferences     | Save and update meal choices       | Easy                | good-first-issue  |
| Calorie Calculator   | Add calorie tracking feature       | Medium              | feature-request   |
| Recipe Search        | Improve search algorithm           | Hard                | feature-request   |
| UI Enhancements      | Improve front-end design           | Easy                | good-first-issue  |

## Other existing sections (if any)

