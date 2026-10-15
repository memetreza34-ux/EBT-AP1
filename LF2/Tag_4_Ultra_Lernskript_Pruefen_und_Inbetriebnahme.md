# TAG 4 — PRÜFEN, MESSEN & IN BETRIEB NEHMEN

**Elektroniker für Betriebstechnik · Lernfeld 2 · AP1-Vorbereitung**  
**Lernskript mit Messprinzipien, Normwerten, Rechnungen, Fehlerbildern und Lösungen**  
**Stand: 15. Oktober 2026 · Ausgabe 1.0**

> **SICHERHEIT:** Dieses Heft ist Lernmaterial und keine Arbeitsfreigabe. Arbeiten an elektrischen Anlagen und Messungen unter Spannung dürfen nur durch entsprechend befugte Personen mit geeigneten Messgeräten, Schutzmaßnahmen und nach betrieblicher Anweisung durchgeführt werden. Ein Azubi arbeitet unter der erforderlichen Aufsicht. Nie Messungen an Spannung allein nach diesem Skript durchführen.

## So nutzt du dieses Skript

Dieses Dokument fasst die acht Lektionen von Tag 4 zusammen. Es erläutert nicht nur *was* bei einer Prüfung gemessen wird, sondern vor allem *woher Spannung und Strom kommen, welchen Weg der Messstrom nimmt, was das Gerät tatsächlich erfasst und wozu die Messung dient*. Diese vier Fragen waren beim Lernen besonders wichtig. Alle Zahlenbeispiele sind – soweit nicht ausdrücklich als Normwert gekennzeichnet – **Rechenbeispiele**, keine pauschalen Grenzwerte.

**Lernreihenfolge:** 1. Fünf Sicherheitsregeln → 2. Erstprüfung → 3. RLO → 4. RISO → 5. ZS → 6. FI/Polarität/Drehfeld → 7. Fehlersuche/Protokoll → 8. Prüfungstraining.

## 0 | Die wichtigste Übersicht: Welche Messung braucht welche Energie?

| Prüfung | Anlage beim üblichen Prüfverfahren | Woher kommt die elektrische Energie? | Was gibt das Gerät vor? | Was wird gemessen? | Was wollen wir wissen? |
|---|---|---|---|---|---|
| **RLO** Schutzleiter | spannungsfrei | Batterie/Quelle im Tester | Prüfstrom, normgemäß mind. 200 mA | Spannungsfall | PE durchgängig und ausreichend niederohmig? |
| **RISO** Isolation | spannungsfrei | Batterie/Hochspannungswandler im Tester | DC-Prüfspannung, oft 500 V | kleiner Leckstrom | Isolation ausreichend hochohmig? |
| **ZS** Fehlerschleife | bei direkter Prüfung unter Netzspannung | **Netz** | zusätzliche zeitweise Belastung, Prüfstrom geräteabhängig | Spannungs- und Stromänderung | Abschaltstrom im Fehlerfall groß genug? |
| **RCD/FI** | unter Netzspannung | **Netz** | definierter Prüffehlerstrom | Auslösestrom, Auslösezeit | Schaltet FI zuverlässig und rechtzeitig ab? |
| **Polarität** | je nach Verfahren | Prüfmittel bzw. Netz | passende Prüfart | Leiterzuordnung/Spannung | L, N, PE funktionell und sicher richtig? |
| **Drehfeld** | unter Netzspannung | Netz | keine zusätzliche hohe Last nötig | Reihenfolge der Phasenspannungen | Rechts- oder Linksdrehfeld? |

**Vokabeln:** *Prüfstrom* = bewusst vom Messgerät hervorgerufener Strom. *Fehlerstrom* = Strom infolge eines elektrischen Fehlers. *Leckstrom* = kleiner Strom durch eine nicht vollkommen isolierende Strecke. *Auslösestrom* = Strom, bei dem eine Schutzeinrichtung unter bestimmten Bedingungen abschalten soll oder abschaltet. Diese Wörter nicht verwechseln.

---

# LEKTION 1 | Die fünf Sicherheitsregeln

Vor Arbeiten an elektrischen Anlagen sind die fünf Sicherheitsregeln in ihrer festgelegten Reihenfolge zu beachten. Maßgeblich sind die jeweiligen Bedingungen der Anlage; nicht jede Regel wird in jeder Niederspannungssituation auf die gleiche Weise umgesetzt.

1. **Freischalten.** Alle relevanten Einspeisungen und Rückspeisemöglichkeiten wirksam trennen. Nur einen Lichtschalter auf AUS zu stellen reicht nicht.
2. **Gegen Wiedereinschalten sichern.** Verhindern, dass andere Personen oder Automatikfunktionen versehentlich wieder zuschalten. Kennzeichnen, verriegeln oder andere betriebsübliche Maßnahmen anwenden.
3. **Spannungsfreiheit feststellen.** Mit geeignetem Prüfmittel an der Arbeitsstelle nachweisen, dass tatsächlich keine Spannung mehr anliegt. Bei Niederspannung normalerweise mit einem geeigneten **zweipoligen Spannungsprüfer**. Prüfmittel auf Funktion prüfen.
4. **Erden und kurzschließen.** Soweit für die Anlage erforderlich; insbesondere im Hochspannungsbereich ein zentraler Schritt. Im Niederspannungsbereich hängt die Notwendigkeit von Anlage und Gefährdung ab.
5. **Benachbarte, unter Spannung stehende Teile abdecken oder abschranken.** Alle verbleibenden Gefahren durch erreichbare spannungsführende Teile sicher beherrschen.

### Warum reicht „Sicherung ausgeschaltet“ nicht?

Vielleicht hat jemand die falsche Sicherung betätigt. Vielleicht gibt es eine zweite Einspeisung, etwa PV, USV oder Generator. Vielleicht wurde versehentlich wieder eingeschaltet. Deshalb gehören **Sichern** und **Spannungsfreiheit feststellen** unbedingt dazu.

### Häufige Prüfungsfallen

- Ein **einpoliger Phasenprüfer** ist kein geeigneter alleiniger Nachweis der Spannungsfreiheit.
- Der **Schutzleiter PE** ist kein Ersatz für eine fachgerechte Freischaltung.
- Stromlos bedeutet nicht automatisch gefahrlos: Kondensatoren können noch geladen sein.
- Die fünf Regeln sind eine **Arbeitsreihenfolge**, keine Liste beliebiger Stichpunkte.

**AP1-Musterantwort:** „Freischalten, gegen Wiedereinschalten sichern, Spannungsfreiheit feststellen, erden und kurzschließen sowie benachbarte unter Spannung stehende Teile abdecken oder abschranken.“

---

# LEKTION 2 | Erstprüfung nach DIN VDE 0100-600

Eine neu errichtete oder wesentlich veränderte Niederspannungsanlage muss vor ihrer bestimmungsgemäßen Inbetriebnahme entsprechend den zutreffenden Anforderungen geprüft werden. Grundbausteine sind **Besichtigen, Erproben und Messen sowie Dokumentieren**.

## 2.1 Besichtigen

Noch ohne das eigentliche Messprogramm wird fachlich kontrolliert, ob alles richtig aufgebaut ist: Leitungsquerschnitt und Schutzorgan, Schutzleiter, Leitungsführung, Klemmen, Abdeckungen, Kennzeichnungen, Netzsystem, äußere Einflüsse, Zustand der Isolierungen, Dokumentation, Auswahl geeigneter Betriebsmittel. Beschädigte Isolationen oder unzulässige Verdrahtung müssen vor dem nächsten Schritt geklärt werden.

## 2.2 Erproben

Geprüft werden die vorgesehenen Funktionen und Schutz-/Verriegelungsfunktionen: Schalterstellungen, Steuerelemente, Motorfunktionen, gegebenenfalls Prüftaste und Anzeigeeinrichtungen. Die Funktion darf nur unter sicheren Bedingungen erprobt werden.

## 2.3 Messen

Die Messung liefert objektive Zahlen, zum Beispiel 0,25 Ω beim Schutzleiter, 150 MΩ beim Isolationswiderstand, 0,8 Ω bei ZS oder 24 ms beim FI. Nur mit passenden **Bewertungsbedingungen** wird aus einer Zahl ein Prüfentscheid. Nicht einfach „0,8 Ω ist immer gut“ schreiben!

## 2.4 Dokumentieren

