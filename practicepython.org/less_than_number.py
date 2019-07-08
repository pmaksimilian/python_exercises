
list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(list)
new_list = []
number = int(input("Print the numbers that are less than (enter number): "))

for i in list:
    if i < number:
        new_list.append(i)

print(new_list)
