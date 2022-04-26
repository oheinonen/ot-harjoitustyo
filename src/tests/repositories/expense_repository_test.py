import unittest
from repositories.expense_repository import expense_repository
from entities.expense import Expense


class TestExpenseRepository(unittest.TestCase):
    def setUp(self):
        expense_repository.delete_all()
        self.testExpense1 = Expense(
            0, 'TV', '200', 'Living', '01/04/2022', 'Matti')
        self.testExpense2 = Expense(
            1, 'Hamburger', '10', 'Food', '05/04/2022', 'Minna')

    def test_create(self):
        expense_repository.create(self.testExpense1)
        expense = expense_repository.find_by_id(self.testExpense1.expense_id)
        self.assertEqual(expense.name, self.testExpense1.name)
        self.assertEqual(str(expense.value), self.testExpense1.value)
        self.assertEqual(expense.category, self.testExpense1.category)

    def test_find_all(self):
        expense_repository.create(self.testExpense1)
        expense_repository.create(self.testExpense2)
        expenses = expense_repository.find_all(self.testExpense1.owner)

        self.assertEqual(len(expenses), 1)
        self.assertEqual(expenses[0]['name'], self.testExpense1.name)

    def test_delete_all(self):
        expense_repository.create(self.testExpense1)
        expense_repository.create(self.testExpense2)
        expense_repository.delete_all()
        expenses = expense_repository.find_all(self.testExpense1.owner)
        self.assertEqual(len(expenses), 0)
