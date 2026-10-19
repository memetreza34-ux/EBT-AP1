# LF4 – Lektion 8: Systematisch Fehler finden und sauber dokumentieren

**Ziel:** IT-Störungen sicher, nachvollziehbar und methodisch eingrenzen; Prüfung und Übergabe nach Kundenauftrag.

## 1. Nicht raten – systematisch eingrenzen

Vorgehen:
1. **Symptom exakt erfassen:** Was klappt nicht, seit wann, bei allen Benutzern?
2. **Änderungen prüfen:** Neues Gerät, Update, Kabel, Zugangsdaten?
3. **Hypothesen aufstellen:** Hardware, Stromversorgung, Treiber, Netzwerk, Berechtigung?
4. **Gefahrlos testen:** Zuerst Sicht-/Statuskontrolle und softwarebasierte Diagnose, dann fachlich zulässige Schritte.
5. **Eine Variable ändern:** Sonst ist die Ursache schwer nachweisbar.
6. **Funktion und Nebenwirkungen prüfen:** Funktioniert auch der Rest?
7. **Maßnahmen dokumentieren, Nutzer einweisen.**

**Sicherheit:** PC-Netzteile können auch nach Abziehen des Netzkabels gefährliche gespeicherte Energie enthalten. Nicht öffnen; Netzspannungsarbeiten nur durch befugte Elektrofachkräfte unter passenden Bedingungen.

## 2. Typische Symptome und sinnvolle erste Fragen

| Symptom | Mögliche Ursachen | Sinnvolle erste Kontrolle |
|---|---|---|
| PC startet nicht | Versorgung, Kabel, Netzteil, Hardware | Statusanzeige, Steckverbindung, bekannte sichere Versorgungsbedingungen |
| Bildschirm bleibt schwarz | Eingang, Monitor, Kabel, Grafikausgabe | Ist Monitor an? Richtiger Eingang? Kabel? |
| USB-Gerät funktioniert nicht | Kabel/Port, Treiber, Rechte | Anderer kompatibler Port, Gerätestatus |
| PC hat kein Netzwerk | Kabel/WLAN, Adapter, DHCP, Gateway | Link, IP-Konfiguration, LAN-Test |
| Webseiten nicht per Namen erreichbar | DNS-Konfiguration/-Dienst | IP-Verbindung vs. Namensauflösung unterscheiden |
| Drucker druckt nicht | Queue, Verbindung, Treiber, Rechte | Status, Testseite, Netzwerkverbindung |
| Daten nicht gefunden | Speicherort, Dateirechte, Backup | Suchpfad, Benutzerkonto, Versionen |

**Hinweis:** Dies sind Hypothesen, keine Diagnosen ohne Messung/Test.

## 3. Funktions- und Abnahmeprüfung

Am Pflichtenheft messen, nicht am Bauchgefühl:

- PC startet zuverlässig.
- Alle vereinbarten Geräte werden erkannt.
- Anwendung öffnet Testdaten.
- Netzwerkverbindung zu den vorgesehenen Ressourcen funktioniert.
- Drucker/Testausgabe funktioniert.
- Backup/Wiederherstellung nach Konzept geprüft.
- Benutzerrechte korrekt.
- Kundin/Kunde kann vereinbarte Grundfunktionen nutzen.

## 4. Protokollvorlage

```text
Auftrag / Kunde: _________________________
Gerät / Inventarnummer: __________________
Datum / ausführende Person: ______________
Anforderungen / Soll: ____________________
Hardware (Typ / Serienbezug): ____________
Betriebssystem / Versionsstand: ___________
Software / Lizenznachweis: ________________
Schnittstellen und Netzwerk: ______________
Sicherheits-/Backupmaßnahmen: ____________
Tests: Testfall | Soll | Ist | Ergebnis
Abweichungen / Fehlerursache: ____________
Abhilfe / Nachtest: _______________________
Einweisung und Übergabe: ________________
Hinweis: keine Passwörter im Protokoll.
```

## 5. Berichte und Präsentation

- Ergebnisse verständlich, kurz, nachweisbar und adressatengerecht darstellen.
- Fachbegriffe korrekt verwenden, bei Kunden gegebenenfalls erläutern.
- Tabellenkalkulation für Kosten, Textverarbeitung für Protokoll, Grafik/Präsentation für Abläufe.
- Beschreibungen sollen einen zweiten Techniker zur nachvollziehbaren Diagnose befähigen.

## 6. Übungen

1. Warum testest du nicht fünf Änderungen gleichzeitig?
2. Drucker wird im Netzwerk angezeigt, druckt aber nicht. Nenne drei Ursachen.
3. Warum ist eine erfolgreiche Funktionsprüfung mehr als „PC geht an“?
4. Welche sechs Angaben gehören mindestens in ein Übergabeprotokoll?
5. Warum sollst du Passwörter nicht offen dokumentieren?
6. Ein PC erreicht seine lokale IP, aber keinen Domainnamen. Was ist eine mögliche Ursache, und wie grenzt du sie ein?

**Danach:** [LF4-Gesamtübung](09_AP1_Probetraining.md).