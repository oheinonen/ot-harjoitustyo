from entities.expense import Expense
from database_connection import get_database_connection


def get_expense_by_row(row):
    if row:
        return Expense(row['expense_id'], row['name'], row['value'],
                       row['category'], row['date'], row['owner'])
    return None


class ExpenseRepository:
    """ Class responsible for database operations of Expense objects
    """

    def __init__(self, connection):
        """Constructor for the class

        Args:
            connection: Connection object for the database
        """
        self._connection = connection

    def create(self, expense):
        """Saves new Expense to the database

        Args:
            expense (Expense): Expense object to be saved into the database

        Returns:
            Expense: Expense object saved to the database
        """

        cursor = self._connection.cursor()

        cursor.execute(
            'insert into expenses (expense_id, name, value, category, date, owner)'
            'values (?, ?, ?, ?, ?, ?)',
            (expense.expense_id, expense.name, expense.value,
             expense.category, expense.date, expense.owner)
        )
        self._connection.commit()
        expense = self.find_by_id(expense.expense_id)

        return expense

    def update(self, expense, new_name, new_value, new_category):
        """Updates existing Expense and saves information to the database

        Args:
            expense_row (Expense): array containing Expense object
            new_name (String):
            name given by the user to be updated to corresponding Expense object
            new_value (String):
            value given by the user to be updated to corresponding Expense object
            new_category (Cateory):
            category given by the user to be updated to corresponding Expense object

        Returns:
            Expense: the updated Expense object
        """
        cursor = self._connection.cursor()
        cursor.execute(
            'update expenses set name = ?, value = ?, category = ? where expense_id = ?',
            (new_name, new_value, new_category, expense.expense_id)
        )
        self._connection.commit()
        expense = self.find_by_id(expense.expense_id)
        return expense

    def remove(self, expense_id):
        cursor = self._connection.cursor()
        cursor.execute(
            'delete from expenses where expense_id = ?',
            (expense_id,)
        )
        self._connection.commit()
        return True

    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute('select * from expenses')
        rows = cursor.fetchall()
        return list(map(get_expense_by_row, rows))
    
    def find_all_by_owner(self, owner):
        cursor = self._connection.cursor()
        cursor.execute(
            'select * from expenses where owner = ?',
            (owner,)
        )
        rows = cursor.fetchall()
        return list(map(get_expense_by_row, rows))
    
    def find_all_by_category_and_owner(self, category, owner):
        cursor = self._connection.cursor()
        cursor.execute(
            'select * from expenses where category = ? and owner = ?',
            (category, owner)
        )
        rows = cursor.fetchall()
        return list(map(get_expense_by_row, rows))

    

    def find_by_id(self, expense_id):
        """Helps to find specified expense by id

        Args:
            expense_id (Int): Number corresponding to expense id

        Returns:
            Expense: Expense object corresponding to the given input
        """

        cursor = self._connection.cursor()
        cursor.execute(
            'select * from expenses where expense_id = ?',
            (expense_id,)
        )
        row = cursor.fetchone()
        return get_expense_by_row(row)

    def next_id(self):
        """Helper function to calculate next id

        Returns:
            Int: next available id number
        """

        cursor = self._connection.cursor()
        cursor.execute(
            'select expense_id from expenses order by expense_id desc limit 1'
        )
        row = cursor.fetchone()
        if row:
            return row[0] + 1
        return None

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute(
            'delete from expenses'
        )
        self._connection.commit()


expense_repository = ExpenseRepository(get_database_connection())
