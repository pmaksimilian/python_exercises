# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

import datetime

print("Please enter your name and age.")

this_year = datetime.datetime.now().year

name = input("Name: ")
age = int(input("Age: "))

when_hundred = this_year + (100 - age)

print(f"Hello {name}, you will be 100 years old in {when_hundred}.")

