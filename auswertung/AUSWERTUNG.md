# PC-Auswertung, Fassung W-1.1

Korrekturfassung vom 31.10.2026 mit tatsächlichem Aufnahmezeitpunkt und neuen
Hashes in WERKZEUGSTAND.json. Der frühere Nachweis bleibt bytegleich unter
historie/WERKZEUGSTAND-W-1.0.json erhalten; dessen Dateihashes beziehen sich
auf den früheren Thesis-Stand 45b020a. Kriterien, Regelsatz, Ausgangscode und
Ledger-Tests bleiben unverändert. Die korrigierte Implementierung akzeptiert
echte Credit-Nullstände und hält Erhebung, Übernahme und Tests getrennt.

Auswahl nach dem am 31.10.2026 dokumentierten K-Nachweis
`../vorbereitung/K-VERSIONSNACHWEIS.json`, vor jeder Modellanfrage.
K-Kern und historisches Manifest bleiben unverändert. Keine Regelwahl anhand
von Baseline-Meldungszahlen; Auswahlzweck ist S03, keine Stiloptimierung.

## Feste Verfahren

- Python 3.13.14, vollständiger Build/Windows-Stand in `environment.json`.
  `unittest`, `ast` und `tokenize` aus genau dieser Standardbibliothek.
  Abweichender Interpreter oder Ruff-/OS-Stand stoppt den Auswertungsaufruf.
- F01: elf unveränderte `unittest`-Tests in temporärem Ordner, bytegleiche
  Kopien als ledger.py und ledger_test.py, isolierter Python-Aufruf `-I`.
  Vollbericht, gesammelt/ausgeführt/bestanden/Fehler/Fehlschlag/Skip getrennt.
  Importfehler ist Startfehler ohne Bestehenszahl. Sollzahl ungleich elf
  ergibt Prüfproblem. 60 Sekunden Prozesslimit, danach Abbruch mit Teilbericht.
- S03: Ruff **0.14.14**, ausschließlich vollständige stabile Pyflakes-Familie
  `F` dieser Version. Zweck: Namen, Imports, Bindungen und Kontrollfluss;
  keine Stil-, Längen-, Komplexitäts- oder prognostizierten Schuldkosten.
  Konfiguration `ruff.toml`; keine Preview, Fixes, per-file-Ignores,
  Git-Ausschlüsse oder Cache. `--ignore-noqa` verhindert ausgabeabhängige
  Unterdrückung. Nur ledger.py prüfen, niemals Tests mitbewerten.
  Vollständiger Regelkatalog `ruff-rules.json`, effektive Einstellungen
  `ruff-settings.txt`. Jeder Rohhinweis benötigt manuelle Prüfung nach S03;
  `confirmed_count` bleibt bis dahin fehlend. Ruff ordnet keine universelle
  Schwere zu; diese ist als nicht ausgewiesen zu dokumentieren.
- U01/U02: `scripts/ledger_study.py`, exakt die Zählkonventionen K-1.0.
  Bytes einschließlich BOM, UTF-8-SIG-Dekodierung nur für Textzählung,
  `splitlines`, Leerraumprüfung, reine COMMENT-Tokenzeilen, `ast.stmt`.
  Alle def/async def/class mit Container, Dekoratoren, Start-/Endzeile.
  Kategorie module/method/nested ist exklusiv je Definition; nested als
  zusätzliche Kennzeichnung überlappt und wird nicht dazugerechnet.
  Methoden sind in Funktionen enthalten. Funktionsspannen überlappen.
  Keine Lambdas oder erfundene Komplexitätskennzahl. Physische Werte bleiben
  bei Syntaxfehler erhalten; Parser-/Tokenfehler geben fehlende Werte mit Grund.
  Messprozess und Ruff erhalten jeweils ebenfalls 60 Sekunden Limit.
- Keine zusätzlichen automatisierten Ledger-Fälle: F02/P01–P04 und
  S01/S02/B01–B03 bleiben begründete manuelle Codeprüfungen. Dafür liegt
  `MANUELLE-PRUEFUNG.md` bereit. Alle sieben Artefakte gleich prüfen.

