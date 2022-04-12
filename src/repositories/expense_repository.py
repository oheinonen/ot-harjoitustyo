from entities.expense import Expense
from database_connection import get_database_connection


def get_expense_by_row(row):
    if row:
        return Expense(row['id'], row['name'], row['value'],
                       row['category'], row['date'], row['owner'])
    return None


class ExpenseRepository:

    def __init__(self, connection):
        self._connection = connection

    def create(self, name, value, category, owner):
        expense_id = self.next_id()
        if not expense_id:
            expense_id = 0
        cursor = self._connection.cursor()

        cursor.execute(
            'insert into expenses (id, name, value, category, date,owner)'
            'values (?, ?, ?, ?, CURRENT_DATE,?)',
            (expense_id, name, value, category, owner)
        )
        self._connection.commit()
        expense = self.find_by_id(expense_id)

        return expense

    def find_by_id(self, expense_id):
        cursor = self._connection.cursor()
        cursor.execute(
            'select * from expenses where id = ?',
            (expense_id,)
        )
        row = cursor.fetchone()
        return get_expense_by_row(row)

    def next_id(self):
        cursor = self._connection.cursor()
        cursor.execute(
            'select id from expenses order by id desc limit 1'
        )
        row = cursor.fetchone()
        if row:
            return row[0] + 1
        return None

    def find_by_name(self, name):
        cursor = self._connection.cursor()
        cursor.execute(
            'select * from expenses where name = ?',
            (name,)
        )
        row = cursor.fetchone()
        return get_expense_by_row(row)

    def find_all(self, owner):
        cursor = self._connection.cursor()
        cursor.execute(
            'select * from expenses where owner = ?',
            (owner,)
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
