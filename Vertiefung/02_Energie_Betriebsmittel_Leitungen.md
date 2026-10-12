# Vertiefung 2 – Energiebedarf, Betriebsmittel, Leitungen und Bemessung

**Ziele:** Kennzeichnungen lesen, Energiebedarf bestimmen, Leitungs-/Schutzorganauswahl begründen, Rechenwege sauber dokumentieren. Reale Bemessung nur auf Basis passender Normen, Herstellerangaben und Tabellenbuch.

## 1. Größen, Einheiten, Rechenregeln

| Größe | Zeichen | Einheit | Bedeutung |
|---|---|---|---|
| Spannung | U | Volt (V) | Potenzialdifferenz |
| Stromstärke | I | Ampere (A) | Strom |
| Wirkleistung | P | Watt (W) | umgesetzte Wirkleistung |
| Energie/Arbeit | E oder W | Wh, kWh | Leistung × Zeit |
| Widerstand | R | Ohm (Ω) | Widerstand |
| Leitungslänge | l | Meter (m) | Länge einfach/gesamt eindeutig festlegen |
| Querschnitt | A | mm² | Leiter-Nennquerschnitt |
| Leistungsfaktor | cos φ | dimensionslos | vereinfacht bei sinusförmigen Vorgängen |

**Ohmsche einphasige Last:** P = U·I, I = P/U. **Allgemeine einphasige sinusförmige Last:** P = U·I·cos φ. **Symmetrischer Drehstrom:** P = √3·U_LL·I_L·cos φ. Bei nichtsinusförmigen Strömen ist die einfache cos-φ-Deutung nur eingeschränkt anwendbar (Leistungsfaktor nicht pauschal mit cos φ gleichsetzen).

**Energie:** E[kWh] = P[kW]·t[h]; Kosten = E·Preis. Watt (Momentanleistung) ist nicht dasselbe wie Kilowattstunde (Energie).

**Gleichzeitigkeit:** Nicht alle angeschlossenen Geräte laufen zwingend gleichzeitig. In Aufgaben wird oft explizit eine Gleichzeitigkeit angenommen oder ein Faktor vorgegeben. **Nie** ohne Annahme blind alle Typenschildleistungen zum Bemessungsstrom umdeuten.

### Durchgerechnetes Beispiel
Drei ohmsche Heizgeräte 400 W, 600 W und 800 W gleichzeitig an **230 V**: P_sum = 1800 W, I = 1800/230 = **7,83 A**. Vier LED mit je 12 W über 5 h: P = 48 W = 0,048 kW, E = 0,048·5 = **0,24 kWh**.

## 2. Typenschilder systematisch lesen

Beispiel fiktives Typenschild: **230 V~, 50 Hz, 120 W, IP44, Schutzklasse II**.
- Spannung für AC und Frequenz ablesen; nicht mit 24-V-DC-Gerät verwechseln.
- 120 W nennt die angegebene Leistung; elektrische Stromaufnahme bei AC ggf. nach Leistungsfaktor bestimmen.
- IP44: Schutz gegen geeignete Fremdkörper-/Spritzwassereinwirkung gemäß Gerätespezifikation, aber **keine universelle Freigabe für alle Außenbereiche**.
- Klasse II: doppelte oder verstärkte Isolierung. Schutzart ≠ Schutzklasse.
- **I_n / U_n / P_n / IΔn** auseinanderhalten; Herstellerdaten und Geräteeignung einbeziehen.

**Ein Gerät ist nur geeignet**, wenn elektrische Werte, Montagebedingungen, Schutzkonzept, Schalt-/Einschaltstrom, Erwärmung, Umgebung und Wirtschaftlichkeit passen. Ein niedriger Kaufpreis allein genügt nicht.

## 3. Leiter, Adern, Kabel, Typen, Farben

- Ader = einzelner isolierter Leiter; Leitung/Kabel = je nach Bauart für bestimmte Verlegung und Beanspruchungen geeignet.
- **NYM-J 3×1,5 mm²** = Installationsleitung mit grün-gelbem Schutzleiter, drei Adern mit je 1,5 mm²; *kein universeller B16-Nachweis*.
- **NYM-J 5×2,5 mm²** = fünf Adern mit je 2,5 mm²; Anzahl und Verwendung nach Auftrag/Plan.
- **H07V-U** = bestimmte Einzelader für zulässige geschützte Verlegung, z. B. passender Kanal/Rohr.
- **N** üblicherweise **blau**, **PE** grün-gelb, **L1–3** oft braun/schwarz/grau; Leiterkennzeichnung und Funktion anhand Unterlagen prüfen. Nie aus einer Farbe allein die Spannungsfreiheit ableiten.
- **PEN** nur bei entsprechend zulässigem Aufbau/Querschnitten/Regeln, keinesfalls beliebig aus N und PE „machen“.

## 4. Installationstechnik und Leitungswege

**Aufputz:** zugängliche Installation, sichtbare Rohre/Kanäle, ggf. in Industrieumgebung. **Unterputz:** Leitungen im Mauerwerk unter Einhaltung dafür geltender Regeln. **Kabelrinne:** mehrere Leitungen in geeigneter Trasse. **Installationsrohr/-kanal:** mechanische Führung, elektrische und thermische Anforderungen beachten.

