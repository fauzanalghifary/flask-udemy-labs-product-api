from copy import copy
from operator import attrgetter
from typing import List
from datetime import datetime

from databases.database import Database, Product
__author__ = "Michael Pogrebinsky - www.topdeveloperacademy.com"


class ProductNotInDatabase(Exception):
    """Exception indicating that a requested product does not exist"""
    pass


class ProductsService:

    def __init__(self, database: Database):
        self._database = database

    def get_deals_of_the_day(self, max_number_of_products: int) -> List[Product]:
        """Returns at most max_number_of_products"""

        return self._database.find_at_most_number_of_products(max_number_of_products)


    def get_products_by_category(self, product_category: str) -> List[Product]:
        """Returns all the products of a given category, sorted alphabetically"""

        if not product_category or not product_category.strip():
            print("Product category should be a non-empty string")
        return sorted(self._database.find_product_by_category(product_category), key=attrgetter("name"))

    def get_all_products(self) -> List[Product]:
        """Returns all the products in the store"""

        products = self._database.find_all_products()

        today = datetime.now()
        day = today.day
        month = today.month

        if day == 1 and month == 2:
            return self._apply_discount(products)
        else:
            return products

    @staticmethod
    def _apply_discount(products: List[Product]) -> List[Product]:
        """Discounts all products by 50%"""
        discounted_products = []

        for product in products:
            discounted_product = copy(product)
            discounted_product.apply_discount(0.5)
            discounted_products.append(discounted_product)

        return discounted_products
