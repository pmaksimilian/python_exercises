print("Fibonaccijevo zaporedje:")
f0 = 1
f1 = 1
f2 = 0
print(f0)
print(f1)
for i in range(15):
    f2 = f0 + f1
    print(f2)
    f0 = f1
    f1 = f2
