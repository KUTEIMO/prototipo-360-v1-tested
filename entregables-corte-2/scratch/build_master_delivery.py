import os
import shutil
import zipfile
import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
import win32com.client

MASTER_DIR = r"c:\Users\SOTO\APLICATIVOS\proyectos unisimon\ORBE360_ENTREGA_SEGUNDO_CORTE_70"
SOURCE_ORBE_GP = r"c:\Users\SOTO\APLICATIVOS\proyectos unisimon\ORBE-GP"
SOURCE_ENTREGABLES = r"c:\Users\SOTO\APLICATIVOS\proyectos unisimon\ORBE\entregables-corte-2"

print("Iniciando construccion del paquete de entrega...")
os.makedirs(MASTER_DIR, exist_ok=True)

# 2. Definir rutas internas
dir_software = os.path.join(MASTER_DIR, "01_Software_Desarrollado_70_Porciento")
dir_docs = os.path.join(MASTER_DIR, "02_Documentacion_y_Entregables_IEEE_1058")
os.makedirs(dir_software, exist_ok=True)
os.makedirs(dir_docs, exist_ok=True)

dir_charter = os.path.join(dir_docs, "1_Acta_Constitucion_Project_Charter_70_30")
dir_gantt = os.path.join(dir_docs, "2_Planificacion_Gantt_y_WBS")
dir_excel = os.path.join(dir_docs, "3_Estimacion_Metrica_Excel_Puntos_de_Funcion_y_PERT")
dir_jira = os.path.join(dir_docs, "4_Gestion_Agil_Jira_Cloud")
dir_prompts = os.path.join(dir_docs, "5_Procesos_Tecnicos_y_Prompts_IA")
dir_sustentacion = os.path.join(dir_docs, "6_Presentacion_Sustentacion")

for d in [dir_charter, dir_gantt, dir_excel, dir_jira, dir_prompts, dir_sustentacion]:
    os.makedirs(d, exist_ok=True)

print("Directorios IEEE 1058 listos.")

# 3. Copiar Software desarrollado si no existe
dest_orbe_gp = os.path.join(dir_software, "ORBE-GP")
if not os.path.exists(dest_orbe_gp):
    print("Copiando codigo y assets de ORBE-GP a carpeta descomprimida...")
    shutil.copytree(
        SOURCE_ORBE_GP,
        dest_orbe_gp,
        ignore=shutil.ignore_patterns(".git", "*.zip", ".DS_Store", "desktop.ini", "Thumbs.db")
    )
    print("ORBE-GP copiado exitosamente.")
else:
    print("Carpeta descomprimida ORBE-GP ya existe.")

# 4. Crear ZIP si no existe
zip_file_path = os.path.join(dir_software, "ORBE-GP-Software-70.zip")
if not os.path.exists(zip_file_path) or os.path.getsize(zip_file_path) < 1000000:
    print("Generando archivo ZIP de ORBE-GP...")
    with zipfile.ZipFile(zip_file_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(dest_orbe_gp):
            dirs[:] = [d for d in dirs if d not in [".git", "temp", "tmp"]]
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, dir_software)
                zipf.write(file_path, arcname)
    print(f"ZIP generado: {zip_file_path} (Tamanio: {os.path.getsize(zip_file_path):,} bytes)")
else:
    print(f"Archivo ZIP ya existe ({os.path.getsize(zip_file_path):,} bytes).")

# 5. Copiar documentos a sus carpetas correspondientes
print("Copiando documentos de gestion y metricas...")

# 1_Acta_Constitucion_Project_Charter_70_30
shutil.copy2(
    os.path.join(SOURCE_ENTREGABLES, "ENTREGABLES_DEFINITIVOS", "1_Inicio_y_Project_Charter", "acta_constitucion_proyecto_charter_CORTE2.docx"),
    os.path.join(dir_charter, "acta_constitucion_proyecto_charter_CORTE2.docx")
)
shutil.copy2(
    os.path.join(SOURCE_ENTREGABLES, "ENTREGABLES_DEFINITIVOS", "1_Inicio_y_Project_Charter", "acta_constitucion_proyecto_charter_CORTE2.pdf"),
    os.path.join(dir_charter, "acta_constitucion_proyecto_charter_CORTE2.pdf")
)

