
# hair color:
black_hair = "CCAGCAATCGC"
brown_hair = "GCCAGTGCCG"
blonde_hair = "TTAGCTATCGC"

# facial shape:
square_face = "GCCACGG"
round_face = "ACCACAA"
oval_face = "AGGCCTCA"

# eye color:
blue_eyes = "TTGTGGTGGC"
green_eyes = "GGGAGGTGGC"
brown_eyes = "AAGTAGTGAC"

# gender:
male = "TGCAGGAACTTC"
female = "TGAAGGACCTTC"

# race:
white_race = "AAAACCTCA"
black_race = "CGACTACAG"
asian_race = "CGCGGGCCG"

# suspects:
eva = {"name": "Eva",
       "gender": female,
       "race": white_race,
       "hair color": blonde_hair,
       "eye color": blue_eyes,
       "face shape": oval_face,
       "suspect": True}

larisa = {"name": "Larisa",
          "gender": female,
          "race": white_race,
          "hair color": brown_hair,
          "eye color": brown_eyes,
          "face shape": oval_face,
          "suspect": True}

matej = {"name": "Matej",
         "gender": male,
         "race": white_race,
         "hair color": black_hair,
         "eye color": blue_eyes,
         "face shape": oval_face,
         "suspect": True}

miha = {"name": "Miha",
        "gender": male,
        "race": white_race,
        "hair color": brown_hair,
        "eye color": green_eyes,
        "face shape": square_face,
        "suspect": True}

people = [eva, larisa, matej, miha]

with open("dna.txt", "r") as dna_file:
    dna = dna_file.read()

for person in people:
    for key in person:
        if (key != "name") and (key != "suspect"):
            if person[key] not in dna:
                person["suspect"] = False
                break

for person in people:
    if person["suspect"] == True:
        print(f"Krivec je {person['name']}")
        break
