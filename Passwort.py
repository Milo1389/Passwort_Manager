import random
import secrets
import string


def pruefGrosBuchstaben(grosbuchstaben,laenge):

    while int(grosbuchstaben) > laenge:
            grosbuchstaben = input("Die Anzahl der Großbuchstaben muss kürzer als die Länge sein"
                                       ", bitte geben Sie nochmals die Anzahl der Großbuchstaben ein, wenn Sie aus dem programm raus gehen wollen schreiben Sie off")
            if not grosbuchstaben.isnumeric() :
                return 0
            elif int(grosbuchstaben) < laenge:
                return grosbuchstaben
    return grosbuchstaben
def pruefKleinBuchstaben(kleinbuchstaben,laenge,grosbuchstaben):

        while int(kleinbuchstaben) > laenge or (int(grosbuchstaben) + int(kleinbuchstaben)) > laenge:
            kleinbuchstaben = input("Die Anzahl der Kleinbuchstaben muss kürzer als die Länge sein"
                                        ", bitte geben Sie nochmals die Anzahl der Kleinbuchstaben ein, wenn Sie aus dem Programm raus gehen wollen schreiben sie off")
            if not kleinbuchstaben.isnumeric():
                break
            elif int(kleinbuchstaben)<laenge:
                return kleinbuchstaben
        return kleinbuchstaben

def pruefSonderZeichen(sonderzeichen,laenge,grosbuchstaben,kleinbuchstaben):
        while int(sonderzeichen) > laenge or (int(grosbuchstaben) + int(kleinbuchstaben) + int(sonderzeichen)) > laenge:
            sonderzeichen = input("Die Anzahl der Sonderzeichen muss kürzer als die Länge sein"
                                      ", bitte geben Sie nochmals die Anzahl der Sonderzeichen ein,wenn Sie aus dem Programm raus gehen wollen schreiben sie off")
            if not sonderzeichen.isnumeric():
                break
            elif int(sonderzeichen)<laenge:
                return sonderzeichen
        return sonderzeichen

def passGenerieren():
    buchstabenGroß = string.ascii_uppercase

    buchstabenKlein = string.ascii_lowercase

    zeichen = "^!§$%&/()=?``'_:;“¬”#£ﬁ^^˜\·˜¯˙˚’—÷˛,.-#+<>≥¯˛÷—’˚≠˙¯·˜˜\^^£#”¬“¿'≠}{|][¢¶“¡±‘–…∞µ"
    pw = ""

    laenge = int(input("Bitte geben Sie die Länge des Passwortes ein: "))
    grosbuchstaben = int(input("Bitte geben Sie die Anzahl der Großbuchstaben ein: "))
    grosbuchstaben=int(pruefGrosBuchstaben(grosbuchstaben,laenge))
    pw = pw + (''.join(secrets.choice(buchstabenGroß) for _ in range (grosbuchstaben)))
    kleinbuchstaben = int(input("Bitte geben Sie die Anzahl der Kleinbuchstaben ein: "))
    kleinbuchstaben=int(pruefKleinBuchstaben(kleinbuchstaben,laenge,grosbuchstaben))

    pw = pw + (''.join(secrets.choice(buchstabenKlein) for _ in range (kleinbuchstaben)))
    sonderzeichen = int(input("Bitte geben Sie die Anzahl der Sonderzeichen ein: "))
    sonderzeichen=int(pruefSonderZeichen(sonderzeichen,laenge,grosbuchstaben,kleinbuchstaben))
    pw = pw + (''.join(secrets.choice(zeichen) for _ in range (sonderzeichen)))
    #file.txt

    digit=string.digits
    pw = pw + (''.join(secrets.choice(digit) for _ in range(laenge-(grosbuchstaben+kleinbuchstaben+sonderzeichen))))

    print(pw)



def lösch_passwort():
    altpasswort=input("Altes Passwort: ")
    beschtätigung=input("Möchten Sie das Passwort sicherlich löschen? [y/n]")
    if beschtätigung == "y":
        passwort=""
        #file.txt
    else:
        pass


def pass_ändern():
    altpass=input("Altes Passwort: ")
    neupass=input("neues Passwort: ")
    #file.txt
    return neupass

def anschauPasswort():
    print("")
    #mitOracleVerbinden-print()


print("Willkommen beim Passwort-Manager")

choices = {
    1: " Anschau der Passwörter" ,
    2: " Neues Passwort hinzufügen" ,
    3: " Passwort ändern" ,
    4: " Passwort löschen"
}
#Master Passwort
mp= input("Bitte geben Sie ein Masterpasswort für Ihren Passwort Manager ein: ")

EingabeMp = input("Bitte geben Sie nun Ihren Masterpasswort ein: ")

if str(EingabeMp) == mp:
    print("Die Eingabe war korrekt.")
    print("Bitte wählen Sie eines der folgenden Möglichkeiten aus: ")
    for key, value in choices.items():
        print(str(key) + ":" + value)

auswahl = int(input("Ihre gewünschte Auswahl : "))

input("Bitte geben Sie den Namen der Webseite an: ").lower()
#.lower() dient dazu, falls der Benutzer den Namen der Webseite groß schreiben sollte
#und Python erkennt, um welche Webseite es sich hier handelt
input("Bitte geben Sie Ihren Benutzernamen ein: ")


möglichkeit = auswahl
if möglichkeit == 1:
  print("")
elif möglichkeit == 2:

    frage=input("Möchten Sie ein neues Passwort generieren lassen oder Ihr eingenes eingeben? [g/e]")
    if frage == "g":
        passGenerieren()
    elif frage =="e":
        input("Bitte geben Sie Ihr Passwort ein")

elif möglichkeit == 3:
    pass_änder()

elif möglichkeit == 4:
    lösch_passwort()

else:
    print("Sie haben eine ungültige Eingabe getätigt.")