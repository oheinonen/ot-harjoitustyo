from re import M
from tkinter import ANCHOR, ttk, constants, StringVar, Listbox

from services.expense_service import expense_service
from services.category_service import category_service
from services.user_service import user_service
from itertools import takewhile


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
        self._listBox = None

        self._initialize()

    def pack(self):
        """Shows the view
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Destroys the view
        """
        self._frame.destroy()
    
    def _initialize_expense_list_header(self):
        header_frame = ttk.Frame(master=self._frame)
        header_label = ttk.Label(master=header_frame,
            text="Your expenses", font=24)
        header_label.grid(
            row=0,
            column=0,
            sticky=constants.NW,
            padx=5,
            pady=5
            )
        header_frame.pack()


    def _initialize_expense_item(self, expense):
        """Initializes view for single Expense object

        Args:
            expense (Expense): the Expense object to be shown
        """
        self._listBox.insert(0,expense_service.stringify_expense(expense))
    
    def _initialize_buttons(self):
        expense_buttons_frame = ttk.Frame(master=self._frame)
        update_button = ttk.Button(
            expense_buttons_frame,
            text='Update',
            command= lambda: self._mainView._update_expense_handler(
                ''.join(
                        map(
                            str,
                            list(
                                takewhile(
                                    lambda x:x !=' ',
                                    self._listBox.get(ANCHOR)[1:]
                                )
                            )
                        )
                    )
                )
        )
        update_button.grid(row=0,column=0,padx=5,pady=5)

        delete_button = ttk.Button(
            expense_buttons_frame,
            text='Delete',
            command=lambda: self._mainView._remove_expense_handler(
                ''.join(
                        map(
                            str,
                            list(
                                takewhile(
                                    lambda x:x !=' ',
                                    self._listBox.get(ANCHOR)[1:]
                                )
                            )
                        )
                    )
                )
        )
        delete_button.grid(row=0,column=1,padx=5,pady=5)

        expense_buttons_frame.pack()

    
    def _initialize(self):
        """Initializes the frame for expense list. 
            If there is not added expenses yet, shows text that tells user about it.
        """
        self._frame = ttk.Frame(master=self._root)        
        self._initialize_expense_list_header()
        nof_expenses = len(self._expenses)

        if not self._expenses:

            no_expenses_frame = ttk.Frame (master=self._frame)
            no_expenses_label = ttk.Label(
                master=no_expenses_frame, 
                text='No expenses added yet.')
            no_expenses_label.grid(
                row=0,
                column=0,
                sticky=constants.NW,
                padx=5,
                pady=5
            )
            no_expenses_frame.pack(fill=constants.X)

        else:
            self._listBox = Listbox(master=self._frame)
            for expense in self._expenses:
                self._initialize_expense_item(expense)
            self._listBox.pack(fill=constants.X)
            self._initialize_buttons()

            # Shows how many expenses user has added
            expense_amount_frame = ttk.Frame(master=self._frame)
            expense_amount_label = ttk.Label(
                master=expense_amount_frame, 
                text='You have added ' + str(nof_expenses) + ' expenses')
            expense_amount_label.grid(
                row=0,
                column=0,
                sticky=constants.NW,
                padx=5,
                pady=5
            )
            expense_amount_frame.pack(fill=constants.X)



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
        self._listBox = None

        self._initialize()

    def pack(self):
        """Shows the view
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Destroys the view
        """
        self._frame.destroy()

    def _initialize_category_list_header(self):
        header_frame = ttk.Frame(master=self._frame)
        header_label = ttk.Label(master=header_frame,
            text="Your categories", font=24)
        header_label.grid(
            row=0,
            column=3,
            sticky=constants.NW,
            padx=5,
            pady=5
            )
        header_frame.pack()


    def _initialize_category_item(self, category):
        """Initializes single Category object

        Args:
            category (Category): Category object to be shown
        """
        self._listBox.insert(0,category_service.stringify_category(category))

    def _initialize_buttons(self):
        category_buttons_frame = ttk.Frame(master=self._frame)
        see_category_button = ttk.Button(
            category_buttons_frame,
            text='View',
            command= lambda: self._mainView._handle_show_category_view(
                category_service.get_category_by_name(
                    self._listBox.get(ANCHOR),
                )
            )
        )
        see_category_button.grid(
            row=0, column=3, sticky=constants.NW, padx=5, pady=5)   

        remove_category_button = ttk.Button(
            master=category_buttons_frame,
            text="remove",
            command=lambda: self._mainView._remove_category_handler(self._listBox.get(ANCHOR))
            )
        remove_category_button.grid(
            row=0, column=4, sticky=constants.NW, padx=5, pady=5)   
        category_buttons_frame.pack()

    def _initialize_category_amount_label(self):
        nof_categories = len(self._categories)
        category_amount_frame = ttk.Frame(master=self._frame)
        category_amount_label = ttk.Label(
            master=category_amount_frame, 
            text='You have added ' + str(nof_categories) + ' categories'
        )
        category_amount_label.grid(
            row=0,
            column=3,
            sticky=constants.NW,
            padx=5,
            pady=5
        )
        category_amount_frame.pack(fill=constants.X)


    def _initialize(self):
        """Initializes frame for the category list
        """
        self._frame = ttk.Frame(master=self._root)        
        self._initialize_category_list_header()

        if not self._categories:
            no_categories_frame = ttk.Frame (master=self._frame)
            no_categories_label = ttk.Label(
                master=no_categories_frame, 
                text='No categories added yet.')
            no_categories_label.grid(
                row=0,
                column=3,
                sticky=constants.NW,
                padx=5,
                pady=5
            )
            no_categories_frame.pack()

        else:
            self._listBox  = Listbox(master=self._frame)

            for category in reversed(self._categories[-10:]):
                self._initialize_category_item(category)
            self._listBox.pack(fill=constants.X)
            self._initialize_buttons()
            self._initialize_category_amount_label()



