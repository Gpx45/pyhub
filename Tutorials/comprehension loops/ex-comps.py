from pprint import pprint

data = [1, 2, 3, 4, 5, 6, 7, 8]

evens = []

for num in data:
    if not num % 2:
        evens.append(num)

print(evens)

evens = [num 
         for num in data 
            if not num % 2
        ]

print(evens)
print("--------------------------------------------")

data = [1, 'one', 2, 'two', 3, 'three', 4, 'four']

words = []
for num in data:
    if isinstance(num, str):
        words.append(num)

print(words)

words =[
    num 
    for num in data
        if isinstance(num, str)
]

print(words)

print("--------------------------------------------")

data = list('So long and thanks for all the fish'.split())
title = []
for word in data:
    title.append(word.title())

print(title)

title = [word.title() for word in data]

print(title)

print("--------------------------------------------")


with open('buzzers.csv') as data:
    ignore = data.readline()
    fts = {}
    for line in data:
        k, v = line.strip().split(',')
        fts[k] = v.strip().title()

west = [k for k, v in fts.items() if v == 'West End']

print(fts)
print(west)

print("--------------------------------------------")

dests = set(fts.values())

#print(dests)

when = {}
for dests in set(fts.values()):
    when[dests] = [k for k, v in fts.items() if v == dests]
pprint(when)
