# Tag 1 – Installationsschaltungen verstehen, auswählen und zeichnen

**Ziel:** Nicht nur Schalternamen auswendig lernen: Zu einem Auftrag entscheiden können, welche Schaltung benötigt wird, wie sie funktioniert und wie sie dokumentiert wird.  
**Arbeitsmittel:** Papier (kariert), Stift, Taschenrechner bei Bedarf, Tabellenbuch.  
**Zeitbedarf:** ca. 5–7 intensive Stunden mit Pausen.  
**Sicherheit:** Alle Aufgaben sind **theoretisch**. Schaltungen nicht an 230-V-Anlagen ausprobieren.

## Block A – Grundlagen, die sitzen müssen

### 1. Die Leiter und ihre Aufgaben

| Kennzeichnung | Aufgabe | übliche Farbe in aktuellen Anlagen |
|---|---|---|
| L bzw. L1/L2/L3 | Außenleiter, führt im Betriebszustand Spannung | braun/schwarz/grau (Zuordnung nach Installation) |
| N | Neutralleiter, betriebsmäßiger Rückleiter | blau |
| PE | Schutzleiter, Schutz bei einem Fehler; kein normaler Betriebsstrompfad | grün-gelb |

**Denkmodell einer Lampe:** In einem einfachen einphasigen Stromkreis verläuft die Versorgung funktional über L → Schaltkontakt → Leuchte → N; der PE hat eine **Schutzfunktion** und darf nicht als Rückleiter missbraucht werden. Ein gewöhnlicher Lichtschalter unterbricht im Regelfall den Außenleiter, nicht den Schutzleiter. Leuchten der Schutzklasse I müssen vorschriftsmäßig mit PE verbunden sein; bei Schutzklasse II ist das anders.

**Kontrollfragen:** Welche Aufgabe hat der PE? Warum wäre es gefährlich, den PE als geschalteten Leiter zu verwenden? Worin unterscheiden sich Neutral- und Schutzleiter?

### 2. Technische Zeichnungen: drei Blickwinkel

- **Installationsplan:** Wo sind Leuchten, Schalter, Steckdosen und Leitungswege im Gebäude? Meist Grundriss.
- **Stromlaufplan:** Wie sind die Betriebsmittel elektrisch verbunden und wie funktioniert die Schaltung? Je nach Aufgabenstellung in zusammenhängender oder aufgelöster Darstellung.
- **Verdrahtungs-/Anschlussplan:** Welche konkrete Klemme bzw. Ader wird mit welcher Gegenstelle verbunden?
- **Klemmenplan:** Welche Klemmen gehören zu welchen externen Anschlüssen?

**Merksatz:** Installationsplan = *wo?* Stromlaufplan = *wie funktioniert es?* Anschlussplan = *welcher Anschluss wohin?*

Lerne die genormten grafischen Symbole aus deinem Tabellenbuch. Die Textmodelle unten erklären die Funktion, **ersetzen keine normgerechten Montagepläne**.

## Block B – Sechs Schaltungsarten

### 3. Ausschaltung: 1 Leuchte / Leuchtengruppe, 1 Bedienstelle

- Ein Schalter schaltet eine Leuchte (oder gemeinsam geschaltete Gruppe) EIN/AUS.
- Funktional: **L → Schalter → Leuchte → N**.
- Beispiel: einzelne Deckenleuchte im Abstellraum.
- Die Zahl der gleichzeitig geschalteten Leuchten bestimmt nicht die Zahl der Bedienstellen.

### 4. Serienschaltung: 2 Gruppen unabhängig von 1 Bedienstelle

- **Serienschalter** enthält zwei unabhängig betätigbare Schaltfunktionen.
- Ein gemeinsamer Einbauort mit zwei Wippen, um z. B. Deckenbeleuchtung und Wandbeleuchtung unabhängig zu schalten.
- **Achtung:** „Serienschaltung“ ist hier eine historische Bezeichnung in der Installationstechnik. Die Leuchten sind **nicht elektrisch in Reihe geschaltet**. Beide Gruppen werden parallel zur Versorgung separat geschaltet.

