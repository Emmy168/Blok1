# Dit is gemaakt door Emmy Schipper, klas ID1G1a, 2-9-2020
# Dit is de extra uitdaging van les 1 Programming
# Dit is geschreven in de snake_case stijl

# Hier staat de input van het gewicht in een float want het is een decimaal getal
gewicht = float(input("Hoeveel weeg je? "))

print("Gewicht in kilogram: ", +gewicht)

# De lengte die wordt ingevuld is in centimeter dus een geheel getal
lengte = int(input("Hoe lang ben je in centimeters? "))

print("Lengte in centimeters: "+str(lengte))

# Hieronder is de berekening die nodig is om het bmi te vinden
bmi = gewicht/((lengte/100)*(lengte/100))

print("BMI: ", +bmi)  
