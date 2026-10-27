# LF3 – Lektion 2D: Optische Sensoren / Lichtschranke / Lichttaster

**Stand:** Unterricht beginnt; AP1-Prüfung noch offen.
**Lernverlauf:** 2A Mechanischer Endschalter 6/8, 2B Induktiver Sensor 11,5/12, 2C Kapazitiver Sensor 11,5/12.
**Ziel:** Aufbau, Signalweg, Funktionsweisen **Einweglichtschranke**, **Reflexionslichtschranke**, **Lichttaster**, Hell-/Dunkelschaltung, Störfaktoren, Ein- und Ausgänge verstehen.

## 1. Grundprinzip: Licht als Messinformation

Ein optischer Sensor (fotoelektrischer Sensor) sendet Licht aus und wertet empfangenes Licht aus. Je nach Sensorbauart erkennt er:
- eine **Unterbrechung** des direkten Lichtwegs (Einweglichtschranke),
- eine **Unterbrechung** des zum Sensor zurückkehrenden reflektierten Lichtwegs (Reflexionslichtschranke mit Reflektor),
- eine **Reflexion am Objekt selbst** (Lichttaster).

**Wichtig:** Bei den ersten beiden Varianten ist das Messsignal bei einem opaken Objekt typischerweise **weniger empfangenes Licht**; beim einfachen Lichttaster typischerweise **mehr empfangenes Licht vom Objekt**. Eine eventuell invertierte Ausgangsfunktion (Hell-/Dunkelschaltung) darf nicht mit der Optik verwechselt werden.

## 2. Bauteile und Aufgabe

1. **Lichtsender:** LED mit sichtbarem Rotlicht oder Infrarot; besondere Sensoren verwenden Laser.
2. **Optik / Linse:** Bündelt und richtet Licht aus.
3. **Lichtempfänger:** Fotodiode/Fototransistor wandelt empfangene Lichtleistung in ein elektrisches Messsignal um.
4. **Verstärker / Signalauswertung:** Prüft Intensität und oft modulierte Lichtsignale, filtert Fremdlicht und vergleicht Messwert mit Schwellwert.
5. **Ausgangsstufe:** Liefert z. B. einen PNP/NPN-Schaltzustand an die SPS.
6. **Gehäuse, LED, Einsteller/Teach-in, Leitung/M8/M12-Stecker:** Montage, Betrieb und Anpassung.

Ein optischer Sensor ist KEIN induktiver Sensor (keine Wirbelströme nötig) und kein kapazitiver Sensor (keine Kapazitätsänderung als primäre Messgröße).

## 3. Einweglichtschranke (Durchlichtsensor)

**Aufbau:** Lichtsender und Lichtempfänger stehen sich in **zwei getrennten Gehäusen** gegenüber. Beide müssen zueinander ausgerichtet sein, im Allgemeinen getrennt elektrisch versorgt (abhängig vom Typ).

**Funktion:**
1. Sender schickt einen Lichtstrahl zum Empfänger.
2. Ohne Objekt empfängt der Empfänger genug Licht.
3. Ein Karton unterbricht den Lichtstrahl.
4. Die Empfangslichtmenge fällt.
5. Auswerteelektronik erkennt Schwellenwertunterschreitung.
6. Ausgangsstufe setzt den gewählten Schaltmodus um → SPS-Eingang wird aktualisiert.

**Vorteile:** Große Reichweiten, gute zuverlässige Erkennung vieler lichtundurchlässiger Objekte; Objektoberfläche und -farbe sind relativ unkritisch.
**Nachteile:** Zwei Geräte an gegenüberliegenden Seiten, mehr Montage/Verdrahtung und Ausrichtung; transparente oder sehr kleine Objekte erfordern Speziallösungen oder sorgfältige Auslegung.

## 4. Reflexionslichtschranke (Retroreflexion)

**Aufbau:** Sender und Empfänger sind in **einem gemeinsamen Sensorgehäuse**; gegenüber liegt ein **passiver Reflektor** (kein elektrischer Anschluss für den Reflektor).

**Funktion:**
1. Sensor sendet Licht zum Reflektor.
2. Reflektor lenkt das Licht zum Empfänger im selben Sensorgehäuse zurück.
3. Ein lichtundurchlässiges Objekt unterbricht Hin- und Rückweg.
4. Der Lichtempfang sinkt; die Auswertung schaltet den Ausgang entsprechend der Einstellung.

**Vorteile:** Nur ein Sensorgehäuse muss elektrisch versorgt werden; einfachere Verkabelung als Einweg; moderate Reichweite.
**Grenzen:** Reflektor muss montiert, sauber und passend ausgerichtet sein. Stark reflektierende/glänzende Gegenstände können bestimmte nicht polarisierte Reflexlichtschranken täuschen; Polarisationsfilter helfen bei entsprechend ausgelegten Sensoren. Durchsichtige Gegenstände brauchen oft speziell ausgelegte Sensoren.

