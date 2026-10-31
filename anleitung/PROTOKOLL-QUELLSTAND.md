# Protokoll für sechs einmalige Ledger-Refactorings

Fassung V-Vorbereitung 1.0, 31. Oktober 2026. **Keine Anfrage ausgeführt.**
Durchführung am Arbeits-Mac mit Copilot Business, technische Auswertung am
Windows-PC. Geplant A Claude Opus 5.5, B GPT-6 Astra; tatsächliche Namen,
Verfügbarkeit und Optionen bleiben am Mac vor A1 zu bestätigen. Fable entfällt.

K-Kern in Commit `c9204cd861773b17fc3a55b53bf95a6c90e2ccda` nachgewiesen:
48/48 Manifestdateien bytegleich geprüft, Nachweis `K-VERSIONSNACHWEIS.json`
vor zusätzlicher Werkzeugwahl. Historisches Manifest unverändert. Keine
unabhängige Zeitbeglaubigung oder unabhängige Kriterienvalidierung behauptet.
Werkzeugstand W-1.0 steht in `../auswertung/`; tatsächliche Mac-Angaben und
abschließende Fixierung V bleiben vor der ersten Anfrage erforderlich.

## Design und Zuordnung

Eine vorhandene Ausgangsfassung; zwei explizit ausgewählte Modelle, gleicher
Ask-Modus in GitHub Copilot/VS Code; je drei neue Chats. Reihenfolge vorab:

| Position | Kennung | Modellplatz | Status |
|---|---|---|---|
| 1 | A1 | A | nicht durchgeführt |
| 2 | B1 | B | nicht durchgeführt |
| 3 | A2 | A | nicht durchgeführt |
| 4 | B2 | B | nicht durchgeführt |
| 5 | A3 | A | nicht durchgeführt |
| 6 | B3 | B | nicht durchgeführt |

A und B erhalten vor der Fixierung die **tatsächlich im selben Ask-Modus
auswählbaren** Modellbezeichnungen einschließlich gegebenenfalls angezeigtem
Versions-/Reasoningzusatz. Kein Auto, keine dynamische Auswahl, kein stiller
Fallback. Kein Teilnehmerdesign, keine Aufgabenstichprobe, keine pass@k-Schätzung.
Der Start mit A ist eine feste organisatorische Regel, keine Randomisierung.

## Einheitlicher expliziter Kontext

Für die Erhebung einen getrennten lokalen Ordner außerhalb des Thesis-Repos
verwenden. Vor jedem Chat gleicher Inhalt und gleiche Hashes:

1. `ledger.py`: bytegleiche Kopie von `upstream/baseline.py`.
2. `ledger_test.py`: bytegleiche Kopie des vorhandenen Testsnapshots.
3. `instructions.md`: bytegleiche Aufgabenanweisung.
4. `aufgabenvertrag.md`: bytegleiche Fassung AV 1.0, einschließlich der
   ausdrücklich eigenen Entscheidungen zu Sortierung, Listenendzustand,
   Formatbesonderheiten, Eingabegrenzen und ergänzender F02-Codeprüfung.

Diese vier Dateien für jeden Chat ausdrücklich als Dateikontext beifügen;
angezeigte Kontextliste vor dem Senden nachweisen. Kein gesamtes Repository,
keine weiteren Antworten, Beispiel-Lösungen, Kriterienmatrix, Literatur,
Prüfberichte oder Kostenannahmen beifügen. Keine markierte Codeauswahl und
kein zufälliger aktiver zusätzlicher Editor. Individuelle/Workspace-/Repository-
Anweisungen, Memory, Zusatzskills und automatisch beigefügter Kontext müssen
vor dem ersten Durchlauf geprüft und soweit kontrollierbar für beide
Bedingungen gleich ausgeschlossen werden; das Produktverhalten darf nicht
ohne Oberflächenprüfung als kontextfrei beschrieben werden. Nicht einsehbare
Systeminstruktionen sind eine dokumentierte Grenze.

