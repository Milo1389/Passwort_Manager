# Yildiz Zehra, Milutinovic Petar, Zahra Mechershavi
from datetime import datetime
import getopt
import secrets
import string
import time
from threading import Thread

import pyperclip
import sys
import os

import stdiomask

websites = []
usernames = []
passwords = []
masterPasswort = ""
startTime = datetime.now()


# Hier wird nach dem Masterpasswort abgefragt
# wir wählten 600 Sekunden, also 10 Minuten aus
# Wir setzten als Bedingung die aktuelle Softwarezeit (datetime.now) ein
# und subtrahierten das mit der Startzeit (startTime).
# Ergebnis wandelten wir in Sekunden um

def checkIfMasterIsneeded():
    if (datetime.now() - startTime).total_seconds() > 600:
        askMaster = input("Please write MP: ")
        if askMaster == masterPasswort:
            print("Richtig")
        else:
            print("Falsch")
            sys.exit(0)
            # damit durch die falsche Eingabe das Programm geschlossen wird, benutzen wir hier
            # sys.exit(0)

# um das Passwort in der Zwischenablage kopieren zu können, benutzen wir pyperclip
# dafür mussten wir pyperclip importieren, sowie im Terminal: pip install pyperclip angeben
# das Passwort bleibt für 30Sek in der Zwischenablage, danach wird es geleert
def startDeleteTimer():
    def deletePassword():
        time.sleep(30)
        pyperclip.copy("")
        print("Zwischenablage geleert")

    thread = Thread(target=deletePassword)
    thread.start()


def readPasswords():
    try:
        file = open('password.txt', 'r')
        lines = file.readlines()
        # wir lesen die file hier

        for index, line in enumerate(lines):
            userdata = line.split(';')
            websites.append(userdata[0].split(" ")[2])
            usernames.append(userdata[1].split(" ")[2])
            passwords.append(userdata[2].split(" ")[2].replace('\n', ''))
        # damit die Information in der File geordnet bleibt, haben wir es strukturiert
        file.close()
    except:
        #Datei existiert nicht, vllt erster start
        pass;
# dient zur Speicherung der Daten von der Benutezreingabe
# 'a' beim File = daten hinzufügen
# hier geht es um das Speichern des generierten Passwortes
def rewriteFile():
    os.remove('password.txt')
    outfile = open('password.txt', 'a')
    for i in range(len(websites)):
        outfile.write(f" Webseite: {websites[i]} ; Benutzername: {usernames[i]} ; Passwort: {str(passwords[i])}\n")
    readPasswords()

# dient zur Speicherung der Daten von der Benutezreingabe
# 'a' beim File = daten hinzufügen
# hier geht es um das Speichern des generierten Passwortes
def fe(ws, bn, eigenes_passwort):
    outfile = open('password.txt', 'a')
    outfile.write(f" Webseite: {ws} ; Benutzername: {bn} ; Passwort: {str(eigenes_passwort)}\n")
    readPasswords()

#falls die Länge länger ist, als die Anzahl der summierten Groß- und Kleinbuchstaben, sowie Sondrzeichen
#wenn es nicht übereinstimmt, wird der Benutzer gefordert es nochmal neu anzugeben
def pruefGrosBuchstaben(grosbuchstaben, laenge):
    while int(grosbuchstaben) > laenge:
        grosbuchstaben = input("Die Anzahl der Großbuchstaben muss kürzer als die Länge sein"
                               ", bitte geben Sie nochmals die Anzahl der Großbuchstaben ein, wenn Sie aus dem programm raus gehen wollen schreiben Sie off")
        if not grosbuchstaben.isnumeric():
            return 0
        elif int(grosbuchstaben) < laenge:
            return grosbuchstaben
    return grosbuchstaben

