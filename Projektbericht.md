# Projektbericht - SE-Projekt: GroupQuest-App

## 1. Projektueberblick

Dieses Projekt wurde im Rahmen der Lehrveranstaltung Software Engineering umgesetzt. Die urspruengliche Idee "GroupQuest-App" wurde fuer den kurzen Projektzeitraum auf eine vorzeigbare Einkaufslisten-App reduziert. Die bestehende private Einkaufsapp diente nur als fachliche Vorlage. Fuer das Schulprojekt wurde eine eigene App nach den Vorgaben der Lehrveranstaltung erstellt.

Die App hilft Nutzer:innen dabei, Einkaufslisten anzulegen, Artikel mit Mengen zu erfassen und den Einkaufsfortschritt sichtbar zu machen.

## 2. Vorgaben und Umsetzung

| Vorgabe | Umsetzung im Projekt |
|---|---|
| Python | App wurde in Python umgesetzt |
| Streamlit | Frontend wurde mit Streamlit umgesetzt |
| SQLite | Daten werden lokal in SQLite gespeichert |
| Deployment ueber GitHub/Streamlit.io | Repo ist auf GitHub vorbereitet; Streamlit.io kann `app.py` starten |
| Projektverwaltung ueber GitHub/GitHub Projects | Backlog wurde als GitHub Issues und Milestones angelegt |
| Keine externen Services | Die App nutzt keine externen Speicherdienste oder APIs |
| SCRUM | Backlog, Sprint Planning, Sprint Review und Retrospektive wurden dokumentiert |
| Stack Authority bei der Gruppe | Der Stack wurde bewusst auf Python, Streamlit und SQLite begrenzt |

## 3. Repository und Projektverwaltung

