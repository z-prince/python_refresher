def add(x, y):
    return x + y


add(5, 8)
result = add(5, 8)
print(result)
print(add(5, 8))

def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You Fool!"


result = divide(15, 0)
print(result)
