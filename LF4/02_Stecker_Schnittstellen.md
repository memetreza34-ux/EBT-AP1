# LF4 – Lektion 2: Stecker, Buchsen und Schnittstellen erkennen

**Schwerpunkt:** Aussehen, Aufgabe, Gerät und Verwechslungsgefahr.  
**Ziel:** Anschlüsse nicht nur auswendig benennen, sondern **an einem realen PC identifizieren** und passend auswählen.

## 1. Drei Begriffe, die man trennen muss

- **Stecker/Buchse (Bauform):** Wie sieht der physische Anschluss aus? Beispiel: USB-C, RJ45-/8P8C-Bauform.
- **Schnittstelle / Übertragungsstandard:** Welche elektrischen und logischen Regeln gelten? Beispiel: USB 2.0, USB4, Ethernet.
- **Protokoll:** Nach welchen Regeln sprechen Geräte miteinander? Beispiel: TCP/IP oder NVMe.

**Prüfungsfalle:** **USB-C beschreibt die Form**, nicht automatisch die Geschwindigkeit oder die verfügbaren Funktionen. **M.2 beschreibt eine Modul-/Steckverbinder-Bauform**, NVMe ein Protokoll für entsprechende Speichergeräte.

## 2. Externe Anschlüsse

| Anschluss | Erkennungsmerkmal (vereinfacht) | Typischer Zweck | Verwechslung vermeiden |
|---|---|---|---|
| USB-A | rechteckige Buchse, nicht rotationssymmetrisch | USB-Geräte wie Maus, Stick, Tastatur | Form ≠ USB-Version |
| USB-B | annähernd quadratisch, oft abgeschrägte Ecken | häufig Drucker / ältere Peripherie | nicht USB-A |
| USB-C | klein, oval, beidseitig steckbar | Daten, teils Strom, teils Video | Video/Leistung nur wenn unterstützt |
| HDMI | flacher trapezförmiger Anschluss | digitale Bild- **und** Tonübertragung | nicht DisplayPort |
| DisplayPort | meist rechteckig, eine abgeschrägte Ecke | digitale Bild-/Tondaten | Steckerform von HDMI unterscheiden |
| VGA (DE-15) | 3 Reihen mit insgesamt 15 Kontakten, oft blau | analoges Bildsignal | kein natives digitales Video |
| DVI | breite Kontaktfläche mit vielen Pins | ältere Videoverbindungen; je nach DVI-Typ digital und/oder analog | DVI-A, DVI-D, DVI-I unterscheiden |
| Ethernet 8P8C (oft „RJ45“) | breiter 8-poliger Modularstecker mit Rastnase | drahtgebundenes LAN | ähnelt kleinerem Telefonstecker |
| 3,5-mm-Klinke | runder Stift/Klinkenbuchse | analoges Audio | Belegung/Ein-/Ausgang beachten |
| PS/2 (älter) | runder Mini-DIN-Anschluss | ältere Maus/Tastatur | kein USB |
| RS-232/DE-9 (älter/Industrie) | 9-poliger D-Sub-Anschluss | serielle Kommunikation | nicht VGA |
| IEC C13/C14 | dreipoliger Geräte-Netzanschluss | Stromversorgung typischer PC-Netzteile | **Netzspannung!** nicht Daten |

**Hinweis:** Die Tabelle beschreibt typische Formen. Es gibt Mini-/Micro-Versionen und andere Sonderbauformen. Ein USB-C-Port kann allein durch seine Form keine spezielle Datenrate, Bildausgabe oder Ladeleistung garantieren.

## 3. Interne Anschlüsse und Bauteilbauformen

| Schnittstelle/Bauform | Wo? | Typische Aufgabe |
|---|---|---|
| **SATA-Datenanschluss** | Mainboard zu Laufwerk | Überträgt Laufwerksdaten |
| **SATA-Stromanschluss** | Netzteil zu Laufwerk | Versorgt kompatibles Laufwerk mit Strom |
| **M.2-Steckplatz** | Mainboard | z. B. SSD oder Netzwerkmodul; Key/Bauform/Protokoll prüfen |
| **PCIe-Steckplatz** | Mainboard | Erweiterungen, z. B. Grafikkarte oder Netzwerkkarte |
| **DIMM-Slot** | Mainboard | passende RAM-Module |
| **CPU-Sockel** | Mainboard | passend unterstützter Prozessor |
| **ATX-Stromstecker / CPU-Versorgung** | Netzteil zu Mainboard | Stromversorgung, nicht Datenschnittstelle |

**Fehler vermeiden:** Eine SSD mit SATA-Anschluss braucht Daten**und** Stromversorgung. Ein M.2-NVMe-Modul benötigt normalerweise kein separates SATA-Datenkabel.

## 4. So erkennst du Stecker zuverlässig

Bei einem Foto oder echten Anschluss nacheinander prüfen:

1. **Form**: eckig, oval, rund, trapezförmig, abgeschrägte Ecke?
2. **Kontakte**: wie viele Reihen, Pins, Rasten, Kerben?
3. **Größe und Einbauort**: hinten am PC? Direkt auf dem Mainboard?
4. **Verwendung**: Netzwerk, Bild, Audio, Daten oder Energie?
5. **Beschriftung / Spezifikation**: Was unterstützt **dieser konkrete Port**?

**AP1-Trickfrage:** „Kann jeder USB-C-Anschluss einen Monitor betreiben?“ – **Nein**, Videofunktion muss unterstützt werden.

## 5. Bild-Lernkarten (im nächsten Gespräch mit echten Abbildungen bearbeiten)

Die Datei ist das **Erkennungsraster**. Für jede Schnittstelle sollte im Unterricht/Chat eine tatsächlich passende, überprüfte Abbildung gezeigt werden; die Form sollte zunächst **ohne sichtbares Label** erkannt werden. Danach Aufgaben:

- Bild A: USB-A, USB-C oder HDMI? Formmerkmale nennen.
- Bild B: HDMI oder DisplayPort? Abgeschrägte Kante/Form beschreiben.
- Bild C: Ethernet 8P8C oder Telefon-Modularstecker?
- Bild D: SATA-Datenkabel oder SATA-Stromkabel?
- Bild E: M.2-SSD oder DIMM-RAM?
- Bild F: 3,5-mm-Klinke, PS/2, DE-9?

**Qualitätsregel:** Für Form-Erkennung **keine KI-Bildfantasie als technischen Beleg** verwenden. Wenn eine Abbildung Kontaktzahlen/Kerben falsch zeigt, nicht zum Lernen benutzen. Hersteller- und Lehrmittel-Fotos bevorzugen.

## 6. Aufgaben

1. Unterschied USB-A und USB-C: Was beschreibt der Name?
2. Zwei Anschlussarten für digitale Monitorübertragung?
3. Welcher Stecker für kabelgebundenes Ethernet am PC?
4. Kann HDMI nur Bild übertragen?
5. Ist VGA eine digitale oder analoge Bildschnittstelle?
6. Welche **zwei** Anschlüsse braucht eine typische 2,5-Zoll-SATA-SSD?
7. Warum passt nicht jede beliebige SSD zu jedem M.2-Steckplatz?
8. Was ist PCIe, was ist ein RAM-DIMM?
9. Ein Monitor bleibt schwarz: Nenne drei sichere, systematische Prüfpunkte.
10. In einem Foto sieht ein Port wie USB-C aus: Was kannst du **nicht** allein aus dem Aussehen schließen?

**Danach:** [Lektion 3 – Daten und Zahlensysteme](03_Daten_Zahlensysteme.md).