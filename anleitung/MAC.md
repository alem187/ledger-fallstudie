# Ledger am Arbeits-Mac durchführen

## 1. Paket und Nachweisordner vorbereiten

ZIP entpacken oder das öffentliche Hilfs-Repository klonen. Den Paketstamm
in einem Terminal öffnen. Python 3.10 oder neuer ist für die lokalen Hilfen
erforderlich; sie senden keine Anfrage und führen keine Ledger-Lösung aus.

```sh
python3 paket.py verify
python3 paket.py init ../ledger-nachweise
```

`../ledger-nachweise` ist die private Rückgabe. Dort sind sechs Slotordner,
Formulare und `V-MAC.json` vorbereitet. Nicht ins öffentliche Repo verschieben.
In VS Code über „Ordner öffnen“ **ausschließlich `eingabe`** öffnen.
Keinen übergeordneten Workspace hinzufügen. Dort liegen genau ledger.py,
ledger_test.py, instructions.md und aufgabenvertrag.md. Prompt und Anleitung
außerhalb dieses Fensters lesen. Keine frühere Antwort oder Auswertung öffnen.

## 2. Vor A1 am Mac ergänzen

`V-MAC.json` in einem gewöhnlichen Texteditor außerhalb des Copilot-Fensters
ausfüllen. JSON-null bedeutet fehlend. Keine unbekannte Version erfinden;
nicht offengelegte Anbieterangaben ausdrücklich „nicht offengelegt“ nennen.

- macOS, VS Code mit Version/Build, Copilot-Komponente mit Version und Profil.
- Business-Zugang und organisatorische Freigabe für die vorgesehenen Modelle,
  Ask-Modus und tatsächliche Modellnamen mit etwaigen Versionszusätzen.
  Geplant: A Claude Opus 5.5, B GPT-6 Astra. Das sind Planbezeichnungen,
  keine Bestätigung der Verfügbarkeit. Fable ist kein Bestandteil.
  Bei fehlender Auswahl nicht starten und keinen Ersatz selbst wählen.
- Tarif-/Abrechnungsquelle, Credit-Einheit, Anzeigequelle, Auflösung,
  Aktualisierungsverzug, Zuordenbarkeit sowie parallele Nutzung prüfen.
  Nur Prozentanzeige: Einzelverbrauch als fehlend dokumentieren.
- Stoppuhr-/Zeitstempelverfahren mit Zeitzone und Export-/Kopiermethode.
- User-/Workspace-/Repository-/Organisationsanweisungen, Memory, Skills,
  automatische Anhänge, offenen Editor/Selektion und Reasoning kontrollieren.
  Kontrollierbare Zusatzanweisungen/Memory/Skills für beide gleich deaktivieren.
  Organisationsvorgaben nicht umgehen; nicht kontrollierbare Einflüsse offenlegen.
  Wenn sie die vier-Dateien-Bedingung verhindern, vor A1 klären.

Screenshots/Exporte der tatsächlich sichtbaren Zustände unter
`ledger-nachweise/vorab` speichern und in V-MAC.json benennen. Interne
Systemprompts und nicht ausgewiesene Modellversionen bleiben unbekannt.
Keine Firmengeheimnisse oder fremde Daten in den Modellkontext aufnehmen.

### Regel für Reasoning und Kontext

Gibt es eine gemeinsame explizite Reasoning-Stufe für beide Modelle im
Ask-Modus, vorab dieselbe Stufe wählen und ihren Wortlaut dokumentieren.
Andernfalls je Modell die unveränderte verfügbare Standardoption wählen,
die Asymmetrie dokumentieren und während aller drei Slots beibehalten.
Keine Auswahl anhand erzeugter Antworten und keine Testanfrage.
Gleiche Namen bedeuten kein gleiches Rechenbudget. Der Vergleich gilt für
die dokumentierten Copilot-Konfigurationen, nicht für isolierte Basismodelle.
Auto-Modellwahl, dynamischer Fallback oder Agent-/Edit-Modus sind unzulässig.
Für beide Modelle ausdrücklich dieselben vier vollständigen Dateien anhängen;
Kontextliste vor jedem Senden sichern. Keine zusätzliche markierte Auswahl.

## 3. Stand V vor der ersten Anfrage sichern

Kriterienstand K ist in Commit c9204cd nachgewiesen; Werkzeugstand W-1.0
und Paketdateien sind mit Hashes dokumentiert. Am Mac keine Regeln ändern.
Nachdem alle tatsächlichen Mac-Angaben/Nachweise ergänzt wurden:

```sh
python3 paket.py seal ../ledger-nachweise
```

