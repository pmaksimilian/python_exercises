print("Select a number between 1 and 100")
izbrana_stevilka = int(input())

for stevec in range(1, izbrana_stevilka + 1):
    print("fizz" * (stevec % 3 == 0) + "buzz" * (stevec % 5 == 0) or stevec)
