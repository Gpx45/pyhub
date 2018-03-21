#!etc/bin/python3
''' This is an example of classes '''
class goUp:

    def __init__(self, v: int = 0, i: int = 1): # This is the dunder that will set your variables in the class.
        self.b = v # Setting each variable with the self, variables to instantiate a class.
        self.inc = i # the self is going to be the variable that actually creates assigns the object.

    def cUp(self):
        self.b += self.inc
        return self.b

    def __repr__(self): # Creating this method will alter the behavior of what the class returns.
        return repr(self.b)


add = goUp()
add.cUp()
print(add)