# 2_Planificacion_Gantt_y_WBS
shutil.copy2(
    os.path.join(SOURCE_ENTREGABLES, "ENTREGABLES_DEFINITIVOS", "5_Metricas_WBS_Gantt_y_PERT", "GANTT_ORBE360_CORTE_2.gan"),
    os.path.join(dir_gantt, "GANTT_ORBE360_CORTE_2.gan")
)
shutil.copy2(
    os.path.join(SOURCE_ENTREGABLES, "ENTREGABLES_DEFINITIVOS", "5_Metricas_WBS_Gantt_y_PERT", "GANTT_ORBE360_CORTE_2.png"),
    os.path.join(dir_gantt, "GANTT_ORBE360_CORTE_2.png")
)
shutil.copy2(
    os.path.join(SOURCE_ENTREGABLES, "ENTREGABLES_DEFINITIVOS", "5_Metricas_WBS_Gantt_y_PERT", "REPORTE_RECURSOS_GANTT.html"),
    os.path.join(dir_gantt, "REPORTE_RECURSOS_GANTT.html")
)

# 3_Estimacion_Metrica_Excel_Puntos_de_Funcion_y_PERT
shutil.copy2(
    os.path.join(SOURCE_ENTREGABLES, "ENTREGABLES_DEFINITIVOS", "5_Metricas_WBS_Gantt_y_PERT", "Gestion de proyectos 222 nuevo.xlsx"),
    os.path.join(dir_excel, "Gestion de proyectos 222 nuevo.xlsx")
)
shutil.copy2(
    os.path.join(SOURCE_ENTREGABLES, "ENTREGABLES_DEFINITIVOS", "5_Metricas_WBS_Gantt_y_PERT", "DIAGRAMA_PERT_RED.html"),
    os.path.join(dir_excel, "DIAGRAMA_PERT_RED.html")
)

# 4_Gestion_Agil_Jira_Cloud
shutil.copy2(
    os.path.join(SOURCE_ENTREGABLES, "ENTREGABLES_DEFINITIVOS", "3_Gestion_Agil_Jira_Cloud", "DOCUMENTO_ENLACE_JIRA_ORBE360.docx"),
    os.path.join(dir_jira, "DOCUMENTO_ENLACE_JIRA_ORBE360.docx")
)
shutil.copy2(
    os.path.join(SOURCE_ENTREGABLES, "ENTREGABLES_DEFINITIVOS", "3_Gestion_Agil_Jira_Cloud", "DOCUMENTO_ENLACE_JIRA_ORBE360.pdf"),
    os.path.join(dir_jira, "DOCUMENTO_ENLACE_JIRA_ORBE360.pdf")
)
shutil.copy2(
    os.path.join(SOURCE_ENTREGABLES, "ENTREGABLES_DEFINITIVOS", "3_Gestion_Agil_Jira_Cloud", "MATRIZ_TRAZABILIDAD_GANTT_JIRA_EXCEL.md"),
    os.path.join(dir_jira, "MATRIZ_TRAZABILIDAD_GANTT_JIRA_EXCEL.md")
)
shutil.copy2(
    os.path.join(SOURCE_ENTREGABLES, "ENTREGABLES_DEFINITIVOS", "CUENTAS_Y_CREDENCIALES_PROYECTO.txt"),
    os.path.join(dir_jira, "CUENTAS_Y_CREDENCIALES_PROYECTO.txt")
)

