
"""
import os
os.chdir('/Users/Victor/buzzdata') # The file 'buzzers' must be inside this directory.

with open('buzzers.csv') as raw_data:
    print(raw_data.read())
"""
import csv

"""
with open('buzzers.csv') as data:
    for line in csv.reader(data):
        print(line)
"""

"""
with open('buzzers.csv') as data:
    for line in csv.DictReader(data):
        print(line)
"""

with open('buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.split(',')
        flights[k] = v
    print(flights)
