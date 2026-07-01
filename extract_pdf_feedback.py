import sys, os
from pathlib import Path

pdf_path = Path(r'cyberfeedbackAvi.pdf')
output_path = Path(r'feedback_pdf.txt')

try:
    import PyPDF2
except ImportError:
    print('PyPDF2 not installed')
    sys.exit(1)

with open(pdf_path, 'rb') as f:
    reader = PyPDF2.PdfReader(f)
    text_chunks = []
    for page in reader.pages:
        text_chunks.append(page.extract_text() or '')
    full_text = '\n'.join(text_chunks)
    output_path.write_text(full_text, encoding='utf-8')
    print('Extracted PDF to', output_path)
