#!/usr/bin/python3
""" Here we start with dictionaries,
These are like lists however they are like a
map (C++, Java) or hash (Perl, Ruby)
They are like a look up table in which use a key value pair
you SEARCH for the key to get the value its corresponds to. """

person = {'Name': 'John Doe',
          'Gender': 'Male',
          'Occupation': 'Researcher',
          'Home Planet': 'Mars'}

# dictionaries understand brackets but instead of indexes of numbers it uses the keys
print(person['Name'])

#You can add keys and values at run-time
person['Age'] = 33
print(person)
