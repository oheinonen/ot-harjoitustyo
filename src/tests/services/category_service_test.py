import unittest
from entities.category import Category
from entities.user import User

from services.category_service import CategoryService
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
        user = filter(lambda user: user.username == username, self.users)
        return list(user)

    def delete_all(self):
        self.users = []


class FakeCategoryRepository:

    def __init__(self, categories=None):
        self.categories = categories or []

    def create(self, category):
        self.categories.append(category)
        return category

    def remove(self, category_id):
        if category_id in self.categories:
            self.categories.remove(self.find_by_id(category_id))
            return True
        else:
            return False

    def find_by_id(self, category_id):
        category = list(filter(lambda category: category.category_id == category_id,
                               self.categories
                               ))
        return category[0] if len(category) else None

    def find_by_name_and_owner(self, name, owner):
        categories = list(filter(lambda category:
                                 category.owner == owner and category.name == name,
                                 self.categories
                                 ))
        return categories

    def find_all_by_owner(self, owner):
        categories = list(
            filter(lambda category: category.owner == owner, self.categories))
        return categories

    def find_all(self):
        return self.categories

    def next_id(self):
        return len(self.categories)

    def delete_all(self):
        self.categories = []


class TestCategoryService(unittest.TestCase):
    def setUp(self):
        self.user_service = UserService(FakeUserRepository())
        self.category_service = CategoryService(
            FakeCategoryRepository(), self.user_service)

        self.testUser1 = User('Matti', '12345')
        self.testUser2 = User('Minna', '54321')
        self.testCategory1 = Category(0, 'Living', 'Matti')
        self.testCategory2 = Category(1, 'Food', 'Minna')
        self.testCategory3 = Category(2, 'Food', 'Matti')

    def login(self, user):
        self.user_service.create_user(user.username, user.password)

    def test_create_category_for_user(self):
        self.login(self.testUser1)

        category = self.category_service.create_category_for_user(
            self.testCategory1.name
        )
        self.assertEqual(
            len(self.category_service._category_repository.categories), 1)
        self.assertEqual(category.name, self.testCategory1.name)
        self.assertEqual(category.owner, self.testCategory1.owner)

        category = self.category_service.create_category_for_user(
            self.testCategory1.name
        )
        self.assertEqual(
            len(self.category_service._category_repository.categories), 1)

    def test_find_all_categories_for_user(self):
        self.login(self.testUser1)

        category = self.category_service.create_category_for_user(
            self.testCategory1.name
        )

        category = self.category_service.find_all_categories_for_user()[0]

        self.assertEqual(
            len(self.category_service._category_repository.categories), 1)
        self.assertEqual(category.name, self.testCategory1.name)
        self.assertEqual(category.owner, self.testCategory1.owner)

    def test_find_all_categories_for_user_text(self):
        self.login(self.testUser1)

        self.category_service.create_category_for_user(
            self.testCategory1.name
        )

        category_1 = self.category_service.find_all_categories_for_user_text()[
            1]

        self.assertEqual(category_1, self.testCategory1.name)

    def test_get_category_by_name(self):
        self.login(self.testUser1)

        self.category_service.create_category_for_user(
            self.testCategory1.name
        )
        category = self.category_service.get_category_by_name(
            self.testCategory1.name)[0]
        self.assertEqual(category.name, self.testCategory1.name)
        self.assertEqual(category.owner, self.testCategory1.owner)

    def test_remove_category_from_user(self):
        self.login(self.testUser1)

        category = self.category_service.create_category_for_user(
            self.testCategory1.name
        )
        self.category_service.remove_category_from_user(category.name)
        self.assertEqual(
            len(self.category_service._category_repository.categories), 1)
