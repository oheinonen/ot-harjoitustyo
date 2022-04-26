from entities.category import Category
from database_connection import get_database_connection


def get_category_by_row(row):
    return Category(row['category_id'], row['name'], row['owner']) if row else None


class CategoryRepository:

    def __init__(self, connection):
        self._connection = connection

    def create(self, category):
        cursor = self._connection.cursor()

        cursor.execute(
            'insert into categories (category_id, name,owner)'
            'values (?, ?, ?)',
            (category.category_id, category.name, category.owner)
        )
        self._connection.commit()
        category = self.find_by_id(category.category_id)

        return category

    def remove(self, category):
        cursor = self._connection.cursor()
        cursor.execute(
            'delete from categories where name = ?',
            (category['name'],)
        )
        self._connection.commit()
        return True

    def find_by_id(self, category_id):
        cursor = self._connection.cursor()
        cursor.execute(
            'select * from categories where category_id = ?',
            (category_id,)
        )
        row = cursor.fetchone()
        return get_category_by_row(row)

    def find_by_name_and_owner(self, name, owner):
        cursor = self._connection.cursor()
        cursor.execute(
            'select * from categories where name = ? and owner = ?',
            (name, owner)
        )
        row = cursor.fetchone()
        return get_category_by_row(row)

    def next_id(self):
        cursor = self._connection.cursor()
        cursor.execute(
            'select category_id from categories order by category_id desc limit 1'
        )
        row = cursor.fetchone()
        if row:
            return row[0] + 1
        return None

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