- GitHub Repository: [Ohneplan1/SE-Projekt-GroupQuest-App](https://github.com/Ohneplan1/SE-Projekt-GroupQuest-App)
- Issues: [GitHub Issues](https://github.com/Ohneplan1/SE-Projekt-GroupQuest-App/issues)
- Milestones: [GitHub Milestones](https://github.com/Ohneplan1/SE-Projekt-GroupQuest-App/milestones)
- Sprint-1-Issues: [Label sprint-1](https://github.com/Ohneplan1/SE-Projekt-GroupQuest-App/issues?q=label%3Asprint-1)

Hinweis: Ein GitHub Project wurde in der aktuellen GitHub-Abfrage nicht gefunden. Die Backlog-Verwaltung ist aber ueber Issues, Labels und Milestones nachvollziehbar dokumentiert.

## 4. SCRUM-Rollen

Die Rollen koennen im Teambericht mit den echten Namen ergaenzt werden:

- Product Owner: offen im Team zu ergaenzen
- SCRUM Master: offen im Team zu ergaenzen
- Development Team: offen im Team zu ergaenzen

## 5. Product Backlog

Das Product Backlog wurde in GitHub als Issues angelegt. Features wurden als Milestones dokumentiert. User Stories wurden als Issues mit Prioritaeten und T-Shirt-Sizes erfasst.

### Features / Milestones

| Milestone | Beschreibung | Issues |
|---|---|---:|
| Nutzerverwaltung | Registrierung, Login, Logout | 3 |
| Einkaufslisten | Einkaufslisten erstellen, anzeigen, bearbeiten, loeschen | 4 |
| Artikelverwaltung | Artikel hinzufuegen, bearbeiten, abhaken, loeschen | 5 |
| Gruppen / Haushalt | Gemeinsame Nutzung und Nachvollziehbarkeit | 3 |
| Kategorien und Prioritaeten | Kategorien, Wichtig-Markierung, Filter | 3 |
| Auswertung / Uebersicht | offene Artikel und einfache Statistik | 2 |

### Prioritaeten

- P0: Muss fuer den ersten lauffaehigen Prototyp vorhanden sein
- P1: Wichtig fuer eine vollstaendigere App
- P2: Optional, wenn noch Zeit bleibt

### T-Shirt-Sizes

- S: kleine, klar abgegrenzte Story
- M: mittlere Story mit mehreren Teilschritten

## 6. Sprint 1

### Sprint-Ziel

Nutzer:innen koennen sich lokal anmelden, eine Einkaufsliste erstellen und erste Artikel hinzufuegen sowie abhaken.

### Sprint-Backlog

| Issue | User Story | Status |
|---|---|---|
| [US1](https://github.com/Ohneplan1/SE-Projekt-GroupQuest-App/issues/1) | Registrierung | erledigt |
| [US2](https://github.com/Ohneplan1/SE-Projekt-GroupQuest-App/issues/2) | Login | erledigt |
| [US4](https://github.com/Ohneplan1/SE-Projekt-GroupQuest-App/issues/4) | Einkaufsliste erstellen | erledigt |
| [US5](https://github.com/Ohneplan1/SE-Projekt-GroupQuest-App/issues/5) | Einkaufslisten anzeigen | erledigt |
| [US8](https://github.com/Ohneplan1/SE-Projekt-GroupQuest-App/issues/8) | Artikel hinzufuegen | erledigt |
| [US9](https://github.com/Ohneplan1/SE-Projekt-GroupQuest-App/issues/9) | Menge erfassen | erledigt |
| [US10](https://github.com/Ohneplan1/SE-Projekt-GroupQuest-App/issues/10) | Artikel abhaken | erledigt |
| [US19](https://github.com/Ohneplan1/SE-Projekt-GroupQuest-App/issues/19) | Offene Artikel zaehlen | erledigt |

### Sprint Review

Im Sprint Review wurde der lauffaehige Streamlit/SQLite-Prototyp gezeigt. Demonstriert wurde folgender Ablauf:

1. Neuen Benutzer registrieren
2. Mit dem Benutzer einloggen
3. Neue Einkaufsliste erstellen
4. Artikel mit Menge hinzufuegen
5. Offene, erledigte und gesamte Artikel anzeigen
6. Artikel abhaken und aktualisierte Zaehler sehen

Alle Sprint-1-Stories wurden nach dem Review in GitHub geschlossen.

### Retrospektive

Gut gelaufen:

- Die wichtigsten Grundfunktionen sind sichtbar und lauffaehig.
- Die App nutzt den geforderten Stack Python, Streamlit und SQLite.
- Der Scope wurde realistisch reduziert.

Nicht optimal gelaufen:

- Die urspruengliche GroupQuest-Idee war fuer die kurze Projektzeit zu gross.
- Ein Teil der Projektorganisation musste zuerst nachgezogen werden.

Verbesserung fuer Sprint 2:

- Keine grossen neuen Systeme einfuehren.
- Fokus auf bestehende Einkaufslisten-Funktionen: Bearbeiten, Loeschen, Kategorien und Filter.

## 7. Technische Umsetzung

### App-Struktur

```text
app.py
database.py
requirements.txt
README.md
Einkaufsapp_Backlog.md
Sprint_1_Review_Retro.md
Projektbericht.md
```

### Datenbank

Die SQLite-Datenbank wird automatisch unter `data/einkaufsapp.db` erstellt. Diese Datei wird nicht ins Repository committed.

Verwendete Tabellen:

- `users`
- `shopping_lists`
- `items`

### Start der App

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 8. Aktueller Stand

Der Sprint-1-Prototyp ist lauffaehig. Nutzer:innen koennen:

- sich registrieren
- sich einloggen
- Einkaufslisten erstellen
- Einkaufslisten anzeigen
- Artikel mit Menge hinzufuegen
- Artikel abhaken
- offene, erledigte und gesamte Artikel sehen

## 9. Naechster Sprint

Empfohlener Sprint-2-Scope:

- [US6](https://github.com/Ohneplan1/SE-Projekt-GroupQuest-App/issues/6): Einkaufsliste umbenennen
- [US7](https://github.com/Ohneplan1/SE-Projekt-GroupQuest-App/issues/7): Einkaufsliste loeschen
- [US11](https://github.com/Ohneplan1/SE-Projekt-GroupQuest-App/issues/11): Artikel bearbeiten
- [US12](https://github.com/Ohneplan1/SE-Projekt-GroupQuest-App/issues/12): Artikel loeschen
- [US16](https://github.com/Ohneplan1/SE-Projekt-GroupQuest-App/issues/16): Artikel kategorisieren
- [US18](https://github.com/Ohneplan1/SE-Projekt-GroupQuest-App/issues/18): Artikel filtern

Gruppenfunktionen sollten erst spaeter umgesetzt werden, da sie fuer SQLite/Streamlit mehr Abstimmung und Testaufwand brauchen.
