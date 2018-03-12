#!usr/bin/python3
"""This will create a list and open or attempt to establish a
    file stream or as many file stream as possible."""
# This will launch an error and will cause the computer to throw an error

files = []

for x in range(10000):
    files.append(open('file.txt', 'w'))


# Error
# --------------------------------------------------
# Traceback (most recent call last):
#  File ".\explode.py", line 8, in <module>
# OSError: [Errno 24] Too many open files: 'file.txt'
# --------------------------------------------------
