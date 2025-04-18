# src/factories/concrete_factory.py

from .abstract_factory import AbstractFactory
from src.product import Product  # Replace with your actual product class

class ConcreteFactory(AbstractFactory):
    
    def create_product(self):
        return Product()  # Instantiate and return the concrete product
