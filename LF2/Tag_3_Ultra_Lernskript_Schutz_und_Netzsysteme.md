# TAG 3 – ULTRA-LERNSKRIPT
## Lernfeld 2 · Schutzmaßnahmen, Netzsysteme, RCD, LS und Sicherheit
**Elektroniker/in für Betriebstechnik · AP1-Lernskript · 14. Oktober 2026**

> **Ziel:** Ein vollständiges Nachschlageheft für die Theorie und für das Verständnis typischer praktischer Installationsaufgaben. Die acht Lektionen stehen in derselben Reihenfolge wie in der heutigen Lerneinheit.

> **Sicherheit:** Die Schaubilder sind vereinfachte Prinzipskizzen und **keine Anschlussanleitungen**. Arbeiten an elektrischen Anlagen und Messungen erfolgen im zulässigen Ausbildungsrahmen unter Aufsicht einer Elektrofachkraft. Vor Inbetriebnahme gelten die vorgeschriebenen Prüfungen.

# Inhalt
1. Netzsysteme: TN-S, TN-C, TN-C-S, TT und IT
2. FI-Schutzschalter (RCD): Aufbau, Ringkern, Messwicklung, Kennwerte
3. Leitungsschutzschalter: Bimetall, Magnetspule, Kennlinien
4. Überlast, Kurzschluss, Körperschluss und Leitungsschutz
5. Schutz gegen elektrischen Schlag, Schutzklassen, SELV/PELV/FELV
6. IP-Schutzarten, Erdung, PE und Schutzpotentialausgleich
7. Praxisfälle: geeignete Schutzmaßnahmen auswählen
8. AP1-Wiederholung: Prüfungsfragen und Lösungen
9. Formelblatt, Schaltzeichen-/Abkürzungsverzeichnis und Lernstand

---

# LEKTION 1 – Die fünf Netzsysteme

## 1.1 Was verraten die Buchstaben?
- **T an erster Stelle:** Ein Punkt der Stromquelle ist direkt geerdet.
- **I an erster Stelle:** Die Stromquelle ist gegen Erde isoliert oder nur über eine hohe Impedanz geerdet.
- **N an zweiter Stelle:** Die Körper der Betriebsmittel sind mit dem geerdeten Punkt der Quelle verbunden.
- **T an zweiter Stelle:** Die Körper sind unabhängig von der Quellenerdung geerdet.
- **S:** Schutzleiter PE und Neutralleiter N sind getrennt.
- **C:** Schutz- und Neutralleiterfunktion sind in einem PEN kombiniert.

**Wichtige Leiter:**
- **L1, L2, L3:** Außenleiter.
- **N:** Neutralleiter, führt im Betrieb Rückstrom.
- **PE:** Schutzleiter, normalerweise kein Betriebsstrom.
- **PEN:** Vereint PE- und N-Funktion. Sein Ausfall ist besonders gefährlich.

## 1.2 Vergleichstabelle

| System | Leiterführung / Erdung | Fehlerstromweg / Besonderheit |
|---|---|---|
| **TN-S** | PE und N durchgehend getrennt | Körper über PE metallisch mit geerdeter Quelle verbunden. |
| **TN-C** | PE und N als PEN kombiniert | PEN führt Betriebsstrom; RCD im TN-C-Abschnitt nicht zulässig. |
| **TN-C-S** | Zuerst PEN, nach Aufteilung getrennte PE/N | Nach der PEN-Aufteilung niemals wieder N und PE verbinden. |
| **TT** | Quelle geerdet; Körper über eigenen Erder geerdet | Fehlerstromweg verläuft auch über Erder/Erdreich; RCD normalerweise nötig. |
| **IT** | Quelle von Erde isoliert oder hochohmig geerdet | Bei erstem Isolationsfehler kann Betrieb unter Bedingungen fortgesetzt werden; IMD überwacht. |

## 1.3 TN-S
Der Transformator hat einen geerdeten Punkt. Das Gehäuse eines Geräts der Schutzklasse I ist über PE mit diesem Punkt verbunden. Berührt L das Gehäuse, fließt der Fehlerstrom auf einem überwiegend metallischen Weg zurück. Der Widerstand ist häufig klein; deshalb kann der Fehlerstrom hoch genug sein, damit LS oder eine andere geeignete Schutzeinrichtung rechtzeitig auslöst.

**Nicht verwechseln:** TN-S bedeutet nicht, dass ein FI grundsätzlich unnötig ist. Für zahlreiche Steckdosen und andere Anwendungen wird ein 30-mA-RCD zusätzlich gefordert.

## 1.4 TN-C
N und PE sind zu einem **PEN** kombiniert. Ein PEN darf nicht wie ein gewöhnlicher aktiver Leiter geschaltet oder abgesichert werden. Eine PEN-Unterbrechung kann zu gefährlichen Berührungsspannungen führen. Ein RCD kann nicht im TN-C-Abschnitt mit gemeinsamem PEN eingesetzt werden.

Typische Mindestquerschnitte eines PEN in fester Installation unter den einschlägigen Voraussetzungen: **10 mm² Kupfer oder 16 mm² Aluminium**. Das sind keine allgemeinen Mindestquerschnitte für jeden PE.

## 1.5 TN-C-S
Ein PEN kommt an und wird an einer geeigneten Stelle in **PE** und **N** getrennt. Dahinter werden beide Leiter separat geführt. **Einmal aufgeteilt, niemals erneut verbinden.** Andernfalls könnten Betriebsströme über PE fließen; Schutz- und FI-Funktion werden beeinträchtigt.