class MainView:
    """View responsible for showing existing expenses and categories and creating new ones
    """

    def __init__(self, root, handle_logout, handle_show_expense_view, handle_show_category_view):
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
        self._handle_show_category_view = handle_show_category_view

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
            text='Budget application',
            font=48
        )
        header_label.grid(row=0, column=0, sticky=constants.NW, padx=5, pady=5)

        logout_button = ttk.Button(
            master=self._frame,
            text="Logout",
            command=self.logout_handler
        )
        logout_button.grid(row=0, column=1, padx=5, pady=5, sticky=constants.NW)

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

    def _initialize_expense(self):
        """Initializes form where user can create new Expense object
        """
        new_expense_frame = ttk.Frame(master=self._frame)
    # _initialize_expense_label(self):
        expense_label = ttk.Label(
            master=new_expense_frame, text="Add new expense", font=24)
        expense_label.grid(row=0, column=0, columnspan=2,
                           sticky=constants.NW, padx=5, pady=5)

    # _initialize_expense_name_field(self):
        name_label = ttk.Label(new_expense_frame, text="Name:")
        self._name_entry = ttk.Entry(new_expense_frame)
        name_label.grid(row=1, column=0, sticky=constants.NW, padx=5, pady=5)
        self._name_entry.grid(
            row=1, column=1, sticky=constants.NW, padx=5, pady=5)

    # _initialize_expense_value_field(self):
        value_label = ttk.Label(new_expense_frame, text="Value:")
        self._value_entry = ttk.Entry(new_expense_frame)
        value_label.grid(row=2, column=0, sticky=constants.NW, padx=5, pady=5)
        self._value_entry.grid(
            row=2, column=1, sticky=constants.NW, padx=5, pady=5)

    # _initialize_expense_category_field(self):
        category_label = ttk.Label(master=new_expense_frame, text="Category:")
        categories = category_service.find_all_categories_for_user_text()
        variable = StringVar()

        # Only existing categories are shown in dropdown menu
        self._category_dropdown = ttk.OptionMenu(new_expense_frame,
                                                variable,
                                                 categories[0],
                                                 *categories)
        category_label.grid(
            row=3, column=0, sticky=constants.NW, padx=5, pady=5)
        self._category_dropdown.grid(
            row=3, column=1, sticky=constants.NW, padx=5, pady=5)
        self._category_entry = variable

    # _initialize_expense_submit_button(self):
        create_expense_button = ttk.Button(
            master=new_expense_frame,
            text="Add expense",
            command=self._create_expense_handler
        )
        create_expense_button.grid(
            row=4, column=0, columnspan=2, sticky=constants.NW, padx=5, pady=5)

        new_expense_frame.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky=constants.NW
        )

    def _initialize_category(self):
        """Initializes form where user can add new category
        """
        new_category_frame = ttk.Frame(master=self._frame)
    # _initialize_category_label(self):
        new_category_label = ttk.Label(
            master=new_category_frame, text="Add new category", font=24)
        new_category_label.grid(row=2, column=3, columnspan=2,
                                sticky=constants.NW, padx=5, pady=5)

    # _initialize_category_name_field(self):
        self._new_category_entry = ttk.Entry(master=new_category_frame)
        self._new_category_entry.grid(
            row=3, column=3, sticky=constants.NW, padx=5, pady=5)

    # _initialize_category_submit_button(self):
        create_new_category_button = ttk.Button(
            master=new_category_frame,
            text="Add category",
            command=self._create_category_handler
        )
        create_new_category_button.grid(
            row=3, column=4, sticky=constants.NW, padx=5, pady=5)

        new_category_frame.grid(
            row=2,
            column=2,
            columnspan=2,
            sticky=constants.NW
        )

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
            sticky=constants.NW
        )
        self._category_list_frame.grid(
            row=1,
            column=2,
            columnspan=2,
            sticky=constants.NW
        )
        self._frame.grid_columnconfigure(0, weight=0, minsize=200)
        self._frame.grid_columnconfigure(1, weight=0)
        self._frame.grid_columnconfigure(2, weight=0)
        self._frame.grid_columnconfigure(3, weight=0, minsize=200)
        self._frame.grid_columnconfigure(4, weight=0)

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

    def _update_expense_handler(self, expense_id):
        """Response for action after user clicks 'Update' button 

        Args:
            expense_id: Id of the Expense to be updated
        """
        expense = expense_service.get_expense_by_id(expense_id)
        self._handle_show_expense_view(expense)


    def _remove_category_handler(self, category):
        """Response for action after user clicks 'remove' button next to one of the categories
            and updating the view

        Args:
            category: Category to be deleted
        """

        category_service.remove_category_from_user(category)
        self._initialize_category_list()
        self._initialize_expense()
