def venusjaar():
    venus = 0.62
    leeftijd = jaarnu - geboortejaar
    venusleeftijd = leeftijd / venus
    print("Jouw leeftijd in Venusjaren is", venusleeftijd)

geboortejaar = int(input("Wat is je geboortejaar? "))
jaarnu = int(input("Wat is het huidige jaar? "))
venusjaar()
