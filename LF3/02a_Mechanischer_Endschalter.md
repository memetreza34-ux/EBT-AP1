# LF3 – Lektion 2A: Mechanischer Endschalter / Positionsschalter

**Status:** Lernmaterial vorbereitet; Prüfung im Chat offen.
**Ziel:** Funktion, mechanischen Aufbau, Schließer/Öffner, Anschlussnummern und Anwendungsfälle ohne Auswendiglernen nachvollziehen.

## 1. Warum braucht man einen Endschalter?
Ein Endschalter meldet das Erreichen einer Position bzw. Endlage. Beispiel: Ein Rolltor fährt hoch und betätigt am oberen Anschlag einen Rollenhebel-Endschalter. Die Steuerung erhält ein geändertes Signal und stoppt die Aufwärtsbewegung über ihr vorgesehenes Schalt-/Antriebssystem. Der Endschalter misst keine Entfernung in Zentimetern; er meldet vor allem das Erreichen einer Betätigungsposition.

## 2. Mechanischer Aufbau
1. **Betätiger:** Rollenhebel, Rollenstößel oder Druckstößel. Die bewegte Maschine drückt auf dieses mechanische Teil.
2. **Betätigungsmechanik:** Überträgt die Kraft/Bewegung in das Schaltgerät.
3. **Schaltkontakte:** Öffner (NC) und/oder Schließer (NO) ändern ihren Zustand. Viele Typen haben eine Sprungschaltung, andere eine Schleichschaltung.
4. **Rückstellfeder:** Bringt den Mechanismus nach dem Loslassen wieder in die Ausgangsstellung, sofern die konkrete Bauform selbsttätig rückstellend ist.
5. **Gehäuse und Anschlussklemmen:** Schützen Mechanik/Kontakte und erlauben Anschluss nach Herstellerplan.

Der Schalter benötigt zum mechanischen Erkennen einer Position nicht selbst zwingend Versorgungselektronik; Kontakte können über einen passenden Steuerstromkreis ausgewertet werden.

## 3. Ablauf Schritt für Schritt
**Unbetätigt:** Rollenhebel in Ruhelage. Bei Schließer: Kontakt offen. Bei Öffner: Kontakt geschlossen.

**Betätigung:** Schaltfahne oder Maschinenteil drückt Rollenhebel, der Stößel überträgt Bewegung auf den Kontaktmechanismus. Bei einem Gerät mit einem NO und einem NC schließen die NO-Kontakte und öffnen die NC-Kontakte beim entsprechenden Betätigungspunkt.

**Rückkehr:** Wenn die Maschine den Rollenhebel wieder freigibt, stellt bei einem selbsttätig rückstellenden Schalter die Feder die ursprüngliche Stellung her.

**Wichtig:** Schaltpunkt, Rückschaltpunkt, Betätigungsweg und erforderliche Betätigungskraft sind bauartabhängig; diese Daten dem Datenblatt entnehmen.

## 4. Schließer und Öffner erkennen
| Kontakt | Unbetätigt | Betätigt | Typische Klemmenbezeichnungen |
|---|---|---|---|
| Schließer (NO) | offen | geschlossen | 13–14 |
| Öffner (NC) | geschlossen | offen | 21–22 |

Die Zahlen gelten für die entsprechend gekennzeichneten Kontakte vieler industrieller Schaltgeräte. Nur tatsächlich vorhandene Klemmen entsprechend Aufdruck/Datenblatt verwenden; nicht jede Gerätebauart trägt diese Nummern.

**Beispiel Stoppen am Tor:** Öffner wird betätigt und öffnet, der für „Tor AUF“ vorgesehene Steuerkreis bzw. Eingang erhält das entsprechende Signal. Die Steuerung sorgt dafür, dass der Aufwärtsantrieb stoppt. Nicht automatisch gleichbedeutend mit einem normgerechten Sicherheits-Endschalter.

## 5. Haupttypen
- **Rollenhebel:** Dreh- oder Schwenkbewegung des Hebels; Rolle verringert Reibung an vorbeifahrenden Teilen.
- **Rollenstößel:** geradlinige Betätigung mit Rolle.
- **Druckstößel:** geradlinige Betätigung ohne Rolle.