Im Prüfbericht werden Stromkreise, Messwerte, Messbedingungen, Schutzorgane, verantwortliche Person, Datum und Mängel in angemessener Form dokumentiert. Das Protokoll zeigt, was **tatsächlich** geprüft wurde. Fehlt eine Messung, darf sie nicht nachträglich erfunden werden.

### Warum zuerst die Prüfungen im spannungsfreien Zustand?

Weil ein übersehener PE- oder Isolationsfehler gefährliche Folgen haben kann, sobald die Anlage eingeschaltet wird. Die genaue Reihenfolge ist situations- und geräteabhängig; ein sicherheitsgerechter Prüfplan wird von befugtem Fachpersonal festgelegt.

**Merke:** „Licht leuchtet“ beweist **nicht**, dass der PE angeschlossen ist oder dass der FI funktioniert.

---

# LEKTION 3 | RLO – Niederohmigkeit und Schutzleiterdurchgängigkeit

## 3.1 Was wird überprüft?

RLO ist die Prüfung des **niederohmigen Schutzleiterwegs**. Beispiel: vom Schutzleiteranschluss bzw. der PE-Schiene bis zum Schutzkontakt einer Steckdose oder zum metallischen Gehäuse eines Schutzklasse-I-Gerätes.

Der Schutzleiter soll im Fehlerfall einen zuverlässigen Rückweg bereitstellen. Eine lockere Klemme oder unterbrochene PE-Ader ist gefährlich, selbst wenn das angeschlossene Gerät normal läuft.

## 3.2 Woher kommt der Strom? Die Anlage ist doch ausgeschaltet!

**Aus dem Messgerät selbst.** Der Installationstester besitzt eine eigene Energiequelle, häufig eine Batterie mit elektronischer Stromregelung. Er benötigt für die RLO-Messung **keine vorhandenen 230 V Netzspannung**. Die Messstrecke wird sicher spannungsfrei hergestellt und bleibt es.

### Der Vorgang in der richtigen Reihenfolge

1. Fachkraft bereitet den spannungsfreien Prüfkreis vor und stellt die Spannungsfreiheit fest.
2. Das Messgerät liegt mit zwei Messleitungen an den Enden des zu überprüfenden PE-Wegs.
3. Der interne Stromkreis des Prüfgeräts erzeugt einen **definierten Prüfstrom**, z. B. 200 oder 300 mA, durch den PE-Weg.
4. Weil der Leiter einen kleinen Widerstand hat, entsteht **ein kleiner Spannungsabfall** an der Messstrecke.
5. Das Prüfgerät misst diesen Spannungsabfall und errechnet **R = U / I**.
6. Das Display zeigt den Widerstand in Ohm an.

**Rückweg:** Der Prüfstrom läuft vom ersten Geräteanschluss durch die gesamte geprüfte Leitung zurück zum zweiten Geräteanschluss. Der Prüfkreis ist damit über das **Messgerät** geschlossen. Er muss nicht durch das Versorgungsnetz zurückfließen.

<div class="flow"><div>Messgerät<br><strong>interne Quelle</strong></div><div class="arrow">→</div><div>erste Prüfleitung</div><div class="arrow">→</div><div>PE-Strecke<br><strong>RLO</strong></div><div class="arrow">→</div><div>zweite Prüfleitung</div><div class="arrow">→</div><div>Messgerät</div></div>

## 3.3 Wichtige Normwerte der RLO-Messung

Für geeignete Schutzleiter-/Potentialausgleichsmessgeräte nach **DIN EN IEC 61557-4 (VDE 0413-4)** gilt im dafür spezifizierten Bereich:

- **Leerlaufspannung:** ungefähr **4 V bis 24 V** (Wechsel- oder Gleichspannung je nach Gerät).
- **Messstrom:** mindestens **200 mA** im betreffenden normativen Messbereich.
- Ein Gerät darf z. B. **300 mA** verwenden; die 200 mA sind nicht der einzige mögliche Wert.

**Wichtig:** Die **Leerlaufspannung** ist die Ausgangsspannung, wenn noch **kein Messstrom** fließt – also bei offenen Anschlüssen. Sie ist **nicht automatisch die Spannung über dem Schutzleiter**, während 200 oder 300 mA fließen!

### Warum sind z. B. 10 V Leerlauf und 0,06 V am PE kein Widerspruch?

Das Gerät regelt Strom und Ausgangsspannung elektronisch. Bei einer niederohmigen Messstrecke reichen wenige Millivolt aus, um den gewünschten Strom aufrechtzuerhalten. Die offene Ausgangsspannung zeigt nur an, welche Spannung im unbelasteten Zustand anliegen kann. Bei einem guten PE liegt während der Messung typischerweise ein viel kleinerer Spannungsabfall an.

**Rechenbeispiel:** I = 300 mA = 0,3 A; R = 0,20 Ω. Gesucht: Spannungsfall.

**U = R · I = 0,20 Ω · 0,30 A = 0,060 V = 60 mV.**

Das Gerät misst ungefähr 60 mV und berechnet daraus 0,20 Ω. Die 0,06 V sind **Ergebnis**, nicht die vorher fest eingestellte Prüfspannung!

## 3.4 Warum kein gewöhnlicher Pieps-Durchgangstest?

Ein normaler Multimeter-Durchgangsprüfer kann bereits bei einem sehr kleinen Strom piepsen. Damit ist noch nicht nachgewiesen, dass der Schutzleiterweg unter einem normgerechten Prüfstrom ausreichend niederohmig ist. Kontaktfehler und Übergangswiderstände müssen fachgerecht beurteilt werden. Die RLO-Prüffunktion des Installationstesters ist dafür vorgesehen.

## 3.5 Warum Gleichstrom? Was passiert bei Wechselstrom?

**Gleichstrom (DC):** Nach dem Einschalten ist die Richtung des Stroms gleich. Bei einem einfachen ohmschen Leiter ist das gut interpretierbar. Bei AC ändert der Strom periodisch seine Richtung, im 50-Hz-Netz **50 vollständige Schwingungen je Sekunde**.

Ein realer Prüfkreis kann auch Spulen und Kapazitäten enthalten. Für eine Spule gilt **XL = 2πfL**, für einen Kondensator **XC = 1/(2πfC)**. Das sind Blindwiderstände. Wenn die **Frequenz fest 50 Hz** ist, sind XL und XC bei unverändertem L und C ebenfalls **fest**; sie wachsen oder schrumpfen **nicht während jeder Schwingung**. Was sich mit der Zeit ändert, sind Momentanwerte und Polaritäten von Spannung/Strom. Je nach Gerät und normgerechtem Verfahren ist RLO mit DC oder AC möglich.

## 3.6 Ist ein gemessener RLO-Wert von 0,25 Ω immer erlaubt?

Nein, nicht als **universeller Grenzwert**. Die Bewertung berücksichtigt insbesondere Leiterlänge, Querschnitt, Material, Verbindungsstellen und Anlagendaten. Ein langer Leiter hat einen größeren Widerstand als ein kurzer. Man kann den theoretischen Leiterwiderstand überschlagen:

**R = ρ · l / A** oder **R = l / (κ · A)**.

Beispiel mit Kupfer bei etwa 20 °C: ρ ≈ 0,0178 Ω·mm²/m, Länge = 20 m, Querschnitt = 1,5 mm²: **R ≈ 0,237 Ω** für diese 20 m Leiterlänge – zusätzliche Kontakte noch nicht berücksichtigt. Das Messgerät braucht die Leiterdaten **nicht**, weil es U und I direkt misst; die Fachkraft kann sie aber zur Plausibilitätsprüfung verwenden.

**Fehlerbild:** RLO zeigt **OL**: eventuell offener Messkreis, nicht angeschlossener PE, defekte Klemme oder Messbereich überschritten. **OL** nicht blind als „0 Ω“ lesen!

**Musterantwort:** „Bei der RLO-Messung prüfe ich an der spannungsfreien Anlage die niederohmige Durchgängigkeit des Schutzleiters. Das Messgerät erzeugt einen Prüfstrom von mindestens 200 mA, misst den Spannungsfall und berechnet mit R = U/I den Widerstand. So erkenne ich Unterbrechungen oder auffällige Übergangswiderstände.“

---

# LEKTION 4 | RISO – Isolationswiderstand

## 4.1 Was bedeutet „Isolation“?

Die stromführende Kupferader ist von isolierendem Material umgeben. Dieses soll verhindern, dass elektrischer Strom ungewollt von L nach PE, zwischen zwei aktiven Leitern oder zu leitfähigen Teilen fließt.

