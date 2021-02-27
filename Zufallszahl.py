import random, sys;


print("Zahlenraten-Spiel: Bitte geben Sie eine Zahl zwischen 0 und 100 ein")
zufallsZahl = random.randint(0,100)
zahl = None

while zahl != zufallsZahl:

    try:
        zahl = int(input("Ihre Zahl: "))
        if(zahl<=100 and zahl >=0):
            if zahl > zufallsZahl: print("Ihre Zahl war größer")

            elif zahl < zufallsZahl : print("Ihre Zahl war kleiner")
        else:
            print("Bitte geben Sie eine Zahl zwischen 0 und 100 ein")
        
    except ValueError:
        print("Es sind nur Zahlen erlaubt")

print("Herzlichen Glückwunsch, Sie haben die Zahl erraten")
sys.exit()  








