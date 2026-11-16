# Auswertung eines ausgefüllten DB-Inbetriebnahmeprotokolls (Foto, Blatt 2/2)

**Erstellt:** 16.11.2026 · **Basis:** vom Lernenden bereitgestelltes Foto eines handschriftlich ausgefüllten Formulars „Inbetriebnahmeprotokoll – Erst- und Wiederholungsprüfung elektrischer Anlagen“, DB Training, Druckdatum **26.03.2026**, „**Seite 2/2**“.  
**Zweck:** Eigenständige **Bild-/Lernanalyse** zur AP1. Kein rechtsverbindlicher Prüfbericht, keine Freigabe einer Anlage und keine Bestätigung der real gemessenen Werte. Das Originalfoto wurde nicht ins öffentliche Repository übertragen.
**Wichtig:** Seite 1 von 2 liegt uns im vorliegenden Foto **nicht** vor. Einige handschriftliche Zahlen sind nicht eindeutig lesbar. Unklare Ziffern nicht als gesicherte Messwerte ausgeben!

## 1. Aufbau der Seite

**Oberer Block:** je Stromkreis/Klemmenziel ein Leitungs- und Querschnittseintrag, Soll-/Istwert der Schutzleiterdurchgängigkeit (Ohm), Soll-/Ist-Isolationswiderstand (MOhm), ggf. RCD-Typ/IΔn/Auslösestrom/Auslösezeit/Berührungsspannung und Überstromschutzgerät mit Bemessungsstrom, Soll-/Ist-Schleifenimpedanz (Ohm), Kurzschlussstrom (A).

**Mittlerer Block:** Betriebs-Spannungsmessungen (Messstellen, Vorgabe, Messwert, AC oder DC).

**Unterer Block:** Erproben (Drehfeld, Anlage, Drehrichtung der Motoren, Einhaltung elektrotechnischer Regeln, Schutz-/Sicherheitseinrichtungen und weiterer handschriftlicher Prüfschritt), festgestellte Mängel/Bemerkungen, Datum und Unterschriften.

## 2. Abschrift der obersten Tabelle (soweit erkennbar)

**Hinweis zur Zuordnung:** Die Zeilennummern dienen hier der Analyse; handschriftliche Gerätebezeichnungen der Fotoquelle sind teilweise überschrieben und schwer lesbar. Keine neuen Geräte-/Normwerte hinzuerfinden.

| Zeile | Leiterquerschnitt laut Foto | RPE-Vorgabe (Ω) | RPE-Messwert (Ω) | RISO-Vorgabe (MΩ) | RISO-Messwert (MΩ) | Zs-Vorgabe (Ω) | Zs-Messwert (Ω) | Ik (A) |
|---:|---:|---|---:|---:|---|---:|---:|---:|
| 1 | 2,5 mm² | handschriftlich unklar („0,?14“ oder ähnlich) | **vermutlich 6,04** | ≥ 1 | > 500 | – | – | – |
| 2 | 1,5 mm² | gleichartiger Eintrag | 0,03 | ≥ 1 | > 500 | 2,7 | 0,7 | 335 |
| 3 | 1,5 mm² | gleichartiger Eintrag | 0,03 | ≥ 1 | > 500 | 2,7 | 1,0 | 237 |
| 4 | 1,5 mm² | gleichartiger Eintrag | 0,03 | ≥ 1 | > 500 | 2,7 | 1,9 | 123 |
| 5 | 1,5 mm² | gleichartiger Eintrag | **leer** | ≥ 1 | > 500 | 7,6 | 1,0 | 235 |
| 6 | 0,75 mm² | gleichartiger Eintrag | 0,05 | ≥ 1 | > 500 | – | – | – |