**RLO soll klein sein; RISO soll groß sein.** Das ist kein Widerspruch: Beim Schutzleiter wünschen wir eine leitende Verbindung, zwischen voneinander zu isolierenden Leitern wünschen wir gerade **keine** leitende Verbindung.

## 4.2 Woher kommen die 500 V? Die Anlage ist abgeschaltet!

Auch hier kommt die Energie **aus dem Prüfgerät selbst**. Ein eingebauter Spannungswandler erzeugt aus der Gerätebatterie die benötigte Gleichprüfspannung, beispielsweise **500 V DC**. Das sind **nicht** die abgeschalteten 230 V aus der Steckdose und auch kein „eingespeistes normales Netz“.

**Messgrundsatz:** Das RISO-Prüfgerät stellt eine **Spannung** bereit, nicht einen feststehenden Leckstrom. Der tatsächlich fließende Strom hängt vom Zustand der Isolation ab.

### Der Ablauf in der richtigen Reihenfolge

1. Anlage durch befugte Personen sicher freischalten; Spannungsfreiheit feststellen. Angeschlossene Elektronik, Überspannungsschutzeinrichtungen und Verbraucher entsprechend Norm/Herstellervorgaben berücksichtigen.
2. Tester wird an die fachlich festgelegten Messpunkte angeschlossen, beispielsweise L und PE.
3. Tester legt die vorgewählte **Gleichprüfspannung** an, beispielsweise 500 V DC.
4. Eine reale Isolation ist nicht immer ideal: sehr kleine **Leckströme** können zwischen den Messpunkten fließen.
5. Diese Ströme gelangen über die zweite Messleitung **zurück zum Prüfgerät** – der Messkreis ist geschlossen.
6. Das Gerät misst den Strom und die tatsächlich erreichte Prüfspannung, berechnet **RISO = U/I** und zeigt MΩ oder GΩ an.
7. Nach Ende der Prüfung müssen gespeicherte Ladungen sicher abgebaut sein. Bei vielen Geräten erfolgt eine automatische Entladung gemäß Anleitung.

<div class="flow"><div>RISO-Tester<br><strong>500 V DC</strong></div><div class="arrow">→</div><div>L</div><div class="arrow">→</div><div>Isolation<br><strong>winziger Leckstrom</strong></div><div class="arrow">→</div><div>PE</div><div class="arrow">→</div><div>RISO-Tester</div></div>

## 4.3 Rechenbeispiele mit Leckstrom

**Einheitenumrechnung:** 1 mA = 0,001 A. 0,1 mA = 0,0001 A. 1 MΩ = 1.000.000 Ω.

| Angelegte Prüfspannung | Leckstrom | Berechnung | Isolationswiderstand |
|---|---|---|---|
| 500 V | 0,5 mA | 500 / 0,0005 | **1 MΩ** |
| 500 V | 0,1 mA | 500 / 0,0001 | **5 MΩ** |
| 500 V | 0,05 mA | 500 / 0,00005 | **10 MΩ** |
| 500 V | 0,005 mA | 500 / 0,000005 | **100 MΩ** |

**Je weniger Leckstrom bei gleicher Prüfspannung fließt, desto größer der Isolationswiderstand.** Wenn ein Gerät „> 999 MΩ“ zeigt, bedeutet das meist nur, dass der Wert oberhalb des anzeigbaren Messbereichs liegt – nicht „mathematisch unendlich“.

## 4.4 Welche Prüfspannung, welcher Mindestwiderstand? DIN VDE 0100-600

| Nennspannung des Stromkreises | DC-Prüfspannung | Mindestisolationswiderstand |
|---|---:|---:|
| SELV / PELV | 250 V | **0,5 MΩ** |
| bis einschließlich 500 V, einschließlich FELV | 500 V | **1,0 MΩ** |
| über 500 V | 1.000 V | **1,0 MΩ** |

Diese Tabelle betrifft die **Erstprüfung von Niederspannungsanlagen** nach DIN VDE 0100-600. Für besondere Betriebsmittel, angeschlossene Überspannungsschutzeinrichtungen und empfindliche Elektronik sind normative Sonderregelungen und Herstellerangaben zu beachten. Eine zulässige Spannungsreduzierung in bestimmten Fällen ist **keine pauschale Erlaubnis**, stets mit 250 V zu messen.

## 4.5 Gibt es eine Norm für den Strom des RISO-Messgeräts?

**Ja: DIN EN IEC 61557-2 (VDE 0413-2).** Sie behandelt die Eigenschaften des Messgeräts. Aus der Ausgabe IEC 61557-2:2019 sind drei wichtige Gerätegrößen:

- **Nennstrom mindestens 1 mA**: Das Prüfgerät muss ihn unter den festgelegten Nennbedingungen bereitstellen können.
- **Messstrom höchstens 15 mA Scheitelwert**: Das ist ein **oberer Momentanwert**, kein Strom, der ständig fließen soll.
- Wechselstromanteil der Messspannung bzw. des Messstroms: Für den Strom gelten zusätzliche Anforderungen (bei genannter Ausgabe maximal 1,5 mA Scheitelwert des AC-Anteils).

**Prüfungsfalle:** „RISO misst immer mit 1 mA“ ist **falsch**. Beispiel: Bei 500 V und guter Isolation von 5 MΩ fließen nur 0,1 mA. **1 mA** bezeichnet die normativ geforderte Bereitstellungsfähigkeit unter spezifizierten Bedingungen, nicht den Strom, den jedes Prüfobjekt aufnehmen muss.

**Scheitelwert = größter Augenblickswert.** Wenn bei einem transienten Vorgang der Strom kurz 12 mA erreicht, später aber nur 0,1 mA fließt, ist 12 mA der Scheitelwert dieses Verlaufs. Die 15 mA aus der Gerätenorm sind eine obere Grenze für den Messstrom und keine garantierte normale Prüfstromstärke.

## 4.6 Warum wird mit Gleichspannung (DC) gemessen?

Zwei Leiter mit Isolierung dazwischen bilden auch eine kleine **Kapazität** – ähnlich einem Kondensator. Beim Anlegen der Gleichspannung fließt daher zusätzlich zunächst ein **Aufladestrom**. Wenn diese Kapazität geladen ist und die Spannung konstant bleibt, geht der reine kapazitive Ladestrom zurück bzw. gegen null. Der Kondensator ist dabei **weiter geladen**! Er entlädt sich nicht einfach schon deswegen, weil der Ladestrom verschwunden ist.

Daneben können Polarisations-/Absorptionsströme auftreten, die mit der Zeit abklingen. Deshalb wartet das Messgerät gegebenenfalls auf eine stabile Anzeige. Was dann übrig bleibt, hängt insbesondere von den realen Isolationseigenschaften ab.

Bei **Wechselspannung** werden Leitungskapazitäten fortlaufend umgeladen. Dadurch entsteht ein wiederkehrender kapazitiver Strom, der die Bewertung der eigentlichen Isolationsleckströme erschwert. Deshalb verwendet die RISO-Messung in diesem Kontext **DC**.

### Warum ist 50 Hz keine ständig steigende Frequenz?

Im Netz bleibt die Frequenz nominal **50 Hz**: Jede Sekunde erfolgen 50 volle Wechselspannungsperioden. Das Vorzeichen und der Betrag von Spannung und Strom wechseln ständig; die **Frequenz** selbst steigt dabei nicht jede halbe Periode an. Deswegen ändern sich bei konstantem f auch **XL = 2πfL** und **XC = 1/(2πfC)** nicht fortlaufend. Der normale ohmsche Widerstand R ist wiederum eine andere Größe als die kapazitiven/induktiven Blindwiderstände.

## 4.7 Typische Isolationsfehler

Beschädigter Mantel, eingeklemmte Ader, nasse Abzweigdose, verschmutzte Oberflächen, gealtertes Isoliermaterial, angeschlossene Verbraucher und fehlerhafte Verdrahtung. „Wert ist niedrig“ nennt noch **nicht automatisch die Ursache**. Erst Fehler eingrenzen, fachgerecht beheben und erneut prüfen.

**Musterantwort:** „Bei der Isolationsmessung wird die vorbereitete spannungsfreie Anlage mit einer Gleichprüfspannung, meist 500 V DC für einen üblichen 230/400-V-Stromkreis, beaufschlagt. Das Gerät liefert die Spannung selbst, misst den kleinen Leckstrom und berechnet RISO = U/I. Für solche Stromkreise beträgt der übliche Mindestwert der Erstprüfung 1 MΩ. Ein möglichst großer Wert ist erwünscht.“

