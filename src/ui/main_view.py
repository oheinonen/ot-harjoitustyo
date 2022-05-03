from tkinter import ttk, constants, StringVar
from services.expense_service import expense_service
from services.category_service import category_service
from services.user_service import user_service


class ExpenseListView:
    """View that is responsible for listing expenses
    """
    def __init__(self, mainView, root, expenses):
        """Constructor for the class. Creates new expense list view

        Args:
            mainView (MainView): Parent view where this expenselist will be included
            root : tkInter element where the view will be included
            expenses (Expense): list of Expense objects that are shown in the view
        """
        self._mainView = mainView
        self._root = root
        self._expenses = expenses
        self._frame = None

        self._initialize()

    def pack(self):
        """Shows the view
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Destroys the view
        """
        self._frame.destroy()

    def _initialize_expense_item(self, expense):
        """Initializes view for single Expense object

        Args:
            expense (Expense): the Expense object to be shown
        """
        expense_frame = ttk.Frame(master=self._frame)
        expense_label = ttk.Label(
            master=expense_frame, text=expense_service.stringify_expense(expense))
        expense_label.grid(
            row=0, column=0, sticky=constants.EW, padx=5, pady=5)

        update_expense_button = ttk.Button(
            master=expense_frame,
            text="update",
            command=lambda: self._mainView._handle_show_expense_view(expense)
        )
        update_expense_button.grid(
            row=0, column=1, sticky=constants.EW, padx=5, pady=5)

        remove_expense_button = ttk.Button(
            master=expense_frame,
            text="remove",
            command=lambda: self._mainView._remove_expense_handler(expense[0])
        )
        remove_expense_button.grid(
            row=0, column=2, sticky=constants.EW, padx=5, pady=5)

        expense_frame.grid_columnconfigure(0, weight=1)
        expense_frame.pack(fill=constants.X)

    def _initialize(self):
        """Initializes the frame for expense list
        """
        self._frame = ttk.Frame(master=self._root)
        for expense in self._expenses:
            self._initialize_expense_item(expense)


class CategoryListView:
    """View that is responsible for listing categories
    """
    def __init__(self, mainView, root, categories):
        """Constructor for the class. Creates new category list view

        Args:
            mainView (MainView): Parent view where this expenselist will be included
            root : tkInter element where the view will be included
            categories (Category): list of Category objects that are shown in the view
        """

        self._mainView = mainView
        self._root = root
        self._categories = categories
        self._frame = None

        self._initialize()

    def pack(self):
        """Shows the view
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Destroys the view
        """
        self._frame.destroy()

    def _initialize_category_item(self, category):
        """Initializes single Category object

        Args:
            category (Category): Category object to be shown
        """
        category_frame = ttk.Frame(master=self._frame)
        category_label = ttk.Label(
            master=category_frame, text=category_service.stringify_category(category))
        category_label.grid(
            row=0, column=0, sticky=constants.EW, padx=5, pady=5)
        remove_category_button = ttk.Button(
            master=category_frame,
            text="remove",
            command=lambda: self._mainView._remove_category_handler(category)
        )
        remove_category_button.grid(
            row=0, column=1, sticky=constants.EW, padx=5, pady=5)

        category_frame.grid_columnconfigure(0, weight=1)
        category_frame.pack(fill=constants.X)

    def _initialize(self):
        """Initializes frame for the category list
        """
        self._frame = ttk.Frame(master=self._root)
        for category in self._categories:
            self._initialize_category_item(category)


