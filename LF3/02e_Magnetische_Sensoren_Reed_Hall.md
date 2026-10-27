# LF3 – Lektion 2E: Magnetische Sensoren – Reedkontakt und Hall-Sensor

**AP1-Lernziel:** Funktion und Aufbau von magnetischen Reed- und Hall-Sensoren detailliert verstehen; Kontakt versus Halbleiter unterscheiden; Magneterkennung eines Pneumatikzylinders erklären; SPS-Signal und Fehlerbilder erklären. Die Lektion 2D wurde im Chat mit **9,25/12 Punkten** bewertet (Praxis teilweise falsch, zu wiederholen).

## 1. Magnetische Positionssensoren

Beide Sensorkonzepte erkennen ein **Magnetfeld**, typischerweise von einem **Permanentmagneten**. Das Magnetfeld kann statisch sein; der Magnet braucht nicht dauerhaft bewegt zu werden. Das ist ausdrücklich anders als die Wirbelstrom-Anregung beim klassischen induktiven Näherungssensor.

Bei Pneumatikzylindern ist oft ein Ringmagnet im **Kolben** integriert. Außen an der meist nichtferromagnetischen Zylinderwand (z. B. Aluminiumprofil) sitzt der Sensor. Wenn der Kolben am Sensor vorbeikommt, erkennt dieser das Magnetfeld: Die SPS kann daraus die Kolbenposition ableiten.

## 2. Reedkontakt – realer Aufbau

1. **Glasröhrchen**: hermetische Kapsel (häufig Schutzgasfüllung, teils Vakuum je nach Typ).
2. **Zwei ferromagnetische Kontaktzungen (Reeds)**: innen befestigt, stehen im Grundzustand bei einem NO-Reed mit kleinem Luftspalt auseinander.
3. **Kontaktoberflächen**: oft beschichtet, um Schaltverhalten zu verbessern.
4. **Anschlussdrähte**: führen zum externen Stromkreis.
5. **Magnetisches Feld**: magnetisiert die Kontaktzungen.

**NO-Reedkontakt schrittweise:**
- Ohne ausreichendes Magnetfeld: Kontaktzungen getrennt, elektrischer Stromweg offen.
- Magnet nähert sich: Feld magnetisiert Kontaktzungen. Sie ziehen sich gegenseitig an.
- Kontaktzungen berühren sich: Kontakt schließt, Stromkreis kann geschlossen werden.
- Magnet entfernt: elastische Rückstellkraft trennt die Zungen wieder, Kontakt öffnet.

**NC- und Wechsler-Reeds gibt es ebenfalls**, aber der normale einfache Reed-Schließer ist das Standardbeispiel.
**Wichtig:** Ein passiver Reedkontakt **erzeugt keine eigene Spannung** und braucht selbst keinen Oszillator. Im angeschlossenen Schaltkreis muss eine passende Versorgung zur Signalauswertung vorliegen. Komplette Reed-Sensoren können LEDs, Schutzbeschaltung und mehr als zwei Drähte enthalten; nicht allein aus der Aderzahl die Funktionsart ableiten.

## 3. Reed – Rolle eines Kontaktes und Grenzen

Vergleich mit mechanischem Endschalter:
- Mechanischer Endschalter: Kontaktänderung durch **Druck eines Hebels**.
- Reedkontakt: Kontaktänderung durch **Magnetkraft**, ohne mechanische Berührung durch das zu detektierende Objekt; **innen bewegen sich trotzdem Kontaktzungen**.

Grenzen: mechanisches Kontaktprellen, endliche Lebensdauer unter Last, Kontaktabbrand/Verkleben bei überlasteten oder induktiven Lasten, Glasbruch durch Stöße. Herstellergrenzen für Schaltstrom/-spannung/-leistung beachten; keine großen Antriebe direkt an kleinem Reedkontakt schalten.

## 4. Hall-Sensor – innerer Aufbau

1. **Hall-Element**: kleine stromdurchflossene Halbleiterplatte.
2. **Stromversorgung/Bias**: treibt Strom durch Hall-Element.
3. **Magnetfeld**: hat eine geeignete Komponente senkrecht zum Stromfluss bzw. zur Hall-Platte.
4. **Lorentzkraft**: lenkt bewegte Ladungsträger seitlich ab.
5. **Hall-Spannung U_H**: durch Ladungstrennung entsteht eine quer zum ursprünglichen Strom messbare Spannung.
6. **Verstärker/Auswertung**: verarbeitet die kleine Hall-Spannung.
7. **Ausgangsstufe**: kann abhängig vom konkreten Typ digital EIN/AUS schalten oder einen analogen Messwert liefern.

**Wichtig:** Hall-Sensoren brauchen eine Betriebsspannung für ihre Elektronik und können **auch ein konstantes/statisches Magnetfeld erkennen**. Hall-Sensoren benötigen keinen Oszillator, der Wirbelströme im Magneten erzeugt. Sie haben keine mechanisch bewegten Schaltkontakte.

