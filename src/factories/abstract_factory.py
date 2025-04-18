# src/factories/abstract_factory.py

from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    
    @abstractmethod
    def create_product(self):
        pass