## 1.6 TT – warum normalerweise FI?
Fehler: Der Außenleiter berührt ein Metallgehäuse.

**Fehlerstromweg:**
**L → Gehäuse → PE → Gebäudeerder → Erdreich → Transformatorerder → geerdeter Quellpunkt**.

Der Stromkreis besitzt oft einen relativ hohen Widerstand. Dadurch könnte beispielsweise nur ein kleiner Fehlerstrom fließen. Ein **B16-LS** würde bei 2 A nicht abschalten, obwohl das Gehäuse eine gefährliche Spannung haben kann. Ein geeigneter **RCD** erkennt jedoch, dass ein Teil des Stroms nicht durch die überwachten aktiven Leiter zurückkehrt.

**Wichtig:** Der RCD hilft nicht dabei, dass der LS auslöst. **Der RCD schaltet selbst ab.**

Zusammenhang im TT-System: Die Erdungsbedingungen und der Bemessungsdifferenzstrom müssen die Schutzanforderung erfüllen, vereinfacht **R_A × I_Δn ≤ U_L**, wobei die tatsächliche Bewertung nach Norm und Anwendungsfall erfolgt.

## 1.7 IT – erster und zweiter Fehler
Die Quelle ist nicht direkt geerdet (oder hochohmig geerdet). Beim **ersten Isolationsfehler** kann der Fehlerstrom klein sein; die Versorgung darf in geeigneten IT-Anlagen unter den vorgeschriebenen Bedingungen weiterlaufen.

Ein **Isolationsüberwachungsgerät (IMD)** meldet den Verschlechterungszustand der Isolation. Die Ursache muss beseitigt werden. Beim **zweiten Fehler** können gefährliche Fehlerströme entstehen; die vorgeschriebene Abschaltung ist sicherzustellen. Typische Anwendungen finden sich in Anlagen mit hohen Anforderungen an Versorgungskontinuität, etwa bestimmten medizinischen Bereichen.

**AP1-Merksätze:**
- TN: metallischer Fehlerstromweg zur Quelle.
- TT: Fehlerstromweg auch über Erdreich, gewöhnlich RCD.
- IT: Isolationsüberwachung, erster Fehler nicht zwingend sofortige Abschaltung.

---

# LEKTION 2 – FI-Schutzschalter (RCD)

## 2.1 Aufgabe
FI = Fehlerstromschutzschalter; internationale Bezeichnung **RCD (Residual Current Device)**. Er erkennt einen **Differenzstrom**: Die vorzeichenrichtige Summe der Ströme aller durch den RCD geführten aktiven Leiter ist nicht mehr null.

Bei L/N in einem einfachen einphasigen Fehlerbeispiel gilt:
**I_Δ = |I_L − I_N|**.

Beispiel: **6,00 A hin, 5,96 A zurück → 0,04 A = 40 mA Differenzstrom**.

## 2.2 Aufbau – Ringkern, Messspule, Auslöser
Ein üblicher elektromechanischer RCD enthält:
1. **Magnetischen Ringkern (Summenstromwandler)**, durch den L/N bzw. L1/L2/L3/N geführt werden.
2. **Messwicklung (Sekundärspule)** auf dem Ringkern.
3. **Auslöseeinrichtung** und mechanischen Schaltmechanismus.
4. **Schaltkontakte** der aktiven Leiter.
5. **Testtaste T mit internem Prüfwiderstand**.

**Fehlerfreier Zustand:** Gleich großer Hin- und Rückstrom erzeugen im Ringkern entgegengesetzte magnetische Wirkungen. Die Summe ist null; die Messspule liefert kein für die Auslösung ausreichendes Signal.

**Fehlerfall:** Ein Teil des Stromes fließt über PE/Erde oder einen anderen Pfad zurück. Im Ringkern bleibt ein zeitlich veränderlicher magnetischer Fluss. In der Messwicklung wird eine Spannung induziert. Das Messsignal betätigt den Auslöser; die Kontakte öffnen.

**Kette für die mündliche Erklärung:**
**Stromdifferenz → magnetischer Fluss im Ringkern → Induktionsspannung in der Messspule → Auslöser → Kontakte öffnen**.

Der PE wird **nicht als geschalteter aktiver Leiter** durch den FI geführt. Ein PEN darf nicht geschaltet werden.

## 2.3 Warum 40 A / 30 mA zwei verschiedene Dinge sind
Auf einem FI steht zum Beispiel **40 A / 0,03 A**.

- **I_n = 40 A:** Bemessungsstrom. Unter den vorgesehenen Bedingungen darf das Gerät 40 A je vorgesehenem Strompfad führen.
- **I_Δn = 30 mA:** Bemessungsdifferenzstrom. Er kennzeichnet die Empfindlichkeit gegenüber Fehlerströmen.

**Entscheidend:** Bei 41 A Betriebsstrom erkennt der FI nicht plötzlich keine 30 mA mehr. **40 A ist keine Messgrenze.** Aber ein Betriebsstrom über dem Bemessungsstrom ist eine Überlastung; die dauerhafte zulässige Belastung wäre überschritten und unzulässige Erwärmung/Beschädigung möglich. Ein gewöhnlicher FI schützt sich nicht selbst gegen Überlast.

