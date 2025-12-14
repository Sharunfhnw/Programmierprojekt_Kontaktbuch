# ============================================
# HAUPTPROGRAMM
# ============================================

from kontakt_operationen import (
    kontakt_hinzufuegen,
    kontakte_anzeigen,
    kontakt_aktualisieren,
    kontakt_loeschen,
    kontakt_suchen
)

def menue_anzeigen():
    """Zeigt das Hauptmenü an."""
    print("\n" + "=" * 50)
    print("KONTAKTBUCH - HAUPTMENÜ")
    print("=" * 50)
    print("1. Kontakt hinzufügen")
    print("2. Alle Kontakte anzeigen")
    print("3. Kontakt aktualisieren")
    print("4. Kontakt löschen")
    print("5. Kontakt suchen")
    print("0. Beenden")
    print("=" * 50)


def main():
    """Hauptfunktion der Anwendung."""
    print("\n*** KONTAKTBUCH ***")
    print("Willkommen!")

    while True:
        try:
            menue_anzeigen()
            wahl = input("\nIhre Wahl: ").strip()

            if wahl == "1":
                kontakt_hinzufuegen()
            elif wahl == "2":
                kontakte_anzeigen()
            elif wahl == "3":
                kontakt_aktualisieren()
            elif wahl == "4":
                kontakt_loeschen()
            elif wahl == "5":
                kontakt_suchen()
            elif wahl == "0":
                print("\nAlle Daten wurden gespeichert. Programm wird beendet.")
                break
            else:
                print("\n[X] Ungültige Eingabe! Bitte 0-5 wählen.")
        except KeyboardInterrupt:
            print("\n\nProgramm abgebrochen.")
            break
        except Exception as e:
            print(f"\n[X] Unerwarteter Fehler: {e}")

if __name__ == "__main__":
    main()

