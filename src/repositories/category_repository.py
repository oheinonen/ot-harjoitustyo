from entities.category import Category
from database_connection import get_database_connection


def get_category_by_row(row):
    return Category(row['category_id'], row['name'], row['owner']) if row else None


class CategoryRepository:
    """ Class responsible for database operations of Category objects
    """

    def __init__(self, connection):
        """Constructor for the class

        Args:
            connection: Connection object for the database
        """
        self._connection = connection

    def create(self, category):
        """Saves new category to the database

        Args:
            category (Category): Category to be saved to the database

        Returns:
            Category: Category object that is saved to the database
        """
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
        """Removes the specified category from the database

        Args:
            category (Category): Category to be deleted

        Returns:
            Boolean: currently always true
        """
        cursor = self._connection.cursor()
        cursor.execute(
            'delete from categories where name = ?',
            (category['name'],)
        )
        self._connection.commit()
        return True

    def find_by_id(self, category_id):
        """Helps to find specified category by id 

        Args:
            category_id (Int): Number corresponding to category id 

        Returns:
            Category: Category object corresponding to the given input
        """
        cursor = self._connection.cursor()
        cursor.execute(
            'select * from categories where category_id = ?',
            (category_id,)
        )
        row = cursor.fetchone()
        return get_category_by_row(row)

    def find_by_name_and_owner(self, name, owner):
        """Helps to find specified category by name and owner

        Args:
            name (String): text corresponding to category name 
            owner (String): tect corresponding to category owner 

        Returns:
            Category: Category object corresponding to the given input
        """

        cursor = self._connection.cursor()
        cursor.execute(
            'select * from categories where name = ? and owner = ?',
            (name, owner)
        )
        row = cursor.fetchone()
        return get_category_by_row(row)

    def next_id(self):
        """Helper function to calculate next id

        Returns:
            Int: next available id number
        """
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
