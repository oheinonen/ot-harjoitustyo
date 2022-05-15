import datetime

from entities.expense import Expense

from services.user_service import (
    user_service as default_user_service
)

from repositories.expense_repository import (
    expense_repository as default_expense_repository
)


class ExpenseService:
    """Class that is responsible for the application logic related to Expense objects
    """

    def __init__(
        self,
        expense_repository=default_expense_repository,
        user_service=default_user_service
    ):
        """Constructor for the class.
        Creates new class for application logic related to Expense objects

        Args:
            expense_repository (ExpenseRepository, optional):
            Object that has same methods as ExpenseRepository.
            Defaults to default_expense_repository.
        """
        self._expense_repository = expense_repository
        self._user_service = user_service
        self._user = None

    def create_expense(self, name, value, category):
        """Creates new expense

        Args:
            name (String): name of the expense given by the user
            value (String): value of the expense given by the user
            category (Category): Category Object given by the user

        Returns:
            Expense: The expense created
        """
        date = datetime.datetime.now().strftime("%d/%m/%Y")
        expense_id = self._expense_repository.next_id()
        if not expense_id:
            expense_id = 0
        user = self._user_service.get_current_user()
        expense = self._expense_repository.create(
            Expense(expense_id, name, value, category, date, user.username))
        return expense

    def update_expense(self, expense, name, value, category):
        """Updates information of specific expense

        Args:
            expense (Expense): Expense object that will be updated
            name (String): new name of the expense given by the user
            value (String): new value of the expense given by the user
            category (Category): new Category Object given by the user

        Returns:
            Expense: the updated Expense
        """
        expense = self._expense_repository.update(
            expense, name, value, category)
        return expense

    def get_expense_by_id(self, expense_id):
        expense = self._expense_repository.find_by_id(expense_id)
        return expense

    def get_expenses_by_category(self, category):
        """Finds all expenses of logged in user that belong to given category

        Args:
            category (String): name of the category 

        Returns:
            Expenses: list of Expense objects that belong to given category by logged in user
        """
        self._user = self._user_service.get_current_user()

        expenses = self._expense_repository.find_all_by_category_and_owner(
            category, self._user.username)
        return expenses

    def remove_expense(self, expense_id):
        return self._expense_repository.remove(expense_id)

    def stringify_expense(self, expense):
        """Makes specific Expense object into more readable format

        Args:
            expense (Expense): the expense that is wanted to be formatted

        Returns:
            String: Expense in readable format
        """
        return '#' + str(
            expense.expense_id) + " " + expense.name + " " + \
            str(expense.value) + " " + expense.category\
            + " " + expense.date

    def find_all_expenses(self, owner):
        return self._expense_repository.find_all_by_owner(owner)


expense_service = ExpenseService()
