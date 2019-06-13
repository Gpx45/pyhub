#!/usr/bin/python3


def any_function(*arg):

    for i in arg:
        print(i, end=' ')
    if arg:
        print()
#d = any_function(1,4,54,674,'dog',4,78,7,4)
#print(d)


def another_func(**kargs):
    for x, y in kargs.items():
        print(x, y, sep='->', end=' ')
    if kargs:
        print()

another_func(a=23, bob='animal')
