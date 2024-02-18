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


if __name__ == '__main__':
    unittest.main()
