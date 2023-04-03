#lambda functions are exclusively used to operate on inputs and return outputs.
# They are almost never used to perform actions

#typical function
def add(x, y):
    return x + y


print(add(5, 7))

#lambda function
# uncommon but possible use case:
(lambda x, y: x + y)(5, 7)

# named lambda function:
# add = lambda x, y: x + y

# Typical use cases for lambda functions:

def double(x):
    return x * 2


sequence = [1, 3, 5, 9]
# list comprehension (faster than map):
doubled = [double(x) for x in sequence]

# mapping (better for synergy in a stack with multiple languages):
doubled = map(double, sequence)
# map function does not return a list of numbers, it returns a map object.
# example of using lambda with map:

doubled = list(map(lambda x: x * 2, sequence))

