import unittest
from repositories.category_repository import category_repository
from entities.category import Category
import datetime


class TestCategoryRepository(unittest.TestCase):
    def setUp(self):
        category_repository.delete_all()
        self.testCategory1 = Category(0, 'Living', 'Matti')
        self.testCategory2 = Category(1, 'Food', 'Minna')
        self.testCategory3 = Category(2, 'School', 'Matti')

    def test_create(self):
        category_repository.create(self.testCategory1)
        categories = category_repository.find_all()

        self.assertEqual(len(categories), 1)
        self.assertEqual(categories[0].name, self.testCategory1.name)
        self.assertEqual(categories[0].owner, self.testCategory1.owner)

    def test_find_all(self):
        category_repository.create(self.testCategory1)
        category_repository.create(self.testCategory2)
        categories = category_repository.find_all()

        self.assertEqual(len(categories), 2)

    def test_find_all_by_owner(self):
        category_repository.create(self.testCategory1)
        category_repository.create(self.testCategory2)
        categories = category_repository.find_all_by_owner(self.testCategory1.owner)

        self.assertEqual(len(categories), 1)
        self.assertEqual(categories[0].name, self.testCategory1.name)
        self.assertEqual(categories[0].owner, self.testCategory1.owner)

    def test_find_by_name_and_owner(self):
        category_repository.create(self.testCategory1)
        category_repository.create(self.testCategory2)
        category = category_repository.find_by_name_and_owner(self.testCategory1.name, self.testCategory1.owner)

        self.assertEqual(category.name, self.testCategory1.name)
        self.assertEqual(category.owner, self.testCategory1.owner)
    
    def test_find_by_id(self):
        category_repository.create(self.testCategory1)
        category = category_repository.find_by_id(self.testCategory1.category_id)

        self.assertEqual(category.name, self.testCategory1.name)
        self.assertEqual(category.owner, self.testCategory1.owner)

    def test_remove(self):
        category_repository.create(self.testCategory1)
        categories = category_repository.find_all()

        self.assertEqual(len(categories), 1)

        category_repository.remove(self.testCategory1)
        categories = category_repository.find_all()

        self.assertEqual(len(categories), 0)

    def test_next_id(self):
        next_id = category_repository.next_id()
        self.assertEqual(next_id, None)
        
        category_repository.create(self.testCategory1)
        category_repository.create(self.testCategory2)
        category_repository.create(self.testCategory3)
        next_id = category_repository.next_id()
        self.assertEqual(next_id, 3)


    def test_delete_all(self):
        category_repository.create(self.testCategory1)
        category_repository.create(self.testCategory2)

        categories = category_repository.find_all()
        self.assertEqual(len(categories), 2)

        category_repository.delete_all()
        categories = category_repository.find_all()
        self.assertEqual(len(categories), 0)

