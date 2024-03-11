#!/usr/bin/python3

"""
Module that lists states from MySQL database
"""
import MySQLdb
import sys


def connectToDB(host, user, password, database, port):
    """Connects to the database
        Args:
            host (str): The `database host`
            user (str): The `database user`
            password (str): The `database user's password`
            database (str): The `database name`
        Returns: The database connection object
    """
    return MySQLdb.connect(host, user, password, db=database, port=port)


def main():
    """Entry of application"""
    args = sys.argv[1:]
    db_host = 'localhost'
    db_port = 3306
    db_user = args[0]
    db_password = args[1]
    database = args[2]
    query = """
        SELECT * FROM states
        ORDER BY states.id ASC;
        """

    dbConnection = connectToDB(
        db_host, db_user, db_password, database, db_port)
    cursor = dbConnection.cursor()
    cursor.execute(query)
    states = cursor.fetchall()
    for state in states:
        print(state)


if __name__ == "__main__":
    main()
