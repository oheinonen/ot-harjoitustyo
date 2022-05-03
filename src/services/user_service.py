from tkinter import messagebox
from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserService:
    """Class that is responsible for the application logic related to User objects
    """

    def __init__(
        self,
        user_repository=default_user_repository
    ):
        """Constructor for the class.
            Creates new class for application logic related to User objects

        Args:
            user_repository (UserRepository, optional):
            Object that has same methods as UserRepository.
            Defaults to default_user_repository.
        """
        self._user = None
        self._user_repository = user_repository

    def login(self, username, password):
        """Logs in the user

        Args:
            username (String): Username give by the user
            password (String): Password give by the user

        Returns:
            User: User object of the logged in user if the login succeedes
        """
        user = self._user_repository.find_by_username(username)
        if not user or user.password != password:
            messagebox.showinfo('', 'Invalid username or password')
            return False
        self._user = user
        return user

    def logout(self):
        """Logs out the user
        """
        self._user = None

    def create_user(self, username, password):
        """Creates new user and and logs that user in

        Args:
            username (String): Username give by the user
            password (String): Password give by the user

        Returns:
            User: User object of the logged in user if the user creation succeedes
        """
        existing_user = self._user_repository.find_by_username(username)

        if existing_user:
            messagebox.showinfo('', f'Username {username} already exists')
            return False

        if 4 > len(username) or len(username) >= 99:
            messagebox.showinfo(
                '', f'Username {username} must be between 4 and 99 characters')
            return False

        user = self._user_repository.create(User(username, password))
        self._user = user
        return user

    def get_current_user(self):
        return self._user

    def delete_all(self):
        return self._user_repository.delete_all()


user_service = UserService()
