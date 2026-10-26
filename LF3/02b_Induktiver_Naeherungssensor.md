# LF3 – Lektion 2B: Induktiver Näherungssensor ausführlich

**Status:** Im Unterricht, Prüfung noch offen.  
**Lernziel:** Ein induktives Sensorsignal physikalisch erklären, Bauteile identifizieren, 3-Draht-PNP/NO von einem mechanischen Öffner unterscheiden, Schaltabstand und Fehler beurteilen.

## 1. Was wird erkannt?
Ein induktiver Näherungssensor erkennt **metallische Objekte ohne Berührung**. Diese können sich bewegen oder stillstehen. Gewöhnliche induktive Näherungssensoren sind für nichtmetallische Kunststoffe, Holz oder Glas nicht geeignet; auch unterschiedliche Metalle werden je nach Sensor mit verschiedenen Schaltabständen erkannt.

**Industriebeispiel:** Stahlblech fährt auf einem Förderband am Sensorkopf vorbei. Die SPS bekommt ein Signal, mit dem sie etwa ein Werkstück zählt oder eine Arbeitsfolge freigibt.

## 2. Aufbau (Grundprinzip klassischer Oszillatorsensoren)
1. **Aktive Fläche:** Vorderseite des Sensorkopfs, durch die das elektromagnetische Wechselfeld austritt.
2. **Spule und oft Ferritkern:** Spule erzeugt das magnetische Wechselfeld; der Ferritkern kann das Feld formen.
3. **Oszillator/LC-Schwingkreis:** Erzeugt eine hochfrequente Wechselanregung; LC steht für Spule (L) und Kondensator (C).
4. **Auswerteeinheit / Schwellwertschaltung:** Erkennt Änderungen der Schwingungsamplitude, etwa über einen Schmitt-Trigger.
5. **Elektronische Ausgangsstufe:** Setzt den Zustand in ein nutzbares Signal, z. B. PNP/NPN-Ausgang.
6. **Gehäuse, LED und Leitung oder M12-Steckverbinder:** Schutz, Zustandserkennung, Anschluss.

Es gibt auch abweichende Sensorkonzepte; dieser Unterricht behandelt den üblichen klassischen induktiven Näherungsschalter mit Oszillator.

## 3. Wirkprinzip (sechs Schritte)
1. Der Sensor erhält elektrische Versorgung, z. B. 24 V DC bei dafür vorgesehenen Sensoren.
2. Der Oszillator erzeugt Wechselstrom in einer Spule.
3. Vor der aktiven Fläche entsteht ein hochfrequentes elektromagnetisches Wechselfeld.
4. Kommt ein **leitfähiges Metallobjekt** in dieses Feld, werden Wirbelströme im Objekt induziert. Bei ferromagnetischen Werkstoffen können zusätzliche Ummagnetisierungsverluste entstehen.
5. Die Wirbelstrom-/Materialverluste entziehen dem Sensor-Schwingkreis Energie, die Schwingung wird **bedämpft** und ihre Amplitude sinkt bzw. das auswertbare Oszillatorsignal ändert sich.
6. Die Auswerteelektronik erkennt eine hinreichende Änderung und schaltet eine elektronische Ausgangsstufe. Dieses Schaltsignal kann die SPS lesen.

**Prüfungsformel in Worten:** Metall in Wechselfeld → Wirbelströme → Energieverlust/Bedämpfung → Auswertung → Schaltsignal.

Ein induktiver Sensor ist **kein mechanischer Schließer**: Er hat keinen von einer Werkstückkante gedrückten Rollenhebel und bei PNP/NPN-Ausgängen typischerweise eine Halbleiterstufe, keinen mechanisch bewegten Ausgangskontakt.

## 4. Vergleich zum mechanischen Endschalter
| Thema | Mechanischer Endschalter | Induktiver Sensor |
|---|---|---|
| Erfassung | durch Druck auf Hebel/Stößel | elektromagnetisches Feld, berührungslos |
| Geeignete Ziele | Mechanisch passende Betätiger | Metall |
| Verschleiß | bewegte Mechanik/Kontakte | keine mechanische Betätigung des Sensorkopfs |
| Signal | häufig mechanische NO/NC-Kontakte | häufig elektronischer PNP/NPN-Ausgang |
| Versorgung | reine Kontakte benötigen nicht selbst Elektronikversorgung | elektronische Sensoren benötigen eigene Versorgung (bei typischen 3-Draht-Typen) |

