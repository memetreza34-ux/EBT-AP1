#!/usr/bin/env python3
"""Build a complete German LF4 illustrated PDF from repository Markdown sources."""
from pathlib import Path
from html import escape
import markdown
from weasyprint import HTML
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'LF4_Komplettlernbuch_AP1.pdf'
CHAPTERS=[
'01_PC_Hardware.md','02_Stecker_Schnittstellen.md','03_Daten_Zahlensysteme.md',
'04_Netzwerke.md','05_Software_Betriebssysteme.md','06_IT_Sicherheit_Datenschutz.md',
'07_Auftrag_Planung_Beschaffung.md','08_Diagnose_Dokumentation.md',
'09_AP1_Probetraining.md','09_Musterloesungen.md']
CONNECTORS=[
('USB-A','breites Rechteck','USB-Peripherie'),
('USB-B','annähernd quadratisch','Drucker, Messgeräte'),
('USB-C','klein, oval-symmetrisch','USB-Daten/Strom, ggf. Bild'),
('RJ45 / 8P8C','acht Kontaktpositionen, Rastnase','Ethernet/LAN'),
('HDMI','flaches Trapez','digitales Bild und Ton'),
('DisplayPort','rechteckig, eine Ecke abgeschrägt','digitales Bild und Ton'),
('VGA / DE-15','D-Form, drei Kontaktreihen','analoges Bild'),
('DVI-D','breites Kontaktfeld','digitale Bildsignale'),
('3,5-mm-Klinke','runder Stift, Isolierringe','Audio'),
('PS/2','Mini-DIN, sechs Kontaktpositionen','ältere Tastaturen/Mäuse'),
('RS-232 / DE-9','D-Form, neun Kontaktpositionen','serielle Verbindung'),
('SATA-Daten','schmale L-Codierung, 7 Kontakte','Laufwerksdaten'),
('SATA-Strom','breite L-Codierung, 15 Kontakte','Laufwerksversorgung'),
('M.2','schmale Steckkarte mit Kerbe','häufig SSD'),
('PCIe','Erweiterungs-Steckkartenleiste','Erweiterungskarten'),
('DIMM','langes Speichermodul','Arbeitsspeicher')]
def icon(name,female=False):
  """Simplified vector icon. Not a manufacturer or dimension drawing."""
  n=name.lower(); a='#dbe6ee' if female else '#53667c'; inside='#223b55'
  b=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 148 82" width="140" height="76">']
  if 'klinke' in n:
    if female:
      b+=['<rect x="45" y="13" width="60" height="55" rx="8" fill="'+a+'" stroke="#16324a" stroke-width="2"/>','<circle cx="75" cy="40" r="19" fill="'+inside+'"/><circle cx="75" cy="40" r="9" fill="#667b8f"/>']
    else:
      b+=['<rect x="14" y="29" width="58" height="24" rx="10" fill="'+a+'"/>','<rect x="72" y="33" width="61" height="16" rx="6" fill="#f1bc55"/>','<path d="M92 33v16 M111 33v16" stroke="#16324a" stroke-width="5"/>']
  elif 'ps/2' in n:
    b+=['<circle cx="74" cy="41" r="33" fill="'+a+'" stroke="#16324a" stroke-width="3"/>','<circle cx="74" cy="41" r="26" fill="'+inside+'"/>']
    for x,y in [(59,30),(75,28),(90,30),(59,49),(75,51),(90,49)]:
      b+=['<circle cx="%d" cy="%d" r="3.3" fill="%s"/>'%(x,y,'#e8f1f7' if female else '#edb94a')]
  elif 'vga' in n or 'de-9' in n or 'rs-232' in n:
    b+=['<path d="M18 19H129L138 62H10Z" fill="'+a+'" stroke="#16324a" stroke-width="3"/>','<path d="M27 28H120L127 54H20Z" fill="'+inside+'"/>']
    rows=3 if 'vga' in n else 2; counts=[5,5,5] if rows==3 else [5,4]
    for ri,num in enumerate(counts):
      for j in range(num):
        b+=['<circle cx="%.1f" cy="%d" r="3" fill="%s"/>'%(46+j*14+(0 if num==5 else 7),35+ri*9,'#edf4f8' if female else '#eabc59')]
  elif 'usb-c' in n:
    b+=['<rect x="10" y="24" width="128" height="33" rx="16" fill="'+a+'" stroke="#16324a" stroke-width="2"/>','<rect x="18" y="30" width="111" height="21" rx="11" fill="'+inside+'"/>','<rect x="24" y="38" width="99" height="5" rx="2" fill="#d9e6ef"/>']
  elif 'usb-b' in n:
    b+=['<path d="M35 8H114L130 24V61L113 76H36L19 61V24Z" fill="'+a+'" stroke="#16324a" stroke-width="3"/>','<path d="M42 19H107L118 30V57L106 66H43L31 55V29Z" fill="'+inside+'"/>']
    for x,y in [(59,35),(88,35),(59,53),(88,53)]:
      b+=['<circle cx="%d" cy="%d" r="4" fill="#efbd60"/>'%(x,y)]
  elif 'usb-a' in n:
    b+=['<rect x="7" y="15" width="134" height="53" rx="5" fill="'+a+'" stroke="#16324a" stroke-width="3"/>','<rect x="17" y="25" width="113" height="33" rx="2" fill="'+inside+'"/>','<rect x="23" y="'+('26' if female else '44')+'" width="100" height="12" fill="#96b8d4"/>']
    for i in range(4):b+=['<rect x="%d" y="39" width="7" height="5" fill="#eabc59"/>'%(39+i*22)]
  elif 'rj45' in n:
    b+=['<path d="M21 11H126V28H137V69H10V28H21Z" fill="'+a+'" stroke="#16324a" stroke-width="3"/>','<rect x="27" y="22" width="94" height="36" fill="'+inside+'"/>']
    for i in range(8):b+=['<rect x="%d" y="25" width="7" height="17" fill="#eabc59"/>'%(30+i*11)]
  elif 'hdmi' in n:
    b+=['<path d="M9 20H139L125 63H23Z" fill="'+a+'" stroke="#16324a" stroke-width="3"/>','<path d="M26 29H121L112 54H35Z" fill="'+inside+'"/>']
    for i in range(10):b+=['<circle cx="%d" cy="41" r="2" fill="#eabc59"/>'%(38+i*8)]
  elif 'displayport' in n:
    b+=['<path d="M27 12H135V69H11V31Z" fill="'+a+'" stroke="#16324a" stroke-width="3"/>','<path d="M33 23H123V56H23V33Z" fill="'+inside+'"/>']
    for i in range(12):b+=['<rect x="%d" y="37" width="3" height="10" fill="#eabc59"/>'%(33+i*7)]
  elif 'dvi' in n:
    b+=['<rect x="7" y="18" width="134" height="47" rx="5" fill="'+a+'" stroke="#16324a" stroke-width="3"/>','<rect x="15" y="25" width="118" height="32" fill="'+inside+'"/>']
    for row in range(3):
      for i in range(8):b+=['<rect x="%d" y="%d" width="4" height="3" fill="#eabc59"/>'%(23+i*9,30+row*10)]
    b+=['<rect x="109" y="39" width="17" height="4" fill="#eabc59"/>']
  elif 'sata' in n:
    count=7 if 'daten' in n else 15
    b+=['<rect x="9" y="18" width="130" height="49" rx="4" fill="'+a+'" stroke="#16324a" stroke-width="3"/>','<path d="M24 31H126V53H36V46H24Z" fill="'+inside+'"/>']
    for i in range(count):
      b+=['<rect x="%.1f" y="33" width="%.1f" height="5" fill="#eabc59"/>'%(40+i*79/max(count-1,1),3 if count==7 else 2)]
  elif 'm.2' in n or 'pcie' in n or 'dimm' in n:
    if female:
      b+=['<rect x="7" y="30" width="134" height="23" rx="4" fill="'+a+'" stroke="#16324a" stroke-width="2"/>','<rect x="17" y="36" width="113" height="9" fill="'+inside+'"/>','<rect x="94" y="33" width="7" height="17" fill="#e1e9f0"/>']
    else:
      b+=['<rect x="7" y="15" width="134" height="46" rx="4" fill="#237c6e" stroke="#16324a" stroke-width="2"/>']
      for i in range(7):b+=['<rect x="%d" y="27" width="13" height="22" fill="#1a303f"/>'%(14+i*18)]
      for i in range(18):b+=['<rect x="%d" y="58" width="4" height="12" fill="#eabc59"/>'%(10+i*7)]
      b+=['<rect x="96" y="57" width="9" height="15" fill="white"/>']
  b+=['</svg>']
  return ''.join(b)
