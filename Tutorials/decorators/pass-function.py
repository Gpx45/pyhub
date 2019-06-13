#!/usr/bin/python3

# In this script its showing how to invoke a passed function.
#(Pass a function to a function)
# First create a function and then pass a built in function ans it'll call the function if returned

#---- Pass a function to a function
"""
def apply(func: object, value: object) -> object:
    return func(value)

print(apply(type, apply))
"""

# Return a function from a function.
# Nested functions.
# Returning a function to another function.
def outer() -> object:
    def inner():
        print('inner function speaking')

    print('outer function.')
    return inner # -> Returns the inner function back out.

print("\n\n")
inside = outer() # -> When you assign the function back out it returns the inner therefore changing the
inside() # -> invokes the inner function.
