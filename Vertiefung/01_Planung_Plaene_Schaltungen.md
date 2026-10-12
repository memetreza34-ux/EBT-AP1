# Vertiefung 1 – Auftrag, Installationspläne und alle wichtigen Schaltungsarten

## Lernziele

Am Ende kannst du einen Installationsauftrag in Einzelanforderungen zerlegen, geeignete Pläne unterscheiden und aus **Schaltorten**, **Leuchtengruppen** und **Betriebsverhalten** die passende Schaltung wählen und auf Papier als normgerechte Skizze aus dem Tabellenbuch entwickeln.

### 1. Vom Kundenwunsch zum technisch prüfbaren Auftrag

**Beispiel:** „In der Montagehalle sollen zwei LED-Leuchtengruppen unabhängig bedient werden, und zwar jeweils vom Eingang und vom Ausgang. An der Werkbank wird zusätzlich eine Steckdose benötigt.“

Vor dem Planzeichnen sechs Fragen klären:
1. Wo genau sollen Schalter, Leuchten und Steckdose sitzen? Raumplan, Installationszonen, Aufputz/Unterputz.
2. Welche **Funktionen** sollen möglich sein? Hier **zwei getrennte Leuchtengruppen**, je **zwei Bedienorte**.
3. Welche Verbrauchsdaten: U, P, Nennstrom, Einschaltströme, Umgebungsbedingungen?
4. Welche bestehende Verteilung, Netzform, Reserve, Schutzorgane und Leitungswege gibt es?
5. Welche Sicherheits-, Brandschutz-, Feuchte-/IP- und Betriebsanforderungen sind vorhanden?
6. Wer stimmt mit anderen Gewerken ab? Wer darf errichten, prüfen und freigeben?

**Wichtig:** Eine Schaltung ist nicht nach „Anzahl Lampen = Anzahl Schalter“ auszuwählen. Eine Leuchtengruppe kann aus beliebig vielen gemeinsam geschalteten Leuchten bestehen. Bei **zwei getrennt schaltbaren Gruppen mit zwei Bedienorten** ist die Lösung nicht die einfache Standard-Serienschaltung (die bedient zwei Gruppen normalerweise **an einem** Ort). Eine mögliche konventionelle Lösung sind zwei unabhängige Wechselschaltungen oder eine passende Mehrkanalsteuerung.

### 2. Stromkreis, Schaltstelle und Leuchtengruppe

- **Stromkreis:** elektrisch durch Schutz-/Schaltorgane abgegrenzter Versorgungsbereich.
- **Schaltstelle/Bedienort:** ein Ort, von dem aus ein bestimmtes Licht geschaltet werden kann.
- **Leuchtengruppe:** eine oder mehrere zusammen geschaltete Leuchten.
- **Unabhängige Leuchtengruppen:** z. B. vorderes und hinteres Licht getrennt bedienbar.
- **Kontakt:** Verbindung, die abhängig vom Schaltzustand geöffnet/geschlossen wird.
- **Wechslerkontakt:** Umschalter mit gemeinsamem Anschluss und zwei Wahlkontakten.
- **Schließer/Öffner:** Kontakt ist im definierten Grundzustand offen bzw. geschlossen (Grundstellung beachten).

**Mini-Beispiel:** 5 Lampen werden gemeinsam von 3 Türen aus bedient: **eine Gruppe**, **drei Orte** → klassische Kreuzschaltung.

### 3. Fachgerechte Planarten unterscheiden

| Plan | Frage, die er beantwortet | Typische Inhalte |
|---|---|---|
| Grundriss-/Installationsplan | Wo montieren und verlegen? | Raumwände, Montageorte, Trassen, Kennzeichnungen |
| Stromlaufplan (zusammenhängend) | Wie hängt die Funktion elektrisch zusammen? | Kontakte, Verbraucher, Leitungen, Verbindungslinien |
| Stromlaufplan (aufgelöst) | Welche Funktionszusammenhänge bestehen? | Strompfade, Steuer-/Leistungsebene, Querverweise |
| Einpoliger Übersichtsschaltplan | Wie sind Verteilung und Stromkreise gegliedert? | Netz, Hauptschalter, Schutzorgane, Abgänge |
| Anschluss-/Verdrahtungsplan | Welche konkrete Klemme und Ader wohin? | Anschlusskennzeichen, Leiter, Klemmen |
| Klemmenplan | Welche außenliegenden Verbindungen sind auf welcher Klemme? | Klemmenleiste, Nummern, Anschlusspunkte |

**Aufgabe:** Zeichne denselben Flur als (a) Grundriss, (b) Funktions-Stromlaufplan und (c) Liste mit zu kennzeichnenden Anschlussstellen. Prüfe die grafischen Symbole **im aktuellen Tabellenbuch**. Die hier beschriebenen Texte sind **keine** normgerechten Installationszeichnungen.

### 4. Die Schaltungsfamilie – sorgfältig vergleichen

**Ausschaltung:** Ein gewöhnlicher rastender Schalter bedient **eine** Leuchtengruppe von **einem** Ort. Ein einfacher Strompfad lässt sich funktional als L → Schaltkontakt → Verbraucher → N verstehen. Bei einem Gerät der Schutzklasse I ist PE als Schutzanschluss zu berücksichtigen, nicht Teil des normalen Laststromkreises.

**Serienschaltung (Installationsbegriff):** Zwei unabhängig schaltbare Gruppen von **einem** Bedienort, oft über eine zweigeteilte Schalterwippe. Der Begriff „Serie“ bedeutet **nicht**, dass Leuchten elektrisch in Reihe betrieben werden!

