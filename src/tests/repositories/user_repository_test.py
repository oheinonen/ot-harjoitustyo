import unittest
from repositories.user_repository import user_repository, get_user_by_row
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.testUser1 = User('Matti', '12345')
        self.testUser2 = User('Minna', '54321')

    def test_create(self):
        user_repository.create(self.testUser1)
        user = user_repository.find_by_username(self.testUser1.username)
        self.assertEqual(user.username, self.testUser1.username)
        self.assertEqual(user.password, self.testUser1.password)

    def test_find_all(self):
        user_repository.create(self.testUser1)
        user_repository.create(self.testUser2)
        users = user_repository.find_all()

        self.assertEqual(len(users), 2)

        self.assertEqual(users[0].username, self.testUser1.username)
        self.assertEqual(users[0].password, self.testUser1.password)
        self.assertEqual(users[1].username, self.testUser2.username)
        self.assertEqual(users[1].password, self.testUser2.password)

    def test_find_by_username(self):
        user_repository.create(self.testUser1)
        user = user_repository.find_by_username(self.testUser1.username)
        self.assertEqual(user.username, self.testUser1.username)
        self.assertEqual(user.password, self.testUser1.password)

    def test_delete_all(self):
        user_repository.create(self.testUser1)
        user_repository.create(self.testUser2)

        expenses = user_repository.find_all()
        self.assertEqual(len(expenses), 2)

        user_repository.delete_all()
        expenses = user_repository.find_all()
        self.assertEqual(len(expenses), 0)
