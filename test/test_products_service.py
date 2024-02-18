import unittest
from datetime import datetime
from typing import List

from databases.database import Database, Product
from unittest.mock import create_autospec, patch

from services.products_service import ProductsService

__author__ = "Michael Pogrebinsky - www.topdeveloperacademy.com"


class TestProductsService:
    PRODUCT1 = Product(1, "Color Markers", "Four high quality markers for any art project", "image1.jpg", 10, "art")
    PRODUCT2 = Product(2, "Desktop Monitor", "High Definition 4k Computer Monitor", "image2.jpg", 14.99, "electronics")
    PRODUCT3 = Product(3, "Apple Laptop", "Perfect computer for anything", "image3.jpg", 7000, "electronics")


if __name__ == '__main__':
    unittest.main()
