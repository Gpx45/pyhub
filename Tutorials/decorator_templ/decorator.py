from functools import Wraps

def decorator_name(func):
    @wraps(func)
    def wrapper(*args, **kargs):
        #1. Code to execute BEFORE calling the decorated function

        #2. Call the decorated function as required, returning items
        # results if needed
        return func(*args, **kargs)

        #3. Cose to execute INSTEAD of calling the decorated function
    return wrapper
