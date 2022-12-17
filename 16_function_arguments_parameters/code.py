def add(x, y):
    print(x + y)


def sub(x, y):
    print(x - y)


def divide(dividend, divisor):
    if divisor != 0:
        print(round(dividend / divisor, 2))
    else:
        print('You fool!')


def say_hello(name, surname):
    print(f'Hello, {name} {surname}!')

# keyword arguments
say_hello(surname='Bob', name='Fledger')
# positional arguments
say_hello('Bob', 'Fledger')

divide(15, 0)
divide(dividend=15, divisor=7)
