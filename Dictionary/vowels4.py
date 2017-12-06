
vowels = ['a','e','i','o','u']
words = input("Please Enter your phrase and or sentence: ")
found = {}
"""

found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0
"""

"""
for x in words:
    if x in vowels:
        if x == 'a':
            found['a'] += 1
        elif x == 'e':
            found['e'] += 1
        elif x == 'i':
            found['i'] += 1
        elif x == 'o':
            found['o'] += 1
        elif x == 'u':
            found['u'] += 1

for k,v in found.items():
    print(k, "There are about ", v, "in this phrase")

"""

#OR

"""
for x in words:
    if x in vowels:

        found[x] += 1

for x, y, in sorted(found.items()):
    print(x, "there are ", y, "ammouts in the sentence OR phrase.")
"""
# Look at fruitsCondition.py first.


for x in words:
    if x in vowels:
        found.setdefault(x,0) # This will add a key and value to the dictionary to initialize the dict obj.
        found[x] +=1
for x, y, in sorted(found.items()):
    print(x, "there are ", y, "ammouts in the sentence OR phrase.")
