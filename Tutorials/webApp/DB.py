#!/usr/bin/python3
import pymysql

class ConnectionError(Exception):
    pass

class CredentialsError(Exception):
    pass

class SQLError(Exception):
    pass

class Database:

    def __init__(self, config: dict) -> None: # The init dunder is the special method that initilizes all of the attributes of the class.
        self.configuration = config

    def __enter__(self) -> 'Cursor': # enter dunder does the setup for the class in terms of a context manager.
        try:
            self.connect = pymysql.connect(**self.configuration) # Make sure to address the parameter as a list with the ** (Remenber * is for a tuple)
            self.cursor = self.connect.cursor()
            return self.cursor
        except mysql.connector.errors.InterfaceError as err:
            raise ConnectionError(err)
        except mysql.connector.errors.ProgramingError as err:
            raise CredentialsError(err)

    def __exit__(self, exc_type, exc_value, exc_trace) -> None: # exit dunder does the breakdown of the methods in the class, in terms of the context manager.
        self.connect.commit()
        self.cursor.close()
        self.connect.close()
