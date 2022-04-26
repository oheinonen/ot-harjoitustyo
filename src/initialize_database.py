from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists users;
    ''')

    cursor.execute('''
        drop table if exists expenses;
    ''')

    cursor.execute('''
        drop table if exists categories;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table users (
            username text primary key,
            password text
        );
    ''')
    cursor.execute('''
        create table expenses (
            expense_id int primary key, 
            name text,
            value int,
            category text,
            date date,
            owner text
        );

    ''')
    cursor.execute('''
        create table categories (
            category_id int primary key,
            name text,
            owner text
        );

    ''')

    connection.commit()


def initialize_database():
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)


if __name__ == '__main__':
    initialize_database()
