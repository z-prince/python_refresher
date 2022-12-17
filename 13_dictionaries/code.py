# friend_ages = {'Rolf': 24, 'Adam': 30, 'Anne': 27}

# friend_ages['Bob'] = 20

# print(friend_ages['Adam'])
# print(friend_ages)

# friend_ages['Rolf'] = 987

# print(friend_ages)

friends = [
    {'name': 'Rolf', 'age': 24},
    {'name': 'Adam', 'age': 34},
    {'name': 'Anne', 'age': 29}
]

print(friends[0]['age'])

student_attendance = {
    'Rolf': 96,
    'Bob': 80,
    'Anne': 100
}

user_input = input('Please enter student name: ')

# for student, attendance in student_attendance.items():
#     print(f"{student}: {attendance}%")

# if 'Bob' in student_attendance:
#     print(f"Bob: {student_attendance['Bob']}%")
# else:
#     print('Bob is not a student in this class.')


if user_input in student_attendance:
    print(f"{user_input}: {student_attendance[user_input]}%")
else:
    print(f'{user_input} is not a student in this class.')


attendance_values = student_attendance.values()
print(sum(attendance_values) / len(attendance_values))

