def hello():
    print('Hello!')


hello()

def user_age_in_seconds():
    user_age = input('Enter your age: ')
    if type(user_age) == type(1):
        age_seconds = user_age * 365 * 24 * 60 * 60
        print(f"Your age in seconds is {age_seconds}.")
    else:
        print('Invalid age.')


print('Welcome to the age in seconds program!')
user_age_in_seconds()
print('Goodbye!')

"""
This is a
multi-line
string test
"""

# friends = ['Rolf', 'Bob']


# def add_friend():
#     friend_name = input('Enter your friend name: ')
#     f = friends + [friend_name]


# add_friend()

def add_friend():
    friends.append('Flambooey')


friends = []
add_friend()

print(friends)

