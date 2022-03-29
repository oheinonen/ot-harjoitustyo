from entities.user import User
from entities.expense import Expense

from repositories.user_repository import (
    user_repository as default_user_repository
)
from repositories.expense_repository import (
    expense_repository as default_expense_repository
)

class UsernameExistsError(Exception):
    pass

class InvalidCredentialsError(Exception):
    pass


class ExpenseService:
    def __init__(
        self,
        user_repository=default_user_repository,
        expense_repository=default_expense_repository
    ):
        self._user = None
        self._user_repository = user_repository
        self._expense_repository = expense_repository

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
            raise InvalidCredentialsError(f'Username {username} must be between 4 and 99 characters')
        
        self._user = user
        return user
    
    def create_expense(self, name, value):
        expense = self._expense_repository.create(Expense(name,value))
        return expense

    def find_all_expenses(self):
        return self._expense_repository.find_all()

expense_service = ExpenseService()