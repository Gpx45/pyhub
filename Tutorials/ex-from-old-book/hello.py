#!/usr/bin/python3
#/usr/bin/env/python
#/usr/local/bin/python
# The lines up above is for UNIX/Linux portability
print("Hello World");
say = "Not on expects " + \
"the Spanish Inquisition!";
# use \ if you wish to break up a statement into 2 lines.
print(say);


#Types don't need to be assigned to a variable.
#Values can get reassined to a variable everytime its reassined.
x = 5;
print(x)
# then we reassin.
x = "Albatros!!!!"
print(x)

# you can also assign any object to (function,class or modules). EVERYTHING IS AN OBJECT!
x = round
print(x(34.577456, 2));
# Or make a regular function.
x = round(55.64574, 2)
print(x)
# The following is to see how you can cause a circular reference, which the garbage collector wont pick up so typically avoid.
a = [1, 2, 3]
b = [4, 5, 6]
a.append(b)
print(a)
print(b)
# You can cause circular references this way so you can add something in between thes "append and dels"
import sys
print(sys.getrefcount(b))
#here:
del a[-1]
del b[-1]

#brings a reference count back
del a
del b # you cannot refer to either of these again after this so be careful.

# if you do not want the garbage collector to collect any references just use. "-without-cycle-gc"
