# Handlungsleitfaden „Prüfen von elektrischen Anlagen“ – vollständige AP1-Auswertung

**Status:** Eigenständige Lernanalyse, keine technische Freigabe und keine Wiedergabe der Originalunterlage.  
**Geprüfte Quelle:** DB Training, Learning & Consulting, *Handbuch mit Lösungen/Hinweisen: Prüfen von elektrischen Anlagen – DIN VDE 0100-600*, Version 25.1, fachlicher Stand 25.03.2026, Produkt Bt1103.  
**Dateiumfang:** 32 PDF-Seiten; Titelseite, Impressum, Inhaltsverzeichnis, 22 Seiten fachlicher Text, anschließend teilweise Platzhalter/Formatvorlagen und Verzeichnisse.  
**Analysedatum:** 16.11.2026.  
**Bedeutung von „Seite“:** Im Folgenden ist die aufgedruckte **Handbuchseite** gemeint. Bei der PDF-Seitenzahl sind sechs Seiten Vorlauf hinzuzurechnen: Handbuch-S. 1 = PDF-S. 6; Handbuch-S. 22 = PDF-S. 27.

> **Urheberrecht:** Die DB untersagt in der Unterlage eine Vervielfältigung oder Bearbeitung ohne Zustimmung. Die Original-PDF wurde daher **nicht** in dieses öffentliche Repository geladen. Die nachfolgende Analyse verwendet eigene Erklärungen, Prüfhinweise und Seitenverweise. Lokaler Originaltitel: „Handlingsleitfaden Inbetriebnahme vorab Version.pdf“.
>
> **Sicherheitsgrenze:** Dies ist Lernmaterial für Elektroniker für Betriebstechnik/AP1. Prüfungen und Schalthandlungen an realen Anlagen nur im zulässigen Ausbildungsrahmen unter Verantwortung einer Elektrofachkraft. Bei Abweichung gelten aktuelle Normen, Herstellerunterlagen und betriebliche Anweisungen.

## 1. Was die Quelle tatsächlich abdeckt

Die Datei ist kein vollständiger Ersatz für DIN VDE 0100-600. Sie bietet einen **praktischen Teilablauf** vor und während der Inbetriebnahme einer elektrischen Anlage. In der Titelzeile heißt es „mit Lösungen/Hinweisen“; in späteren Seiten sind deutlich noch Entwurfs- und Layoutreste enthalten.

| Handbuchseiten | PDF-Seiten | Originalkapitel | Inhalt und AP1-Bedeutung |
|---|---:|---|---|
| 1 | 6 | 1 Vorbereitung | Zuständigkeiten, Anlage identifizieren, Unterlagen prüfen |
| 2–3 | 7–8 | 2.1 | Fünf Sicherheitsregeln, Freischalten und Spannungsfreiheit |
| 3–5 | 8–10 | 2.2–2.3.1 | Montage, Mängel, Auswahl der Geräte, Verbindungen |
| 6–7 | 11–12 | 2.3.2–2.3.4 | Leiterfarben, Querschnitte, Wärme, Leitungsverlegung |
| 8–10 | 13–15 | 2.4–2.6 | Bedienelemente, Farben, Kennzeichnung; Sensoren/Aktoren nur Platzhalter |
| 11–14 | 16–19 | 3.1 | Schutzleiterdurchgängigkeit / Niederohmmessung RLO |
| 14–17 | 19–22 | 3.2 | Isolationswiderstand RISO |
| 18–20 | 23–25 | 4 | Zuschalten, Polarität, Spannungsmessung |
| 21 | 26 | – | Praktisch leere Seite |
| 22–23 | 27–28 | 5.1 | Abschaltbedingungen/RCD-Zeiten, anschließend Layouttext |
| 24–26 | 29–31 | 5.2–5.4 | Notizfläche, Piktogramme, Tabellen-/Grafikvorlagen – keine neue Prüfanleitung |
| 27 | 32 | 6 | Quellen, leeres Abkürzungsverzeichnis, Verzeichnisse |

