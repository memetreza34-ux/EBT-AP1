# Kritische Stellen und Normenabgleich – DB-Handlungsleitfaden Bt1103

**Basis:** vollständige Sichtung der 32-seitigen PDF, Version 25.1, Stand 25.03.2026. Die nachstehenden Punkte sind eine **redaktionelle Sicherheits- und Plausibilitätsprüfung** – keine amtliche Normenauskunft und keine vollständige Zertifizierung. Quellen bleiben kenntlich.

## A. Sofort richtigstellen – sicherheitsrelevant

| Priorität | Original-Handbuchseite | Problem im PDF / warum problematisch | Fachliche Handhabung |
|---|---:|---|---|
| **Sehr hoch** | 2 | Neben einem Spannungsprüfer soll unter Bedingungen auch das Beobachten des Erlöschens einer internen Statusanzeige genügen. | **Nicht als alleinigen Spannungsfreiheitsnachweis verwenden.** Für Niederspannungsanlagen geeigneten zweipoligen Spannungsprüfer einsetzen; allpolig prüfen; Prüfer vor/nach Nutzung auf Funktion kontrollieren. Status-LED kann defekt sein, die falsche Versorgung anzeigen oder Fremdspannung übersehen. |
| **Sehr hoch** | 2 | Bloßes Abkleben eines Schalters mit Isolierband wird als Einschalt-Sicherung genannt. | Nicht als allgemeine geeignete Lockout-Maßnahme übernehmen; Schaltstelle gegen Betätigung verriegeln/sperren, ggf. Sicherungen gesichert entfernen und korrekt kennzeichnen nach Arbeitsanweisung. |
| **Sehr hoch** | 14 | Ein zufälliges metallisches Objekt wie ein Heizkörper wird als alternativ anschließbarer Referenzpunkt für RLO genannt. | Kein verlässlicher PE-Referenzpunkt ohne nachgewiesene Verbindung. Geeigneten, eindeutig identifizierten PE-/PA-Anschlusspunkt des Prüfobjekts einsetzen. |
| **Sehr hoch** | 16 | Bei RISO werden Verbraucher überbrücken, abklemmen oder Messung entfallen lassen als einfache Alternativen genannt. | Das sind nur in fachlich begründeten/zulässigen Fällen nutzbare Maßnahmen. Vorher Herstellerhinweise, Schutz von Elektronik, vollständigen Prüfumfang und Prüfplan beurteilen. **Keine 500 V DC ungeprüft an SPS/Netzteil/Sensoren.** |
| **Hoch** | 5 | Verallgemeinerte Anzugsdrehmomente und „normaler Schraubendreher genügt“ für Kontrolle. | **Gerätespezifisches Drehmoment** anwenden; wo erforderlich geeignetes Drehmomentwerkzeug nutzen; festes Gefühl beweist keinen korrekten Nm-Wert. |
| **Hoch** | 3 | Erden/Kurzschließen sei „erst >1000 V Pflicht“ und überall vorher immer maximal sicher. | Bei Niederspannung kann unter nachgewiesenen Bedingungen darauf verzichtet werden; bei Sonderfällen (Fremdeinspeisung, Induktion usw.) ist eine andere Bewertung nötig. Anlagen- und Gefährdungsbeurteilung geht vor. |

