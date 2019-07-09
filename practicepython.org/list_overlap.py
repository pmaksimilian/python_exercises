import random

def random_list():
    lenght = random.randint(10, 20)
    list = []
    for x in range(lenght):
        list.append(random.randint(1, 30))
    list.sort()
    return list


a = random_list()
b = random_list()

c = []

for x in a:
    if x in b and x not in c:
        c.append(x)

print(a)
print(b)
print(c)
