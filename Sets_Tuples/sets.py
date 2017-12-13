
# We will be looking at sets
# They are like Lists, execpt the difference is that, they do not allow duplicates.

# Notation of sets:

# ex. With just curly braces separated by commas
# vowels = {'a','e','i','o','u'}
# OR
# vowels = set('a','e','i','o','u')
# They can also use the sorted() function to order them as they by themselves do not place order as dictionaries.

# Examples of vowels.py version 3
# vowels = ['a','e','i','o','u']

# word = input("\nPlease provide a word: ") # asks user for input

# word = input("\nPLease provide a word: " # asks user for input)

# found = []

"""
for x in word: # check every object in word string obj
    if x in vowels: # if one of those chars are in  vowels then go
        if x not in found: # if they are not inside  found list
            found.append(x) # append that object to the end of the list
for y in found: # For each letter of the found
    print(y) # Print each indexed letter.
"""

# we can place

vowels = set('aeeeiouuu')
word = input("\nPLease provide a word: ") # asks user for input

print('Vowels: ',sorted(vowels))
print('Input: ',sorted(word))

new_set = sorted(vowels.union(set(word)))
print('New Set: ',sorted(new_set))

left_over = sorted(vowels.difference(set(word)))
print('Left Over: ',sorted(left_over))

common = sorted(vowels.intersection(set(word)))
print('Common: ',sorted(common))

# Check vowels7.py
