class User:
    """ Class that expresses users
    """
    def __init__(self, username, password):
        """Constructor for the class that creates new user

        Args:
            username (String): username of the user
            password (String): password of the user
        """
        self.username = username
        self.password = password
