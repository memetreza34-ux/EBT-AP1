"""Build the GitHub-hosted Tag 2 PDF from the maintained Markdown appendix."""
from pathlib import Path
import mistune
from weasyprint import HTML
from pypdf import PdfReader, PdfWriter

root=Path(__file__).resolve().parents[1]
appendix_md=root/'LF2/Tag_2_Abschlusspruefung_60_Punkte_mit_Auswertung.md'
appendix_pdf=appendix_md.with_suffix('.pdf')
booklet_pdf=root/'LF2/Tag_2_Ultra_Lernskript_Leitungen_Berechnungen.pdf'
html_body=mistune.create_markdown(plugins=['table'])(appendix_md.read_text(encoding='utf-8'))
css='''
@page{size:A4;margin:19mm 18mm 22mm 18mm;@bottom-left{content:"LF2 / TAG 2  ·  AP1-orientierte Übungsprüfung";font-size:7pt;color:#526174;}@bottom-right{content:counter(page);font-size:7pt;color:#526174;}}
body{font-family:DejaVu Sans,Arial,sans-serif;font-size:9.1pt;line-height:1.43;color:#102B4B}h1{font-size:22pt;color:#102B4B;line-height:1.18;margin:12pt 0 20pt}h2{font-size:16pt;color:#164B83;margin:22pt 0 9pt;padding-bottom:5pt;border-bottom:1px solid #D6E1ED;break-after:avoid}h3{font-size:11.5pt;color:#164B83;margin:15pt 0 5pt;break-after:avoid}p{margin:4pt 0 9pt}li{margin:4pt 0}strong{font-weight:700}table{border-collapse:collapse;width:100%;margin:12pt 0 15pt;font-size:8pt}th,td{border-bottom:1px solid #D6E1ED;padding:6pt 7pt;text-align:left}th{background:#EFF6FC;color:#164B83}tr{break-inside:avoid}blockquote{padding:10pt 14pt;border-left:4px solid #1F806B;background:#EFF6FC;margin:12pt 0}code{font-family:DejaVu Sans Mono,monospace;font-size:.91em;color:#102B4B;overflow-wrap:anywhere}hr{border:0;border-top:1pt solid #D6E1ED;margin:20pt 0}h2,h3{page-break-after:avoid}ul,ol{padding-left:21pt}
'''
HTML(string='<html lang="de"><meta charset="utf-8"><style>'+css+'</style><body>'+html_body+'</body></html>',base_url=str(root)).write_pdf(appendix_pdf)
book=PdfReader(booklet_pdf); extra=PdfReader(appendix_pdf)
if len(book.pages)<29:raise RuntimeError('Die 29 Originalseiten fehlen')
writer=PdfWriter()
for p in book.pages[:29]:writer.add_page(p)
for p in extra.pages:writer.add_page(p)
writer.add_metadata({'/Title':'LF2 Tag 2 - 8 Lektionen mit 60-Punkte-Abschlusspruefung', '/Author':'EBT AP1 Lernmaterial'})
with booklet_pdf.open('wb') as f: writer.write(f)
print('Erstellt',appendix_pdf,'Seiten',len(extra.pages),'Gesamtseiten',len(writer.pages))