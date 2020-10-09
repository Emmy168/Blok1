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