**Wichtigster möglicher Fehler:** Bei Zeile 1 sieht die erste Ziffer des RPE-Messwerts nach einer **6** aus, nicht nach einer 0: **„6,04 Ω“**. Bei einem typischen kurzen Schutzleiterweg wäre das ein hochgradig auffälliger Wert und vermutlich deutlich oberhalb des eingetragenen Sollwerts. **Keine Freigabe auf Grundlage dieses Fotos.** Original-Eintrag und Messung am realen, sicheren Prüfaufbau durch die verantwortliche EFK klären. Wenn nur „0,04 Ω“ gemeint war, muss die Handschrift vor der Dokumentation eindeutig korrigiert werden, nicht stillschweigend umgedeutet werden.

**Zweiter dokumentarischer Fehler:** Zeile 5 hat im RPE-Messwertfeld keinen Eintrag. Ob die Messung fehlt, nicht erforderlich ist oder die Dokumentation unvollständig ist, lässt sich ohne Schaltplan/Seite 1 nicht beurteilen. Ggf. **„nicht anwendbar“ mit Begründung** statt leerem Feld dokumentieren.

### Isolationsmessungen

Alle sechs Messwerte scheinen **„>500 MΩ“** zu lauten; der Sollwert scheint sechsmal **„≥1 MΩ“** zu sein. Zahlenvergleich: >500 MΩ liegt deutlich über ≥1 MΩ. **Das beweist aber nicht**, dass jeder zu prüfende Leiter korrekt geprüft wurde: Prüfgleichspannung, Messkonfiguration, Schutz/Abtrennung empfindlicher SPS-Geräte, tatsächlicher Stromkreis und Messgerät stehen nicht in diesem Foto.

Die übliche Mindesttabelle DIN VDE 0100-600: SELV/PELV 250 V DC / 0,5 MΩ; bis 500 V einschließlich FELV 500 V DC / 1 MΩ; über 500 V 1000 V DC / 1 MΩ. **Die konkrete Stromkreisart zuerst bestimmen.**

### Überstromschutz/Schleifenimpedanz

Die vier eingetragenen Istwerte sind 0,7 / 1,0 / 1,9 / 1,0 Ω, gegen die jeweiligen Vordrucke 2,7 / 2,7 / 2,7 / 7,6 Ω. **Reiner Zahlenvergleich:** jeder Istwert ist kleiner als der angegebene Vorgabewert.

Dass die Werte rechnerisch zusammenpassen, zeigt **U≈Z×Ik**:
- 0,7 Ω × 335 A = **234,5 V**.
- 1,0 Ω × 237 A = **237 V**.
- 1,9 Ω × 123 A = **233,7 V**.
- 1,0 Ω × 235 A = **235 V**.

Alle vier berechneten Werte liegen bei rund 234–237 V, passend zu dem Fotoeintrag ca. 233–234 V AC. Das ist eine **Plausibilitätskontrolle**, keine unabhängige Messung des Kurzschlussstroms.

**Nicht gesichert:** Ob 2,7 Ω und 7,6 Ω tatsächlich die zulässigen Schleifenimpedanzen der eingesetzten Schutzorgane sind. Die handschriftlichen Einträge zu Typ, Kennlinie, Nennstrom und Netzsystem lassen sich nicht ausreichend eindeutig lesen. Daher **kein normatives „bestanden“ allein aus dem Zahlenvergleich**. Für den MSS ist dessen magnetischer Auslösestrom, Ansprechbereich und Schutzkombination relevant; für Sicherungen/LS die jeweilige Zeit-Strom-Kennlinie, Netzsystem und geforderte Abschaltzeit.

### RCD-Block

Alle RCD-Felder sind leer. Daraus folgt **nicht automatisch**, dass eine vorgeschriebene RCD-Prüfung fehlt: Vielleicht wurde kein RCD eingesetzt, vielleicht dokumentiert Seite 1 eine RCD, vielleicht ist die Prüfung tatsächlich offen. Ein „entfällt – keine RCD in diesem geprüften Stromkreis“ wäre nachvollziehbarer als ein unbegründetes Leerfeld, **falls das fachlich zutrifft**.

## 3. Betriebs-Spannungen (Foto, mittlerer Block)

