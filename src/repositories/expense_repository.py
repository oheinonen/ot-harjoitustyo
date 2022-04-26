from entities.expense import Expense
from database_connection import get_database_connection


def get_expense_by_row(row):
    if row:
        return Expense(row['expense_id'], row['name'], row['value'],
                       row['category'], row['date'], row['owner'])
    return None


class ExpenseRepository:

    def __init__(self, connection):
        self._connection = connection

    def create(self, expense):

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

    def update(self, expense_row, new_name, new_value, new_category):
        cursor = self._connection.cursor()
        expense = get_expense_by_row(expense_row)
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

    def find_all(self, owner):
        cursor = self._connection.cursor()
        cursor.execute(
            'select * from expenses where owner = ?',
            (owner,)
        )
        expenses = cursor.fetchall()
        return expenses


    def find_by_id(self, expense_id):
        cursor = self._connection.cursor()
        cursor.execute(
            'select * from expenses where expense_id = ?',
            (expense_id,)
        )
        row = cursor.fetchone()
        return get_expense_by_row(row)

    def next_id(self):
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
