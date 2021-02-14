import random, sys;


print("Zahlenraten-Spiel: Bitte geben Sie eine Zahl zwischen 0 und 100 ein")
x = True
zufallsZahl = random.randint(0,100)

while x :
    try:
        zahl = int(input("Ihre Zahl: "))
        y = True
    except ValueError:
        y = False

    if  y :
        if(zahl<=100 and zahl >=0):
            if zahl > zufallsZahl: print("Ihre Zahl war größer")

            elif zahl < zufallsZahl : print("Ihre Zahl war kleiner")

            elif zahl == zufallsZahl :
                print("Herzlichen Glückwunsch, Sie haben die Zahl erraten")
                x = False; 
        else:
            print("Bitte geben Sie eine Zahl zwischen 0 und 100 ein")
    else:
        print("Es sind nur Zahlen erlaubt")

sys.exit()  