---

# LEKTION 5 | ZS – Schleifenimpedanz und Fehlerstrom

## 5.1 Was ist eine Fehlerschleife?

Beispiel: Bei einem Gerät der Schutzklasse I berührt eine defekte Außenleiterader das metallische Gehäuse. Das ist ein **Körperschluss**. Im üblichen **TN-System** kann der Fehlerstrom über L, die Fehlerstelle, PE/PEN und die Stromquelle zurückfließen. Der Transformator und alle Leiter- und Kontaktwiderstände gehören zum gesamten Fehlerkreis. Dessen **Wechselstromimpedanz** heißt **ZS**.

**Wichtig zum Stromweg:** Der Fehlerstrom fließt im TN-System überwiegend über den metallischen Schutzleiterweg und die Quelle zurück, nicht einfach „in die Erde und verschwindet dort“. Strom fließt in einem geschlossenen Stromkreis.

<div class="flow"><div>Trafo<br><strong>230 V</strong></div><div class="arrow">→</div><div>L</div><div class="arrow">→</div><div>Fehler am<br><strong>Gehäuse</strong></div><div class="arrow">→</div><div>PE / PEN</div><div class="arrow">→</div><div>Trafo / Sternpunkt</div></div>

## 5.2 Warum ist eine kleine ZS günstig?

Bei vereinfachter Berechnung gilt **Ik ≈ U0 / ZS**. Bei gleicher Spannung bewirkt eine **kleine Impedanz einen großen möglichen Fehlerstrom**, eine **große Impedanz einen kleinen Fehlerstrom**.

- Bei zu großem ZS könnte der LS **nicht schnell genug** auslösen.
- Ein fehlerhaftes Gehäuse kann dann **zu lange eine gefährliche Berührungsspannung** führen.
- Der Sinn der ZS-Prüfung ist der Nachweis der **Abschaltbedingungen**, nicht einfach die Suche nach einer besonders niedrigen Zahl.

## 5.3 Woher kommt der Prüfstrom bei ZS?

Anders als RLO und RISO verwendet die **übliche direkte ZS-Messung das vorhandene Netz**. Ein Installationstester misst die Netzspannung, schaltet für kurze Zeit eine definierte zusätzliche **Belastung** zu und erfasst die dadurch entstehende **Stromänderung ΔI** und **Spannungsänderung ΔU**. Daraus bestimmt er näherungsweise **ZS ≈ ΔU/ΔI**. Die reale Gerätetechnik kann komplexer sein.

**Beispiel:** zusätzlicher Prüfstrom 5 A, Spannungsänderung 2 V. **ZS ≈ 2 V / 5 A = 0,40 Ω**. Die 5 A sind **nur ein Rechenbeispiel**, kein allgemeiner Norm-Prüfstrom.

### Gibt die DIN bei ZS einen einheitlichen Prüfstrom vor?

**Nein, nicht als universellen Stromwert.** **DIN EN IEC 61557-3 (VDE 0413-3)** regelt Anforderungen an geeignete Schleifenimpedanzmessgeräte und das Messen über den Spannungsfall bei Belastung. Wie hoch der Prüfstrom ist, hängt vom **Gerät, Messbereich und Messverfahren** ab.

Bei Geräten kommen z. B. Messbereiche mit mehreren Ampere und besondere **RCD-schonende Prüfungen** im Bereich weniger Milliampere vor. Beispiele wie 6 mA oder 15 mA sind **Gerätedaten**, nicht allgemeine DIN-Prüfstromvorgaben.

## 5.4 Warum kann bei ZS der FI auslösen?

Bei einer gewöhnlichen Messung zwischen **L und PE** fließt ein zusätzlicher Prüfstrom am Summenstromwandler des FI vorbei zurück zur Quelle, statt mit demselben Betrag über den überwachten Neutralleiter zurückzufließen. Der FI erkennt eine **Stromdifferenz** und kann auslösen.

Ein geeigneter **No-Trip-/RCD-schonender Messmodus** minimiert dieses Risiko, beispielsweise mit einem kleinen Strom. Aber auch unter 15 mA ist die Auslösung **nicht absolut ausgeschlossen**, weil bereits vorhandene Ableitströme und Gerätebesonderheiten relevant sind.

## 5.5 Den möglichen Fehlerstrom berechnen

**Formel:** Ik ≈ U0 / ZS. U0 ist im Beispiel 230 V, nicht die 400 V zwischen zwei Außenleitern.

**Beispiel A:** ZS = 2,0 Ω. **Ik = 230 / 2 = 115 A.**

**Beispiel B:** ZS = 4,0 Ω. **Ik = 230 / 4 = 57,5 A.**

**Vergleich:** Der Strom in Beispiel B ist kleiner, weil die Impedanz doppelt so hoch ist. Genau das war der wichtigste Gedanke bei der Übungsfrage.

## 5.6 B16, C16 und D16 – magnetische Schnellauslösung

| LS-Charakteristik | magnetischer Auslösebereich | obere Kennliniengrenze bei 16 A |
|---|---|---:|
| B | 3 bis 5 × In | **80 A** |
| C | 5 bis 10 × In | **160 A** |
| D | 10 bis 20 × In | **320 A** |

Die **untere Grenze** bedeutet nicht, dass bei diesem Strom die magnetische Schnellauslösung **sicher** stattfindet. Für einen vereinfachten sicheren Nachweis anhand der oberen Auslösegrenze rechnen wir bei B mit **5 × In**, bei C mit **10 × In** und bei D mit **20 × In**. Die tatsächlichen Abschaltbedingungen müssen anhand der zutreffenden Schutzeinrichtung und Norm geprüft werden.

**Beispiel mit B16 und ZS = 2 Ω:** Ik = 115 A. Benötigte obere magnetische Grenze = **5 × 16 A = 80 A**. **115 A > 80 A**: Im vereinfachten Modell ausreichend für magnetische Schnellauslösung.

**Beispiel mit B16 und ZS = 4 Ω:** Ik = 57,5 A. **57,5 A < 80 A**: schnelle magnetische Auslösung **nicht sicher nachgewiesen**. Das bedeutet **nicht**, dass der LS niemals abschaltet; er kann z. B. thermisch später auslösen.

## 5.7 Maximale ZS – theoretische Faustformel

**ZS,max = U0 / Ia**, wobei Ia der erforderliche Strom für die zulässige Abschaltzeit ist.

Für **B16 und 230 V** mit vereinfachter magnetischer Bedingung: **Ia = 80 A**.  
**ZS,max,ideal = 230 V / 80 A = 2,875 Ω**.

**Sehr wichtige Einschränkung:** 2,875 Ω ist ein **idealisierter rechnerischer Wert**, kein allgemeiner unmittelbarer Grenzwert für eine reale Erstprüfung. Netzspannung kann sinken, Leitungen erwärmen sich und Messfehler/Verfahrensvorgaben sind zu beachten. Deshalb verwendet die Fachpraxis geeignete Korrekturen, Bewertungsregeln und Herstellerdaten. Beispiel für eine **mögliche** Sicherheitsbetrachtung mit Faktor 1,5: 2,875 Ω / 1,5 ≈ 1,92 Ω. Dieser Faktor ist **nicht pauschal für alle Anlagen und Prüfverfahren verbindlich**.

## 5.8 Wie schnell muss im Fehlerfall abgeschaltet werden?

Bei 230/400-V-AC-Netzen gelten nach DIN VDE 0100-410 typischerweise:

| Netzsystem / Stromkreisart | maximal zulässige Abschaltzeit (typischer Fall) |
|---|---:|
| TN, einschlägiger Endstromkreis | **0,4 s** |
| TT, einschlägiger Endstromkreis | **0,2 s** |
| TN, bestimmter Verteilungsstromkreis | **5 s** |
| TT, bestimmter Verteilungsstromkreis | **1 s** |

**Präzision:** Die Zuordnung der Stromkreisarten richtet sich nach der Norm; zu den erfassten Endstromkreisen gehören u. a. bestimmte Steckdosenstromkreise bis 63 A und fest angeschlossene Verbraucher bis 32 A. Nicht alle Abzweige sind automatisch gleich zu bewerten.

## 5.9 TT statt TN: Warum ist der FI häufig entscheidend?

