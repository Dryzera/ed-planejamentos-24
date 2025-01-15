from docx import Document
from datetime import datetime
from project.settings import MEDIA_ROOT
import locale
import string
import random
from home.planejamento.api_ia.main_ia import generate_planning_ia

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

DEFAULT_SAVE_FOLDER = MEDIA_ROOT / 'files_docx_generated'

def generate_slug() -> str:
    return ''.join(random.choices(string.ascii_letters, k=15))

def init_generate_document(matters: list, date: str, term_for_ia: str, extra: str, school, teacher):
    try:
        date_formated = datetime.strptime(date, '%Y-%m-%d')
        date_exibs = datetime.strftime(date_formated, '%d de %B de %Y')
        document = Document()
        font = document.styles['Normal'].font
        font.name = 'Arial'
        document.add_heading(f'{school}, {date_exibs} - {teacher.first_name} {teacher.last_name}', 0).alignment

        for matter in matters:
            hour_formated = datetime.strptime(str(matter.hour), '%H:%M:%S')
            hour_exibs = datetime.strftime(hour_formated, '%Hh%M')

            info_aula = document.add_paragraph(f'{hour_exibs} - ')
            info_aula.add_run(matter.matter).bold = True

            term = term_for_ia[f'{matter.pk}']
            if term:
                document.add_paragraph(generate_planning_ia(term))
            else:
                document.add_paragraph('').add_run('(escreva aqui)').italic = True
            
        if extra:
            document.add_paragraph(extra)

        slug_name = generate_slug()
        file_name = DEFAULT_SAVE_FOLDER / f'planejamento_{slug_name}.docx'

        document.save(file_name)
        return slug_name
    except:
        # if raise any error, return False (this is treated on view)
        return False