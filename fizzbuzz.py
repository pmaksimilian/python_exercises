
print("Select a number between 1 and 100")
izbrana_stevilka = int(input())

for stevec in range(1, izbrana_stevilka + 1):
    if stevec % 15 == 0:
        print("fizzbuzz")
    elif stevec % 3 == 0:
        print("fizz")
    elif stevec % 5 == 0:
        print("buzz")
    else:
        print(stevec)