**Wichtigste Lücke:** Trotz des Titels „Prüfen von elektrischen Anlagen“ ist die Normabdeckung nicht vollständig. Die Quelle behandelt insbesondere Fehlerschleifenimpedanz, Netzinnenimpedanz, Drehfeld, Spannungsfall, Schutz durch andere Schutzmaßnahmen und umfassende Funktionsprüfungen **nicht systematisch**. Diese Inhalte dürfen beim Lernen der vollständigen Erstprüfung nicht ausfallen.

## 2. Kapitel 1 – Vorbereitende Maßnahmen (S. 1)

### Personen und Verantwortlichkeiten
Vor Beginn muss klar sein, wer beauftragt, wer die Prüfung durchführt und wer bei einem Team fachlich verantwortlich ist. In der Dokumentation dürfen „Auftraggeber“, „Ausführender“ und „prüfende/verantwortliche Person“ nicht verwechselt werden. Die Quelle fordert die entsprechenden Angaben im Prüfprotokoll.

**Warum das wichtig ist:** Eine Messung ohne zugeordneten Stromkreis, Prüfperson und Prüfzweck ist später kaum nachvollziehbar.

### Anlage eindeutig bestimmen
Funktion, Ort und Kennzeichnung der Anlage festhalten. Bei einem Schaltschrank reicht „Lüftung“ allein nicht, wenn mehrere Lüftungsanlagen im Gebäude existieren. Für deine AP1-Übung würde man z. B. Prüfobjekt, Schaltschrankbezeichnung, Einspeisung und betrachtete Stromkreise dokumentieren.

### Unterlagen prüfen
Die Quelle nennt drei Ebenen:
1. **Vollständigkeit:** Sind alle Unterlagen/Seiten vorhanden?
2. **Übereinstimmung:** Gehören Stromlaufplan und Materialliste zu **diesem** Schaltschrank?
3. **Fachliche Lesbarkeit:** Lassen sich Anschlüsse, Funktionen und Betriebsmittel nachvollziehen?

**Typische Prüfungsfrage:** Warum darfst du mit einem fremden oder veralteten Stromlaufplan nicht einfach messen? Weil Messpunkte und angenommene Schutzmaßnahmen nicht zur realen Anlage passen könnten.

## 3. Kapitel 2 – Sichtprüfung (S. 2–10)

### 3.1 Fünf Sicherheitsregeln (S. 2–3)
Die Reihenfolge:
1. Freischalten.
2. Gegen Wiedereinschalten sichern.
3. Spannungsfreiheit **mit geeignetem Prüfgerät** feststellen.
4. Erden und kurzschließen, soweit nach Anlagenart und Gefährdung erforderlich.
5. Benachbarte, unter Spannung stehende Teile abdecken oder abschranken.

**Korrektur gegenüber der Quelle:** Eine erlöschende Netzteil-LED oder Statusleuchte ist **kein ausreichender Ersatz** für das fachgerechte allpolige Feststellen der Spannungsfreiheit. Für Niederspannungsanlagen wird der geeignete zweipolige Spannungsprüfer verwendet und vor/nach der Prüfung auf Funktion kontrolliert. Die Aussagen zu bloßem Isolierband als Einschaltschutz sind nicht als allgemeine sichere Vorgehensweise zu übernehmen. Details siehe [Kritische-Stellen](02_Kritische_Stellen_und_Normenabgleich.md).

### 3.2 Geräte im Schaltschrank (S. 3–5)
**Montage prüfen:** Stimmt der Ort im Montageplan? Ist das Gerät mechanisch sicher fixiert? Passen Einbaulage, Beschriftung, Zugänglichkeit und Abdeckung? Bei Reihenklemmen sind korrekte Endplatten/Abschlüsse und Berührungsschutz wichtig.

**Schäden prüfen:** Gehäuse, Verrastung, Verfärbung, Brandspuren, lockere Teile, beschädigte Anschlussklemmen und grobe Verschmutzung sind mögliche Mängel.

**Geräteauswahl überprüfen:** Nicht nur „passt in den Schaltschrank?“, sondern „passt die elektrische Funktion?“
- Schutzgerät: Welchen Fehler soll es erkennen? Überlast, Kurzschluss, Fehlerstrom?
- Schaltgerät: Welche Last, Gebrauchskategorie, Kontakte und Spulen-/Steuerspannung?
- Anschluss: Welche Leiterarten, Querschnitte, Drehmomente und ggf. Aderendhülsen erlaubt der Hersteller?
- Betriebsmittel: Welche Bemessungsspannung, welcher Strom, welche Schutzart?