**Installationszonen:** In Wohnungen gibt es vorgesehene Leitungsführungszonen, insbesondere waagerechte/vertikale Bereiche. Genaue Maße und Ausnahmen im **aktuellen Tabellenbuch / einschlägigen Normen** kontrollieren. Nicht unbesehen horizontal und diagonal Leitungen ziehen.

**Übungsfrage:** Warum könnten bei zwei ansonsten gleichen 1,5-mm²-Leitungen **unterschiedliche** Schutzorgane benötigt werden? Weil Wärmeabgabe/Belastbarkeit sich mit Verlegeart, Temperatur, Häufung und Randbedingungen ändert.

## 5. Strombelastbarkeit und Leitungsauswahl

**Entscheidung in richtiger Reihenfolge:**

1. Lasten/Gleichzeitigkeit → Bemessungsstrom **I_B**.
2. Leitungstyp, Aderzahl und Leiterwerkstoff festlegen.
3. Montage-/Verlegeart, Häufung, Temperatur, wärmegedämmte Abschnitte, Zahl belasteter Leiter erfassen.
4. Relevante Tabellen und Korrekturfaktoren nutzen → korrigierte zulässige Strombelastbarkeit **I_z**.
5. Passenden Schutz **I_n** festlegen; grundlegende Bedingung **I_B ≤ I_n ≤ I_z** (zusätzliche normgerechte Überlastanforderung an Auslöseverhalten beachten).
6. Spannungsfall prüfen.
7. Schutz gegen elektrischen Schlag, automatische Abschaltbedingungen, Kurzschluss und weitere Anforderungen prüfen.
8. Bemessung und Quellen dokumentieren.

**Gefährlicher Denkfehler:** „Eine Leitung mit 1,5 mm² darf immer mit 16 A abgesichert werden.“ **Falsch**.

### Spannungsfall (vereinfachte Übungsaufgaben)

Mit **ρ_Cu = 0,0178 Ω·mm²/m** bei ungefähr 20 °C und **einfacher Leitungslänge** l:

- R = ρ·l/A für **einen** Leiter.
- Für einen einfachen einphasigen, ohmschen Stromkreis mit Hin- und Rückleiter: **ΔU ≈ 2·ρ·l·I/A**.
- ΔU% = ΔU/U·100.

**Beispiel:** l = 30 m einfach, I = 12 A, A = 2,5 mm²: ΔU = 2·0,0178·30·12/2,5 = **5,1264 V**; bei 230 V → **2,23 %**.

**WICHTIG:** Reale Leitung wird wärmer; Wechsel-/Drehstrom, Leitungsreaktanz, Verlege- und Abschaltbedingungen können die Bemessung ändern. Ein kleiner Spannungsfall **allein** macht eine Anlage nicht automatisch sicher.

## 6. Energie, Wirtschaftlichkeit und Ökologie

- **Betriebskosten:** kWh × Preis berechnen (Werte aus Aufgabe).
- **Wirkungsgrad/Verluste:** Ein sparsameres Gerät kann trotz höherem Anschaffungspreis wirtschaftlicher sein.
- **Umwelt:** sinnvoll dimensionieren, Material und Leitungsabfälle minimieren, geeignete langlebige Komponenten, geltende Entsorgungspflichten beachten.

## 7. Üben (mit Formeln, Einheiten, Begründung)

1. 1200-W-Heizung bei 230 V ohmsch: I?
2. 5 LED à 18 W laufen 8 Stunden: E in kWh?
3. E aus Aufgabe 2 zu 0,29 €/kWh: Kosten?
4. Symmetrischer Drehstrom: 400 V, 8 A, cos φ = 0,85: Wirkleistung?
5. Cu: 20 m einfach, 9 A, 1,5 mm², ρ = 0,0178: ΔU in V und % von 230 V?
6. Gegeben I_B=12 A, I_n=16 A, I_z=15 A: Ist die Überlast-Grundbedingung erfüllt?
7. Nenne 6 Bedingungen für eine reale Querschnittsauswahl und begründe zwei.
8. Warum ist ein Typenschild mit IP54 **keine** Information über die Schutzklasse?
9. Welche Leitungsart kann in deinem Tabellenbuch für eine geeignete Verlegung in Installationsrohr vorgesehen sein? Erkläre, warum „die Ader einfach frei verlegen“ nicht automatisch zulässig ist.
10. Fünf Leuchten à 20 W werden zu zwei unabhängigen Gruppen aufgeteilt: Welche Angaben fehlen für einen vollständigen Energiebedarfs- und Materialplan?

**Transfer:** Fertige eine Tabelle mit vorgegebenen Anlagenlasten, Gleichzeitigkeit, U, I, Schutzkonzept, Leitungsweg, Querschnitt und offenen Nachweisen an. Ein Häkchen ohne Begründung zählt nicht als verstanden.

[Zurück zum Kursplan](../00_START_HIER_LF2_VOLLSTAENDIG.md).