#falls die Länge länger ist, als die Anzahl der summierten Groß- und Kleinbuchstaben, sowie Sondrzeichen
#wenn es nicht übereinstimmt, wird der Benutzer gefordert es nochmal neu anzugeben
def pruefKleinBuchstaben(kleinbuchstaben, laenge, grosbuchstaben):
    while int(kleinbuchstaben) > laenge or (int(grosbuchstaben) + int(kleinbuchstaben)) > laenge:
        kleinbuchstaben = input("Die Anzahl der Kleinbuchstaben muss kürzer als die Länge sein"
                                ", bitte geben Sie nochmals die Anzahl der Kleinbuchstaben ein, wenn Sie aus dem Programm raus gehen wollen schreiben sie off")
        if not kleinbuchstaben.isnumeric():
            break
        elif int(kleinbuchstaben) < laenge:
            return kleinbuchstaben
    return kleinbuchstaben

#falls die Länge länger ist, als die Anzahl der summierten Groß- und Kleinbuchstaben, sowie Sondrzeichen
#wenn es nicht übereinstimmt, wird der Benutzer gefordert es nochmal neu anzugeben
def pruefSonderZeichen(sonderzeichen, laenge, grosbuchstaben, kleinbuchstaben):
    while int(sonderzeichen) > laenge or (int(grosbuchstaben) + int(kleinbuchstaben) + int(sonderzeichen)) > laenge:
        sonderzeichen = input("Die Anzahl der Sonderzeichen muss kürzer als die Länge sein"
                              ", bitte geben Sie nochmals die Anzahl der Sonderzeichen ein,wenn Sie aus dem Programm raus gehen wollen schreiben sie off")
        if not sonderzeichen.isnumeric():
            break
        elif int(sonderzeichen) < laenge:
            return sonderzeichen
    return sonderzeichen

#hier wird das Passwort generiert
#dazu haben wir die Groß- und Kleinbuchstaben, sowie Sonderzeichen
def passGenerieren():
    buchstabenGross = string.ascii_uppercase

    buchstabenKlein = string.ascii_lowercase

    zeichen = "^!§$%&/()=?``'_:;“¬”#£ﬁ^^˜\·˜¯˙˚’—÷˛,.-#+<>≥¯˛÷—’˚≠˙¯·˜˜\^^£#”¬“¿'≠}{|][¢¶“¡±‘–…∞µ"
    pw = ""
    # Hier muss der Benutzer eingeben, wie viele Groß-und Kleinbuchstaben, sowie Sonderzeichen er haben möchte
    # Programmt wählt durch die Funktion secrets.choice zufällige Zeichen aus
    # und es wird zusammengefügt alles
    laenge = int(input("Bitte geben Sie die Länge des Passwortes ein: "))
    grosbuchstaben = int(input("Bitte geben Sie die Anzahl der Großbuchstaben ein: "))
    grosbuchstaben = int(pruefGrosBuchstaben(grosbuchstaben, laenge))
    pw = pw + (''.join(secrets.choice(buchstabenGross) for _ in range(grosbuchstaben)))
    kleinbuchstaben = int(input("Bitte geben Sie die Anzahl der Kleinbuchstaben ein: "))
    kleinbuchstaben = int(pruefKleinBuchstaben(kleinbuchstaben, laenge, grosbuchstaben))

    pw = pw + (''.join(secrets.choice(buchstabenKlein) for _ in range(kleinbuchstaben)))
    sonderzeichen = int(input("Bitte geben Sie die Anzahl der Sonderzeichen ein: "))
    sonderzeichen = int(pruefSonderZeichen(sonderzeichen, laenge, grosbuchstaben, kleinbuchstaben))
    pw = pw + (''.join(secrets.choice(zeichen) for _ in range(sonderzeichen)))
    # file.txt

    digit = string.digits
    pw = pw + (
        ''.join(secrets.choice(digit) for _ in range(laenge - (grosbuchstaben + kleinbuchstaben + sonderzeichen))))

    print(pw)
    # pyperclip speichert das Passwort in die Zwischenablage ab
    pyperclip.copy(pw)
    print("Dein erstelltes Passwort wurde im Clipboard gespeichert. ")
    return pw