# 5_Procesos_Tecnicos_y_Prompts_IA
shutil.copy2(
    os.path.join(SOURCE_ENTREGABLES, "ENTREGABLES_DEFINITIVOS", "4_Procesos_Tecnicos_y_Prompts_IA", "DOCUMENTO_OFICIAL_PROMPTS_AGENTES_IA.docx"),
    os.path.join(dir_prompts, "DOCUMENTO_OFICIAL_PROMPTS_AGENTES_IA.docx")
)
shutil.copy2(
    os.path.join(SOURCE_ENTREGABLES, "ENTREGABLES_DEFINITIVOS", "4_Procesos_Tecnicos_y_Prompts_IA", "DOCUMENTO_OFICIAL_PROMPTS_AGENTES_IA.pdf"),
    os.path.join(dir_prompts, "DOCUMENTO_OFICIAL_PROMPTS_AGENTES_IA.pdf")
)

# Copiar el formato IEEE 1058 buscando por nombre sin problemas de acentos
formatos_dir = os.path.join(SOURCE_ENTREGABLES, "formatos")
for f in os.listdir(formatos_dir):
    if "IEEE" in f and f.endswith(".docx"):
        src_ieee = os.path.join(formatos_dir, f)
        dst_ieee = os.path.join(dir_prompts, "Planificacion_de_Procesos_Tecnicos_IEEE_1058.docx")
        shutil.copy2(src_ieee, dst_ieee)
        print("Copiado marco IEEE 1058 a Procesos Tecnicos.")
        break

# 6_Presentacion_Sustentacion
shutil.copy2(
    os.path.join(SOURCE_ENTREGABLES, "presentacion", "Sustentacion_Orbe360_Segundo_Corte.pptx"),
    os.path.join(dir_sustentacion, "Sustentacion_Orbe360_Segundo_Corte.pptx")
)
shutil.copy2(
    os.path.join(SOURCE_ENTREGABLES, "presentacion", "Sustentacion_Orbe360_Segundo_Corte.pdf"),
    os.path.join(dir_sustentacion, "Sustentacion_Orbe360_Segundo_Corte.pdf")
)
shutil.copy2(
    os.path.join(SOURCE_ENTREGABLES, "ENTREGABLES_DEFINITIVOS", "2_Organizacion_del_Equipo_y_Sustentacion", "GUION_MAESTRO_SUSTENTACION.md"),
    os.path.join(dir_sustentacion, "GUION_MAESTRO_SUSTENTACION.md")
)
guiones_dest = os.path.join(dir_sustentacion, "GUIONES_INDIVIDUALES")
shutil.copytree(
    os.path.join(SOURCE_ENTREGABLES, "ENTREGABLES_DEFINITIVOS", "GUIONES_INDIVIDUALES"),
    guiones_dest,
    dirs_exist_ok=True
)

print("Documentos copiados a sus carpetas.")

# 6. Crear documento formal de portada / indice: LEAME_PRIMERO_ENTREGA_CORTE_2.docx
doc_leame = docx.Document()

for section in doc_leame.sections:
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)

normal_style = doc_leame.styles['Normal']
normal_style.font.name = 'Calibri'
normal_style.font.size = Pt(11)
normal_style.font.color.rgb = RGBColor(0x33, 0x33, 0x33)

