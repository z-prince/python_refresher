# List, regular array
l = ['Bob', 'Rolf', 'Anne']

# Tuple, unmodifiable array
t = ('Bob', 'Rolf', 'Anne')

# Set, Array that cannot have duplicates and has no particular order
s = {'Bob', 'Rolf', 'Anne'}

print(l[0])

print(t[2])

l[0] = 'Smith'
print(l)

l.append('Smith')
print(l)
# ['Smith', 'Rolf', 'Anne', 'Smith']

l.remove('Anne')
print(l)
# ['Smith', 'Rolf', 'Smith']

s.add('Smith')
s.add('Smith')
print(s)
# {'Rolf', 'Smith', 'Anne', 'Bob'}
