#!/usr/bin/python3

"""Module for accessing the hbtn_0e_0_usa database"""
import MySQLdb
import sys


def connectToDB(host, user, password, database, port):
    """Connects to the database
        Args:
            host (str): The `database host`
            user (str): The `database user`
            password (str): The `database user's password`
            database (str): The `database name`
            port (str): The `database port` to connect to
        Returns: The database connection object
    """
    return MySQLdb.connect(host, user, password, db=database, port=port)


def main():
    """Entry point of the application"""
    args = sys.argv[1:]
    db_host = 'localhost'
    db_port = 3306
    db_user = args[0]
    db_password = args[1]
    database = args[2]
    query = """
    SELECT cities.id, cities.name, states.name FROM cities
    JOIN states
    ON states.id = cities.state_id
    ORDER BY cities.id ASC;
    """
    db_connection = connectToDB(
        host=db_host, user=db_user,
        password=db_password,
        database=database,
        port=db_port)
    db_cursor = db_connection.cursor()
    db_cursor.execute(query)
    results = db_cursor.fetchall()
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