Im **TT-System** verläuft der Fehlerstromkreis über die **Erdungsanlagen und das Erdreich**. Der Erdungswiderstand kann vergleichsweise hoch sein und den Fehlerstrom so klein machen, dass eine reine Überstromschutzeinrichtung nicht rechtzeitig abschaltet. Deshalb wird der Fehlerschutz dort üblicherweise mit einer geeigneten **RCD** verwirklicht. Für den Nachweis können andere Größen, z. B. Erdungswiderstand **RA** und RCD-Daten, maßgeblich sein.

**Musterantwort:** „Mit der ZS-Messung prüfe ich den Wechselstromwiderstand der Fehlerschleife. Das Gerät belastet den unter Netzspannung stehenden Stromkreis kurzzeitig und bestimmt ZS aus Strom- und Spannungsänderung. Über Ik ≈ U0/ZS beurteile ich, ob bei einem Körperschluss genügend Strom für die rechtzeitige automatische Abschaltung zur Verfügung steht.“

---

# LEKTION 6 | RCD/FI-Prüfung, Polarität und Drehfeld

## 6.1 40 A / 30 mA – zwei vollkommen verschiedene Angaben

Steht auf einem FI beispielsweise **40 A / 30 mA**, bedeutet:

- **40 A = Bemessungsstrom In**: welcher Betriebsstrom vom Gerät im vorgesehenen Einsatz dauerhaft getragen werden kann. Das ist **nicht** sein Fehlerstrom-Auslösewert und macht ihn **nicht** zu einem Überlastschutz.
- **30 mA = Bemessungsdifferenzstrom IΔn**: Auf welche Fehlerstromgröße die RCD-Auslösefunktion ausgelegt ist. Der FI soll Fehlerströme erkennen und abschalten.

Ein FI (RCCB) ersetzt für sich allein **keinen Leitungsschutzschalter** für Überlast und Kurzschluss. Ein FI/LS (RCBO) kombiniert beide Funktionen.

## 6.2 Wie arbeitet der Summenstromwandler?

Im normalen einphasigen Betrieb gilt: Der Strom fließt über **L** hin und über **N** zurück. Im ringförmigen Summenstromwandler heben sich die magnetischen Wirkungen der beiden Ströme auf. Die Summe der überwachten Ströme ist im Idealfall **null**.

Beim Fehler, zum Beispiel L zum geerdeten Gehäuse, fließt ein Teilstrom **über PE zurück** und nicht durch den Summenstromwandler des FI. Die Summe ist dann **nicht null**. Ein resultierender magnetischer Fluss führt zur Induktion im Wandler und zur Betätigung des Auslösemechanismus.

**Wichtig:** Der FI „misst nicht einfach den Strom im PE“. Er vergleicht die Summe der **durch ihn geführten aktiven Leiter**. Bei einem dreiphasigen FI sind die Außenleiter und gegebenenfalls N mit erfasst, PE aber nicht.

## 6.3 Woher kommt der Strom bei der FI-Prüfung?

Bei der üblichen RCD-Prüfung an einer **unter Spannung stehenden** Anlage erzeugt das Prüfgerät mit der **vorhandenen Netzversorgung** einen festgelegten **Prüffehlerstrom**. Beim üblichen L-PE-Prüfweg fließt dieser an der Rückleitung über N durch den FI vorbei. Das erzeugt die beabsichtigte Stromdifferenz. Der FI schaltet ab.

Das Prüfgerät misst die **Zeit vom Beginn des Prüffehlerstroms bis zum Abschalten** in Millisekunden. In einer **Rampenprüfung** steigert es den Prüffehlerstrom, bis die RCD auslöst, und zeigt den **tatsächlichen Auslösestrom** an.

## 6.4 Wichtige RCD-Prüfwerte für unverzögerte 30-mA-FI

| Prüfung mit sinusförmigem Fehlerstrom | Prüffehlerstrom | Anforderung/typischer Grenzwert aus Gerätenormen |
|---|---:|---|
| 0,5 × IΔn | **15 mA** | darf unter normierten Bedingungen **nicht auslösen** |
| 1 × IΔn | **30 mA** | muss bis spätestens **300 ms** auslösen |
| 2 × IΔn | **60 mA** | muss bis spätestens **150 ms** auslösen |
| 5 × IΔn | **150 mA** | muss bis spätestens **40 ms** auslösen |

Das sind die hier behandelten **klassischen Produktnorm-Prüfwerte** eines gewöhnlichen unverzögerten RCD bei sinusförmigem Fehlerstrom, keine uneingeschränkt allgemeinen Installationsvorgaben für jede RCD-Art und jeden Messmodus. **Typ A** muss auch für pulsierende Gleichfehlerströme geprüft/geeignet sein; Typ, Prüfwellenform, Hersteller, Verzögerung und Normbezug beachten. Eine **selektive RCD (Typ S)** hat andere zulässige Auslösezeiten.

### Was bedeutet ein Rampen-Auslösestrom von 22 mA?

Beim betrachteten unverzögerten **30-mA-FI mit sinusförmigem Prüffehlerstrom** liegt 22 mA zwischen **15 mA (0,5 × IΔn)** und **30 mA (1 × IΔn)**. Das ist **grundsätzlich zulässig**. Die 30 mA bedeuten also **nicht**, dass das Gerät erst exakt ab 30,000 mA auslösen darf.

### Ist 55 ms bei 150 mA bestanden?

Für den betrachteten unverzögerten FI gilt bei **5 × IΔn (150 mA)** als Produktnorm-Prüfwert höchstens **40 ms**. **55 ms > 40 ms**: dieses **Prüfergebnis liegt über dem genannten Grenzwert**. Die Fachkraft bewertet die Messung unter Berücksichtigung des RCD-Typs, der Prüfeinstellung und des anwendbaren Prüfverfahrens.

## 6.5 Warum löst der FI bei einer normalen ZS-Messung eventuell aus?

Weil bei einer üblichen L-PE-Schleifenmessung ein Prüffehlerstrom entsteht, der über PE statt über N durch den FI zurückfließt. Die Summe der überwachten Ströme ist nicht null. Deshalb benutzt man, falls erforderlich und geeignet, ein **RCD-schonendes ZS-Verfahren**, nicht pauschal irgendeinen beliebigen Prüfstrom.

## 6.6 FI-Testtaste und Installationstester – Unterschied

Die **T-Taste** testet über eine eingebaute Prüfschaltung die grundsätzliche Auslösefunktion. Sie misst aber nicht automatisch alle erforderlichen Messwerte der elektrischen Anlage. Ein Installationstester kann **Zeit und Strom** unter dokumentierten Bedingungen erfassen. Die Prüfung nach Herstellervorgabe und die fachgerechte Erstprüfung bleiben wichtig.

## 6.7 Polaritätsprüfung

Die Leiter müssen **funktionell und normgerecht richtig zugeordnet** sein. In der üblichen Installation: Außenleiter **L**, Neutralleiter **N**, Schutzleiter **PE**. Häufige Kennfarben sind braun/schwarz/grau (L), blau (N) und grün-gelb (PE). Farben sind eine wichtige Orientierung, aber kein vollständiger elektrischer Nachweis.

**Typische Spannungswerte in einem fehlerfreien 230-V-TN-Stromkreis:**

| Messpunkte | ungefährer Spannungswert |
|---|---:|
| L – N | 230 V AC |
| L – PE | 230 V AC |
| N – PE | nahe 0 V, je nach Betriebszustand ggf. etwas mehr |

**Wichtig:** Diese Werte beweisen **allein noch keine** sichere PE-Durchgängigkeit. Diese ist gesondert nachzuweisen. Einpolige Schalter sollen den vorgesehenen **Außenleiter** unterbrechen, nicht irrtümlich nur N. Bei deutschen Schutzkontaktsteckdosen gibt es keine allgemein verbindliche „L immer links“-Zuordnung, da der Stecker gedreht werden kann.

## 6.8 Drehfeldprüfung

Im üblichen Drehstromnetz gibt es **L1, L2, L3**. Zwischen L und N liegen ungefähr **230 V**, zwischen zwei Außenleitern ungefähr **400 V**. Die drei sinusförmigen Spannungen haben nominal **50 Hz** und sind jeweils um **120° elektrisch** phasenverschoben.

Ein **Drehfeldmessgerät** erkennt die zeitliche Phasenfolge. Bei festgelegter Anschlusszuordnung wird als Rechtsdrehfeld beispielsweise die Folge **L1 → L2 → L3** bezeichnet. **Zwei Außenleiter vertauschen** kehrt die Drehfeldrichtung um. Das kann dazu führen, dass ein Drehstrommotor verkehrt herum dreht. Die tatsächliche mechanische Motordrehrichtung hängt zusätzlich von dessen Anschlussbelegung ab.

