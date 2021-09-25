k# -*- coding: utf-8 -*-
import sys
from colorama import Fore, Back  # Style
from tqdm import tqdm
import time
import numpy
blad = 1
blad1 = True
for i in tqdm(range(100)):
    time.sleep(0.005)
for i in tqdm(range(87)):
    time.sleep(0.005)
for i in tqdm(range(75)):
    time.sleep(0.005)
for i in tqdm(range(62)):
    time.sleep(0.005)
for i in tqdm(range(50)):
    time.sleep(0.005)
for i in tqdm(range(37)):
    time.sleep(0.005)
for i in tqdm(range(25)):
    time.sleep(0.005)
for i in tqdm(range(12)):
    time.sleep(0.005)
for i in tqdm(range(1)):
    time.sleep(0.005)
try:
    print(Fore.GREEN+"           _________        ____       ___        _________        ___  ___________       _________  _________       ")
    print("          |  _____  |      / /\ \      | |       |  _____  |       |_|  |___   ___|        \     /    \     /        ")
    print("          | |     |_|     / /__\ \     | |       | |     |_|       ___      | |             \   /      \   /         ")
    print("          | |      _     / ______ \    | |       | |      _        | |      | |              \_/        \_/          ")
    print("          | |_____| |   / /      \ \   | |_____  | |_____| |       | |      | |              ___        ___          ")
    print("          |_________|  /_/        \_\  |______|  |_________|       |_|      |_|              |_|        |_|          ")
    print("")
    print("")
    print("")
    print("")
    print("")
    pi = 3.14159265359
    stop = True
    while stop:
        stop2 = True
        stop3 = True
        print(
            "_____________________________________________________________MENU_____________________________________________________________")
        print("")
        print("")
        print("                         ___________________________________________________ ")
        print("                        /      1         /       2        /       3        / ")
        print("                       /   Dodawanie    /  Odejmowanie   /    Mnożenie    /  ")
        print("                      /________________/________________/________________/   ")
        print("                      \        4       \         5      \        6       \   ")
        print("                       \    Dzielenie   \     Potęgi     \   pierwiastki  \  ")
        print("                        \________________\________________\________________\ ")
        print("                        |        7       |        8       |       9        | ")
        print("                        | Więcej Działań |      Wzory     |   Informacje   | ")
        print("                        |________________|________________|________________| ")
        print("                          /      10      \       11       /      12      \   ")
        print("                         /    Notatnik    \    Silnia    /     Wyjście    \  ")
        print("                        /__________________\____________/__________________\ ")
        print("")
        print("")
        print("")
        print("")
        print("")
        print(
            "                                                                          WSZELKIE PRAWA ZASTRZEŻONE! PRZEZ GRUPĘ KRECIK® v1.7")
        info = int(input("Wybór: "))
        if info == 1:
            a = float(input("Podaj pierwszy składnik: "))
            b = float(input("Podaj drugi składnik: "))
            print("Suma:", a + b)
        elif info == 2:
            a = float(input("Podaj odjemną: "))
            b = float(input("Podaj odjemnik: "))
            print("Różnica:", a - b)
        elif info == 3:
            a = float(input("Podaj pierwszy czynnik: "))
            b = float(input("Podaj drugi czynnik: "))
            print("Iloczyn:", a * b)
        elif info == 4:
            a = float(input("Podaj dzielną: "))
            b = float(input("Podaj dzielnik: "))
            print("Iloraz:", a / b)
        elif info == 5:
            a = numpy.int64(input("Podaj Podstawę: "))
            b = numpy.int64(input("Podaj wykładnik: "))
            print("Potęga:", a ** b)
        elif info == 6:
            print("wybierz mądrze ")
            print("1.Pierwiastek pierwszego stopnia (dla kumatych)")
            print("2.Pierwiastek drugiego stopnia")
            print("3.Pierwiastek trzeciego stonia")
            print("4.Pierwiastek x stopnia")
            inf = int(input("Wybór: "))
            if inf == 1:
                a = float(input("Podaj liczbę podpierwiastkową: "))
                print("Pierwiastek:", a ** 1)
            elif inf == 2:
                a = float(input("Podaj liczbę podpierwiastkową: "))
                print("Pierwiastek:", a ** (1 / 2))
            elif inf == 3:
                a = float(input("Podaj liczbę podpierwiastkową: "))
                print("Pierwiastek:", a ** (1 / 3))
            elif inf == 4:
                a = float(input("Podaj liczbę podpierwiastkową: "))
                b = float(input("podaj stopień pierwiastka: "))
                print("Pierwiastek:", a ** (1 / b))
        elif info == 7:
            while stop2:
                print("")
                print("")
                print(
                    "________________________________________________________Więcej Działań________________________________________________________")
                print("                                                        1.Pole koła")
                print("                                                       2.Obwód koła")
                print("                                                     3.Objętość walca")
                print("                                                   4.Pole całości walca")
                print("                                                      5.Pole kwadratu")
                print("                                                     6.Obwód kwadratu")
                print("                                                   7.Objętość sześcianu")
                print("                                                 8.Pole całości sześcianu")
                print("                                                     9.Pole prostokąta")
                print("                                                    10.Obwód Prostokąta")
                print("                                               11.Objętość prostopadłościanu")
                print("                                             12.Pole całości prostopadłościanu")
                print("                                                     13.Pole trójkąta")
                print("                                                    14.Obwód trójkąta")
                print("                                                        15.Powrót")
                print("")
                info2 = int(input("Wybór: "))
                if info2 == 1:
                    a = float(input("Podaj promień: "))
                    print("Pole:", pi * a ** 2)
                elif info2 == 2:
                    a = float(input("Podaj promień: "))
                    print("Obwód:", 2 * pi * a)
                elif info2 == 3:
                    a = float(input("Podaj promień: "))
                    b = float(input("Podaj wysokość: "))
                    print("Objętość:", (pi * a ** 2) * b)
                elif info2 == 4:
                    a = float(input("Podaj promień: "))
                    b = float(input("Podaj wysokość: "))
                    print("Pole całości:", 2 * pi * a ** 2 + 2 * pi * a * b)
                elif info2 == 5:
                    a = float(input("Podaj długość boku: "))
                    print("Pole:", a ** 2)
                elif info2 == 6:
                    a = float(input("Podaj długość boku: "))
                    print("Obwód:", a * 4)
                elif info2 == 7:
                    a = float(input("Podaj długość boku: "))
                    print("Objętość:", a ** 3)
                elif info2 == 8:
                    a = float(input("Podaj długość boku: "))
                    print("Pole całości:", 6 * a ** 2)
                elif info2 == 9:
                    a = float(input("Podaj długość pierwszego boku: "))
                    b = float(input("Podaj długość drugiego boku: "))
                    print("Pole:", a * b)
                elif info2 == 10:
                    a = float(input("Podaj długość pierwszego boku: "))
                    b = float(input("Podaj długość drugiego boku: "))
                    print("Obwód:", a * 2 + b * 2)
                elif info2 == 11:
                    a = float(input("Podaj długość pierwszego boku: "))
                    b = float(input("Podaj długość drugiego boku: "))
                    c = float(input("Podaj wysokość: "))
                    print("Objętość:", a * b * c)
                elif info2 == 12:
                    a = float(input("Podaj długość pierwszego boku: "))
                    b = float(input("Podaj długość drugiego boku: "))
                    c = float(input("Podaj wysokość: "))
                    print("Pole całości:", 2 * (a * b + a * c + b * c))
                elif info2 == 13:
                    a = float(input("Podaj długość podstawy: "))
                    b = float(input("Podaj wysokość: "))
                    print("Pole:", (a * b) / 2)
                elif info2 == 14:
                    a = float(input("Podaj długość pierwszego boku: "))
                    b = float(input("Podaj długość drugiego boku: "))
                    c = float(input("Podaj długość trzeciego boku: "))
                    print("Obwód:", a + b + c)
                elif info2 == 15:
                    stop2 = False
                else:
                    print("                                                !!!ERROR!!!")
        elif info == 8:
            while stop3:
                print("")
                print("")
                print(
                    "________________________________________________________Wzory________________________________________________________")
                print("                                                  1.Pole, obwód koła")
                print("                                           2.Objętość, pole całości walca")
                print("                                                  3.Pole, obwód kwadratu")
                print("                                            4.Objętość, pole całości sześcianu")
                print("                                                 5.Pole, obwód prostokąta")
                print("                                        6.Objętość, pole całości Prostopadłościanu")
                print("                                                 7.Pole, obwód trójkąta")
                print("                                                           8.")
                print("                                                           9.")
                print("                                                          10.")
                print("                                                          11.")
                print("                                                          12.")
                print("                                                          13.")
                print("                                                          14.")
                print("                                                       15.Powrót")
                print("")
                info3 = int(input("Wybór: "))
                if info3 == 1:
                    print("______Pole koła______")
                    print("P=pi*r^2")
                    print("______Obwód koła_____")
                    print("O=2*pi*r")
                    print("")
                    print("r=promień")
                    print("")
                elif info3 == 2:
                    print("____Objętość walca____")
                    print("V=(pi*r^2)*h")
                    print("__Pole całości walca__")
                    print("Ppc=2*pi*r^2+2*pi*r*h")
                    print("")
                    print("r=promień")
                    print("h=Wysokość")
                    print("")
                elif info3 == 3:
                    print("____Pole kwadratu____")
                    print("P=a^2")
                    print("____Obwód Kwadratu___")
                    print("O=a*4")
                    print("")
                    print("a=bok kwadratu")
                    print("")
                elif info3 == 4:
                    print("__Objętość Sześcianu__")
                    print("V=a^3")
                    print("_Pole całośi sześcianu")
                    print("6*a^2")
                    print("")
                    print("a=bok sześcianu")
                    print("")
                elif info3 == 5:
                    print("___Pole prostokąta___")
                    print("P=a*b")
                    print("___Obwód prostokąta__")
                    print("O=a*2+b*2")
                    print("")
                    print("a=pierwszy bok prostokąta")
                    print("b=drugi bok prostokąta")
                    print("")
                elif info3 == 6:
                    print("___Objętość prostopadłościanu___")
                    print("V=a*b*c")
                    print("_Pole całości Prostopadłościanu_")
                    print("Ppc=2*(a*b+a*c+b*c)")
                    print("")
                    print("a=pierwszy bok prostopadłościanu")
                    print("b=drugi bok prostopadłościanu")
                    print("c=trzeci bok prostopadłościanu")
                    print("")
                elif info3 == 7:
                    print("___Pole trójkąta___")
                    print("P=(a*h)/2")
                    print("___Obwód trójkąta__")
                    print("O=a+b+c")
                    print("")
                    print("a=pierwszy bok trujkąta")
                    print("b=drugi bok trójkąta")
                    print("c=trzeci bok trójkąta")
                    print("h=wysokość trójkąta")
                    print("")
                # elif info3 == 8:
                # elif info3 == 9:
                # elif info3 == 10:
                # elif info3 == 11:
                # elif info3 == 12:
                # elif info3 == 13:
                # elif info3 == 14:
                elif info3 == 15:
                    stop3 = False
                else:
                    print("                                                !!!ERROR!!!")
        elif info == 9:
            print("")
            print("")
            print("W budowie!!")
            print("_______________________________________________________________________________________________")
            print("|                     |                                                                       |")
            print("|   Autor:            |                               Krecik                                  |")
            print("|_____________________|_______________________________________________________________________|")
            print("|                     |                                                                       |")
            print("|    Wersja python:   |                              python 3.X                               |")
            print("|_____________________|_______________________________________________________________________|")
            print("|                     |                                                                       |")
            print("| Używane biblioteki: |              sys, time, tqdm, colorama, numpy                         |")
            print("|_____________________|_______________________________________________________________________|")
            print("|                     |                                                                       |")
            print("|       Kontakt:      |  e-mail: milicja@vip.onet.pl                                          |")
            print("|_____________________|_______________________________________________________________________|")
            print("|                                                                                             |")
            print("|                             Znalazłeś błąd, zgłoś go!                                       |")
            print("|_____________________________________________________________________________________________|")
            print("|                                                                                             |")
            print("|                    ", Fore.RED + "!!!WSZELKIE PRAWA ZASTRZEŻONE!!! PRZEZ GRUPĘ KRECIK®", Fore.GREEN+ "                   |")
            print("|_____________________________________________________________________________________________|")
            print("")
            print("")
        elif info == 10:
            stop4=True
            while stop4:

                print(
                    "__________________________________________________________NOTATNIK___________________________________________________________")
                print("")
                print("")
                print("1.Zapis")
                print("2.Odczyt")
                print("3.Usuwanie")
                print("4.Powrót")
                print("")
                print("")
                print("")
                print("")
                print("")
                print("")
                print("")
                print("")
                print("")
                print("")
                print("")
                a = int(input("Wybór: "))
                if a == 1:
                    a = str(input("wpisz zawartość:\n"))
                    plik = open("plik.txt", "a+")
                    plik.write("  "+a+'\n')
                    plik.close()
                elif a == 2:
                    plik = open("plik.txt", "r")
                    plikr=plik.read()
                    plik.close()
                    print("")
                    print("")
                    print("")
                    print(plikr)
                    print("")
                    print("")
                    print("")
                elif a == 3:
                    print("Czyszczenie...", end='')
                    plik = open("plik.txt", "w+")
                    plik.write("")
                    plik.close()
                    time.sleep(2)
                    print("zakończono")
                elif a == 4:
                    stop4 = False
        elif info == 11:
            a = int(input("podaj silnie:"))
            x = 1
            for i in range(a):
                x = (i + 1) * x
            print(x)
        elif info == 12:
            print("Czy na pewno chcesz wyjść?")
            print("1.tak")
            print("2.NIE")
            a = int(input(""))
            if a == 1:
                kropka = 1
                for i in tqdm(range(100)):
                    time.sleep(0.1)
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    if kropka == 1:
                        print("Trwa zamykanie .")
                        print("")
                        print("")
                        print("")
                        print("")
                        print("")
                        kropka += 1
                    elif kropka == 2:
                        print("Trwa zamykanie ..")
                        print("")
                        print("")
                        print("")
                        print("")
                        print("")
                        kropka += 1
                    elif kropka == 3:
                        print("Trwa zamykanie ...")
                        print("")
                        print("")
                        print("")
                        print("")
                        print("")
                        kropka += 1
                    elif kropka == 4:
                        print("Trwa zamykanie ....")
                        print("")
                        print("")
                        print("")
                        print("")
                        print("")
                        kropka += 1
                    elif kropka == 5:
                        print("Trwa zamykanie .....")
                        print("")
                        print("")
                        print("")
                        print("")
                        print("")
                        kropka += 1
                    elif kropka == 6:
                        print("Trwa zamykanie ....")
                        print("")
                        print("")
                        print("")
                        print("")
                        print("")
                        kropka += 1
                    elif kropka == 7:
                        print("Trwa zamykanie ...")
                        print("")
                        print("")
                        print("")
                        print("")
                        print("")
                        kropka += 1
                    elif kropka == 8:
                        print("Trwa zamykanie ..")
                        print("")
                        print("")
                        print("")
                        print("")
                        print("")
                        kropka = 1
                sys.exit()
            elif a == 2:
                print("I to rozumiem  :)")
        #elif info == 12:
        else:
            print("                                                !!!ERROR!!!")
except Exception:

    while blad1:
        print(Fore.RED + Back.GREEN + "                                              !!!   KRYTYCZNY BŁĄD SYSTEMU  !!!")
        blad += 1
        if blad == 1000000:
            blad1 = False
