import random
import secrets
import string
import pyperclip
#pyperclip muss importiert, aber auch installiert werden. Dafür muss man im Terminal: pip install pyperclip eingeben

from threading import Timer
#Damit man auf den Timer zugreifen kann, bin mir nicht sicher ob man es
#beim Terminal installieren muss also: pip install timer

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

    pyperclip.copy(pw)
    print("Dein erstelltes Passwort wurde im Clipboard gespeichert. ")
    #damit das generierte Passwort in der Zwischenablage gespeichert ist
    #muss nur noch für 30sek gespeichert werden

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

#Master Passwort
#Als allererstes wird von dem Benutzer befohlen einen Masterpasswort zu erstellen
# nach der Erstellung wird nach dem Masterpasswort wieder gefragt
# Falls der Nutzer die korrekte Eingabe tätigt, wird Ihnen die 5 verfügbaren Möglichkeiten zur Auswahl gelegt
mp= input("Bitte geben Sie ein Masterpasswort für Ihren Passwort Manager ein: ")

EingabeMp = input("Bitte geben Sie nun Ihren Masterpasswort ein: ")

while mp!= EingabeMp:
    if mp != EingabeMp:
        print(("Falsches Passwort! "))
        break
if mp == EingabeMp:
    print("Die Eingabe war korrekt." + '\n')
    print("Bitte wählen Sie eines der folgenden Möglichkeiten aus: ")

    while True:
        print("Press 1: Anschau Passwörter")
        print("Press 2: Passwort generieren")
        print("Press 3: Passwort löschen")
        print("Press 4: Psswort ändern")
        print("Press 5: Beenden")
        auswahl = int(input("Ihre gewünschte Auswahl : "))
        möglichkeit = auswahl
        if möglichkeit ==1:
            with open('password.txt', 'r') as f:
                f_contents = f.read()
                print(f_contents + '\n')
        # Bei der ersten Möglichkeit steht dem Benutzer zur Option sich seine Passwörter anzeigen zu lassen
        # Nach der Abbildung der Passwörter, kann sich die Person sein weiteren Zug auswählen
        elif möglichkeit ==2:
            ws = input("Bitte geben Sie den Namen der Webseite an: ").lower()
            # .lower() dient dazu, falls der Benutzer den Namen der Webseite groß schreiben sollte
            # und Python erkennt, um welche Webseite es sich hier handelt
            bn = input("Bitte geben Sie Ihren Benutzernamen ein: ")
            frage = input("Möchten Sie ein neues Passwort generieren lassen oder Ihr eingenes eingeben? [g/e]")
            if frage == "g":
             passGenerieren()
            elif frage == "e":
             eigenes_passwort = input("Bitte geben Sie Ihr Passwort ein: ")
             pyperclip.copy(eigenes_passwort)
             print("Dein erstelltes Passwort wurde im Clipboard gespeichert. ")



             def fe():
                 outfile = open('password.txt', 'a')
                 outfile.write(f" Webseite: {ws} ; Benutzername: {bn} ; Passwort:  {str(eigenes_passwort)}")

             fe()
        # Bei der zweiten Möglichkeit geht es um das erstellen eines Passwortes
        # Dem Nutzer steht die Auswahl sich das Passwort selbst auszusuchen oder das Programm erledigt es für Ihn.
        # Die Person kann sich sein Passwort nach dem Schema, wie viele Sonderzeichen, Großbuchstaben, Kleinbuchstaben, Zahlen
        # aussuchen
        # Das Passwort,die Webseite und der Benutzername werden dann automatisch in dem File passwort.txt gespeichert
        # Außerdem wird das Passwort noch im Clipboard gespeichert durch die Funktion Pyperclip
        elif möglichkeit == 3:
             ws = input("Bitte geben Sie den Namen der Webseite an: ").lower()
             bn = input("Bitte geben Sie Ihren Benutzernamen ein: ")
             pass_ändern()

        elif möglichkeit == 4:
                ws = input("Bitte geben Sie den Namen der Webseite an: ").lower()
                bn = input("Bitte geben Sie Ihren Benutzernamen ein: ")
                lösch_passwort()

        elif möglichkeit == 5:
                print("Auf Wiedersehen!")
                exit()
        # Zuletzt steht ihm das Verlassen des Programms zur Auswahl
        # Möglichkeit 5 fertig

        else:
                print("Sie haben eine ungültige Eingabe getätigt")

#was alles fehlt:
#1) die Eingaben lesen => fertig, nur noch in die Tabelle einlesen
    # und bei der 2ten Möglichkeit das generierte Passwort einlesen
    #also von der Methode passGenerieren() pw einlesen
#2) Masterpasswort wird nach ner Zeit wieder nachgefragt
#3) das Passwort in eine Zwischenablage speichern => wurde erledigt
# fehlt nur dass es in der Zwischenablage 30sek lang gespeichert bleibt
#4) passwort ändern und löschen
#zahlen fehlen beim Passwort erstellen