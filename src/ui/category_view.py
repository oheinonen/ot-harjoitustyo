from tkinter import ttk, constants, StringVar
from services.expense_service import expense_service
from services.user_service import user_service
from services.category_service import category_service
from ui.main_view import ExpenseListView


class CategoryView:
    def __init__(self, root, handle_show_main_view, handle_show_expense_view, category):
        self._root = root
        self._user = user_service.get_current_user()
        self._frame = None
        self._expense_list_view = None
        self._expense_list_frame = None
        self._handle_show_main_view = handle_show_main_view
        self._handle_show_expense_view = handle_show_expense_view
        self._category = category_service.get_category_by_name(category)

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_header(self):
        header_label = ttk.Label(
            master=self._frame,
            text='Expenses in ' + self._category.name + ' category',
            font=36
        )
        header_label.grid(row=0, column=0, sticky=constants.EW, padx=5, pady=5)

        go_back_button = ttk.Button(
            master=self._frame,
            text="Back to front page",
            command=self._handle_show_main_view
        )
        go_back_button.grid(row=0, column=1, padx=5,
                            pady=5, sticky=constants.W)

    def _initialize_expense_list(self):
        if self._expense_list_view:
            self._expense_list_view.destroy()
        expenses = expense_service.get_expenses_by_category(self._category.name)
        self._expense_list_view = ExpenseListView(
            self,
            self._expense_list_frame,
            expenses
        )
        self._expense_list_view.pack()


    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._expense_list_frame = ttk.Frame(master=self._frame)
        self._initialize_header()
        self._initialize_expense_list()
        self._expense_list_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=constants.NW
        )


    def _update_expense_handler(self, expense_id):
        """Response for action after user clicks 'Update' button 

        Args:
            expense_id: Id of the Expense to be updated
        """
        expense = expense_service.get_expense_by_id(expense_id)
        self._handle_show_expense_view(expense)


    def _remove_expense_handler(self, expense_id):
        """Response for action after user clicks 'remove' button next to one of the expenses 
            and updating the view

        Args:
            expense_id: Id of the Expense to be deleted
        """
        expense_service.remove_expense(expense_id)
        self._initialize_expense_list()
