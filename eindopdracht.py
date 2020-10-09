###############################################################################
# Programming Eindopdracht Blok 1
# Date: 09/10/2020
# Author: Emmy Schipper
# Klas: ID1G1a
###############################################################################
# Dit programma checkt of de medewerker naar zijn/haar
# werk mag komen, wegens COVID-19, of thuis moet blijven.
# Er moet nog gewerkt worden aan de klachten lijst
# en hoe deze uitgeprint wordt.
################################################################################

#Import modules
import sys
import wikipedia as wikipedia

#Intro input
naam = input("Wat is uw naam? ")
print("Hoi",naam,"welkom bij de 'kan-ik-wel-naar-mijn-werk' COVID-19 check!"
                 "\nHieronder wat algemene informatie over COVID-19: ")

print(wikipedia.summary("Coronavirus"))

#Functies
def kwetsbaar():
    antwoord = input("Behoort u tot de groep kwetsbare personen? JA/NEE: ")
    if antwoord.lower() != "ja":
        print("Gelukkig. We kunnen door naar de volgende stap.")
    else:
        print("Blijf thuis en bel uw werkgever.")
        sys.exit()

def ggd():
    antwoord = input("Bent u door de GGD gebeld over contact met iemand met COVID-19? JA/NEE: ")
    if antwoord.lower() != "ja":
        print("Mooi zo. We kunnen door naar de volgende stap.")
    else:
        print("Blijf thuis en bel uw werkgever.")
        sys.exit()

def temperatuur(check):
    geen_koorts = 37.5
    wel_koorts = 37.6
    if check <= geen_koorts:
        print("U heeft geen verhoging.")
    elif check >= wel_koorts:
        print("Uw lichaamstemperatuur is te hoog! Blijf thuis en bel GGD voor een corona test.")
        sys.exit()

#Refers naar functies en user input
kwetsbaar()
ggd()

#Refers naar functie temperatuur
temp = float(input("Wat is uw lichaamstemperatuur? "))
temperatuur(temp)

#Lijst van klachten
klachten_lijst = []

print("1) Verkoudheid 2) Keelpijn 3) Hoesten 4) Smaakverlies 5) Geurverlies")
while True:
    klacht = input("Heeft u 1 van de bovengenoemde klachten(1-5)?"
                       "\nIndien geen klachten, voer dan 6 voor nee in: ")
    if klacht == 1:
        klachten_lijst.append({"verkouden": naam})
    elif klacht == 2:
        klachten_lijst.append({"keelpijn": naam})
    elif klacht == 3:
        klachten_lijst.append({"hoesten": naam})
    elif klacht == 4:
        klachten_lijst.append({"smaakverlies": naam})
    elif klacht == 5:
        klachten_lijst.append({"geurverlies": naam})
    elif klacht == 6:
        print("Oke dat is goed nieuws.")
        break
    else:
        break

print(f"De klachten die u aangeeft te hebben zijn: {klachten_lijst}. Blijf thuis en bel voor een coronatest.")

#Outro
meer_info = input("Wilt u meer informatie krijgen over COVID-19? JA/NEE: ")
while meer_info.lower() != "ja":
    print("Fijn dat alles duidelijk is! Ik wens u veel gezondheid toe!")
    break
if meer_info.lower() != "nee":
    print("Bel voor meer informatie: 0800-1202 of download de corona app!")