class MainView:
    """View responsible for showing existing expenses and categories and creating new ones
    """
    def __init__(self, root, handle_logout, handle_show_expense_view):
        """Constructor for the class. Creates new main view

        Args:
            root : tkInter element where the ui will be outlined
            handle_logout: Value that is called when user logs out
            handle_show_expense_view: Value that is called when user wants to see expense view of one Expense
        """
        self._root = root
        self._user = user_service.get_current_user()
        self._frame = None
        self._name_entry = None
        self._value_entry = None
        self._category_entry = None
        self._expense_list_view = None
        self._category_list_view = None
        self._category_list_frame = None
        self._expense_list_frame = None
        self._handle_logout = handle_logout
        self._handle_show_expense_view = handle_show_expense_view

        self._initialize()

    def pack(self):
        """Shows the view
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Destroys the view
        """
        self._frame.destroy()

    def _initialize_header(self):
        """Creates the top of the view
        """
        header_label = ttk.Label(
            master=self._frame,
            text='Welcome to the budget application!',
            font=36
        )
        header_label.grid(row=0, column=0, sticky=constants.EW, padx=5, pady=5)

        logout_button = ttk.Button(
            master=self._frame,
            text="Logout",
            command=self.logout_handler
        )
        logout_button.grid(row=0, column=1, padx=5, pady=5, sticky=constants.W)

    def _initialize_expense_list(self):
        """Creates the expense list view
        """
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
        """Creates the category list view
        """

        if self._category_list_view:
            self._category_list_view.destroy()
        categories = category_service.find_all_categories_for_user()
        self._category_list_view = CategoryListView(
            self,
            self._category_list_frame,
            categories
        )
        self._category_list_view.pack()

    def _initialize_expense_label(self):
        expense_label = ttk.Label(
            master=self._frame, text="Add new expense", font=24)
        expense_label.grid(row=2, column=0, columnspan=2,
                           sticky=constants.EW, padx=5, pady=5)

    def _initialize_expense_name_field(self):
        name_label = ttk.Label(master=self._frame, text="Name:")
        self._name_entry = ttk.Entry(master=self._frame)
        name_label.grid(row=3, column=0, sticky=constants.EW, padx=5, pady=5)
        self._name_entry.grid(
            row=3, column=1, sticky=constants.E, padx=5, pady=5)

    def _initialize_expense_value_field(self):
        value_label = ttk.Label(master=self._frame, text="Value:")
        self._value_entry = ttk.Entry(master=self._frame)
        value_label.grid(row=4, column=0, sticky=constants.EW, padx=5, pady=5)
        self._value_entry.grid(
            row=4, column=1, sticky=constants.E, padx=5, pady=5)

    def _initialize_expense_category_field(self):
        category_label = ttk.Label(master=self._frame, text="Category:")
        categories = category_service.find_all_categories_for_user_text()
        variable = StringVar()

        # Only existing categories are shown in dropdown menu
        self._category_dropdown = ttk.OptionMenu(self._frame,
                                                 variable,
                                                 categories[0],
                                                 *categories)
        category_label.grid(
            row=5, column=0, sticky=constants.EW, padx=5, pady=5)
        self._category_dropdown.grid(
            row=5, column=1, sticky=constants.E, padx=5, pady=5)
        self._category_entry = variable
    
    def _initialize_expense_submit_button(self):
        create_expense_button = ttk.Button(
            master=self._frame,
            text="Add new expense",
            command=self._create_expense_handler
        )
        create_expense_button.grid(
            row=6, column=1, sticky=constants.EW, padx=5, pady=5)

    def _initialize_expense(self):
        """Initializes form where user can create new Expense object
        """
        self._initialize_expense_label()
        self._initialize_expense_name_field()
        self._initialize_expense_value_field()
        self._initialize_expense_category_field()
        self._initialize_expense_submit_button()

    def _initialize_cateory_label(self):
        new_category_label = ttk.Label(
            master=self._frame, text="Add new category", font=24)
        new_category_label.grid(row=7, column=0, columnspan=2,
                                sticky=constants.EW, padx=5, pady=5)

    def _initialize_cateory_name_field(self):
        self._new_category_entry = ttk.Entry(master=self._frame)
        self._new_category_entry.grid(
            row=7, column=1, sticky=constants.EW, padx=5, pady=5)

    def _initialize_cateory_submit_button(self):
        create_new_category_button = ttk.Button(
            master=self._frame,
            text="Create",
            command=self._create_category_handler
        )
        create_new_category_button.grid(
            row=8, column=1, sticky=constants.EW, padx=5, pady=5)


    def _initialize_category(self):
        """Initializes form where user can add new category
        """
        self._initialize_cateory_label()
        self._initialize_cateory_name_field()
        self._initialize_cateory_submit_button()
        

    def _initialize(self):
        """Creates the frame where the view is build with the help of other functions
        """
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

    def logout_handler(self):
        """Responsible for action after user clicks 'Log out' button: 
            logs out the user and changes view to the login view
        """
        user_service.logout()
        self._handle_logout()

    def _create_expense_handler(self):
        """Responsible for action after user clicks 'Add new expense' button: 
            calls create_expense function and clears the entries if new expense is created
        """
        name = self._name_entry.get()
        value = self._value_entry.get()
        category = self._category_entry.get()
        if name and value and category:
            if expense_service.create_expense(name, value, category):
                self._initialize_expense_list()
                self._name_entry.delete(0, constants.END)
                self._value_entry.delete(0, constants.END)

    def _create_category_handler(self):
        """Responsible for action after user clicks 'Add new category' button: 
            calls create_category_for_user function and clears the entries if new expense is created
        """

        category = self._new_category_entry.get()
        if category:
            category_service.create_category_for_user(category)
            self._initialize_category_list()
            self._initialize_expense()
            self._new_category_entry.delete(0, constants.END)

    def _remove_expense_handler(self, expense_id):
        """Response for action after user clicks 'remove' button next to one of the expenses 
            and updating the view

        Args:
            expense_id: Id of the Expense to be deleted
        """
        expense_service.remove_expense(expense_id)
        self._initialize_expense_list()

    def _remove_category_handler(self, category):
        """Response for action after user clicks 'remove' button next to one of the categories
            and updating the view

        Args:
            category: Category to be deleted
        """

        category_service.remove_category_from_user(category)
        self._initialize_category_list()
        self._initialize_expense()
