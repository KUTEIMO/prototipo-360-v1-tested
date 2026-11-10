import os
import shutil

DIR_DEF = r"c:\Users\SOTO\APLICATIVOS\proyectos unisimon\ORBE360_ENTREGA_SEGUNDO_CORTE_70"
DIR_EDIT = r"c:\Users\SOTO\APLICATIVOS\proyectos unisimon\ORBE360_ENTREGA_SEGUNDO_CORTE_EDICION"

print("1. Creando o actualizando carpeta de EDICION...")
if os.path.exists(DIR_EDIT):
    shutil.rmtree(DIR_EDIT)

# Copiar todo a la carpeta de EDICION para conservar palabras, markdown y fuentes originales
shutil.copytree(DIR_DEF, DIR_EDIT)
print(f"Carpeta de EDICION creada con exito en: {DIR_EDIT}")

# Tambien copiar los guiones individuales y guion mapa a la carpeta de EDICION
guiones_src = r"c:\Users\SOTO\APLICATIVOS\proyectos unisimon\ORBE\entregables-corte-2"
guiones_dst = os.path.join(DIR_EDIT, "02_Documentacion_y_Entregables_IEEE_1058", "6_Presentacion_Sustentacion", "GUIONES_Y_DEFENSA")
os.makedirs(guiones_dst, exist_ok=True)

for f in os.listdir(guiones_src):
    if f.startswith("GUION_") or f.startswith("GUIA_"):
        shutil.copyfile(os.path.join(guiones_src, f), os.path.join(guiones_dst, f))
        print(f"Copiado a EDICION/GUIONES: {f}")

print("\n2. Limpiando carpeta DEFINITIVA PARA DRIVE (dejando solo PDFs, XLSX, GAN, ZIP, TXT y assets)...")
removed_count = 0
for root, dirs, files in os.walk(DIR_DEF):
    # No tocar el codigo fuente dentro de ORBE-GP
    if "01_Software_Desarrollado_70_Porciento" in root and "ORBE-GP" in root:
        continue
    for f in files:
        ext = os.path.splitext(f)[1].lower()
        if ext in [".md", ".docx", ".pptx"]:
            file_to_remove = os.path.join(root, f)
            os.remove(file_to_remove)
            print(f"Eliminado de definitiva: {os.path.relpath(file_to_remove, DIR_DEF)}")
            removed_count += 1

# Eliminar carpeta vacia GUIONES_INDIVIDUALES si existiera en definitiva
empty_dir = os.path.join(DIR_DEF, "02_Documentacion_y_Entregables_IEEE_1058", "6_Presentacion_Sustentacion", "GUIONES_INDIVIDUALES")
if os.path.exists(empty_dir) and not os.listdir(empty_dir):
    os.rmdir(empty_dir)

print(f"\nProceso finalizado: {removed_count} archivos editables (.md, .docx, .pptx) eliminados de la carpeta definitiva.")
