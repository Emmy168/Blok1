import random


# Checkt of de input een getal is
def isInt(value):
    try:
        para = input(value)
        return int(para)
    except ValueError:
        print("Probeer opnieuw")
        return False


# Definiëner van variables
getal_min = 0
getal_max = 0
gok_max = 0
lijst = []

print("Laten we een spel spelen!")
# Intro loop
while True:
    getal_min = isInt("Welk getal moet het minimum zijn? ")
    if getal_min != False:
        break

while True:
    getal_max = isInt("Welk getal moet het maximum zijn? ")
    if getal_max != False:
        break

while True:
    gok_max = isInt("Hoeveel keer wil je de gok wagen? Kies tussen 1 - 5: ")
    if gok_max == False:
        continue
    elif gok_max < 1 or gok_max > 5:
        print("Ik snap je niet. Probeer het nog eens ")
    else:
        break

# Spel
print("Raad het getal tussen", getal_min, "en", getal_max)
gok = 0
antwoord = int(random.randint(getal_min, getal_max))
aantal_gokken = 0
while gok != antwoord and aantal_gokken < gok_max:
    aantal_gokken += 1
    gok = isInt("Doe een gok: ")
    if gok == False:
        continue

    if gok < antwoord:
        lijst.append({"value": gok, "score": "Te laag!"})
        print("Sorry! Dit is te laag. Gokken over: " + str(gok_max - aantal_gokken))
    elif gok > antwoord:
        lijst.append({"value": gok, "score": "Te hoog!"})
        print("Sorry! Dit is te hoog. Gokken over: " + str(gok_max - aantal_gokken))
    else:
        lijst.append({"value": gok, "score": "Goed!"})
        print("YES! Heel goed gedaan. Het getal was inderdaad", antwoord)

for item in lijst:
    print(item["value"], "=", item["score"])
