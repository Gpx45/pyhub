
"""
import os
os.chdir('/Users/Victor/buzzdata') # The file 'buzzers' must be inside this directory.

with open('buzzers.csv') as raw_data:
    print(raw_data.read())
"""
import csv
from datetime import datetime
import pprint

def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')



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
        k, v = line.strip().split(',')
        flights[k] = v
    
pprint.pprint(flights)
print() 

flights2 = {}
for k, v in flights.items():
    flights2[convert2ampm(k)] = v.title()
pprint.pprint(flights2)

## How to create comprehensions to shorten the pattern of creating a new data structure and extracting data to it with a for loop.
destinations = []

for dest in flights.values():
    destinations.append(dest.title())
print(destinations)

## Above you see a pretty common pattern in Python. So below its a shorthand (also known as a comprehension.)

more_dest = [dest.title() for dest in flights.values()]
print(more_dest)
## In the above example you see that you can create the conversation within the more_dest data structure.

flight_times = []
for ft in flights.keys():
    flight_times.append(convert2ampm(ft))
print(flight_times)

fts2 = [convert2ampm(ft) for ft in flights.keys()]
print(fts2)
## Another example but with Keys this time.

