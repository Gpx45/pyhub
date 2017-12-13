# Will be seeing functions and their basic setup in Python.
"""
def search_vowels():
    vowels = set('aeeeiouuu')
    word = input("\nPLease provide a word: ") # asks user for input
    common = sorted(vowels.intersection(set(word))) # Takes vowels (set) and cycles it against word (set) and shows which objects they have in common.
    print('Common: ',sorted(common))

"""
# Another example with parameters.

def search_vowels(word):
    vowels = set('aeeeiouuu')
    common = sorted(vowels.intersection(set(word))) # Takes vowels (set) and cycles it against word (set) and shows which objects they have in common.
    print('Common: ',sorted(common))


# Check Bools folder for explanation:

def search_vowels(word):
    vowels = set('aeeeiouuu')
    common = sorted(vowels.intersection(set(word))) # Takes vowels (set) and cycles it against word (set) and shows which objects they have in common.
    return bool(common)

# Return can only return one object so to return multuiple things you need to return
# an entire structure.

def search_vowels(word):
    vowels = set('aeeeiouuu')
    common = vowels.intersection(set(word))
    return common
