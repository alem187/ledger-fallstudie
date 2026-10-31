# Was pro Slot gespeichert wird

`protokoll.json` mit Texteditor bearbeiten. Leere Werte nicht durch 0 ersetzen.
Zeitformat mit Zeitzone, z. B. `2026-10-31T14:00:00+01:00` (nur Formatbeispiel).

- slot unverändert lassen; status konkret benennen (durchgefuehrt, zeitlimit,
  produktfehler, keine_antwort, nicht_durchgefuehrt).
- actual_model: tatsächlich sichtbarer Name, kein aus Plan übernommenes Label.
- settings: tatsächlicher Stand/Verweis auf V und Abweichungen; context_evidence
  verweist auf Screenshot der vier Anhänge vor dem Senden.
- sent_at/answer_end_at: echte Zeitpunkte, Fehlerende bei Abbruch.
- response_method und chat_id: vollständiger Export/Kopie und verfügbare Kennung.
- Vollständige Rohantwort einschließlich Zäunen in rohantwort.md; Originalexport
  daneben aufbewahren. Keine Inhalte umschreiben.
- code_completeness: vollstaendig/unvollstaendig/unklar nach Sichtung.
  Das ist nur Übernahmevollständigkeit, keine Aussage über Syntax oder Richtigkeit.
- credits_before/after: numerische Ablesungen oder null; credit_direction ist
  used bei kumuliert verbraucht, remaining bei verbleibend. Einheit und Quelle,
  Auflösung, Ablesezeitpunkte, Aktualisierung und Screenshotpfade angeben.
  credits_assignable nur true bei gesicherter Zuordnung, ausreichender Auflösung
  und ausgeschlossener paralleler Nutzung. Sonst false und credit_missing_reason.
- intervals: pro disjunktem Teilintervall Objekt mit phase, start, end, seconds,
  method und note. Zulässige Phasen: bedienung_vor, warten, bedienung_nach,
  pruefung, unterbrechung. Keine Lücken als Null interpretieren.
- phase_complete: je Phase erst true setzen, wenn alle zugehörigen Teilintervalle
  am Mac vollständig erfasst sind. Bei false bleibt ihre Summe fehlend.
  Spätere PC-Zeiten getrennt über pc-template/--pc-times ergänzen; gesicherte
  Mac-Protokolle und Rückgabehashes niemals nachträglich ändern.
- deviations und errors: alle Abweichungen/Fehler mit Zeitpunkt und Grund.

Numerische Credit-Zählerstände von 0 sind gültig; null bedeutet fehlend,
false ist kein Zählerstand. Gesicherte Zuordnung und Nachweise bleiben nötig.
Die Auswertung erhält status als collection_status und berichtet die spätere
Codeübernahme unter extraction_status; zeitlimit/produktfehler bleiben sichtbar.

Intervalleintrag (Werte durch tatsächliche Messung ersetzen, keine Fantasiezeiten):

```json
{"phase":"bedienung_vor","start":null,"end":null,"seconds":null,"method":null,"note":null}
```

Fehlgeschlagene Slots behalten ihren Ordner und alle verfügbaren Nachweise.
Keine Codekorrektur, keine Wiederholung, keine Auswahl unter mehreren Varianten.
