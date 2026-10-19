# LF4 – Lektion 4: Netzwerke von Grund auf verstehen

**Ziel:** Ein PC-Netzwerk erklären, Komponenten unterscheiden, grundlegende Adressierung anwenden und Fehler systematisch eingrenzen.

## 1. Ein einfacher Weg durch das Netzwerk

Beispiel: Du öffnest auf deinem PC eine Webseite.

1. Das Programm benötigt die Zieladresse des Servers; ein **DNS-Dienst** kann einen Domainnamen in eine IP-Adresse auflösen.
2. Der PC schickt Datenpakete an den passenden Empfänger. Für Ziele außerhalb des lokalen IP-Netzes nutzt er normalerweise sein **Standardgateway**.
3. Im lokalen kabelgebundenen Netz leitet ein **Switch** Ethernet-Frames nach MAC-Adressen weiter.
4. Der **Router** verbindet verschiedene IP-Netze, z. B. LAN und Internet; beim Heimrouter sind oft WLAN, Switch, DHCP und Router in einem Gehäuse vereint.
5. Der Server antwortet, Daten gelangen zum PC zurück.

**Prüfungsfalle:** Ein Switch ist nicht automatisch ein Router. Ein Router verbindet Netze; ein üblicher Layer-2-Switch verbindet Geräte innerhalb eines Ethernet-Netzes.

## 2. Geräte und Fachwörter

| Begriff | Funktion |
|---|---|
| LAN | Lokales Netzwerk |
| WLAN | Drahtloses lokales Netzwerk |
| Switch | Verbindet Geräte im LAN über Ethernet |
| Router | Verbindet IP-Netze |
| Access Point | Ermöglicht WLAN-Zugang zu einem Netz |
| Netzwerkkarte/Adapter | Netzwerkschnittstelle des Endgeräts |
| MAC-Adresse | Adresse einer Netzwerkschnittstelle auf der Sicherungsebene (Layer 2), nicht weltweit unveränderlich garantiert |
| IPv4-Adresse | Logische Netzadresse, z. B. 192.168.10.20 |
| Subnetzmaske | Trennt Netz- und Hostanteil einer IPv4-Adresse |
| Standardgateway | Router-Adresse für Ziele außerhalb des lokalen Netzes |
| DHCP | Vergibt z. B. IP-Adresse, Maske, Gateway, DNS automatisch |
| DNS | Ordnet Namen Adressen zu, z. B. www.example.org → IP-Adresse |
| TCP | Zuverlässiger, verbindungsorientierter Transport mit Quittungen/Sortierung |
| UDP | Verbindungsloser Transport ohne eingebaute Zustellgarantie |

## 3. Beispiel: Adressen in einem Netz

- PC A: **192.168.10.20**
- PC B: **192.168.10.30**
- Subnetzmaske: **255.255.255.0**, auch **/24**
- Gateway: **192.168.10.1**

Beide PCs liegen mit diesen Werten im selben Netz **192.168.10.0/24**.

Die **Netzadresse** ist 192.168.10.0; die **Broadcastadresse** ist 192.168.10.255. Im üblichen /24-Netz sind Adressen .1 bis .254 prinzipiell als Host-Adressen verwendbar, sofern nicht anderweitig reserviert/belegt.

**Merke:** Gateway ist die lokale Router-Adresse, nicht die IP-Adresse des Internets.

## 4. IPv4, DHCP und DNS – unbedingt auseinanderhalten

- **IP-Adresse:** „Wie erreiche ich das Zielnetz/Endgerät?“
- **DHCP:** „Wie erhalte ich automatisch meine IP-Konfiguration?“
- **DNS:** „Welche IP gehört zu diesem Namen?“
- **MAC:** „Wie adressiere ich das Gerät/Interface im lokalen Ethernet-Abschnitt?“

**Beispiel:** Kein Internet trotz WLAN-Verbindung:
- Verbindung zum Access Point kann bestehen, auch wenn die IP-Konfiguration fehlerhaft ist.
- Kein DNS? Webseiten per Namen möglicherweise nicht erreichbar, per IP eventuell schon.
- Kein Gateway? Lokales Netz erreichbar, fremde Netze nicht.
- Leitungs-/Funkproblem? Schon Zugang zum lokalen Netz gestört.

## 5. Datenübertragung und Medien

- **Twisted-Pair-Ethernet:** Häufig Kupfernetzwerkleitung mit 8P8C-Modularstecker.
- **LWL/Glasfaser:** Überträgt optische Signale, unempfindlich gegenüber elektromagnetischer Einkopplung.
- **WLAN:** Funk; Signalqualität, Kanalbelegung und Verschlüsselung beachten.
- Typische Raten: 100 Mbit/s, 1 Gbit/s, 10 Gbit/s usw. – die **tatsächliche Geschwindigkeit** hängt von der gesamten Verbindung ab.

## 6. Netzwerkdiagnose – gedankliche Reihenfolge

1. Physikalisch: Steckt das Kabel? Link-LED? WLAN-Verbindung?
2. Konfiguration: Welche IP, Maske, Gateway, DNS?
3. Lokal: Andere Geräte im eigenen Subnetz erreichbar?
4. Gateway: Router erreichbar?
5. Extern: IP-Ziel erreichbar? Namen über DNS auflösbar?
6. Ursache dokumentieren; nach der Behebung erneut testen.

Typische Werkzeuge: **ipconfig** (Windows), **ip addr** (Linux), **ping**, **tracert/traceroute**, **nslookup**. **Ein ausgebliebener Ping beweist nicht allein einen Leitungsfehler** (ICMP kann blockiert sein).

## 7. Aufgaben

1. Unterschied Router/Switch/Access Point in je einem Satz.
2. DHCP oder DNS – wer vergibt IP-Adressen?
3. DHCP oder DNS – wer löst www.example.org in eine IP-Adresse auf?
4. Wozu braucht ein PC das Standardgateway?
5. Haben 192.168.10.20/24 und 192.168.10.30/24 dasselbe lokale Netz?
6. Was ist der Unterschied zwischen IP- und MAC-Adresse?
7. 1 Gbit/s entspricht theoretisch wie vielen MB/s?
8. PC erreicht den Drucker lokal, aber keine Webseite. Nenne zwei mögliche Ursachen und einen Test.
9. Wofür könnte LWL an einer Industrieanlage sinnvoll sein?
10. Warum beweist die Meldung „WLAN verbunden“ allein keine Internetverbindung?

**Danach:** [Lektion 5 – Software und Betriebssysteme](05_Software_Betriebssysteme.md).