# This small programs ensures that the __name__ dunder is set to __main__ before it executes code.
#  Remember that __name__ is the variable the enterpreter keeps stored.
#  If the module is executed then it will work since the module is the main namespace.
#  If it is imported then it won't be the main namespace, because remember it was brought into the namespace of another module.

print('We start off in:', __name__)
if __name__ == '__main__':
    print('And end up in:', __name__)
