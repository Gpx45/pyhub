#!/usr/bin/python3
# Here We'll showing slice notation on lists
# Take the funtionality of range function into lists
# list[start:stop:step]
# By default if START is missing then the defaults is 0
# By default if STOP is missing then it takes the maximum value available by the lists
# By default if STEP is missing then the defaults is 1

letters = ['D','o','n',"''",'t',' ', 'p', 'a', 'n', 'i','c', '!']
list1 = letters[0:10:3]
# This statement starts at 0 stops at position 10 if exists and goes up by three

list2 = letters[3:]
# This statement starts at 3 and give everything else.

list3 = letters[:10]
# This statement starts at 0 stop at pos. 10 and go up by one.

list4 = letters[::2]
# This statement starts at 0 stops at the end of the list and goes up by 2.

#print(list1)
#print(list2)
#print(list3)
#print(list4)


# Now a proper example on how to place a string into a list
#-------------------------------------------------------------------------------------
book = "The Lord of the Rings"
book_list = list(book)
# This is how you can place objects into a list

# You can use the join function with slice notation

str1 = ''.join(book_list[:3])
#print(str1)

# You can also go backwards
str2 = ''.join(book_list[-5:])
#print(str2)

# You can go backwards with negative numbers on the STEP
backwards =  book_list[::-1]
#print(backwards)

# You can slice out a word from the sentence backwards
str3 = ''.join(book_list[20:15:-1])
print(str3)
