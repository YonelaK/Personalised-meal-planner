# src/tests/test_abstract_factory.py

import unittest
from factories.concrete_factory import ConcreteFactory
from src.product import Product


class TestAbstractFactory(unittest.TestCase):

    def test_create_product(self):
        factory = ConcreteFactory()
        product = factory.create_product()
        self.assertIsInstance(product, Product)  # Check that it's a Product instance
        self.assertEqual(
            product.get_name(), "Product"
        )  # Optional, depends on your product class


if __name__ == "__main__":
    unittest.main()
