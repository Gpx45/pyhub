#!/usr/bin/python3
from functools import wraps # -> To prevent decorator functions from losing identity.
from flask import session

def check_logged_in(func: object) -> object:
    @wraps(func) # -> Wraps the decorator in its own container for intergrity.
    def wrapper(*args, **kargs): # -> Allows the function to accept any number of arguments.
        if 'logged_in' in session:
            return func(*args, **kargs) # -> When creating a decorator you must always have the same number of arguments applied from the parent function.
        return 'You are NOT logged in'
    return wrapper
