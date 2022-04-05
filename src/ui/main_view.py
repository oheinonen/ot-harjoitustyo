from tkinter import ttk, constants
from services.expense_service import expense_service


class MainView:
    def __init__(self, root, handle_show_login_view):
        self._root = root
        self._frame = None
        self._name_entry = None
        self._value_entry = None
        self._category_entry = None
        self._expense_list = None
        self._handle_show_login_view = handle_show_login_view

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_header_field(self):
        header_label = ttk.Label(
            master=self._frame,
            text='Welcome to the budget application!',
            font=24
        )
        header_label.grid(sticky=constants.EW, padx=5, pady=5)

    def _initialize_expense_list_field(self):
        expenses = expense_service.find_all_expenses()
        for expense in expenses:
            text = str(expense['id']) + " " + expense['name'] + " " + str(expense['value']) + " " + expense['category'] + " " + expense['date']
            expense_label = ttk.Label(master=self._frame, text=text)
            expense_label.grid(sticky=constants.EW, padx=5, pady=5)

    def _initialize_expense_field(self):
        expense_label = ttk.Label(master=self._frame, text="Add new expense")
        expense_label.grid(sticky=constants.EW, padx=5, pady=5)

        name_label = ttk.Label(master=self._frame, text="Name")
        self._name_entry = ttk.Entry(master=self._frame)
        name_label.grid(sticky=constants.EW, padx=5, pady=5)
        self._name_entry.grid(sticky=constants.EW, padx=5, pady=5)

        value_label = ttk.Label(master=self._frame, text="Value")
        self._value_entry = ttk.Entry(master=self._frame)
        value_label.grid(sticky=constants.EW, padx=5, pady=5)
        self._value_entry.grid(sticky=constants.EW, padx=5, pady=5)

        category_label = ttk.Label(master=self._frame, text="Category")
        self._category_entry = ttk.Entry(master=self._frame)
        category_label.grid(sticky=constants.EW, padx=5, pady=5)
        self._category_entry.grid(sticky=constants.EW, padx=5, pady=5)


        create_expense_button = ttk.Button(
            master=self._frame,
            text="Add!",
            command=self._create_expense_handler
        )
        create_expense_button.grid(sticky=constants.EW, padx=5, pady=5)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._initialize_header_field()
        self._initialize_expense_list_field()
        self._initialize_expense_field()

        logout_button = ttk.Button(
            master=self._frame,
            text="Logout",
            command=self._handle_logout
        )
        logout_button.grid(padx=5, pady=5)
        self._frame.grid_columnconfigure(0, weight=1, minsize=500)

    def _handle_logout(self):
        expense_service.logout()
        self._handle_show_login_view()

    def _create_expense_handler(self):
        name = self._name_entry.get()
        value = self._value_entry.get()
        category = self._category_entry.get()
        expense_service.create_expense(name, value,category)
