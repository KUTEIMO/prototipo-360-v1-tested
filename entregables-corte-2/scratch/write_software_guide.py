text = """================================================================================
ORBE360 — SOFTWARE DESARROLLADO 70% (SEGUNDO CORTE PARCIAL)
UNIVERSIDAD SIMON BOLIVAR — GESTION DE PROYECTOS (2026-2)
DOCENTE EVALUADORA: ING. NATALY DUQUE PAEZ
================================================================================

CONTENIDO DE ESTA CARPETA:
1. ORBE-GP/ (Carpeta Descomprimida):
   Contiene el codigo fuente completo del software funcional al 70%, incluyendo
   las 62 escenas 360, 43 hotspots interactivos, audios descriptivos con voz
   neuronal colombiana (es-CO-SalomeNeural), subtitulos sincronizados WebVTT
   y el archivo ejecutable 'INICIAR_PROYECTO.bat'.

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
INSTRUCCIONES DE EJECUCION LOCAL:
--------------------------------------------------------------------------------
Opcion 1 (Doble Clic):
  Abra la carpeta 'ORBE-GP' y haga doble clic en el archivo 'INICIAR_PROYECTO.bat'.
  El script verificara Node.js, abrira el navegador en http://localhost:8081/
  e iniciara el servidor local de manera automatica.

Opcion 2 (Terminal / NPM):
  Abra una terminal dentro de la carpeta 'ORBE-GP' y ejecute:
    npm start
  Luego acceda desde su navegador web a:
    http://localhost:8081/

Opcion 3 (Desde GitHub por PowerShell en una sola linea):
  cd $HOME; if (-not (Test-Path "ORBE-GP")) { git clone https://github.com/KUTEIMO/ORBE-GP.git }; cd ORBE-GP; Start-Process "http://localhost:8081/"; node scripts/dev-server.mjs
"""

path = r"c:\Users\SOTO\APLICATIVOS\proyectos unisimon\ORBE360_ENTREGA_SEGUNDO_CORTE_70\01_Software_Desarrollado_70_Porciento\GUIA_Y_ENLACES_DEL_SOFTWARE.txt"
with open(path, "w", encoding="utf-8") as f:
    f.write(text)

print("GUIA_Y_ENLACES_DEL_SOFTWARE.txt generado exitosamente.")