**Bezug zu deinen Bauteilen (Lernbeispiel, nicht aus diesem Handbuch):**
- MSS Moeller/Eaton PKZM01-4, thermisch einstellbar von 2,5 bis 4 A. Ein realer Motor mit 0,85 A Nennstrom liegt **außerhalb** dieses Einstellbereichs.
- Schütz Moeller/Eaton DILM9-10 mit 24-V-DC-Spule: Spulenspannung und Hauptkontaktbelastbarkeit sind getrennte Angaben.
- **Aderendhülse:** Der Leiterquerschnitt und die Abisolierlänge aus dem Geräteblatt sind nicht automatisch eine Festlegung auf eine beliebige Metallhülsenlänge. Beide Klemmen müssen mit dem konkreten Leitertyp/herstellerkonformen Anschluss verglichen werden.

### 3.3 Anschlüsse und Drehmoment (S. 5)
Wichtige Sichtprüfung: Liegt der Leiter richtig in der Klemme? Ist die Isolation unbeschädigt? Sitzt die Aderendhülse vollständig passend? Gibt es lose Einzeldrähte, Zugbelastung oder Leitungen außerhalb des zulässigen Klemmbereichs?

**Korrektur:** Pauschalwerte wie „bei unter 16 A meist 1,2 Nm“ und die Aussage, ein normaler Schraubendreher genüge zur Drehmomentkontrolle, sind kein Ersatz für die **exakte Herstellerangabe und geeignete Drehmomentprüfung**. Bei deinem PKZM01-4 kann ein Wert anders sein als beim Schütz.

### 3.4 Leiterfarben (S. 6)
Die Quelle unterscheidet Installations- und Maschinenkennzeichnung:
- In typischen Installationsstromkreisen sind PE grün-gelb und N blau; Außenleiter werden üblicherweise braun, schwarz und grau zugeordnet.
- Für Maschinensteuerungen werden häufig Schwarz für Hauptstromkreise, Rot für AC-Steuerung, Blau für DC-Steuerung und Orange für bestimmte Fremd-/Sonderkreise verwendet.

**Wichtig:** Farben nie allein als Beweis der Leiterfunktion verwenden. Plan und fachgerechte Prüfung sind entscheidend. Nicht jeder blaue Steuerleiter ist automatisch ein Neutralleiter.

### 3.5 Leitungsquerschnitt (S. 6–7)
Die Quelle erläutert: Strombelastbarkeit, Umgebungstemperatur, Verlegeart/Wärmeabfuhr und mechanische Beanspruchung beeinflussen die Auswahl. Die Erwärmung folgt der Verlustleistungsbeziehung **P = I² × R**; ein größerer Querschnitt hat bei gleicher Länge und gleichem Material üblicherweise einen kleineren Widerstand.

**Wichtige Präzisierung:** Die im Handbuch genannten **2,5 mm² (mechanisch geschützt)** bzw. **4 mm² (ungeschützt)** betreffen unter bestimmten Bedingungen **separat verlegte Kupfer-Schutzleiter**. Das ist keine allgemeine Mindestgröße für den grün-gelben Leiter innerhalb jedes mehradrigen Kabels. Die Querschnitte der Haupt- und Steuerleitungen sind stets für den konkreten Fall zu bemessen; die Quelle nennt 0,75 mm² als gängige Steueradergröße, **aber die jeweilige Geräteklemme muss das erlauben**.

### 3.6 Leitungsverlegung (S. 7)
Beim Besichtigen auf ausreichend Bewegungsreserve, saubere Kanalführung, Biegeradien, Kantenschutz, Trennung nach erforderlicher Schutzart und Zugentlastung achten. Keine unter Spannung stehenden Adern anfassen oder durch bloße Zugprobe gefährden.

