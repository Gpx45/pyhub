
# Here you use a try catch to resolve runtime error that raise exceptions.

try:
    with open('myfile.txt') as fh:
        file_data = fh.read()
    print(file_data)
except FileNotFoundError:
    print('The data file is missing.')
except PermissionError:
    print('You do not have permission.')
except Exception as err: # This sets an exception object in general to output its object content to the err variable.
    print("An error happened: ", str(err))