def autoPassGenerieren():
    buchstabenGross = string.ascii_uppercase

    buchstabenKlein = string.ascii_lowercase

    zeichen = "^!§$%&/()=?``'_:;“¬”#£ﬁ^^˜\·˜¯˙˚’—÷˛,.-#+<>≥¯˛÷—’˚≠˙¯·˜˜\^^£#”¬“¿'≠}{|][¢¶“¡±‘–…∞µ"
    pw = ""

    laenge = 12
    grosbuchstaben = int(pruefGrosBuchstaben(4, laenge))
    pw = pw + (''.join(secrets.choice(buchstabenGross) for _ in range(grosbuchstaben)))
    kleinbuchstaben = int(pruefKleinBuchstaben(4, laenge, grosbuchstaben))

    pw = pw + (''.join(secrets.choice(buchstabenKlein) for _ in range(kleinbuchstaben)))
    sonderzeichen = int(pruefSonderZeichen(4, laenge, grosbuchstaben, kleinbuchstaben))
    pw = pw + (''.join(secrets.choice(zeichen) for _ in range(sonderzeichen)))
    # file.txt

    digit = string.digits
    pw = pw + (
        ''.join(secrets.choice(digit) for _ in range(laenge - (grosbuchstaben + kleinbuchstaben + sonderzeichen))))

    pyperclip.copy(pw)
    print("Dein erstelltes Passwort wurde im Clipboard gespeichert. ")  # VERBESSERN
    return pw

