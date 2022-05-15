from datetime import datetime
import unittest
import datetime
from entities.expense import Expense
from entities.user import User

from services.expense_service import ExpenseService
from services.user_service import UserService


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
        return list(user)
    
    def delete_all(self):
        self.users = []

class FakeExpenseRepository:

    def __init__(self, expenses=None):
        self.expenses = expenses or []

    def create(self, expense):
        self.expenses.append(expense)
        
        return expense

    def remove(self, expense_id):
        self.expenses.remove(self.find_by_id(expense_id))
        return True

    def update(self, expense, new_name, new_value, new_category):

        index = self.expenses.index(self.find_by_id(expense.expense_id))
        self.expenses[index] = Expense(
            expense.expense_id,
            new_name,
            new_value,
            new_category,
            expense.date,
            expense.owner
            ) 
        return self.expenses[index]

    def find_all_by_owner(self, owner):
        expenses = list(filter(lambda expense: expense.owner == owner, self.expenses))
        return expenses

    def find_all_by_category_and_owner(self, category, owner):

        expenses = list(filter(lambda expense:
            expense.owner == owner and expense.category == category, 
            self.expenses
            ))
        return expenses

    def find_by_id(self, expense_id):
        expense = list(filter(lambda expense: expense.expense_id == expense_id,
                         self.expenses
                         ))[0]
        return expense

    def find_all(self):
        return self.expenses
    
    def next_id(self):
        return len(self.expenses)

    def delete_all(self):
        self.expenses = []

class TestExpenseService(unittest.TestCase):
    def setUp(self):
        self.user_service = UserService(FakeUserRepository())
        self.expense_service = ExpenseService(FakeExpenseRepository(),self.user_service)

        self.testUser1 = User('Matti', '12345')
        self.testUser2 = User('Minna', '54321')
        self.testExpense1 = Expense(
            0, 'TV', '200', 'Living', datetime.datetime.now().strftime('%d/%m/%Y'), 'Matti')
        self.testExpense2 = Expense(
            1, 'Hamburger', '10', 'Food', datetime.datetime.now().strftime('%d/%m/%Y'), 'Minna')
        self.testExpense3 = Expense(
            0, 'Pizza', '10', 'Food', datetime.datetime.now().strftime('%d/%m/%Y'), 'Matti')


    def login(self, user):
        self.user_service.create_user(user.username, user.password)

    def test_create_expense(self):
        self.login(self.testUser2)

        expense = self.expense_service.create_expense(
            self.testExpense2.name,
            self.testExpense2.value,
            self.testExpense2.category
        )

        self.assertEqual(expense.name, self.testExpense2.name)
        self.assertEqual(expense.value, self.testExpense2.value)
        self.assertEqual(expense.category, self.testExpense2.category)
        self.assertEqual(expense.date, self.testExpense2.date)
        self.assertEqual(expense.owner, self.testExpense2.owner)

    def test_update_expense(self):
        self.login(self.testUser2)
        updated_name = 'Laptop'
        updated_value = 100
        updated_category = 'School'

        expense = self.expense_service.create_expense(
            self.testExpense2.name,
            self.testExpense2.value,
            self.testExpense2.category
        )
        
        updated_expense = self.expense_service.update_expense(
            expense,
            updated_name,
            updated_value,
            updated_category
        )

        self.assertEqual(updated_expense.name, updated_name)
        self.assertEqual(updated_expense.value, updated_value)
        self.assertEqual(updated_expense.category, updated_category)
        self.assertEqual(updated_expense.date, self.testExpense2.date)
        self.assertEqual(updated_expense.owner, self.testExpense2.owner)

    def test_remove_expense(self):
        self.login(self.testUser2)

        expense = self.expense_service.create_expense(
            self.testExpense2.name,
            self.testExpense2.value,
            self.testExpense2.category
        )

        self.expense_service.remove_expense(expense.expense_id)
        expenses = self.expense_service.find_all_expenses(self.testUser2)
    
        self.assertEqual(len(expenses), 0)


    def test_get_expense_by_id(self):
        self.login(self.testUser1)

        expense = self.expense_service.create_expense(
            self.testExpense1.name,
            self.testExpense1.value,
            self.testExpense1.category
        )
        expense = self.expense_service.get_expense_by_id(self.testExpense1.expense_id)

        self.assertEqual(expense.name, self.testExpense1.name)
        self.assertEqual(expense.value, self.testExpense1.value)
        self.assertEqual(expense.category, self.testExpense1.category)
        self.assertEqual(expense.date, self.testExpense1.date)
        self.assertEqual(expense.owner, self.testExpense1.owner)

    def test_get_expenses_by_category(self):
        self.login(self.testUser1)

        self.expense_service.create_expense(
            self.testExpense1.name,
            self.testExpense1.value,
            self.testExpense1.category
        )

        self.expense_service.create_expense(
            self.testExpense3.name,
            self.testExpense3.value,
            self.testExpense3.category
        )

        expenses = self.expense_service.get_expenses_by_category(self.testExpense1.category)
        expense1 = expenses[0]

        self.assertEqual(len(expenses),1)
        self.assertEqual(expense1.name, self.testExpense1.name)
        self.assertEqual(expense1.value, self.testExpense1.value)
        self.assertEqual(expense1.category, self.testExpense1.category)
        self.assertEqual(expense1.date, self.testExpense1.date)
        self.assertEqual(expense1.owner, self.testExpense1.owner)


