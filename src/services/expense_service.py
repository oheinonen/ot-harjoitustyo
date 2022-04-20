from entities.user import User

from repositories.user_repository import (
    user_repository as default_user_repository
)
from repositories.expense_repository import (
    expense_repository as default_expense_repository
)
from repositories.category_repository import (
    category_repository as default_category_repository
)


class UsernameExistsError(Exception):
    pass

class CategoryExistsError(Exception):
    pass


class InvalidCredentialsError(Exception):
    pass


class ExpenseService:
    def __init__(
        self,
        user_repository=default_user_repository,
        expense_repository=default_expense_repository,
        category_repository=default_category_repository

    ):
        self._user = None
        self._user_repository = user_repository
        self._expense_repository = expense_repository
        self._category_repository = category_repository

    def login(self, username, password):
        user = self._user_repository.find_by_username(username)
        if not user or user.password != password:
            raise InvalidCredentialsError('Invalid username or password')

        self._user = user

        return user

    def logout(self):
        self._user = None

    def create_user(self, username, password):

        existing_user = self._user_repository.find_by_username(username)

        if existing_user:
            raise UsernameExistsError(f'Username {username} already exists')

        user = self._user_repository.create(User(username, password))

        if 4 > len(user.username) or len(user.username) >= 99:
            raise InvalidCredentialsError(
                f'Username {username} must be between 4 and 99 characters')
        self._user = user
        return user
    
    def get_current_user(self):
        return self._user

    
    def create_category_for_user(self, category):

        existing_category = self._category_repository.find_by_name(category)

        if existing_category:
            raise CategoryExistsError(f'Category {category} already exists')

        category = self._category_repository.create(category, self._user.username)

        return category
    
    def find_all_categories_for_user(self):
        return self._category_repository.find_all(self._user.username)
    
    def find_all_categories_for_user_text(self):
        categories = self._category_repository.find_all(self._user.username)
        categories_text = []
        for category in categories:
            categories_text.append(category['name'])
        return categories_text


    def remove_category_from_user(self, category):
        return self._category_repository.remove(category)

    def stringify_category(self, category):
        return category['name']


    def create_expense(self, name, value, category):
        expense = self._expense_repository.create(
            name, value, category, self._user.username)
        return expense

    def remove_expense(self,expense_id):
        return self._expense_repository.remove(expense_id)

    def stringify_expense(self, expense):
        return str(
            expense['id']) + " " + expense['name'] + " " + \
            str(expense['value']) + " " + expense['category']\
             + " " + expense['date']

    def find_all_expenses(self, owner):
        return self._expense_repository.find_all(owner)


expense_service = ExpenseService()