**AP1-Musterantwort:** „Bei der Drehfeldprüfung kontrolliere ich die Reihenfolge der drei Außenleiterspannungen mit einem geeigneten Drehfeldmessgerät. Die Phasenfolge entscheidet über die Drehrichtung des Drehfeldes; werden zwei Außenleiter getauscht, kehrt sie sich um.“

---

# LEKTION 7 | Systematische Fehlersuche, Inbetriebnahme und Protokoll

## 7.1 Sicherer Ablauf eines Installationsauftrags

**Auftrag verstehen → Plan prüfen → Sicherheitsmaßnahmen und Zuständigkeiten klären → spannungsfrei errichten → besichtigen → geeignete Schutzprüfungen im spannungsfreien Zustand → erforderliche Messungen/Erprobungen unter Spannung nur durch befugte Fachkräfte → Fehler beheben und nachprüfen → dokumentierte Freigabe → Übergabe.**

**Grundsatz:** Die erforderlichen Schutzmaßnahmen werden **vor** Freigabe beurteilt. Eine funktionierende Leuchte ist kein Ersatz für das Prüfprotokoll.

## 7.2 Fehlerbild A: „Steckdose funktioniert, PE-Messung zeigt OL“

- **Beobachtung:** L–N = 230 V; ein angeschlossenes Gerät arbeitet; RLO zwischen PE-Schiene und Schutzkontakt zeigt OL.
- **Warum das möglich ist:** Für den normalen Gerätebetrieb reichen oft L und N. Der PE ist im Normalzustand **kein Betriebsstromleiter**.
- **Gefahr:** Bei einem Körperschluss ist der sichere Rückweg nicht nachgewiesen. Das Metallgehäuse kann gefährlich unter Spannung stehen.
- **Entscheidung:** **Nicht freigeben.** Schutzleiterweg und Messaufbau fachgerecht prüfen lassen, Ursache beheben und erneut prüfen.

## 7.3 Fehlerbild B: „RISO zeigt 0,4 MΩ“

Bei einem üblichen Stromkreis mit 500-V-DC-Prüfung der Erstprüfung ist der Mindestwert **1 MΩ**. **0,4 MΩ < 1 MΩ**: Die Anforderung ist nicht erfüllt. Mögliche Ursachen: Feuchtigkeit, beschädigte Isolierung, eingeklemmte Ader, ungeeignete angeschlossene Elektronik. Fehlerstelle durch sichere, systematische Prüfung eingrenzen; nicht „einfach FI gegen größeren tauschen“.

## 7.4 Fehlerbild C: „ZS zu hoch“

Überhöhte Schleifenimpedanz bedeutet geringeren möglichen Fehlerstrom. Mögliche Ursachen: ungünstige Leitungsdaten, lose Klemmen, beschädigte PE-/PEN-Verbindungen. Die Bewertung ist von Netzsystem, Schutzgerät und Abschaltzeit abhängig. Ein **B16** und ein **C16** haben unterschiedliche Voraussetzungen für magnetische Schnellauslösung.

## 7.5 Fehlerbild D: „FI fällt immer wieder“

Mögliche Ursachen: fehlerhafte Isolierung, Feuchtigkeit, Ableitströme angeschlossener Geräte, unzulässige N-PE-Verbindungen hinter dem FI oder Verdrahtungsfehler. Vorgehen: Symptome dokumentieren, betroffene Stromkreise sicher bestimmen, nach fachlich festgelegtem Ablauf eingrenzen, anschließend erneut prüfen. **FI niemals überbrücken oder ohne Beurteilung durch einen unempfindlicheren ersetzen!**

## 7.6 Fehlerbild E: „Wechselschaltung geht nur bei manchen Stellungen“

Falsche Zuordnung des gemeinsamen Kontakts und der Korrespondierenden, lose Kontakte oder Planungsfehler kommen infrage. Gedanklich zuerst den Stromweg anhand des **Stromlaufplans** für jede Schalterstellung verfolgen. Anschließend unter fachlich sicheren Bedingungen und mit geeigneten Prüfmitteln systematisch kontrollieren.

## 7.7 Beispiel: Vereinfachtes Prüfprotokoll

**Objekt:** Ausbildungswerkstatt, Steckdosen-Endstromkreis · **Netz:** TN, 230 V · **LS:** B16 · **RCD:** 30 mA.

| Prüfbereich | Musterergebnis | Aussage |
|---|---|---|
| Besichtigung | ohne erkennbare Mängel | Sichtbefund dokumentiert |
| RLO | 0,25 Ω | PE-Weg anhand Anlagenangaben bewerten |
| RISO bei 500 V DC | 150 MΩ | über 1 MΩ |
| ZS | 0,80 Ω | Abschaltbedingungen passend bewerten |
| RCD mit 1 × IΔn | 24 ms | unter 300 ms beim betrachteten unverzögerten RCD |
| Polarität | zugeordnet | Leiterzuordnung geprüft |
| Funktionsprüfung | i. O. | Funktion kontrolliert |

**Dieses Muster ist absichtlich vereinfacht.** Ein tatsächlicher normgerechter Erstprüfbericht benötigt abhängig von der Anlage weitere Angaben, Stromkreiszuordnung, gegebenenfalls ergänzende Messungen und die endgültige Bewertung durch eine befugte Fachkraft.

**Dokumentationsfalle:** Niemals „i. O.“ schreiben, wenn die Messung nicht durchgeführt wurde. Messwert, Einheit, Prüfverfahren und Bewertung müssen zusammenpassen.

---

# LEKTION 8 | AP1-Trainingsprüfung: 30 Punkte

Dieses Training enthält eigene, prüfungsnahe Übungsaufgaben. Es sind **keine Original-IHK-Aufgaben**. Rechne ohne vorweg auf die Lösungsseite zu schauen. Für jede Aufgabe ist die erreichbare Punktzahl angegeben.

## Aufgabe 1: Fünf Sicherheitsregeln (5 P.)

Nenne die fünf Sicherheitsregeln in der richtigen Reihenfolge.

## Aufgabe 2: Erstprüfung (3 P.)

(a) Nenne die drei großen Bestandteile der Erstprüfung. (1 P.)  
(b) Nenne zwei Punkte, die beim Besichtigen kontrolliert werden. (1 P.)  
(c) Warum beweist eine funktionierende Lampe allein noch keine sichere Anlage? (1 P.)

## Aufgabe 3: RLO (3 P.)

(a) Woher stammt der Prüfstrom, obwohl die Anlage spannungsfrei ist? (1 P.)  
(b) Wie hoch ist der normativ relevante Mindestprüfstrom des RLO-Messgeräts? (1 P.)  
(c) Ein Tester verwendet 300 mA. An 0,20 Ω fallen wie viel Volt ab? (1 P.)

## Aufgabe 4: RISO (4 P.)

(a) Was gibt das Prüfgerät vor – konstanten Prüfstrom oder Prüfspannung? (1 P.)  
(b) Welche DC-Prüfspannung und welchen Mindestisolationswiderstand verwendet man üblicherweise bei der Erstprüfung eines 230/400-V-Stromkreises? (1 P.)  
(c) 500 V Prüfgleichspannung, gemessener Leckstrom 0,1 mA: Berechne RISO. (1 P.)  
(d) Warum wird DC und nicht dauerhaft AC für diese Isolationsmessung verwendet? (1 P.)

## Aufgabe 5: ZS und B16 (5 P.)

Ein Steckdosenstromkreis hat U0 = 230 V, ZS = 2,0 Ω und einen B16.  
(a) Wozu wird ZS gemessen? (1 P.)  
(b) Berechne Ik. (1 P.)  
(c) Nenne die obere magnetische Auslösegrenze des B16. (1 P.)  
(d) Ist nach unserem vereinfachten Modell die magnetische Schnellauslösung nachgewiesen? (1 P.)  
(e) Woher stammt bei der üblichen direkten ZS-Messung die elektrische Energie für die Prüfbelastung? (1 P.)

## Aufgabe 6: FI (4 P.)

