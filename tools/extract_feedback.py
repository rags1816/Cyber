import zipfile
import xml.etree.ElementTree as ET
import os

docx_path = r'cyberfeedbackAvi.docx'
output_path = r'feedback.txt'

with zipfile.ZipFile(docx_path, 'r') as z:
    with z.open('word/document.xml') as f:
        xml_bytes = f.read()
        root = ET.fromstring(xml_bytes)
        # Namespace handling
        ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        texts = []
        for node in root.iterfind('.//w:t', ns):
            texts.append(node.text)
        full_text = '\n'.join(filter(None, texts))
        with open(output_path, 'w', encoding='utf-8') as out:
            out.write(full_text)
print('Extracted to', output_path)
