# Vertiefung 3 – Netzsysteme, Schutzmaßnahmen und Sicherheitsbestimmungen

**Ziel:** Vor jeder Installation verstehen, was gegen gefährliche Berührung, Überlast und Fehlerstrom schützen soll. Die Antworten richten sich nach einer vorgegebenen Anlage; keine dieser Erklärungen ist eine Freigabe zu Arbeiten an Netzspannung.

## 1. Sicherheit zuerst

Elektrischer Strom kann Körperdurchströmung, Verbrennungen, Störlichtbogen und Brand verursachen. Gefährdung hängt von Stromstärke, Einwirkdauer, Stromweg, Körperbedingungen und Umgebung ab. „230 V ist normal“ bedeutet **nicht ungefährlich**. Bei Arbeiten an elektrischen Anlagen gelten die betrieblichen Verantwortlichkeiten, vorgeschriebene Qualifikation und Elektrofachkraftaufsicht.

**Fünf Sicherheitsregeln in dieser Reihenfolge:**
1. **Freischalten.**
2. **Gegen Wiedereinschalten sichern.**
3. **Spannungsfreiheit feststellen** – mit geeignetem Prüfmittel durch dazu befugte Person.
4. **Erden und kurzschließen** – soweit für das Netz/die Arbeitsstelle erforderlich.
5. **Benachbarte, unter Spannung stehende Teile abdecken oder abschranken.**

Beim Arbeiten in Niederspannungsanlagen ist Regel 4 je nach Fall nicht erforderlich; bei Hochspannung hat sie besondere Bedeutung. Ob eine Regel anwendbar ist, ist **nicht** eine freie Entscheidung eines Auszubildenden. **Einpolige Prüfschraubendreher sind kein Ersatz** für eine fachgerechte Spannungsfreiheitsprüfung.

## 2. Grundfunktionen der Leiter

- **Außenleiter L/L1–L3:** Spannung gegenüber Erdpotenzial; liefert den Energiefluss.
- **Neutralleiter N:** bestimmungsgemäß stromführender Rückleiter.
- **Schutzleiter PE:** verhindert in Verbindung mit geeigneten Schutzmaßnahmen, dass gefährliche Berührspannungen dauerhaft bestehen; kein normaler Laststrompfad.
- **PEN:** kombinierte Funktion aus PE + N, nur in dafür zulässigen Netzabschnitten und mit besonderen Regeln; nach zulässiger Trennung normalerweise nicht wieder verbinden.

**PE niemals schalten, zweckentfremden oder als Ersatz-Neutralleiter verwenden.** Ein falsch verdrahteter Schutzleiter kann lebensgefährlich sein.

## 3. Netzsysteme – erkennen und unterscheiden

| System | Quelle/Körper und Schutz-/Neutralleiter | Wesentliche Idee |
|---|---|---|
| TN-S | Quelle geerdet, Körper über PE mit geerdeter Quelle verbunden; N und PE getrennt | getrennte Leiter ab Versorgungsquelle |
| TN-C | Quelle geerdet, Körper über PEN verbunden | kombinierte PE-/N-Funktion im betreffenden Abschnitt |
| TN-C-S | Kombination aus TN-C und nachgeschaltetem TN-S | PEN bis zur Aufteilung, anschließend getrennte N/PE |
| TT | Quelle geerdet; Körper an örtlichem, elektrisch unabhängigem Erder | Fehlerstromschutz/Abschaltung nach passenden Bedingungen, RCD in der Praxis sehr bedeutsam |

**Prüfungsfragen:** Was bedeutet „S“? → getrennt. Was bedeutet „C“? → combined/kombiniert. Kann ein RCD im TN-C-Abschnitt als gewöhnlicher Schutz über den PEN betrieben werden? → Nein. Warum ist die Verbindung N↔PE nach der Aufteilung problematisch? → Schutzleiter kann Betriebsstrom führen und Differenzstromschutz kann gestört werden.

**Achtung:** Normgerechtes Erdungs-, Schutz- und Abschaltkonzept erfordert mehr als nur die Bezeichnung TN oder TT.

## 4. Basis-, Fehler- und Zusatzschutz

- **Basisschutz:** unter normalen Umständen direkte Berührung aktiver Teile verhindern, z. B. durch Isolierung/geeignete Abdeckung.
- **Fehlerschutz:** bei einem Fehler Schutz vor gefährlichen Berührspannungen, z. B. automatische Abschaltung in einem geeigneten Schutzsystem.
- **Zusatzschutz:** zusätzliche Schutzmaßnahme in den jeweils vorgeschriebenen Fällen, häufig ein RCD mit IΔn ≤ 30 mA.

**Schutzklasse I:** Verbindung berührbarer leitfähiger Körper mit PE als Teil der Maßnahme. **Schutzklasse II:** doppelte oder verstärkte Isolierung. **Schutzklasse III:** Versorgung mit geeigneter Schutzkleinspannung. **IP-Schutzart** beschreibt hingegen den Widerstand der Umhüllung gegenüber Berührung/Fremdkörpern und Wasser, nicht den Schutzklassentyp.

