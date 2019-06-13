#!/usr/bin/python3
# A pig latin generator

phrase = input("Please Enter your phrase: ")
plist = list(phrase)
first_letter = plist.pop(0)
plist.append(first_letter)
new_phrase = ''.join(plist)
print(new_phrase + 'ay')