css=r'''@page{size:A4;margin:20mm 15mm 18mm 15mm;@top-left{content:"LF4  |  INFORMATIONSTECHNISCHE SYSTEME";font:8pt Lato;color:#4f6377} @bottom-right{content:counter(page);font:9pt Lato;color:#4f6377}}
@font-face{font-family:Lato;src:local("Lato")}
body{font-family:Lato,"DejaVu Sans",sans-serif;color:#223449;font-size:9.5pt;line-height:1.52}
.cover{height:205mm;background:#142b46;color:white;padding:20mm 12mm;box-sizing:border-box;border-radius:8mm;page-break-after:always}
.cover h1{font-size:32pt;line-height:1.2;color:white;border:0;margin:22mm 0 8mm}
.cover .eyebrow{display:inline-block;background:#15a8a0;padding:3mm 5mm;border-radius:3mm;font-weight:bold}
.cover p{font-size:13pt;color:#d4e9fa}
.cover .chip{margin-top:10mm;border-left:4px solid #e9b44e;padding-left:5mm}
h1{font-size:21pt;color:#153654;border-bottom:2px solid #11a7a0;padding-bottom:3mm;page-break-before:always;page-break-after:avoid}
h2{font-size:14pt;color:#165ca2;page-break-after:avoid;margin-top:6mm}
h3{font-size:11.5pt;color:#14344f;page-break-after:avoid}
table{width:100%;border-collapse:collapse;margin:3mm 0 5mm;font-size:8.4pt;page-break-inside:auto}
thead{display:table-header-group} tr{page-break-inside:avoid}
th{background:#185da5;color:white;text-align:left}td,th{padding:2mm 2.5mm;border-bottom:.3pt solid #dce5eb;vertical-align:top}
tr:nth-child(even) td{background:#f3f7fb}
pre{background:#f2f6fb;padding:4mm;white-space:pre-wrap;overflow-wrap:anywhere}
code{background:#eaf0f5;padding:0 1mm;overflow-wrap:anywhere}
blockquote{border-left:3pt solid #0da69b;background:#eef9f7;padding:2mm 4mm;margin:3mm 0}
li{margin-bottom:1mm}.intro{border:1px solid #d4e3ed;background:#eff6fb;border-radius:4mm;padding:4mm}
.connector-grid{display:grid;grid-template-columns:1fr 1fr;gap:4mm}
.connector-card{border:1px solid #d6e4eb;border-radius:3mm;page-break-inside:avoid;padding:2mm 3mm}
.connector-card h3{background:#153654;color:white;padding:1.8mm 3mm;margin:-2mm -3mm 3mm}
.pair{display:flex;justify-content:space-around;text-align:center}.pair>div{width:49%}.pair small{display:block;color:#66798c;font-size:7pt}
.connector-card p{margin:2mm 0;font-size:8pt}
section.chapter{page-break-before:always}
.legend{font-size:8pt;color:#536c80}
footer{font-size:8pt;color:#607388;margin-top:15mm}
'''
intro='''<div class="cover"><span class="eyebrow">AP1 LERNBUCH · LERNFELD 4</span><h1>Informationstechnische Systeme bereitstellen</h1><p>Das komplette Lernfeld 4: PC-Hardware, Stecker und Buchsen, Zahlensysteme, Netzwerke, Software, IT-Sicherheit, Planung, Diagnose und Übungen.</p><p class="chip">16 illustrierte Anschlusstypen · 8 Themenbereiche · 50-Punkte-Probeprüfung mit Musterlösungen</p></div><h1>Über dieses Lernbuch</h1><div class="intro">Dieses Buch fasst die Lernmodule des EBT-AP1-Repositories vollständig zusammen. Zusätzlich enthält es selbst erstellte, vereinfachte Vektorzeichnungen von Steckern, Buchsen und internen Steckplätzen. Die Grafiken sind schematisch und nicht maßstabsgetreu; für echte Anschlüsse gelten die jeweiligen Herstellerangaben.</div><h2>Lernweg</h2><ol><li>Kapitel lesen und Begriffe verstehen.</li><li>Zu jedem Stecker die passende Buchse lernen.</li><li>Berechnungen selbst mit Zwischenschritten lösen.</li><li>Übungsfragen ohne Lösungen bearbeiten.</li><li>Mit den Musterlösungen kontrollieren.</li></ol>'''
cards=[]
for n,shape,use in CONNECTORS:
  cards.append('<div class="connector-card"><h3>'+escape(n)+'</h3><div class="pair"><div>'+icon(n,False)+'<small>Stecker / Modul</small></div><div>'+icon(n,True)+'<small>Buchse / Steckplatz</small></div></div><p><b>Erkennen:</b> '+escape(shape)+'<br/><b>Verwendung:</b> '+escape(use)+'</p></div>')
