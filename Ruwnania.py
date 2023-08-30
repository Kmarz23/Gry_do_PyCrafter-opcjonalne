import os
import sys

os.system('cls' if os.name == 'nt' else 'clear')
print("Witaj w grze Ruwnania\n")
print("Napisz dobrą odpowiedź a wygrasz!\n")
input("Naciśnij enter aby zacząć")
os.system('cls' if os.name == 'nt' else 'clear')
print("Lvl 1")
lvl1 = input("1 + 1 = ? \n: ")
if lvl1 == "2":
    print("\nDobrze\n")
    print("Lvl 2\n")
    print("37 x 7 = ? \n")
    lvl2 = input(": ")
    if lvl2 == "259":
        print("Gratulacje")
        sys.exit()
    else:
        print("Przegrałeś")
        sys.exit()
else:
    print("Przegrałeś")
    sys.exit()