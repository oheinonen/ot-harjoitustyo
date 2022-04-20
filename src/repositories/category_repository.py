from entities.category import Category
from database_connection import get_database_connection


def get_category_by_row(row):
    return Category(row['name'], row['owner']) if row else None


class CategoryRepository:

    def __init__(self, connection):
        self._connection = connection

    def create(self, name, owner):
        cursor = self._connection.cursor()

        cursor.execute(
            'insert into categories (name,owner)'
            'values (?,?)',
            (name, owner)
        )
        self._connection.commit()
        category = self.find_by_name(name)

        return category
    
    def remove(self,category):
        cursor = self._connection.cursor()
        cursor.execute(
            'delete from categories where name = ?',
            (category['name'],)
        )
        self._connection.commit()
        return True

    def find_by_name(self, name):
        cursor = self._connection.cursor()
        cursor.execute(
            'select * from categories where name = ?',
            (name,)
        )
        row = cursor.fetchone()
        return get_category_by_row(row)

    def find_all(self, owner):
        cursor = self._connection.cursor()
        cursor.execute(
            'select * from categories where owner = ?',
            (owner,)
        )
        categories = cursor.fetchall()
        return categories

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute(
            'delete from categories'
        )
        self._connection.commit()


category_repository = CategoryRepository(get_database_connection())
