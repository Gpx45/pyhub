#!/usr/bin/python3
# These represent the difference between passed by value append
# and passed by reference.

def double(arg):
	print('Before: ', arg)
	num=arg * 2
	print('After: ',num)


def change(arg):
	print('Before: ', arg)
	num3=arg.append('what')
	print('After: ',num3)

num3=[2,3,4]
num=2
#double(num)
change(num3)
print(num3)
#print(num)
