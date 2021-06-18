import secrets


print("Willkommen beim Passwort-Manager")

choices = {
    1: "Neues Passwort hinzufügen",
    2: "Anschau der Passwörter",
    3: "Passwort ändern",
    4: "Passwort löschen"
}
print("Bitte wählen Sie eines der folgenden Möglichkeiten aus: ")
print(choices)
möglichkeit=int(input("Möglichkeit: "))
if möglichkeit ==1:
    print(input("Bitte geben Sie den Namen der Webseite an: "))
    print(input("Bitte geben Sie Ihren Benutzernamen ein: "))

elif möglichkeit == 2:
    print("hallo")

elif möglichkeit == 3:
    print("ja")

elif möglichkeit ==4:
    print("aka")

else:
    print("Sie haben eine ungültige Eingabe getätigt.")

buchstabenGroß = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

buchstabenKlein = "abcdefghijklmnopqrstuvwxyz"


zeichen = "^!§$%&/()=?``'_:;“¬”#£ﬁ^^˜\·˜¯˙˚’—÷˛,.-#+<>≥¯˛÷—’˚≠˙¯·˜˜\^^£#”¬“¿'≠}{|][¢¶“¡±‘–…∞µ"
pw = ""
laenge= int(input("Bitte geben Sie die Länge des Passwortes ein: "))
großbuchstaben = int(input("Bitte geben Sie die Anzahl der Großbuchstaben ein: "))
kleinbuchstaben = int(input("Bitte geben Sie die Anzahl der Kleinbuchstaben ein: "))
sonderzeichen = int(input("Bitte geben Sie die Anzahl der Sonderzeichen ein: "))
# for _ in range(laenge):
# pw = pw + secrets.choice(pw)

for _ in range(großbuchstaben):
    pw = pw + secrets.choice(buchstabenGroß)
for _ in range(kleinbuchstaben):
    pw = pw + secrets.choice(buchstabenKlein)
for _ in range(sonderzeichen):
    pw = pw + secrets.choice(zeichen)

print(pw)