## 5. Lichttaster (diffus/reflexiv am Objekt)

**Aufbau:** Sender und Empfänger in einem Gehäuse, **kein gegenüberliegender Reflektor** erforderlich.
**Funktion:**
1. Sender strahlt ein Objekt an.
2. Licht reflektiert an dessen Oberfläche in Richtung Sensor.
3. Der Empfänger erfasst eine ausreichende reflektierte Lichtmenge.
4. Elektronik wertet das Signal aus und schaltet den Ausgang.

**Vorteile:** Nur ein Gerät, kein Reflektor, einfacher Aufbau.
**Grenzen:** Abstand und Erkennung hängen beim einfachen Lichttaster stärker von Oberfläche, Größe, Farbe, Glanz und Hintergrund ab. Ein schwarzes mattes Objekt reflektiert häufig weniger Licht als ein weißes.

**Hintergrundausblendung:** Ein spezieller Lichttaster nutzt oft optische Triangulation/mehrere Empfangsbereiche, um Objekte innerhalb eines eingestellten Entfernungsbereichs zu erkennen und einen weiter entfernten Hintergrund zu ignorieren. Nicht bloß die Helligkeitsschwelle eines einfachen Lichttasters.

## 6. Vergleichstabelle
| Typ | Sender | Empfänger | Reflektor | Bei Karton auf Lichtweg/Position |
|---|---|---|---|---|
| Einweglichtschranke | separates Gehäuse | separates Gehäuse | Nein | direktes Licht unterbrochen |
| Reflexionslichtschranke | im Sensor | im Sensor | Ja, gegenüber | zurückkehrendes Licht unterbrochen |
| Lichttaster | im Sensor | im Sensor | Nein | reflektiertes Licht vom Karton steigt |

## 7. Hell-/Dunkelschaltung

Achtung auf getrennte Begriffe:
- **Hellschaltend / Light-on (LO):** Ausgang aktiviert, wenn Empfänger ausreichend Licht erkennt.
- **Dunkelschaltend / Dark-on (DO):** Ausgang aktiviert, wenn Empfänger **nicht ausreichend Licht** erkennt.

Bei einer **Einweglichtschranke** mit Karton im Strahl:
- Karton unterbricht Strahl → Empfänger ist „dunkel“.
- **Dunkelschaltender Ausgang** wird nun aktiv.
- **Hellschaltender Ausgang** wäre bei freiem Strahl aktiv.

Beim **einfachen Lichttaster** ist die Lichtlage häufig umgekehrt: Objekt reflektiert Licht zum Empfänger; dann kann **hellschaltend = Objekt erkannt** sinnvoll sein.

Das Ausgangssignal hängt immer von Schaltmodus und Geräteverdrahtung ab.
**PNP/NPN** beschreibt die elektrische Ausgangsstufe und ist nicht mit Hell-/Dunkelschaltung gleichzusetzen.
**NO/NC** beschreibt die logische Schaltfunktion; je nach Hersteller und Betriebsart ist die Zuordnung zur optischen Erkennungslogik zu prüfen.

## 8. Anschluss am Beispiel eines 3-Leiter-DC-Sensors

Ein häufiger Anschluss laut jeweiligem Datenblatt:
- Braun (BN): L+, Versorgung 24 V DC (modellabhängig)
- Blau (BU): M, 0 V
- Schwarz (BK): Q, Schaltausgang

Empfangsleistung → elektrische Messgröße → Auswerteeinheit/Schwellwert → Ausgangstransistor → SPS-Eingang.
Der Sender einer Einweglichtschranke hat häufig eigene Versorgungsanschlüsse; nicht jedes Lichtschrankenset ist ein einzelnes 3-Draht-Gerät.

## 9. Störungen und Schutz
- Schmutz/Staub auf Linse oder Reflektor senkt Lichtleistung und damit die **Funktionsreserve**.
- Fremdlicht/Sonne, Reflexionen, Nebel und Dampf können Fehlfunktionen auslösen; modulierte Sender und optische Filter können die Störfestigkeit erhöhen.
- Falsche Ausrichtung, nicht passender Reflektor oder zu großer Abstand.
- Dunkle/hochglänzende oder transparente Objekte bei einfacher Tastererfassung kritisch.
- Durchsichtige Flaschen: passende transparente-Objekt-Spezialsensoren verwenden.
- Laser-Lichtquellen: nur entsprechend Geräteklassifizierung und Anleitung handhaben; nicht direkt in den Strahl sehen.

**Diagnose:** Sichtprüfung, Ausrichtung, Sensor-/Empfänger-LED, Verschmutzung, Schaltschwelle/Teach-in, Ausgangslogik, Versorgung, Bezugspotenzial und SPS-Eingang prüfen. Nie an laufende Maschinen oder an spannungsführende Anschlüsse ohne geeignetes Sicherheitsverfahren gehen.

