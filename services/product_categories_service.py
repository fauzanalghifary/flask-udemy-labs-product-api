from databases.database import Database

__author__ = "Michael Pogrebinsky - www.topdeveloperacademy.com"


class ProductCategoriesService:
    def __init__(self, database: Database):
        self._database = database

    def get_all_supported_categories(self) -> str:
        """Returns a comma separated list of categories, sorted alphabetically"""
        return ",".join(sorted(set(self._database.find_all_categories())))
