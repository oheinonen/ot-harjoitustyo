from entities.user import User
from database_connection import get_database_connection


def get_user_by_row(row):
    return User(row['username'], row['password']) if row else None


class UserRepository:
    """ Class responsible for database operations of User objects
    """

    def __init__(self, connection):
        """Constructor for the class

        Args:
            connection: Connection object for the database
        """
        self._connection = connection

    def create(self, user):
        """Saves new User to the database

        Args:
            user (User): User object to be saved to the database

        Returns:
            User: User object saved to the database
        """
        cursor = self._connection.cursor()

        cursor.execute(
            'insert into users (username, password) values (?, ?)',
            (user.username, user.password)
        )

        self._connection.commit()

        return user

    def find_all(self):

        cursor = self._connection.cursor()

        cursor.execute('select * from users')

        rows = cursor.fetchall()

        return list(map(get_user_by_row, rows))

    def find_by_username(self, username):
        """Helps to find specified expense by username

        Args:
            username (String): text corresponding to username

        Returns:
            User: User object corresponding to the given input
        """

        cursor = self._connection.cursor()

        cursor.execute(
            'select * from users where username = ?',
            (username,)
        )

        row = cursor.fetchone()

        return get_user_by_row(row)

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute(
            'delete from users'
        )
        self._connection.commit()


user_repository = UserRepository(get_database_connection())
