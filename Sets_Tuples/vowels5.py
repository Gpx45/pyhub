
vowels = set('aeeeiouuu')
word = input("\nPLease provide a word: ") # asks user for input
common = sorted(vowels.intersection(set(word))) # Takes vowels (set) and cycles it against word (set) and shows which objects they have in common.
print('Common: ',sorted(common))

# Please check sets.py to understand.
