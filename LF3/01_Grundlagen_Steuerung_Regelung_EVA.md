# LF3 – Lektion 1: Steuerung, Regelung, EVA und Wirkungskette

**Lernziel:** Die Steuerung einer Anlage in Eingabe, Verarbeitung und Ausgabe zerlegen; die Ursache-Wirkung-Kette erklären; Steuerung und Regelung unterscheiden; Sensorsignal, Steuerung und Aktor richtig zuordnen.

## 1. Berufssituation: Förderband

Ein Werkstück liegt auf einem Förderband. Ein Bediener betätigt **Start**. Die Steuerung verarbeitet das Startsignal und schaltet über ein Schütz den Motor. Das Band fördert die Ware. Betätigt der Bediener **Stopp**, wird die Abschaltung veranlasst. Die genauen Funktionen einer realen Anlage richten sich nach ihrer dokumentierten Steuerung und ihrem Sicherheitskonzept.

**Wichtig:** Der Starttaster schaltet im üblichen Aufbau nicht den Motor-Leistungsstrom direkt. Die Steuerung betätigt ein geeignetes Schaltgerät; der Motor liegt im Hauptstromkreis.

## 2. EVA in der Steuerungstechnik

| Stufe | Aufgabe | Förderbandbeispiel |
|---|---|---|
| E – Eingabe | Bedien- und Sensorsignale aufnehmen | Starttaste, Stopptaste, Endschalter |
| V – Verarbeitung | Bedingungen prüfen, Ausgang festlegen | Relaislogik oder SPS |
| A – Ausgabe | Schaltbefehl an Aktor übermitteln | Schützspule erhält Ansteuerung; Motor kann über Hauptkontakte versorgt werden |

**Begriffe:**
- Sensor: Erfasst einen physikalischen Zustand und liefert ein Signal (z. B. Näherungssensor).
- Aktor: Setzt ein Signal in eine physikalische Wirkung um (z. B. Motor, Magnetventil).
- Steuergerät: Verarbeitet Eingaben nach festgelegter Logik.
- Schnittstelle: Übergang zwischen Geräten/Signalbereichen; Signalart und Pegel müssen kompatibel sein.

## 3. Steuerung und Regelung

**Steuerung:** Ausgang wird durch die Eingangsgrößen und die Steuerlogik beeinflusst. Die tatsächliche Ausgangsgröße wird dabei **nicht notwendigerweise** rückgeführt und zur fortlaufenden Korrektur benutzt.

**Regelung:** Die zu regelnde Größe wird gemessen (**Istwert**), mit einem **Sollwert** verglichen und die Stellgröße bei einer Abweichung so verändert, dass die Regelgröße dem Sollwert folgt. Geschlossener Wirkungsablauf/Rückführung.

Beispiel Steuerung: Ein Motor läuft nach Start für eine festgelegte Zeit, ohne dass die tatsächlich zurückgelegte Strecke zurückgemeldet und korrigiert wird.

Beispiel Regelung: Raumtemperatur auf 22 °C halten: Sensor misst Temperatur, Regler vergleicht mit Sollwert und beeinflusst Heizung/Kühlung.

**Falle:** Eine Steuerung darf Sensoren haben! Entscheidend für die Abgrenzung ist, ob die **Regelgröße** zur Korrektur rückgeführt wird. Ein Endschalter einer Torsteuerung macht sie nicht automatisch zu einer Regelung.

## 4. Blockschaltbild und Wirkungskette

**Blockschaltbild Förderband:**
Start/Stopp, Sensoren → Logik/Steuerung → Schütz/Antrieb → Förderbandbewegung

Die **Wirkungskette** beschreibt in Worten die Reihenfolge:
1. Bediener betätigt Start.
2. Eingabesignal gelangt zur Signalverarbeitung.
3. Steuerung prüft die vorgesehenen Einschaltbedingungen.
4. Der Ausgang zur Schützspule wird angesteuert.
5. Das Schütz schaltet im Hauptstromkreis die Motorversorgung; Förderband läuft.

