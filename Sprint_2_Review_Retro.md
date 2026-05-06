# Sprint 2 Review und Retrospektive

## Sprint-Ziel

Nutzer:innen koennen Einkaufslisten und Artikel nachtraeglich pflegen, strukturieren und filtern.

## Umgesetzte User Stories

- US6: Einkaufsliste umbenennen
- US7: Einkaufsliste loeschen
- US11: Artikel bearbeiten
- US12: Artikel loeschen
- US16: Artikel kategorisieren
- US18: Artikel filtern

## Review-Ergebnis

Im Sprint Review wurde der erweiterte Streamlit/SQLite-Prototyp gezeigt. Der Ablauf wurde am Produkt geprueft:

1. Bestehende Einkaufsliste umbenennen
2. Neue Einkaufsliste zum Loeschtest erstellen
3. Einkaufsliste nach Bestaetigung loeschen
4. Artikel mit Kategorie hinzufuegen
5. Artikelname, Menge und Kategorie bearbeiten
6. Artikel nach Status filtern
7. Artikel loeschen

Alle Sprint-2-Stories wurden im Review erfolgreich demonstriert.

## Retrospektive

### Gut gelaufen

- Die App wurde funktional deutlich vollstaendiger, ohne den Stack zu erweitern.
- Die neuen Funktionen bauen direkt auf Sprint 1 auf.
- SQLite-Migration fuer Kategorien wurde rueckwaertskompatibel umgesetzt.

### Nicht optimal gelaufen

- Streamlit-Formulare in der Sidebar und im Hauptbereich muessen klar getrennt bedient werden.
- Loeschen braucht eine Bestaetigung, damit im Review keine Daten versehentlich entfernt werden.

### Verbesserung fuer den naechsten Sprint

- Naechster Fokus sollte auf Statistik und optionaler Wichtig-Markierung liegen.
- Gruppen-/Freigabe-Funktionen bleiben riskant und sollten nur umgesetzt werden, wenn genug Zeit bleibt.
