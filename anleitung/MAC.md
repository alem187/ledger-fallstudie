# Durchführung am Arbeits-Mac

## Vor A1

- Erst den Kriteriennachweis im maßgeblichen Thesis-Repo prüfen, anschließend
  Analysewerkzeuge und Konfigurationen festlegen; vor A1 vollständigen Stand V sichern.
- Dieses Hilfs-Repo ist ein Transportpaket und kein Nachweis eines abgeschlossenen V.
- Nur `eingabe` als einzelnen VS-Code-Ordner öffnen, nicht den Repository-Stamm.
- VS-Code-Version, Copilot-Komponenten mit Version, Business-Zugang und angezeigte
  Abrechnungseinheit dokumentieren. Keine vertraulichen Firmeninhalte beifügen.
- Geplant: A Claude Opus 5.5, B GPT-6 Astra. Das sind Nutzerangaben, keine bestätigte
  Verfügbarkeitsaussage. Tatsächliche Namen und Verfügbarkeit am Mac prüfen;
  kein Auto, Fallback oder eigenmächtiger Modelltausch.
- Ask-Modus für beide Modelle bestätigen. Automatische Anweisungen, Memory,
  Skills, Kontext und Reasoning-Optionen prüfen und kontrollierbar gleich halten.
  Gemeinsame explizite Einstellung verwenden, falls verfügbar; andernfalls die
  tatsächlichen Modelleinstellungen dokumentieren und vor A1 begründet festlegen.
  Gleiche Bezeichnungen belegen kein gleiches Rechenbudget.
- Alle vier Kontextdateien ausdrücklich beifügen und deren sichtbare Liste sichern.
  Keine Kriterien, früheren Antworten oder Auswertungen in den Modellkontext geben.
- Credit-Anzeige, Auflösung, Verzögerung und Zeitmessverfahren ohne Probe-Anfrage prüfen.
- Lokalen Nachweisordner außerhalb von `eingabe` anlegen. Leere Vorlagen aus `vorlagen`
  dorthin kopieren; darin Unterordner A1/B1/A2/B2/A3/B3 anlegen.
- Tatsächliche Einstellungen, Quellencommit, Paket-Hashes und vollständigen Stand V
  mit Zeitpunkt und Zeitzone vor dem ersten Absenden unveränderlich sichern.

## Genau sechs Slots

Reihenfolge A1, B1, A2, B2, A3, B3. Für jeden Slot:

1. Unveränderte Eingabedateien und Hashes kontrollieren. Neuen leeren Chat öffnen.
2. Ask, explizites Modell und vier Dateianhänge kontrollieren und sichern.
3. Credit-Stand mit Einheit, Quelle, Ablesezeit und Screenshot erfassen.
4. Bedienungsintervall starten; denselben Prompt aus PROMPT.txt wortgleich einsetzen.
5. Einmal senden, Absendezeit mit Zeitzone erfassen. Wartezeit separat messen.
6. Vollständiges Antwortende oder Fehler dokumentieren; nach 600 Sekunden stoppen.
7. Vollständige erste Antwort unverändert im Slotordner als rohantwort.md bzw.
   Originalexport sichern; auch Erläuterungen, Fehler und Abbruchanzeigen erhalten.
8. Nachher-Credits samt Ablesezeit, Einheit, Auflösung und Aktualisierungsstatus sichern.
9. Modell, Einstellungen, Kontext, Chatkennung, Zeitintervalle und Abweichungen erfassen.

Ab Senden zählt der Slot auch bei Fehlern. Keine Folgeprompts, Wiederholungen,
Regenerierungen, Reparaturen oder Ersatzslots. Bei geändertem Dienst vor dem
nächsten Slot pausieren und klären. Fehlende Daten leer lassen und begründen.
Verzögerte/gerundete oder durch parallele Nutzung beeinflusste Credit-Differenzen
nicht als gemessenen Einzelverbrauch ausgeben. Prozentstände sind keine Credit-Mengen.
Bedienung, Warten, menschliche Prüfung und Unterbrechungen getrennt erfassen.

## Rückgabe an den PC

Gesamten lokalen Nachweisordner mit Stand V, ausgefüllten CSVs, sechs Slotordnern,
Rohantworten/Originalexporten, Kontext- und Einstellungsnachweisen, Credit-Ablesungen
und Zeitprotokollen als ZIP privat an den PC übertragen. Hashes der gesicherten
Dateien erfassen. Keine Antworten im öffentlichen Hilfs-Repo speichern.

Codeextraktion erst nach der festgelegten Regel im PROTOKOLL-QUELLSTAND.md:
genau ein vollständiger python/py-Codeblock, ausschließlich Zäune entfernen,
UTF-8 ohne BOM, LF; nichts reparieren oder zusammensetzen. Rohantwort erhalten.
Keine technischen Laufzeiten als menschliche Prüfzeiten ausgeben.
