
def indexOfCaps(args):
    return [args.index(letter) for letter in list(args) if letter.isupper() == True ]
print(indexOfCaps("HellO WORld"))