### 3.7 Bedienelemente (S. 8–10)
Im Fokus stehen:
- Bauart und Schutzart passend zur Umgebung.
- Taster-/Kontakt-/Leuchtelement korrekt aufgesteckt.
- Innere Bauteilkennzeichnung und äußere Funktionsbeschriftung auseinanderhalten.
- Angemessene Betätigungs-/Meldegerätfarben und eindeutige Legende.
- Leitungen zu beweglichen Türen/Bedienstellen mechanisch sichern und kennzeichnen.

Die Farbzuordnungen im Handbuch sind **eine vereinfachte Eselsbrücke**, keine alleinige Entscheidung über die Zulässigkeit einer Farbe. **Sensoren/Aktoren (2.6) sind in der gelieferten Fassung nicht ausgearbeitet.**

## 4. Kapitel 3 – Messungen im spannungsfreien Zustand (S. 11–17)

### 4.1 RLO: Schutzleiterdurchgängigkeit (S. 11–14)
**Zweck:** Prüfen, ob alle erforderlichen Schutzleiter- und Schutzpotentialausgleichsverbindungen elektrisch zuverlässig durchgängig sind.

**Prinzip:** Das Prüfgerät speist einen Prüfstrom ein und ermittelt über den Spannungsfall den Widerstand: **R = U / I**. Für die normgerechte Niederohmprüfung sind einschlägige Anforderungen an Prüfstrom, Spannungsquelle und Gerät zu beachten; in der Ausbildung wird häufig mit mindestens **200 mA** gearbeitet.

**Was der Handlungsleitfaden lehrt:**
1. Zustand von Gerät und Messleitungen kontrollieren.
2. RLO-Funktion wählen; die Polung bei DC sowie ggf. automatische Umpolung berücksichtigen.
3. Gute und schlechte Anzeige am Prüfgerät kontrollieren.
4. Prüfleitungs-/Zubehörwiderstand bei Bedarf über Offset kompensieren.
5. Messstellen an Schutzleiterverbindungen möglichst aussagekräftig wählen.
6. Prüfen, Messwert mit berechnetem/erwartetem Widerstand vergleichen, protokollieren.

**Offset-Beispiel:** Anzeigenwert 0,26 Ohm inklusive 0,08 Ohm Prüfleitung → nach korrektem Offset ungefähr 0,18 Ohm für den geprüften Abschnitt. Das ist **nur ein Rechenbeispiel**, kein gemessener Anlagenwert.

**Grenzwert:** Kein allgemeiner universeller Fixwert wie „RPE muss immer kleiner als 1 Ohm sein“. Erwarteter Leitungswiderstand abhängig von Länge, Querschnitt, Material und Übergangsstellen. Der im Handbuch genannte Pauschalansatz für Klemmstellen ist nur eine Abschätzung, kein pauschal normativer Grenzwert.

**Sicherheitskorrektur:** Ein beliebiger Heizkörper darf nicht ohne Nachweis als zuverlässiger Schutzleiter-Bezugspunkt angenommen werden. Und „höherer Prüfstrom ist immer genauer“ ist zu allgemein.

### 4.2 RISO: Isolationswiderstand (S. 14–17)
**Zweck:** Nachweisen, dass zwischen dafür voneinander getrennten leitfähigen Teilen keine unzulässigen Isolations-/Leckpfade vorhanden sind.

**Prinzip:** Das Isolationsmessgerät legt eine definierte **Gleichprüfspannung** an und bestimmt einen sehr großen Widerstand. Messung im **spannungsfreien** Zustand, dafür geeignete Prüfmittel und fachgerechtes Trennen empfindlicher Betriebsmittel. Die DC-Prüfung vermeidet einen dauerhaften kapazitiven Wechselstrom, der die Widerstandsmessung verfälschen würde.

| Stromkreis | Typische Prüfgleichspannung für Erstprüfung | Mindest-Isolationswiderstand |
|---|---:|---:|
| SELV / PELV | 250 V DC | 0,5 MOhm |
| Bis einschließlich 500 V sowie FELV | 500 V DC | 1 MOhm |
| Über 500 V | 1000 V DC | 1 MOhm |

Diese Zahlen aus der Quelle stimmen mit der Mindestwert-Tabelle der DIN VDE 0100-600:2017-06 überein. **Die Auswahl hängt von der tatsächlichen Stromkreisart ab**, nicht bloß davon, ob am Netzteil irgendwo „24 V“ steht.

