#!/usr/bin/python3

phrase = "Mavin the Paranoid Android"
plist = list(phrase)
for x in plist:
    print("\t",x)

# for loops can use bracket notation with slices and it'll work as well.
for x in plist[:6]:
    print("\t"*2,x) # Using * 'multiplication operator is used to print tab 2 times'

for x in plist[-7:]:
    print("\t"*3,x)

for x in plist[10:18]:
    print("\t"*4,x)
