import subprocess
from django.conf import settings

def convert_to_docx(slug):
    docx_path = settings.MEDIA_ROOT / f'files_docx_generated/planejamento_{slug}.docx'
    pdf_path = settings.MEDIA_ROOT / f'files_docx_generated/planejamento_{slug}.pdf'
    try:
        subprocess.run(["pandoc", docx_path, "-o", pdf_path], check=True)
        print(f"PDF salvo em: {pdf_path}")
    except subprocess.CalledProcessError as e:
        print(f"Erro na conversão: {e}")