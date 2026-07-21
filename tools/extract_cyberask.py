import docx, json, sys
from pathlib import Path

DOCX_PATH = Path(r'cyberask0107.docx')
OUT_PATH = Path(r'cyberask0107.txt')

def extract_text(path):
    doc = docx.Document(path)
    paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
    return "\n".join(paragraphs)

text = extract_text(DOCX_PATH)
OUT_PATH.write_text(text, encoding='utf-8')
print('Extracted to', OUT_PATH)