atlas='<section class="chapter"><h1>Stecker- und Buchsenatlas: 16 Typen</h1><p class="legend">Links schematisches Steckteil bzw. Modul, rechts zugehörige Buchse bzw. Steckplatz. Bei DE-9 sind auch Steckteile mit weiblichen Kontaktöffnungen üblich.</p><div class="connector-grid">'+''.join(cards)+'</div></section>'
parts=[intro,atlas]
for i,path in enumerate(CHAPTERS):
  f=ROOT/path
  if not f.exists():continue
  html=markdown.markdown(f.read_text(encoding='utf-8'),extensions=['tables','fenced_code','sane_lists'])
  parts.append('<section class="chapter"><h1>Kapitel '+str(i+1)+': '+escape(f.stem.replace('_',' '))+'</h1>'+html+'</section>')
parts.append('<footer>Quellenbasis: LF4-Projektmaterial EBT-AP1 und der darin verlinkte BIBB-Ausbildungsrahmen. Eigenes Trainingsmaterial, keine offizielle IHK/PAL-Prüfung.</footer>')
HTML(string='<html lang="de"><head><meta charset="utf-8"><style>'+css+'</style></head><body>'+''.join(parts)+'</body></html>',base_url=str(ROOT)).write_pdf(OUT)
print('Erstellt:',OUT,OUT.stat().st_size)
