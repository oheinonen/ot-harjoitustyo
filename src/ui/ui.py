import imp
from ui.login_view import LoginView
from ui.create_user_view import CreateUserView
from ui.main_view import MainView
from ui.expense_view import ExpenseView


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None
        self._user = None

    def start(self):
        self._show_login_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(
            self._root,
            self._show_main_view,
            self._show_create_user_view
        )

        self._current_view.pack()

    def _show_main_view(self):
        self._hide_current_view()

        self._current_view = MainView(
            self._root,
            self._show_login_view,
            self._show_expense_view
        )

        self._current_view.pack()

    def _show_create_user_view(self):
        self._hide_current_view()

        self._current_view = CreateUserView(
            self._root,
            self._show_main_view,
            self._show_login_view
        )

        self._current_view.pack()

    def _show_expense_view(self, expense):
        self._hide_current_view()

        self._current_view = ExpenseView(
            self._root,
            self._show_main_view,
            expense
        )
        self._current_view.pack()