Jeder Durchlauf beginnt in einem neuen leeren Chat im selben Ask-Modus und
mit denselben Kontextdateien. `PROMPT.txt` wortgleich einfügen. Lokale
Anweisungsklärungen niemals nach dem ersten Durchlauf nachreichen.
Die öffentliche Exercism-Anweisung schlägt kleine iterative Änderungen und
ein Änderungslog vor. Dieses **Studienprotokoll** begrenzt den Ablauf auf
eine vollständige Erstantwort; die Abweichung vom Lernworkflow wird offen
dokumentiert und für beide Modelle identisch gehalten.

## Antwort- und Codeübernahme

- Genau einmal senden. Keine Folgeanfrage, keine Regenerierung, kein
  Fortsetzen abgeschnittener Antworten, keine Reparatur und kein Ersatz.
- Vollständige erste Antwort einschließlich etwaiger Erklärungen, Warnungen,
  Abbruchanzeige und Codeblöcke zuerst exportieren beziehungsweise vollständig
  kopieren. Originalexport unverändert erhalten; Export-/Kopiermethode nennen.
- Für die Auswertung nur **einen** vollständigen fenced Codeblock mit
  Sprachkennung `python` oder `py` übernehmen. Ohne genau einen solchen
  Block: `keine_codeausgabe` beziehungsweise `mehrdeutige_codeuebernahme`.
  Andere Codeblöcke, mehrere Alternativen und Ausschnitte werden weder
  zusammengesetzt noch nach Testbestehen ausgewählt.
- Äußerliche Erläuterungen allein machen einen ansonsten eindeutigen
  vollständigen Block nicht unbrauchbar; Promptabweichung gesondert markieren.
- Nur öffnenden/schließenden Codezaun entfernen und als UTF-8 ohne BOM mit
  LF-Zeilenenden speichern. Keine sonstige Veränderung an Zeichen, Einrückung,
  Leerzeilen, Imports oder Code. Ein vom Export nicht erhaltener letzter
  Zeilenumbruch wird nicht erfunden; tatsächliche Übertragung dokumentieren.
- Eine unvollständige oder syntaktisch falsche Fassung bleibt unverändert
  mit entsprechendem Status. Kein funktionaler Erfolg wird aus der
  Formatkonformität abgeleitet. Bei nicht eindeutig vollständiger Ausgabe
  `unklar`/`unvollstaendig` dokumentieren und keine Ergänzungen vornehmen.
- Rohantwort, extrahierte Datei (falls vorhanden), Hash, Kontextnachweis und
  Protokoll erhalten dieselbe Durchlaufkennung. Prüfergebnisse separat halten.

## Zeiten und Verbrauch

Gemäß Nutzerfestlegung werden für Copilot **Credits** erhoben. Die
Verbrauchsspalten erhalten die tatsächlich angezeigte Credit-Einheit;
Tokenzahlen und Premium Requests sind keine zusätzlichen Messgrößen.
Nicht vorhandene Credit-Werte bleiben fehlend. Die Geldbewertung der
Credits erfolgt separat anhand des tatsächlichen Tarifs.

Zeitstempel mit Zeitzone plus Stoppuhrintervalle in Sekunden erfassen.
Keine rückwirkende Schätzung. Die folgenden Phasen sind disjunkt:

| Phase | Start | Ende | Behandlung |
|---|---|---|---|
| Bedienung vor Anfrage | Beginn des neuen Chats nach bereitgestelltem Ausgangsordner | Absenden | Modell-/Kontextkontrolle und Promptübertragung |
| Warten | Absenden | vollständige stabile Antwort oder dokumentierter Abbruch | Streaming eingeschlossen; nicht gleichzeitig als Bedienung zählen |
| Bedienung nach Antwort | Ende des Wartens | Rohantwort und extrahierter Code gesichert | Übertragung/Hashes; keine Codeänderung |
| Prüfung | erster Prüfaufruf/erste Schema-Prüfung nach Sicherung | letzter gespeicherter Befund | Werkzeuge und begründete Codeprüfung, Teilintervalle gesondert |
| Unterbrechung | Fremdunterbrechung beginnt | Fortsetzung | Grund und Dauer getrennt; nicht als aktive Arbeit zählen |

