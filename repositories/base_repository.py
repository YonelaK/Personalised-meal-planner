from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional, List

T = TypeVar('T')  # Generic entity type
ID = TypeVar('ID')  # Generic ID type

class Repository(ABC, Generic[T, ID]):
    @abstractmethod
    def save(self, entity: T) -> T:
        """Save an entity and return the saved version"""
        pass
    
    @abstractmethod
    def find_by_id(self, id: ID) -> Optional[T]:
        """Find entity by ID or return None"""
        pass
    
    @abstractmethod
    def find_all(self) -> List[T]:
        """Return all entities"""
        pass
    
    @abstractmethod
    def delete_by_id(self, id: ID) -> None:
        """Delete entity by ID"""
        pass
    
    @abstractmethod
    def exists_by_id(self, id: ID) -> bool:
        """Check if entity exists"""
        pass