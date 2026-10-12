# Tag 2 – Leitungen, Netzsysteme und Schutz

**Ziel:** Komponenten für eine Installationsaufgabe fachlich begründet auswählen und Schutzkonzepte verstehen. **Zeit:** ca. 5–7 Stunden mit Pausen.  
**Voraussetzung:** Tag 1 (L, N, PE und Schaltungswahl) mindestens verstanden.  
**Sicherheit:** Keine Eigenversuche an Netzspannung; dies ist ein theoretischer Lerntext.

## Block A – Leitungen und Betriebsmittel

### 1. Leitung, Kabel, Ader

- **Ader** = einzeln isolierter Leiter (vereinfacht).
- **Leitung** = ein oder mehrere isolierte Leiter mit Aufbau/Schutz, für festgelegte Installationsbedingungen.
- **Kabel** = im Allgemeinen robuster für vorgesehene anspruchsvollere Verlegebedingungen, z. B. Erdreich; genaue Verwendung richtet sich nach Norm und Typ.
- **NYM-J 3×1,5 mm²**: gebräuchliche Mantelleitung mit Schutzleiter („-J“), drei Adern mit jeweils 1,5 mm² Nennquerschnitt. Bezeichnung **allein** sagt noch nicht, dass diese Leitung für jede konkrete Absicherung/Verlegeart zulässig ist.
- **H07V-U**: isolierte Einzelader zur zulässigen Verlegung etwa in geeigneten Installationsrohren/-kanälen; Typbezeichnung lesen lernen.
- **NYM-O**: ohne grün-gelben Schutzleiter; nicht beliebig anstelle von „-J“ einsetzen.

### 2. Aderfarben und Kennzeichnung

- **PE** grün-gelb und **N** blau; Außenleiter üblicherweise braun/schwarz/grau.
- Farben sind **keine** zuverlässige Bestätigung der elektrischen Funktion: Kennzeichnung und Mess-/Prüfunterlagen sind maßgeblich; Altanlagen können abweichen.
- PEN vereint Neutral- und Schutzleiterfunktionen, jedoch **nur unter dafür zugelassenen Bedingungen**. PEN ist nicht mit N oder PE beliebig austauschbar.

### 3. Verlegearten und Umgebungsbedingungen

Vergleiche: im Rohr in wärmegedämmter Wand, auf Putz, auf Kabelrinne, im Kanal, im Erdreich. Je nach Wärmeabfuhr hat dieselbe Leitung eine unterschiedliche zulässige Strombelastbarkeit. Weitere Einflussgrößen: Umgebungstemperatur, Häufung mehrerer Leitungen, Anzahl belasteter Adern, Aderisolierung, Länge, mechanische Beanspruchung und Brandschutz.

**Faustfehler, den wir vermeiden:** „1,5 mm² bekommt immer einen B16-Automaten.“ Das ist **nicht allgemein richtig** – zuerst die konkreten Bedingungen und Tabellen prüfen.

### 4. Betriebsmitteldaten lesen

Achte auf **Nennspannung U_n**, **Nennstrom I_n**, **Nennleistung P_n**, Schutzart (IP), Schutzklasse (I/II/III), Temperaturbereich, Montage- und Herstellerangaben.

- **Schutzklasse I:** Schutzleiteranschluss und Schutzerdung als Teil des Schutzkonzepts.
- **Schutzklasse II:** doppelte/verstärkte Isolierung; kein Schutzleiteranschluss an einem entsprechenden Gerät nötig.
- **IP44** vereinfacht: Schutz gegen feste Fremdkörper ab 1 mm und gegen Spritzwasser; eine konkrete Eignung ergibt sich dennoch aus der Einbausituation und dem Gerätedatenblatt.
- **IP** ist **nicht** dasselbe wie Schutzklasse.

## Block B – Netzsysteme

Die Bezeichnungen beschreiben das Verhältnis von Stromquelle, Körpern und Erde.

| System | Grundidee | Merkmale |
|---|---|---|
| TN-S | N und PE von der Quelle bis zum Verbraucher getrennt | getrennte Schutz- und Neutralleiterfunktion |
| TN-C | PEN als kombinierter Leiter im betreffenden Abschnitt | besondere Regeln, RCD im TN-C-Abschnitt nicht anwendbar |
| TN-C-S | erst PEN, danach Aufteilung in PE und N | nach Trennung PE und N nicht wieder beliebig zusammenführen |
| TT | Körper mit eigenem örtlichem Erder geerdet | Schutz durch geeignete automatische Abschaltung, häufig RCD besonders bedeutsam |

**Nicht verwechseln:** Die erste Kennbuchstabe bezieht sich auf die Erdung der Stromquelle, der zweite auf die Körper der Anlage. Detaillierte Anforderungen ergeben sich aus gültigen technischen Regeln.

