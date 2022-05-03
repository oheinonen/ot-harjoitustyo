from entities.category import Category
from services.user_service import user_service

from repositories.category_repository import (
    category_repository as default_category_repository
)


class CategoryExistsError(Exception):
    pass


class CategoryService:
    def __init__(
        self,
        category_repository=default_category_repository

    ):
        self._category_repository = category_repository
        self._user = None

    def create_category_for_user(self, category):

        category_id = self._category_repository.next_id()
        if not category_id:
            category_id = 0

        existing_category = self._category_repository.find_by_name_and_owner(
            category, self._user.username)

        if existing_category:
            raise CategoryExistsError(f'Category {category} already exists')

        category = self._category_repository.create(
            Category(category_id, category, self._user.username))

        return category

    def find_all_categories_for_user(self):
        return self._category_repository.find_all(self._user.username)

    def find_all_categories_for_user_text(self):
        self._user = user_service.get_current_user()
        categories = self._category_repository.find_all(
            self._user.username)
        categories_text = ['Other']
        for category in categories:
            categories_text.append(category['name'])
        return categories_text

    def remove_category_from_user(self, category):
        return self._category_repository.remove(category)

    def stringify_category(self, category):
        return category['name']


category_service = CategoryService()
