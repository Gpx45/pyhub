
vowels = ['a','e','i','o','u']

word = input("\nPlease provide a word: ") # asks user for input

word = input("\nPLease provide a word: " # asks user for input)

found = []

for x in word: # check every object in word string obj
    if x in vowels: # if one of those chars are in  vowels then go
        if x not in found: # if they are not inside  found list
            found.append(x) # append that object to the end of the list
for y in found: # For each letter of the found
    print(y) # Print each indexed letter.
