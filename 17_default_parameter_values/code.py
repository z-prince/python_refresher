def add(x, y=8):
    print(x + y)


add(3)

# Cannot put a positional argument after an assigned argument

default_y = 3

def add(x, y=default_y):
    sume = x + y
    print(sum)


add(2)

default_y = 4

add(2)
