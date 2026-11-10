import os
import shutil
import subprocess
import zipfile
import docx
import win32com.client

GP_DIR = r"c:\Users\SOTO\APLICATIVOS\proyectos unisimon\ORBE-GP"
ORBE_DIR = r"c:\Users\SOTO\APLICATIVOS\proyectos unisimon\ORBE"
ENTREGA_DIR = r"c:\Users\SOTO\APLICATIVOS\proyectos unisimon\ORBE360_ENTREGA_SEGUNDO_CORTE_70"

print("1. Limpiando archivos temporales en ORBE-GP...")
temp_png = os.path.join(GP_DIR, "plataforma", "assets", "sedes", "unisimon_biblioteca_mural_1791299957209 _.png")
if os.path.exists(temp_png):
    os.remove(temp_png)
    print("Eliminado archivo temporal con guion bajo.")

# 2. Actualizar README.md en ORBE-GP
print("2. Actualizando README.md con la Opcion C (actualizar instalacion existente)...")
readme_gp_path = os.path.join(GP_DIR, "README.md")
with open(readme_gp_path, "r", encoding="utf-8") as f:
    readme_content = f.read()

opcion_c_text = """### Opción C: Actualizar cambios en equipo ya descargado (sincronizar y ejecutar)
Si ya tiene el proyecto descargado en el computador y desea actualizarlo con los últimos cambios publicados (sin tener que volver a descomprimir ni reconfigurar nada), copie y pegue en Windows PowerShell y presione Enter:

```powershell
cd $HOME\\ORBE-GP; if (Test-Path .git) { git pull } else { Invoke-WebRequest -Uri "https://github.com/KUTEIMO/ORBE-GP/archive/refs/heads/main.zip" -OutFile "$HOME\\update.zip"; Expand-Archive -Path "$HOME\\update.zip" -DestinationPath "$HOME\\temp_update" -Force; Copy-Item -Path "$HOME\\temp_update\\ORBE-GP-main\\*" -Destination "$HOME\\ORBE-GP" -Recurse -Force; Remove-Item "$HOME\\update.zip", "$HOME\\temp_update" -Recurse -Force }; Start-Process "http://localhost:8081/"; node scripts/dev-server.mjs
```

---
"""

if "Opción C:" not in readme_content:
    target_pos = "### Opción B: Si ya está descargado (iniciar directamente)"
    if target_pos in readme_content:
        # Encontrar el final del bloque de codigo de Opcion B
        idx_b = readme_content.find(target_pos)
        idx_code_end = readme_content.find("```", idx_b + len(target_pos))
        idx_code_close = readme_content.find("```", idx_code_end + 3) + 3
        # Insertar Opcion C justo despues de Opcion B
        readme_content = (
            readme_content[:idx_code_close] + "\n\n" + opcion_c_text + "\n" + readme_content[idx_code_close:]
        )
        with open(readme_gp_path, "w", encoding="utf-8") as f:
            f.write(readme_content)
        print("README.md de ORBE-GP actualizado con Opcion C.")
    else:
        print("No se encontro encabezado Opcion B exactamente.")
else:
    print("Opcion C ya presente en README.md de ORBE-GP.")

# 3. Sincronizar a ORBE (repositorio principal)
print("3. Sincronizando archivos a ORBE...")
shutil.copy2(
    os.path.join(GP_DIR, "plataforma", "index.html"),
    os.path.join(ORBE_DIR, "plataforma", "index.html")
)
shutil.copy2(
    readme_gp_path,
    os.path.join(ORBE_DIR, "README.md")
)

sedes_gp = os.path.join(GP_DIR, "plataforma", "assets", "sedes")
sedes_orbe = os.path.join(ORBE_DIR, "plataforma", "assets", "sedes")
for f in os.listdir(sedes_gp):
    src = os.path.join(sedes_gp, f)
    dst = os.path.join(sedes_orbe, f)
    if os.path.isfile(src):
        shutil.copy2(src, dst)
print("Archivos sincronizados a ORBE.")

# 4. Sincronizar a ORBE360_ENTREGA_SEGUNDO_CORTE_70
print("4. Sincronizando a carpeta maestra de entrega...")
dest_entrega_gp = os.path.join(ENTREGA_DIR, "01_Software_Desarrollado_70_Porciento", "ORBE-GP")
shutil.copy2(
    os.path.join(GP_DIR, "plataforma", "index.html"),
    os.path.join(dest_entrega_gp, "plataforma", "index.html")
)
shutil.copy2(
    readme_gp_path,
    os.path.join(dest_entrega_gp, "README.md")
)

sedes_entrega = os.path.join(dest_entrega_gp, "plataforma", "assets", "sedes")
for f in os.listdir(sedes_gp):
    src = os.path.join(sedes_gp, f)
    dst = os.path.join(sedes_entrega, f)
    if os.path.isfile(src):
        shutil.copy2(src, dst)