### 5. Wechselschaltung: 1 Leuchtengruppe, 2 Bedienstellen

- An jedem von **zwei Orten** lässt sich dieselbe Leuchte umschalten.
- Zwei Wechselschalter (Umschaltkontakte) bilden eine klassische Lösung.
- Funktionsmodell: L an den gemeinsamen Anschluss des ersten Wechselschalters; **zwei korrespondierende Leiter** zwischen den Umschaltern; gemeinsamer Anschluss des zweiten zum geschalteten Leuchtenleiter; N zur Leuchte. **Nur ein Prinzipbild, kein Verdrahtungsauftrag.**
- Beim Betätigen **eines beliebigen** Schalters ändert sich der Zustand der Leuchte.
- Beispiel: Flur mit einer Tür am Anfang und am Ende.

**Verständnisübung:** Zeichne zwei Schalterkästchen mit je einem „gemeinsamen“ Anschluss C sowie Kontaktweg 1 und Kontaktweg 2. Zeichne die beiden möglichen Korrespondierenden. Markiere, in welchen Kontaktstellungen ein durchgehender Stromweg besteht.

### 6. Kreuzschaltung: 1 Gruppe, 3 oder mehr Bedienstellen

- Für **drei Stellen** klassisch: Wechselschalter – Kreuzschalter – Wechselschalter.
- Ein Kreuzschalter vertauscht die beiden korrespondierenden Stromwege („gerade“ oder „gekreuzt“).
- Für **vier Stellen** klassisch: zwei Wechselschalter an den Enden und **zwei Kreuzschalter dazwischen**.
- Merke: Zwei Wechselschalter an den Enden; für jede zusätzliche Schaltstelle zwischen den Enden ein Kreuzschalter.
- Beispiel: langer Flur mit drei Türen. Nicht mit „3 Leuchten“ verwechseln.

### 7. Taster + Stromstoßschalter: flexible Mehrstellenbedienung

- Ein **Taster** kehrt durch Federwirkung nach Betätigung in die Ausgangsstellung zurück.
- Mehrere Taster können die Ansteuerung eines geeigneten Stromstoßschalters auslösen; dessen Schaltkontakt übernimmt den Laststromkreis.
- Nützlich bei vielen Schaltstellen: jeder Impuls schaltet den Zustand (je nach Gerät und Konfiguration) um.
- **Unterscheide** vom Treppenlicht-Zeitrelais: Dieses schaltet die Beleuchtung meist nur für eine festgelegte Zeit ein und später automatisch aus.
- Eine **Kontrollschaltung** / Beleuchtung des Schalters ist wieder ein anderes Thema; aus der Aufgabenstellung und den verwendeten Schaltertypen ableiten.

### 8. Steckdosen und Schaltung – nicht durcheinanderbringen

- Zwei zusätzliche Steckdosen ändern eine Wechselschaltung nicht zu einer Kreuzschaltung.
- Prüfe in Aufträgen immer separat: **Wie viele Leuchten(gruppen)? Wie viele unabhängige Gruppen? Von wie vielen Orten schalten? Welche Steckdosen?**
- Steckdosenversorgung und Beleuchtungssteuerung sind planerisch separat zu betrachten (Stromkreise und Schutzvorkehrungen nach Aufgabe).

## Block C – Auswahlmatrix

| Auftragssituation | Typische Lösung |
|---|---|
| 1 Gruppe, 1 Stelle | Ausschaltung |
| 2 Gruppen unabhängig, 1 Stelle | Serienschaltung / 2 getrennte Schalter |
| 1 Gruppe, 2 Stellen | Wechselschaltung |
| 1 Gruppe, 3 Stellen | Kreuzschaltung (2 Wechsel + 1 Kreuz) |
| 1 Gruppe, 4 Stellen | Kreuzschaltung (2 Wechsel + 2 Kreuz) |
| 1 Gruppe, viele Stellen; Taster gewünscht | Taster + Stromstoßschalter |
| 1 Gruppe mit automatischer Abschaltung | z. B. Taster + Treppenlicht-Zeitrelais |