Beispiel A: 35 A hin, 35 A zurück → **I_Δ = 0**, FI löst aufgrund eines Fehlerstroms nicht aus.
Beispiel B: 2 A hin, 1,96 A zurück → **I_Δ = 40 mA**, geeigneter 30-mA-FI löst aus.
Beispiel C: 42 A hin, 42 A zurück → **I_Δ = 0**, aber 40-A-Gerät ist über seinem Bemessungsstrom belastet; **Überstromschutz erforderlich**.

## 2.4 Testtaste und das Symbol mit Widerstand von L nach N
Auf vielen RCDs ist ein internes **Schaltbild mit Taster T und Widerstand R** aufgedruckt. Ein Beispiel ist eine Verbindung von L auf einer Seite der Summenstrommessung über **T + R** zu N auf der anderen Seite. Die tatsächliche Ausführung steht im Hersteller-Schaltbild.

Beim Tastendruck schließt sich ein Prüfstromkreis, der den Summenstromwandler teilweise umgeht. Dadurch entsteht künstlich eine Differenz; der FI soll auslösen. **Der Widerstand begrenzt den Prüfstrom.** Es ist **kein direkter Kurzschluss** zwischen L und N.

Die Taste prüft nur die grundlegende Geräteauslösung. Sie ersetzt **keine RLO-Messung**, keine Erdungsmessung und keine vollständige Erstprüfung.

## 2.5 RCD-Typen

| Typ | Erkennungsbereich | Praxis |
|---|---|---|
| **AC** | Sinusförmige Wechselfehlerströme | Für übliche Neuanlagen in Deutschland keine generelle Wahl. |
| **A** | Wechsel- und pulsierende Gleichfehlerströme | Häufiger Typ für allgemeine Installationen. |
| **F** | Wie A, zusätzlich bestimmte Mischfrequenzen | Bestimmte einphasige Frequenzumrichter. |
| **B** | Zusätzlich glatte Gleichfehlerströme | Bestimmte industrielle Umrichter/Anwendungen. |
| **B+** | Allstromsensitiv, zusätzliche Anforderungen im höheren Frequenzbereich | Spezielle Schutz- und Brandschutzkonzepte. |

**Typ A = pulsstromsensitiv.** Ein glatter Gleichfehlerstrom wird von Typ A **nicht bestimmungsgemäß erkannt** und kann seine Erkennungsfunktion beeinträchtigen. Geräte- und Anlagenvorgaben für den RCD-Typ beachten.

**B beim FI ist NICHT dasselbe wie B16 beim LS!** Beim FI bezeichnet es Fehlerstromformen; beim LS die magnetische Kennlinie.

## 2.6 Wichtige Prüfwerte für 30-mA-RCD
Für einen **unverzögerten Standard-RCD** und die hier betrachtete Prüfung mit sinusförmigem Wechselfehlerstrom:

| Prüfstrom | Beispiel bei I_Δn = 30 mA | Produktnorm-Prüfverhalten |
|---|---|---|
| 0,5 × I_Δn | 15 mA | Darf unter festgelegten Bedingungen nicht auslösen. |
| 1 × I_Δn | 30 mA | Muss auslösen; max. 300 ms. |
| 2 × I_Δn | 60 mA | Muss auslösen; max. 150 ms. |
| 5 × I_Δn | 150 mA | Muss auslösen; max. 40 ms. |

Andere RCD-Typen, Fehlerstromformen und Selektivitätsausführungen besitzen zusätzliche oder andere Prüfbedingungen. Diese Produktnormwerte sind nicht mit jeder installationsseitigen Abschaltzeit gleichzusetzen.

## 2.7 Weitere Aufschriften
- **U_e:** Bemessungsbetriebsspannung, z. B. 230/400 V.
- **U_i:** Bemessungsisolationsspannung.
- **U_imp:** Bemessungsstoßspannungsfestigkeit.
- **I_m:** Bemessungsschaltvermögen.
- **I_Δm:** Bemessungsfehlerstrom-Schaltvermögen.
- **I_nc:** Bedingter Bemessungskurzschlussstrom mit passender vorgeschalteter Schutzeinrichtung.
- **S im Kästchen:** Selektive/zeitverzögerte Ausführung.
- **T/TEST:** Prüftaste; **I/O:** Ein/Aus.
- **2P** für passende einphasige, **4P** für passende mehrphasige Stromkreise; Klemmenbelegung laut Datenblatt.

## 2.8 Praxis – Querschnitte, Aderendhülsen, Drehmoment
Es gibt **keinen universellen Anschlussquerschnitt für alle RCDs**. Zulässige Leiterarten (starr/flexibel), Querschnitte, Abisolierlängen, Aderendhülsen, Anzahl Leiter pro Klemme und Anzugsdrehmomente stehen im Herstellerdatenblatt.

**Beispiel eines bestimmten Modells** (nicht verallgemeinern): Ein vierpoliger 40-A-/30-mA-RCD kann Klemmen für starre Leiter bis 25 mm², flexible Leiter bis 16 mm² und ein Drehmoment um 2,8 Nm vorsehen. Für dein tatsächliches Gerät gelten ausschließlich dessen eigene Angaben.

**Ein gewöhnlicher RCCB hat keinen integrierten Überstromschutz.** Ein RCBO (FI/LS) kombiniert FI- und LS-Funktion.

---

# LEKTION 3 – Leitungsschutzschalter (LS)

