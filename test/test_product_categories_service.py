import unittest.mock
from unittest.mock import Mock
from databases.database import Database
from unittest.mock import create_autospec
from services.product_categories_service import ProductCategoriesService

__author__ = "Michael Pogrebinsky - www.topdeveloperacademy.com"


class TestProductCategoriesService(unittest.TestCase):

    def setUp(self):
        self.database = create_autospec(Database)
        self.service = ProductCategoriesService(self.database)

    def test_get_all_supported_categories(self):
        self.database.find_all_category_names.return_value = ["electronics", "art", "toys"]
        expected_categories = "art,electronics,toys"
        self.assertEqual(self.service.get_all_supported_categories(), expected_categories)

    def test_get_all_supported_categories_remove_duplicates(self):
        self.database.find_all_category_names.return_value = ["electronics", "art", "toys", "art"]
        expected_categories = "art,electronics,toys"
        self.assertEqual(self.service.get_all_supported_categories(), expected_categories)

if __name__ == '__main__':
    unittest.main()
