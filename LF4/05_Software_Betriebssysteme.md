# LF4 – Lektion 5: Betriebssystem, Software und Konfiguration

**Ziel:** Ein IT-System sinnvoll vorbereiten, Softwarearten unterscheiden und typische Konfigurationsfehler erkennen.

## 1. Welche Software gibt es?

| Art | Zweck | Beispiel |
|---|---|---|
| **Firmware** | Geräteinterne Grundfunktionen, hardwarenah | UEFI des PCs |
| **Betriebssystem** | Verwaltet Prozesse, Speicher, Dateien, Rechte und Geräte | Windows, Linux |
| **Treiber** | Ermöglicht die Kommunikation zwischen OS und bestimmter Hardware | Druckertreiber |
| **Standardsoftware** | Verbreitete allgemeine Aufgaben | Tabellenkalkulation, Textverarbeitung |
| **Anwendungsspezifische Software** | Spezieller betrieblicher Zweck | Messdatenerfassung, Anlagenvisualisierung |

**Beispiel:** PC erkennt den Drucker, aber es lässt sich nicht drucken. Mögliche Ursache: falscher Treiber, keine Netzwerkverbindung, Druckerwarteschlange, fehlende Zugriffsberechtigung. Nicht sofort „Hardware kaputt“ behaupten.

## 2. Was passiert beim Einschalten eines PCs?

1. Netzteil stellt passende Versorgungsspannungen bereit.
2. CPU startet den vorgesehenen Firmwarecode.
3. UEFI initialisiert/prüft nötige Hardware und wählt einen Startweg.
4. Bootloader/Betriebssystem werden geladen.
5. Betriebssystem stellt Dienste und Benutzeroberfläche bereit; Anwendungsprogramme können gestartet werden.

**Unterschied:** UEFI startet und initialisiert, das Betriebssystem verwaltet den laufenden Rechner; Treiber verbinden Betriebssystem und Hardware.

## 3. Installation/Konfiguration nach Auftrag

Beispiel: Werkstatt braucht PC für Messdaten und Ausdrucke.

- Anforderungen vorab: benötigte Programme, Schnittstellen, Kompatibilität, Nutzer, Netzwerk, Datensicherheit, Budget.
- Hardware auswählen und kompatibel prüfen: CPU-Architektur, ausreichend RAM, Speicherkapazität, Ports, Geräte-/Treiberunterstützung.
- Betriebssystem und benötigte Software legal, passend und sicher bereitstellen.
- Netzwerkeinstellungen / Drucker / Berechtigungen konfigurieren.
- Updates, Datensicherung und Zugriffsschutz einrichten.
- Funktionsprüfung nach definierten Kriterien, Dokumentation und Übergabe.

**Prüfungsfalle:** „USB-Stecker passt“ garantiert **keine** passende Software oder Treiber; „System startet“ garantiert **nicht**, dass der Auftrag erfüllt ist.

## 4. Laufwerke und Dateien

- **Datei:** zusammengehörende Daten mit Name/Format.
- **Ordner:** Strukturierung von Dateien.
- **Dateisystem:** Organisiert Speicherung; z. B. NTFS, exFAT. Auswahl hängt von Anforderungen und Kompatibilität ab.
- **Partition:** logische Unterteilung eines Datenträgers.
- **Backup:** zusätzliche, wiederherstellbare Datenkopie; nicht bloß zweite Verknüpfung zum selben Ordner.

## 5. Typische Aufgaben

1. Nenne je eine Aufgabe von UEFI, Betriebssystem und Treiber.
2. Warum kann ein Gerät erkannt sein und trotzdem nicht richtig funktionieren?
3. Was muss vor dem Kauf einer Softwarelizenz geprüft werden?
4. Welche Probleme können bei einem Betriebssystemwechsel entstehen?
5. Wann sind Updates und Zugriffsrechte wichtig?
6. Warum gehört eine Funktionsprobe nach der Softwareinstallation dazu?

**Danach:** [Lektion 6 – IT-Sicherheit und Datenschutz](06_IT_Sicherheit_Datenschutz.md).