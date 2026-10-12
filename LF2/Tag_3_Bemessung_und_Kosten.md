# Tag 3 – Energiebedarf, Leitungsbemessung und Kosten

**Ziel:** Sicher rechnen, Formeln mit Einheiten anwenden, Annahmen erkennen und Auswahlentscheidungen begründen. **Zeit:** ca. 5–7 Stunden mit Pausen.

## Block A – Formelsammlung mit Bedeutung

### 1. Leistung, Strom, Spannung

Für einfache **ohmsche Einphasen-Übungsaufgaben**:

- **P = U · I**, daher **I = P / U** und **U = P / I**.
- P in W, U in V, I in A.
- Bei Wechselstrom mit Leistungsfaktor: **P = U · I · cos φ** (Einphase; vereinfachtes Modell).
- Bei symmetrischem Drehstrom: **P = √3 · U_LL · I_L · cos φ**; Leiterspannung z. B. 400 V.

Beispiel: 1150 W ohmsche Last bei 230 V: I = 1150 / 230 = **5 A**.

### 2. Energieverbrauch und Kosten

- **E = P · t**, dabei P in kW und t in h → E in **kWh**.
- **Stromkosten = E · Arbeitspreis in €/kWh**.

Beispiel: Heizgerät mit 0,8 kW läuft drei Stunden: E = 0,8 · 3 = **2,4 kWh**; bei angenommenen 0,32 €/kWh = **0,77 €** gerundet.

### 3. Leitungswiderstand und Spannungsfall

- **R = ρ · l / A**: l in m, A in mm², ρ in Ω·mm²/m.
- Für unsere Aufgaben nehmen wir Kupfer mit **ρ = 0,0178 Ω·mm²/m bei rund 20 °C** an. Real ändern u. a. Temperatur und Material den Wert.
- Einfaches einphasiges Gleichstrom-/ohmsches Übungsmodell mit Hin- und Rückleiter: **ΔU ≈ 2 · ρ · l · I / A**; hier ist l die **einfache Länge** zur Last.
- Relativ: **ΔU% = (ΔU / U) · 100**.
- Für Wechsel-/Drehstrom und echte Planung können weitere Faktoren (u. a. Leistungsfaktor, Reaktanz, Betriebstemperatur) wichtig sein; unsere vereinfachte Formel ist kein vollständiger normativer Dimensionierungsnachweis.

Beispiel: 25 m (einfach), 10 A, 2,5 mm² Cu: ΔU ≈ 2·0,0178·25·10/2,5 = **3,56 V**. Anteil an 230 V ≈ **1,55 %**.

## Block B – Leitungsdimensionierung als Entscheidungsprozess

**Nicht nur Querschnitt einsetzen:** In realen Anlagen müssen mehrere Bedingungen gleichzeitig erfüllt sein.

1. Verbraucher und Bemessungsstrom **I_B** bestimmen (gleichzeitig anliegende Last beachten).
2. Installationsbedingungen bestimmen: Leitungstyp, Aderzahl, Verlegeart, Temperatur, Häufung, Wärmeisolation, Umgebung.
3. Aus passenden Tabellen und Korrekturfaktoren zulässige Strombelastbarkeit **I_z** bestimmen.
4. Überstromschutz **I_n** auswählen: als grundlegende Auslegungsbeziehung bei Überlast **I_B ≤ I_n ≤ I_z**; ergänzend Abschaltcharakteristik/konventioneller Auslösestrom und weitere normative Bedingungen beachten.
5. Spannungsfall und zulässige Grenzen anhand des konkreten Anwendungsfalls prüfen.
6. Abschaltbedingungen, Kurzschlussstrom, Schutz gegen elektrischen Schlag, mechanische Eignung und ggf. weitere Anforderungen prüfen.
7. Ergebnis mit Angabe der **Annahmen, Tabellen, Leitungslänge, Schutzgerät und Prüfwerte** dokumentieren.

