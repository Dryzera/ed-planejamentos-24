from docx import Document
from docx.shared import Inches
from datetime import datetime
from project.settings import BASE_DIR
import locale
import string
import random
from api_ia.main_ia import generate_planning_ia

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

DEFAULT_SAVE_FOLDER = BASE_DIR / 'files_docx_generated'

def generate_slug() -> str:
    return ''.join(random.choices(string.ascii_letters, k=15))

def init_generate_document(list_matters: list, date: str, term_for_ia):
    print(term_for_ia)
    try:
        date_formated = datetime.strptime(date, '%Y-%M-%d')
        date_exibs = datetime.strftime(date_formated, '%d de %B de %Y')
        document = Document()
        document.add_heading(f'Planejamento - {date_exibs}', 0)

        for matters in list_matters:
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

        slug_name = generate_slug()
        file_name = DEFAULT_SAVE_FOLDER / f'planejamento_{slug_name}.docx'

        document.save(file_name)
        return slug_name
    except:
        # if raise any error, return False (this is treated on view)
        return False