| Eintrag | Messstelle laut Handschrift | Soll | Ist | Rechnerischer Unterschied |
|---|---|---:|---:|---|
| M1 | vermutlich Motor-Klemmen U1/V1 | 400 V AC | **404 V AC** | +1 % |
| M2 | überstrichene/ersetzte Klemmenbezeichnung, offenbar L1/PE | 230 V AC | **234 V AC** | +1,74 % |
| M3 | vermutlich Motor-Klemmen U1/V1 | 400 V AC | **406 V AC** | +1,5 % |
| T1 | N/L | 230 V AC | **233 V AC** | +1,30 % |
| T2 | L+/L− | 24 V DC | **vermutlich 25,3 V DC** | +5,42 % |

Die Werte sind **zahlenmäßig plausibel**, wenn Messstellen und Betriebsmittel dazu passen. Der zulässige Betriebsspannungsbereich muss aber aus **Geräte-/Netzteil-Datenblatt und konkreter Anwendung** abgeleitet werden. Gerade 24-V-SPS-Netzteile dürfen nicht allein anhand einer pauschalen ±10-%-Faustregel beurteilt werden. Strich-Korrekturen der Messstellen sollten lesbar und nachvollziehbar bereinigt werden.

## 4. Erproben: Kennzeichnungen im unteren Block

| Prüffeld | Eintrag im Foto | Feststellung |
|---|---|---|
| Rechtsdrehfeld der Drehstromsteckdosen | i. O. angekreuzt | Positive Behauptung im Protokoll, ohne unabhängigen Nachweis |
| Funktion der Anlage | **nicht i. O. angekreuzt** | **Expliziter Mangel**, aber Grund nicht beschrieben |
| Drehrichtung der Motoren | i. O. angekreuzt | Positive Behauptung |
| Anlage entspricht anerkannten Regeln der Elektrotechnik | i. O. angekreuzt | **Vorsicht:** Bewertung ist fraglich, solange der auffällige RPE-Wert/fehlende Angaben ungeklärt sind |
| Funktion der Schutz- und Sicherheitseinrichtungen | i. O. angekreuzt | Positive Behauptung, keine Einzelprotokolle sichtbar |
| Weitere handschriftliche Zeile („Spannungsfall“ oder ähnlich) | i. O. angekreuzt | Prüfschritt und Mess-/Berechnungsgrundlage nicht eindeutig lesbar |

**Sehr wichtig:** Bei „Funktion der Anlage – nicht i. O.“ fehlt im Feld „festgestellte Mängel/Bemerkungen“ die **Fehlerbeschreibung**. Ohne Mangelort, Fehlerart, Behebung, ggf. Nachprüfung und Freigabe darf daraus nicht „Anlage vollständig geprüft und betriebsbereit“ gemacht werden.

## 5. Weitere Dokumentationslücken

1. **Foto zeigt nur Seite 2/2**; Seite 1 mit Anlagenidentifikation, Netzsystem, Messgerät und Prüfumfang muss zusätzlich geprüft werden.
2. **Prüfer/Datum/Unterschrift** und Auftraggeberangaben am Seitenende sind nicht eingetragen. Je nach Gestaltung kann eine Signatur auf Seite 1 stehen; **nicht annehmen**, dass es reicht.
3. Keine explizite Angabe der **RISO-Prüfspannung** auf dieser Seite.
4. Die sechs identischen/ähnlichen RPE-Vorgaben sind ohne Leitungswege/Querschnitte bzw. Herkunft der Sollwerte nicht nachvollziehbar. **Vorgabe aus Plan/Berechnung klären.**
5. Das Feld RCD ist leer; Relevanz erst nach Anlagen-/Netzsystemprüfung beurteilen.
6. Zeile 5 hat keinen dokumentierten RPE-Istwert.
7. Der erste RPE-Istwert könnte **6,04 Ω** sein; dringende Lese- und Messwertklärung.
8. Überstromschutzkennlinien/Nennströme sind handschriftlich teils unlesbar; die Zs-Sollwerte können deshalb nicht unabhängig bestätigt werden.
9. Die Funktionsprüfung der Anlage ist **ausdrücklich „nicht i. O.“**, aber es gibt **keinen Eintrag** zu Mangel und Maßnahmen.
10. Korrigierte/überschriebene Messpunkte sind schwer zuzuordnen.