## 6. Einsatzgebiete
- Tor/Hubanlage: Endlage oben/unten melden.
- Förderband: Position einer Mechanik oder eines Werkstückträgers melden.
- Maschinenachse: Endbereich bzw. Referenzposition erkennen.
- Verpackungsmaschine: Position eines bewegten Mechanikteils erfassen.

## 7. Typische Fehler und Grenzen
- Betätiger nicht erreicht: falsche Position/Justage.
- Hebel/Rolle beschädigt, blockiert oder abgebrochen.
- Kabel/Steckverbindung, Klemme oder Kontakt defekt.
- NO und NC verwechselt, weil die Ruhestellung nicht verstanden wurde.
- Rückschaltverhalten durch Verschleiß/Schmutz beeinträchtigt.

Bei der Fehlersuche auf freigegebene, sichere Prüfbedingungen achten. An laufenden Maschinen nicht in bewegliche Bereiche greifen; Schaltkreise nur entsprechend der Qualifikation prüfen.

## 8. Sicherheit
Ein normaler Positions-Endschalter ist **nicht automatisch eine geeignete Schutzeinrichtung**. Für sicherheitsbezogene Aufgaben werden die dazu erforderlichen Geräte und die gesamte Sicherheitsfunktion ausgelegt und bewertet. Zwangsöffnende NC-Kontakte können nach EN/IEC 60947-5-1 eine wichtige Eigenschaft sein; sie allein gewährleisten nicht die Sicherheit der Gesamtanlage.

## Hefteintrag
**Mechanischer Endschalter:** Melder für eine mechanisch erreichte Stellung/Endlage. Ein bewegtes Anlagenteil betätigt Rollenhebel oder Stößel. Dadurch wechseln die Kontakte ihren Zustand; beim Loslassen stellt die Feder den Mechanismus bei selbsttätig rückstellender Ausführung wieder zurück.

- **NO = Schließer:** unbetätigt offen, betätigt geschlossen (oft 13–14).
- **NC = Öffner:** unbetätigt geschlossen, betätigt offen (oft 21–22).
- **Aufbau:** Betätiger → Mechanik → Kontakte → Anschlussklemmen, oft mit Rückstellfeder und Gehäuse.
- **Beispiel:** Tor erreicht obere Endlage → Schalter betätigt → Steuerung stoppt Aufwärtsantrieb.
- **Fehler:** falsche Justage, beschädigte Rolle, klemmender Mechanismus, Kabel-/Kontaktfehler, falscher NO/NC-Anschluss.
- **Wichtig:** Positionsendschalter ist nicht automatisch sicherheitsgerichtet.

## Lernfragen
1. Was löst beim Endschalter das elektrische Schalten aus?
2. Nenne mindestens drei wesentliche Bauteile des Endschalters.
3. Welche Zustände haben NO und NC vor und nach der Betätigung?
4. Was bedeuten 13–14 und 21–22 typischerweise?
5. Warum stoppt ein Tor nicht zwangsläufig direkt durch den Schalter selbst?
6. Ist eine elektrisch überwachte Schutztür mit einem beliebigen Endschalter automatisch normgerecht sicher?
7. Ein Tor fährt am oberen Endschalter vorbei. Nenne zwei plausible Fehlerursachen.
8. Wann könnte statt eines mechanischen Endschalters ein berührungsloser Sensor geeigneter sein?

## Herstellerquellen
- Siemens SIRIUS mechanische Positionsschalter, IC10 2025: https://support.industry.siemens.com/cs/attachments/109772004/SIRIUS_IC10_chap12_German_2025_202409251714416287.pdf
- Siemens SIRIUS Betriebsanleitung: https://cache.industry.siemens.com/dl/files/659/25246659/att_101838/v1/3348651_10_000_RS_AB_008_201212141230027299.pdf
- Schneider Electric zu positiver Betätigung: https://www.se.com/ie/en/faqs/FA24894/
