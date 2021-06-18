import random
import secrets

def passGenerieren():
    buchstabenGroß = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    buchstabenKlein = "abcdefghijklmnopqrstuvwxyz"

    zeichen = "^!§$%&/()=?``'_:;“¬”#£ﬁ^^˜\·˜¯˙˚’—÷˛,.-#+<>≥¯˛÷—’˚≠˙¯·˜˜\^^£#”¬“¿'≠}{|][¢¶“¡±‘–…∞µ"
    pw = ""
    laenge = int(input("Bitte geben Sie die Länge des Passwortes ein: "))
    großbuchstaben = int(input("Bitte geben Sie die Anzahl der Großbuchstaben ein: "))
    kleinbuchstaben = int(input("Bitte geben Sie die Anzahl der Kleinbuchstaben ein: "))
    sonderzeichen = int(input("Bitte geben Sie die Anzahl der Sonderzeichen ein: "))
    # for _ in range(laenge):
    # pw = pw + secrets.choice(pw)

    for _ in range(großbuchstaben):
        pw = pw + random.choice(buchstabenGroß)
    for _ in range(kleinbuchstaben):
        pw = pw + random.choice(buchstabenKlein)
    for _ in range(sonderzeichen):
        pw = pw + random.choice(zeichen)
    for _ in range(laenge-(großbuchstaben+kleinbuchstaben+sonderzeichen)):
        pw = pw + str(random.randint(0,9))

    print(pw)

def lösch_passwort():
    altpasswort=input("Altes Passwort: ")
    beschtätigung=input("möchten Sie das Passwort sicherlich löschen? [y/n]")
    if beschtätigung == "y":
        passwort=""
    else:
        pass


def pass_ändern():
    altpass=input("Altes Passwort: ")
    neupass=input("neues Passwort: ")
    return neupass

print("Willkommen beim Passwort-Manager")

choices = {
    1: "Anschau der Passwörter",
    2: "Neues Passwort hinzufügen",
    3: "Passwort ändern",
    4: "Passwort löschen"
}
input("Bitte geben Sie den Namen der Webseite an: ")
input("Bitte geben Sie Ihren Benutzernamen ein: ")

print("Bitte wählen Sie eines der folgenden Möglichkeiten aus: ")
print(choices)

möglichkeit = int(input("Möglichkeit: "))
if möglichkeit == 1:
  print("")
elif möglichkeit == 2:

    frage=input("möchten Sie ein neues Passwort generieren lassen oder Ihr eingenes eingeben? [g/e]")
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