## 6. Was davon für die AP1 zu lernen ist

- **RPE:** Niedriger Messwert allein genügt nicht. Liegt er über dem tatsächlich erwarteten Wert, Fehler suchen – und Leitungswege/Querschnitte beachten.
- **RISO:** Widerstand **oberhalb** des zutreffenden Mindestwerts gut, aber nur wenn Messspannung, Messweg und Elektronikschutz stimmen.
- **Zs:** **Kleiner** als der zutreffende Maximalwert ist günstig; Schutzgerät/-kennlinie muss den Maximalwert begründen.
- **Ik:** Näherungsweise **Ik = U0 / Zs**. Je größer die Impedanz, desto kleiner der zu erwartende Fehlerstrom; prüfe, ob Schutzorgan schnell genug abschalten kann.
- **RCD:** IΔn, gemessener Auslösestrom und gemessene Zeit sind verschiedene Felder; bei Nichtanwendbarkeit nicht imaginäre Werte eintragen.
- **U:** Soll und Ist sowie AC/DC, Messstellen und herstellerspezifische Toleranz dokumentieren.
- **Erproben:** „nicht i. O.“ ohne Fehlerbeschreibung ist keine abgeschlossene Mängelbearbeitung.
- **Unterschrift/Freigabe:** Eine Tabelle mit handschriftlichen Zahlen alleine ist kein gültiger Nachweis der fachlich freigegebenen Gesamtanlage.

## 7. Bewertung und nächster Abgleich

**Erste vorläufige Bewertung:**  
- **Plausibel:** Schleifenimpedanz–Kurzschlussstrom-Paare und die meisten Spannungswerte.  
- **Vorläufig zahlenmäßig positiv:** >500 MΩ gegen ≥1 MΩ, **aber** Messaufbau/Prüfspannung offen.  
- **Ungeklärt/kritisch:** RPE-Zeile 1, RPE-Leerfeld Zeile 5, Zuordnung/Zulässigkeit der Zs-Vorgaben, leere RCD-Spalte, „Anlagenfunktion nicht i. O.“.  
- **Nicht belegbar:** vollständige Normkonformität oder Freigabe.

**Für die vollständige Einordnung fehlen:** das zugehörige **Blatt 1/2**, gut lesbare erste RPE-Messwertzelle im Original, Schaltplan/Netzsystem und eindeutige Schutzgeräte (inkl. Einstellwert/Kennlinie).

## 8. Fachliche Referenzen

- DKE – DIN VDE 0100-600:2017-06 – Anwendungsbereich: https://www.dke.de/de/normen-standards/dokument?id=7089969&type=dke%7Cdokument
- DKE – Mindestinhalte eines Prüfberichts und Bewertung der Messwerte (Klarstellung): https://www.dke.de/de/arbeitsfelder/core-safety/normenhinweise/dke-uk-221-1-zu-mindestinhalte-eines-pruefberichts
- WEKA – Erstprüfung, Messarten, RISO-Mindestwerte: https://www.weka.de/elektrosicherheit/erstpruefung-nach-din-vde-0100-600/
- DB-Trainingshandbuch vom 25.03.2026: Auswertung und fachliche Einordnung in [01_Analyse_Handlungsleitfaden.md](01_Analyse_Handlungsleitfaden.md) und [02_Kritische_Stellen_und_Normenabgleich.md](02_Kritische_Stellen_und_Normenabgleich.md).

**Hinweis zur Quellenlogik:** Alles, was als „Foto zeigt“, „scheinbar“, „vermutlich“ bezeichnet wird, ist die **Transkription bzw. visuelle Einschätzung** der vorliegenden Abbildung. Berechnungen und die Norm-/Sicherheitseinordnung sind **zusätzliche eigene Analyse**.