## 3.1 Aufgabe und zwei Auslöser
Der LS schützt Leitungen vor **Überlast** und **Kurzschluss**.

**Thermischer Auslöser / Bimetall:** Länger anhaltender erhöhter Strom erwärmt zwei verbundene Metalle unterschiedlich. Das Bimetall verbiegt sich und löst mit Verzögerung aus.

**Elektromagnetischer Auslöser / Spule mit Anker:** Ein ausreichend großer Strom erzeugt ein starkes Magnetfeld. Der Anker betätigt sehr schnell den Auslösemechanismus. Beim Öffnen der Kontakte wird der entstehende Lichtbogen in der Lichtbogenlöscheinrichtung gelöscht.

**Merksatz:** Überlast → Bimetall; Kurzschluss → Magnetspule.

## 3.2 B16, C16, D16
Der Buchstabe kennzeichnet die **Auslösecharakteristik**, die Zahl den **Bemessungsstrom in A**.

| Kennlinie | Magnetischer Bereich | Beispiel bei 16 A |
|---|---|---|
| B | 3–5 × I_n | 48–80 A |
| C | 5–10 × I_n | 80–160 A |
| D | 10–20 × I_n | 160–320 A |

Das sind die magnetischen Grenzbereiche unter normierten Prüfbedingungen. Ein C16 benötigt im Vergleich zum B16 grundsätzlich einen **höheren Fehlerstrom**, um magnetisch sicher schnell auszulösen. Er ist nicht automatisch besser.

**Anwendungsbeispiel:** Ein Motor kann beim Einschalten kurzzeitig erhöhten Strom ziehen. C kann geeigneter sein als B, **wenn** Einschaltverhalten, Leitungsschutz und Abschaltbedingungen geprüft und erfüllt werden.

## 3.3 Thermische Überlastauslösung
Ein B16 muss nicht bei 16,1 oder 17 A sofort auslösen. Typische konventionelle Prüfwerte nach EN 60898-1 für die betrachteten Geräte:
- **1,13 × I_n**: innerhalb der konventionellen Prüfzeit keine Auslösung.
- **1,45 × I_n**: Auslösung innerhalb der konventionellen Prüfzeit (bei üblichem In bis 63 A: 1 h).
- **2,55 × I_n**: deutlich kürzere Auslösezeiten unter festgelegten Bedingungen.

## 3.4 Aufdruck 6000 / 6 kA
Steht auf einem geeigneten LS **6000**, bezeichnet das ein **Bemessungskurzschlussausschaltvermögen von 6000 A = 6 kA**, unter den normierten Bedingungen. Der LS löst **nicht erst bei 6000 A** aus. Der mögliche Kurzschlussstrom am Einbauort muss zum Ausschaltvermögen/Schutzkonzept passen.

## 3.5 Fehlerstrom und Schleifenimpedanz
Vereinfachter Zusammenhang: **I_k ≈ U_0 / Z_s**. Bei 230 V und Z_s = 2 Ω ergibt sich I_k ≈ 115 A. Für die sichere magnetische Schnellauslösung eines B16 wird häufig der obere Grenzwert **5 × 16 A = 80 A** als rechnerisches Kriterium angesetzt; normgerechte Prüfung berücksichtigt weitere Faktoren. C16 verlangt gegenüber B16 höhere Ströme für die entsprechende Schnellauslösung.

**Warum nicht einfach B16 gegen C16 tauschen?** Die höhere magnetische Auslöseschwelle kann dazu führen, dass am entferntesten Fehlerort die geforderte Abschaltzeit nicht mehr eingehalten wird.

---

# LEKTION 4 – Überlast, Kurzschluss und Leitungsschutz

## 4.1 Drei verschiedene Fehler
- **Überlast:** Ein intakter Stromkreis wird zu stark belastet; Beispiel mehrere Heizgeräte, 24 A an einem nur entsprechend kleiner ausgelegten Stromkreis.
- **Kurzschluss:** Unbeabsichtigte niederimpedante Verbindung zwischen Punkten unterschiedlicher Spannung; Beispiel L und N berühren sich.
- **Körperschluss:** Ein aktiver Leiter berührt durch einen Fehler ein berührbares leitfähiges Gehäuse; Beispiel L am Metallgehäuse der Waschmaschine.

Ein Körperschluss kann je nach Netzsystem einen großen oder kleinen Fehlerstrom verursachen.

## 4.2 Erwärmung
**P_V = I² × R**: Die Verlustleistung im Leiter wächst mit dem Quadrat des Stroms. Bei doppeltem Strom wird sie bei gleichem Widerstand viermal so groß.

Außerdem können **lockere Klemmen** mit hohem Übergangswiderstand örtlich stark erwärmen, auch wenn der LS wegen insgesamt nicht zu hohen Betriebsstroms nicht auslöst.

## 4.3 Überlastschutz richtig auslegen
**I_B ≤ I_n ≤ I_Z**

- **I_B:** Betriebsstrom der Last.
- **I_n:** Bemessungsstrom des Schutzgerätes.
- **I_Z:** Zulässige Strombelastbarkeit der Leitung unter realen Verlegebedingungen.

Zusätzliche Schutzbedingung: **I_2 ≤ 1,45 × I_Z**. Für genormte LS kann I_2 typischerweise mit 1,45 × I_n angesetzt werden.

