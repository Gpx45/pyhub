
def russian(a,b):
    x = a; y = b
    z = 0
    while x > 0:
        if x % 2 == 1: z + y
        y = y << 1
        x = x >> 1
        print(z)
        print(x)
        print(y)
    return z

russian(2,2)