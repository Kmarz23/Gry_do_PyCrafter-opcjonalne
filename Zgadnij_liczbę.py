import os
import random

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_console()
    print("Witaj w grze 'Zgadnij liczbę'!")
    print("Spróbuj zgadnąć liczbę z zakresu od 1 do 100.")
    print("Masz 8 prób.")

    secret_number = random.randint(1, 100)
    attempts = 0

    while attempts < 8:
        try:
            guess = int(input("Podaj swoją liczbę: "))
        except ValueError:
            print("To nie jest poprawna liczba. Spróbuj jeszcze raz.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Za mało!")
        elif guess > secret_number:
            print("Za dużo!")
        else:
            print(f"Gratulacje! Zgadłeś liczbę {secret_number} po {attempts} próbach.")
            break
    else:
        print(f"Przegrałeś! Tajna liczba to {secret_number}.")

if __name__ == "__main__":
    main()