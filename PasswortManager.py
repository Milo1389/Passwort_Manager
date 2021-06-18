import random
import string

def lösch_passwort():
    username = str(input("Username: "))
    titel = input("Titel : ")
    passwort=input("Passwort: ")
    m=int(input("möchten Sie das Passwort löschen oder ändern? 1.löschen 2.ändern"))
    if m==1:
        beschtätigung=input("möchten Sie das Passwort sicherlich löschen? zum beschtätigen 1 eingeben")
        if beschtätigung==1:
            passwort=""
        else:
            pass
    elif m==2:
        passwort=input("Geben Sie das neue Passwort ein")
lösch_passwort()









