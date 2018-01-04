
# Here we will create a dictionary and expend it and check to add
# more values.

fruits = {'apples': 10,'bananas': 3}


"""
if 'pears' not in  fruits:
    fruits['pears'] = 0
fruits['pears'] += 1
for x, y, in fruits.items():
    print(x,y)
"""

# Another way of writting this code with a function setdefault()

fruits.setdefault('pears', 0)
fruits['pears'] += 1
for x,y in fruits.items():
    print(x,y)
