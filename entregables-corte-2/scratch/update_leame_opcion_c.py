import os
import docx
from docx.shared import Pt, Inches, RGBColor
import win32com.client

ENTREGA_DIR = r"c:\Users\SOTO\APLICATIVOS\proyectos unisimon\ORBE360_ENTREGA_SEGUNDO_CORTE_70"

# 1. Actualizar TXT
txt_path = os.path.join(ENTREGA_DIR, "LEAME_PRIMERO_ENTREGA_CORTE_2.txt")
with open(txt_path, "r", encoding="utf-8") as f:
    txt = f.read()

txt_cmd = """Opcion 4 (Actualizar instalacion ya descargada en el equipo):
  cd $HOME\\ORBE-GP; if (Test-Path .git) { git pull } else { Invoke-WebRequest -Uri "https://github.com/KUTEIMO/ORBE-GP/archive/refs/heads/main.zip" -OutFile "$HOME\\update.zip"; Expand-Archive -Path "$HOME\\update.zip" -DestinationPath "$HOME\\temp_update" -Force; Copy-Item -Path "$HOME\\temp_update\\ORBE-GP-main\\*" -Destination "$HOME\\ORBE-GP" -Recurse -Force; Remove-Item "$HOME\\update.zip", "$HOME\\temp_update" -Recurse -Force }; Start-Process "http://localhost:8081/"; node scripts/dev-server.mjs
"""

if "Opcion 4" not in txt:
    txt = txt.strip() + "\n" + txt_cmd
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(txt)
    print("LEAME_PRIMERO.txt actualizado con Opcion 4.")

# 2. Actualizar DOCX y regenerar PDF
docx_path = os.path.join(ENTREGA_DIR, "LEAME_PRIMERO_ENTREGA_CORTE_2.docx")
doc = docx.Document(docx_path)
p = doc.add_paragraph()
p.paragraph_format.space_before = Pt(4)
p.paragraph_format.space_after = Pt(4)
r = p.add_run("• Modalidad 4 (Actualizar cambios en computador ya descargado):\n"
              "  cd $HOME\\ORBE-GP; if (Test-Path .git) { git pull } else { Invoke-WebRequest -Uri \"https://github.com/KUTEIMO/ORBE-GP/archive/refs/heads/main.zip\" -OutFile \"$HOME\\update.zip\"; Expand-Archive -Path \"$HOME\\update.zip\" -DestinationPath \"$HOME\\temp_update\" -Force; Copy-Item -Path \"$HOME\\temp_update\\ORBE-GP-main\\*\" -Destination \"$HOME\\ORBE-GP\" -Recurse -Force; Remove-Item \"$HOME\\update.zip\", \"$HOME\\temp_update\" -Recurse -Force }; Start-Process \"http://localhost:8081/\"; node scripts/dev-server.mjs")
r.font.size = Pt(9.5)
r.font.name = "Consolas"
doc.save(docx_path)
print("LEAME_PRIMERO.docx guardado.")

word = win32com.client.Dispatch("Word.Application")
word.Visible = False
opened = word.Documents.Open(docx_path)
pdf_path = os.path.join(ENTREGA_DIR, "LEAME_PRIMERO_ENTREGA_CORTE_2.pdf")
opened.SaveAs(pdf_path, FileFormat=17)
opened.Close()
word.Quit()
print("LEAME_PRIMERO.pdf regenerado exitosamente.")