**Ein B16 passt nicht automatisch zu 1,5 mm²!** Die Auswahl hängt von Verlegeart, Anzahl belasteter Adern, Häufung, Umgebungstemperatur, Leitungslänge, Material, Spannungsfall und Abschaltbedingungen ab.

## 4.4 Kleinster und größter Kurzschlussstrom
- **I_k,min:** Muss ausreichen, damit die Schutzvorrichtung rechtzeitig abschaltet.
- **I_k,max:** Muss innerhalb der Ausschaltmöglichkeiten der Schutzvorrichtung bzw. koordinierten Schutzkombination liegen.

---

# LEKTION 5 – Schutz gegen elektrischen Schlag

## 5.1 Drei Schutzebenen

| Schutzebene | Wann? | Beispiel |
|---|---|---|
| **Basisschutz** | Im fehlerfreien Betrieb | Isolierung aktiver Leiter, Abdeckungen |
| **Fehlerschutz** | Wenn ein Fehler vorliegt | Automatische Abschaltung mit PE und passender Schutzeinrichtung |
| **Zusatzschutz** | Ergänzend | 30-mA-RCD in den vorgeschriebenen Anwendungen |

**Eselsbrücke:**
- Basisschutz: „Ich kann L normalerweise nicht anfassen.“
- Fehlerschutz: „Wenn Isolation versagt, soll ich weiter geschützt sein.“
- Zusatzschutz: „Eine weitere Schutzebene begrenzt das Restrisiko.“

Ein 30-mA-FI schützt **nicht vor jedem Stromschlag**: Bei Berührung von L und N kann sich die Stromsumme ausgleichen, obwohl Strom durch den Körper fließt.

## 5.2 Schutzklassen

| Klasse | Schutzprinzip | Zeichen / Beispiel |
|---|---|---|
| **I** | Basisisolierung und Schutzleiteranschluss | PE-Symbol am Anschluss; viele Waschmaschinen |
| **II** | Doppelte oder verstärkte Isolierung | Quadrat im Quadrat; bestimmte Netzteile |
| **III** | Versorgung mit SELV-Schutzkleinspannung | III in Raute; geeignete 12-V-SELV-Leuchte |

Nicht jedes Metallgehäuse bedeutet automatisch Klasse I und nicht jedes Kunststoffgehäuse Klasse II.

## 5.3 SELV – von null
**SELV = Safety Extra-Low Voltage.** Es handelt sich um eine Schutzmaßnahme, **nicht um ein zusätzliches einzelnes Bauteil**.

**Beispiel:** Die Steckdose liefert 230 V, eine LED benötigt 12 V. Ein dafür geeignetes Netzteil erzeugt 12 V und trennt die Ausgangsseite **sicher** von den 230 V.

Warum nicht einfach nur 12 V erzeugen? Eine nicht sicher getrennte Schaltung könnte zwar 12 V zwischen ihren Ausgangsklemmen haben, aber gefährliche Spannungen **gegen Erde** ermöglichen. SELV verlangt die sichere Trennung.

**Bei SELV ist der Ausgangsstromkreis nicht absichtlich geerdet.** Es wird also weder +12 V noch 0 V absichtlich mit PE verbunden. Der Netzteilkörper selbst kann je nach Schutzklasse einen PE-Anschluss besitzen, ohne dass dies den Ausgang automatisch erdet.

**Merksatz SELV:** Niedrige Spannung + sichere Trennung + kein absichtlicher Erdbezug des Ausgangsstromkreises.

## 5.4 PELV – aus der Praxis
**PELV = Protective Extra-Low Voltage.** Ebenfalls niedrige Spannung und sichere Trennung, **aber der Kleinspannungsstromkreis darf absichtlich geerdet werden**.

**Beispiel:** Ein geeignetes sicher getrenntes 24-V-Netzteil versorgt eine SPS. In der vorgesehenen Anlagenplanung verbindet der Elektroniker **0 V mit PE**.

**Wichtig zur Spannung:** Der Ausgang bleibt **+24 V gegenüber 0 V**, auch wenn 0 V mit PE verbunden ist. PE „nimmt nicht die Spannung weg“.

Normalerweise fließt der Betriebsstrom von +24 V durch die SPS und über 0 V zurück. **PE führt im fehlerfreien Betrieb keinen Betriebsstrom.**

**Konkreter Fehler:** +24 V berührt ein geerdetes Metallgehäuse. Ein möglicher Fehlerstromweg lautet:
**+24 V → Gehäuse → PE → 0-V-/PE-Verbindung → 24-V-Netzteil**.

Eine geeignet ausgelegte Sicherung oder elektronische Absicherung **auf der 24-V-Seite** kann reagieren. Der vorgeschaltete 230-V-FI erkennt aufgrund der sicheren Trennung normalerweise **keinen eigenen Differenzstrom** aus diesem 24-V-Fehler. Die konkrete Abschaltung hängt von der Schutztechnik ab.

**Wichtig:** Nur an den laut Schaltplan/Hersteller vorgesehenen Stellen die Verbindung zwischen 0 V und PE herstellen.

## 5.5 FELV
**FELV = Functional Extra-Low Voltage.** Kleinspannung aus funktionellen Gründen, **ohne** dass sämtliche Anforderungen an SELV/PELV erfüllt sind. Deshalb **keine eigenständige Schutzmaßnahme gegen elektrischen Schlag**; weitere Schutzvorkehrungen erforderlich.

