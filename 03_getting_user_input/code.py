# String
# name = input("Enter your name:")
# print(name)

# Integers
size_input = input("How big is your gouse (in square feet): ")
square_feet = int(size_input)
square_meters = square_feet / 10.8
print(
    f"{square_feet} square feet is equal to approximately {round(square_meters, 2)} square meters!"
)
