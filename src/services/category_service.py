from tkinter import messagebox
from entities.category import Category

from services.user_service import (
    user_service as default_user_service
)

from repositories.category_repository import (
    category_repository as default_category_repository
)


class CategoryService:
    """Class that is responsible for the application logic related to Category objects
    """

    def __init__(
        self,
        category_repository=default_category_repository,
        user_service=default_user_service

    ):
        """Constructor for the class.
            Creates new class for application logic related to Category objects

        Args:
            category_repository (CategoryRepository, optional):
            Object that has same methods as CategoryRepository.
            Defaults to default_category_repository.
        """
        self._category_repository = category_repository
        self._user_service = user_service
        self._user = None

    def create_category_for_user(self, category):
        """Creates new cateory for the user that is logged in

        Args:
            category (String): name of the category given by the user

        Returns:
            Category: the created category if it doesn't alreay exist
        """
        self._user = self._user_service.get_current_user()
        category_id = self._category_repository.next_id()
        if not category_id:
            category_id = 0

        existing_category = self._category_repository.find_by_name_and_owner(
            category, self._user.username)

        if existing_category:
            messagebox.showinfo('', f'Category {category} already exists')
            return False

        category = self._category_repository.create(
            Category(category_id, category, self._user.username))

        return category

    def find_all_categories_for_user(self):
        return self._category_repository.find_all_by_owner(self._user.username)

    def find_all_categories_for_user_text(self):
        """Responsible for retrieving all categories of specific user

        Returns:
            Category: list of Categories of logged in user
        """
        self._user = self._user_service.get_current_user()
        categories = self._category_repository.find_all_by_owner(
            self._user.username)
        categories_text = ['Other']
        for category in categories:
            categories_text.append(category.name)
        return categories_text

    def get_category_by_name(self, category):
        self._user = self._user_service.get_current_user()
        category = self._category_repository.find_by_name_and_owner(
            category, self._user.username)
        return category

    def remove_category_from_user(self, category_name):
        self._user = self._user_service.get_current_user()
        category = self._category_repository.find_by_name_and_owner(
            category_name, self._user.username)
        return self._category_repository.remove(category)

    def stringify_category(self, category):
        return category.name


category_service = CategoryService()
