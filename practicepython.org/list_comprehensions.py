
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even = []

for x in a:
    if x % 2 == 0:
        even.append(x)

print(even)

b = [y for y in a if y % 2 == 0]

print(b)
