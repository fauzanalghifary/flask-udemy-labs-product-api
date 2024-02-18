import unittest.mock
from unittest.mock import Mock
from databases.database import Database
from unittest.mock import create_autospec
from services.product_categories_service import ProductCategoriesService

__author__ = "Michael Pogrebinsky - www.topdeveloperacademy.com"


class TestProductCategoriesService(unittest.TestCase):

    def test_get_all_supported_categories(self):
        database = Mock()
        database.find_all_categories.return_value = ["electronics", "art", "toys"]
        service = ProductCategoriesService(database)
        expected_categories = "art,electronics,toys"
        self.assertEqual(service.get_all_supported_categories(), expected_categories)

if __name__ == '__main__':
    unittest.main()
