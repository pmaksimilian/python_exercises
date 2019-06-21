a = int(input("Prvo stevilo: "))
b = int(input("Drugo stevilo: "))
operacija = input("Operacija (+ - * /): ")

if operacija == "+":
    c = a + b
    print(f"{a} + {b} = {c}")
elif operacija == "-":
    c = a - b
    print(f"{a} - {b} = {c}")
elif operacija == "*":
    c = a * b
    print(f"{a} * {b} = {c}")
elif operacija == "/":
    c = a / b
    print(f"{a} / {b} = {c}")
else:
    print("Neznana operacija.")