Beispiel: Allegro A1104EUA-T ist ein integrierter Hall-Schalter im Dreibeingehäuse (Gehäusefoto); ein **Hall-IC** ist nicht automatisch ein komplettes für 24-V-SPS verdrahtetes Industriesensorgehäuse.

## 5. Reed vs. Hall (AP1)

| Merkmal | Reedkontakt | Hall-Sensor |
|---|---|---|
| Physikalisches Prinzip | Magnetisierte metallische Zungen ziehen sich an | Magnetfeld erzeugt Hall-Spannung im stromdurchflossenen Halbleiter |
| Mechanisch bewegte Kontakte innen | Ja | Nein |
| Externer Magnet | Üblich | Üblich |
| Statisches Magnetfeld messbar | Ja | Ja |
| Benötigt Sensor-Elektronikversorgung | Reiner passiver Kontakt: nein (Signalkreis benötigt Versorgung) | Ja |
| Ausgänge | Mechanischer NO/NC/Wechsler-Kontakt (modellabhängig) | Elektronisch, z. B. digital oder analog |
| Typische Störungen | Kontaktprellen, Überlast, Glasbruch, Montage | Falsche Polung/Orientierung, Versorgung fehlt, Störungen, Montage |
| Typische Verwendung | Zylinder-Positionsschalter, Türen/Fenster | Zylinderposition, Drehzahl, Stellung, Magnetfeldmessung |

Der Unterschied **Reed (Kontakt)** vs. **Hall (Halbleiter)** ist wichtiger als eine pauschale Aderfarbenregel.

## 6. Praxis: Pneumatikzylinder

- Im Kolben ist bei entsprechend ausgerüsteten Pneumatikzylindern ein Dauermagnet integriert.
- Außen sitzt der Reed-/Hall-Sensor in einer T-Nut oder an Halterung.
- Bewegt sich der Kolben vor den Sensor, erreicht dessen Magnetfeld das Sensorelement.
- Reedkontakt schließt/öffnet, oder Hall-Elektronik schaltet je nach Typ.
- SPS bekommt Signal „Kolben an Position X“ und kann die nächste Aktion freigeben.
- Zwei Sensoren in zwei Endlagen ermöglichen die getrennte Rückmeldung „eingefahren“ und „ausgefahren“.

Der Magnet muss nicht bei jedem Zeitpunkt bewegen, damit ein Schaltsignal bestehen bleibt. Die Position des Sensors relativ zum Magneten entscheidet.

## 7. Hall-Schaltschwelle und Hysterese

Bei einem digitalen Hall-Schalter:
- **B_OP**: magnetischer Schaltpunkt (Magnetfeldstärke für Auslösen).
- **B_RP**: magnetischer Rückschaltpunkt.
- Magnetische Hysterese: Unterschied zwischen B_OP und B_RP; verhindert häufiges Umschalten bei Störfeld/kleinen Bewegungen.
Hier hat die Hysterese zunächst **die Einheit einer magnetischen Flussdichte** (z. B. mT), nicht automatisch Millimeter. An einem bewegten Zylinder kann sich daraus räumlich ein unterschiedlicher Ein-/Ausschaltpunkt ergeben.
N-/S-Pol-Empfindlichkeit ist typabhängig: unipolare, bipolare und omnipolare Hall-Schalter existieren. Nicht jeder Hall-Sensor reagiert beliebig auf beide Pole.

## 8. Elektrischer Signalweg

Reedkontakt (Grundbeispiel):
**Magnet → Kontaktzungen schließen → Spannung im externen passenden Stromkreis wird an SPS-Eingang erkennbar**.

Hall-Schalter (Grundbeispiel):
**Magnetfeld → Hall-Spannung → Verstärker/Schwellwert → elektronische Ausgangsstufe → SPS-Eingang**.

Bei Industriesensoren Pinbelegung/PNP/NPN und Betriebsspannung strikt nach Datenblatt; die übliche BN/L+, BU/M, BK/Q-Belegung vieler dreipoliger DC-Sensoren ist nicht universell und gilt **nicht automatisch** für alle Hall-ICs oder passiven Reeds.

## 9. Fehlerbilder

- Keine Positionsmeldung am Zylinder: Kein Magnet im Kolben, Sensor falsch montiert oder zu weit entfernt, Sensortyp/Magnetfeldrichtung unpassend.
- Reed-Ausgang prellt/instabil: Vibration, Verschleiß, ungeeignete Position, magnetische Hysterese, zu hohe Schaltlast.
- Hall meldet nicht: Versorgung fehlt, falscher Magnetsüd-/Nordpol, falsche Ausrichtung, Schaltschwelle nicht erreicht, falsche SPS-Eingangsbeschaltung.
- LED schaltet, SPS nicht: Verdrahtung, falscher Ausgangstyp oder Bezugspotenzial.

