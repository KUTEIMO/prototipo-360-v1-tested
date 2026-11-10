# UNIVERSIDAD SIMÓN BOLÍVAR — SEDE CÚCUTA
## FACULTAD DE INGENIERÍAS — PROGRAMA DE INGENIERÍA DE SISTEMAS
### ASIGNATURA: GESTIÓN DE PROYECTOS — SEMESTRE 2026-2

---

# INFORME DE ACCESO Y GESTIÓN ÁGIL EN ATLASSIAN JIRA SOFTWARE
## PROYECTO: ORBE360 (PEVCI) — SEGUNDO CORTE

**Docente Evaluadora:** Ing. Nataly Duque Páez  
**Fecha de Entrega:** Octubre de 2026  

---

### ENLACES DIRECTOS AL PROYECTO OFICIAL EN ATLASSIAN JIRA CLOUD:

1. **Tablero Kanban / Scrum Principal del Proyecto:**  
   `https://orbe-experience360.atlassian.net/jira/software/projects/KAN/boards`

2. **Resumen Ejecutivo y Métricas del Proyecto KAN:**  
   `https://orbe-experience360.atlassian.net/jira/software/projects/KAN/summary`

> **Nota de Acceso:** El espacio se encuentra alojado bajo la organización oficial en Atlassian Cloud. Para la evaluación por la docente, los permisos de visualización pública y lectura de incidencias se encuentran completamente habilitados.

---

### 1. MÉTRICAS DEL TABLERO Y AVANCE DEL 70% EN EL SEGUNDO CORTE

El tablero de Jira Software cuenta con la totalidad de los 54 requerimientos formales (RF-01 a RF-42 y RNF-04 a RNF-19) inventariados en el Excel de estimación por Puntos de Función. El cumplimiento del 70% del alcance se distribuye en las columnas del tablero de la siguiente forma:

| Columna / Estado en Jira | Cantidad de Tickets | Porcentaje | Módulos Comprendidos |
| :--- | :---: | :---: | :--- |
| **Finalizada (Done)** | 26 Requerimientos | 48.1% | Módulos Core 360°, Audio Descriptivo, Base de Datos Convex |
| **En Revisión / QA (In Review)** | 12 Requerimientos | 22.2% | Accesibilidad WCAG 2.1 AA, Video LSC, Navegación por Teclado |
| **En Curso (In Progress)** | 8 Requerimientos | 14.8% | CMS, Panel de Administración, Ruteo Virtual |
| **Tareas por Hacer (To Do - Corte 3)** | 8 Requerimientos | 14.9% | Pruebas 100% ISO 29119, Captura de Pisos Superiores |
| **TOTAL CONSOLIDADO** | **54 Requerimientos** | **100%** | **70.3% de Avance Funcional Efectivo (Segundo Corte)** |

---

### 2. ESTANDARIZACIÓN DE TICKETS: HISTORIAS DE USUARIO Y GHERKIN

Cada incidencia registrada bajo las claves `KAN-1` a `KAN-54` fue estandarizada bajo el estándar de la cátedra e integrada mediante el protocolo Atlassian MCP (`atlassian-mcp-server`). La estructura de cada requerimiento comprende:
* **Historia de Usuario Ágil:** "Como [rol de usuario] quiero [acción funcional] para [beneficio esperado]".
* **Criterios de Aceptación bajo sintaxis Gherkin** (`Dado que... Cuando... Entonces...`) que delimitan la Definición de Terminado (DoD).
* **Bloque de Trazabilidad Cruzada:** Código EDT/WBS, Código de Excel IFPUG y Complejidad Técnica asignada.
* **Asignación Oficial:** Asignado al estudiante responsable con su correo `@unisimon.edu.co`.

---

### 3. EQUIPO DE INGENIERÍA Y ASIGNACIONES EN JIRA SOFTWARE

| Integrante | Rol Oficial en Jira | Módulos de Requerimientos a Cargo |
| :--- | :--- | :--- |
| **Eduardo José Soto Herrera** | Líder Frontend 360° | Motor 360°, WebGL, Gráficos y Ruteo Virtual (`KAN-18`) |
| **Saraic Noemi León Hernández** | Líder QA & Accesibilidad | Audio 3D, LSC, Teclado y WCAG 2.1 AA (`KAN-19`, `KAN-20`, `KAN-25`) |
| **Kevin Eduardo García Moreno** | Líder Backend & Jira | Autenticación RBAC, Sesiones y Jira MCP (`KAN-1`, `KAN-2`, `KAN-54`) |
| **Sebastián David Omaña Villamizar** | DevSecOps & Base de Datos | Base de Datos Convex, Drift Check y Playwright E2E |
| **Jesús Omar Avendaño Avendaño** | Planificación & Riesgos | WBS, Cronograma GanttProject, PERT y Estimación IFPUG |

---
**Cúcuta, Norte de Santander — Octubre de 2026**