Bedienung vor/nach als getrennte Intervalle speichern und erst danach
zusammenfassen. Einmalige Einrichtung, Bereitstellung und Prüfung der
Ausgangsversion als gemeinsame Vorbereitung getrennt erfassen. Nicht die
bereits ausgeführte Kompatibilitätsprüfung rückwirkend als gemessene
Prüfarbeitszeit ausgeben. Bei Datenlücke fehlend statt null. Auch Ablauf-
und Kalenderzeit sind von aktiven Zeiten zu unterscheiden.

Organisatorisches Antwortlimit: **600 Sekunden ab Absenden**, sofern nicht
früher ein definitiver Produktfehler eintritt. Bei Erreichen stoppen,
Zwischenstand sichern, `zeitlimit` vermerken, nicht erneut senden.
Das ist eine eigene administrative Regel und kein empirischer Grenzwert für
Modellleistung. Für den identischen vorhandenen Funktionstestbestand wird
nach Umgebungsfixierung ein Prozesslimit von **60 Sekunden** angesetzt;
die Regel ist vor dem ersten Durchlauf zu dokumentieren. Zusätzliche
Analysewerkzeuge und ihre Grenzen werden erst nach Kriterienfixierung ergänzt.

Credit-Verbrauch vor und nach jedem Durchlauf mit sichtbarer Einheit, genauer
Quelle, Ablesezeit und Aktualisierungsstatus erfassen. Bei AI Credits nicht
von einer einzigen Premium Request ausgehen. Keine Tokenzahlen aus Codezeichen zurückrechnen. Bei
verzögerten/gerundeten Sammelanzeigen oder parallel laufender Nutzung ist
die Differenz nicht sicher einem Durchlauf zurechenbar: als fehlend oder
lediglich aggregierter Verbrauch kennzeichnen. Tatsächliche Null kann nur
bei ausreichender Anzeigeauflösung und gesicherter Zuordnung behauptet werden.
Eine Verbrauchsbeobachtung ist keine Rechnung über zusätzliche Geldkosten.
Tarif, enthaltene Nutzung, Währung, Rechnungsbasis und Lizenzumlage separat.

## Ausfälle und Protokollabweichungen

Vor dem Senden erkannte fehlende Startvoraussetzungen: gar nicht beginnen,
kein verbrauchter Durchlauf. **Ab erfolgtem Senden zählt der Slot**, auch bei
Netzfehler, Kontingentgrenze, verweigerter Antwort, Kontextfehler oder
Modellwechsel. Ausfall mit Zeitpunkt dokumentieren, nicht ersetzen.
Bei nicht mehr wählbarem Modell oder verändertem Dienst vor dem nächsten
Slot pausiert die Erhebung bis zur Klärung; kein stiller Modelltausch.
Bereits beobachtete Daten bleiben erhalten, eine etwaige spätere Änderung
ist eine kenntlich gemachte Abweichung. Keine zusätzlichen Slots hinzufügen.

Leere/mehrdeutige Antwort, Syntaxfehler, Import-/Teststartfehler und
fachliche Testfehler bleiben verschiedene Status. Kriterienmatrix regelt,
welche übrigen Größen trotzdem beurteilt werden können. Alle sechs Slots
mit Status berichten. Prüfungen nach Erhebung wiederholen nur bei
technischem Anlass und als neuer Bericht; Rohartefakte bleiben erhalten.

## Prüfberichte und Formulare

`durchlaeufe.csv` führt genau die sechs Slots; ein zugehöriger
`nachweispfad` verweist auf Rohantwort, deren Hash, Kontextliste/-hashes,
Chatkennung, Umgebungsstand V und dokumentierte Abweichungen. Die beiden
Credit-Ablesungen erhalten je Zeitpunkt mit Zone, Quelle und
Aktualisierungsstatus. Rundung/Anzeigeauflösung und parallele Nutzung stehen
im Nachweis. Ein Prozentstand allein ist keine Credit-Menge.
`zeitintervalle.csv` enthält disjunkte aktive Teilintervalle; Pausen als
eigene Zeilen, Summe pro Phase erst danach. Technische Prüflaufzeit ist ein
Teil der Prüfphase und kein zusätzlicher menschlicher Aufwand.

