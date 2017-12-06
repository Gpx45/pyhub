# This is how you can work with a dictionary
# Typically you want to use it to work with structured data

found = {}

found['a'] = 0
found['e'] = 1
found['i'] = 0
found['o'] = 2
found['u'] = 0

#for key in found:
    #print(key, "was found ",found[key], "times")

# dictionaries don't typically make things sort so don't count on keeping it all sorted.
# you can use the sorted() function on a dictionary to sort it as it was placed.

#for key in sorted(found):
    #print("\n", key, "was found ",found[key], "times")

# You can also use the items() function to output a list of the dictionary

for key, value in sorted(found.items()):
    print(key, "has about ", value, "ammouts ")