**Funktionsbeschreibung:** in klaren Wenn-/Dann-Sätzen. Beispiel:
> Wenn Start anliegt **und** die definierten Freigabebedingungen erfüllt sind, wird der Motor eingeschaltet.

Bei realen Maschinen müssen die notwendigen sicherheitsbezogenen Funktionen separat fachgerecht ausgelegt sein. Die stark vereinfachte Wirkungskette ersetzt keinen normgerechten Sicherheitsplan.

## 5. VPS und SPS im Überblick

**VPS:** Verbindungsprogrammierte Steuerung: Funktion entsteht durch Verdrahtung von Kontakten, Relais, Schützen und ggf. Zeitrelais.

**SPS:** Speicherprogrammierbare Steuerung: Funktion entsteht überwiegend durch ein im Steuergerät hinterlegtes Programm, Ein-/Ausgangsmodule und Parametrierung.

Beide können je nach Auslegung ähnliche Aufgaben erfüllen. Detailvergleich, Wahrheitstabellen und konkrete Schaltbilder folgen in späteren Lektionen.

## 6. Hefteintrag – zum Abschreiben

**Lernfeld 3: Steuerungen analysieren und anpassen**

**EVA-Prinzip:**
- **Eingabe:** Signale von Tastern, Schaltern oder Sensoren.
- **Verarbeitung:** Logik durch Relais-/Schützsteuerung oder SPS.
- **Ausgabe:** Ansteuerung von Aktoren wie Schütz, Motor oder Magnetventil.

**Sensor:** Erfasst Zustände und wandelt sie in Signale.  
**Aktor:** Setzt Steuersignale in eine physikalische Wirkung um.  
**Steuerung:** Eine festgelegte Logik beeinflusst den Prozess, ohne die Regelgröße fortlaufend zur Sollwertkorrektur rückzuführen.  
**Regelung:** Der Istwert der Regelgröße wird mit einem Sollwert verglichen; ein Regler verändert die Stellgröße bei einer Abweichung.

**Wirkungskette:** Eingabesignal → Verarbeitung/Entscheidung → Ansteuerung → Wirkung.

**VPS:** Funktion wird durch elektrische Verbindungen und Schaltgeräte festgelegt.  
**SPS:** Funktion ist überwiegend durch ein Steuerungsprogramm festgelegt.

**Merksatz:** Eine Sensor-Rückmeldung allein macht aus einer Steuerung noch keine Regelung. Entscheidend ist die Rückführung der geregelten Größe zum Soll-Ist-Vergleich.

## 7. Aufgaben (Lösungen erst nach eigener Bearbeitung!)

1. Ordne bei einer Förderbandanlage Starttaster, SPS und Motor den Stufen E, V und A zu.
2. Was bedeutet EVA?
3. Beschreibe den Unterschied zwischen Steuerung und Regelung.
4. Eine Heizung schaltet unabhängig vom aktuellen Raumtemperaturwert alle 10 Minuten für 2 Minuten ein. Steuerung oder Regelung?
5. Eine Heizung misst kontinuierlich die Raumtemperatur und beeinflusst die Heizleistung abhängig von Soll- und Isttemperatur. Steuerung oder Regelung?
6. Ist ein Lichttaster Sensor oder Aktor? Ist ein Magnetventil Sensor oder Aktor?
7. Warum ist ein Endschalter nicht automatisch ein Beweis für eine Regelung?
8. Wofür stehen VPS und SPS?
9. Beschreibe eine Wirkungskette für ein Tor, das bei Betätigung von „Öffnen“ bis zum vorgesehenen Endpunkt fährt.
10. Worin unterscheidet sich der Steuerstromkreis vom Hauptstromkreis einer Schützsteuerung?

**Nach diesen Grundlagen:** LF3 Lektion 2 – Sensoren und Aktoren mit echten Bildern und Anschlussbeispielen.
