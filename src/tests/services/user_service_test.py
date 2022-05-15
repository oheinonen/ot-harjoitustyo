from datetime import datetime
import unittest
import datetime
from entities.expense import Expense
from entities.user import User

from services.expense_service import ExpenseService
from services.user_service import UserService


class FakeUserRepository:

    def __init__(self, users=None):
        self.users = users or []

    def create(self, user):
        self.users.append(user)
        return user

    def find_all(self):
        return self.users

    def find_by_username(self, username):
        user = list(filter(lambda user: user.username == username, self.users))
        return list(user)[0] if len(list(user)) else None

    def delete_all(self):
        self.users = []


class TestUserService(unittest.TestCase):
    def setUp(self):
        self.user_service = UserService(FakeUserRepository())

        self.testUser1 = User('Matti', '12345')
        self.testUser2 = User('Mi', '54321')

    def test_create_user(self):
        self.user_service.create_user(
            self.testUser1.username, self.testUser1.password)

        self.assertEqual(len(self.user_service._user_repository.users), 1)

        self.user_service.create_user(
            self.testUser2.username, self.testUser2.password)

        self.assertEqual(len(self.user_service._user_repository.users), 1)

        self.user_service.create_user(
            self.testUser1.username, self.testUser1.password)

        self.assertEqual(len(self.user_service._user_repository.users), 1)

    def test_logout(self):
        self.user_service.create_user(
            self.testUser1.username, self.testUser1.password)
        self.user_service.logout()
        self.assertEqual(self.user_service._user, None)

    def test_login(self):
        self.user_service.create_user(
            self.testUser1.username, self.testUser1.password)
        self.user_service.logout()
        self.user_service.login(self.testUser1.username,
                                self.testUser1.password)

        self.assertEqual(self.user_service._user.username,
                         self.testUser1.username)
        self.assertEqual(self.user_service._user.password,
                         self.testUser1.password)

        self.user_service.logout()

        self.user_service.login(self.testUser2.username,
                                self.testUser2.password)

        self.assertEqual(self.user_service._user, None)

    def test_delete_all(self):
        self.user_service.create_user(
            self.testUser1.username, self.testUser1.password)
        self.user_service.delete_all()
        self.assertEqual(len(self.user_service._user_repository.users), 0)
