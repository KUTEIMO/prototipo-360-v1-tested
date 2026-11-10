import os
import docx
from docx.shared import RGBColor, Pt
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn
import win32com.client

# Target directories
BASE_EDIT = r"c:\Users\SOTO\APLICATIVOS\proyectos unisimon\ORBE360_ENTREGA_SEGUNDO_CORTE_EDICION"
BASE_DEF = r"c:\Users\SOTO\APLICATIVOS\proyectos unisimon\ORBE360_ENTREGA_SEGUNDO_CORTE_70"

docs_to_normalize = [
    os.path.join(BASE_EDIT, "LEAME_PRIMERO_ENTREGA_CORTE_2.docx"),
    os.path.join(BASE_EDIT, "02_Documentacion_y_Entregables_IEEE_1058", "1_Acta_Constitucion_Project_Charter_70_30", "acta_constitucion_proyecto_charter_CORTE2.docx"),
    os.path.join(BASE_EDIT, "02_Documentacion_y_Entregables_IEEE_1058", "4_Gestion_Agil_Jira_Cloud", "DOCUMENTO_ENLACE_JIRA_ORBE360.docx"),
    os.path.join(BASE_EDIT, "02_Documentacion_y_Entregables_IEEE_1058", "5_Procesos_Tecnicos_y_Prompts_IA", "DOCUMENTO_OFICIAL_PROMPTS_AGENTES_IA.docx"),
    os.path.join(BASE_EDIT, "02_Documentacion_y_Entregables_IEEE_1058", "6_Presentacion_Sustentacion", "ENLACE_PRESENTACION_CANVA_ORBE360.docx")
]

# IEEE Palette: Sober, Academic, Monochrome
COLOR_BLACK = RGBColor(0, 0, 0)
COLOR_DARK = RGBColor(34, 34, 34)       # #222222
COLOR_MUTED = RGBColor(85, 85, 85)     # #555555

def normalize_to_ieee_style(docx_path):
    print(f"\nProcesando estilo IEEE en: {os.path.basename(docx_path)}...")
    doc = docx.Document(docx_path)

    # 1. Normalizar párrafos fuera de tablas
    for p in doc.paragraphs:
        for r in p.runs:
            if r.font.color and r.font.color.rgb:
                hex_col = str(r.font.color.rgb).upper()
                # Si era cualquier color brillante (azul, celeste, verde, teal, rojo)
                if hex_col in ["0284C7", "0F2547", "003366", "004488", "002244", "1F4E79", "00A8A8", "B43232", "1E293B", "475569", "64748B"]:
                    # Si es texto en negrita o encabezado
                    if r.bold or (p.style and "heading" in p.style.name.lower()):
                        r.font.color.rgb = COLOR_BLACK
                    else:
                        r.font.color.rgb = COLOR_DARK
                elif hex_col in ["555555", "787878", "646464", "808080", "505050"]:
                    r.font.color.rgb = COLOR_MUTED

    # 2. Normalizar tablas (estilo IEEE: sin fondos de colores vivos, encabezados en gris neutro sutil o blanco)
    for table in doc.tables:
        for row_idx, row in enumerate(table.rows):
            is_header = (row_idx == 0)
            for cell in row.cells:
                tcPr = cell._tc.get_or_add_tcPr()
                
                # Revisar sombreado (w:shd)
                shd = tcPr.find(qn("w:shd"))
                fill_color = shd.get(qn("w:fill")) if shd is not None else None
                
                # Si el sombreado era de color oscuro/vivo (azul, teal, celeste)
                if is_header:
                    # Encabezados de tabla estilo IEEE: gris muy sutil #F2F2F2 o blanco con texto negro
                    if shd is not None:
                        shd.set(qn("w:fill"), "F2F2F2")
                    else:
                        new_shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="F2F2F2"/>')
                        tcPr.append(new_shd)
                else:
                    # Filas de datos: blanco o gris alternado muy sutil
                    if fill_color and fill_color.upper() in ["0284C7", "003366", "1F4E79", "00A8A8", "EFF6FF", "F0F9FF", "F2F7F7", "F4F6F9", "F1F5F9", "F4F7FB"]:
                        if shd is not None:
                            shd.set(qn("w:fill"), "FAFAFA" if row_idx % 2 == 1 else "FFFFFF")

                # Revisar texto dentro de la celda
                for p in cell.paragraphs:
                    for r in p.runs:
                        if r.font.color and r.font.color.rgb:
                            hex_col = str(r.font.color.rgb).upper()
                            # Si era blanco (#FFFFFF) pero ahora la celda es clara, cambiar a NEGRO
                            if hex_col == "FFFFFF" and is_header:
                                r.font.color.rgb = COLOR_BLACK
                                r.bold = True
                            elif hex_col in ["0284C7", "0F2547", "003366", "004488", "002244", "1F4E79", "00A8A8", "B43232", "1E293B", "475569", "64748B"]:
                                r.font.color.rgb = COLOR_BLACK if (r.bold or is_header) else COLOR_DARK
                        else:
                            if is_header:
                                r.font.color.rgb = COLOR_BLACK
                                r.bold = True

    doc.save(docx_path)
    print(f"Guardado docx normalizado: {docx_path}")

print("Iniciando normalizacion de documentos...")
for path in docs_to_normalize:
    if os.path.exists(path):
        normalize_to_ieee_style(path)
    else:
        print(f"No encontrado: {path}")

# 3. Exportar todos a PDF con Word COM
print("\nExportando versiones PDF actualizadas...")
word = win32com.client.Dispatch("Word.Application")
word.Visible = False

try:
    for path in docs_to_normalize:
        if not os.path.exists(path):
            continue
        pdf_path_edit = path.replace(".docx", ".pdf")
        rel_from_edit = os.path.relpath(path, BASE_EDIT)
        pdf_path_def = os.path.join(BASE_DEF, rel_from_edit).replace(".docx", ".pdf")

        print(f"Exportando a PDF: {os.path.basename(path)}...")
        doc = word.Documents.Open(path)
        doc.SaveAs(pdf_path_edit, FileFormat=17) # wdFormatPDF
        doc.Close()
        print(f"  -> PDF en EDICION: {pdf_path_edit}")

        # Copiar el PDF a la carpeta definitiva
        os.makedirs(os.path.dirname(pdf_path_def), exist_ok=True)
        import shutil
        shutil.copyfile(pdf_path_edit, pdf_path_def)
        print(f"  -> PDF en DEFINITIVA: {pdf_path_def}")

finally:
    word.Quit()
    print("\nTodos los PDFs se han regenerado bajo la norma sobria IEEE.")
