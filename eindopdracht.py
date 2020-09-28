# Dit is Emmy Schipper's eindopdracht voor de les Programming!
# Het bevat een flowchart om te kijken of de medewerker wel naar zijn werk mag ivm Corona


print("Welkom bij de 'kan ik wel naar mijn werk' corona editie check!")
naam = input("Wat is je naam? ")

print("Hoi", naam, "behoor je tot de groep medewerkers met een kwetsbare gezondheid? ")
kwetsbaar = input("Ja of Nee? ")

while kwetsbaar == "ja" or kwetsbaar == "Ja":
    print("Ik adviseer je thuis te blijven en je werkgever te bellen.")
    break

if kwetsbaar == "nee":
    print("Dat is fijn! Ben je door de GGD gebeld over dat je in contact bent geweest met iemand met Corona? ")
    ggd = input("Ja of Nee? ")
    if ggd == "ja":
        print("De GGD bepaald welke maatregelen je moet nemen. Volg de instructies die je hebt gekregen. Blijf thuis.")
    elif ggd == "nee":
        print("Oke gelukkig maar.")

klachten = ["Verkoudheid", "Keelpijn", "Hoesten", "Verhoging", "Verlies van smaak en/of geur"]
print("Heb je last van 1 van de volgende klachten?")
print(klachten)
klachten = input("Ja of Nee? ")

if klachten == "ja":
    print(
        "Heb je ernstige klachten die passen bij het coronavirus? Zoals benauwdheid, koorts of wordt je steeds zieker?")
    zieker = input("Ja of Nee? ")
    if zieker == "ja":
        print("Meld je ziek en blijf thuis!")
    elif zieker == "nee":
        print(
            "Blijf thuis, bel 0800-1202 en maak een afspraak voor een coronatest. Blijf thuis tot de uitslag van de test bekend is")

if klachten == "nee":
    print(
        "Er zijn geen bijzondere maatregelen. Volg de afspraken die op de werkvloer zijn gemaakt ten aanzien van werken.")

meer_info = input("Zou je het fijn vinden om meer informatie te krijgen? Ja of Nee? ")
while meer_info == "ja":
    print("Je kan de GGD bellen voor meer informatie: 0800-1202 of download de corona app!")
    herhaal = input("Zal ik het herhalen? ")
    if herhaal == "nee":
        print("Fijn dat alles duidelijk is! Ik wens je veel gezondheid toe!")
if meer_info == "nee":
    print("Fijn dat alles duidelijk is! Ik wens je veel gezondheid toe!")
