

# ============================================
# KONTAKT-OPERATIONEN
# ============================================

from kontakt_helfer import (
    kontakte_laden, kontakte_speichern,
    ist_gueltige_telefonnummer, ist_gueltige_email,
    eingabe_mit_wiederholung
)

def kontakt_hinzufuegen():
    """Fügt einen neuen Kontakt hinzu."""
    print("\n" + "=" * 50)
    print("NEUEN KONTAKT HINZUFÜGEN")
    print("=" * 50)
    try:
        name = ""
        while not name:
            name = input("Name: ").strip()
            if not name:
                print("[X] Name darf nicht leer sein!")

        telefon = eingabe_mit_wiederholung(
            "Telefonnummer: ",
            ist_gueltige_telefonnummer,
            "[X] Ungültige Telefonnummer! Es sind nur Zahlen erlaubt und das Feld darf nicht leer sein.",
            optional=False,
        )

        email = eingabe_mit_wiederholung(
            "E-Mail-Adresse (optional): ",
            ist_gueltige_email,
            "[X] Ungültige E-Mail-Adresse! Wenn eine E-Mail eingegeben wird, muss sie ein '@' enthalten.",
            optional=True,
        )

        adresse = input("Adresse (optional): ").strip()

        kontakte = kontakte_laden()
        kontakte.append(
            {"name": name, "telefon": telefon, "email": email, "adresse": adresse}
        )

        if kontakte_speichern(kontakte):
            print(f'\n[OK] Kontakt "{name}" erfolgreich gespeichert!')

    except KeyboardInterrupt:
        print("\nAbgebrochen.")
    except Exception as e:
        print(f"[FEHLER] Fehler: {e}")


def kontakte_anzeigen():
    """Zeigt alle Kontakte an."""
    kontakte = kontakte_laden()
    print("\n" + "=" * 50)
    print(f"ALLE KONTAKTE ({len(kontakte)} im System)")
    print("=" * 50)

    if not kontakte:
        print("Keine Kontakte vorhanden.")
        input("\nDrücken Sie Enter, um zum Menü zurückzukehren...")
        return

    for i, kontakt in enumerate(kontakte, start=1):
        print(f"\n{i}. Name: {kontakt['name']}")
        print(f"   Telefon: {kontakt['telefon']}")
        print(f"   E-Mail: {kontakt['email']}")
        print(f"   Adresse: {kontakt['adresse']}")
    input("\nDrücken Sie Enter, um zum Menü zurückzukehren...")


def kontakt_suchen():
    """Sucht nach Kontakten anhand eines Suchbegriffs (Name, Telefon, E-Mail, Adresse)."""
    kontakte = kontakte_laden()
    if not kontakte:
        print("\nKeine Kontakte vorhanden.")
        input("\nDrücken Sie Enter, um zum Menü zurückzukehren...")
        return

    print("\n" + "=" * 50)
    print("KONTAKT SUCHE")
    print("=" * 50)
    suchbegriff = input("Suchbegriff (Name/Telefon/E-Mail/Adresse): ").strip()
    if not suchbegriff:
        print("[X] Suchbegriff darf nicht leer sein.")
        return

    suchbegriff_lower = suchbegriff.lower()
    treffer = []
    for kontakt in kontakte:
        if (
            suchbegriff_lower in kontakt["name"].lower()
            or suchbegriff_lower in kontakt["telefon"].lower()
            or suchbegriff_lower in kontakt["email"].lower()
            or suchbegriff_lower in kontakt["adresse"].lower()
        ):
            treffer.append(kontakt)

    print(f"\nErgebnisse für '{suchbegriff}': {len(treffer)} Treffer")
    if not treffer:
        print("Keine passenden Kontakte gefunden.")
    else:
        for i, k in enumerate(treffer, start=1):
            print(f"\n{i}. {k['name']}")
            print(f"   Telefon: {k['telefon']}")
            print(f"   E-Mail: {k['email']}")
            print(f"   Adresse: {k['adresse']}")
    input("\nDrücken Sie Enter, um zum Menü zurückzukehren...")


