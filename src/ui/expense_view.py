from tkinter import ttk, constants, StringVar
from services.expense_service import expense_service
from services.user_service import user_service
from services.category_service import category_service


class ExpenseView:
    def __init__(self, root, handle_show_main_view, expense):
        self._root = root
        self._user = user_service.get_current_user()
        self._frame = None
        self._name_entry = None
        self._value_entry = None
        self._category_entry = None
        self._handle_show_main_view = handle_show_main_view
        self._expense = expense

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_header(self):
        header_label = ttk.Label(
            master=self._frame,
            text='Update expense',
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

    def _initialize_expense(self):
        expense_label = ttk.Label(
            master=self._frame, text="Update expense", font=24)
        expense_label.grid(row=2, column=0, columnspan=2,
                           sticky=constants.EW, padx=5, pady=5)

        name_label = ttk.Label(master=self._frame, text="Name:")
        self._name_entry = ttk.Entry(master=self._frame)
        self._name_entry.insert(0, self._expense.name)
        name_label.grid(row=3, column=0, sticky=constants.EW, padx=5, pady=5)
        self._name_entry.grid(
            row=3, column=1, sticky=constants.E, padx=5, pady=5)

        value_label = ttk.Label(master=self._frame, text="Value:")
        self._value_entry = ttk.Entry(master=self._frame)
        self._value_entry.insert(0, self._expense.value)
        value_label.grid(row=4, column=0, sticky=constants.EW, padx=5, pady=5)
        self._value_entry.grid(
            row=4, column=1, sticky=constants.E, padx=5, pady=5)

        category_label = ttk.Label(master=self._frame, text="Category:")
        categories = category_service.find_all_categories_for_user_text()
        variable = StringVar()

        self._category_dropdown = ttk.OptionMenu(self._frame,
                                                 variable,
                                                 self._expense.category,
                                                 *categories)
        category_label.grid(
            row=5, column=0, sticky=constants.EW, padx=5, pady=5)
        self._category_dropdown.grid(
            row=5, column=1, sticky=constants.E, padx=5, pady=5)

        self._category_entry = variable

        create_expense_button = ttk.Button(
            master=self._frame,
            text="Update!",
            command=self._update_expense_handler
        )
        create_expense_button.grid(
            row=6, column=1, sticky=constants.EW, padx=5, pady=5)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._initialize_header()
        self._initialize_expense()

    def _update_expense_handler(self):
        name = self._name_entry.get()
        value = self._value_entry.get()
        category = self._category_entry.get()
        if name and value and category:
            expense_service.update_expense(
                self._expense,
                name,
                value,
                category
            )
            self._handle_show_main_view()
