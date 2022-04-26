from tkinter import ttk, constants
from services.user_service import user_service, InvalidCredentialsError


class LoginView:
    def __init__(self, root, handle_login, handle_show_create_user_view):
        self._root = root
        self._username_entry = None
        self._password_entry = None
        self._frame = None
        self._handle_login = handle_login
        self._handle_show_create_user_view = handle_show_create_user_view

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
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

    def _initialize(self):
        self._frame = ttk.Frame(master=self._frame)

        header = ttk.Label(master=self._frame, font=24, text="Login")
        header.grid(columnspan=2, sticky=constants.EW, padx=5, pady=5)

        self._initialize_username_field()
        self._initialize_password_field()

        login_button = ttk.Button(
            master=self._frame,
            text="Login",
            command=self._login_handler
        )
        create_user_button = ttk.Button(
            master=self._frame,
            text="Create new user",
            command=self._handle_show_create_user_view,
        )

        login_button.grid(sticky=constants.W, padx=5, pady=5)
        create_user_button.grid(
            row=3, column=1, sticky=constants.W, padx=5, pady=5)
        self._frame.grid_columnconfigure(1, weight=1, minsize=300)

    def _login_handler(self):
        """ Checks that the user exists, password matches 
        and opens the main view 
        """
        username = self._username_entry.get()
        password = self._password_entry.get()

        user_service.login(username, password)
        self._handle_login()