**Wechselschaltung:** **Eine** Gruppe, **zwei** Orte. Zwei Wechselschalter, zwei Korrespondierende im klassischen Prinzip. Jeder Bedienvorgang **an einem der beiden Umschalter** kehrt den Lichtzustand um. **Kein** Schutzleiter wird als Korrespondierender benutzt.

**Kreuzschaltung:** **Eine** Gruppe, **mindestens drei** Orte; zwei Wechselschalter an den Enden, dazwischen **ein Kreuzschalter pro zusätzlicher Schaltstelle**. Kreuzschalter tauscht die beiden korrespondierenden Verbindungswege. Bei 5 Orten konventionell: **2 Wechselschalter + 3 Kreuzschalter**.

**Taster + Stromstoßschalter:** Der Taster ist nicht rastend; er gibt einen Impuls an ein passendes Schaltgerät. Mehrere Taster können von vielen Orten dieselbe Gruppe bedienen. Ein geeigneter Stromstoßschalter wechselt bei jedem Impuls den Zustand (modell-/konfigurationsabhängig).

**Taster + Treppenlichtautomat:** Die Beleuchtung wird nach Tastendruck **zeitabhängig** automatisch wieder abgeschaltet. Verwechslung mit Stromstoßfunktion = häufige konzeptuelle Fehlentscheidung.

**Kontroll-/Orientierungslicht am Schalter:** Funktion muss aus der Aufgabe hervorgehen. Nicht allein wegen einer Leuchtanzeige eine falsche Schaltungsart wählen.

**Dimmen/Bewegungsmelder/Smart-Aktor:** Nach Aufgabenanforderung mögliche Alternative; Kompatibilität mit LED-Treiber, Leitungskonzept, Energieverbrauch, Umgebungsbedingungen und Herstellervorgaben beachten. Sie ersetzen nicht die Grundkenntnisse der klassischen Schaltungen.

### 5. Auswahl-Schnellalgorithmus

1. Wie viele **unabhängige** Gruppen sollen geschaltet werden?
2. Von wie vielen **Orten** soll **jede Gruppe** schaltbar sein?
3. Soll nach **Zeit**, **Bewegung** oder manuell geschaltet werden?
4. Werden **rastende Schalter** oder **Taster** vorgeschrieben?
5. Ist die Auswahl für Leistung, Schutz, Montage und Norm geeignet?

**Beispiellösungen:**
- 2 Lampen zusammen, 2 Stellen → **eine Wechselschaltung**.
- 2 Lampen getrennt, 1 Stelle → **eine Serienschaltung** bzw. zwei Ausschalter.
- 2 Lampen getrennt, 2 Stellen → **zwei Wechselschaltungen** oder gleichwertige geeignete Steuerung.
- 1 Gruppe, 4 Stellen → **zwei Wechsel + zwei Kreuz** (klassisch).
- 1 Gruppe, 8 Taster, jeder Impuls umschalten → **passender Stromstoßschalter**.
- Treppenhaus, nach 2 min automatisch aus → **passender Treppenlicht-Zeitautomat**.

### 6. Lesen, Zeichnen, Prüfen

**Bei einer Planzeichenaufgabe:** (a) Angaben markieren, (b) Funktion benennen, (c) Leiter und Betriebsmittel mit Kennzeichen notieren, (d) Strompfade logisch durchgehen, (e) Schalterstellungen als Zustandstabellen überprüfen, (f) eigene Darstellung mit Tabellenbuchsymbolen vergleichen.

**Tabelle für eine Wechselschaltung:** Entscheidend ist, ob die zwei Wechselschalter einen durchgängigen Weg über **dieselbe Korrespondierende** wählen. Treffen die Verbindungen funktional zusammen → Strompfad geschlossen; sind verschiedene Wege gewählt → unterbrochen.

**Merksatz:** Ein echter **Schaltplan** zeigt elektrische Funktionen, ein **Installationsplan** Orte und Leitungswege.

### 7. Üben (zuerst ohne Lösung)

1. Im Lager: 4 gemeinsam geschaltete Leuchten, Bedienort nur an der Tür. Welche Schaltung?
2. Flur mit 4 Türen und **zwei** unabhängig bedienbaren Lichtgruppen. Welche Schaltanforderungen existieren? Ist „eine Kreuzschaltung“ als Antwort vollständig?
3. Zwei Wippen an einer Stelle schalten je eine Gruppe. Wie heißt die typische Installationstechnik?
4. Eine Leuchte soll beim Tastendruck 90 Sekunden laufen. Stromstoßrelais oder Treppenlichtautomat?
5. Nenne zwei Unterschiede zwischen Grundriss/Installationsplan und Stromlaufplan.
6. Weshalb kann eine neue Steckdose nicht einfach unbesehen zur bestehenden Beleuchtungssteuerung „dazugezeichnet“ werden?
7. Zeichne jeweils einen *funktionalen* Grundplan für Aus-, Wechsel- und Kreuzschaltung mit Symbolen aus deinem Tabellenbuch.
8. Erkläre, wann zwei korrespondierende Leiter verwendet werden und welche Funktion PE ausdrücklich **nicht** übernimmt.
9. Zwei Leuchtengruppen sollen an **drei** Stellen getrennt geschaltet werden. Erkläre, warum du jede Gruppe separat planen musst.
10. Schreibe fünf notwendige Rückfragen an den Kunden des Beispielauftrags zu Beginn dieses Skripts.

**Erfolgskriterium:** Du kannst die Schaltungsart begründen und **selbst zeichnen**, nicht nur richtig ankreuzen.

[Zurück zum Kursplan](../00_START_HIER_LF2_VOLLSTAENDIG.md).
