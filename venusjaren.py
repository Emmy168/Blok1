# Dit is practicumopdracht 1 gemaakt voor Emmy Schipper, klas ID1G1a, 2-9-2020
# Het doel van de opdracht is een leeftijdsberekening in 2020 en in Venusjaren
# Dit is geschreven in de snake_case stijl

# Input
naam = input("Hoe heet je? ")
geboortejaar = input("Wat is je geboortejaar? ")

# Berekening
huidige_jaar = 2020
leeftijd = (int(huidige_jaar) - int(geboortejaar))
venus_jaar = 0.62
venus_leeftijd = leeftijd / venus_jaar

# Output
print("Beste "+naam, "in 2020 zal je leeftijd op aarde "+str(+leeftijd), "zijn.")
print("En je leeftijd is dan "+str(venus_leeftijd), "in Venusjaren.")
