# LF3 – Lektion 2C: Kapazitiver Näherungssensor – ausführlich

**Status:** Unterricht und AP1-Prüfung vorbereitet; Prüfung noch offen. 
**Bisheriger Lernstand:** 2A Mechanischer Endschalter **6/8**; 2B Induktiver Sensor **11,5/12**.

## 1. Aufgabe und industrielle Verwendung

Ein kapazitiver Näherungssensor erfasst eine **Änderung der elektrischen Kapazität** in seinem Messfeld. Er kann je nach Bauform und Einstellungen **Metalle, Flüssigkeiten und nichtleitende Stoffe** wie Kunststoff, Glas, Holz oder Pulver berührungslos erfassen. **Nicht alles gleich gut:** Material, Feuchtigkeit, Größe, Abstand und Umgebungsbedingungen bestimmen die tatsächliche Erkennung.

**Beispiel:** Der Wasserstand in einem geeigneten nichtmetallischen Kunststoffbehälter wird von außen an einer bestimmten Füllhöhe erkannt. Der Sensor braucht keinen direkten Flüssigkeitskontakt, sofern die Wanddicke und die Materialeigenschaften zum Gerät passen.

## 2. Was ist elektrische Kapazität?

Ein Kondensator speichert elektrische Ladung und Energie in einem elektrischen Feld. Zwei leitende Elektroden, getrennt durch einen Isolierstoff (Dielektrikum), bilden ein einfaches Modell.

**Kapazität C** beschreibt, wie viel Ladung bei einer bestimmten Spannung gespeichert wird: **C = Q / U**.
**Einheit:** Farad (F); im Sensor typischerweise winzige Kapazitätsänderungen.

Für den idealisierten Plattenkondensator:
**C = ε0 · εr · A / d**
- ε0: elektrische Feldkonstante
- εr: relative Permittivität des Materials (Dielektrizitätszahl)
- A: überlappende Elektrodenfläche
- d: Elektrodenabstand

Dies ist ein **Modell**, nicht die exakte Formel für das offene, gekrümmte Feld eines tatsächlichen Näherungssensors.
Mit größerem εr steigt bei ansonsten gleicher Geometrie die Kapazität.

## 3. Innerer Aufbau

1. Aktive Sensorfläche und **Messelektrode**.
2. Je nach Sensor: Gegenelektrode/GND-Elektrode oder Umgebung als Gegenpotenzial.
3. Optional Abschirm- oder Kompensationselektrode (formt das Feld, verringert Störeinflüsse).
4. **Oszillator** (häufig RC-Prinzip) beziehungsweise elektronische Kapazitätsmessung.
5. Auswertung mit definierter Schaltschwelle und Hysterese.
6. Elektronische Ausgangsstufe (z. B. PNP/NPN; NO/NC).
7. Schutzgehäuse, Anschlüsse, LED und teilweise Empfindlichkeitseinstellung.

## 4. Physikalische Funktion Schritt für Schritt

1. Elektronischer Sensor erhält eine passende Versorgung (viele DC-Typen z. B. 24 V DC, modellabhängig).
2. Die Sensor-Elektrode erzeugt ein **elektrisches Wechselfeld** vor der aktiven Fläche.
3. In Luft hat die Elektrodenanordnung eine bestimmte Ausgangskapazität.
4. Nähert sich ein anderes Material, verändert es das elektrische Feld und die **wirksame Kapazität**.
5. Ein Oszillator/Messkreis reagiert auf die Kapazitätsänderung, z. B. durch geänderte Schwingungsamplitude oder Anschwingen bei Schwellwert. Ausführung variiert nach Hersteller.
6. Die Auswerteelektronik vergleicht den Messwert mit einer Schaltschwelle.
7. Der Ausgang wechselt seine logische Schaltstellung und liefert ein SPS-Eingangssignal.

**Merksatz:** Objekt/Material → elektrisches Feld und Kapazität verändern sich → Oszillator/Auswertung → Schaltsignal.

Anders als bei einem klassischen **induktiven Sensor** stehen nicht **magnetisches Wechselfeld und Wirbelströme**, sondern **elektrisches Feld und Kapazität** im Zentrum.