## 5. Dreiadriger DC-Sensor: PNP und NPN
Viele industrielle Gleichspannungssensoren: **Braun (BN) = L+**, **Blau (BU) = M/0 V**, **Schwarz (BK) = Q/Ausgang**. Nur als häufiges Beispiel, der konkrete Hersteller-Schaltplan ist entscheidend.

- **PNP**: Aktiviertes Schaltsignal liefert typischerweise positives Potenzial am Q-Ausgang.
- **NPN**: Aktivierter Ausgang schaltet typischerweise gegen 0 V.
- **NO (Schließerfunktion)**: Im nicht erfassten Zustand nicht schaltend, bei erkanntem Ziel aktiv; je nach Ausgangsart elektronische „Schließer“-Funktion.
- **NC (Öffnerfunktion)**: Umgekehrtes logisches Schaltverhalten. **NO/NC und PNP/NPN sind unabhängige Merkmale.**

Beispiel eines **PNP-NO-Sensors**: Kein Metall → Q nicht aktiv; Metall erkannt → Q schaltet zur positiven Versorgung, passender SPS-Digitaleingang kann HIGH erkennen. Die Eingangsbeschaltung muss dazu passen.

## 6. Schaltabstand und Montage
- **Nennschaltabstand Sn**: Vom Hersteller unter definierten Normbedingungen mit geeignetem Referenzziel bestimmter Wert, keine pauschale Garantie für jedes Metall/jede Einbaulage.
- **Gesicherter Schaltabstand Sa**: Kleinerer Bereich, in dem unter den Datenblattbedingungen zuverlässig erkannt wird.
- **Hysterese**: Annäherungs- und Rückschaltabstand sind etwas verschieden, damit der Ausgang am Schaltpunkt nicht flattert.
- **Bündig montierbar**: Bei entsprechend ausgewiesenen Sensoren bis zur Stirnfläche in metallischer Umgebung einbaubar.
- **Nicht bündig montierbar**: Sensor benötigt vor der aktiven Fläche eine passende metallfreie Zone/Freiraum nach Herstellerangabe.
- **Materialfaktor**: Kupfer oder Aluminium kann bei herkömmlichen Sensoren kürzere Schaltabstände als Stahl bewirken; es gibt Spezial-„Faktor-1“-Sensoren.

**Rechenbeispiel nur für ausgewiesene Datenblätter mit Sa = 0,81·Sn:** Sn = 8 mm → Sa = 0,81·8 mm = 6,48 mm. Das ist ein typbezogenes Modell, kein universelles Gesetz für alle Hersteller und Sensorprinzipien.

## 7. Anwendungsfälle
1. Stahlteile auf einem Förderband zählen.
2. Position eines metallischen Schlittens erfassen.
3. Zahnradzähne erkennen oder Bewegungssignale liefern.
4. Metallische Werkstückträger/Anschläge detektieren.

Induktiv ist meist **ungeeignet für reine Kunststoffflaschen**. Hier ist je nach Lage ein optischer oder kapazitiver Sensor zu erwägen.

## 8. Fehlerbilder
- Sensor schaltet nicht: kein Metallziel, Ziel zu weit entfernt, Materialfaktor, falsche Einbauart, fehlende 24-V-Versorgung, Kabelbruch, falscher Ausgangstyp oder defekter Sensor.
- Sensor schaltet zu früh/unzuverlässig: benachbarte Metallteile, falscher Mindestabstand zwischen Sensoren, Vibration, schlechte Montage, elektromagnetische Störungen oder falsche Parametrierung.
- LED leuchtet, SPS erkennt nichts: Ausgänge/Q-Verdrahtung, PNP/NPN-Eingangskompatibilität, gemeinsames Bezugspotenzial, SPS-Eingang/Programm prüfen.

