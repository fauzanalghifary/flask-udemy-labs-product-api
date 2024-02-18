import unittest
from datetime import datetime
from typing import List

from databases.database import Database, Product
from unittest.mock import create_autospec, patch

from services.products_service import ProductsService

__author__ = "Michael Pogrebinsky - www.topdeveloperacademy.com"


class TestProductsService(unittest.TestCase):
    PRODUCT1 = Product(1, "Color Markers", "Four high quality markers for any art project", "image1.jpg", 10, "art")
    PRODUCT2 = Product(2, "Desktop Monitor", "High Definition 4k Computer Monitor", "image2.jpg", 14.99, "electronics")
    PRODUCT3 = Product(3, "Apple Laptop", "Perfect computer for anything", "image3.jpg", 7000, "electronics")

    def setUp(self):
        self.database = create_autospec(Database)
        self.service = ProductsService(self.database)

    def test_get_deals_of_the_day_with_limit(self):
        self.database.find_at_most_number_of_products.return_value = \
            [TestProductsService.PRODUCT1, TestProductsService.PRODUCT2]
        deals_of_the_day = self.service.get_deals_of_the_day(2)
        self.database.find_at_most_number_of_products.assert_called_once()
        self.assertListEqual(deals_of_the_day, [TestProductsService.PRODUCT1, TestProductsService.PRODUCT2])

    def test_get_products_by_category_correct_category_products(self):
        def mock_find_product_by_category(category: str) -> List[Product]:
            if category == "art":
                return [TestProductsService.PRODUCT1]
            elif category == "electronics":
                return [TestProductsService.PRODUCT2, TestProductsService.PRODUCT3]
            else:
                raise AssertionError(f"Unexpected Category {category}")
        self.database.find_product_by_category.side_effect = mock_find_product_by_category
        self.assertListEqual(self.service.get_products_by_category("art"), [TestProductsService.PRODUCT1])
        self.assertListEqual(self.service.get_products_by_category("electronics"),
                             [TestProductsService.PRODUCT3, TestProductsService.PRODUCT2])

    def test_get_products_by_category_empty_category_raises_exception(self):
        with self.assertRaises(ValueError) as context_manager:
            self.service.get_products_by_category("")
        self.database.find_product_by_category.assert_not_called()

if __name__ == '__main__':
    unittest.main()
