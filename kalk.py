#!/usr/bin/env python3

def dodaj(a, b):
    return a + b

def odejmij(a, b):
    return a - b

def pomnoz(a, b):
    return a * b

def podziel(a, b):
    if b != 0:
        return a / b
    else:
        return "Nie można dzielić przez zero!"

print("Wybierz działanie:")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnożenie")
print("4. Dzielenie")

wybor = input("Twój wybór (1/2/3/4): ")

if wybor in ('1', '2', '3', '4'):
    num1 = float(input("Podaj pierwszą liczbę: "))
    num2 = float(input("Podaj drugą liczbę: "))

    if wybor == '1':
        print("Wynik dodawania:", dodaj(num1, num2))
    elif wybor == '2':
        print("Wynik odejmowania:", odejmij(num1, num2))
    elif wybor == '3':
        print("Wynik mnożenia:", pomnoz(num1, num2))
    elif wybor == '4':
        print("Wynik dzielenia:", podziel(num1, num2))
else:
    print("Nieprawidłowy wybór")

