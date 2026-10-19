# LF4 – Lektion 1: PC-Hardware verstehen

**Ziel:** Ein Computersystem erklären, Teile erkennen, deren Aufgaben und Zusammenarbeit begründen.  
**Ausgangspunkt:** Stell dir vor, ein Kunde öffnet ein Textdokument und speichert es. Was passiert innen im PC?

## 1. Die Grundidee: EVA-Prinzip

**Eingabe → Verarbeitung → Ausgabe (EVA)**

- **Eingabe:** Tastatur (Text), Maus (Bewegung), Mikrofon (Ton), Sensor (Messwert).
- **Verarbeitung:** CPU führt Befehle aus, während RAM die aktuell benötigten Daten bereithält.
- **Ausgabe:** Monitor zeigt Text, Drucker druckt, Lautsprecher gibt Ton aus.
- **Speichern:** SSD/HDD erhält die Datei dauerhaft – ein zusätzlicher Schritt, der in vielen EVA-Beispielen als Speicherung ergänzt wird.

### Beispiel „Text schreiben und speichern“

1. Du drückst A auf der Tastatur → ein Eingabesignal entsteht.
2. Betriebssystem und Textprogramm verarbeiten den Tastendruck mit Hilfe der CPU; Daten/Programm befinden sich während der Arbeit im RAM.
3. Die Grafikausgabe erzeugt das sichtbare „A“ am Monitor.
4. Du speicherst → das Programm schreibt die Datei über das Betriebssystem auf SSD oder HDD.
5. Du schaltest aus → **RAM-Inhalte gehen ohne Strom normalerweise verloren**, die gespeicherte Datei bleibt auf dem Massenspeicher.

**Prüfungsfalle:** Der Prozessor ist nicht „der Speicher“; CPU, RAM und SSD/HDD haben verschiedene Aufgaben.

## 2. PC-Komponenten – Grundaufgaben

| Bauteil | Aufgabe | Bildlich merken | Typische Frage |
|---|---|---|---|
| **CPU (Prozessor)** | Führt Maschinenbefehle aus und verarbeitet Daten | Arbeiter | Rechnet/steuert |
| **RAM (Arbeitsspeicher)** | Schneller, flüchtiger Speicher für laufende Programme/Daten | Arbeitsfläche | Was passiert nach Stromausfall? |
| **SSD** | Nichtflüchtiger Massenspeicher mit Flashspeicher | Aktenschrank | Programme/Dateien langfristig |
| **HDD** | Nichtflüchtiger magnetischer Massenspeicher mit rotierenden Scheiben | Mechanisches Archiv | SSD vs. HDD |
| **Mainboard** | Verbindet CPU, RAM, Speicher, Erweiterungen und Anschlüsse; enthält Verbindungswege und Steuerbausteine | Verbindungsnetz | Wo werden Teile verbunden? |
| **Netzteil (PSU)** | Wandelt Netzwechselspannung in geeignete Gleichspannungen für die PC-Komponenten | Stromversorgung | Versorgt Komponenten elektrisch |
| **Grafikeinheit (GPU)** | Berechnet/generiert Grafik- und Bildausgaben; separat oder integriert | Bildverarbeitung | Bildausgabe |
| **Netzwerkadapter (NIC)** | Verbindet PC mit dem Netzwerk, z. B. Ethernet/WLAN | Netzwerkanschluss | MAC-/Netzwerkschnittstelle |
| **Kühlung** | Transportiert Abwärme ab | Wärmemanagement | Warum Lüfter/Kühlkörper? |

**Vorsicht bei Vereinfachungen:** Ein Display kann an integrierter Grafik betrieben werden; eine dedizierte Grafikkarte ist dafür nicht immer nötig. ROM und Flash sind nicht einfach das gleiche wie RAM.

## 3. Wie wirken CPU, RAM und SSD zusammen?

- **SSD/HDD:** Behält die gespeicherten Daten auch ohne Strom.
- **RAM:** Stellt aktuell gebrauchte Programmdaten schnell bereit.
- **CPU:** Führt Befehle aus und verarbeitet die Daten.

