from cmath import exp
from nis import cat
from tkinter import ttk, constants, StringVar
from services.expense_service import expense_service


class ExpenseListView:
    def __init__(self, mainView, root, expenses):
        self._mainView = mainView
        self._root = root
        self._expenses = expenses
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_expense_item(self, expense):
        expense_frame = ttk.Frame(master=self._frame)
        expense_label = ttk.Label(
            master=expense_frame, text=expense_service.stringify_expense(expense))
        expense_label.grid(
            row=0, column=0, sticky=constants.EW, padx=5, pady=5)
        remove_expense_button = ttk.Button(
            master=expense_frame,
            text="remove",
            command= lambda: self._mainView._remove_expense_handler(expense[0])
        )
        remove_expense_button.grid(
            row=0,column=1, sticky=constants.EW, padx=5, pady=5)
        
        expense_frame.grid_columnconfigure(0, weight=1)
        expense_frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        for expense in self._expenses:
            self._initialize_expense_item(expense)

class CategoryListView:
    def __init__(self, mainView, root, categories):
        self._mainView = mainView
        self._root = root
        self._categories = categories
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_category_item(self, category):
        category_frame = ttk.Frame(master=self._frame)
        category_label = ttk.Label(
            master=category_frame, text=expense_service.stringify_category(category))
        category_label.grid(
            row=0, column=0, sticky=constants.EW, padx=5, pady=5)
        remove_category_button = ttk.Button(
            master=category_frame,
            text="remove",
            command= lambda: self._mainView._remove_category_handler(category)
        )
        remove_category_button.grid(
            row=0, column=1, sticky=constants.EW, padx=5, pady=5)
        
        category_frame.grid_columnconfigure(0, weight=1)
        category_frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        for category in self._categories:
            self._initialize_category_item(category)


class MainView:
    def __init__(self, root, handle_show_login_view):
        self._root = root
        self._user = expense_service.get_current_user()
        self._frame = None
        self._name_entry = None
        self._value_entry = None
        self._category_entry = None
        self._expense_list_view = None
        self._category_list_view = None
        self._category_list_frame = None
        self._expense_list_frame = None
        self._handle_show_login_view = handle_show_login_view

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_header(self):
        header_label = ttk.Label(
            master=self._frame,
            text='Welcome to the budget application!',
            font=36
        )
        header_label.grid(row=0, column=0, sticky=constants.EW, padx=5, pady=5)

        logout_button = ttk.Button(
            master=self._frame,
            text="Logout",
            command=self._handle_logout
        )
        logout_button.grid(row=0, column=1, padx=5, pady=5, sticky=constants.W)

    def _initialize_expense_list(self):
        if self._expense_list_view:
            self._expense_list_view.destroy()
        expenses = expense_service.find_all_expenses(self._user.username)
        self._expense_list_view = ExpenseListView(
            self,
            self._expense_list_frame,
            expenses
        )
        self._expense_list_view.pack()

    def _initialize_category_list(self):
        if self._category_list_view:
            self._category_list_view.destroy()
        categories = expense_service.find_all_categories_for_user()
        self._category_list_view = CategoryListView(
            self,
            self._category_list_frame,
            categories
        )
        self._category_list_view.pack()

    def _initialize_expense(self):
        expense_label = ttk.Label(
            master=self._frame, text="Add new expense", font=24)
        expense_label.grid(row=2, column=0, columnspan=2,
                           sticky=constants.EW, padx=5, pady=5)

        name_label = ttk.Label(master=self._frame, text="Name:")
        self._name_entry = ttk.Entry(master=self._frame)
        name_label.grid(row=3, column=0, sticky=constants.EW, padx=5, pady=5)
        self._name_entry.grid(
            row=3, column=1, sticky=constants.E, padx=5, pady=5)

        value_label = ttk.Label(master=self._frame, text="Value:")
        self._value_entry = ttk.Entry(master=self._frame)
        value_label.grid(row=4, column=0, sticky=constants.EW, padx=5, pady=5)
        self._value_entry.grid(
            row=4, column=1, sticky=constants.E, padx=5, pady=5)

        category_label = ttk.Label(master=self._frame, text="Category:")
        categories=expense_service.find_all_categories_for_user_text()
        variable = StringVar()

        self._category_dropdown = ttk.OptionMenu(self._frame,
                                                variable,
                                                categories[1],
                                                *categories)
        category_label.grid(
            row=5, column=0, sticky=constants.EW, padx=5, pady=5)
        self._category_dropdown.grid(
            row=5, column=1, sticky=constants.E, padx=5, pady=5)
        
        self._category_entry = variable

        create_expense_button = ttk.Button(
            master=self._frame,
            text="Add!",
            command=self._create_expense_handler
        )
        create_expense_button.grid(
            row= 6, column=1, sticky=constants.EW, padx=5, pady=5)

    def _initialize_category(self):
        new_category_label = ttk.Label(
            master=self._frame, text="Add new category", font=24)
        new_category_label.grid(row=7, column=0, columnspan=2,
                           sticky=constants.EW, padx=5, pady=5)
        self._new_category_entry = ttk.Entry(master=self._frame)
        self._new_category_entry.grid(
            row=7, column=1, sticky=constants.EW, padx=5, pady=5)

        create_new_category_button = ttk.Button(
            master=self._frame,
            text="Create",
            command=self._create_category_handler
        )
        create_new_category_button.grid(
            row=8,column=1, sticky=constants.EW, padx=5, pady=5)


    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._expense_list_frame = ttk.Frame(master=self._frame)
        self._category_list_frame = ttk.Frame(master=self._frame)

        self._initialize_header()
        self._initialize_expense_list()
        self._initialize_expense()
        self._initialize_category_list()
        self._initialize_category()

        self._expense_list_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )
        self._category_list_frame.grid(
            row=10,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )
        self._frame.grid_columnconfigure(0, weight=1, minsize=500)
        self._frame.grid_columnconfigure(1, weight=0)

    def _handle_logout(self):
        expense_service.logout()
        self._handle_show_login_view()

    def _create_expense_handler(self):
        name = self._name_entry.get()
        value = self._value_entry.get()
        category = self._category_entry.get()
        if name and value and category:
            expense_service.create_expense(name, value, category)
            self._initialize_expense_list()
            self._name_entry.delete(0, constants.END)
            self._value_entry.delete(0, constants.END)
            
    def _create_category_handler(self):
        category = self._new_category_entry.get()
        if category:
            expense_service.create_category_for_user(category)
            self._initialize_category_list()
            self._new_category_entry.delete(0, constants.END)

    def _remove_expense_handler(self,expense_id):
        expense_service.remove_expense(expense_id)
        self._initialize_expense_list()

    def _remove_category_handler(self,category):
        expense_service.remove_category_from_user(category)
        self._initialize_category_list()
