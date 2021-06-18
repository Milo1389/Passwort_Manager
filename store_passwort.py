import random
import string
import pprint
def store_passwort():
    username= str(input("Username: "))
    titel= input("Titel : ")
    passwort = str(input("Haben Sie ein Passwort? schreiben Sie P; möchten Sie ein neues Passwort generieren? schreiben Sie G :"))
    passwort.lower()
    passw = ""
    if passwort == "g":
            länge = int(input("wie lang soll das Passwort sein: "))
            gros= input("Soll das Passwort Großbuchstaben enthalten? [y/n]:")
            if gros=="y":
                gros1=int(input("wie viele Größbuchstaben möchten Sie"))
                for i in range(gros1):
                    charg = random.choice(string.ascii_uppercase)
                    passw += charg
                else:
                    pass
            klein= input("Soll das Passwort Sonderzeichen enthalten?: [y/n]:")
            if klein=="y":
                klein1 = int(input("wie viele Kleinbuchstaben möchten Sie"))
                for j in range(klein1):
                    chark = random.choice(string.ascii_lowercase)
                    passw += chark
            zahl= input("Soll das Passwort Zahlen enthalten?: [y/n]: ")
            for x in range(länge):
                chari=random.randint(0,9)
                passw +=chari
            print(passw)
    else :
        passw=input("Passwort: ")


store_passwort()