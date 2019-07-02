import random
import json
import datetime
import time


score_file_name = "score4.txt"

player_name =input("Vnesite vase ime: ")

with open(score_file_name, "r") as score_file:
    score_list = json.loads(score_file.read())
    score_list = sorted(score_list, key=lambda k: k["score"])
    print(f"Najboljsi trije: {score_list[:3]}")

random_stevilo = random.randint(1, 100)


print("Pozdravljeni! Ugibali boste skrivno stevilko!")

start_time = time.time()

for loop in range(10):
    vneseno_stevilo = int(input("Prosimo vnesite stevilo med 1 in 100: "))

    if random_stevilo < vneseno_stevilo:
        print("Ni pravilno! Ugibaj nizje!")
    elif random_stevilo > vneseno_stevilo:
        print("Ni pravilno! Ugibaj visje!")
    else:
        print(f"Uganil si v {loop + 1} poskusih!")
        end_time = time.time() - start_time
        elapsed_time = time.strftime("%M:%S", time.gmtime(end_time))
        current_date = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
        score_list.append(
            {"date": current_date,
             "name": player_name,
             "score": loop+1,
             "time": elapsed_time}
        )
        with open(score_file_name, "w") as score_file:
            score_file.write(json.dumps(score_list))
        break

