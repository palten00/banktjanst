print("välkommen  till banktjänsten.se")
saldo = 0 
meny = 0

while meny != 4: # sålänge 4 in körs så startar den menyn igen
    print("tryck 1 för insättning ")
    print("tryck 2 för uttag ")
    print("tryck 3 för visa saldo ")
    print("tryck 4 för att avsluta ")
    try:
        meny = int(input("välj en siffra för att fortsätta ")) #skriv in en siffra från menyn för att fortsätta
    except:
        print("du måste välja en siffra") #om ingen siffra angavs så loopar den tillbaka till meny grejen
    if meny == 1: 
        saldo = saldo + int(input("sätt in pengar ")) # den tar saldot och lägger till det man skriver 
    elif meny == 2: 
        saldo = saldo - int(input("ta ut pengar ")) #den tar saldot och drar pengar ifrån det
    elif meny == 3:
        saldo = print("ditt saldo är:", saldo) #visar saldo
    elif meny == 4:
        print("tack för att du har använt oss") # avslutar programmet 