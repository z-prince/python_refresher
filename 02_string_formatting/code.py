name = 'Bob'
greeting = f"Hello, {name}"

# print(greeting)

name = 'Rolf'

# print(greeting)

# print(f"Hello,  {name}")


# Templates

name = 'Bob'
greeting = "Hello, {}"
with_name = greeting.format(name)

print(with_name)

name = 'Rolf'

print(with_name)


longer_phrase = "Hello, {}. Today is {}"

formatted = longer_phrase.format('Rolf', 'Monday')
print(formatted)