## Block C – Überstromschutz und Fehlerstromschutz

### 5. Leitungsschutzschalter (LS)

Schützt bei richtiger Auswahl insbesondere Leiter und Leitungsanlagen vor **Überlast und Kurzschluss**, indem er Überströme abschaltet. Ein **B16** bedeutet: Charakteristik B, Bemessungsstrom 16 A. Daraus folgt **nicht**, dass jede 1,5-mm²-Leitung geeignet ist oder dass Berührungsschutz automatisch gewährleistet ist.

### 6. RCD / FI-Schutzschalter

Ein Fehlerstrom-Schutzschalter vergleicht die Ströme, die über die aktiven Leiter hinein- und hinausfließen. Bei entsprechendem Differenzstrom löst er aus. **IΔn = 30 mA** bedeutet Bemessungsdifferenzstrom, **nicht** eine zulässige Dauerberührung. Ein gewöhnlicher RCD ist **kein Ersatz für einen LS** und schützt nicht selbst vor jeder Überlast.

### 7. Schutzkonzept

- Basisschutz = Schutz gegen direktes Berühren unter normalen Betriebsbedingungen.
- Fehlerschutz = Schutz bei einem Isolations-/Körperschlussfehler.
- Zusatzschutz = ergänzende Maßnahme, z. B. geeignete RCDs in den einschlägig vorgeschriebenen Fällen.
- Schutzmaßnahmen hängen von Netzsystem, Schleifenimpedanz, Erdung, Schutzorganen und den Installationsbedingungen ab.
- Ein Schutzleiter darf **nicht** durch gewöhnliche Bedien-Schaltkontakte unterbrochen werden.

**Kurzschluss vs. Überlast vs. Fehlerstrom:**
- Überlast: unzulässig hoher Betriebsstrom, ohne dass zwingend ein Kurzschluss besteht.
- Kurzschluss: unerwünscht niederohmige Verbindung zwischen unterschiedlichen Potenzialen.
- Fehlerstrom: Strom über einen nicht vorgesehenen Pfad, beispielsweise über einen Fehler zur Erde.

## Block D – Lern- und Prüfungsaufgaben (je 2 Punkte; 15 Fragen = 30 Punkte)

1. Wofür steht „3×1,5 mm²“ bei NYM-J?
2. Was sagt der Buchstabe **J** bei NYM-J?
3. Warum darf man den Querschnitt nicht allein nach dem LS-Nennstrom festlegen?
4. Nenne drei Einflussfaktoren der Strombelastbarkeit.
5. Worin unterscheiden sich N und PE im Normalbetrieb?
6. Was bedeutet TN-S im Hinblick auf N/PE?
7. Was ist ein PEN?
8. Warum darf man PE und N nach der Aufteilung eines PEN nicht einfach wieder verbinden?
9. Nenne die Hauptfunktion des LS-Schalters.
10. Nenne die Hauptfunktion eines RCD.
11. Warum ersetzt ein RCD gewöhnlich keinen LS-Schalter?
12. Wofür steht bei B16 das **B** und wofür die **16**?
13. Erkläre den Unterschied zwischen Schutzart IP und Schutzklasse.
14. Eine Leitung liegt in Wärmedämmung und mehrere Leitungen verlaufen dicht daneben: Warum ist das bei der Auslegung wichtig?
15. Ein Gerät trägt das Doppelquadrat-Symbol. Welcher Schutzklasse gehört es an, und welche grundsätzliche Schutzidee steckt dahinter?

**Ziel:** mindestens 24/30 Punkten und alle sicherheitsbezogenen Fragen verstanden. Falls nicht, weitere Übungsfälle erarbeiten.

## Block E – Transfer: Mini-Kundenauftrag

„In einem Werkstattbereich werden zusätzliche Steckdosen und eine Leuchte geplant. Leitungen verlaufen abschnittsweise in geschlossenen Kanälen, mehrere Stromkreise sind gemeinsam geführt.“

Schreibe vor jeder Querschnitts-/Schutzorganauswahl **acht Informationen** auf, die dir für eine seriöse Planung fehlen. Tipp: Verbraucher, Leitungslänge, Häufung, Temperatur, Netzsystem, Verlegeart, mögliche mechanische Einflüsse, Abschaltbedingungen.

## Merkkarten

**LS → Überstrom. RCD → Fehlerstrom. PE → Schutz. N → Betriebsrückleiter.**  
**Querschnitt nach realen Bedingungen – nicht nach einem universellen „1,5 = B16“-Merkspruch.**

**Fortsetzung:** [Tag 3 – Bemessung und Kosten](Tag_3_Bemessung_und_Kosten.md).