Ein unverzögerter 30-mA-RCD wird mit geeignetem sinusförmigem Fehlerstrom geprüft.  
(a) Was erzeugt das Prüfgerät? (1 P.)  
(b) Welche maximale Auslösezeit wird bei 1 × IΔn nach den hier behandelten Geräte-Prüfwerten erwartet? (1 P.)  
(c) Welche maximale Auslösezeit bei 5 × IΔn? (1 P.)  
(d) Erkläre, warum ein FI mit 22 mA Rampenauslösestrom grundsätzlich in Ordnung sein kann. (1 P.)

## Aufgabe 7: Polarität und Drehfeld (3 P.)

(a) Nenne die typischen Spannungen L–N und L–PE im fehlerfreien 230-V-TN-Stromkreis. (1 P.)  
(b) Warum reicht die Spannungsmessung L–PE allein nicht als PE-Durchgängigkeitsprüfung? (1 P.)  
(c) Was passiert mit der Drehfeldrichtung, wenn zwei Außenleiter vertauscht werden? (1 P.)

## Aufgabe 8: Fehlersuche/Protokoll (3 P.)

(a) Eine Steckdose funktioniert, aber RLO zeigt „OL“ zwischen PE-Schiene und Schutzkontakt. Welche Gefahr besteht? (1 P.)  
(b) Darf die Steckdose ohne Klärung freigegeben werden? (1 P.)  
(c) Nenne zwei Angaben, die in ein Prüfprotokoll gehören. (1 P.)

---

# MUSTERLÖSUNGEN | AP1-Trainingsprüfung

**1 (5 P.):** 1. Freischalten. 2. Gegen Wiedereinschalten sichern. 3. Spannungsfreiheit feststellen. 4. Erden und kurzschließen. 5. Benachbarte unter Spannung stehende Teile abdecken oder abschranken.

**2 (3 P.):** (a) Besichtigen, Erproben und Messen; Dokumentation als abschließender Nachweis. (b) Z. B. Klemmen und Isolierungen; auch Leiterkennzeichnung/Schutzorgane. (c) Eine Leuchte kann auch ohne intakten Schutzleiter funktionieren – Sicherheit ist nicht automatisch nachgewiesen.

**3 (3 P.):** (a) Aus der Batterie/internen Quelle des Testers. (b) Mindestens 200 mA in spezifiziertem Messbereich nach IEC 61557-4. (c) U = R · I = 0,20 Ω · 0,30 A = **0,060 V**.

**4 (4 P.):** (a) Prüfspannung (DC), nicht stets denselben Leckstrom. (b) **500 V DC**, **mindestens 1 MΩ** unter den üblichen Bedingungen. (c) R = 500 V / 0,0001 A = 5.000.000 Ω = **5 MΩ**. (d) Nach dem kapazitiven Aufladen verschwindet der reine DC-Ladestrom weitgehend; bei AC würden Leitungskapazitäten ständig umgeladen und der kapazitive Anteil den Messstrom beeinflussen.

**5 (5 P.):** (a) Abschaltbedingungen im Körperschlussfall prüfen. (b) **Ik ≈ 230 / 2 = 115 A**. (c) **5 × 16 A = 80 A**. (d) Ja, im vereinfachten Modell: 115 A > 80 A. (e) Aus dem **vorhandenen Netz**, das durch den Tester kurz belastet wird.

**6 (4 P.):** (a) Definierten Prüffehlerstrom, der im FI eine Stromdifferenz erzeugt. (b) **300 ms**. (c) **40 ms** bei 150 mA. (d) Der Auslösestrom liegt zwischen 0,5 × 30 mA = 15 mA und 1 × 30 mA = 30 mA.

**7 (3 P.):** (a) L–N ≈ 230 V und L–PE ≈ 230 V. (b) Eine Spannungsanzeige ersetzt nicht den niederohmigen Kontinuitätsnachweis des PE. (c) Die Drehfeldrichtung kehrt sich um.

**8 (3 P.):** (a) Der PE-Weg ist möglicherweise unterbrochen; bei Körperschluss kann eine gefährliche Berührungsspannung bestehen bleiben. (b) **Nein.** Fehler klären und erneut fachgerecht prüfen. (c) Z. B. Stromkreis-ID, Datum, Prüfgerät, Schutzorgan, Messwert und Einheit, Mangel/Bewertung, prüfende Person.

## Eigene Punkteauswertung

| Thema | Max. Punkte | Erreichte Punkte |
|---|---:|---|
| Fünf Regeln | 5 | ______ |
| Erstprüfung | 3 | ______ |
| RLO | 3 | ______ |
| RISO | 4 | ______ |
| ZS | 5 | ______ |
| FI | 4 | ______ |
| Polarität / Drehfeld | 3 | ______ |
| Fehlersuche / Protokoll | 3 | ______ |
| **GESAMT** | **30** | **______** |

**Hinweis zum Lernstand:** Die 30-Punkte-Prüfung wurde im Chat **nicht tatsächlich vollständig bearbeitet**. Es gibt deshalb hier **keine erfundene Note**. Die Antworten und Übungen dienen deinem Selbsttest.

---

# ZUSATZWISSEN | Die Verständnisfragen aus unserem Lerntag

## Frage 1: Kann beim RLO-Messen Strom fließen, obwohl die Anlage spannungsfrei ist?

**Ja.** Die Anlage ist von der Versorgung getrennt; die **Batterie des Prüfgeräts** erzeugt einen eigenen **kleinen, kontrollierten Messstrom** durch den geprüften Leiter. Der Rückweg geht zurück zum Gerät.

## Frage 2: Wenn am Tester 10 V Leerlaufspannung stehen, müssten dann nicht 10 V über dem PE anliegen?

**Nein.** Leerlauf heißt **ohne Stromfluss**. Bei niederohmigem PE regelt der Tester auf seinen Prüfstrom und es fallen beispielsweise nur **0,06 V** an der Messstrecke ab. Die offene Ausgangsspannung ist kein Dauerwert über dem angeschlossenen Prüfling.

## Frage 3: Warum ist RISO gerade andersherum als RLO?

RLO: möglichst **kleiner** Widerstand, damit der Schutzleiter ein leitender Fehlerstromweg ist. RISO: möglichst **großer** Widerstand, damit zwischen L und PE **kein nennenswerter unerwünschter Strom** fließt.

## Frage 4: Woher kommt bei RISO der Leckstrom?

Er wird **vom RISO-Prüfgerät geliefert**. Das Gerät legt z. B. 500 V an. Die Isolation lässt je nach Zustand einen **kleinen Teilstrom** durch. Der Strom fließt über die zweite Messleitung zum Gerät zurück. **Es ist keine Netzspannung nötig.**

## Frage 5: Wie viel Strom legt das RISO-Messgerät fest – 1 mA?

Es legt primär die **Prüfspannung** fest. Die **1 mA** sind eine normative Anforderung an den **Nennstrom des Geräts**, nicht der dauerhaft tatsächliche Leckstrom. Bei 500 V und 5 MΩ fließen nur 0,1 mA.

## Frage 6: Bedeutet „15 mA Scheitelwert“ dauerhaft 15 mA?

**Nein.** Scheitelwert bedeutet größter **Augenblickswert** eines Strom- oder Spannungsverlaufs. Die IEC-61557-2-Grenze ist ein maximal zulässiger Messstromspitzenwert, nicht der Sollstrom einer guten Isolation.

## Frage 7: Warum fließt beim Anlegen von DC kurz mehr Strom über die Leitungskapazität?

Weil zwei voneinander isolierte Leiter einen **Kondensator** bilden. Dieser muss sich zunächst aufladen. Bei konstant bleibender Gleichspannung nimmt der Ladestrom danach ab. Die Ladung bleibt zunächst gespeichert und muss **nach Prüfende kontrolliert entladen** werden.

## Frage 8: Ändern sich XL und XC dauernd, weil AC ja hin und her schwingt?

**Nein, nicht bei fester Frequenz und konstanten L/C.** Der **Stromaugenblickswert** ändert sich periodisch, die Frequenz ist aber weiterhin nominal 50 Hz. Deshalb haben XL und XC bei dieser Frequenz definierte Werte.

## Frage 9: Wenn ZS zu groß wird, kann weniger Strom über PE zurückfließen?

**Ja, im TN-Körperschlussfall.** ZS größer → möglicher Fehlerstrom kleiner → automatische Abschaltung mit dem LS ist unter Umständen **nicht schnell genug**. Der Fehlerstromkreis und das Netzsystem müssen dabei richtig betrachtet werden.

## Frage 10: Rechnet man bei B16 mit 3 × 16 A oder 5 × 16 A?

