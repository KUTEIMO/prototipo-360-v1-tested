# UNIVERSIDAD SIMÓN BOLÍVAR
## FACULTAD DE INGENIERÍAS — INGENIERÍA DE SISTEMAS
### GESTIÓN DE PROYECTOS (SEMESTRE 2026-2)

---

# INFORME TÉCNICO DE GESTIÓN ÁGIL EN ATLASSIAN JIRA SOFTWARE Y TRAZABILIDAD CON GITHUB
**Proyecto:** ORBE360 — Plataforma Web de Recorridos Virtuales 360° (PEVCI)  
**Docente Evaluadora:** Ing. Nataly Duque Páez  
**Entrega:** Tercer Corte (Avance 15% y Proyección al 30% Final)  
**Fecha:** Noviembre de 2026  

---

## 1. ENLACES DIRECTOS A LOS TABLEROS EN JIRA SOFTWARE CLOUD

El seguimiento del ciclo de vida ágil del software se gestiona formalmente en Atlassian Jira Cloud:

- **Tablero Kanban / Scrum Principal (Sprints 1 al 4):**  
  [https://orbe-experience360.atlassian.net/jira/software/projects/KAN/boards](https://orbe-experience360.atlassian.net/jira/software/projects/KAN/boards)

- **Resumen Ejecutivo del Proyecto (Project Summary):**  
  [https://orbe-experience360.atlassian.net/jira/software/projects/KAN/summary](https://orbe-experience360.atlassian.net/jira/software/projects/KAN/summary)

- **Repositorio Oficial Conectado (Smart Commits):**  
  [https://github.com/KUTEIMO/ORBE-GP](https://github.com/KUTEIMO/ORBE-GP)

---

## 2. ESTRUCTURA DE SPRINTS Y ALCANCE POR CORTE ACADÉMICO

| Sprint | Fechas | Alcance Asociado | Estado | Requerimientos Clave |
| :--- | :--- | :--- | :--- | :--- |
| **Sprint 1: Cimientos y 360** | 18/08/2026 - 15/09/2026 | Arquitectura Base (35%) | [COMPLETADO] | KAN-1 al KAN-22: Visor WebGL Marzipano, 62 escenas, hot spots iniciales. |
| **Sprint 2: Accesibilidad Universal** | 16/09/2026 - 14/10/2026 | Segundo Corte (70%) | [COMPLETADO] | KAN-23 al KAN-54: Contraste WCAG 2.1 AA, teclado accesible, panel administrativo. |
| **Sprint 3: Avance Tercer Corte (15%)** | 04/11/2026 - 11/11/2026 | Avance Examen (85% acum.) | [COMPLETADO] | KAN-55 al KAN-60: Audio humano Saraic Noemí, precarga espacial, diagnóstico WCAG en vivo. |
| **Sprint 4: Cierre Final (15% restante)** | 12/11/2026 - 24/11/2026 | Previo Final 100% (30% total) | [EN PROGRESO] | KAN-61 al KAN-63: Expansión multi-campus, cierre de pruebas Playwright y UAT final. |

---

## 3. DETALLE DE TICKETS DEL AVANCE DEL 15% (SPRINT 3)

1. **KAN-55 [Accesibilidad] Locución Humana Institucional Real:**  
   Sustitución de audio sintético TTS por grabaciones de estudio de Saraic Noemí León Jaimes con subtítulos WebVTT sincronizados.
2. **KAN-56 [Performance] Motor de Precarga Espacial por Grafo de Adyacencia:**  
   Precarga predictiva de panoramas en memoria para transición fluida con 0ms de retraso percibido.
3. **KAN-57 [Frontend] Selector Multi-Sede y Diagnóstico WCAG 2.1 AA:**  
   Nuevo modal interactivo en el visor para inspección en tiempo real de contraste, foco y lectores de pantalla.
4. **KAN-58 [UI/UX] Normalización de Tokens de Diseño Claro/Oscuro:**  
   Corrección de visibilidad de texto y badges en ambos temas garantizando ratio de contraste 8.2:1.
5. **KAN-59 [QA] Especificación de Casos de Prueba Funcionales CRUD:**  
   Casos de prueba de hotspots y navegación formalizados bajo el estándar internacional ISO/IEC/IEEE 29119.
6. **KAN-60 [QA] Auditoría Automatizada de Usabilidad y Lighthouse v2:**  
   Medición de métricas de calidad bajo ISO/IEC 25010: 98/100 en Accesibilidad y 92/100 en Rendimiento.

---

## 4. INTEGRACIÓN BIDIRECCIONAL GITHUB SMART COMMITS

Cada commit en la rama `main` de `https://github.com/KUTEIMO/ORBE-GP` incluye el código de la incidencia entre corchetes:
- `[KAN-55] feat: Integracion de locucion humana de Saraic Noemi y subtitulos WebVTT`
- `[KAN-56] perf: Algoritmo de precarga por adyacencia de nodos espaciales`
- `[KAN-57] feat: Modal de diagnostico WCAG 2.1 AA e indicador de calidad ISO 25010`
- `[KAN-58] fix: Tokens semanticos y contraste para modo claro y modo oscuro`
- `[KAN-59] test: Casos de prueba CRUD de hotspots segun ISO 29119`
- `[KAN-60] test: Reporte de auditoria Lighthouse v2 y matriz de defectos IEEE 829`

Esta trazabilidad garantiza cumplimiento estricto con los lineamientos de la asignatura.
