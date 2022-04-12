import unittest
from repositories.expense_repository import expense_repository
from entities.expense import Expense


class TestExpenseRepository(unittest.TestCase):
    def setUp(self):
        expense_repository.delete_all()
        self.testExpense1 = Expense(
            0, 'TV', '200', 'Living', '2022-04-01', 'Matti')
        self.testExpense2 = Expense(
            1, 'Hamburger', '10', 'Food', '2022-04-05', 'Minna')
        

    def test_create(self):
        expense_repository.create(self.testExpense1.name, 
                                    self.testExpense1.value, 
                                    self.testExpense1.category, 
                                    self.testExpense1.owner)
        expense = expense_repository.find_all(self.testExpense1.owner)[0]
        self.assertEqual(expense['name'], self.testExpense1.name)
        self.assertEqual(str(expense['value']), self.testExpense1.value)
        self.assertEqual(expense['category'], self.testExpense1.category)

    def test_find_all(self):
        expense_repository.create(self.testExpense1.name, 
                                    self.testExpense1.value, 
                                    self.testExpense1.category, 
                                    self.testExpense1.owner)
        expense_repository.create(self.testExpense2.name, 
                                    self.testExpense2.value, 
                                    self.testExpense2.category, 
                                    self.testExpense2.owner)
        expenses = expense_repository.find_all(self.testExpense1.owner)

        self.assertEqual(len(expenses), 1)
        self.assertEqual(expenses[0]['name'], self.testExpense1.name)

    def test_delete_all(self):
        expense_repository.create(self.testExpense1.name, 
                                    self.testExpense1.value, 
                                    self.testExpense1.category, 
                                    self.testExpense1.owner)
        expense_repository.create(self.testExpense2.name, 
                                    self.testExpense2.value, 
                                    self.testExpense2.category, 
                                    self.testExpense2.owner)
        expense_repository.delete_all()
        expenses = expense_repository.find_all(self.testExpense1.owner)
        self.assertEqual(len(expenses), 0)
