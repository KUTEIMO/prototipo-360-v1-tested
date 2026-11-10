# PAQUETE MAESTRO DE ENTREGABLES — SEGUNDO CORTE (2026-2)
## ESTRUCTURACIÓN DE PROCESOS TÉCNICOS BAJO LA NORMA IEEE 1058
### PROYECTO: ORBE360 (PEVCI) — CAMPUS INCLUSIVO UNIVERSIDAD SIMÓN BOLÍVAR

**Docente Evaluadora:** Ing. Nataly Duque Páez  
**Asignatura:** Gestión de Proyectos — Facultad de Ingenierías  
**Fecha de Congelamiento Oficial:** Lunes 12 de Octubre de 2026 (18:30:00 -0500)  

---

### Integrantes del Equipo de Proyecto:
1. **EDUARDO JOSÉ SOTO HERRERA** — `e_soto2@unisimon.edu.co` — Líder General de Proyecto & Arquitecto Frontend 360°
2. **SARAIC NOEMI LEÓN HERNÁNDEZ** — `s_leon3@unisimon.edu.co` — Líder de Calidad & Especialista en Accesibilidad WCAG
3. **KEVIN EDUARDO GARCÍA MORENO** — `k_garcia8@unisimon.edu.co` — Líder Backend & Gestión de Requerimientos Jira
4. **SEBASTIÁN DAVID OMAÑA VILLAMIZAR** — `s_omana1@unisimon.edu.co` — Ingeniero DevSecOps & Infraestructura
5. **JESÚS OMAR AVENDAÑO AVENDAÑO** — `j_avendano4@unisimon.edu.co` — Ingeniero de Planificación, Cronograma & Riesgos

---

## 1. MATRIZ DE CONFORMIDAD FRENTE A LOS REQUERIMIENTOS DE LA DOCENTE

| Requerimiento Exigido por la Docente | Ubicación Oficial en este Paquete (IEEE 1058) | Archivo Específico |
| :--- | :--- | :--- |
| **1. Link para subir al Drive el software** | Carpeta `6_Proyecto_Software_70_Porciento/` | [`ENLACES_OFICIALES_GITHUB_Y_DRIVE.md`](./6_Proyecto_Software_70_Porciento/ENLACES_OFICIALES_GITHUB_Y_DRIVE.md) |
| **2. Gantt Project (con antecesores y recursos)** | Carpeta `5_Metricas_WBS_Gantt_y_PERT/` | [`GANTT_ORBE360_CORTE_2.gan`](./5_Metricas_WBS_Gantt_y_PERT/GANTT_ORBE360_CORTE_2.gan) |
| **3. Excel con Puntos de Función y PERT** | Carpeta `5_Metricas_WBS_Gantt_y_PERT/` | [`Gestion de proyectos 222 nuevo.xlsx`](./5_Metricas_WBS_Gantt_y_PERT/Gestion%20de%20proyectos%20222%20nuevo.xlsx) |
| **4. Acta Constitución Charter (70% vs 30%)** | Carpeta `1_Inicio_y_Project_Charter/` | [`acta_constitucion_proyecto_charter_CORTE2.docx`](./1_Inicio_y_Project_Charter/acta_constitucion_proyecto_charter_CORTE2.docx) |
| **5. Proyecto Desarrollado 70% (Funcional)** | Carpeta `6_Proyecto_Software_70_Porciento/` y repo externo `ORBE-GP` | [`ORBE-GP-Software-70.zip`](./6_Proyecto_Software_70_Porciento/ORBE-GP-Software-70.zip) |
| **6. Documento Word del Prompt e IA usada** | Carpeta `4_Procesos_Tecnicos_y_Prompts_IA/` | [`DOCUMENTO_OFICIAL_PROMPTS_AGENTES_IA.docx`](./4_Procesos_Tecnicos_y_Prompts_IA/DOCUMENTO_OFICIAL_PROMPTS_AGENTES_IA.docx) |
| **7. Presentación de la Sustentación** | Carpeta `2_Organizacion_del_Equipo_y_Sustentacion/` | [`GUION_MAESTRO_SUSTENTACION.md`](./2_Organizacion_del_Equipo_y_Sustentacion/GUION_MAESTRO_SUSTENTACION.md) y Guiones Individuales |
| **8. Link de Jira en un Documento Word** | Carpeta `3_Gestion_Agil_Jira_Cloud/` | [`DOCUMENTO_ENLACE_JIRA_ORBE360.docx`](./3_Gestion_Agil_Jira_Cloud/DOCUMENTO_ENLACE_JIRA_ORBE360.docx) |
| **9. Estructuración según Norma IEEE 1058** | Raíz de Entregables Definitivos | 6 Módulos / Carpetas normalizadas |

---

## 2. ESTRUCTURA DE DIRECTORIOS SEGÚN LA NORMA IEEE 1058

La organización de las carpetas atiende el formato institucional oficial:

