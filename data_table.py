

# We can store any kind data structure into any other type of data structure.
# Since everything is an object. You can create quick objects that contains other or the same type.
# This allow of deeper programing projects.

people = {}
people['Ford'] = {'Name':'Ford Reskalsky','Gender':'Male',
                'Occupation':'Reasearcher','Home':'Earth'}
# ex.
#INTERPRETER:
# print(people)
# {'Ford': {'Name': 'Ford Reskalsky', 'Gender': 'Male', 'Occupation': 'Reasearcher', 'Home': 'Earth'}}


people ['Josepth'] = {'Name':'Josepth Green','Gender':'Male',
                'Occupation':'Procurer','Home':'Uranus'}
people ['Jenny'] = {'Name':'Jenny Miller','Gender':'Female',
                'Occupation':'Sandwich-Maker','Home':'Mars'}

# You can use the pprint module to structure the data more

import pprint

pprint.pprint(people)
