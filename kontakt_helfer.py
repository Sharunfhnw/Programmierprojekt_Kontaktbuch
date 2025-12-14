# ============================================
# DATEI-OPERATIONEN
# ============================================
def kontakte_laden():
    """Lädt alle Kontakte aus der Datei."""
    kontakte = []
    try:
        with open("kontakte.txt", "r", encoding="utf-8") as datei:
            zeile = datei.readline()
            while zeile != "":
                kontakt = {
                    "name": zeile.rstrip(),
                    "telefon": datei.readline().rstrip(),
                    "email": datei.readline().rstrip(),
                    "adresse": datei.readline().rstrip(),
                }
                kontakte.append(kontakt)
                zeile = datei.readline()
    except FileNotFoundError:
        pass  # Leere Liste, wenn Datei nicht existiert
    except Exception as e:
        print(f"Fehler beim Laden: {e}")
    return kontakte


def kontakte_speichern(kontakte):
    """Speichert alle Kontakte in die Datei."""
    try:
        with open("kontakte.txt", "w", encoding="utf-8") as datei:
            for kontakt in kontakte:
                datei.write(kontakt["name"] + "\n")
                datei.write(kontakt["telefon"] + "\n")
                datei.write(kontakt["email"] + "\n")
                datei.write(kontakt["adresse"] + "\n")
        return True
    except IOError as e:
        print(f"Fehler beim Speichern: {e}")
        return False


# ============================================
# HILFSFUNKTIONEN
# ============================================
def ist_gueltige_telefonnummer(telefon):
    """Prüft, ob die Telefonnummer nur aus Ziffern besteht und nicht leer ist."""
    return bool(telefon) and telefon.isdigit()


def ist_gueltige_email(email):
    """Einfache Prüfung: wenn nicht leer, muss ein '@' enthalten sein."""
    if email == "":
        return True  # optional erlaubt
    return "@" in email


def eingabe_mit_wiederholung(prompt, pruef_funktion, fehlermeldung, optional=False):
    """
    Allgemeine Eingabe mit Wiederholung:
    - prompt: Eingabeaufforderung
    - pruef_funktion: Funktion, die True für gültige Eingabe zurückgibt
    - fehlermeldung: Text, der bei ungültiger Eingabe gezeigt wird
    - optional: wenn True, ist leere Eingabe erlaubt (liefert "")
    """
    while True:
        wert = input(prompt).strip()
        if optional and wert == "":
            return ""
        if pruef_funktion(wert):
            return wert
        print(fehlermeldung)