## 5.6 Spannungsgrenzen
Unter üblichen Bedingungen: **höchstens 50 V Wechselspannung oder 120 V weitgehend glatte Gleichspannung**. In besonderen Bereichen, z. B. bestimmten Feuchträumen, können strengere Grenzwerte gelten.

**Prüfungsfalle:** Nicht jedes 12-V-/24-V-Netzteil ist automatisch SELV oder PELV. Die Eigenschaften der sicheren Trennung und alle weiteren Anforderungen müssen gegeben sein.

---

# LEKTION 6 – IP-Schutzarten, Erdung, Potentialausgleich

## 6.1 IP-Kennzeichnung lesen
**IPxy:** erste Zahl x = Schutz gegen Zugang zu gefährlichen Teilen und feste Fremdkörper; zweite Zahl y = Schutz gegen Wasser.

**Erste Kennziffer:**
- 0: kein festgelegter Schutz.
- 1: Fremdkörper ab 50 mm.
- 2: ab 12,5 mm / Fingerschutz.
- 3: ab 2,5 mm.
- 4: ab 1 mm.
- 5: staubgeschützt (kein schädigendes Staubeindringen).
- 6: staubdicht.

**Zweite Kennziffer:**
- 0: kein Wasserschutz.
- 1: senkrechtes Tropfwasser.
- 2: Tropfwasser bei Gehäuseneigung bis 15°.
- 3: Sprühwasser.
- 4: allseitiges Spritzwasser.
- 5: Strahlwasser.
- 6: starkes Strahlwasser.
- 7: zeitweiliges Untertauchen.
- 8: dauerndes Untertauchen unter vereinbarten Bedingungen.
- 9: Wasser bei Hochdruck-/Hochtemperaturreinigung.

| IP-Art | Merkhilfe |
|---|---|
| **IP20** | Fingerschutz, kein ausgewiesener Wasserschutz. |
| **IP44** | Fremdkörper ab 1 mm + Spritzwasser. |
| **IP54** | Staubgeschützt + Spritzwasser. |
| **IP65** | Staubdicht + Strahlwasser. |
| **IP67** | Staubdicht + zeitweiliges Untertauchen. |

**Achtung:** IP67 ist nicht automatisch nach IP65 gegen Strahlwasser geprüft. Schutz gilt für korrekt montierte Gehäuse, Dichtungen und geeignete Kabeleinführungen. UV-/Temperaturbeständigkeit zusätzlich beachten.

## 6.2 Erdung
**Erdung** = bewusste elektrische Verbindung eines Punktes oder leitfähigen Teils zur Erde, über eine geeignete Erdungsanlage. Ein Erder kann etwa als Fundamenterder oder andere normgerechte Ausführung vorhanden sein.

**PE (grün-gelb)** verbindet entsprechend vorgesehene Körper elektrischer Betriebsmittel mit dem Schutzsystem. Im Normalbetrieb führt PE grundsätzlich keinen Betriebsstrom; bei einem Körperschluss kann er Fehlerstrom führen. PE darf nicht wie ein aktiver Leiter geschaltet oder abgesichert werden.

## 6.3 Schutzpotentialausgleich
**Schutzpotentialausgleich** verbindet **relevante fremde leitfähige Teile** mit der **Haupterdungsschiene (HES)**, um gefährliche Potentialunterschiede zu vermindern.

Beispiel: Bestimmte metallene Wasser-/Heizungsrohre können fremde leitfähige Teile sein. Bei einem Fehler soll zwischen gleichzeitig berührbaren metallischen Teilen möglichst keine gefährliche Spannung entstehen.

**Unterschied merken:**
- **Erdung:** Verbindung zur Erde.
- **Schutzpotentialausgleich:** Schutzverbindungen zwischen relevanten leitfähigen Teilen zum Verringern von Spannungsunterschieden.
- **HES:** Zentraler Anschluss-/Verbindungspunkt.

Nicht jedes beliebige Metallteil wird pauschal angeschlossen; Zuordnung nach DIN VDE 0100-540.

## 6.4 Querschnitte
Für Schutzpotentialausgleichsleiter zur HES gelten nach DIN VDE 0100-540 in den hier betrachteten allgemeinen Fällen Mindestquerschnitte von **6 mm² Cu, 16 mm² Al oder 50 mm² Stahl**, zusätzlich die halbe Querschnittsregel zum größten PE und weitere Bemessungsanforderungen. Die allgemeine Bemessungsregel verlangt keinen größeren Leiter als 25 mm² Cu bzw. gleichwertig. **Nicht verwechseln mit dem normalen PE einzelner Stromkreise.**

## 6.5 Erstprüfung – wichtige Kürzel
- **R_LO:** Niederohmige Schutzleiter-/Schutzpotentialausgleichs-Durchgängigkeit.
- **R_ISO:** Isolationswiderstand.
- **Z_s:** Fehlerschleifenimpedanz.
- **RCD-Prüfung:** Auslösefunktion/entsprechende Zeiten.
- **Erdungswiderstand:** Falls zum Schutzkonzept gehörend.

R_LO bedeutet nicht nur „irgendeinen Widerstand messen“, sondern **prüfen, ob die Schutzleiter- und erforderlichen Potentialausgleichsverbindungen ausreichend niederohmig durchgängig sind**.

---

# LEKTION 7 – Fünf Praxisfälle

