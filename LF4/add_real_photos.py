#!/usr/bin/env python3
"""Append freely licensed real connector and hardware photographs to the LF4 PDF.
Images are loaded at build time from Wikimedia Commons. Kept separate from the
schematic diagrams, since AI illustrations should not be used for pinouts.
"""
from pathlib import Path
from urllib.parse import quote
import io, time
import fitz
import requests
from PIL import Image

HERE=Path(__file__).resolve().parent
PDF=HERE/'LF4_Komplettlernbuch_AP1.pdf'
SOURCES=[
    ('Originalfotos: USB-Stecker und Buchsen','USB_types.jpg',
     'Von links: Mini-USB, Mini-USB, Standard-USB-B, Standard-USB-A-Buchse, Standard-USB-A-Stecker. Ein Größenvergleich.',
     'George Shuklin','Public Domain'),
    ('Originalfoto: SATA-Datenkabel','SATA-cable.jpg',
     'Echtes SATA-Datenkabel mit zwei Steckern. SATA-Strom ist ein separater, breiterer Anschluss.',
     'Evan-Amos','Public Domain'),
    ('Originalfoto: PC-Mainboard','Motherboard_computer.jpg',
     'Echte Hauptplatine eines PCs. Anschluesse und Steckplaetze unterscheiden sich je nach Modell.',
     'Iwan Gabovitch','Public Domain')
]
SESS=requests.Session()
SESS.headers['User-Agent']='AP1-LF4-StudyGuide/1.0 (educational open-media compilation)'
def download(name):
    url='https://commons.wikimedia.org/wiki/Special:Redirect/file/'+quote(name,safe='')
    r=SESS.get(url,timeout=40)
    r.raise_for_status()
    if not r.headers.get('Content-Type','').lower().startswith('image/'):
        raise ValueError('No picture data from '+url+': '+r.headers.get('Content-Type',''))
    data=r.content
    Image.open(io.BytesIO(data)).verify()
    return data
doc=fitz.open(PDF)
photos_added=0
for title,filename,caption,author,license in SOURCES:
    try:
        data=download(filename)
    except Exception as exc:
        print('PHOTO NOT EMBEDDED:',filename,str(exc)[:400])
        continue
    page=doc.new_page(width=595,height=842)
    page.draw_rect(fitz.Rect(0,0,595,95),color=None,fill=(0.07,.17,.29))
    page.insert_text((35,54),title,fontsize=18,color=(1,1,1),fontname='helv')
    frame=fitz.Rect(35,118,560,565)
    page.insert_image(frame,stream=data,keep_proportion=True)
    page.insert_textbox(fitz.Rect(38,595,555,656),caption,fontsize=11,color=(.10,.20,.30),fontname='helv')
    source='Foto: '+author+' | '+license+' | Wikimedia Commons: https://commons.wikimedia.org/wiki/File:'+filename
    page.insert_textbox(fitz.Rect(38,693,556,770),source,fontsize=8,color=(.25,.38,.48),fontname='helv')
    photos_added+=1
print('Embedded authentic photos:',photos_added)
if photos_added==0:
    raise RuntimeError('No authentic photo downloaded – refusing to claim image edition was produced')
tmp=PDF.with_suffix('.photo.tmp.pdf')
doc.save(tmp,garbage=4,deflate=True)
doc.close()
tmp.replace(PDF)
print('PDF size',PDF.stat().st_size)