Das erstellt `V-FIXIERT.json`, prüft vollständige Felder und verhindert das
Überschreiben. Es ist eine lokale Integritätsaufnahme, keine unabhängige
Zeitbeglaubigung. Den gesamten Vorabstand einschließlich V-FIXIERT.json
vor A1 separat datiert sichern, etwa als private schreibgeschützte Kopie
auf einem zweiten Datenträger. Datum/Zeitzone und Sicherungsort protokollieren.
Noch nicht begonnene Slots dürfen keine Absendezeiten enthalten.

## 4. Sechs einmalige Chats

Reihenfolge **A1 → B1 → A2 → B2 → A3 → B3**. Vor jedem Slot:

1. `python3 paket.py verify` ausführen. Eingabedateien nicht ändern.
2. Neuen leeren Chat im Ask-Modus öffnen, explizites Modell A/B wählen.
3. Einstellungen wie Stand V prüfen. Genau vier Dateien ausdrücklich
   anhängen. Modell, Modus und Kontextliste als Screenshot im Slotordner sichern.
4. Numerischen Credit-Stand mit Einheit, Quelle, Ablesezeit und Nachweis
   sichern. Bei ungeeigneter Anzeige fehlend mit Grund erfassen.
5. Bedienung vor Anfrage ab Beginn des neuen Chats messen. PROMPT.txt aus
   `anleitung` wortgleich kopieren und **genau einmal** senden.
6. Absendezeit mit Zeitzone notieren. Jetzt endet Bedienung vor, Warten beginnt.
7. Vollständiges stabiles Antwortende oder Abbruch mit Zeitpunkt sichern.
   Streaming gehört zum Warten. Nach 600 Sekunden stoppen und Zwischenstand
   sichern. Ab Senden zählt der Slot, auch bei Fehler oder Kontingentgrenze.
8. Bedienung nach Antwort messen. Gesamte erste Antwort als `rohantwort.md`
   im passenden privaten Slotordner speichern; zusätzliche Originalexporte
   unverändert daneben erhalten. Auch Erklärungen und Codezäune kopieren.
   Fehler-/Abbruchanzeigen gegebenenfalls zusätzlich als Screenshot sichern.
9. Credit-Stand danach mit Ablesezeit, Einheit und Aktualisierungsstatus
   sichern. Kein verlässlich aufgelöster Unterschied: fehlend, nicht Null.
10. `protokoll.json` des Slots ausfüllen. Unklaren/unvollständigen Code
    ausdrücklich kennzeichnen; Code nicht ergänzen. Die spätere Extraktion
    am PC folgt dem mitgelieferten Protokoll und wählt keine günstigere Alternative.

Keine Folgeprompts, Fortsetzungen, Regenerierungen, Reparaturen oder
Wiederholungen. Bei Modell-/Dienständerung vor dem nächsten Slot pausieren
und klären. Ausfallslots bleiben erhalten. Keine Ergebnisse vorab prüfen,
um die nächsten Antworten oder Einstellungen daran anzupassen.

Zeitintervalle disjunkt erfassen: bedienung_vor, warten, bedienung_nach,
spätere pruefung; Unterbrechungen aus aktiven Intervallen ausschneiden und
separat kennzeichnen. Falls Extraktion erst am PC erfolgt, Bedienung nach
am Mac und Extraktionsbedienung am PC getrennt als Teilintervalle erfassen.
Keine rückwirkende Schätzung. PC-Prüfzeit später tatsächlich messen.

## 5. Privat an den PC zurückgeben

Nach allen Slots enthält der Nachweisordner:

- V-MAC.json, V-FIXIERT.json und sämtliche Vorabnachweise;
- A1/B1/A2/B2/A3/B3 mit protokoll.json, rohantwort.md (soweit vorhanden),
  unveränderten Originalexporten, Kontext-/Modell-/Credit-/Fehlernachweisen;
- ergänzende durchlaeufe.csv/zeitintervalle.csv/befunde.csv, sofern verwendet,
  kostenparameter.json (unbekannte Parameter bleiben null).

Primäre maschinenlesbare Erfassung ist protokoll.json. CSVs sind ergänzende
Übersichten; Widersprüche vor Auswertung klären, nicht still überschreiben.

```sh
python3 paket.py return ../ledger-nachweise
```

Das ZIP einschließlich Rückgabehashes privat an den PC übertragen. Es enthält
keine automatische Veröffentlichung. Dort gemäß auswertung/AUSWERTUNG.md
importieren und prüfen. Die ursprünglichen Rohdaten unverändert aufbewahren.