Der magnetische Bereich reicht **von 3 × bis 5 × In**. Für den vereinfachten **sicheren** Nachweis der magnetischen Schnellauslösung wird die **obere** Kennliniengrenze **5 × 16 A = 80 A** benutzt. 3 × 16 A = 48 A beschreibt die untere Grenze, nicht die garantierte Schnellauslösung.

## Frage 11: Warum fließt der ZS-Prüfstrom bei L–PE nicht über N zurück?

Er wird über den **PE-Weg** zur Quelle zurückgeführt. Deshalb kann im FI eine **Stromdifferenz** entstehen. Bei solchen Stromkreisen braucht man ein passendes RCD-schonendes ZS-Prüfverfahren, wenn ein versehentliches Auslösen vermieden werden soll.

## Frage 12: Was erkennt der FI wirklich – Magnetfeld oder Stromdifferenz?

Das Wesentliche ist die **Stromdifferenz** zwischen den überwachten aktiven Leitern. Diese Differenz erzeugt den resultierenden **magnetischen Fluss im Summenstromwandler**, und der Mechanismus führt zur Auslösung. Das Wort „Magnetfeld“ allein beschreibt noch nicht, **warum** die Schutzfunktion anspricht.

## Frage 13: Misst der FI-Tester nach der Auslösung die Spannung oder den Strom?

Je nach Prüfmodus ermittelt er insbesondere die **Auslösezeit** in Millisekunden und bei der **Rampenprüfung den Auslösestrom**. Er kennt den selbst erzeugten Prüffehlerstrom und erkennt den Zeitpunkt der Abschaltung.

## Frage 14: Warum ist eine noch funktionierende Steckdose mit unterbrochenem PE gefährlich?

Weil L und N den normalen Betriebsstromkreis schließen können. Der PE ist aber für den **Fehlerfall** vorgesehen. Ein funktionsfähiges Gerät beweist deshalb nicht, dass der Schutzleiter intakt ist.

---

# SPICKZETTEL | Werte, Formeln und typische Fallen

| Thema | Für die AP1 merken | Achtung |
|---|---|---|
| RLO | R = U/I; ≥ 200 mA normativer Messstrom | Leerlaufspannung ≠ Spannungsfall bei Messstrom |
| RLO-Gerät | 4–24 V Leerlaufspannung im spezifizierten normgerechten Verfahren | Gerät kann AC/DC, Strom z. B. 300 mA |
| RISO | RISO = U/IL; 500 V DC und ≥ 1 MΩ bei üblichem 230/400-V-Stromkreis | nicht 1 mA „immer“; kleine Leckströme |
| RISO-Gerät | Nennstrom mindestens 1 mA; Messstrom maximal 15 mA Spitze | Norm des Geräts ≠ Norm der Anlage |
| ZS | Ik ≈ U0/ZS; ZS ≈ ΔU/ΔI | Norm legt keinen universellen Prüfstrom für ZS fest |
| B16 | magnetisch 3–5 × 16 A; sicherer Oberwert 80 A | 48 A ≠ sicherer magnetischer Grenzstrom |
| C16 | magnetisch 5–10 × 16 A; Oberwert 160 A | andere Kennlinie als B16 |
| FI 30 mA | 15 mA nicht auslösen; 30 mA ≤300 ms; 150 mA ≤40 ms | für hier behandelten unverzögerten FI/AC-Fehlerstrom |
| TN 230 V | relevante Endstromkreise typ. 0,4 s | Anwendung je Stromkreisart prüfen |
| TT 230 V | relevante Endstromkreise typ. 0,2 s | häufig RCD erforderlich |
| 3~ | 230 V L–N; 400 V L–L; 50 Hz; 120° | 2 Außenleiter tauschen = Drehfeldumkehr |
| Dokumentation | echter Messwert + Einheit + Zuordnung + Bewertung | fehlende Messungen nicht erfinden |

## Für welche Größe steht welches Formelzeichen?

| Symbol | Bedeutung | Einheit |
|---|---|---|
| U, U0 | (Netz-)Spannung | V |
| I, Ik | Strom, angenäherter Fehler-/Kurzschlussstrom | A |
| In | Bemessungsstrom eines Schutzgeräts | A |
| IΔn | Bemessungsdifferenzstrom eines RCD | mA oder A |
| Ia | zur Abschaltung erforderlicher Strom | A |
| RLO, RISO | Durchgangs- bzw. Isolationswiderstand | Ω, MΩ |
| ZS | Schleifenimpedanz | Ω |
| ΔU, ΔI | Änderung der Spannung bzw. des Stroms | V, A |
| XL, XC | induktiver / kapazitiver Blindwiderstand | Ω |
| f | Frequenz | Hz |
| L, C | Induktivität, Kapazität | H, F |
| ρ, κ | spezifischer Widerstand, Leitfähigkeit | Ω·mm²/m, m/(Ω·mm²) |

**Schnelles Kopfrechnen:** 1 Ω bei 230 V → 230 A; 2 Ω → 115 A; 4 Ω → 57,5 A. 500 V / 1 MΩ → 0,5 mA; 500 V / 5 MΩ → 0,1 mA. 300 mA · 0,2 Ω → 0,06 V.

---

# QUELLEN, NORMEN UND GRENZEN

Die nachstehenden Quellen sind zur fachlichen Einordnung geeignet. Normen selbst können kostenpflichtig sein; verbindlich sind jeweils die **für Anlage, Zeitpunkt und Prüfaufgabe anwendbare Normausgabe**, die Herstellerangaben und betriebliche Anweisungen. Die genannten Zahlen sind keine Erlaubnis, Netzspannungsprüfungen allein durchzuführen.

1. **DIN VDE 0100-600** – Erstprüfung von Niederspannungsanlagen. Für die Isolationsprüfspannungen und Grenzwerte siehe u. a. WEKA: https://www.weka.de/elektrosicherheit/erstpruefung-nach-din-vde-0100-600/
2. **IEC 60364-6** – Verification / Tabelle der Isolationsprüfung und Hinweise zu Überspannungsschutz: https://www.iteh.us/catalog/standards/iec/a24425bb-9f3d-43e0-8a53-21f5f4bf18c0/iec-60364-6-2016
3. **DIN EN IEC 61557-2 / IEC 61557-2:2019** – Isolationswiderstandsmessgeräte; DC, Nennstrom ≥ 1 mA, Messstrom ≤ 15 mA Spitzenwert: https://www.iteh.eu/catalog/standards/iec/686dae8e-7391-4e80-b4cf-5e415e8e0ef7/iec-61557-2-2019
4. **DIN EN IEC 61557-3 / IEC 61557-3:2019** – Schleifenimpedanzmessgeräte: https://webstore.iec.ch/en/publication/60893
5. **DIN EN IEC 61557-4 / IEC 61557-4:2019** – Widerstand von Schutzleitern/Potentialausgleichsleitern; Überblick: https://www.vde-verlag.de/p/normen/iec-61557-4-2019/247859-BI-PDF
6. **DIN VDE 0100-410** – Schutz gegen elektrischen Schlag, Abschaltbedingungen; Erläuterung der DKE: https://www.dke.de/de/arbeitsfelder/core-safety/normenhinweise/konzept-0100-410
7. **DIN EN 61008 / 61009** – Produktanforderungen an FI/RCD bzw. FI/LS. Produktdaten und Zeitprüfwerte eines Herstellers: https://www.se.com/pl/pl/faqs/FA246981/
8. **DIN EN IEC 61557-6** – Anforderungen an RCD-Prüfgeräte; **DIN EN IEC 61557-7** – Anforderungen an Drehfeldmessgeräte.
9. **DGUV und betriebliche Arbeitsschutzbestimmungen** – fünf Sicherheitsregeln und Arbeiten an elektrischen Anlagen: https://aug.dguv.de/arbeitssicherheit/stromunfaelle-vermeiden/
10. **Benning, Sonel, Gossen Metrawatt und andere Gerätehersteller** – Bedienungsanleitungen für konkrete Messbereiche, Prüfströme und Verfahren; ein Gerätebeispiel ist kein allgemeiner Normwert.

**Erstellt als Lernskript zu Tag 4.** Die Inhalte der Gespräche sind in einem zusammenhängenden Heft aufbereitet, fachlich präzisiert und um passende Übungen ergänzt. Die vollständige 30-Punkte-Simulation wurde im Unterrichtsgespräch nicht zu Ende geschrieben; sie ist in diesem Heft als **neue selbstständige Übung** mit Lösungen enthalten.