Offizielle Werkzeugreferenzen, abgerufen 31.10.2026:
[Ruff-Regeln](https://docs.astral.sh/ruff/rules/) und
[Konfiguration](https://docs.astral.sh/ruff/configuration/).
Die archivierte Ausgabe der festgelegten Version ist für den konkreten
Regelbestand maßgeblich, nicht eine später veränderte Website.

## Aufrufe im Thesis-Stamm unter Windows

Einrichtung ist lokal bereits erfolgt. Bei Wiederherstellung zuerst den
festgelegten Python-Build bereitstellen, dann:

```powershell
python -m venv .venv-ledger
.\.venv-ledger\Scripts\python.exe -m pip install -r versuch/auswertung/requirements.txt
```

Rückgabe-ZIP außerhalb des Thesis-Repos entpacken. Keine ausgefüllten Nachweise
in das öffentliche Hilfs-Repository hochladen. Prüfung und Extraktion:

```powershell
.\.venv-ledger\Scripts\python.exe scripts/ledger_study.py import --return-dir C:/Pfad/Rueckgabe --out versuch/lokal/import-01
.\.venv-ledger\Scripts\python.exe scripts/ledger_study.py pc-template --imported versuch/lokal/import-01 --out versuch/lokal/pc-zeiten-01.json
.\.venv-ledger\Scripts\python.exe scripts/ledger_study.py evaluate --imported versuch/lokal/import-01 --out versuch/lokal/auswertung-01
```

Neue Berichtsordner müssen noch nicht existieren; vorhandene Berichte werden
nicht überschrieben. Wiederholung nur mit Anlass und neuem Namen dokumentieren.
Rohantwort bleibt unverändert, genau ein vollständiger python/py-Block wird
nach manueller Vollständigkeitsentscheidung extrahiert. Leere/mehrdeutige oder
unklare Ausgaben werden nicht repariert und erscheinen weiter in der Übersicht.
Ein formal eindeutiger, aber syntaktisch falscher vollständiger Block bleibt
prüfbar. Importprüfung kontrolliert V-Dateihashes, Kennungen und Zeitintervalle;
Warnungen bleiben sichtbar, sie ersetzen keine fachliche Protokollprüfung.

`overview.json` enthält BASE und alle sechs Slots, `absolute-differences.json`
Umfangsdifferenzen, `descriptive-summary.json` Einzelwerte/n/Median/Minimum/
Maximum nur verfügbarer Größen. Bei n=1 keine Variationsaussage.
Je Artefakt: Code-/Test-/Konfigurationshash, Rohberichte, Prozessstatus und
technische Laufzeit. Keine menschliche Prüfzeit aus Laufzeit ableiten.

`collection_status` erhält den dokumentierten Ablauf/Abbruch (z. B. zeitlimit),
`extraction_status` die Codeübernahme (z. B. extrahiert/keine_ausgabe),
`technical_status` die Ausführbarkeit (z. B. syntaxfehler/startfehler/ausgefuehrt).
Die vollständigen Testergebnisse stehen separat unter tests. Diese Angaben
sind in import.json, overview.json und overview.csv unterscheidbar; ein
Zeitlimit wird auch mit einem vollständigen Codeblock nicht zum normalen Lauf.
Importdaten enthalten die beiden ersten Status, die technische Stufe folgt
erst bei Auswertung. Rohprotokoll einschließlich Fehlern/Abweichungen bleibt erhalten.

## PC-Zeiten getrennt nachtragen

Mac-Rückgabe einschließlich rueckgabe-hashes.json nach Übertragung unverändert
lassen. Ergänzungen gehören **außerhalb** der Rohdaten und des Importordners
in die mit pc-template angelegte pc-zeiten-01.json. Diese Datei ist über
import_sha256 an genau diesen Import gebunden. Kein echter Versuch ist in
der Vorlage ausgefüllt. Eine neue Vorlage überschreibt keine bestehende Datei.

Vor dem Import die tatsächliche aktive Bedienung für Übertragung/Codeübernahme
mit Zeitpunkten und Stoppuhr erfassen, nicht später aus Prozesslaufzeiten schätzen.
Nach Import je Slot die Sicherung und Sichtkontrolle seiner extrahierten Datei
einzeln bearbeiten und diese aktive Bedienung separat messen. In die Vorlage
die wirklich gemessenen Teilintervalle übertragen. Gemeinsame Einrichtung bzw.
Sammelbedienung getrennt als gemeinsame Vorbereitung dokumentieren und bei
Kosten gegebenenfalls einheitlich über common_eur berücksichtigen; dieselben
Minuten niemals sechsfach als Slotbedienung eintragen.

Die technische Auswertung kann zunächst ohne --pc-times laufen; Bedienung nach
Antwort und Prüfung bleiben dann bewusst fehlend. Beim tatsächlichen Prüfen
jedes Artefakts (BASE, A1, B1, A2, B2, A3, B3) Stoppuhr/Zeiten erfassen,
inklusive begründeter manueller Codeprüfung. Nicht allein die Prozessdauer
übernehmen. Inaktive Pausen aus aktiven Intervallen ausschneiden.

Pro Eintrag unter artifacts/KENNUNG/intervals angeben:
artifact_id, eindeutige interval_id, phase, start/end mit Zeitzone, seconds,
method und origin (konkretes Zeitprotokoll/Notiz als Herkunft). Erlaubte
PC-Phasen: bedienung_nach für Extraktionsbedienung, pruefung, unterbrechung.
Für BASE nur pruefung/unterbrechung. Die Intervallvorlage enthält keine Zahlen:

```json
{"artifact_id":"A1","interval_id":null,"phase":"pruefung","start":null,"end":null,"seconds":null,"method":null,"origin":null}
```

Unter phase_complete nur dann true setzen, wenn die betreffende PC-Arbeit
vollständig gemessen ist. coverage_note beschreibt Abdeckung, Messquelle und
etwaige Lücken. Die Mac-Flags bleiben unverändert und beschreiben deren lokale
Teilintervalle. Unvollständige Mac-Bedienung wird durch einen PC-Nachtrag nicht
nachträglich vollständig. Die regulär erst am PC beginnende Prüfung braucht
keine erfundene Mac-Prüfzeit. Ein true-Flag ohne gemessenes Intervall ergibt
keinen Nullwert. Fehlende Angaben bleiben fehlend.

```powershell
.\.venv-ledger\Scripts\python.exe scripts/ledger_study.py evaluate --imported versuch/lokal/import-01 --pc-times versuch/lokal/pc-zeiten-01.json --out versuch/lokal/auswertung-mit-zeiten-01
```

Für einen späteren Anlass einen neuen Berichtordner verwenden. Die Auswertung
prüft Importbindung, Kennungen, Zeitzonen, Dauer, Herkunft, eindeutige IDs und
Überschneidungen über Artefakte, Phasen und Mac/PC hinweg. human-times.json
enthält alle verwendeten Intervalle mit Herkunft, Dateihashes, Phasensummen
und Fehlgründen; pc-times-source.json hält die verwendete Ergänzungsfassung
fest. overview.json/csv zeigen die zusammengeführten Messwerte und die
gesonderte BASE-Prüfzeit. BASE-Zeit wird nicht bei jedem Slot erneut addiert.

## Kosten nur mit ausdrücklich belegten/angenommenen Parametern

`kostenparameter.json` ist leer vorbereitet, alle Felder zunächst null.
Pro Slot Euro-Stundensatz, Wartebindungsanteil, gleiche gemeinsame Kosten,
zugeordnete Lizenzkosten, variable Nutzungskosten sowie zusätzliche Arbeit,
Nacharbeit und Wartung in Minuten samt Begründung eintragen.
Kein Automatismus Credits × API-Preis. Bereits abgegoltene Nutzung nicht
zusätzlich berechnen. Gleiche Vergleichsgrenze und Wartungshorizont belegen.

```powershell
.\.venv-ledger\Scripts\python.exe scripts/ledger_study.py evaluate --imported versuch/lokal/import-01 --pc-times versuch/lokal/pc-zeiten-01.json --parameters C:/Pfad/kostenparameter.json --out versuch/lokal/auswertung-kosten-01
```

Rechnung entsprechend Kapitel 6: gemeinsame Kosten + Lizenz + variable Nutzung
+ Stundensatz/60 × (Bedienungsminuten + beta × Warteminuten + Prüfminuten
+ nicht gemessene Arbeitsminuten + Nacharbeit + Wartung). Sekunden werden
zunächst durch 60 geteilt. Fehlende Messung oder Annahme ergibt null im JSON
im Sinn von **fehlend**, niemals Zahl 0. Kosten bleiben bedingte Szenarien,
Qualitätsstatus daneben; keine Siegernote oder empirische Zeitersparnis.
Parameterkopien mit begründet variierten Werten und jeweils eigenem Bericht
erlauben Sensitivitätsrechnung ohne vorgegebene Fantasiebeträge.