## 5. Praxisbeispiel Füllstand durch Kunststoffwand

- Bei leerem Behälter beeinflussen überwiegend Luft und die Behälterwand das Sensorfeld.
- Wenn die Flüssigkeit die Sensorhöhe erreicht, ändert sich die Umgebung des Sensors deutlich.
- Daraus entsteht eine messbare Kapazitätsänderung; die Elektronik kann einen Schwellwert erkennen.
- SPS erhält das Signal und kann eine Meldung ausgeben oder über ein geeignetes Schaltgerät den Füllvorgang beenden.

**Grenzen:** Besonders wichtig sind nichtleitende Behälterwand, geeignete Wanddicke, Material/Permittivität der Flüssigkeit, sichere Montage, Vermeidung störender metallischer Umgebung und richtige Empfindlichkeitseinstellung.

## 6. Typische Einflüsse und Fehlerquellen

| Einfluss | Wirkung |
|---|---|
| Material/relative Permittivität εr | Höhere εr bedeutet oft leichter messbare Kapazitätsänderung bei gleicher Geometrie |
| Abstand/Objektgröße | Weiter entfernte/kleinere Objekte wirken schwächer |
| Feuchtigkeit/Tropfen/Schmutz | Können Kapazität verändern und Fehlansprechen verursachen |
| Behälterwand/Metallnähe | Kann Feld abschirmen/verändern und Schaltverhalten verschieben |
| Temperatureinfluss/Versorgung | Können Drift verursachen; Datenblatt beachten |
| Empfindlichkeitsregler (Potentiometer/Teach-in) | Schwellwert einstellbar bei dafür vorgesehenen Geräten |

Moderne Sensoren können Kompensationselektroden und digitale Filterung nutzen, die Störeinflüsse reduzieren.

## 7. Schaltabstand, Empfindlichkeit und Hysterese

**Sn:** Nennschaltabstand unter Referenzbedingungen; **nicht für jedes Material und jede Umgebung garantiert**.
**Sa/Arbeitsbereich:** Vom Hersteller spezifizierter, gesicherter nutzbarer Bereich; Vorgaben konkret lesen.
**Hysterese:** Unterschied zwischen dem Abstand beim Ein- und beim Ausschalten. Beispiel: bei 5 mm EIN und bei 5,6 mm AUS → **0,6 mm Hysterese**.

**Wichtig:** Der für manche induktiven Sensoren im Unterricht benutzte Faktor **Sa=0,81·Sn** ist **keine universelle Rechenregel** für kapazitive Sensoren. Materialien und Referenzbedingungen beeinflussen den Schaltabstand stark.

## 8. Typischer DC-Anschluss und Schaltfunktionen

Bei vielen DC-Dreileitersensoren gilt laut jeweiligem Herstellerplan:
- Braun (BN): L+; Blau (BU): M/0 V; Schwarz (BK): Q/Schaltausgang.
- **PNP:** Ausgang schaltet bei aktiver Funktion typischerweise positives Potenzial.
- **NPN:** Ausgang schaltet bei aktiver Funktion typischerweise nach 0 V.
- **NO:** Ausgang ist beim Erkennen eines Zielobjekts aktiv (Schließerfunktion).
- **NC:** Ausgang ist ohne Zielobjekterkennung aktiv (Öffnerfunktion).

Konkreten Sensor vor Inbetriebnahme nach Datenblatt auf Versorgung, Pinbelegung, Schaltlogik, Eingangsverträglichkeit, Stromgrenzen und Funktion prüfen.

## 9. Drei Sensorprinzipien im Vergleich

| Merkmal | Mechanischer Endschalter | Induktiver Sensor | Kapazitiver Sensor |
|---|---|---|---|
| Berührung nötig? | Ja | Nein | Nein |
| Primäre physikalische Wirkung | Mechanische Betätigung | Magnetfeld/Wirbelströme | Elektrisches Feld/Kapazitätsänderung |
| Typische Zielobjekte | Mechanisch geeignete Betätiger | Metall | Metall und geeignete Nichtmetalle |
| Typischer Einsatz | Endlage Tor | Stahlteil zählen | Füllstand an Kunststofftank |

