import random
import string

def lösch_passwort():
    username = str(input("Username: "))
    titel = input("Titel : ")
    passwort=input("Passwort: ")
    m=int(input("Möchten Sie das Passwort löschen oder ändern? 1.Löschen 2.Ändern"))
    if m==1:
        bestätigung=input("Möchten Sie das Passwort wirklich löschen? Zum bestätigen bitte 1 eingeben")
        if bestätigung == 1:
            passwort=""
        else:
            pass
    elif m == 2:
        passwort = input("Geben Sie das neue Passwort ein")
lösch_passwort()









