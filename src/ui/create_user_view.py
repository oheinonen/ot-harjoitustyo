from tkinter import ttk, constants
from services.user_service import user_service


class CreateUserView:
    """View responsible for new account creation
    """
    def __init__(self, root, handle_create_user, handle_show_login_view):
        """Constructor for the class. Creates new create user view

        Args:
            root : tkInter element where the ui will be outlined
            handle_create_user: Value that is called when user logs inis created
            handle_show_login_view: Value that is called when user wants to see login view
        """
        self._root = root
        self._username_entry = None
        self._password_entry = None
        self._handle_create_user = handle_create_user
        self._handle_show_login_view = handle_show_login_view
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

    def _initialize_username_field(self):
        username_label = ttk.Label(master=self._frame, text='Username')
        self._username_entry = ttk.Entry(master=self._frame)
        username_label.grid(sticky=constants.W, padx=5, pady=5)
        self._username_entry.grid(
            row=1, column=1, sticky=constants.EW, padx=5, pady=5)

    def _initialize_password_field(self):
        password_label = ttk.Label(master=self._frame, text="Password")
        self._password_entry = ttk.Entry(master=self._frame, show="*")
        password_label.grid(sticky=constants.W, padx=5, pady=5)
        self._password_entry.grid(
            row=2, column=1, sticky=constants.EW, padx=5, pady=5)
    
    def _initialize_create_user_button(self):
        create_user_button = ttk.Button(
            master=self._frame,
            text="Create!",
            command=self._create_user_handler
        )
        create_user_button.grid(
            row=3, column=1, sticky=constants.W, padx=5, pady=5)

    def _initialize_login_button(self):
        login_button = ttk.Button(
            master=self._frame,
            text="Login",
            command=self._handle_show_login_view
        )
        login_button.grid(row=3,column=0,sticky=constants.W, padx=5, pady=5)
        

    def _initialize(self):
        """Creates the frame where the create user view is build with the help of other functions
        """

        self._frame = ttk.Frame(master=self._frame)

        header = ttk.Label(master=self._frame, font=24, text="Create new user")
        header.grid(columnspan=2, sticky=constants.EW, padx=5, pady=5)

        self._initialize_username_field()
        self._initialize_password_field()
        self._initialize_create_user_button()
        self._initialize_login_button()
        self._frame.grid_columnconfigure(1, weight=1, minsize=300)

    def _create_user_handler(self):
        """ Checks that the user does not exist, creates new user and saves it 
        to the database and opens the main view 
        """
        username = self._username_entry.get()
        password = self._password_entry.get()

        if user_service.create_user(username, password):
            self._handle_create_user()