**Messpunkte:** Aktive Leiter untereinander und aktive Leiter gegen Schutzleiter gemäß anwendbarem Verfahren; berücksichtigen, ob Schalter/Schütze Teile der Leitung abtrennen. Ob Einzelleiter geprüft oder zusammengefasst werden, richtet sich nach Anwendungsfall/Norm/Schutz der angeschlossenen Geräte.

**Beispiel:** 500-V-Prüfung, Messwert 8,6 MOhm → oberhalb des tabellarischen Mindestwerts von 1 MOhm. Aussage nur für korrekt gewählten Prüfaufbau/Umfang; kein Freibrief für die gesamte Anlage.

**Sehr wichtig für deine SPS-Anlage:** Ein PLC-Eingang, Netzteil, Sensor, Überspannungsschutz oder elektronische Verbraucher können durch eine ungeeignete 500-V-Isolationsprüfung beschädigt werden. In der Quelle genannte Alternativen wie „Verbraucher kurzschließen“ oder „Messung weglassen“ sind **keine pauschalen Anweisungen**. Nur nach Prüfplan, EFK-Bewertung und Herstellerunterlagen vorgehen.

**Messprotokoll:** Der Leitfaden erwähnt, dass für den PAL-AP1-Ausbildungsfall die **Einzeldokumentation einer Zuleitung** verlangt werde (S. 17). Das ist als Aussage **dieses Ausbildungsskripts** zu behandeln; die konkrete Prüfungsunterlage und die aktuelle PAL-Vorgabe sind separat maßgeblich.

## 5. Kapitel 4 – Messungen unter Spannung (S. 18–20)

**Achtung:** Erst nach abgeschlossenem/ausgewertetem spannungsfreien Teil, nach sicherer Freigabe und im zugelassenen Ausbildungsrahmen. Es ist nicht Aufgabe eines Lerntexts, eine Person ohne Aufsicht zum Einschalten aufzufordern.

### 5.1 Spannungsrichtigkeit/Polarität
Bei DC ist **Plus/Minus** funktional wichtig (z. B. 24 V DC L+/M); bei AC müssen Leiterzuordnung und die Schutzmaßnahmen stimmen. Der Leitfaden nennt besonders DC-Stromkreise und einpolig geschaltete Einrichtungen.

### 5.2 Messkategorien und Messgeräte
Die Quelle erklärt CAT I–IV anhand von Einsatzbereichen. **Praktische Frage:** Ist das Messgerät bei der konkreten Anlage und dem möglichen Kurzschluss-/Überspannungsrisiko geeignet? Messkategorie, Nennspannung, Leitungen, Messspitzen und Gerätezustand prüfen.

**Achtung:** Ein Messgerät kann Messwerte außerhalb seines spezifizierten Messbereichs anzeigen. Dass eine Anzeige „24 V“ zeigt, beweist daher weder korrekte Messfunktion noch korrekte Polarität; passende DC-Messfunktion und Messbereich sind erforderlich.

### 5.3 Spannungswert messen und dokumentieren
Zu einem Messwert gehört: Messpunkte, **AC oder DC**, Sollwert, Istwert, Einheit, Messgerät, Datum/Prüfer und Bewertung. Ein Wert nur als „24“ ist unvollständig. Die im Text genannte pauschale **±10-%-Grenze auch für 24-V-DC-Steuerkreise** ist nicht generell aus EN 50160 ableitbar; konkrete Geräte- und Netzteil-Toleranzen prüfen.

**Beispiel (fiktiv):** SPS-Versorgung zwischen L+ und M: Soll 24 V DC, gemessen 24,3 V DC. Das Ergebnis lässt sich **erst nach Vergleich mit zulässiger Toleranz** als in Ordnung bewerten.

## 6. Kapitel 5 – Abschaltbedingungen/RCD (S. 22–23)

Die Quelle unterscheidet:
- **Abschaltbedingung der Schutzmaßnahme:** abhängig von Netzsystem, Spannung und Schutzkonzept, beispielsweise TN-System bei 230 V.
- **Gerätebezogene RCD-Auslösezeit:** abhängig von RCD-Typ, Bemessungsdifferenzstrom, Prüfstrom und selektiver/zeitverzögerter Ausführung.

