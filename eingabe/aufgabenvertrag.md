# Aufgabenvertrag Ledger

Fassung AV 1.0, 31. Oktober 2026. Inhaltlich ausgearbeitet; Bestandteil des
vorbereiteten Kriterienstands K-1.0, noch kein nachgewiesener Freeze.
Für Ausgangsversion und alle sechs Ausgaben gilt derselbe Vertrag.

## Grundlage und Vorrang

**Originalvorgabe:** `upstream/instructions.md` und `description.md` verlangen
ein Refactoring eines Ledger-Druckers für amerikanische/niederländische
Locale und Dollar/Euro. Sie nennen weder eine eindeutige Sortierhierarchie
noch die Behandlung der Eingabeliste. Die elf unveränderten Python-Tests
legen konkrete Aufrufe und Ausgabezeichenfolgen fest. Die kanonische Datei
enthält zwölf Fälle; `tests.toml` schließt den älteren Beschreibungsfall
`502c4106-0371-4e7c-a7d8-9ce33f16ccb1` aus und bindet dessen Ersatz ein.
Die elf eingeschlossenen Fälle entsprechen den elf Testmethoden.
`herkunft.json` nennt die vollständigen Versionen und Prüfsummen.

Die am 31.10.2026 zusätzlich gelesene historische
[README am Ausgangscommit](https://raw.githubusercontent.com/exercism/python/190407706124bff6fe56d39dba424108982a5bb5/exercises/ledger/README.md)
enthält ebenfalls keine weitergehende Sortier- oder Mutationsregel. Ihr
allgemeiner Abschnitt zu Fehlermeldungen definiert keinen Ledger-Fehlerfall.
Der [ursprüngliche PR #1408](https://github.com/exercism/python/pull/1408)
erklärt die bewusst ungünstige Refactoring-Vorlage und die Herkunft der Tests.
Der [Implementierungscommit](https://github.com/exercism/python/commit/169f56d503c08bff650e892cf53e68dfde26f4c8)
zeigt Sortiervergleiche und `pop`; er macht diese Beobachtung nicht zu einer
ausdrücklich formulierten Exercism-Anforderung.

**Eigene Studienentscheidung:** Die expliziten Sollausgaben des fixierten
Testkorpus bleiben maßgeblich (R01–R02). Wo dieser Korpus keine eindeutige
Regel liefert, wird innerhalb der unten abgegrenzten Eingaben das beobachtbare
Verhalten der unveränderten historischen Vorlage erhalten (R03–R05).
Dies begrenzt den Vergleich auf Refactoring. Eine fachlich plausiblere
Ausgabe oder schonendere Eingabebehandlung darf nicht stillschweigend die
Vergleichsbasis ersetzen. Ein bisher nicht erkannter Konflikt mit einem
expliziten Sollwert wäre vor Erhebung zu klären; nach Erhebung wird er als
Grenze/Abweichung dokumentiert, ohne den Vertrag rückwirkend umzuschreiben.

## Verbindliche Regeln für den Untersuchungsumfang

| ID | Regel | Herkunft und Nachweis |
|---|---|---|
| R01 | Die öffentlichen Aufrufe `create_entry(date, description, change)` und `format_entries(currency, locale, entries)` mit diesen Parametern bleiben verfügbar. Ein von `create_entry` erzeugter Eintrag muss an `format_entries` übergebbar sein. | Aufrufe im vorhandenen Python-Testkorpus. Eigene Abgrenzung: konkrete Klasse, Attribute, Objektidentität und direkte Nutzung von `LedgerEntry` sind keine zusätzliche öffentliche API. |
| R02 | Alle elf vorhandenen Tests bleiben unverändert; deren vollständige Sollstrings einschließlich Leerzeichen, Überschriften, Datum, Vorzeichen, Währungssymbol, Kürzung und Zeilenumbrüchen gelten. | Python-Tests und kanonische Fälle; F01 berichtet nur deren tatsächliche Ausführung. |
| R03 | Sortierung aufsteigend nach Datum, dann numerischem `change`, dann vollständiger Beschreibung nach Python-Stringvergleich. Erst nach der Sortierung wird für die Ausgabe gekürzt. | Beobachtung: `baseline.py`, beide Abschnitte „Find next entry in order“. Als eigene Verhaltenserhaltungsentscheidung verbindlich, keine behauptete Exercism-Spezifikation. |
| R04 | Nach erfolgreichem `format_entries` ist die ursprünglich übergebene Liste leer, auch über einen Alias betrachtet. Die enthaltenen Einträge werden dabei nicht inhaltlich verändert. Eine anfangs leere Liste bleibt leer. Anzahl und Zeitpunkt interner Entfernschritte sind nicht vorgegeben. | Beobachtung: beide `while`-/`pop`-Pfade der Vorlage und ausschließlich lesende Zugriffe auf Eintragsfelder. Eigene Festlegung des beobachtbaren Endzustands; keine Originalanforderung an Mutation. |
| R05 | Innerhalb des Untersuchungsumfangs bleibt der zurückgegebene String der Vorlage erhalten, auch bei nicht durch R02 erfassten Formatbesonderheiten. Keine stillschweigende Fehlerkorrektur an Gruppierung, Rundung oder Auffüllung. | Eigene Refactoring-Abgrenzung. Insbesondere fügt die Vorlage bei mehrteiligen Ganzzahlgruppen keine führenden Nullen innerhalb einer Gruppe ein. Ein Wechsel zu konventioneller Geldformatierung kann deshalb Verhalten ändern. Dies ist kein Nachweis fachlicher Richtigkeit der Vorlage. |
| R06 | Keine neuen fachlichen Funktionen oder externen Abhängigkeiten verlangen; interne Datenstruktur, Helfer und Standardbibliothek dürfen wechseln, sofern R01–R05 erhalten bleiben. | Eigene einheitliche Studienbedingung; kein pauschales Verbot zusätzlicher Funktionen oder Klassen. |

**Abgegrenzte Eingaben (eigene Studienentscheidung):** `currency` ist `USD`
oder `EUR`, `locale` ist `en_US` oder `nl_NL`, in allen vier Kombinationen.
`entries` ist eine gewöhnliche Python-Liste von über `create_entry` erzeugten
Einträgen; auch leere Listen, gleiche Datumswerte und Duplikate gehören dazu.
Datum: gültiges Kalenderdatum als zehnstelliger String `YYYY-MM-DD`.
Beschreibung: gewöhnlicher String ohne Steuerzeichen; Länge wird wie in der
Vorlage in Python-Zeichen gezählt, nicht nach visueller Displaybreite.
`change`: vorzeichenbehaftete ganze Centzahl (kein bool), für die die Vorlage
ohne Überlauf oder Ausnahme terminiert. Es wird weder eine neue
Bank-/Dezimalpräzisionsanforderung noch ein Geldbetragsgrenzwert erfunden.

Nicht Gegenstand: ungültige Datumswerte, unbekannte Locale-/Währungscodes,
falsche Typen, `None`, Fremdobjekte, Listenunterklassen, Generatoren,
nebenläufige Listenänderung, direkte Attributmanipulation, Überläufe und
Fehlerzustände während eines abgebrochenen Aufrufs. Dafür sind weder konkrete
Ausnahmen/Fehlermeldungen noch partielle Mutation zu erhalten oder neu
einzuführen. Verhalten dort wird nicht als F02-Vertragsverletzung bewertet.
Zusätzliche Validierung ist jedoch auf ihren Beitrag und ihre Abhängigkeiten
nach B01–B03 prüfbar; ihr bloßes Vorhandensein beweist kein Bloating.

## Sortierkonflikt und zulässige Aussage

Die Namen `multiple_entries_on_same_date_ordered_by_description` und
`final_order_tie_breaker_is_change` legen Datum → Beschreibung → Betrag nahe.
Der erste Fall (kanonische UUID `9c70709f-cbbd-4b3b-b367-81d7c6101de4`)
ordnet „Buy present“/−1000 vor „Get present“/+1000; beide Hierarchien liefern
dasselbe. Im Tie-Breaker-Fall (`29dd3659-6c2d-4380-94a8-6d96086e28e1`)
sind Datum und Beschreibung gleich; auch er trennt die Hierarchien nicht.
`tests.toml` ersetzt den älteren Beschreibungsfall, ergänzt aber keine
unterscheidenden Daten. Testnamen bleiben ein ernstzunehmender Gegenhinweis,
jedoch keine durch die Sollstrings entschiedene Priorität.

Eine Umstellung auf Beschreibung vor Betrag wäre gegenüber R03 eine
Verhaltensänderung und möglicherweise eine Fehlerkorrektur im Sinne dieser
Testnamen. Die Studie verlangt sie nicht. Ebenso wäre eine unveränderte
Eingabeliste gegenüber R04 eine Änderung des aufruferseitig sichtbaren
Verhaltens. Diesen Seiteneffekt beizubehalten ist keine Empfehlung für neue
Software. Die Studie untersucht bewusst ungünstigen Übungscode und keine
repräsentative professionelle manuelle Lösung.

## Vorab festgelegte ergänzende Codeprüfung F02

Keine neuen automatisierten Tests, keine Ersatzimplementierung. Dieselben
folgenden manuellen Pfadprüfungen werden an allen sieben Artefakten
dokumentiert. Jede benötigt Codeposition, Soll, hergeleitetes Ist,
Gegenargument und Status. Herleitung ist kein gemessener Testlauf.

| Kennung | Feste Eingabesituation / Prüffrage | Soll und Zuordnung |
|---|---|---|
| P01 | Datum `2015-01-01`, Eingangsreihenfolge Beschreibung `A`, change +100; Beschreibung `Z`, change −100. | `Z` vor `A`; R03. Trennt Betrag- von Beschreibungspriorität. |
| P02 | Gleiches Datum und change 0, Eingangsreihenfolge `Z`, `A`; zusätzlich dieselben Felder doppelt. | `A` vor `Z`, keine Einträge verlieren; Reihenfolge vollständig identischer Einträge ohne sichtbaren Unterschied ist kein Zusatzkriterium; R03. |
| P03 | Liste mit einem regulären Eintrag, zweiter Verweis auf dieselbe Liste; Aufruf je Locale-/Währungskombination. | Beide Verweise danach leer; Eintragsdaten unverändert; zweiter Aufruf mit derselben Liste liefert nur Header; R04/R02. |
| P04 | Datum, positive/negative/Null-Centwerte, Beschreibungslängen unter/genau/über 25 und alle vier Formatkombinationen am Code verfolgen. Gruppierung zusätzlich bei change 100001 nachvollziehen. | Datum und Ausgabe wie Vorlage: bei über 25 Zeichen erste 22 plus drei Punkte; unter 25 rechts auffüllen. Bei 100001 entsteht `1,0.01` (en_US) bzw. `1.0,01` (nl_NL) als Zahlenteil; keine Korrektur auf dreistellige Untergruppe verlangen; R02/R05. |

Vollständige Pfadnachweise werden später im Befundformular erfasst. Wo eine
Herleitung (etwa dynamischer Zugriff) nicht belastbar gelingt, lautet F02
`unklar`; wo nicht geprüft, `nicht_untersucht`. Testbestehen F01 und
F02-Vertragsbefund stehen unabhängig nebeneinander. Der begrenzte
Prüfumfang belegt keine Äquivalenz für sämtliche zugelassenen Eingaben.
