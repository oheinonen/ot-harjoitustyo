import unittest
from repositories.expense_repository import expense_repository
from entities.expense import Expense
import datetime


class TestExpenseRepository(unittest.TestCase):
    def setUp(self):
        expense_repository.delete_all()
        self.testExpense1 = Expense(
            0, 'TV', '200', 'Living', datetime.datetime.now().strftime('%d/%m/%Y'), 'Matti')
        self.testExpense2 = Expense(
            1, 'Hamburger', '10', 'Food', datetime.datetime.now().strftime('%d/%m/%Y'), 'Minna')
        self.testExpense3 = Expense(
            2, 'Pizza', '10', 'Food', datetime.datetime.now().strftime('%d/%m/%Y'), 'Matti')

    def test_create(self):
        expense_repository.create(self.testExpense1)
        expenses = expense_repository.find_all()

        self.assertEqual(len(expenses), 1)
        self.assertEqual(expenses[0].name, self.testExpense1.name)
        self.assertEqual(str(expenses[0].value), self.testExpense1.value)
        self.assertEqual(expenses[0].category, self.testExpense1.category)
        self.assertEqual(expenses[0].date, self.testExpense1.date)
        self.assertEqual(expenses[0].owner, self.testExpense1.owner)

    def test_find_all(self):
        expense_repository.create(self.testExpense1)
        expense_repository.create(self.testExpense2)
        expenses = expense_repository.find_all()

        self.assertEqual(len(expenses), 2)

    def test_find_all_by_owner(self):
        expense_repository.create(self.testExpense1)
        expense_repository.create(self.testExpense2)
        expenses = expense_repository.find_all_by_owner(self.testExpense1.owner)

        self.assertEqual(len(expenses), 1)
        self.assertEqual(expenses[0].name, self.testExpense1.name)
        self.assertEqual(str(expenses[0].value), self.testExpense1.value)
        self.assertEqual(expenses[0].category, self.testExpense1.category)
        self.assertEqual(expenses[0].date, self.testExpense1.date)
        self.assertEqual(expenses[0].owner, self.testExpense1.owner)

    def test_update(self):
        updated_name = 'Laptop'
        updated_value = 100
        updated_category = 'School'
        expense_repository.create(self.testExpense1)
        expense_repository.update(
            self.testExpense1,
            updated_name,
            updated_value,
            updated_category
            )
        expenses = expense_repository.find_all()
        updated_expense = expenses[0]

        self.assertEqual(len(expenses), 1)
        self.assertEqual(updated_expense.name, updated_name)
        self.assertEqual(updated_expense.value, updated_value)
        self.assertEqual(updated_expense.category, updated_category)
        self.assertEqual(updated_expense.date, self.testExpense1.date)
        self.assertEqual(updated_expense.owner, self.testExpense1.owner)

    def test_remove(self):
        expense_repository.create(self.testExpense1)
        expenses = expense_repository.find_all()
        self.assertEqual(len(expenses), 1)
        expense_repository.remove(self.testExpense1.expense_id)
        expenses = expense_repository.find_all()
        self.assertEqual(len(expenses), 0)

    def test_find_all_by_category_and_owner(self):
        expense_repository.create(self.testExpense1)
        expense_repository.create(self.testExpense3)
        expenses = expense_repository.find_all_by_category_and_owner(self.testExpense3.category, self.testExpense1.owner)

        self.assertEqual(len(expenses), 1)
        self.assertEqual(expenses[0].name, self.testExpense3.name)
        self.assertEqual(str(expenses[0].value), self.testExpense3.value)
        self.assertEqual(expenses[0].category, self.testExpense3.category)
        self.assertEqual(expenses[0].date, self.testExpense3.date)
        self.assertEqual(expenses[0].owner, self.testExpense3.owner)

    def test_find_by_id(self):
        expense_repository.create(self.testExpense1)
        expense = expense_repository.find_by_id(self.testExpense1.expense_id)

        self.assertEqual(expense.name, self.testExpense1.name)
        self.assertEqual(str(expense.value), self.testExpense1.value)
        self.assertEqual(expense.category, self.testExpense1.category)
        self.assertEqual(expense.date, self.testExpense1.date)
        self.assertEqual(expense.owner, self.testExpense1.owner)

    def test_next_id(self):
        next_id = expense_repository.next_id()
        self.assertEqual(next_id, None)
        
        expense_repository.create(self.testExpense1)
        expense_repository.create(self.testExpense2)
        expense_repository.create(self.testExpense3)
        next_id = expense_repository.next_id()
        self.assertEqual(next_id, 3)


    def test_delete_all(self):
        expense_repository.create(self.testExpense1)
        expense_repository.create(self.testExpense2)

        expenses = expense_repository.find_all()
        self.assertEqual(len(expenses), 2)

        expense_repository.delete_all()
        expenses = expense_repository.find_all()
        self.assertEqual(len(expenses), 0)

