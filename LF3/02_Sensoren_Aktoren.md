# LF3 – Lektion 2: Sensoren und Aktoren (AP1)

**Lernziel:** Sensor- und Aktortypen erkennen, anhand ihrer Funktion auswählen, das EVA-Prinzip auf reale Anlagen übertragen und Kontakt-/Ausgangsfunktionen unterscheiden.

## 1. Eingang, Verarbeitung, Ausgabe
- **Bediengerät**: Start-/Stopptaster stellt ein Eingangssignal bereit.
- **Sensor**: Erfasst einen Prozesszustand und gibt ein Signal an die Steuerung, z. B. Position einer Kiste.
- **Steuerung (VPS/SPS)**: Prüft Eingangssignale und die programmierten/verdrahteten Bedingungen.
- **Aktor**: Bewirkt eine physikalische Veränderung, z. B. Motor dreht, Magnetventil schaltet Druckluft.

EVA-Wirkungskette: **Sensor → SPS/VPS → Ausgang/Schaltgerät → Aktor → mechanische Wirkung**.
Ein Schütz ist ein elektrisch betätigtes Schaltgerät, über das beispielsweise der Leistungsstrom eines Motors geschaltet werden kann. Die SPS steuert nicht automatisch einen Motor direkt mit ihrem kleinen Signal-Ausgangsstrom.

## 2. Wichtige Sensorarten (mit Erkennung)

| Gerät | Wirkprinzip | Typischer Einsatz | AP1-Merksatz |
|---|---|---|---|
| Mechanischer Endschalter/Rollenhebel | Ein Objekt betätigt mechanisch den Kontakt | Endlage an Tor oder Maschine | Berührende Erfassung |
| Induktiver Näherungssensor | Metall verändert ein elektromagnetisches Feld | Metallteil vor Förderband | Berührungslos, **Metall** |
| Kapazitiver Näherungssensor | Material verändert elektrisches Feld/Kapazität | Plastik/Glas, Füllstand, Metall | Erfasst **auch Nichtmetalle**; Eignung von Material/Umgebung abhängig |
| Optischer Sensor/Lichtschranke | Lichtstrahl/Reflexion wird ausgewertet | Karton auf Förderband | Licht als Messprinzip |
| Magnetsensor/Reedkontakt | Magnetfeld betätigt Kontakt/Schaltsignal | Zylinderposition | Magnetfeld |
| Temperatursensor | Temperaturabhängiges Messsignal | Heizung, Lagerüberwachung | Messwert statt reines Tasterkommando |

**Lichtschranke:** Bei einer Einweglichtschranke stehen Sender und Empfänger getrennt; ein unterbrochener Strahl kann zur Erkennung dienen. Reflexions-Lichtschranken nutzen einen Reflektor; Lichttaster detektieren reflektiertes Licht vom Objekt selbst. Reflexion/Fremdlicht kann die Erfassung beeinflussen.

## 3. Schließer, Öffner, Wechsler

- **Schließer (NO, Normally Open)**: Im unbetätigten Grundzustand offen, bei Betätigung geschlossen.
- **Öffner (NC, Normally Closed)**: Im unbetätigten Grundzustand geschlossen, bei Betätigung offen.
- **Wechsler**: Ein gemeinsamer Kontakt schaltet zwischen zwei Kontaktwegen um.

Bei mechanischen Tastern im Grundzustand bezieht sich die Bezeichnung auf die unbetätigte Stellung. Bei elektronischen Sensoren beschreibt NO/NC die Schaltausgangsfunktion bezogen auf die jeweilige Erkennungsbedingung; Datenblatt beachten.

Beispiel: Starttaster oft Schließer; gewöhnlicher Stopptaster in Steuerstromkreisen häufig Öffner. Das allein ist noch kein normgerechtes Sicherheitskonzept für einen Not-Halt.

## 4. PNP/NPN und übliche 3-Draht-DC-Sensoren (Grundlagen)

- **PNP (positiv schaltend):** Bei aktivem Schaltausgang wird typischerweise eine positive Spannung für einen geeigneten Eingang bereitgestellt.
- **NPN (negativ schaltend):** Bei aktivem Schaltausgang wird typischerweise gegen 0 V geschaltet.
- **PNP/NPN** ist nicht mit **NO/NC** gleichzusetzen. Beide Kombinationen sind möglich.
- Viele 3-Leiter-Gleichspannungssensoren haben **Braun = L+**, **Blau = M/0 V**, **Schwarz = Ausgang Q**. Der Typ kann abweichen; Anschlussbelegung immer aus dem konkreten Datenblatt lesen.
- Anschluss niemals nach Farben allein. Prüfen: Betriebsspannung, Pinbelegung, Ausgangstyp und zulässige Last.

