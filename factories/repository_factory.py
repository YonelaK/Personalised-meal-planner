from repositories.meal_plan_repository import MealPlanRepository
from repositories.inmemory.in_memory_meal_plan_repository import InMemoryMealPlanRepository
from repositories.user_repository import UserRepository  # Assuming these exist
from repositories.inmemory.in_memory_user_repository import InMemoryUserRepository

class RepositoryFactory:
    """Factory for creating repository instances with configurable storage backend."""
    
    _STORAGE_TYPES = {
        'memory': {
            'meal_plan': InMemoryMealPlanRepository,
            'user': InMemoryUserRepository
        },
        # Future storage types can be added here:
        # 'database': {...},
        # 'filesystem': {...}
    }

    @classmethod
    def get_repository(cls, 
                     entity_type: str, 
                     storage_type: str = 'memory') -> MealPlanRepository | UserRepository:
        """
        Get a repository instance for the specified entity and storage type.
        
        Args:
            entity_type: 'meal_plan' or 'user'
            storage_type: Storage backend (default: 'memory')
            
        Returns:
            Repository instance
            
        Raises:
            ValueError: For invalid entity or storage types
        """
        try:
            return cls._STORAGE_TYPES[storage_type][entity_type]()
        except KeyError:
            raise ValueError(
                f"Unsupported combination: entity={entity_type}, storage={storage_type}"
            )

    # Alternative simplified version (if you only need meal plans):
    @classmethod
    def get_meal_plan_repository(cls, storage_type: str = 'memory') -> MealPlanRepository:
        """Convenience method for meal plan repositories"""
        return cls.get_repository('meal_plan', storage_type)

# Add this to your existing RepositoryFactory class
_STORAGE_TYPES = {
    'memory': {
        'meal_plan': InMemoryMealPlanRepository,
        'user': InMemoryUserRepository
    },
    'database': {  # New storage type
        'meal_plan': DatabaseMealPlanRepository,
        # 'user': DatabaseUserRepository  # Add when implemented
    }
}

# Optional: Add database configuration method
@classmethod
def configure_database(cls, connection_string: str):
    """Future method to configure database connections"""
    cls._db_connection = connection_string
    print(f"Database configured (Not fully implemented yet)")