## 10. Praxisfall: Pakete zählen

An beiden Förderbandseiten Sender und Empfänger einer Einweglichtschranke.
1. Paket kommt in den Strahl.
2. Lichtweg ist unterbrochen; Empfängerlicht sinkt.
3. Auswertung schaltet einen passenden Ausgang (z. B. dunkel-schaltend aktiv).
4. SPS erkennt den Eingang und zählt bei einem geeigneten Signalflankenereignis ein Paket.
5. Wenn das Paket den Strahl verlässt, kommt Licht zurück. Ausgang schaltet in den Ausgangszustand.
**Wichtig:** Zählung vorzugsweise bei Zustandswechsel/Flanke; nicht in jedem SPS-Zyklus erneut, während der Lichtweg unterbrochen bleibt.

## 11. Hefteintrag zum Abschreiben

**Optischer Sensor:** Ein Sensor, der Objekte mittels ausgesendetem und empfangenem Licht erkennt.

**Aufbau:** Lichtsender (LED/evtl. Laser) – Optik/Linse – Lichtempfänger (Fotodiode/Fototransistor) – Auswerteelektronik – Schaltausgang – Gehäuse und Anschlüsse.

**Funktionsablauf:** Licht aussenden → Licht wird empfangen/unterbrochen/reflektiert → Empfänger wandelt Licht in elektrisches Messsignal um → Auswerteelektronik prüft Schwellwert → Ausgangsstufe schaltet → SPS erhält Signal.

**Einweglichtschranke:** Sender und Empfänger in **zwei gegenüberliegenden Gehäusen**; Objekt unterbricht Licht.
**Reflexionslichtschranke:** Sender und Empfänger in **einem Gehäuse**, gegenüber **passiver Reflektor**; Objekt unterbricht Rücklichtweg.
**Lichttaster:** Sender und Empfänger in **einem Gehäuse**, **kein Reflektor**; Objekt reflektiert Licht zum Empfänger.

**Hellschaltung:** Ausgang aktiv bei ausreichendem Lichtempfang.
**Dunkelschaltung:** Ausgang aktiv bei zu wenig Lichtempfang.

**Störfaktoren:** Schmutz, Fehljustage, Fremdlicht, transparente Objekte, Entfernung, Oberflächenfarbe/-reflexion und Hintergrund.

**Merksatz:** Einweg = 2 elektrische Geräte; Reflex = 1 elektrischer Sensor + Reflektor; Taster = 1 Sensor, Objekt reflektiert.

## 12. Prüfungsfragen ohne Lösungen
1. Was macht der Sender einer Lichtschranke?
2. Welches Bauteil wandelt empfangenes Licht in ein elektrisches Signal um?
3. Wie viele Geräte stehen bei einer Einweglichtschranke einander gegenüber?
4. Welche Rolle hat der Reflektor einer Reflexionslichtschranke? Benötigt er eine Versorgung?
5. Wie kommt Licht bei einem Lichttaster zum Empfänger zurück?
6. Bei einer Einweglichtschranke unterbricht der Karton das Licht. Ist der Empfänger jetzt hell oder dunkel?
7. Was bedeutet dunkel-schaltend?
8. Warum kann ein schwarzer Karton einen einfachen Lichttaster schwieriger machen als ein weißer?
9. Wie hilft Hintergrundausblendung?
10. Sender, Empfänger, Auswertung und Ausgangsstufe in richtiger Reihenfolge erklären.
11. Eine Lichtschranke soll Pakete zählen: Wie vermeidet die SPS, dass ein Paket mehrfach gezählt wird?
12. Fehlersuche: Reflektionslichtschranke schaltet nicht – drei plausible Ursachen.

## Herstellerquellen (fachlich)
- [ifm: Photoelectric sensing principles](https://www.ifm.com/us/en/us/learn-more/position/photoelectric-sensor/select-by-application)
- [ifm: Through-beam, retroreflective, diffuse](https://www.ifm.com/us/en/us/learn-more/position/standard-photoelectric)
- [Balluff: Differences between photoelectric sensors](https://www.balluff.com/en-de/document/FAQ-18442625)

## Reale Bilder (zugehörige konkrete Modelle, Weblinks)
- [SICK WSE4SC, Sender und Empfänger – Produktfoto](https://uk.rs-online.com/web/p/photoelectric-sensors/1347785)
- [Panasonic CX-491-Y, Reflexionslichtschranke und Reflektor – Produktfoto](https://uk.rs-online.com/web/p/photoelectric-sensors/9012863?gb=s)
- [Turck QS18EN6DB, Lichttaster – Herstellerfoto](https://www.turck.com.tr/tr/product/3068745)

**Hinweis:** Fotos zeigen konkrete Typen. Der Sensoraufbau und Anschluss unterscheiden sich modellabhängig; vor jeder Installation das Originaldatenblatt verwenden.