`befunde.csv` gilt auch für die Ausgangsversion (`artefakt_id=BASE`).
`nachweisart` unterscheidet `testlauf`, `codeherleitung`, `werkzeugmeldung`
und `umfangsmessung`. `anforderungsherkunft` benennt `originalvorgabe` oder
`studienentscheidung`; bei Strukturhinweisen ohne einzelne R-ID wird deren
Aufgabenbezug erläutert. `pruefumfang` nennt untersuchte Regeln/Pfade und
offene Bereiche. Auch `ohne_befund`, `unklar` und `nicht_untersucht` müssen
nachvollziehbar sein; nur Kandidaten aufzuschreiben reicht nicht.
Rohberichte für Tests/Meldungen/Zählwerte werden über `berichtpfad`
referenziert. Mehrere Kriterien derselben Ursache teilen eine Befund-ID mit
Kriterienverweisen; keine kompensierende Gesamtnote.

Die Reihenfolge der Qualitätsprüfung und der sieben Artefakte folgt K-1.0.
F02 führt P01–P04 als manuelle Herleitung aus; keine neuen automatisierten
Tests, keine zusätzlichen LLM-Anfragen zur Prüfung und keine Codeänderung.
Ein unklarer Codepfad wird nicht durch eine günstigere Ersatzfassung aufgelöst.

## Werkzeugstand W-1.0 nach K-Nachweis

Vollständige Auswahl, Konfiguration, Regeln und Kommandos:
`../auswertung/AUSWERTUNG.md`, `environment.json`, `ruff.toml`,
`ruff-rules.json`, `WERKZEUGSTAND.json`. Python 3.13.14/Windows,
elf unveränderte unittest-Tests, Ruff 0.14.14 mit Pyflakes-Familie F,
ast/tokenize-Zählungen exakt nach K-1.0. Je Prozess 60 Sekunden Limit.
Keine Fixes, keine ausgabenspezifischen Ausschlüsse oder neuen Ledger-Tests.
Gleiche Prüfkommandos für BASE/A1/B1/A2/B2/A3/B3. Rohberichte mit Hashes,
Exitstatus und Fehlwertgründen; manuelle Kriterien bleiben eigenständig.
Keine Komplexitäts-, Coverage-, Schuld- oder Siegerkennzahl ergänzt.

## Reasoning und Kontext vor A1

Gemeinsame ausdrücklich verfügbare Reasoning-Stufe für beide Modelle
vorab gleich wählen; sonst je Modell unveränderte Standardoption samt
Asymmetrie dokumentieren. Keine Auswahl nach Antworten. Gleicher Wortlaut
belegt kein gleiches Rechenbudget. Kontrollierbare Zusatzanweisungen,
Memory und Skills gleich ausschließen, Organisationsvorgaben nicht umgehen.
Nicht einsehbare Einflüsse offenlegen; bei unvereinbarer Kontextbedingung
vor A1 klären. Vier explizite Dateien, keine zusätzliche Selektion.

## Vor dem ersten Durchlauf noch erforderlich

1. Paket- und K-/W-Hashes prüfen; Kriterienkern nicht ändern.
2. Am Arbeits-Mac Business-Zugang, Ask, zwei explizite Modelle und tatsächliche
   Versionen/Einstellungen nachweisen; keine frühere PC-Anzeige übernehmen.
3. Kontext-/Anweisungseinflüsse und Reasoning nach obiger Regel dokumentieren.
4. Credit-Anzeige/Auflösung/Verzug und Zeitmessung ohne Probe-Anfrage prüfen.
5. Vorabnachweise und vollständige V-MAC.json ergänzen, über paket.py seal
   als V-FIXIERT.json sichern und vor A1 separat datiert aufbewahren.

Schrittfolge und Slotformulare sind im separaten Hilfspaket vorbereitet.
Lokale Hashfixierung ersetzt keine unabhängige Zeitbeglaubigung. Noch offene
Mac-Angaben sind keine gemessenen Werte. Keine Startbehauptung aus einem Build.
