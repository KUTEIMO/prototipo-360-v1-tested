# INFORME TÉCNICO DE GESTIÓN ÁGIL EN ATLASSIAN JIRA SOFTWARE Y TRAZABILIDAD CON GITHUB
### PROYECTO: ORBE360 (PEVCI) — SEGUNDO CORTE (70% ALCANCE)

**Institución:** Universidad Simón Bolívar (Sede Cúcuta)  
**Facultad:** Ingenierías — Programa de Ingeniería de Sistemas  
**Asignatura:** Gestión de Proyectos (Semestre 2026-2)  
**Docente Evaluadora:** Ing. Nataly Duque Páez  
**Fecha de Entrega:** Octubre de 2026  

---

## 📌 ENLACES DIRECTOS OFICIALES DE ACCESO

* **1. Tablero Kanban / Scrum en Jira Software Cloud (Tablero de Requerimientos):**  
  [https://orbe-experience360.atlassian.net/jira/software/projects/KAN/boards](https://orbe-experience360.atlassian.net/jira/software/projects/KAN/boards)
* **2. Resumen Ejecutivo de Proyecto en Jira:**  
  [https://orbe-experience360.atlassian.net/jira/software/projects/KAN/summary](https://orbe-experience360.atlassian.net/jira/software/projects/KAN/summary)
* **3. Repositorio Oficial en GitHub (Historial Sincronizado con Gantt):**  
  [https://github.com/KUTEIMO/ORBE-GP](https://github.com/KUTEIMO/ORBE-GP)

> **Nota de Acceso y Seguridad:** El espacio en Jira está alojado en la organización oficial Atlassian Cloud con permisos de visualización para la evaluación docente. El repositorio en GitHub cuenta con 20 commits fechados según el cronograma (Agosto a Octubre 2026). Por directrices de seguridad de software, el repositorio público no almacena contraseñas; las credenciales administrativas de prueba se entregan de forma confidencial a la docente evaluadora.

---

## 1. MÉTRICAS DEL TABLERO Y AVANCE DEL 70% EN EL SEGUNDO CORTE

El tablero de Jira Software cuenta con la totalidad de los 54 requerimientos formales (RF-01 a RF-42 y RNF-04 a RNF-19) inventariados en el Excel de estimación por Puntos de Función (IFPUG). El cumplimiento del 70% del alcance se distribuye en las columnas del tablero de la siguiente forma:

| Columna / Estado en Jira | Cantidad de Tickets | Porcentaje Respecto al Total | Descripción del Alcance Cubierto |
| :--- | :---: | :---: | :--- |
| **Finalizada (Done)** | 26 Requerimientos | 48.1% | Módulos Core 360°, Audio Espacial 3D, Grafo Convex |
| **En Revisión / QA (In Review)** | 12 Requerimientos | 22.2% | Accesibilidad WCAG 2.1 AA, Widget LSC, Foco Teclado |
| **En Curso (In Progress)** | 8 Requerimientos | 14.8% | CMS, Control de Contenido Web, Sincronización Local |
| **Tareas por Hacer (To Do - Corte 3)** | 8 Requerimientos | 14.9% | Pruebas 100% ISO 29119 y Pisos Superiores (Torre 2) |
| **TOTAL GENERAL** | **54 Requerimientos** | **100.0%** | **70.3% Funcional Ejecutado en Corte 2** |

---

## 2. INTEGRACIÓN Y TRAZABILIDAD BIDIRECCIONAL GITHUB <-> JIRA CLOUD

Para asegurar una trazabilidad técnica de nivel profesional entre la gestión ágil y el código fuente, se implementó el estándar de **Smart Commits** de Atlassian integrando Jira Software con el repositorio GitHub:

1. **Nomenclatura de Commits (Smart Commits):** Cada confirmación en Git incluye el identificador de la incidencia entre corchetes (ej: `[KAN-18]`, `[KAN-19]`, `[KAN-20]`, `[KAN-25]`, `[KAN-54]`). Esto permite a Atlassian asociar automáticamente confirmaciones y revisiones de código a cada requerimiento.
2. **Comentarios Automatizados via API Atlassian MCP:** Las incidencias clave en Jira cuentan con comentarios registrados automáticamente que enlazan al commit exacto, autor institucional (`@unisimon.edu.co`), rama `main` y resultado de verificación.
3. **Cronograma Histórico Real en GitHub:** Los 20 commits en GitHub reflejan con exactitud las fechas del cronograma en GanttProject (Agosto a Octubre 2026), demostrando el avance distribuido entre los 5 integrantes del equipo.
4. **Blindaje de Seguridad en Repositorio Público:** Atendiendo buenas prácticas de ciberseguridad, ninguna clave sensible reside en el repositorio público.

### Matriz de Trazabilidad Jira Issue <-> GitHub Commit

| Ticket Jira | Módulo Técnico | Commit en GitHub | Autor Responsable (@unisimon.edu.co) |
| :--- | :--- | :--- | :--- |
| **KAN-1** | Autenticación y Esquema Convex | `00c718c` [KAN-1] feat: Esquema RBAC | Kevin García (`k_garcia8@unisimon.edu.co`) |
| **KAN-18** | Visor 360° y Texturas Biblioteca | `c48b2c0` [KAN-18] feat: Texturas Anita Consuegra | Eduardo Soto (`e_soto2@unisimon.edu.co`) |
| **KAN-19** | Audio Espacial Descriptivo 3D | `64de794` [KAN-19] feat: Subsistema Web Audio | Saraic León (`s_leon3@unisimon.edu.co`) |
| **KAN-20** | Lengua de Señas Colombiana (LSC) | `855cf05` [KAN-20] feat: Widget PIP adaptable | Saraic León (`s_leon3@unisimon.edu.co`) |
| **KAN-25** | Navegación Teclado WCAG 2.1 AA | `4a40139` [KAN-25] feat: Anillo de foco accesible | Saraic León (`s_leon3@unisimon.edu.co`) |
| **KAN-54** | Control Acceso Admin de Sede | `69c1d28` [KAN-54] feat: Validación tokens sede | Kevin García (`k_garcia8@unisimon.edu.co`) |

---

## 3. EQUIPO DE INGENIERÍA Y ASIGNACIONES OFICIALES

| Integrante | Rol en Jira | Módulo de Requerimientos a Cargo |
| :--- | :--- | :--- |
| **Eduardo José Soto Herrera** | Líder Frontend 360° | Motor 360°, WebGL, Gráficos y Ruteo Virtual (KAN-18) |
| **Saraic Noemi León Hernández** | Líder QA & Accesibilidad | Audio 3D, LSC, Teclado y WCAG 2.1 AA (KAN-19, KAN-20, KAN-25) |
| **Kevin Eduardo García Moreno** | Líder Backend & Jira | Autenticación RBAC, Sesiones y Jira MCP (KAN-1, KAN-2, KAN-54) |
| **Sebastián David Omaña Villamizar** | DevSecOps & Base de Datos | Base de Datos Convex, Drift Check y Playwright E2E |
| **Jesús Omar Avendaño Avendaño** | Planificación & Riesgos | WBS, Cronograma GanttProject, PERT y Estimación IFPUG |

---
*Universidad Simón Bolívar — San José de Cúcuta, Colombia — Octubre 2026*
