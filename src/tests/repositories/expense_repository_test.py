import unittest
from repositories.expense_repository import expense_repository
from entities.expense import Expense


class TestExpenseRepository(unittest.TestCase):
    def setUp(self):
        expense_repository.delete_all()
        self.testExpense1 = Expense('TV', '200')
        self.testExpense2 = Expense('Rent', '400')

    def test_create(self):
        expense_repository.create(self.testExpense1)
        expense = expense_repository.find_by_name(self.testExpense1.name)
        expenses = expense_repository.find_all()
        self.assertEqual(expense.name, self.testExpense1.name)

    def test_find_by_name(self):
        expense_repository.create(self.testExpense1)
        expense = expense_repository.find_by_name(self.testExpense1.name)
        self.assertEqual(expense.name, self.testExpense1.name)

    def test_find_all(self):
        expense_repository.create(self.testExpense1)
        expense_repository.create(self.testExpense2)
        expenses = expense_repository.find_all()

        self.assertEqual(len(expenses), 2)
        self.assertEqual(expenses[0]['name'], self.testExpense1.name)
        self.assertEqual(expenses[1]['name'], self.testExpense2.name)

    def test_delete_all(self):
        expense_repository.create(self.testExpense1)
        expense_repository.create(self.testExpense2)
        expense_repository.delete_all()
        expenses = expense_repository.find_all()
        self.assertEqual(len(expenses), 0)
