import random

drzava_mesto = {"Slovenija": "Ljubljana",
                "Avstrija": "Dunaj",
                "Hrvaska": "Zagreb"}


def choose_random_country(country_dict):
    drzave = list(country_dict.keys())
    return random.choice(drzave)


def check_guess(guess, answer):
    return guess == answer


chosen_country = choose_random_country(drzava_mesto)

print(f"Katero je glavno mesto drzave {chosen_country}?")

for guess_num in range(5):
    ans = input("Odgovor: ").lower().capitalize()
    if check_guess(ans, drzava_mesto[chosen_country]):
        print("Super")
        break
    print("Poskusi se enkrat!")