def kontakt_aktualisieren():
    """Aktualisiert einen bestehenden Kontakt."""
    kontakte = kontakte_laden()
    if not kontakte:
        print("\nKeine Kontakte vorhanden.")
        input("\nDrücken Sie Enter, um zum Menü zurückzukehren...")
        return

    print("\n" + "=" * 50)
    print("KONTAKT AKTUALISIEREN")
    print("=" * 50)
    for i, kontakt in enumerate(kontakte, start=1):
        print(f"{i}. {kontakt['name']}")

    try:
        nr = int(input("\nKontakt-Nummer: "))
        if 1 <= nr <= len(kontakte):
            kontakt = kontakte[nr - 1]

            print(f"\n--- Aktueller Kontakt ---")
            print(f"Name: {kontakt['name']}")
            print(f"Telefon: {kontakt['telefon']}")
            print(f"E-Mail: {kontakt['email']}")
            print(f"Adresse: {kontakt['adresse']}")

            # Neuer Name (optional)
            neuer_name = input("Neuer Name (Enter = unverändert): ").strip()
            if neuer_name:
                kontakt["name"] = neuer_name

            # Neue Telefonnummer (optional, aber wenn eingegeben muss sie gültig sein)
            while True:
                neue_telefon = input("Neue Telefonnummer (Enter = unverändert): ").strip()
                if neue_telefon == "":
                    break  # unverändert
                if ist_gueltige_telefonnummer(neue_telefon):
                    kontakt["telefon"] = neue_telefon
                    break
                print("[X] Ungültige Telefonnummer! Es sind nur Zahlen erlaubt und das Feld darf nicht leer sein.")

            # Neue E-Mail (optional, aber wenn eingegeben muss sie ein '@' enthalten)
            while True:
                neue_email = input("Neue E-Mail (Enter = unverändert): ").strip()
                if neue_email == "":
                    break  # unverändert
                if ist_gueltige_email(neue_email):
                    kontakt["email"] = neue_email
                    break
                print("[X] Ungültige E-Mail-Adresse! Wenn eine E-Mail eingegeben wird, muss sie ein '@' enthalten.")

            neue_adresse = input("Neue Adresse (Enter = unverändert): ").strip()
            if neue_adresse:
                kontakt["adresse"] = neue_adresse

            if kontakte_speichern(kontakte):
                print(f"\n[OK] Kontakt erfolgreich aktualisiert!")
        else:
            print("[X] Ungültige Nummer!")

    except ValueError:
        print("[X] Bitte eine Zahl eingeben!")
    except Exception as e:
        print(f"[X] Fehler: {e}")


def kontakt_loeschen():
    """Löscht einen Kontakt."""
    kontakte = kontakte_laden()
    if not kontakte:
        print("\nKeine Kontakte vorhanden.")
        input("\nDrücken Sie Enter, um zum Menü zurückzukehren...")
        return

    print("\n" + "=" * 50)
    print("KONTAKT LÖSCHEN")
    print("=" * 50)
    for i, kontakt in enumerate(kontakte, start=1):
        print(f"{i}. {kontakt['name']} ({kontakt['telefon']})")

    try:
        nr = int(input("\nKontakt-Nummer: "))
        if 1 <= nr <= len(kontakte):
            kontakt = kontakte[nr - 1]

            # Schleife für die j/n-Eingabe
            while True:
                antwort = input(f'Wirklich "{kontakt["name"]}" löschen? (j/n): ').strip().lower()

                if antwort == "j":
                    kontakte.pop(nr - 1)
                    if kontakte_speichern(kontakte):
                        print("\n[OK] Kontakt erfolgreich gelöscht!")
                    break
                elif antwort == "n":
                    print("Löschen abgebrochen.")
                    break
                else:
                    print('[X] Ungültige Eingabe! Nur "j" oder "n" möglich!')

        else:
            print("[X] Ungültige Nummer!")
    except ValueError:
        print("[X] Bitte eine Zahl eingeben!")
    except Exception as e:
        print(f"[X] Fehler: {e}")