## 5. LS, Schmelzsicherung, RCD, RCBO

- **Leitungsschutzschalter (LS):** schützt bei sachgerechter Zuordnung Leitungen gegen Überlast und Kurzschluss. Kennzeichnung etwa **B16** = Kennlinie B, Bemessungsstrom 16 A. Die Kennlinie ist keine Aussage über die zulässige Leitung an jeder beliebigen Stelle.
- **Schmelzsicherung:** unterbricht bei ausreichend hohem Überstrom nach ihrer Charakteristik; nach Auslösung zu ersetzen.
- **RCD (FI):** vergleicht die Ströme durch die überwachten aktiven Leiter; löst bei unerlaubtem Differenzstrom nach Gerätekriterien aus. **30 mA ist keine „sichere Strommenge“** für einen Menschen.
- **RCBO (FI/LS):** kombiniert passenden Fehlerstrom- und Leitungsschutz **in einem** Gerät.
- **AFDD**, Überspannungsschutzeinrichtungen usw. können für spezifische Anforderungen relevant sein, sind aber **kein pauschaler Ersatz** für alle genannten Schutzmaßnahmen.

**Ein gewöhnlicher RCD schützt nicht selbst zuverlässig vor Überlast und Kurzschluss.** Ein LS wiederum ersetzt einen erforderlichen RCD nicht. Die Anwendung ist nach Netzform, Stromkreis, Geräteeigenschaften und Vorschriften zu bestimmen.

## 6. Fehlerarten unterscheiden

**Überlast:** zu viel Laststrom im ordnungsgemäß verbundenen Stromkreis; Leitung kann sich unzulässig erhitzen.  
**Kurzschluss:** niederohmiger, unbeabsichtigter Kontakt zwischen Punkten unterschiedlichen Potenzials.  
**Erd-/Körperschluss:** Fehler gegen Erde/leitfähiges Gehäuse.  
**Isolationsfehler:** Isolationszustand beschädigt oder unzureichend.  
**Neutralleiterunterbrechung:** je nach Netzaufbau kann dies sehr gefährlich sein (insbesondere asymmetrische Drehstromlasten). Nicht versuchen, Symptome unter Spannung zu provozieren.

## 7. Potenzialausgleich und Erdung

**Erdung** stellt eine geeignete Verbindung zu Erde her; **Schutzpotenzialausgleich** verbindet dafür vorgesehene leitfähige Teile, damit gefährliche Potenzialdifferenzen im Fehlerfall vermindert werden. Schutzleiter, Erdungsanlage und potenzialausgleichende Verbindungen sind **nicht automatisch dasselbe Bauteil**. Ein korrektes Konzept hängt von den anwendbaren technischen Regeln ab.

## 8. Auswahl einer Schutzmaßnahme – Denkschritte

1. Netzsystem **feststellen**, nicht raten.
2. Art des Stromkreises und Betriebsmittels feststellen, z. B. Steckdosen / Licht / fest angeschlossenes Gerät.
3. Basis- und Fehlerschutz mit zulässiger Abschaltung begründen.
4. Erforderliche RCD-/Überstromschutzorgane auswählen; Typ, Nennwerte, Kurzschlussfestigkeit und Verwendungsfall aus Datenblättern/Normen bestimmen.
5. Leiter und PE-Verbindungen richtig bemessen/kennzeichnen.
6. Schutzkonzept durch die vorgesehenen Prüfungen **fachlich nachweisen**.

## 9. Aufgaben

1. Nenne die fünf Sicherheitsregeln in korrekter Reihenfolge.
2. Erkläre N, PE und PEN und wieso man sie nicht austauschen darf.
3. Ein RCD 30 mA und ein LS B16 sind eingebaut. Welcher schützt gegen welchen Fehler? Kann der FI den LS ersetzen?
4. Worin unterscheiden sich TN-S und TN-C-S? 
5. Warum sollte man bei TT-Netzen die Erdungs-/Abschaltbedingungen nicht nur anhand einer Schalterbezeichnung beurteilen?
6. Eine Leuchte ist Schutzklasse II, ihr Gehäuse hat IP44. Was bedeuten die zwei unabhängigen Angaben?
7. Warum darf ein Schutzleiter nicht durch einen normalen Schalter unterbrochen werden?
8. Wie unterscheidet sich ein Isolationsfehler von einer Überlast?
9. Nenne ein Beispiel für Basis-, Fehler- und Zusatzschutz.
10. Ein RCD löst häufig aus: Welche sicheren **Planungs- und Prüfschritte** sind erforderlich? Was darfst du ausdrücklich nicht tun?

**Erfolgskriterium:** Bei Schutzfragen kannst du **Zweck, Wirkprinzip und Grenzen** jedes Geräts richtig erklären.

[Zurück zum Kursplan](../00_START_HIER_LF2_VOLLSTAENDIG.md).
