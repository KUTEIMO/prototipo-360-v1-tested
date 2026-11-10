import os
import shutil
import win32com.client
import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

CANVA_URL = "https://canva.link/s8g3tugujjg7h6f"
DEF_DIR = r"c:\Users\SOTO\APLICATIVOS\proyectos unisimon\ORBE360_ENTREGA_SEGUNDO_CORTE_70"
EDIT_DIR = r"c:\Users\SOTO\APLICATIVOS\proyectos unisimon\ORBE360_ENTREGA_SEGUNDO_CORTE_EDICION"

# 1. Update text file for Canva link in presentation folder
pres_txt = os.path.join(DEF_DIR, "02_Documentacion_y_Entregables_IEEE_1058", "6_Presentacion_Sustentacion", "ENLACE_PRESENTACION_CANVA_ORBE360.txt")
canva_content = f"""================================================================================
ORBE360 (PEVCI) - ENLACE OFICIAL DE DIAPOSITIVAS EN CANVA (SEGUNDO CORTE 70%)
UNIVERSIDAD SIMON BOLIVAR - GESTION DE PROYECTOS (2026-2)
DOCENTE EVALUADORA: ING. NATALY DUQUE PAEZ
================================================================================

ENLACE DIRECTO DE PRESENTACION EN CANVA:
>>> {CANVA_URL} <<<

EQUIPO DE DESARROLLO Y ROLES IEEE 1058:
1. Eduardo Soto       - Director de Proyecto & Arquitectura Frontend
2. Sebastian Omana    - Lider de Backend Convex DB, Datos y DevSecOps
3. Saraic Leon        - Lider de Accesibilidad Universal WCAG 2.1 AA & UX
4. Jesus Avendano     - Lider de Metricas, Estimacion (COCOMO II, PF) y PERT
5. Kevin Garcia       - Lider de Calidad QA, Trazabilidad Jira Cloud y Documentacion

================================================================================
DISTRIBUCION DE CONTENIDO POR EXPOSITOR:
- Slide 1: Portada Ejecutiva con Equipo y Enlaces (Eduardo Soto)
- Slide 2: Problema Institucional y Proposito Inclusivo (Eduardo Soto)
- Slide 3: Delimitacion Formal del 70% vs 30% segun Project Charter (Eduardo Soto)
- Slide 4: Estimacion Metrica Formal: Puntos de Funcion 400.84 PFA (Jesus Avendano)
- Slide 5: Modelo Matematico COCOMO II y Esfuerzo 59.40 PM (Jesus Avendano)
- Slide 6: Planificacion Predictiva: Cronograma Gantt 123 Tareas (Jesus Avendano)
- Slide 7: Red PERT, Precedencias y Ruta Critica (Jesus Avendano)
- Slide 8: Gestion Agil: Trazabilidad 1 a 1 en Jira Software Cloud KAN (Kevin Garcia)
- Slide 9: Arquitectura Frontend y Motor Virtual 360 (Eduardo Soto)
- Slide 10: Base de Datos en Tiempo Real y DevSecOps con Convex DB (Sebastian Omana)
- Slide 11: Motor de Accesibilidad Universal WCAG 2.1 AA (Saraic Leon)
- Slide 12: Gobierno de IA (Prompts IEEE 1058), Acuerdo QA y Cierre (Cierre de Equipo)
================================================================================
"""

with open(pres_txt, "w", encoding="utf-8") as f:
    f.write(canva_content)
print("Updated ENLACE_PRESENTACION_CANVA_ORBE360.txt")

# 2. Create a clean formal DOCX and PDF for the Canva Presentation link
doc_canva = docx.Document()
for sec in doc_canva.sections:
    sec.top_margin = Inches(0.8)
    sec.bottom_margin = Inches(0.8)
    sec.left_margin = Inches(0.8)
    sec.right_margin = Inches(0.8)

