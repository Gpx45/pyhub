#!/usr/bin/python3
# Here we will be manipulating a list with built functions
# of the list class



phrase = "Don't Panic!"
plist = list(phrase) # create a list and assign it a string

print(phrase)
print(plist)

for x in range(4): # This loops 4 times
    plist.pop() # Each time it pops the last chracters in the plist

plist.pop(0) # This takes out specifically the first item in the index


plist.remove("'") # This searches are removes a space

=======
plist.remove("'") # This searches are removes a space

plist.extend([plist.pop(),plist.pop()]) # This first pops the last item
# in the list, then after that it pops the nex last item on the list
# Then takes them both and extends both as a list in order in which
# They were orginally popped off.
<<<<<<< HEAD

plist.insert(2,plist.pop(3)) # This pops the T and then inserts
# It in front of the space that was orginally in front of it.

new_list = ''.join(plist) # This takes the list and parses it into
# a string object.

=======
plist.insert(2,plist.pop(3)) # This pops the T and then inserts
# It in front of the space that was orginally in front of it.
new_list = ''.join(plist) # This takes the list and parses it into
# a string object.

print(new_list) # Prints out the new string that was created.
