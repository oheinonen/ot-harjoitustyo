from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UsernameExistsError(Exception):
    pass


class InvalidCredentialsError(Exception):
    pass


class UserService:
    def __init__(
        self,
        user_repository=default_user_repository

    ):
        self._user = None
        self._user_repository = user_repository

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

    def delete_all(self):
        return self._user_repository.delete_all()


user_service = UserService()