Im Handbuch werden als **vereinfachte Beispiele für gewöhnliche, nicht zeitverzögerte RCCB** genannt: bei 1 × IΔn höchstens 300 ms, 2 × IΔn höchstens 150 ms, bei 5 × IΔn 40 ms **nur im einschlägigen Gerätekontext**. Dies sind **keine universellen Werte für jeden RCD-Typ**.

**Wichtig:** Eine bestandene RCD-Auslösezeit allein beweist nicht den vollständigen Schutz der Anlage. Netzsystem, RCD-Eigenschaften, PE-Verbindung und weitere Schutzbedingungen gehören in die Bewertung.

## 7. Was du auswendig erklären und tatsächlich verstehen solltest

| Begriff | Einfache fachliche Erklärung |
|---|---|
| Besichtigen | Ohne betriebliche Funktion auszulösen prüfen: Ist Anlage korrekt aufgebaut und geeignet? |
| Erproben | Funktion/Einstellungen von vorgesehenen Einrichtungen kontrollieren |
| Messen | Mit geeignetem Gerät Zahlenwerte nachweisen und bewerten |
| RLO / RPE | Niederohm-/Schutzleiterdurchgängigkeit |
| RISO | Hoher Widerstand der Isolation zwischen getrennten Stromkreisteilen |
| Offset | Eigenwiderstand von Messleitung/Zubehör rechnerisch abziehen |
| Prüfspannung | Spannung, die das Prüfgerät zur Messung erzeugt |
| Messkategorie CAT | Eignung des Messgeräts für die Überspannungs-/Energieumgebung |
| IΔn | Bemessungsdifferenzstrom des RCD |
| Abschaltzeit | Maximale Zeit bis die vorgesehene Schutzeinrichtung abschaltet |
| Prüfprotokoll | Nachvollziehbare Ergebnisse von Besichtigen, Erproben, Messen und Mängeln |

## 8. Was im Leitfaden fehlt – für eine komplette AP1 ergänzen

1. **Fehlerschleifenimpedanz Zs:** Kurzschluss-/Fehlerstromweg L–PE in passendem Netzsystem; Abschaltbedingungen beurteilen.
2. **Netzinnenimpedanz Zi / prospektiver Kurzschlussstrom:** Kurzschluss L–N oder L–L, Zuordnung zu Überstromschutzgerät.
3. **Drehfeldprüfung:** Phasenfolge, Motor-Drehrichtung, sichere Inbetriebnahme.
4. **RCD-Auslösestrom und RCD-Typen:** neben Zeit auch Prüfstrom und Typ A/F/B/S angemessen beurteilen.
5. **Spannungsfall:** Messung/Berechnung und Vergleich.
6. **Elektrische und funktionale Steuerungsprüfung:** Taster, Meldeleuchten, Verriegelungen, Schütze, Motorschutz, SPS-Programm und Not-Halt-/Schutzfunktionen, soweit vorhanden.
7. **Konkreter Prüfbericht:** Mängelbewertung, Nichtbestanden/Bestanden, Prüfumfang, eingesetzte Geräte, Fachfreigabe.
8. **Anlagenspezifische Sensoren und Aktoren:** Abschnitt 2.6 der Original-PDF ist unvollständig.
9. **Aktueller Normen-/Herstellerabgleich:** Die DB-Unterlage weist selbst darauf hin, dass sie nicht fortlaufend aktualisiert wird.

## 9. Beispiel: Den Ablauf auf dein Lüftungsanlagen-Trainingsprojekt übertragen

**Vorbereitung:** Aufgabe, Stromlaufplan, Klemmenliste, Betriebsmitteldaten, Einspeiseart sowie geplanter/realer Unterschied der simulierten Motoren klären. Die bisher bekannte Laborschaltung verwendet SPS, 24-V-DC-Steuerung, Motorschutzschalter, Schütze, drei Sensorsignale und Meldeanzeigen; konkrete Ausführung am Prüfstand gegen die **aktuelle** Planversion verifizieren.

