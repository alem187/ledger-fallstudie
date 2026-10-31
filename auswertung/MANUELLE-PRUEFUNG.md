# Gleiche manuelle Prüfung je Artefakt

Für BASE, A1, B1, A2, B2, A3, B3 je eine Kopie außerhalb des Modellkontexts.
Ausgefallene Artefakte bleiben sichtbar; keine Bewertung fehlenden Codes.
Zeit der tatsächlich geleisteten Prüfung in disjunkten Intervallen erfassen.

| Kriterium | Gleicher Prüfumfang | Status / Fundstellen / Gegenargument / Unsicherheit |
|---|---|---|
| F01 | Rohbericht, elf gesammelt/ausgeführt, Fehler/Fehlschlag/Skip | offen |
| F02 | R01–R06, P01–P04 aus AV 1.0, Soll/hergeleitetes Ist je Pfad | offen |
| S01 | Datum, Betrag, Beschreibung, Sortierung, Listenendzustand, Tabellenbau; Abhängigkeiten | offen |
| S02 | beide Locales/Währungen, Vorzeichen/Null, Kürzung, Sortierung, Listenendzustand; konkrete Verständnishürde | offen |
| S03 | jede Rohmeldung mit Regelbedingung/Aufgabenbezug prüfen; keine Meldung nur im ausgewählten Regelsatz | offen |
| B01 | alle Zweige, Stellenpaare gleicher Regel, Mehrfachaufwand und entlastende Unterschiede | offen |
| B02 | alle Imports/Definitionen/Zuweisungen/Zweige; Einstiegspunkte, Initialisierung, Mutation und Formatbesonderheiten | offen |
| B03 | alle Klassen/Helfer/Konfigurationen/Weiterleitungen; Aufgabe, Verfolgungslast und Gegenargumente | offen |
| U01 | Hash/Bytes/Zeilen/Kommentar-/Statementwerte, Fehlgründe, keine Qualitätsschwelle | offen |
| U02 | Definitionsliste und Container/Spannen/Dekoratoren, fehlende Syntaxwerte | offen |

Zulässige manuelle Status: ohne_befund, begruendeter_befund, unklar,
nicht_anwendbar, nicht_untersucht. Ohne Befund immer mit geprüftem Umfang.
Fundstelle, Begründung, Regelherkunft und Gegenargument in befunde.csv
übertragen. Gleiche Ursache über Kriterien nur als verknüpften Fall führen.
Keine Summennote; F01 und F02 sowie Umfang und Bloating bleiben getrennt.
