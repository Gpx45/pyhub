
def naive(a,b):
    x = a
    y = b
    z = 0

    while x > 0:
        z = z + y
        print("This is b: {}".format(z))
        x = x - 1
        print("This is a: {}".format(x))
    return z

    # What does naive(a,b) compute as a function of a and b

print("This is z: ", naive(20,12))


# the algo is a * b

