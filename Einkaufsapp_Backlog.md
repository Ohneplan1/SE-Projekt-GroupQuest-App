# Einkaufsapp - Projektbacklog

## MVP-Ziel

Die Einkaufsapp soll Haushalten oder kleinen Gruppen helfen, gemeinsame Einkaufslisten zu erstellen, Artikel zu verwalten und erledigte Einkaeufe sichtbar abzuhaken. Die erste Version konzentriert sich bewusst auf Listen, Artikel, Status und einfache Zusammenarbeit. Komplexe Funktionen wie Barcode-Scan, externe Preisvergleiche oder Cloud-Sync sind nicht Teil des MVP.

## Features / Milestones

### 1. Nutzerverwaltung

Ziel: Nutzer:innen koennen lokal angelegt werden und ihre eigenen Einkaufslisten sehen.

### 2. Einkaufslisten

Ziel: Nutzer:innen koennen Einkaufslisten erstellen, anzeigen, bearbeiten und loeschen.

### 3. Artikelverwaltung

Ziel: Nutzer:innen koennen Artikel zu Listen hinzufuegen, bearbeiten, abhaken und entfernen.

### 4. Gruppen / Haushalt

Ziel: Mehrere Nutzer:innen koennen an einer gemeinsamen Liste arbeiten.

### 5. Kategorien und Prioritaeten

Ziel: Artikel koennen strukturiert werden, damit der Einkauf uebersichtlich bleibt.

### 6. Auswertung / Uebersicht

Ziel: Nutzer:innen sehen offene Artikel, erledigte Artikel und einfache Einkaufsstatistiken.

## User Stories

| Nr. | Feature | User Story | Prioritaet | Schaetzung |
|---:|---|---|---|---|
| 1 | Nutzerverwaltung | Als Nutzer:in moechte ich mich registrieren, damit meine Einkaufslisten gespeichert werden koennen. | P0 | M |
| 2 | Nutzerverwaltung | Als Nutzer:in moechte ich mich einloggen, damit ich Zugriff auf meine Listen bekomme. | P0 | M |
| 3 | Nutzerverwaltung | Als Nutzer:in moechte ich mich ausloggen, damit andere Personen nicht in meinem Account weiterarbeiten. | P1 | S |
| 4 | Einkaufslisten | Als Nutzer:in moechte ich eine neue Einkaufsliste erstellen, damit ich einen Einkauf planen kann. | P0 | S |
| 5 | Einkaufslisten | Als Nutzer:in moechte ich alle meine Einkaufslisten sehen, damit ich die richtige Liste auswaehlen kann. | P0 | S |
| 6 | Einkaufslisten | Als Nutzer:in moechte ich den Namen einer Einkaufsliste bearbeiten, damit ich Listen nachtraeglich korrigieren kann. | P1 | S |
| 7 | Einkaufslisten | Als Nutzer:in moechte ich eine Einkaufsliste loeschen, damit alte Listen nicht stoeren. | P1 | S |
| 8 | Artikelverwaltung | Als Nutzer:in moechte ich einen Artikel zu einer Liste hinzufuegen, damit ich ihn beim Einkauf nicht vergesse. | P0 | S |
| 9 | Artikelverwaltung | Als Nutzer:in moechte ich eine Menge zu einem Artikel erfassen, damit klar ist, wie viel gekauft werden soll. | P0 | S |
| 10 | Artikelverwaltung | Als Nutzer:in moechte ich Artikel als gekauft abhaken, damit der Fortschritt sichtbar ist. | P0 | S |
| 11 | Artikelverwaltung | Als Nutzer:in moechte ich Artikel bearbeiten, damit Tippfehler oder Mengen korrigiert werden koennen. | P1 | S |
| 12 | Artikelverwaltung | Als Nutzer:in moechte ich Artikel loeschen, damit falsche Eintraege entfernt werden koennen. | P1 | S |
| 13 | Gruppen / Haushalt | Als Nutzer:in moechte ich eine Liste fuer andere Nutzer:innen freigeben, damit wir gemeinsam einkaufen koennen. | P1 | M |
| 14 | Gruppen / Haushalt | Als Nutzer:in moechte ich sehen, wer einen Artikel hinzugefuegt hat, damit Aenderungen nachvollziehbar sind. | P2 | M |
| 15 | Gruppen / Haushalt | Als Nutzer:in moechte ich sehen, wer einen Artikel abgehakt hat, damit klar ist, wer ihn gekauft hat. | P2 | M |
| 16 | Kategorien und Prioritaeten | Als Nutzer:in moechte ich Artikel einer Kategorie zuordnen, damit die Liste im Supermarkt uebersichtlicher ist. | P1 | M |
| 17 | Kategorien und Prioritaeten | Als Nutzer:in moechte ich Artikel als wichtig markieren, damit dringende Dinge auffallen. | P1 | S |
| 18 | Kategorien und Prioritaeten | Als Nutzer:in moechte ich die Liste nach offenen und gekauften Artikeln filtern, damit ich mich auf offene Einkaeufe konzentrieren kann. | P1 | M |
| 19 | Auswertung / Uebersicht | Als Nutzer:in moechte ich sehen, wie viele Artikel noch offen sind, damit ich den Einkaufsfortschritt einschaetzen kann. | P0 | S |
| 20 | Auswertung / Uebersicht | Als Nutzer:in moechte ich eine einfache Statistik zu erledigten Artikeln sehen, damit ich abgeschlossene Einkaeufe nachvollziehen kann. | P2 | M |

## Sprint 1

### Sprint-Ziel

Nutzer:innen koennen sich lokal anmelden, eine Einkaufsliste erstellen und erste Artikel hinzufuegen sowie abhaken.

### Sprint-Backlog

| Nr. | User Story | Prioritaet | Schaetzung |
|---:|---|---|---|
| 1 | Registrierung | P0 | M |
| 2 | Login | P0 | M |
| 4 | Einkaufsliste erstellen | P0 | S |
| 5 | Einkaufslisten anzeigen | P0 | S |
| 8 | Artikel hinzufuegen | P0 | S |
| 9 | Menge erfassen | P0 | S |
| 10 | Artikel abhaken | P0 | S |
| 19 | Anzahl offener Artikel anzeigen | P0 | S |

## Empfohlene technische Startstruktur

```text
einkaufsapp/
  app.py
  database.py
  requirements.txt
  README.md
  data/
    einkaufsapp.db
```

## Empfohlene SQLite-Tabellen fuer Sprint 1

```sql
users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT NOT NULL UNIQUE,
  password TEXT NOT NULL
)

shopping_lists (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  name TEXT NOT NULL,
  created_at TEXT NOT NULL
)

items (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  list_id INTEGER NOT NULL,
  name TEXT NOT NULL,
  quantity TEXT,
  is_done INTEGER NOT NULL DEFAULT 0,
  created_at TEXT NOT NULL
)
```

## Definition of Done

- Die App startet lokal mit `streamlit run app.py`.
- Daten werden in SQLite gespeichert und bleiben nach einem Neustart erhalten.
- Jede User Story ist im GitHub Project als Issue angelegt.
- Jede User Story hat Prioritaet und T-Shirt-Size.
- Abgeschlossene Stories werden im Sprint Review am laufenden Produkt gezeigt.
- Der Projektbericht dokumentiert Ziel, Rollen, Backlog, Sprint-Ziel, Review-Ergebnis und Retrospektive.