**Optisch anhand einer Zylinderform allein nicht sicher zu unterscheiden:** Induktive und kapazitive Sensoren können sehr ähnlich aussehen. Datenblatt und Aufdruck entscheiden.

## 10. Hefteintrag zum Abschreiben

**Kapazitiver Näherungssensor:** Ein berührungsloser Sensor, der Änderungen der elektrischen Kapazität im elektrischen Feld vor seiner aktiven Fläche erkennt.

**Grundaufbau:** Messelektrode, mögliche Gegen-/Abschirmelektrode, Oszillator bzw. Kapazitätsmessung, Auswerteelektronik, Schaltausgang, Gehäuse/Anschluss.

**Funktionsweise:** Sensorfeld vorhanden → Material nähert sich → elektrische Kapazität verändert sich → Oszillator-/Messsignal verändert sich → Schwellwert wird ausgewertet → Ausgang schaltet.

**Erkennbare Stoffe:** Je nach Material und Sensor: Metalle, Kunststoffe, Holz, Glas, Pulver, Flüssigkeiten.

**Wichtige Einflussgrößen:** Dielektrizitätszahl εr, Materialmenge/Größe, Abstand, Wanddicke, Feuchtigkeit, Verschmutzung, Einbausituation und Empfindlichkeitseinstellung.

**Anwendung:** Füllstand eines geeigneten Kunststoffbehälters von außen erkennen.

**Abgrenzung:** Induktiv = Metall/Wirbelströme/magnetisches Wechselfeld; kapazitiv = Metall und Nichtmetalle/Kapazitätsänderung/elektrisches Feld.

**Schaltabstand:** Sn ist ein Nennwert und keine Garantie für jedes Material. Hysterese ist die Distanzdifferenz zwischen Ein- und Ausschaltpunkt.

## 11. AP1-Trainingsfragen

1. Was ist bei einem kapazitiven Sensor die entscheidende Messgröße?
2. Welche Materialien erkennt er typischerweise?
3. Wozu dienen die Elektroden?
4. Was verändert sich, wenn eine Kunststoffflasche in das Sensorfeld gelangt?
5. Wie beeinflusst die Dielektrizitätszahl εr die Kapazität (bei sonst identischer Geometrie)?
6. Warum kann ein geeigneter Sensor Füllstand durch eine Kunststoffwand erfassen?
7. Warum kann Feuchtigkeit eine Störung auslösen?
8. Ist das „Wirbelstromprinzip“ die Haupterklärung für einen kapazitiven Sensor?
9. Warum lässt sich Sa nicht für alle kapazitiven Sensoren pauschal aus 0,81·Sn berechnen?
10. Praxis: Erkläre von „Tank leer“ bis „Tank voll“ den Weg zur SPS-Meldung.
11. Wiederholung: Ein mechanischer Öffner (NC) wird betätigt – was passiert mit seinem Kontaktzustand?
12. Beispiel Hysterese: EIN 5,0 mm, AUS 5,6 mm – H berechnen.

## Herstellerinformationen / weiterführend
- Baumer: https://www.baumer.com/de/de/service-support/funktionsweise/funktionsweise-und-technologie-von-kapazitiven-sensoren/a/Know-how_Function_Capacitive-sensors
- Pepperl+Fuchs: https://www.pepperl-fuchs.com/de/support/knowledge-and-literature/knowledge-bases-for-industrial-sensors/knowledge-base-for-capacitive-sensors/detection-method-and-function-gp30377
- ifm: https://www.ifm.com/de/de/shared/technologien/kapazitiv/technologieubersicht
- Omron: https://www.ia.omron.com/support/faq/answer/41/faq00397/

**Hinweis:** Nur fachgerecht und nach sicherem Hersteller-Anschlussplan installieren/prüfen. Das Lernmaterial ersetzt keine Gefährdungsbeurteilung und kein Sicherheitskonzept.
