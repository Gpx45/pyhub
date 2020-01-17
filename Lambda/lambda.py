
# Expressions used to create an anonymous function:

# Compare structures

# def double(x):
#     return x * 2

# Lambda structure:

double = lambda x: x * 2


print(double(2))


# Example of a lambda function:

cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

def is_short(name):
    return len(name) < 10
# I avoided the above function:
# Ultilizaing a lambda function in the built-in higher order function "filter"
short_cities = list(filter(lambda name: len(name) < 10, cities))
print(short_cities)


numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

maps = map(lambda x: sum(x),numbers)
for i in maps:
    print(i)


