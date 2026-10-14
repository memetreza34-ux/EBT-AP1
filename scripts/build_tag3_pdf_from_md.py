#!/usr/bin/env python3
"""Build the Tag 3 AP1 PDF study guide from the versioned Markdown source."""
from __future__ import annotations
import pathlib
import re

import mistune
from weasyprint import HTML

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT / "LF2" / "Tag_3_Ultra_Lernskript_Schutz_und_Netzsysteme.md"
DST = ROOT / "LF2" / "Tag_3_Ultra_Lernskript_Schutz_und_Netzsysteme.pdf"

CSS = r"""
@page {
  size: A4;
  margin: 21mm 17mm 19mm 17mm;
  @top-left { content: "EBT · AP1  |  LERNFELD 2"; font-family: "DejaVu Sans", sans-serif; font-size: 8pt; font-weight: 700; letter-spacing: .7px; color: #557087; }
  @top-right { content: "TAG 3  ·  14.10.2026"; font-family: "DejaVu Sans", sans-serif; font-size: 8pt; color: #557087; }
  @bottom-left { content: "Netzsysteme · FI · LS · Schutzmaßnahmen"; font-family: "DejaVu Sans", sans-serif; font-size: 7.5pt; color: #6f8795; }
  @bottom-right { content: "Seite " counter(page) " / " counter(pages); font-family: "DejaVu Sans", sans-serif; font-size: 8pt; color: #6f8795; }
}
@page:first {
  @top-left { content: none; }
  @top-right { content: none; }
}
* { box-sizing: border-box; }
html { color: #243647; }
body { font-family: "DejaVu Sans", Arial, sans-serif; font-size: 10.25pt; line-height: 1.49; }
h1, h2, h3 { font-family: "DejaVu Sans", Arial, sans-serif; break-after: avoid; }
h1 { font-size: 19.7pt; color: #0f4165; padding-bottom: 8px; border-bottom: 2.5px solid #90b6cd; margin-top: 0; margin-bottom: 14px; letter-spacing: -.35px; }
h1:not(:first-child) { break-before: page; }
h2 { font-size: 13pt; color: #115b83; margin: 17px 0 7px; }
h3 { font-size: 11.3pt; color: #15506f; margin: 13px 0 5px; }
p { margin: 7px 0; orphans: 3; widows: 3; }
ul, ol { padding-left: 19px; margin: 5px 0 10px; }
li { margin: 3px 0; }
strong { color: #173f58; }
em { color: #395064; }
blockquote { border-left: 4px solid #508cac; background: #edf4f7; padding: 7px 13px; margin: 13px 0 16px; color: #284a5f; }
blockquote p { margin: 4px 0; }
hr { border: 0; border-top: 1px solid #d3e0e9; margin: 13px 0; }
table { width: 100%; table-layout: fixed; border-collapse: collapse; margin: 9px 0 16px; font-size: 8.5pt; line-height: 1.34; }
thead { display: table-header-group; }
tr { break-inside: avoid; }
th { background: #dcebf3; color: #153c54; font-weight: 700; text-align: left; border: 1px solid #d1e0e8; padding: 6px 7px; overflow-wrap: anywhere; }
td { border: 1px solid #dbe5ec; padding: 6px 7px; vertical-align: top; overflow-wrap: anywhere; }
tbody tr:nth-child(even) { background: #f5f9fb; }
code { font-family: "DejaVu Sans Mono", monospace; font-size: .9em; background: #eef3f6; padding: 1px 3px; }
pre { white-space: pre-wrap; overflow-wrap: anywhere; background: #eef3f6; border-radius: 5px; padding: 8px; }
pre code { background: transparent; }
a { color: #13658c; }
h1:first-child { background: #123f5b; color: white; border: none; padding: 26px 19px; border-radius: 5px; margin-bottom: 10px; font-size: 24pt; }
h1:first-child + h2 { font-size: 16.5pt; color: #155a80; margin-top: 11px; }
"""

def main() -> None:
    source = SRC.read_text(encoding="utf-8")
    if len(source) < 10000:
        raise ValueError("Study guide unexpectedly short.")
    markdown = mistune.create_markdown(plugins=["table"])
    body = markdown(source)
    html = (
        '<!DOCTYPE html><html lang="de"><head><meta charset="utf-8">'
        '<title>Tag 3 – LF2 AP1: Schutzmaßnahmen und Netzsysteme</title>'
        "<style>" + CSS + "</style></head><body>" + body + "</body></html>"
    )
    DST.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=html, base_url=str(ROOT)).write_pdf(str(DST))
    from pypdf import PdfReader
    reader = PdfReader(str(DST))
    extracted = "\n".join(page.extract_text() or "" for page in reader.pages)
    required = ["TN-C-S", "Summenstromwandler", "Schutzpotentialausgleich", "PELV", "IP65"]
    missing = [w for w in required if w not in extracted]
    if missing:
        raise ValueError(f"PDF content incomplete: {missing}")
    if len(reader.pages) < 10:
        raise ValueError(f"Unexpected PDF page count: {len(reader.pages)}")
    print(f"Built {DST} ({DST.stat().st_size} bytes; {len(reader.pages)} pages)")

if __name__ == "__main__":
    main()
