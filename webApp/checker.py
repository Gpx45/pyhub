#!/usr/bin/python3
from flask import session


def check_logged_in(func: object) -> object:
    def wrapper():
        if 'logged_in' in session:
            return "You are currently logged in."
        return 'You are NOT logged in'
    return wrapper
