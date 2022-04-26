import datetime

from entities.expense import Expense
from services.user_service import user_service

from repositories.expense_repository import (
    expense_repository as default_expense_repository
)


class ExpenseService:
    def __init__(
        self,
        expense_repository=default_expense_repository
    ):
        self._expense_repository = expense_repository

    def create_expense(self, name, value, category):
        date = datetime.datetime.now().strftime("%d/%m/%Y")
        expense_id = self._expense_repository.next_id()
        if not expense_id:
            expense_id = 0

        expense = self._expense_repository.create(
            Expense(expense_id, name, value, category, date, user_service._user.username))
        return expense

    def update_expense(self, expense, name, value, category):
        expense = self._expense_repository.update(
            expense, name, value, category)
        return expense

    def remove_expense(self, expense_id):
        return self._expense_repository.remove(expense_id)

    def stringify_expense(self, expense):
        return str(
            expense['expense_id']) + " " + expense['name'] + " " + \
            str(expense['value']) + " " + expense['category']\
            + " " + expense['date']

    def find_all_expenses(self, owner):
        return self._expense_repository.find_all(owner)


expense_service = ExpenseService()