**Prüfungsfalle:** „B16 und 1,5 mm² passt immer“ ist falsch. Ein mit anderen Leitungen gehäufter Stromkreis in Dämmung wird anders bewertet als ein frei verlegter Stromkreis.

## Block C – Installation kalkulieren

**Beispiel (fiktiv, reine Übungswerte):**

| Position | Menge | Einzelpreis netto | Gesamt netto |
|---|---:|---:|---:|
| Steckdosen | 12 | 4,20 € | 50,40 € |
| Schalter | 8 | 7,50 € | 60,00 € |
| Leitung | 65 m | 1,20 €/m | 78,00 € |
| Arbeitszeit | 3,5 h | 48,00 €/h | 168,00 € |
| **Summe netto** | | | **356,40 €** |
| Umsatzsteuer (Übungsannahme 19 %) | | | **67,72 €** |
| **Brutto** | | | **424,12 €** |

Reale Angebote brauchen je nach Aufgabe weitere Positionen: Vorbereitung, Fahrzeit, Zubehör, Klemmen/Verteiler, Materialaufschlag, Entsorgung, Prüfaufwand, Nachweise etc.

## Block D – Übungsaufgaben (10 × 3 Punkte = 30 Punkte)

**Zeige bei jeder Rechnung Formel → Einsetzen → Ergebnis → Einheit.**

1. Ein ohmscher Verbraucher hat P = 920 W an U = 230 V. Berechne I.
2. Ein Verbraucher nimmt I = 6 A bei U = 230 V (cos φ = 1) auf. Berechne P in W.
3. Ein 1,2-kW-Heizgerät läuft 2,5 Stunden. Wie viele kWh verbraucht es?
4. Mit Übungs-Strompreis 0,30 €/kWh: Was kosten die 3,0 kWh aus Aufgabe 3?
5. Berechne im vereinfachten einphasigen Modell den Spannungsfall: Cu, l = 20 m einfach, I = 8 A, A = 2,5 mm², ρ = 0,0178 Ω·mm²/m.
6. Wie groß ist in Aufgabe 5 der relative Spannungsfall bei U = 230 V?
7. Berechne die Wirkleistung einer **symmetrischen Drehstromlast**: U_LL = 400 V, I = 10 A, cos φ = 0,8; verwende √3 ≈ 1,732.
8. Nenne vier reale Bedingungen, die bei der Auswahl eines Leitungsquerschnitts berücksichtigt werden müssen. Erkläre, warum allein P und U nicht genügen.
9. Rechnung: 10 Steckdosen zu 5 € netto, 30 m Leitung zu 2 € netto/m und 2 h Arbeit zu 50 € netto/h. Bestimme die Nettosumme und den Bruttobetrag bei **19 %** Übungssteuersatz.
10. Eine Übungsleitung hat I_B = 13 A, I_n = 16 A, **I_z = 14 A nach allen Korrekturen**. Ist die Überlastbedingung I_B ≤ I_n ≤ I_z erfüllt? Begründe und sage, was du ändern bzw. neu prüfen müsstest.

**Ziel:** mindestens 24/30 Punkte; Rechenweg und Einheiten zählen mit.

## Block E – Zusatzfall (freiwillig, vertiefend)

Eine Leuchte soll in 60 m Entfernung versorgt werden; Laststrom 15 A, zunächst A = 2,5 mm². Rechne den **vereinfachten** Spannungsfall (Kupfer ρ = 0,0178), ermittle Prozent bei 230 V. Diskutiere, warum das Ergebnis **noch keine vollständige Leitungsfreigabe** ist.

## Merkkarten

- **Leistung:** P = U·I (nur bei passender Annahme).
- **Energie:** kW · Stunden = kWh.
- **Leitung:** Ausreichende Strombelastbarkeit, Schutz, Spannungsfall und Umfeld gehören zusammen.
- **Kalkulation:** Positionen netto addieren, danach vereinbarte Steuern berücksichtigen.

**Fortsetzung:** [Tag 4 – Prüfen und Inbetriebnehmen](Tag_4_Pruefung_und_Inbetriebnahme.md).