p_title = doc_canva.add_paragraph()
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p_title.add_run("UNIVERSIDAD SIMÓN BOLÍVAR - CÚCUTA\nGESTIÓN DE PROYECTOS DE SOFTWARE (2026-2)")
r.font.name = "Arial"
r.font.size = Pt(11)
r.font.color.rgb = RGBColor(90, 106, 126)
r.bold = True

p_h1 = doc_canva.add_paragraph()
p_h1.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p_h1.add_run("ENLACE OFICIAL DE LA PRESENTACIÓN EN CANVA\nPROYECTO ORBE360 (CORTE 2 - 70%)")
r.font.name = "Arial"
r.font.size = Pt(16)
r.font.color.rgb = RGBColor(2, 132, 199)
r.bold = True

doc_canva.add_paragraph()

# Table with Canva Link
t = doc_canva.add_table(rows=2, cols=1)
t.alignment = WD_TABLE_ALIGNMENT.CENTER
cell_top = t.cell(0, 0)
cell_top.paragraphs[0].text = "DIAPOSITIVAS OFICIALES DE LA SUSTENTACIÓN"
cell_top.paragraphs[0].runs[0].font.bold = True
cell_top.paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="0284C7"/>')
cell_top._tc.get_or_add_tcPr().append(shd)

cell_bot = t.cell(1, 0)
p_link = cell_bot.paragraphs[0]
p_link.add_run("Enlace directo a Canva (Modo Presentación):\n").font.size = Pt(10)
r_url = p_link.add_run(CANVA_URL)
r_url.bold = True
r_url.font.size = Pt(14)
r_url.font.color.rgb = RGBColor(2, 132, 199)
shd2 = parse_xml(f'<w:shd {nsdecls("w")} w:fill="F4F7FB"/>')
cell_bot._tc.get_or_add_tcPr().append(shd2)

doc_canva.add_paragraph()
p_meta = doc_canva.add_paragraph()
p_meta.add_run("Docente Evaluadora: ").bold = True
p_meta.add_run("Ing. Nataly Duque Páez\n")
p_meta.add_run("Equipo de Trabajo:\n").bold = True
p_meta.add_run("• Eduardo Soto (Líder / Arquitectura Frontend)\n• Sebastián Omaña (Líder Backend Convex DB & Seguridad)\n• Saraic León (Líder Accesibilidad WCAG 2.1 AA & UX)\n• Jesús Avendaño (Líder Métricas, Puntos de Función & PERT)\n• Kevin García (Líder Calidad QA, Jira Cloud & Documentación)\n")

p_note = doc_canva.add_paragraph()
r = p_note.add_run("Nota: Además del enlace en línea, la carpeta contiene la versión exportada en PDF (Sustentacion_Orbe360_Segundo_Corte.pdf) para visualización inmediata sin requerir conexión a internet.")
r.font.size = Pt(9.5)
r.font.italic = True
r.font.color.rgb = RGBColor(90, 106, 126)

canva_docx_path = os.path.join(DEF_DIR, "02_Documentacion_y_Entregables_IEEE_1058", "6_Presentacion_Sustentacion", "ENLACE_PRESENTACION_CANVA_ORBE360.docx")
doc_canva.save(canva_docx_path)
print("Saved ENLACE_PRESENTACION_CANVA_ORBE360.docx")

# Convert to PDF
word = win32com.client.Dispatch("Word.Application")
word.Visible = False
try:
    doc = word.Documents.Open(canva_docx_path)
    canva_pdf_path = os.path.join(DEF_DIR, "02_Documentacion_y_Entregables_IEEE_1058", "6_Presentacion_Sustentacion", "ENLACE_PRESENTACION_CANVA_ORBE360.pdf")
    doc.SaveAs(canva_pdf_path, FileFormat=17)
    doc.Close()
    print("Generated ENLACE_PRESENTACION_CANVA_ORBE360.pdf successfully!")
finally:
    word.Quit()