Nur nach geeignetem Arbeits-/Sicherheitsverfahren prüfen. Keine Anschlussarbeit unter Spannung; bei Maschine die Bewegung gegen unerwarteten Anlauf sichern.

## 9. Hefteintrag – Zum Abschreiben
**Induktiver Näherungssensor:** Erfasst Metall berührungslos durch ein hochfrequentes elektromagnetisches Wechselfeld.

**Aufbau:** Aktive Fläche – Spule/Ferritkern – Oszillator – Auswerteelektronik – Schaltausgang – Gehäuse/Anschluss.

**Funktionsfolge:**
1. Oszillator regt die Spule an.
2. Vor dem Sensor entsteht ein elektromagnetisches Wechselfeld.
3. Metall nähert sich; im Metall bilden sich Wirbelströme.
4. Wirbelströme entziehen dem Schwingkreis Energie: Bedämpfung.
5. Auswertung erkennt die Signaländerung und schaltet den Ausgang.

**Vorteile:** Berührungslos; keine mechanische Betätigung, daher kein verschleißender Rollenhebel; für industrielle Metallpositionen und Zählung geeignet.  
**Grenzen:** Nur geeignete Metalle, begrenzter Schaltabstand, Einbaulage und Material beeinflussen die Funktion.

**Typischer DC-Dreileiter:** Braun = L+, Blau = 0 V/M, Schwarz = Ausgang Q (Datenblatt prüfen).  
**PNP** schaltet positiv; **NPN** schaltet nach 0 V.  
**NO** schaltet bei Erkennung aktiv, **NC** in der umgekehrten Logik.  
**Sn** = Nennschaltabstand; **Sa** = gesicherter Schaltabstand; **Hysterese** = Unterschied zwischen Ein- und Ausschaltpunkt.

**Merksatz:** Metall → Wirbelströme → Bedämpfung → Elektronik erkennt → Schaltsignal zur SPS.

## 10. AP1-Übungsfragen ohne Lösung
1. Welcher Sensor erkennt Stahl berührungslos?
2. Was ist die Funktion der Spule?
3. Was erzeugt der Oszillator?
4. Wie entstehen Wirbelströme und was bewirken sie?
5. Warum erkennt ein gewöhnlicher induktiver Sensor keine Kunststoffflasche?
6. PNP-NO-Sensor: Was passiert beim Heranbringen eines Metallteils am Ausgang?
7. Was bedeutet „bündig montierbar“?
8. Welche Art von Schaltabstand ist für zuverlässige Auslegung maßgeblich?
9. Sn = 8 mm, gegeben Sa = 0,81 Sn: Sa berechnen.
10. Sensor-LED leuchtet beim Metall, aber SPS-Eingang bleibt aus: zwei plausible Ursachen nennen.
11. Worin unterscheidet sich der induktive Sensor von einem mechanischen Endschalter?
12. Warum bedeutet PNP nicht automatisch Schließer (NO)?

## Herstellerquellen
- Pepperl+Fuchs, „Erkennungsmethode und Funktion“: https://www.pepperl-fuchs.com/de-ch/support/knowledge-and-literature/knowledge-bases-for-industrial-sensors/knowledge-base-for-inductive-sensors/detection-method-and-function-gp28703
- Baumer, „Funktionsweise und Technologie von induktiven Sensoren“: https://www.baumer.com/ch/de/service-support/funktionsweise/funktionsweise-und-technologie-von-induktiven-sensoren/a/Know-how_Function_Inductive-sensors
- ifm, „Ganzmetallsensoren – Wirbelstromprinzip“: https://www.ifm.com/de/de/shared/technologien/ganzmetallsensoren/technologie
- SICK, „Induktive Sensoren – Funktion, Montage und Anwendung“: https://www.sick.com/at/de/induktive-sensoren-funktion-montage-und-anwendung/w/blog-induktiver%20sensor
- SICK, „Sensing range explanation for inductive sensors“: https://support.sick.com/sick-knowledgebase/article/?id=4d64512e-4499-f011-b4cc-7c1e527246ab
