#!/usr/bin/python3
# every object in Python has a truth value associated with it, in that the object
# evaluates to either TRUE or FALSE

"""
>>> bool(0)     If results are 0 their FALSE
False
>>> bool(0.0)   If results are 0 their FALSE
False
>>> bool('')    If results are empty their FALSE
False
>>> bool([])    If results are empty their FALSE
False
>>> bool({})    If results are empty their FALSE
False
>>> bool(())    If results are empty their FALSE
False
>>> bool(None)  In Python the "None" value is FALSE
False
>>>

"""
# Now for TRUE
"""
>>> bool(1)     Any number that is not 0 is TRUE
True
>>> bool(-1)    Any number that is not 0 is TRUE
True
>>> bool(42)    Any number that is not 0 is TRUE
True
>>> bool(0000000000000.0000000000000000000000001)   Any number that is not 0 is TRUE
True
>>> bool('Panic')   Any non-empty string is always TRUE
True
>>> bool([53,64,2,234])     Any non-empty structure is always TRUE
True
>>> bool({'a': 43,'b': 67,'c': 41,'d': 4})     Any non-empty structure is always TRUE
True
>>>

"""