Quellen:
- [SICK Betriebsanleitung induktive Sensoren](https://www.sick.com/media/docs/2/82/582/operating_instructions_inductive_proximity_sensors_induktive_n%C3%A4herungssensoren_en_de_fr_it_es_zh_ru_pt_ja_im0085582.pdf)
- [Schneider Electric: PNP/NPN-Sensoren](https://www.se.com/uk/en/faqs/FA142566/)
- [ifm: kapazitive Sensoren](https://www.ifm.com/de/de/shared/technologien/kapazitiv/chemisch-resistente-kapazitive-sensoren)

## 5. Aktoren: Beispiele
- **Elektromotor:** Wandelt elektrische Energie in mechanische Drehbewegung.
- **Magnetventil:** Elektromagnet schaltet ein Fluidventil; kann z. B. Druckluft zu einem Zylinder freigeben.
- **Pneumatikzylinder:** Setzt Druckluft in eine lineare Bewegung um.
- **Meldeleuchte/Summer:** Gibt optische/akustische Rückmeldung.
- **Schütz:** Ein elektrisch betätigtes Schaltgerät zur Schaltung einer Last; die Schützspule ist der Steuerungsausgang zugeordnet, der Motor erzeugt die mechanische Wirkung.

## 6. Fallbeispiel: Förderband
1. Ein optischer Sensor erkennt einen Karton.
2. Das SPS-Eingangsmodul erfasst den Schaltzustand.
3. Das SPS-Programm prüft, ob der Motor anhalten soll.
4. Der entsprechende Ausgang steuert ein geeignetes Schaltgerät/Antriebssystem.
5. Der Motor hält an; Nachprüfung und ggf. Meldung.

**Prüfungsfalle:** Eine Lichtschranke erkennt nicht automatisch jede Materialfarbe gleich gut, ein induktiver Sensor erkennt nicht einfach beliebige Kunststoffe und der SPS-Ausgang ersetzt kein geeignetes Motor-Leistungsschaltgerät.

## 7. Hefteintrag zum Abschreiben

**Sensor:** Erkennt eine physikalische Größe oder einen Zustand und liefert ein Signal an die Steuerung. Beispiele: Endschalter, induktiver Sensor, Lichtschranke.

**Aktor:** Setzt ein elektrisches Steuersignal bzw. die Steuerwirkung in einen physikalischen Vorgang um. Beispiele: Motor, Magnetventil, Meldeleuchte.

**Sensorprinzipien:**
- Mechanisch: Berührung/Betätigung.
- Induktiv: Erfassung von Metall.
- Kapazitiv: Auch nichtmetallische Stoffe/Füllstände.
- Optisch: Lichtstrahl/Lichtreflexion.
- Magnetisch: Magnetfeld.

**Schließer (NO):** Im Grundzustand offen; beim Auslösen geschlossen.
**Öffner (NC):** Im Grundzustand geschlossen; beim Auslösen offen.

**PNP:** Bei Aktivierung positiver Schaltausgang.
**NPN:** Bei Aktivierung negativer Schaltausgang (gegen 0 V).
**NO/NC beschreibt die Schaltfunktion, PNP/NPN die Ausgangsschaltung.**

Übliche Farben vieler DC-Dreileitersensoren: **braun L+**, **blau M/0 V**, **schwarz Q/Ausgang**. **Hersteller-Anschlussplan ist maßgeblich.**

**EVA im Förderband:** Lichtschranke (E) → SPS (V) → Schütz/Antrieb/Motor (A).

## 8. Übung
1. Metallteil berührungslos erkennen: Welcher Sensor?
2. Nichtmetallischen Füllstand erfassen: Welcher Sensor?
3. Was unterscheidet Lichtschranke und Lichttaster?
4. Im Grundzustand geschlossener Kontakt: NO oder NC?
5. In einem DC-Dreileitersensor: Was sind L+, M und Q?
6. PNP und NPN: Was schaltet gegen Plus, was gegen 0 V?
7. Sensor meldet, Motor läuft dennoch: drei plausible Fehlerbereiche nennen.
8. Ein Motor soll nur anlaufen, wenn Start gedrückt und kein Werkstück an Position X erkannt wurde. Welche Eingangsbedingungen sind zu prüfen?
9. Ordne dem EVA-Prinzip zu: Lichtschranke, SPS, Motor.
10. Warum sind Steuerstromkreis und Hauptstromkreis zu unterscheiden?

**Sicherheit:** Anschlussarbeiten nur spannungsfrei und nach dem verifizierten Geräteanschlussplan mit geeigneter Qualifikation/Anleitung. Die Übung ersetzt kein Sicherheitssystem.