**Externer Sicherheitsabgleich:** [DGUV Information 203-001](https://publikationen.dguv.de/widgets/pdf/download/article/284), insbesondere Sicherheitsregeln 2 und 3; passende Originalnorm/Betriebsanweisung haben Vorrang.

## B. Fachliche Präzisierungen und Kontexte

| Nr. | S. | Aussage/Unschärfe | Korrektur/Einordnung |
|---|---:|---|---|
| 1 | 1 | Anlagendokumentation werde fachlich nur auf Lesbarkeit geprüft. | Lesbarkeit ist notwendig, aber Übereinstimmung der Dokumente mit realer Anlage, technische Richtigkeit und Anwendbarkeit der gewählten Schutzmaßnahme bleiben entscheidend. |
| 2 | 3–4 | Stark vereinfachtes Betriebsmittelkennzeichen: Minuszeichen, drei Buchstaben, Zahl. | Kennzeichnung nach anwendbarem System und Projektnorm, nicht blind aus einem einzigen Beispiel ableiten. |
| 3 | 4–5 | Lasttrennschalter könne generell ein Schütz ersetzen, umgekehrt nie. | Lasttrennschalter und Schütz haben andere Funktionen, Schaltvermögen, Gebrauchskategorien und Automatisierungsanforderungen; keine pauschale Austauschbarkeit ohne Auslegung. |
| 4 | 5 | Anpress-/Klemmkontrolle durch „festen Schraubendreher“. | Herstellerdrehmoment, Klemmenart und qualifizierte Prüfung entscheiden. |
| 5 | 6 | Farbe allein identifiziert die Stromkreisfunktion. | Leiterkennzeichnung ist nützlich, aber Plan/Anschlusslage und tatsächliche Prüfung sind maßgeblich; bei Maschinensteuerungen darf blau nicht automatisch „N“ bedeuten. |
| 6 | 6–7 | 70-°C-Grenze für PVC als allgemeine Leitungseigenschaft. | Hängt vom konkreten Leitungstyp und Hersteller ab; häufig 70 °C bei PVC-Aderleitung, aber keine universelle Eigenschaft aller PVC-Produkte. |
| 7 | 7 | PE 2,5 mm² bzw. 4 mm² ohne klare Abgrenzung. | Diese mechanischen Mindestquerschnitte betreffen **separat verlegte Kupfer-PE**; nicht pauschal PE in einer gemeinsamen mehradrigen Leitung. Anwendbare Normtabellen/Adiabatik berücksichtigen. |
| 8 | 7 | Hauptstromkreis über 1,5 mm², Steuerkreis über 0,5 mm² in pauschaler Form. | Die tatsächlichen Mindestquerschnitte hängen u. a. von Norm, Leitungsart, Mechanik, Verlegung und Klemmen ab. „>“ nicht pauschal als „≥“ interpretieren. Keine universelle AP1-Regel daraus machen. |
| 9 | 7–9 | Leitungen durch Wackeln/Ziehen allgemein prüfen. | In spannungsfreiem und entsprechend gesichertem Zustand mit sachgerechter Methode; keine unspezifische mechanische Belastung empfindlicher/energieführender Anschlüsse. |
| 10 | 9 | Farben Rot/Gelb/Grün/Blau werden stark verkürzt beschrieben. | Farbwahl richtet sich nach Funktion und einschlägiger Maschinen-/Bediennorm; keine universal gültige 1:1-Übersetzung ohne Kontext. |
| 11 | 10 | Abschnitt Sensoren/Aktoren beginnt, enthält aber nichts. | **Inhaltliche Lücke**, kein Lernstoff zu Sensorprüfung, Signalweg, Aktor, SPS. |
| 12 | 11 | RLO-Prüfstrom 0,2 bis 10 A; höherer Strom sei automatisch genauer. | 200 mA sind ein wichtiger Richtwert; die Eignung hängt von Messverfahren, Prüfgerät, Anlagenzustand und Bauteilen ab. Mehr Prüfstrom ist nicht in jedem Fall besser oder nötig. |
| 13 | 11 | „Messgerät muss kalibriert sein“ ohne Unterscheidung. | Auswahl, Sicherheit und metrologische Kontrolle gemäß betrieblichen Anforderungen und Messaufgabe; Kalibrierstatus allein ersetzt keine Geräteselbstprüfung. |
| 14 | 12 | Offset wird ausdrücklich als Pflicht für die Ausbildungsbewertung gefordert, selbst bei minimalem Zusatzwiderstand. | **Ausbildungsspezifischer Hinweis**, nicht als allgemeiner normativer Satz „immer zwingend“ ausgeben; beim tatsächlichen Messgerät korrekt durchführen. |
| 15 | 13 | PELV-Anschluss am A2-Kontakt eines Schützes könne PE-Messstelle sein. | Nur bei tatsächlich geprüfter PE-/PELV-Verbindung und geeignetem Messpunkt; Schütz-A2 ist nicht per se ein Schutzleiteranschluss. |
| 16 | 14 | Kein RPE-Grenzwert, Übergangswiderstand pauschal 0,01 Ohm/Klemmstelle. | Der fehlende allgemeine Fixwert ist nachvollziehbar. Der 0,01-Ohm-Ansatz ist eine **Schätzung**, keine stets erfüllte Eigenschaft aller Klemmen. |
| 17 | 14 | RISO-Grenzwert aus „1 kOhm pro Volt Betriebsspannung“ abgeleitet. | Für die Erstprüfung sind die **tabellierten Grenzwerte der Norm** maßgeblich, nicht eine frei angewendete 1-kOhm/V-Formel. |
| 18 | 14–15 | „Maximaler Messstrom liegt bei 1 mA“. | **Fachlich fragwürdig/falsch verallgemeinert.** IEC 61557-2 spezifiziert u. a. einen Bemessungsstrom von mindestens 1 mA; maximaler Messstrom/Kurzschlussstrom ist separat begrenzt. Den Grenzwert nicht als universelles „max. 1 mA“ lernen. |
| 19 | 16 | 5-Leiter-Stromkreis immer genau zehn RISO-Messungen. | Fünf Leiter ergeben mathematisch zehn Paare. Welche Einzelprüfungen normativ sinnvoll/erforderlich und technisch zulässig sind, hängt von Prüfkonzept, Elektronik und Anschluss der Anlage ab. |
| 20 | 17 | PAL verlange genau diese Einzeldokumentation der Zuleitung. | Nur **Ausbildungsskript-Aussage**, für eigene AP1 aktuelle Aufgaben-/PAL-Unterlagen prüfen. DKE erläutert, dass DIN VDE 0100-600 nicht die Aufzeichnung jedes Einzelwerts pauschal fordert. |
| 21 | 18 | Messkategorien CAT I–IV anhand von Kurzbeispielen. | Als Einstieg brauchbar; genaue Messkategorie nach Norm und Herstellervorgabe wählen, keine Auswahl nur nach „24 V“. |
| 22 | 19 | ±10 % gelte aus EN 50160 gleichermaßen für AC und DC-Stromkreise. | **Zu pauschal.** EN 50160 behandelt die Spannungsqualität öffentlicher Versorgungsnetze; DC-Steuerungen/Netzteile haben eigene Spezifikationen. Auch Netzspannungs-Toleranzen beziehen sich auf definierte Betriebsbedingungen und Zeiträume. |
| 23 | 19 | „Normale Multimeter“ hätten pauschale Widerstands-/Frequenzbereiche. | Hersteller-/modellabhängig; als universeller Satz nicht verwendbar. |
| 24 | 20 | Spannungsmessung werde in VDE 0100-600 nicht vorgeschrieben. | Die reine Spannungswertkontrolle ist von normativ geforderten Polaritäts-, Abschaltbedingungs- und Funktionsprüfungen zu unterscheiden; nicht als „Spannung muss nie geprüft werden“ missverstehen. |
| 25 | 22 | 300/150/40 ms wird als generelle RCD-Regel formuliert. | Gilt nicht für **alle** RCDs. Hersteller-, Geräte-, Zeitverzögerungs-, Prüfstrom- und Schutzmaßnahmeanforderungen beachten. Insbesondere selektive RCDs benötigen andere Grenzwerte. |
| 26 | 22–23 | RCD-Prüfung wird zur gesamten Kontrolle der Abschaltbedingungen verkürzt. | Es fehlen im Dokument weitere Nachweise wie ggf. Schleifenimpedanz, Netzsystem-/Schutzmaßnahmenbewertung und RCD-Eigenschaften. |

## C. Verifizierte Eckwerte zum Lernen

| Prüfgröße | Angabe | Einordnung |
|---|---|---|
| RISO SELV/PELV | 250 V DC, mindestens 0,5 MOhm | Tabelle 6.1, DIN VDE 0100-600:2017-06 |
| RISO bis 500 V inkl. FELV | 500 V DC, mindestens 1 MOhm | Tabelle 6.1 |
| RISO über 500 V | 1000 V DC, mindestens 1 MOhm | Tabelle 6.1 |
| RPE/RLO | mindestens 200 mA bei geeigneter Prüfung | konkrete Geräte-/Anlagennorm prüfen |
| RPE-Grenzwert | kein allgemeiner Pauschalwert | Erwartungswert über Leitung/Widerstand und Kontaktstellen berechnen |
| PE separat mechanisch geschützt (Cu) | unter einschlägigen Bedingungen mindestens 2,5 mm² | nicht mit mehradriger Leitung verwechseln |
| PE separat nicht mechanisch geschützt (Cu) | unter einschlägigen Bedingungen mindestens 4 mm² | nicht mit mehradriger Leitung verwechseln |
| RCD 1 × IΔn | 300 ms als üblicher Gerätegrenzwert für unverzögerte Standard-RCCB | kein pauschaler Ersatz für Schutz-/Netzsystembewertung |
| RCD 5 × IΔn | 40 ms nur in passendem Gerätekontext | z. B. nicht beliebig auf selektive RCD übertragen |

**Besonderer Hinweis zur Normausgabe:** DIN VDE 0100-600:2017-06 ist die bestätigte Grundlage der genannten Tabelle; spätere Entwürfe/Änderungen und Herstellerangaben können relevant sein. Maßgeblich sind jeweils die zum Prüfzeitpunkt geltenden Anforderungen, die Elektrofachkraft und Prüfaufgabe.

## D. Inhaltliche und redaktionelle Lücken der Originaldatei

1. **S. 10:** Abschnitt 2.6 „Sensoren und Aktoren“ enthält keine ausgearbeitete Prüfanleitung.
2. **S. 21:** Kein inhaltlich tragendes Kapitel, obwohl weitere Prüfschritte zu erwarten wären.
3. **S. 23–26:** Lehr-/Druckvorlagen wie Beispiele für Piktogramme, Tabellen, Abbildungen und Notizfelder; nicht als fachliche Prüfschritte missverstehen.
4. **S. 27:** Abkürzungsverzeichnis ist nicht ausgefüllt.
5. **Kein vollständiger Ablauf** von Schutzmaßnahme, RCD/Überstromschutz, Fehlerschleifen-/Netzimpedanz, Drehfeld, Spannungsfall, Steuerungs-/Funktionsprüfung und Abschlussbewertung.
6. **Normmischung:** DIN VDE 0100-600 (Niederspannungsanlagen), DIN EN 60204-1 (elektrische Ausrüstung von Maschinen) und produktbezogene Prüfanforderungen werden im Text wechselnd verwendet. Für einen Prüfgegenstand muss klar sein, **welche Norm für welchen Teil gilt**.
7. **Vorab-/Trainingsfassung:** Die PDF weist selbst ausdrücklich darauf hin, nicht dem Änderungsdienst zu unterliegen. Nicht blind als aktuellen Normvolltext verwenden.

## E. Leitfragen für die AP1

1. Warum beweist eine erloschene Netzteil-LED keine Spannungsfreiheit?
2. Warum muss der Spannungsprüfer vor und nach dem Feststellen getestet werden?
3. Welche drei Angaben benötigst du, um einen erwarteten RPE-Leitungswiderstand zu berechnen?
4. Wieso kann eine fehlerhafte Offset-Einstellung die Bewertung des RPE verfälschen?
5. Warum dürfen nicht alle 24-V-SPS-Stromkreise pauschal mit 500 V geprüft werden?
6. Welche drei Fälle gibt die Isolations-Prüfspannungstabelle an?
7. Warum ist ein Prüfwert oberhalb von 1 MOhm kein Beweis, dass **alle** abgeschnittenen Stromkreisabschnitte geprüft sind?
8. Was ist an „alle Schrauben brauchen 1,2 Nm“ falsch?
9. Welcher Unterschied besteht zwischen gemessenem RCD-Auslösestrom, RCD-Auslösezeit und Netz-Abschaltbedingung?
10. Warum sind 2,5 mm² als PE-Mindestquerschnitt nicht auf jedes fünfadrige Kabel übertragbar?
11. Was dokumentierst du, wenn du wegen angeschlossener SPS einen Teil der RISO-Messung nicht sicher durchführen kannst?
12. Was fehlt dieser PDF für die vollständige DIN-VDE-0100-600-Erstprüfung?

## F. Externe Nachweise und Grenzen dieser Recherche

- **DGUV Sicherheitsregeln/Spannungsprüfer:** https://publikationen.dguv.de/widgets/pdf/download/article/284
- **DKE – Geltungsbereich VDE 0100-600:** https://www.dke.de/de/normen-standards/dokument?id=7089969&type=dke%7Cdokument
- **DKE – Klarstellung Dokumentation 2019:** https://www.dke.de/de/arbeitsfelder/core-safety/normenhinweise/dke-uk-221-1-zu-mindestinhalte-eines-pruefberichts
- **WEKA – Erstprüfung und RISO-Tabellenwerte (2026):** https://www.weka.de/elektrosicherheit/erstpruefung-nach-din-vde-0100-600/
- **DKE – DIN EN IEC 61557-2:** https://www.dke.de/de/normen-standards/dokument?id=7178976&type=dke%7Cdokument
- **IEC-61557-2-Information zu mindestens 1 mA Bemessungsstrom:** https://www.iteh.eu/catalog/standards/iec/686dae8e-7391-4e80-b4cf-5e415e8e0ef7/iec-61557-2-2019
- **WEKA – DIN VDE 0100-540:2024-06, Mindestquerschnitte separat verlegter PE:** https://shop.weka.de/media/?file=media%2Freading-sample%2Fnormen-und-vorschriften-der-elektrotechnik-5915-reading-sample-1.pdf
- **ABB – Fragen zu RCDs, Prüfströmen und Zeiten:** https://new.abb.com/low-voltage/de/produkte/installationsgeraete/fehlerstrom-schutzeinrichtungen/faq
- **DIN Media – Anwendungsbereich EN 50160:** https://www.dinmedia.de/en/standard/din-en-50160/136886057

**Nicht verifiziert:** Genaue betriebliche Prüfverfahren im Ausbildungsbetrieb, konkretes Gossen-MetraWatt-Messgerätemodell vor Ort, aktuelle PAL-Aufgabenformulierung, konkrete Stromlaufplan-Revision und an den Prüfstand angeschlossene Elektronik. Diese Punkte dürfen nicht erfunden oder als geprüft ausgegeben werden.