# Actualizar GUIA_Y_ENLACES_DEL_SOFTWARE.txt en entrega
guia_txt_path = os.path.join(ENTREGA_DIR, "01_Software_Desarrollado_70_Porciento", "GUIA_Y_ENLACES_DEL_SOFTWARE.txt")
guia_content = f"""================================================================================
ORBE360 — SOFTWARE DESARROLLADO 70% (SEGUNDO CORTE PARCIAL)
UNIVERSIDAD SIMON BOLIVAR — GESTION DE PROYECTOS (2026-2)
DOCENTE EVALUADORA: ING. NATALY DUQUE PAEZ
================================================================================

CONTENIDO DE ESTA CARPETA:
1. ORBE-GP/ (Carpeta Descomprimida):
   Contiene el codigo fuente completo del software funcional al 70%, incluyendo
   las 62 escenas 360, 43 hotspots interactivos, audios descriptivos con voz
   neuronal colombiana (es-CO-SalomeNeural), subtitulos sincronizados WebVTT,
   nuevas fotografias institucionales de sedes y el archivo 'INICIAR_PROYECTO.bat'.

2. ORBE-GP-Software-70.zip (Archivo Comprimido):
   Paquete ZIP con la totalidad del software desarrollado por si se prefiere
   descargar en un unico archivo directamente desde OneDrive.

--------------------------------------------------------------------------------
ENLACES OFICIALES DEL PROYECTO:
--------------------------------------------------------------------------------
• Repositorio Oficial en GitHub:
  https://github.com/KUTEIMO/ORBE-GP

• Tablero Kanban / Scrum en Jira Software Cloud:
  https://orbe-experience360.atlassian.net/jira/software/projects/KAN/boards

• Resumen Ejecutivo del Proyecto en Jira Cloud:
  https://orbe-experience360.atlassian.net/jira/software/projects/KAN/summary

• Carpeta Oficial de Entrega en OneDrive / SharePoint:
  https://unisimonedu-my.sharepoint.com/:f:/g/personal/nataly_duquep_unisimon_edu_co/IgCDRbT32DI0RYKHcylj9cxVAbtjusyMMuwxKrXtXb7X8D4?e=YKLsou

--------------------------------------------------------------------------------
INSTRUCCIONES DE EJECUCION Y ACTUALIZACION:
--------------------------------------------------------------------------------
Opcion 1 (Doble Clic Local):
  Abra la carpeta 'ORBE-GP' y haga doble clic en el archivo 'INICIAR_PROYECTO.bat'.
  El script verificara Node.js, abrira el navegador en http://localhost:8081/
  e iniciara el servidor local de manera automatica.

Opcion 2 (Terminal / NPM):
  Abra una terminal dentro de la carpeta 'ORBE-GP' y ejecute:
    npm start
  Luego acceda desde su navegador web a:
    http://localhost:8081/

Opcion 3 (Primera vez desde GitHub por PowerShell en una sola linea):
  cd $HOME; if (-not (Test-Path "ORBE-GP")) {{ git clone https://github.com/KUTEIMO/ORBE-GP.git }}; cd ORBE-GP; Start-Process "http://localhost:8081/"; node scripts/dev-server.mjs

Opcion 4 (Actualizar cambios en equipo donde ya se descargo previamente):
  cd $HOME\\ORBE-GP; if (Test-Path .git) {{ git pull }} else {{ Invoke-WebRequest -Uri "https://github.com/KUTEIMO/ORBE-GP/archive/refs/heads/main.zip" -OutFile "$HOME\\update.zip"; Expand-Archive -Path "$HOME\\update.zip" -DestinationPath "$HOME\\temp_update" -Force; Copy-Item -Path "$HOME\\temp_update\\ORBE-GP-main\\*" -Destination "$HOME\\ORBE-GP" -Recurse -Force; Remove-Item "$HOME\\update.zip", "$HOME\\temp_update" -Recurse -Force }}; Start-Process "http://localhost:8081/"; node scripts/dev-server.mjs
"""
with open(guia_txt_path, "w", encoding="utf-8") as f:
    f.write(guia_content)
print("GUIA_Y_ENLACES_DEL_SOFTWARE.txt actualizado.")

# Regenerar ZIP en carpeta de entrega
zip_dest = os.path.join(ENTREGA_DIR, "01_Software_Desarrollado_70_Porciento", "ORBE-GP-Software-70.zip")
print("Regenerando ZIP de ORBE-GP en entrega...")
with zipfile.ZipFile(zip_dest, "w", zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(dest_entrega_gp):
        dirs[:] = [d for d in dirs if d not in [".git", "temp", "tmp"]]
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, os.path.join(ENTREGA_DIR, "01_Software_Desarrollado_70_Porciento"))
            zipf.write(file_path, arcname)
print(f"ZIP regenerado: {zip_dest} (Tamanio: {os.path.getsize(zip_dest):,} bytes)")

# 5. Git Commit y Push en ORBE-GP
print("5. Realizando Git commit y push en ORBE-GP...")
subprocess.run(["git", "add", "."], cwd=GP_DIR, check=True)
commit_msg = "[KAN-18] feat: Actualizar fotografias de sedes, Laboratorios de Salud y comando de actualizacion rapida"
try:
    subprocess.run(["git", "commit", "-m", commit_msg], cwd=GP_DIR, check=True)
    print("Commit realizado con exito.")
except subprocess.CalledProcessError:
    print("Sin cambios pendientes para commit.")

push_res = subprocess.run(["git", "push", "origin", "main"], cwd=GP_DIR, capture_output=True, text=True)
print("Git push output:", push_res.stdout, push_res.stderr)

print("Proceso de sincronizacion completado exitosamente.")
