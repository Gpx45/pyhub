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


# Now lets see what could we do if we needed to generalize the function
# But still maintain the old simple method
# We can set a  default value on the argument call.

def vsearch(phrase: str, letters: str = 'aeiou' )-> set:
    return set(letters).intersection(set(phrase))
# INTERPRETER----------------------------------------------------------
# >>> vsearch('hello')
# >>> {i,o}

# Now for keyword assignment, this allows you to  have each argument in any order.
# See mymodule folder for this function.