def set_cell_bg(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>'))

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

p_head = doc_leame.add_paragraph()
p_head.alignment = WD_ALIGN_PARAGRAPH.CENTER
r_univ = p_head.add_run("UNIVERSIDAD SIMON BOLIVAR\nFACULTAD DE INGENIERIAS — PROGRAMA DE INGENIERIA DE SISTEMAS\n")
r_univ.font.size = Pt(10)
r_univ.font.bold = True
r_univ.font.color.rgb = RGBColor(0x00, 0x33, 0x66)

r_title = p_head.add_run("ENTREGA OFICIAL DE SEGUNDO CORTE (70% DE DESARROLLO)\nESTRUCTURACION DE PROCESOS TECNICOS BAJO NORMA IEEE 1058\n")
r_title.font.size = Pt(13)
r_title.font.bold = True
r_title.font.color.rgb = RGBColor(0x00, 0x22, 0x44)

r_sub = p_head.add_run("PROYECTO: ORBE360 (PEVCI) — CAMPUS VIRTUAL INCLUSIVO\nDocente Evaluadora: Ing. Nataly Duque Paez | Semestre Academico: 2026-2\n")
r_sub.font.size = Pt(10)
r_sub.font.italic = True
r_sub.font.color.rgb = RGBColor(0x55, 0x55, 0x55)

p_team = doc_leame.add_paragraph()
p_team.paragraph_format.space_before = Pt(8)
p_team.paragraph_format.space_after = Pt(8)
r_t1 = p_team.add_run("Integrantes del Equipo de Proyecto:\n")
r_t1.bold = True
r_t1.font.color.rgb = RGBColor(0x00, 0x33, 0x66)

integrantes = [
    ("Eduardo Jose Soto Herrera", "e_soto2@unisimon.edu.co", "Lider General de Proyecto & Arquitecto Frontend 360"),
    ("Saraic Noemi Leon Hernandez", "s_leon3@unisimon.edu.co", "Lider de Calidad & Especialista en Accesibilidad WCAG"),
    ("Kevin Eduardo Garcia Moreno", "k_garcia8@unisimon.edu.co", "Lider Backend & Gestion de Requerimientos Jira"),
    ("Sebastian David Omana Villamizar", "s_omana1@unisimon.edu.co", "Ingeniero DevSecOps & Infraestructura Base de Datos"),
    ("Jesus Omar Avendano Avendano", "j_avendano4@unisimon.edu.co", "Ingeniero de Planificacion, Cronograma & Estimacion")
]
for nom, cor, rol in integrantes:
    p_item = doc_leame.add_paragraph()
    p_item.paragraph_format.space_before = Pt(0)
    p_item.paragraph_format.space_after = Pt(2)
    p_item.paragraph_format.left_indent = Inches(0.25)
    r_n = p_item.add_run(f"• {nom}")
    r_n.bold = True
    p_item.add_run(f" ({cor}) — {rol}")

p_sec1 = doc_leame.add_paragraph()
p_sec1.paragraph_format.space_before = Pt(12)
r_s1 = p_sec1.add_run("1. MATRIZ DE CONFORMIDAD Y UBICACION DE ENTREGABLES")
r_s1.bold = True
r_s1.font.size = Pt(11)
r_s1.font.color.rgb = RGBColor(0x00, 0x33, 0x66)

table = doc_leame.add_table(rows=1, cols=3)
table.alignment = WD_TABLE_ALIGNMENT.CENTER
table.autofit = False

headers = ["Item Exigido por la Docente", "Carpeta Oficial (IEEE 1058)", "Archivo Especifico Incluido"]
hdr_widths = [Inches(2.2), Inches(2.2), Inches(2.1)]
for i, name in enumerate(headers):
    cell = table.rows[0].cells[i]
    cell.width = hdr_widths[i]
    set_cell_bg(cell, "003366")
    set_cell_margins(cell, top=120, bottom=120, left=140, right=140)
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(name)
    r.bold = True
    r.font.size = Pt(9.5)
    r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

items_docente = [
    ("Link para subir al Drive el software", "01_Software_Desarrollado_70_Porciento/", "ORBE-GP/ (Descomprimido) y ORBE-GP-Software-70.zip"),
    ("Gantt Project", "02_Documentacion_y_Entregables_IEEE_1058/2_Planificacion_Gantt_y_WBS/", "GANTT_ORBE360_CORTE_2.gan y GANTT_ORBE360_CORTE_2.png"),
    ("Excel Puntos de Funcion y PERT", "02_Documentacion_y_Entregables_IEEE_1058/3_Estimacion_Metrica_Excel_Puntos_de_Funcion_y_PERT/", "Gestion de proyectos 222 nuevo.xlsx (Hojas: IFPUG, COCOMO II, PERT y Ruta Critica)"),
    ("Acta Constitucion Charter (70% y 30%)", "02_Documentacion_y_Entregables_IEEE_1058/1_Acta_Constitucion_Project_Charter_70_30/", "acta_constitucion_proyecto_charter_CORTE2.docx y .pdf"),
    ("Proyecto Desarrollado 70%", "01_Software_Desarrollado_70_Porciento/", "ORBE-GP/ (62 escenas 360, audios Salome, subtitulos WebVTT e INICIAR_PROYECTO.bat)"),
    ("Documento Word del Prompt e IA", "02_Documentacion_y_Entregables_IEEE_1058/5_Procesos_Tecnicos_y_Prompts_IA/", "DOCUMENTO_OFICIAL_PROMPTS_AGENTES_IA.docx y .pdf"),
    ("Presentacion de la Sustentacion", "02_Documentacion_y_Entregables_IEEE_1058/6_Presentacion_Sustentacion/", "Sustentacion_Orbe360_Segundo_Corte.pptx y .pdf"),
    ("Link de Jira en un Doc Word", "02_Documentacion_y_Entregables_IEEE_1058/4_Gestion_Agil_Jira_Cloud/", "DOCUMENTO_ENLACE_JIRA_ORBE360.docx y .pdf"),
    ("Procesos Tecnicos segun IEEE 1058", "02_Documentacion_y_Entregables_IEEE_1058/", "Estructuracion normalizada de carpetas y Planificacion_de_Procesos_Tecnicos_IEEE_1058.docx")
]

for idx, (req, carp, arch) in enumerate(items_docente):
    row = table.add_row()
    bg = "F4F6F9" if idx % 2 == 1 else "FFFFFF"
    for c_i, text in enumerate([req, carp, arch]):
        cell = row.cells[c_i]
        cell.width = hdr_widths[c_i]
        set_cell_bg(cell, bg)
        set_cell_margins(cell, top=80, bottom=80, left=120, right=120)
        p = cell.paragraphs[0]
        r = p.add_run(text)
        r.font.size = Pt(9)
        if c_i == 0:
            r.bold = True

p_sec2 = doc_leame.add_paragraph()
p_sec2.paragraph_format.space_before = Pt(12)
r_s2 = p_sec2.add_run("2. ENLACES OFICIALES EN LINEA Y ACCESOS DEL PROYECTO")
r_s2.bold = True
r_s2.font.size = Pt(11)
r_s2.font.color.rgb = RGBColor(0x00, 0x33, 0x66)

enlaces = [
    ("Repositorio GitHub Oficial (ORBE-GP):", "https://github.com/KUTEIMO/ORBE-GP"),
    ("Tablero Jira Software Cloud:", "https://orbe-experience360.atlassian.net/jira/software/projects/KAN/boards"),
    ("Resumen Ejecutivo Jira:", "https://orbe-experience360.atlassian.net/jira/software/projects/KAN/summary"),
    ("Carpeta OneDrive/SharePoint Docente:", "https://unisimonedu-my.sharepoint.com/:f:/g/personal/nataly_duquep_unisimon_edu_co/IgCDRbT32DI0RYKHcylj9cxVAbtjusyMMuwxKrXtXb7X8D4?e=YKLsou")
]
for tit, url in enlaces:
    p_enlace = doc_leame.add_paragraph()
    p_enlace.paragraph_format.space_before = Pt(0)
    p_enlace.paragraph_format.space_after = Pt(2)
    p_enlace.paragraph_format.left_indent = Inches(0.25)
    r_tit = p_enlace.add_run(f"• {tit} ")
    r_tit.bold = True
    r_u = p_enlace.add_run(url)
    r_u.font.color.rgb = RGBColor(0x00, 0x44, 0x88)
    r_u.underline = True

p_sec3 = doc_leame.add_paragraph()
p_sec3.paragraph_format.space_before = Pt(12)
r_s3 = p_sec3.add_run("3. GUIA DE EJECUCION DEL SOFTWARE DESARROLLADO (70%)")
r_s3.bold = True
r_s3.font.size = Pt(11)
r_s3.font.color.rgb = RGBColor(0x00, 0x33, 0x66)

p_inst = doc_leame.add_paragraph()
p_inst.paragraph_format.space_before = Pt(2)
p_inst.paragraph_format.space_after = Pt(2)
p_inst.add_run("El software puede ejecutarse de manera inmediata en cualquier computador mediante cualquiera de las siguientes tres modalidades:\n\n"
               "• Modalidad 1 (Doble Clic Local): Abra la carpeta '01_Software_Desarrollado_70_Porciento/ORBE-GP' y ejecute el archivo 'INICIAR_PROYECTO.bat'. Este script verifica Node.js, abre el navegador en http://localhost:8081/ y levanta el servidor local de forma automatica.\n"
               "• Modalidad 2 (Comando NPM / Node): En una terminal dentro de 'ORBE-GP', ejecute 'npm start' o 'node scripts/dev-server.mjs' y navegue a http://localhost:8081/.\n"
               "• Modalidad 3 (Desde GitHub por PowerShell en una sola linea):\n"
               "  cd $HOME; if (-not (Test-Path \"ORBE-GP\")) { git clone https://github.com/KUTEIMO/ORBE-GP.git }; cd ORBE-GP; Start-Process \"http://localhost:8081/\"; node scripts/dev-server.mjs")

doc_leame_path = os.path.join(MASTER_DIR, "LEAME_PRIMERO_ENTREGA_CORTE_2.docx")
doc_leame.save(doc_leame_path)
print(f"Documento guardado: {doc_leame_path}")

word = win32com.client.Dispatch("Word.Application")
word.Visible = False
doc_opened = word.Documents.Open(doc_leame_path)
pdf_leame_path = os.path.join(MASTER_DIR, "LEAME_PRIMERO_ENTREGA_CORTE_2.pdf")
doc_opened.SaveAs(pdf_leame_path, FileFormat=17)
doc_opened.Close()
word.Quit()
print(f"PDF generado: {pdf_leame_path} (Tamanio: {os.path.getsize(pdf_leame_path):,} bytes)")

txt_leame_path = os.path.join(MASTER_DIR, "LEAME_PRIMERO_ENTREGA_CORTE_2.txt")
with open(txt_leame_path, "w", encoding="utf-8") as f:
    f.write("""================================================================================
UNIVERSIDAD SIMON BOLIVAR — FACULTAD DE INGENIERIAS — INGENIERIA DE SISTEMAS
ENTREGA OFICIAL SEGUNDO CORTE (70% DE DESARROLLO) — GESTION DE PROYECTOS (2026-2)
DOCENTE EVALUADORA: ING. NATALY DUQUE PAEZ
PROYECTO: ORBE360 (PEVCI) — CAMPUS VIRTUAL INCLUSIVO
================================================================================

INTEGRANTES DEL EQUIPO:
1. Eduardo Jose Soto Herrera (e_soto2@unisimon.edu.co) — Lider General & Arquitecto Frontend 360
2. Saraic Noemi Leon Hernandez (s_leon3@unisimon.edu.co) — Lider de Calidad & Especialista WCAG
3. Kevin Eduardo Garcia Moreno (k_garcia8@unisimon.edu.co) — Lider Backend & Gestion Jira
4. Sebastian David Omana Villamizar (s_omana1@unisimon.edu.co) — Ingeniero DevSecOps & Convex
5. Jesus Omar Avendano Avendano (j_avendano4@unisimon.edu.co) — Ingeniero Planificacion & PERT

--------------------------------------------------------------------------------
1. MATRIZ DE CONFORMIDAD FRENTE A LOS REQUERIMIENTOS DEL PARCIAL
--------------------------------------------------------------------------------
Item Exigido: Link para subir al Drive el software
Ubicacion:    Carpeta 01_Software_Desarrollado_70_Porciento/
Archivos:     ORBE-GP/ (Descomprimido) y ORBE-GP-Software-70.zip

Item Exigido: Gantt Project
Ubicacion:    Carpeta 02_Documentacion_y_Entregables_IEEE_1058/2_Planificacion_Gantt_y_WBS/
Archivos:     GANTT_ORBE360_CORTE_2.gan y GANTT_ORBE360_CORTE_2.png (123 tareas, recursos nivelados)

Item Exigido: Excel donde estan los Puntos de Funcion y el PERT
Ubicacion:    Carpeta 02_Documentacion_y_Entregables_IEEE_1058/3_Estimacion_Metrica_Excel_Puntos_de_Funcion_y_PERT/
Archivos:     Gestion de proyectos 222 nuevo.xlsx (Hojas: Iteracion 1, 2, 3, COCOMO II, PERT y Ruta Critica)

Item Exigido: Acta Constitucion Charter indicando el 70% y el 30%
Ubicacion:    Carpeta 02_Documentacion_y_Entregables_IEEE_1058/1_Acta_Constitucion_Project_Charter_70_30/
Archivos:     acta_constitucion_proyecto_charter_CORTE2.docx y .pdf (Tabla 9 con delimitacion 70% vs 30%)

Item Exigido: Proyecto Desarrollado 70%
Ubicacion:    Carpeta 01_Software_Desarrollado_70_Porciento/ORBE-GP/
Archivos:     62 escenas 360, 43 hotspots, audios neuronales Salome, subtitulos WebVTT e INICIAR_PROYECTO.bat

Item Exigido: Documento Word del prompt y cual IA se uso
Ubicacion:    Carpeta 02_Documentacion_y_Entregables_IEEE_1058/5_Procesos_Tecnicos_y_Prompts_IA/
Archivos:     DOCUMENTO_OFICIAL_PROMPTS_AGENTES_IA.docx y .pdf

Item Exigido: Presentacion de la Sustentacion
Ubicacion:    Carpeta 02_Documentacion_y_Entregables_IEEE_1058/6_Presentacion_Sustentacion/
Archivos:     Sustentacion_Orbe360_Segundo_Corte.pptx y .pdf (13 diapositivas ejecutivas)

Item Exigido: Link de Jira en un Doc Word
Ubicacion:    Carpeta 02_Documentacion_y_Entregables_IEEE_1058/4_Gestion_Agil_Jira_Cloud/
Archivos:     DOCUMENTO_ENLACE_JIRA_ORBE360.docx y .pdf

Item Exigido: Procesos Tecnicos segun norma IEEE 1058
Ubicacion:    02_Documentacion_y_Entregables_IEEE_1058/
Detalle:      Estructura de 6 modulos normalizados bajo IEEE Std 1058.

--------------------------------------------------------------------------------
2. ENLACES OFICIALES EN LINEA
--------------------------------------------------------------------------------
• Repositorio Oficial GitHub:
  https://github.com/KUTEIMO/ORBE-GP

• Tablero Jira Software Cloud:
  https://orbe-experience360.atlassian.net/jira/software/projects/KAN/boards

• Resumen Ejecutivo Jira:
  https://orbe-experience360.atlassian.net/jira/software/projects/KAN/summary

• Carpeta Oficial OneDrive / SharePoint Docente:
  https://unisimonedu-my.sharepoint.com/:f:/g/personal/nataly_duquep_unisimon_edu_co/IgCDRbT32DI0RYKHcylj9cxVAbtjusyMMuwxKrXtXb7X8D4?e=YKLsou

--------------------------------------------------------------------------------
3. INSTRUCCIONES DE EJECUCION DEL SOFTWARE (70%)
--------------------------------------------------------------------------------
Opcion 1: Doble clic en '01_Software_Desarrollado_70_Porciento/ORBE-GP/INICIAR_PROYECTO.bat'.
Opcion 2: En la terminal dentro de 'ORBE-GP', ejecutar 'npm start' y abrir http://localhost:8081/.
Opcion 3: En PowerShell ejecutar el comando de despliegue desde GitHub:
  cd $HOME; if (-not (Test-Path "ORBE-GP")) { git clone https://github.com/KUTEIMO/ORBE-GP.git }; cd ORBE-GP; Start-Process "http://localhost:8081/"; node scripts/dev-server.mjs
""")

print("LEAME_PRIMERO.txt generado.")
print("Construccion de paquete maestro finalizada con exito.")