**Besichtigen:** Sind Haupt- und Steueradern den richtigen Klemmen zugeordnet? Sind Hilfskontakt und Hauptanschluss nicht verwechselt? Ist der MSS bei real angeschlossenen Motoren auf passende Nennströme ausgelegt? Welche Klemmen erlauben 0,75 mm², welche erst ab 1 mm²? Trägt die Schützspule 24 V DC?

**Spannungsfreie Messungen:** PE-Durchgängigkeit und Isolation nach freigegebenem Prüfplan und anlagengerechter Abtrennung empfindlicher Elektronik; nicht beliebig an SPS und Sensorplatine mit hoher Prüfspannung messen.

**Spannungsführende Prüfung/Funktion:** Erst nach Freigabe 24-V-Versorgung, Eingangs-/Ausgangsfunktionen, Taster, Meldelampen, Sensorzustände und die im Programm festgelegten Mindestlauf-/Nachlaufzeiten testen. Ein TON/TOF-Funktionsnachweis ist keine Schutzleiter-/Isolationsprüfung.

**Abschluss:** Messwerte und Ergebnisse auf den **tatsächlich** überprüften Umfang begrenzen; Abweichungen dokumentieren und vor Freigabe korrigieren lassen.

## 10. Lern- und Nachweismodell

- **Stufe 1 (Verstehen):** Erkläre ohne Ablesen die Reihenfolge Vorbereiten → Besichtigen → Messen/Erproben → Bewerten → Dokumentieren.
- **Stufe 2 (Rechnen):** Widerstand R = U/I, Leitungswiderstand aus Länge/Querschnitt, RISO-Tabellenwerte, einfacher Spannungs-Sollwertvergleich.
- **Stufe 3 (Anwenden):** Für reale/abgebildete Bauteile Herstellerdaten zu Strom, Spannung, Klemmen, Anzugsdrehmoment, Schutzart und Kategorie finden.
- **Stufe 4 (Urteilen):** Eine nicht fachgerechte Verbindung, ungeeignete Prüfgerät-Einstellung oder falschen Grenzwert **begründen**, nicht nur „falsch“ markieren.
- **Stufe 5 (Nachweisen):** Prüfbericht vollständig und überprüfbar ausfüllen – niemals Messwerte erfinden.

## Weitere Dateien in diesem Lernordner

- [02 – Kritische Aussagen und Normenabgleich](02_Kritische_Stellen_und_Normenabgleich.md)
- [03 – AP1-Prüfcheckliste und Lernaufgaben](03_AP1_Pruefcheckliste.md)

## Recherche-/Nachschlagequellen (externe Quellen; Quelle oben bleibt ausdrücklich getrennt)

- DKE, Geltungsbereich DIN VDE 0100-600: https://www.dke.de/de/normen-standards/dokument?id=7089969&type=dke%7Cdokument
- DKE, Klarstellung zum Prüfbericht: https://www.dke.de/de/arbeitsfelder/core-safety/normenhinweise/dke-uk-221-1-zu-mindestinhalte-eines-pruefberichts
- DGUV Information 203-001, fünf Sicherheitsregeln: https://publikationen.dguv.de/widgets/pdf/download/article/284
- WEKA, Erstprüfung/Isolationsmessung (Fachartikel, 2026): https://www.weka.de/elektrosicherheit/erstpruefung-nach-din-vde-0100-600/
- ABB, RCD-FAQ: https://new.abb.com/low-voltage/de/produkte/installationsgeraete/fehlerstrom-schutzeinrichtungen/faq
- DKE, Isolationsmessgeräte DIN EN IEC 61557-2: https://www.dke.de/de/normen-standards/dokument?id=7178976&type=dke%7Cdokument

**Redaktionelle Trennung:** Aussagen, die mit „Quelle“ oder Handbuchseite bezeichnet sind, geben den Inhalt der hochgeladenen PDF sinngemäß wieder. Als **Korrektur**, **Präzisierung** oder **Zusatz** gekennzeichnete Angaben sind unsere zusätzliche Einordnung. Für die praktische Durchführung gelten stets die aktuellen Originalnormen und Geräteunterlagen.