## Praxisfall A – Außensteckdose
1. Umgebungsbedingungen und geeignete IP-Schutzart beurteilen; oft geeignete IP44-Ausführung, abhängig vom Ort.
2. Für übliche Steckdosen bis 32 A ist ein RCD mit **höchstens 30 mA** in den genannten Anwendungen vorgeschrieben.
3. Leitung und LS nach I_B, I_Z, Verlegeart, Leitungslänge und Abschaltbedingungen auslegen.
4. PE, Klemmen, Feuchtigkeitsschutz und Prüfung sicherstellen.

## Praxisfall B – Motor mit hohem Einschaltstrom
Ein C16 kann sich bezüglich des Einschaltstroms anders als ein B16 verhalten. Aber höherer magnetischer Auslösebereich bedeutet auch **höheren erforderlichen Fehlerstrom** für sichere Schnellauslösung. Deswegen Schleifenimpedanz/Abschaltbedingungen prüfen. Ggf. Motorschutz berücksichtigen.

## Praxisfall C – PEN-Aufteilung
PEN bei einer normgerechten Stelle in N und PE aufteilen. **Danach keine Wiederverbindung.** Ein RCD gehört nur in den Abschnitt mit korrekt getrennten aktiven Leitern und PE.

## Praxisfall D – 24-V-SPS-Steuerung
Geeignetes sicher getrenntes 24-V-Netzteil, ggf. **0 V mit PE = PELV**. +24-V-Körperschluss kann einen Fehlerstromweg über PE → 0 V erzeugen. Schutz auf der 24-V-Seite auslegen.

## Praxisfall E – Frequenzumrichter
Wenn beim Betriebsmittel glatte Gleichfehlerströme auftreten können, reicht ein üblicher Typ-A-RCD möglicherweise nicht. Geeigneten allstromsensitiven RCD, beispielsweise Typ B, nach Hersteller- und Normanforderung auswählen.

---

# LEKTION 8 – Wiederholung und AP1-Prüfungsfragen

## 8.1 Zehn typische mündliche Fragen – Musterantworten

**1. Warum im TT-System normalerweise ein FI?**
Weil der Fehlerstrom über Erder/Erdreich zurückfließt und wegen des Widerstands zu klein sein kann, um einen LS rechtzeitig auszulösen. Der RCD erkennt Differenzstrom und schaltet selbst ab.

**2. Was macht der Summenstromwandler?**
Er vergleicht die vorzeichenrichtige Summe der Leiterströme über die magnetische Wirkung im Ringkern. Eine Differenz erzeugt ein Signal in der Messwicklung.

**3. Was bedeuten 40 A / 30 mA am FI?**
40 A = Bemessungsstrom; 30 mA = Bemessungsdifferenzstrom. 40 A ist keine obere Messgrenze des Fehlerstroms.

**4. Warum Prüfwiderstand neben T im FI-Schaltbild?**
Er begrenzt den künstlich erzeugten Prüfstrom; durch den Teststrom entsteht eine Stromdifferenz, die den FI auslösen soll.

**5. Warum darf man B16 nicht beliebig gegen C16 tauschen?**
C16 verlangt einen größeren Fehlerstrom für sichere magnetische Schnellauslösung. Die Abschaltbedingungen müssen erhalten bleiben.

**6. Was bedeutet 6000 auf einem LS?**
Bemessungskurzschlussausschaltvermögen: 6000 A = 6 kA unter den festgelegten Bedingungen.

**7. Drei Schutzebenen?**
Basisschutz = direktes Berühren im Normalbetrieb verhindern; Fehlerschutz = Schutz bei Fehler; Zusatzschutz = ergänzender Schutz, z. B. 30-mA-RCD.

**8. Warum bleibt eine PELV-SPS bei 0-V-/PE-Verbindung auf 24 V?**
Weil die Spannung zwischen +24 V und 0 V weiter 24 V beträgt. Die Erdverbindung legt nur das Bezugspotential fest.

**9. Unterschied Erdung/Schutzpotentialausgleich?**
Erdung verbindet zur Erde; Schutzpotentialausgleich verbindet relevante leitfähige Teile zur Verringerung gefährlicher Spannungsunterschiede.

**10. Was prüfen R_LO, R_ISO und Z_s?**
R_LO = Schutzleiterdurchgängigkeit; R_ISO = Isolationswiderstand; Z_s = Fehlerschleifenimpedanz für Abschaltbedingungen.

## 8.2 Mini-Abschlusstest (ohne Lösungen auf dieser Seite)
1. Nenne TN-S, TN-C, TN-C-S, TT und IT mit jeweils einem Merkmal.
2. Erkläre in einem Satz, warum TT normalerweise einen RCD benötigt.
3. Beschreibe Ringkern, Messspule und Auslösung des RCD.
4. Erkläre 40 A und 30 mA am FI.
5. Unterscheide Typ A und Typ B.
6. Unterscheide thermischen und magnetischen LS-Auslöser.
7. Erkläre Basisschutz, Fehlerschutz und Zusatzschutz.
8. Unterscheide SELV und PELV und erkläre eine 0-V-/PE-Verbindung.
9. Erkläre IP44 und IP65.
10. Erkläre Erdung, HES und Schutzpotentialausgleich.

---

# FORMELBLATT – Tag 3