Nie an einer unter Druck stehenden oder sich bewegenden Maschine ungesichert arbeiten. Magnetische Positionssensoren sind nicht ohne Weiteres sicherheitsgerichtete Schutzeinrichtungen.

## 10. Hefteintrag (zum Abschreiben)

**Magnetischer Näherungssensor:** Erkennt das Magnetfeld eines Magneten, z. B. am Kolben eines Pneumatikzylinders.

**Reedkontakt: Aufbau:** Hermetisches Glasröhrchen mit zwei ferromagnetischen, elastischen Kontaktzungen und elektrischen Anschlüssen.

**Reedkontakt: Funktion:** Magnetfeld magnetisiert Zungen → Zungen ziehen sich an → bei NO schließen die Kontakte → bei Entfernen des Feldes öffnen sie wieder. Ein passiver Reedkontakt erzeugt keine eigene Spannung; er schaltet einen vorhandenen Stromkreis.

**Hall-Sensor: Aufbau:** Stromdurchflossenes Hall-Halbleiterelement, Auswerte- und Ausgangselektronik.

**Hall-Sensor: Funktion:** Magnetfeld wirkt auf Ladungsträger im stromdurchflossenen Halbleiter → Lorentzkraft lenkt Ladungsträger quer ab → Hall-Spannung entsteht → Auswertelektronik erkennt Feld und schaltet Ausgang bzw. liefert Messwert.

**Praxis:** Magnet im Zylinderkolben bewegt sich am außen montierten Sensor vorbei → SPS erkennt Kolbenposition.

**Reed vs. Hall:** Reed hat innen mechanische Kontakte; Hall arbeitet elektronisch ohne mechanisch bewegte Kontakte. Beide können ein stehendes Magnetfeld erkennen.

**Hysterese Hall:** Unterschied zwischen magnetischem Ein- und Rückschaltpunkt (z. B. in mT), nicht mit Sn/Sa gleichzusetzen.

## 11. AP1-Training (Lösungen nach Bearbeitung)

1. Welche Größe wird von Reed und Hall erkannt?
2. Wie sind die Kontakte in einem einfachen NO-Reedkontakt ohne Magnet angeordnet?
3. Was bewirkt das äußere Magnetfeld in den Reed-Zungen?
4. Braucht ein rein passiver Reedkontakt eine eigene Betriebsspannung, um seine Zungen zu bewegen?
5. Was bewirkt die Lorentzkraft im Hall-Element?
6. Was ist die Hall-Spannung?
7. Können Reed und Hall einen ruhenden Magneten erkennen?
8. Welcher der beiden Sensortypen besitzt bewegte mechanische Kontakte?
9. Warum sitzt am Kolben eines geeigneten Pneumatikzylinders ein Magnet?
10. Weshalb kann das elektrische Ausgangssignal eines Hall-Sensors abhängig vom Typ unterschiedlich sein?
11. Was bedeuten B_OP und B_RP eines digitalen Hall-Schalters?
12. Wiederholung Lichtschranke: Ist die LED oder die Fotodiode der Lichtsender? Was ist bei einem dunkel-schaltenden Sensor mit unterbrochenem Strahl aktiv?
13. Praxis: Ein Zylinder erreicht Endposition. Beschreibe Magnet, Sensor, internes Signal, SPS-Eingang, mögliche Folgereaktion.

## Hersteller-/Quellen
- Festo: [Näherungsschalter SME-8M mit Reed-Messprinzip](https://www.festo.com/at/de/p/naherungsschalter-id_SME_8M)
- ZF: [Magnetische Näherungssensoren – Hall und Reed](https://switches-sensors.zf.com/de/sensors-faqs/)
- Allegro MicroSystems: [Hall-effect sensor applications guide](https://www.allegromicro.com/en/Insights-and-Innovations/Technical-Documents/Hall-Effect-Sensor-IC-Publications/Hall-Effect-IC-Applications-Guide)
- Balluff: [Pneumatic-cylinder magnetic sensing](https://www.balluff.com/assets/services/downloads/white-papers/Sensor-Technologies-to-Detect-Pneumatic-Cylinder-Position_011422.pdf)

### Echte Bilder – externe Quellen
- [Glas-Reedkontakt – echtes Produktbild](https://dsmonline.in/product/2x10-mm-magnetic-reed-switch-dwqmp)
- [Festo SME-8M – Reed Zylindersensor, echtes Foto](https://it.rs-online.com/web/p/sensori-per-cilindri-pneumatici/1215823)
- [Allegro A1104 – integrierter Hall-Schalter, echtes Produktfoto](https://evelta.com/a1104eua-t-hall-effect-switch-sip-3-allegro-microsystems/)
- [Pneumatikzylinder und außen montierter Sensor – Produktfoto](https://www.alifsensor.com/products/dfgj-magnetic-cylinder-sensor/)

**Sicherheit:** Nur qualifiziert, nach passenden Geräteanschlussplänen und abgesicherter Anlage messen/anschließen; keine direkte Lastschaltung mit unterdimensioniertem Reedkontakt.
