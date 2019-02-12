import csv
from datetime import datetime
import pprint

def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')

with open('buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v.strip()

# Create a new dictionary

more_flights = {convert2ampm(k) : v.title() for k, v in flights.items()}
#                               ^
# Note the colon to separate the key values
print(flights, "\n")

print(more_flights)

# Adding filters to the comprehensions:
just_freeport = {}
for k, v in flights.items():
    if v == 'FREEPORT':
        just_freeport[convert2ampm(k)] = v.title()

print("\n", just_freeport)

just_freeport = {convert2ampm(k) : v.title() for k, v in flights.items() if v == 'FREEPORT'}
print('\n', just_freeport)

print(more_flights['09:35AM'])