# While Loop
number = 7 

# while True:
#     user_input = input("Would you like to play? (Y/n) ")

#     if user_input == 'n':
#         print('Maybe next time!')
#         break

#     user_number = int(input("Guess our number: "))
#     if user_number == number:
#         print('You guessed correctly!')
#     # elif number - user_number in (1, -1):
#     elif abs(number - user_number) == 1:
#         print('You were off by one!')
#     else: 
#         print("Sorry it's wrong...")


# For Loop
friends = ['Rolf', 'Jen', 'Bob', 'Anne']

# print(f"{friends[0]} is my friend.")

for friend in friends:
    print(f"{friend} is my friend.")

# Rolf is my friend
# Jen is my friend
# Bob is my friend
# Anne is my friend

for friend in range(4):
    print(f"{friend} is my friend.")

# 0 is my friend
# 1 is my friend
# 2 is my friend
# 3 is my friend

grades = [35, 67, 98, 100, 100]
total = 0 # sum(grades)
amount = len(grades)

for grade in grades:
    total += grade

print(total / amount)