### `1_Inicio_y_Project_Charter/` (Sección 1 IEEE 1058)
* **`acta_constitucion_proyecto_charter_CORTE2.docx`**: Project Charter formal con presupuesto consolidado de $63.000.000 COP, 400.84 PFA, 59.40 Persona-Mes y la **delineación explícita del 70% entregado en Corte 2 vs. 30% reservado para Corte 3**.
* **`PROJECT_CHARTER.md`**: Versión Markdown de consulta rápida.

### `2_Organizacion_del_Equipo_y_Sustentacion/` (Sección 2 IEEE 1058)
* **`GUION_MAESTRO_SUSTENTACION.md`**: Protocolo completo de exposición de 12 a 15 minutos en laptop con flujo de 3 ventanas (GanttProject -> Jira -> Software 360° en vivo).
* **Carpeta `GUIONES_INDIVIDUALES/`**: Guiones directos e individuales para cada integrante:
  - `GUION_INDIVIDUAL_EDUARDO_SOTO.md` (Apertura, Stack Frontend y Cierre).
  - `GUION_INDIVIDUAL_JESUS_AVENDANO.md` (Cronograma, Antecesores, Nivelación y PERT).
  - `GUION_INDIVIDUAL_KEVIN_GARCIA.md` (Tablero Jira, Historias de Usuario, Gherkin y MCP).
  - `GUION_INDIVIDUAL_SEBASTIAN_OMANA.md` (Base de Datos Convex, DevSecOps y Playwright).
  - `GUION_INDIVIDUAL_SARAIC_LEON.md` (Accesibilidad WCAG 2.1 AA, Audio Espacial y LSC).

### `3_Gestion_Agil_Jira_Cloud/` (Sección 3 IEEE 1058)
* **`DOCUMENTO_ENLACE_JIRA_ORBE360.docx`**: Documento Word oficial solicitado por la docente con los enlaces directos a Jira Cloud, métricas del tablero (54 tickets), demostración del 70% completado y detalle de historias de usuario con criterios Gherkin.
* **`DOCUMENTO_ENLACE_JIRA_ORBE360.md`**: Versión Markdown sincronizada.
* **`MATRIZ_TRAZABILIDAD_GANTT_JIRA_EXCEL.md`**: Matriz 1:1 que vincula cada requerimiento del Excel con su ID de Jira (`KAN-1..54`) y su tarea en el Gantt.
* **`JIRA_ESTADO_Y_MEJORAS.md`**: Auditoría del tablero en la nube.

### `4_Procesos_Tecnicos_y_Prompts_IA/` (Sección 4 IEEE 1058)
* **`DOCUMENTO_OFICIAL_PROMPTS_AGENTES_IA.docx`**: Dossier formal de ingeniería de prompts y metodología Human-in-the-Loop, con el System Prompt institucional (`AGENTS.md`), las 17 cadenas multi-turno de arquitectura y depuración de código, autoría por estudiante y firmas formales.
* **`DOCUMENTO_OFICIAL_PROMPTS_AGENTES_IA.md`**: Versión Markdown sincronizada.
* **`MANUAL_DE_DESPLIEGUE_Y_EJECUCION_PC_DOCENTE.md`**: Instrucciones sencillas de 3 pasos (`npm install`, `npm start`, abrir navegador) para que la profesora ejecute el software de forma autónoma en su computador.

### `5_Metricas_WBS_Gantt_y_PERT/` (Sección 5 IEEE 1058)
* **`GANTT_ORBE360_CORTE_2.gan`**: Archivo de GanttProject con 123 tareas en 7 fases, antecesores vinculados y **nivelación de recursos aplicada (0% sobreasignaciones / 0 barras rojas)**.
* **`Gestion de proyectos 222 nuevo.xlsx`**: Hoja de cálculo con Puntos de Función IFPUG (400.84 PFA), COCOMO II y la **nueva hoja técnica `PERT y Ruta Crítica`** con estimación probabilística de 3 puntos, varianzas y holguras.
* **`GANTT_ORBE360_CORTE_2.png`**: Exportación en alta resolución del cronograma en formato apaisado.
* **`REPORTE_RECURSOS_GANTT.html`**: Informe HTML de carga diaria por integrante (≤ 100%).
* **`DIAGRAMA_PERT_RED.html`**: Visualizador interactivo de la red PERT y ruta crítica.

### `6_Proyecto_Software_70_Porciento/` (Sección 6 IEEE 1058)
* **`ENLACES_OFICIALES_GITHUB_Y_DRIVE.md`**: Enlaces directos a la carpeta de OneDrive de la docente y al repositorio GitHub `ORBE-GP`.
* **`ORBE-GP-Software-70.zip`**: Paquete comprimido (274 MB) con el software 100% funcional y autónomo listo para subir a OneDrive.
* **Repositorio Local Autónomo (`c:\Users\SOTO\APLICATIVOS\proyectos unisimon\ORBE-GP`)**: Repositorio Git limpio, sin archivos temporales ni notas internas, congelado con fecha previa al inicio de los exámenes parciales (`2026-10-12 18:30:00 -0500`).

---
**Universidad Simón Bolívar — Sede Cúcuta — Octubre de 2026**