**Beispiel:** Ein Programm liegt auf der SSD. Beim Start lädt das Betriebssystem benötigte Teile in den RAM. Die CPU führt Befehle aus; Arbeitsdaten werden laufend im RAM genutzt. Beim Speichern gehen die vorgesehenen Daten zurück auf den Massenspeicher.

**Warum nicht alles direkt auf der SSD?** RAM hat in der Regel eine wesentlich niedrigere Zugriffsverzögerung für den aktiven Arbeitsspeicherzugriff. Die CPU besitzt zudem eigene schnelle **Caches**; das ersetzt RAM nicht.

**Merksatz:** SSD **behält**, RAM **hält bereit**, CPU **verarbeitet**.

## 4. Firmware, BIOS/UEFI und Betriebssystem

- **Firmware:** Software, die in Geräten eingebettet ist und grundlegende Steuerungsfunktionen bereitstellt.
- **BIOS / UEFI:** Start-Firmware des Computers. Initialisiert Hardware und führt den Startprozess zum Betriebssystem; UEFI ist der moderne Standard vieler PCs.
- **Betriebssystem (z. B. Windows/Linux):** Verwaltet Hardware-Ressourcen, Dateien, Programme und Benutzer.
- **Anwendungssoftware (z. B. Textverarbeitung):** Erledigt konkrete Benutzeraufgaben.
- **Treiber:** Software, die eine Hardwarekomponente über das Betriebssystem ansprechbar macht.

**Prüfungsfalle:** UEFI ist nicht Windows. Betriebssystem ist nicht Anwendungssoftware.

## 5. Bauformen und Anschlüsse – erst verstehen, dann optisch lernen

- **DIMM:** Typische Arbeitsspeichermodule in vielen Desktop-PCs.
- **M.2:** Kompakte Steckkarten-/Modulbauform; viele SSDs nutzen M.2. **M.2 bedeutet nicht automatisch NVMe.** Manche M.2-SSDs arbeiten über SATA, andere über PCIe/NVMe.
- **SATA:** Schnittstelle für Speicherlaufwerke, etwa bestimmte SSDs/HDDs.
- **PCIe:** Schnelle interne Verbindung u. a. für Erweiterungskarten und NVMe-SSDs.

Siehe [Lektion 2 – Stecker und Schnittstellen](02_Stecker_Schnittstellen.md).

## 6. Woran erkenne ich eine technisch passende Auswahl?

Nicht nach „große Zahl ist immer besser“ wählen. Der **Kundenauftrag** zählt:

- Büroarbeit: ausreichend CPU/RAM/SSD, passende Anschlüsse, Zuverlässigkeit, Wartbarkeit.
- Messdatenerfassung: kompatible Schnittstellen, Treiber, Software, Netzwerkanbindung, sichere Datenhaltung.
- Erweiterung: freie Schnittstellen/Steckplätze, passende Bauform/Leistung/Kompatibilität prüfen.
- Energieverbrauch, Anschaffungskosten und Ergonomie mit berücksichtigen.

## 7. Mini-Übung – zuerst ohne Hilfe lösen

1. Was bedeutet EVA? Nenne je ein Beispiel.
2. Erkläre den Weg von einer gespeicherten Datei auf der SSD bis zu einem geöffneten Dokument am Monitor.
3. Warum verschwindet ein ungespeicherter Text bei plötzlichem Stromausfall möglicherweise?
4. Sind „SSD“, „RAM“ und „CPU“ drei unterschiedliche Speicherarten? Begründe.
5. Was macht das Netzteil; was macht das Mainboard?
6. Worin unterscheidet sich UEFI vom Betriebssystem?
7. Braucht ein PC grundsätzlich eine separate Grafikkarte, um ein Bild anzuzeigen?
8. Was ist der Unterschied zwischen einem Hardware-Anschluss (z. B. M.2) und einem Datenübertragungsprotokoll (z. B. NVMe)?

**Erfolgskriterium:** 7 von 8 selbstständig erklären können; sonst offene Fragen notieren.  
**Danach:** [Lektion 2 – Stecker & Schnittstellen](02_Stecker_Schnittstellen.md).