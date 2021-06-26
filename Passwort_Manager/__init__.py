from getpass import getpass



benutzername = "milo"
passwort = "apfel123"



bname = input("Gib deinen Benutzernamen ein: ")

if bname != benutzername:
    print("Falscher Benutzername!")
else:
    pwort = getpass.("Gib dein Passwort ein: ")
    if pwort == passwort:
        print("Richtiges Passwort. Sie sind erfolgreich angemeldet!")
    else:
        print("Falsches Passwort!")

textdatei = open("passwortliste.txt", "w")
textdatei.write("Wurde das Textdokument erstellt?")
textdatei.close()
