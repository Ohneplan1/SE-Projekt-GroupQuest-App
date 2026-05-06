# SE-Projekt: GroupQuest-App

Streamlit/SQLite-Prototyp fuer das Software-Engineering-Projekt.

## Projektdokumentation

- [Projektbericht](Projektbericht.md)
- [Projektbacklog](Einkaufsapp_Backlog.md)
- [Sprint 1 Review und Retrospektive](Sprint_1_Review_Retro.md)
- [Sprint 2 Review und Retrospektive](Sprint_2_Review_Retro.md)
- [GitHub Issues](https://github.com/Ohneplan1/SE-Projekt-GroupQuest-App/issues)
- [GitHub Milestones](https://github.com/Ohneplan1/SE-Projekt-GroupQuest-App/milestones)

## Sprint-1-Umfang

- Registrierung
- Login
- Einkaufslisten erstellen
- Einkaufslisten anzeigen
- Artikel hinzufuegen
- Mengen erfassen
- Artikel abhaken
- offene Artikel zaehlen

## Sprint-2-Umfang

- Einkaufslisten umbenennen
- Einkaufslisten loeschen
- Artikel bearbeiten
- Artikel loeschen
- Artikel kategorisieren
- Artikel nach Status filtern

## Lokal starten

```bash
pip install -r requirements.txt
streamlit run app.py
```

Die SQLite-Datenbank wird beim Start automatisch unter `data/einkaufsapp.db` erstellt.

## Technische Vorgaben

- Python
- Streamlit
- SQLite
- keine externen Services
- vorbereitet fuer Deployment ueber GitHub und Streamlit.io