# 3, wegen Title, Username & Password
def main(argv):
    if len(argv) < 3:
        print("Kein Aufruf mit Argumenten")
        print("Willkommen beim Passwort-Manager")
        # hier wird nach dem Masterpasswort gefragt
        # kommt eine wiederholte abfrage
        # Programm vergleicht diese
        # falls es richtig ist, läuft das Programm

        mp = stdiomask.getpass("Bitte geben Sie ein Masterpasswort für Ihren Passwort Manager ein: ")
        global masterPasswort
        masterPasswort = mp
        EingabeMp = stdiomask.getpass("Bitte geben Sie nun Ihr Masterpasswort ein: ")

        while mp != EingabeMp:
            if mp != EingabeMp:
                print(("Falsches Passwort! "))
                break
        if mp == EingabeMp:
            print("Die Eingabe war korrekt." + '\n')
            print("Bitte wählen Sie eines der folgenden Möglichkeiten aus: ")
            # wir erstellten 5 Möglichkeiten für den Benutzer, die er frei wählen kann
            while True:
                print("Auswahl 1: Sichtbarkeit Passwörterr")
                print("Auswahl 2: Passwort generieren")
                print("Auswahl 3: Passwort löschen")
                print("Auswahl 4: Psswort ändern")
                print("Auswahl 5: Beenden")
                auswahl = int(input("Ihre gewünschte Auswahl : "))
                moeglichkeit = auswahl
                if moeglichkeit == 1:
                    checkIfMasterIsneeded()
                    with open('password.txt', 'r') as f:
                        f_contents = f.read()
                        print(f_contents + '\n')
                        # Hier kann der Benutzer sich seine Passwörter anschauen
                        # dafür wird die File gelesen

                elif moeglichkeit == 2:
                    checkIfMasterIsneeded()
                    ws = input("Bitte geben Sie den Namen der Webseite an: ").lower()
                    bn = input("Bitte geben Sie Ihren Benutzernamen ein: ")
                    frage = input("Möchten Sie ein neues Passwort generieren lassen oder Ihr eingenes eingeben? [g/e]")
                    if frage == "g":
                        generiertes_passwort = passGenerieren()
                        fe(ws, bn, generiertes_passwort)
                    elif frage == "e":
                        eigenes_passwort = input("Bitte geben Sie Ihr Passwort ein: ")
                        pyperclip.copy(eigenes_passwort)
                        print("Dein erstelltes Passwort wurde im Clipboard gespeichert. ")
                        fe(ws, bn, eigenes_passwort)
                    startDeleteTimer();
                    # hier kann der Benutzer ein neues Passwort hinzufügen
                    # kann sich auswählen, ob das Programm eins für ihn generiert
                    # oder er selbst eins erstellt
                    # die Passwörter werden dann in der File datei gespeichert


                elif moeglichkeit == 3:
                    checkIfMasterIsneeded()
                    print("Passwort loeschen:")
                    websiteZuLoeschen = input("Website?:")
                    auswahlSicher = input("Sicher? J/N")
                    if auswahlSicher.lower() == "j":
                        elementAnStelle = -1
                        for i in range(len(websites)):
                            if websites[i].lower() == websiteZuLoeschen.lower():
                                websites.pop(i)
                                usernames.pop(i)
                                passwords.pop(i)
                                rewriteFile()
                                elementAnStelle = i
                                break
                        if elementAnStelle == -1:
                            print("Eintrag nicht gefunden")
                        else:
                            print("Eintrag geloescht")
                            # Funktion, um Passwort löschen zu können
                            # Nutzer soll die Webseite angeben, die gemeinsam mit dem Passwort gelöscht wird
                            # For schleife erstellt, damit das gesuchte Element an der i-Schleife gelöscht wird

                elif moeglichkeit == 4:
                    checkIfMasterIsneeded()
                    print("Passwort Aendern:")
                    passwrdAenderung = input("Website?:")
                    elementAnStelle = -1
                    for i in range(len(websites)):
                        if websites[i].lower() == passwrdAenderung.lower():
                            elementAnStelle = i
                            break
                    if elementAnStelle == -1:
                        print("Eintrag nicht gefunden")
                    else:
                        neuesPasswort = input("Bitte geben Sie das neue Passwort ein: ")
                        passwords[elementAnStelle] = neuesPasswort
                        print("Passwort geandert")
                        rewriteFile()
                        # Funktion, um Passwort ändern zu können
                        # Nutzer soll die Webseite angeben, damit man da das Passwort ändern kann
                        # For schleife erstellt, damit das gesuchte Element an der i-Schleife geändert wird

                elif moeglichkeit == 5:
                    print("Auf Wiedersehen!")
                    exit()
                    # hier kann der Nutzer das Programm beenden



                else:
                    print("Sie haben eine ungültige Eingabe getätigt")
                    # Falls der Nutzer was anders statt den Zahlen 1-5 eingibt
    else:
        # Eingabestrings normieren zum vergleich
        if argv[0].lower() == "add":
            if len(argv) != 6:
                # 6 Parameter=> damit man sich an add -title moodle -username -generatepassword orientiert
                print("Parameter Fehlt")
                print("Bitte folgendes Schema benutzen:")
                print("password_manager.py Add -title <Title> -username <Username> -generatepassword")
                sys.exit(0)
            title = ""
            username = ""
            generatedpassword = False
            for i in range(1, len(argv)):
                if argv[i] == "-title":
                    try:
                        title = argv[i + 1]
                    except:
                        pass
                elif argv[i] == "-username":
                    try:
                        username = argv[i + 1]
                    except:
                        pass
                elif argv[i] == "-generatepassword":
                    generatedpassword = True

            if title == "" or username == "" or generatedpassword == False:
                print("Falsche eingabe")
                sys.exit(0)
            else:
                print("Ausgewaehlte Title: " + title)
                print("Ausgewaehlte Username: " + username)
                fe(title, username, autoPassGenerieren())
                print("OK password created and copied to clipboard")

        if argv[0].lower() == "copy":
            # 3 wegen title, username, generatepassword
            if len(argv) == 3:
                if argv[1] == "-title":
                    title = argv[2]
                    for i in range(len(websites)):
                        if websites[i].lower() == title.lower():
                            print("Username:" + usernames[i])
                            print("Password:" + passwords[i])
                            pyperclip.copy(passwords[i])
                            print("Password copied to clipboard")

            else:
                print("Parameter Fehlt")
                print("Bitte folgendes Schema benutzen:")
                print("password_manager.py copy -title <Title> ")
                sys.exit(0)


if __name__ == "__main__":
    readPasswords()
    main(sys.argv[1:])
