from datetime import datetime
import unittest
import datetime
from entities.expense import Expense
from entities.category import Category
from entities.user import User

from services.expense_service import ExpenseService


from services.user_service import (
    UserService,
    InvalidCredentialsError,
    UsernameExistsError
)
from services.category_service import (
    CategoryService,
    CategoryExistsError
)


class FakeUserRepository:

    def __init__(self, users=None):
        self.users = users or []

    def create(self, user):
        self.users.append(user)

        return user

    def find_all(self):
        return self.users

    def find_by_username(self, username):
        user = filter(lambda user: user.username == username, self.users)
        return user

    def delete_all(self):
        self.users = []


class FakeExpenseRepository:

    def __init__(self, expenses=None):
        self.expenses = expenses or []

    def create(self, expense):
        self.expenses.append(expense)

    def remove(self, expense_id):
        self.expenses.remove(self.find_by_id(expense_id))

    def find_by_id(self, expense_id):
        expense = filter(lambda expense: expense.expense_id == expense_id,
                         self.expenses
                         )
        return expense

    def find_all(self, owner):
        expenses = filter(lambda expense: expense.owner == owner,
                          self.expenses
                          )
        return expenses

    def delete_all(self):
        self.expenses = []


class TestExpenseService(unittest.TestCase):
    def setUp(self):
        self.expense_service = ExpenseService(FakeExpenseRepository())
        self.user_service = UserService(FakeUserRepository())
        self.testUser1 = User('Matti', '12345')
        self.testUser2 = User('Minna', '54321')
        self.testExpense1 = Expense(
            0, 'TV', '200', 'Living', '01/04/2022', 'Matti')
        self.testExpense2 = Expense(
            1, 'Hamburger', '10', 'Food', '05/04/2022', 'Minna')

    def login(self, user):
        self.user_service.create_user(user.username, user.password)


#    def test_create_expense(self):
#       self.login(self.testUser2)
#
#        self.expense_service.create_expense(
#           self.testExpense2.name,
#             self.testExpense2.value,
#              self.testExpense2.category
#        )
#        expenses = self.find_all_expenses()
#        self.assertEqual(len(expenses), 1)
#        self.assertEqual(expenses[0].name, self.testExpense2.name)
#        self.assertEqual(expenses[0].value, self.testExpense2.value)
#        self.assertEqual(expenses[0].category, self.testExpense2.category)
#        self.assertEqual(expenses[0].date, datetime.datetime.now().strftime('%d/%m/%Y'))
#        self.assertEqual(expenses[0].owner, self.testExpense2.owner)
