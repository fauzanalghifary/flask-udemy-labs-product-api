from typing import List, Optional
import sqlite3

__author__ = "Michael Pogrebinsky - www.topdeveloperacademy.com"


class Product:

    def __init__(self, product_id: int, name: str, description: str, image_file_name: str, price_usd: float,
                 category: str):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.image_file_name = image_file_name
        self.price_usd = price_usd
        self.category = category

    def to_dict(self):
        return {"id": self.product_id,
                "name": self.name,
                "description": self.description,
                "imageFileName": self.image_file_name,
                "priceUSD": self.price_usd,
                "category": self.category}

    def apply_discount(self, discount: float):
        self.price_usd = self.price_usd * discount


class Database:
    DATABASE_FILE = "resources/database.db"

    def find_all_category_names(self) -> List[str]:
        """Returns the category names as a list of strings"""

        connection = sqlite3.connect(Database.DATABASE_FILE)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        results = cursor.execute("SELECT * FROM product_categories").fetchall()
        connection.close()

        return [category[1] for category in results]

    def find_at_most_number_of_products(self, max_number_of_products) -> List[Product]:
        """Returns at most max_number_of_products of products from the database"""
        connection = sqlite3.connect(Database.DATABASE_FILE)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        rows = cursor.execute("SELECT * FROM products limit (?)", (max_number_of_products,)).fetchall()

        connection.close()

        return [Product(row['id'],
                        row['name'],
                        row['description'],
                        row['image_file_name'],
                        row['priceusd'],
                        row['category']) for row in rows]

    def find_product_by_category(self, category: str) -> List[Product]:
        """Returns all the products of a given category"""

        connection = sqlite3.connect(Database.DATABASE_FILE)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        rows = cursor.execute("SELECT * FROM products WHERE category = (?)", (category,)).fetchall()

        connection.close()

        return [Product(
            row['id'],
            row['name'],
            row['description'],
            row['image_file_name'],
            row['priceusd'],
            row['category']) for row in rows]

    def find_all_products(self) -> List[Product]:
        """Returns all the products in the database"""

        connection = sqlite3.connect(Database.DATABASE_FILE)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        rows = cursor.execute("SELECT * FROM products").fetchall()

        connection.close()
        return [Product(
            row['id'],
            row['name'],
            row['description'],
            row['image_file_name'],
            row['priceusd'],
            row['category']) for row in rows]

    def find_product_by_id(self, product_id: int) -> Optional[Product]:
        """Returns a particular product given its unique id"""

        connection = sqlite3.connect(Database.DATABASE_FILE)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        row = cursor.execute("SELECT * FROM products where id = (?)", (product_id,)).fetchone()

        connection.close()

        if row is None:
            return None

        return Product(
            row['id'],
            row['name'],
            row['description'],
            row['image_file_name'],
            row['priceusd'],
            row['category'])
