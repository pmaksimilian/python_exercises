import random

random_stevilo = random.randint(1, 10)

print("Pozdravljeni! Ugibali boste naso skrivno stevilko!")
vneseno_stevilo = int(input("Prosimo vnesite stevilo med 1 in 10: "))

if random_stevilo == vneseno_stevilo:
    print("Cestitamo! Zadeli ste glavno nagrado!")
else:
    print(f"Zal vam tokrat ni uspelo. Pravilni odgovor bi bil {random_stevilo}")
