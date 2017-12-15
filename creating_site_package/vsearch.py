
def vsearch(phrase: str, letters: str = 'aeiou' )-> set:
    return set(letters).intersection(set(phrase))

# INTERPRETER----------------------------------------------------------
# >>> vsearch(letters = 'hello', phrase = 'aie')
# >>> {e}
