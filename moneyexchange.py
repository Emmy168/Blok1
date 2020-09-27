#Dit is Practicumopdracht 2 Moneyexchange gemaakt door Emmy Schipper ID1G1a

#Input
valuta = input("Welke valuta wilt u wisselen? 1= USD 2= GBP 3= JPY ")

#USD naar EUR
if valuta == '1':
    dollar = float(input("Hoeveel Dollar wilt u wisselen? "))
    wisselkoers = 0.84
    berekening = (dollar * wisselkoers)
    transactiepercentage = float(1.5)
    transactiekosten = round(berekening / transactiepercentage, 2)
    print("Voor $", dollar, "krijgt u €", berekening)
    if transactiekosten <= 2:
        transactie_nieuw = int(2)
        totaal = round(berekening - transactie_nieuw, 2)
        print("De transactiekosten bedraagt €",int(transactie_nieuw))
        print("U ontvangt €",totaal)
    elif 2 < transactiekosten < 15:
        totaal = round(berekening - transactiekosten, 2)
        print("De transactiekosten bedraagt €",transactiekosten)
        print("U ontvangt €",totaal)
    elif transactiekosten >= 15:
        transactie_nieuw = int(15)
        totaal = round(berekening - transactie_nieuw, 2)
        print("De transactiekosten bedraagt €",int(transactie_nieuw))
        print("U ontvangt €",totaal)

#GBP naar EUR
if valuta == '2':
    gbp = float(input("Hoeveel GBP wilt u wisselen? "))
    wisselkoers = 1.12
    berekening = (gbp * wisselkoers)
    transactiepercentage = float(1.5)
    transactiekosten = round(berekening / transactiepercentage, 2)
    print("Voor £", gbp, "krijgt u €", berekening)
    if transactiekosten <= 2:
        transactie_nieuw = int(2)
        totaal = round(berekening - transactie_nieuw, 2)
        print("De transactiekosten bedraagt €",int(transactie_nieuw))
        print("U ontvangt €",totaal)
    elif 2 < transactiekosten < 15:
        totaal = round(berekening - transactiekosten, 2)
        print("De transactiekosten bedraagt €",transactiekosten)
        print("U ontvangt €",totaal)
    elif transactiekosten >= 15:
        transactie_nieuw = int(15)
        totaal = round(berekening - transactie_nieuw, 2)
        print("De transactiekosten bedraagt €",int(transactie_nieuw))
        print("U ontvangt €",totaal)

#JPY naar EUR
if valuta == '3':
    jpy = float(input("Hoeveel JPY wilt u wisselen? "))
    wisselkoers = 0.0080
    berekening = (jpy * wisselkoers)
    transactiepercentage = float(1.5)
    transactiekosten = round(berekening / transactiepercentage, 2)
    print("Voor ¥", jpy, "krijgt u €", berekening)
    if transactiekosten <= 2:
        transactie_nieuw = int(2)
        totaal = round(berekening - transactie_nieuw, 2)
        print("De transactiekosten bedraagt €",int(transactie_nieuw))
        print("U ontvangt €",totaal)
    elif 2 < transactiekosten < 15:
        totaal = round(berekening - transactiekosten, 2)
        print("De transactiekosten bedraagt €",transactiekosten)
        print("U ontvangt €",totaal)
    elif transactiekosten >= 15:
        transactie_nieuw = int(15)
        totaal = round(berekening - transactie_nieuw, 2)
        print("De transactiekosten bedraagt €",int(transactie_nieuw))
        print("U ontvangt €",totaal)
