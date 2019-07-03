# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

number = int(input("Enter number: "))

print(f"Divisors of {number} are:")

for divisor in range(2, number):
    if number % divisor == 0:
        print(divisor)
