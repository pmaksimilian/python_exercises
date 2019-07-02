# Ask the user for a number.
# Depending on whether the number is even or odd, print out an appropriate message to the user.
# Extras:
#     1. If the number is a multiple of 4, print out a different message.
#     2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
#        If check divides evenly into num, tell that to the user. If not, print a different appropriate message.


number = int(input("Please enter a number: "))

if number % 4 == 0:
    print(f"Number {number} is a multiple of 4.")
elif number % 2 == 0:
    print(f"Number {number} is an even number.")
else:
    print(f"Number {number} is an odd number.")

check = int(input("Add another number, to check if first one divides by it: "))

if number % check == 0:
    print("It divides!")
else:
    print("It doesn't divide")
