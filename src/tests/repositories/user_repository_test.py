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

    def test_find_by_username(self):
        user_repository.create(self.testUser1)

        user = user_repository.find_by_username(self.testUser1.username)
        self.assertEqual(user.username, self.testUser1.username)