**Wichtig:** Das ist eine Schaltungswahl-Tabelle und keine Vorschrift, dass ausschließlich genau diese Technik zulässig ist. Bei automatisierten oder smarten Anlagen können andere Lösungen sinnvoll sein.

## Block D – Aufgaben ohne Hilfestellung

*Schreibe deine Antworten in ein Heft. Die Musterlösungen stehen separat unter `Loesungen/Tag_1_Loesungen.md` – erst danach öffnen.*

### Teil 1: Fachwissen (je 2 Punkte)

1. Erkläre in einem Satz den Unterschied zwischen **N** und **PE**.
2. Was zeigt ein Installationsplan, was ein Stromlaufplan?
3. Warum spricht man bei zwei unabhängig geschalteten Leuchtengruppen vom **Serienschalter**, obwohl die Lampen nicht in Reihe sind?
4. Wozu dienen bei der klassischen Wechselschaltung die **Korrespondierenden**?
5. Worin unterscheidet sich ein Taster von einem rastenden Schalter?
6. Was ist der funktionale Unterschied zwischen Stromstoßschalter und Treppenlicht-Zeitrelais?

### Teil 2: Welche Schaltung? (je 2 Punkte)

7. Eine Leuchte im Keller soll nur an der Tür geschaltet werden.
8. Im Wohnzimmer sollen Deckenlicht und Wandlicht von einem Bedienplatz unabhängig schaltbar sein.
9. Ein Flur hat einen Lichtschalter an jedem Ende.
10. Ein Flur hat drei Türen. Von jeder Tür aus soll das **gleiche** Licht EIN/AUS geschaltet werden.
11. Eine lange Halle hat sechs Taster; jede Betätigung soll dieselbe Leuchtengruppe abwechselnd EIN und AUS schalten.
12. Treppenhaus: Taste drücken, Beleuchtung geht automatisch nach einer definierten Zeit aus.

### Teil 3: Zeichnen und Anwenden (je 4 Punkte)

13. Zeichne auf Papier das **Funktionsprinzip** einer Ausschaltung (L, Schaltkontakt, Lampe, N, PE als Schutzverbindung bei SK I). Beschrifte alle Leiter.
14. Zeichne das Prinzip einer **Wechselschaltung** mit zwei Wechselschaltern und zwei Korrespondierenden. Erkläre schriftlich die Zustandsänderung bei einer Schalterbetätigung.
15. Planungsauftrag: **zwei Lampen gemeinsam**, **zwei Schaltorte**, zusätzlich **zwei Steckdosen**. Nenne die Schaltung; begründe, warum nicht Kreuz- oder Serienschaltung erforderlich ist. Liste auf, was du vor einer realen Installation zusätzlich klären musst (mindestens vier Punkte).

**Gesamt:** 12 + 12 + 12 = **36 Punkte**. Ab **29 Punkten** (~80 %) gilt das Lernziel für den Einstieg als erreicht; nicht die offizielle IHK-Bewertung.

## Block E – 10-Minuten-Transfer

Beantworte ohne Nachschauen:
- 1, 2, 3, 4 Schaltorte: Welche klassische Schaltung?
- Woran erkenne ich einen Taster?
- Was bedeutet „Serien“ bei einem Serienschalter?
- Was unterscheidet N und PE?

Wenn du eine Antwort nur geraten hast, markiere sie gelb im Fehlerprotokoll. Wenn du die Begründung sauber geben kannst, markiere sie grün.

## Merkkarte

**1 Stelle = Ausschaltung. 2 Stellen = Wechsel. 3+ Stellen = Wechsel + Kreuz dazwischen. Mehrere Leuchtengruppen getrennt an 1 Stelle = Serienschaltung. Viele Taster = häufig Stromstoß oder Zeitrelais je nach gewünschter Funktion.**

**Fortsetzung:** [Tag 2 – Leitungen und Schutz](Tag_2_Leitungen_und_Schutz.md).
