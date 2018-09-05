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


def last_function(*args, **kargs):
    if args:
        for i in args:
            print(i, sep=' ', end=' ')
    if kargs:
        for a, b in kargs.items():
            print(a, b, sep=' ', end=' ')

last_function(1,2,3,4, a=23,b='frog', c=20)
