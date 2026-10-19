# LF4 – Lektion 6: IT-Sicherheit, Datensicherung, Datenschutz und Recht

**Ziel:** Begriffspaare sauber unterscheiden und für einen echten Auftrag passende Maßnahmen nennen.

## 1. Drei Schutzziele

- **Vertraulichkeit:** Unbefugte dürfen Daten nicht einsehen → Rechte/Rollen, Verschlüsselung.
- **Integrität:** Daten sollen vollständig und unverändert bleiben → Prüfsummen, Berechtigungen, nachvollziehbare Änderungen.
- **Verfügbarkeit:** Systeme/Daten sollen gebraucht nutzbar sein → Backups, Wartung, Ersatzkonzept.

**Beispiel:** Messprotokoll der Produktion:
- Nur Berechtigte dürfen es sehen (vertraulich).
- Werte dürfen nicht heimlich verändert werden (integer).
- Bei PC-Ausfall muss es wiederherstellbar sein (verfügbar).

## 2. Datenschutz vs. Datensicherheit

- **Datenschutz:** Schutz *personenbezogener Daten* und rechtmäßiger Umgang damit (z. B. nach DSGVO).
- **Datensicherheit:** Schutz *aller relevanten Daten und Systeme* vor Verlust, unberechtigtem Zugriff und Manipulation.

**Prüfungsfalle:** Backup gehört primär zur Datensicherung; es ersetzt keine Datenschutzmaßnahmen.

## 3. Datensicherung

Praxisempfehlung **3-2-1-Regel**: mindestens drei Datenkopien, auf zwei unterschiedlichen Medientypen, davon eine Kopie getrennt vom Hauptstandort. **Das ist ein bewährtes Prinzip, keine universelle gesetzliche oder normativ zwingende Mindestzahl.**

Wichtiger als ein bloß vorhandenes Backup ist: **Wiederherstellung testen**. Versionierung und regelmäßige Sicherungsintervalle nach Schutzbedarf auswählen.

**RAID ≠ Backup:** RAID kann Verfügbarkeit verbessern, ersetzt aber keine unabhängige Sicherung gegen Fehlbedienung, Malware, Brand oder Löschung.

## 4. Schutzmaßnahmen im Alltag

| Risiko | Geeignete Maßnahmen |
|---|---|
| Unbefugter Zugang | Individuelle Benutzerkonten, starke Passwörter/Passkeys, MFA wo sinnvoll |
| Schadsoftware | Updates, vertrauenswürdige Software, Schutzmechanismen, keine unbekannten Anhänge |
| Datendiebstahl | Rollen/Rechte, Verschlüsselung, sichere Entsorgung |
| Datenverlust | Backupkonzept + Wiederherstellungstest |
| Geräteausfall | Wartung, Dokumentation, Ersatz-/Notfallplan |
| Offenes WLAN | Moderne WLAN-Verschlüsselung, sichere Netzkonfiguration |

**Grundsatz:** Nur benötigte Rechte vergeben („Least Privilege“). Keine Kennwörter im Prüfprotokoll offen ablegen.

## 5. Urheber- und Medienrecht / Lizenzen

- Software und Bilder dürfen nicht einfach ohne passende Nutzungsrechte kopiert werden.
- Unterschied Freeware, Open Source und kommerzielle Lizenz verstehen: **Open Source ist nicht automatisch lizenzpflichtfrei oder bedingungslos**.
- Kundenbezogene Daten nur zweckgebunden und rechtmäßig nutzen; Aufbewahrung/Löschung nach Anforderung berücksichtigen.
- Bei Auftragsdokumentation keine sensiblen Zugangsdaten veröffentlichen.

## 6. Übungen

1. Erkläre Datenschutz und Datensicherheit mit je einem Beispiel.
2. Warum ist eine Kopie auf derselben Festplatte kein gutes Backup?
3. Warum ersetzt RAID keine Datensicherung?
4. Nenne zwei Maßnahmen für Vertraulichkeit.
5. Was ist der Vorteil verschiedener Benutzerkonten mit beschränkten Rechten?
6. Darfst du ein fremdes Foto für eine Firmenbroschüre verwenden, nur weil du es online gefunden hast?

**Danach:** [Lektion 7 – Auftrag und Auswahl](07_Auftrag_Planung_Beschaffung.md).