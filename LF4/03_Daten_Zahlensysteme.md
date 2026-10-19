# LF4 – Lektion 3: Bit, Byte, Binär und Datenraten

**Ziel:** Rechenaufgaben mit klaren Einheiten lösen. Kein bloßes Formel-Auswendiglernen.

## 1. Bit und Byte

- **Bit (b):** eine binäre Information, 0 oder 1.
- **Byte (B):** 8 Bit; häufig grundlegende Einheit für Speichergrößen.
- **Wichtig:** kleines **b** bei bit, großes **B** bei Byte.

**Beispiel:** 80 bit ÷ 8 = **10 Byte**.

## 2. Dezimal und Binär

- Dezimal nutzt die Stellenwerte 1, 10, 100, …
- Binär nutzt die Stellenwerte 1, 2, 4, 8, 16, 32, 64, 128, …

**Beispiel:** Binär **101101₂** = 32 + 8 + 4 + 1 = **45₁₀**.

**Umgekehrt: 13₁₀ → binär**
- 13 = 8 + 4 + 1 → Stellenwerte 8, 4, 2, 1 → **1101₂**.

**Übe immer auch die Gegenprobe.**

## 3. Hexadezimal

Basis 16: Ziffern 0–9 und **A=10, B=11, C=12, D=13, E=14, F=15**.

1 Hex-Zeichen repräsentiert 4 Bit.

**Beispiel:** 3F₁₆ = 3×16 + 15 = **63₁₀**.  
**Beispiel:** 1100 1010₂ = **CA₁₆** (1100 = C, 1010 = A).

## 4. Speicherpräfixe richtig unterscheiden

| Einheit | Bedeutung |
|---|---:|
| kB | 1.000 B |
| MB | 1.000.000 B |
| GB | 1.000.000.000 B |
| KiB | 1.024 B |
| MiB | 1.048.576 B |
| GiB | 1.073.741.824 B |

**Prüfungsfalle:** GB ist nicht exakt GiB. Lies die im Auftrag geforderten Einheiten; wenn die Aufgabe selbst „1 kB = 1024 B“ vorgibt, rechne nach **dieser expliziten Übungsannahme** und nenne sie.

## 5. Übertragungsrate

Grundformeln:
- **Datenmenge = Datenrate × Zeit**
- **Zeit = Datenmenge ÷ Datenrate**

**Beispiel 1:** 100 Mbit/s entspricht theoretisch 100 ÷ 8 = **12,5 MB/s** (SI-Einheiten; vor Overhead).  
**Beispiel 2:** Eine Datei mit 600 MB wird über eine idealisierte Verbindung von 80 Mbit/s übertragen.

Rechnung: 80 Mbit/s ÷ 8 = 10 MB/s; 600 MB ÷ 10 MB/s = **60 s**.

**Wichtig:** In realen Netzen dauern Übertragungen wegen Protokoll-Overhead, Verzögerungen und Auslastung meist länger.

## 6. Rechenaufgaben

1. 64 bit = ? Byte.
2. 3 kB = ? Byte (dezimal).
3. 2 KiB = ? Byte (binär).
4. 101010₂ = ? dezimal.
5. 29₁₀ = ? binär.
6. A5₁₆ = ? dezimal.
7. 1111 0000₂ = ? hexadezimal.
8. 1 Gbit/s = ? MB/s (theoretisch, dezimal).
9. Wie lange dauert 120 MB bei idealen 24 Mbit/s?
10. Erkläre mit einem Satz, warum 1 GB und 1 GiB nicht genau gleich groß sind.

**Danach:** [Lektion 4 – Netzwerke](04_Netzwerke.md).