from entities.expense import Expense
from database_connection import get_database_connection

def get_expense_by_row(row):
    return Expense(row['id'],row['name'], row['value'],row['category'], row['date']) if row else None


class ExpenseRepository:

    def __init__(self, connection):
        self._connection = connection

    def create(self, id, name, value,category):
        cursor = self._connection.cursor()
        cursor.execute(
            'insert into expenses (id, name, value, category, date) values (?, ?, ?, ?, CURRENT_DATE)',
            (id, name, value, category)
        )
        expense = self.find_by_id(id)
        self._connection.commit()
        return expense

    def find_by_id(self, id):
        cursor = self._connection.cursor()
        cursor.execute(
            'select * from expenses where id = ?',
            (id,)
        )
        row = cursor.fetchone()
        return get_expense_by_row(row)


    def find_by_name(self, name):
        cursor = self._connection.cursor()
        cursor.execute(
            'select * from expenses where name = ?',
            (name,)
        )
        row = cursor.fetchone()
        return get_expense_by_row(row)

    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute(
            'select * from expenses'
        )
        expenses = cursor.fetchall()
        return expenses

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute(
            'delete from expenses'
        )
        self._connection.commit()


expense_repository = ExpenseRepository(get_database_connection())