| Formel / Wert | Bedeutung |
|---|---|
| **I_Δ = |I_L − I_N|** | Einphasiger Differenzstrom im einfachen Fehlerbeispiel. |
| **I = U / R** | Ohmsches Gesetz. |
| **P_V = I² × R** | Verlustleistung/Wärme in einem Widerstand. |
| **I_B ≤ I_n ≤ I_Z** | Erste Bedingung für Überlastschutz. |
| **I_2 ≤ 1,45 × I_Z** | Weitere Überlastschutzbedingung. |
| **I_k ≈ U_0 / Z_s** | Vereinfachter Fehlerstrom aus Schleifenimpedanz. |
| **B: 3–5 × I_n** | Magnetischer LS-Bereich. |
| **C: 5–10 × I_n** | Magnetischer LS-Bereich. |
| **D: 10–20 × I_n** | Magnetischer LS-Bereich. |
| **1 A = 1000 mA** | Umrechnung; 0,03 A = 30 mA. |
| **1 s = 1000 ms** | Umrechnung; 40 ms = 0,04 s. |

# ZEICHEN UND ABKÜRZUNGEN

| Kürzel / Zeichen | Bedeutung |
|---|---|
| **L, L1, L2, L3** | Außenleiter |
| **N** | Neutralleiter |
| **PE** | Schutzleiter |
| **PEN** | Kombinierter Schutz- und Neutralleiter |
| **HES** | Haupterdungsschiene |
| **IMD** | Isolationsüberwachungsgerät |
| **RCD / FI / RCCB** | Fehlerstromschutzeinrichtung / FI ohne Überstromschutz |
| **LS / MCB** | Leitungsschutzschalter |
| **RCBO** | Kombinierter FI/LS |
| **I_n** | Bemessungsstrom |
| **I_Δn** | Bemessungsdifferenzstrom |
| **I_B** | Betriebsstrom |
| **I_Z** | Zulässige Strombelastbarkeit der Leitung |
| **Z_s** | Fehlerschleifenimpedanz |
| **R_LO** | Niederohmigkeit / Schutzleiterdurchgängigkeit |
| **R_ISO** | Isolationswiderstand |
| **IPxy** | Gehäuseschutzart: Fremdkörper/Berührung, Wasser |
| **I / O** | Ein / Aus |
| **T** | RCD-Testtaste |
| **S im Kästchen** | Selektiver RCD |
| **Quadrat im Quadrat** | Schutzklasse II |
| **III in Raute** | Schutzklasse III |
| **PE-/Erdungszeichen** | Schutzleiteranschluss |

# LERNSTAND UND GEZIELTE WIEDERHOLUNG

**Interaktiv abgefragter Stand am 14.10.2026:**
- **Lektion 1 Netzsysteme:** 17 von 21 Punkten.
- **Lektion 2 FI/RCD:** 10,5 von 13 bisher bewerteten Punkten; danach auf Wunsch übersprungen.
- **Lektion 3 LS:** 13 von 18 möglichen Punkten, einschließlich übersprungener Rechenfragen.
- **Lektion 4:** Übungsfragen auf Wunsch übersprungen.
- **Lektion 5:** Übungsfragen auf Wunsch übersprungen; SELV und PELV wurden später intensiv geklärt.
- **Lektion 6:** Übungsfragen auf Wunsch übersprungen.
- **Lektion 7:** Übungsfragen auf Wunsch übersprungen.
- **Lektion 8 AP1-Simulation:** 18 von 24 Punkten nach vier beantworteten Prüfungsblöcken. **Der fünfte Prüfungsblock ist noch offen**; eine Gesamtpunktzahl von 30 kann deshalb noch nicht vergeben werden.

**Zuerst wiederholen:**
1. TT: Fehlerstromweg über die Erdungsanlagen → LS kann unzureichend sein → RCD schaltet selbst.
2. Fehlerschutz vs. Zusatzschutz sicher unterscheiden.
3. Erdung vs. Schutzpotentialausgleich und Zweck der HES.
4. IP-Ziffern präzise erklären: IP65 = staubdicht/Strahlwasser; IP44 = Fremdkörper ab 1 mm/Spritzwasser.
5. Schutzleiterdurchgängigkeit mit R_LO erklären, nicht bloß „Widerstand messen“.
6. RCD-Typ B erkennt zusätzlich glatte Gleichfehlerströme.
7. B-/C-/D-Kennlinien und die benötigten Fehlerströme nochmals rechnen.

# Normen zum Nachschlagen
- **DIN VDE 0100-410:** Schutz gegen elektrischen Schlag.
- **DIN VDE 0100-430:** Schutz bei Überstrom.
- **DIN VDE 0100-530:** Auswahl und Errichtung von Schalt- und Schutzgeräten.
- **DIN VDE 0100-540:** Erdung und Schutzpotentialausgleich.
- **DIN VDE 0100-600:** Erstprüfung elektrischer Anlagen.
- **DIN EN 60529 (VDE 0470-1):** IP-Schutzarten.
- **DIN EN 60898-1:** Leitungsschutzschalter.
- **DIN EN 61008-1:** FI ohne Überstromschutz.
- **DIN EN 61009-1:** FI/LS mit Überstromschutz.
- **DIN EN 62423:** Ergänzende Anforderungen an RCD Typ F/B.

**Hinweis:** Dieses Skript erklärt die Prinzipien zu Lernzwecken. Für konkrete Planung, Messung, Schutzgerätauswahl und Verdrahtung sind aktuelle Normenausgaben, Datenblätter, die konkrete Anlage und die Anweisungen der verantwortlichen Elektrofachkraft entscheidend.

**Ende des Tag-3-Lernskripts.**