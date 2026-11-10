# Project Charter (Acta de Constitución del Proyecto) — Orbe360
> **Código:** CHR-ORBE-01  
> **Proyecto:** Orbe360 — Plataforma Web de Recorridos Virtuales 360° con Inclusión y Accesibilidad Universal  
> **Institución:** Universidad Simón Bolívar (Sede Cúcuta)  
> **Docente Evaluadora:** Ing. Nataly Duque Páez  
> **Asignatura:** Gestión de Proyectos — 2026-2  
> **Fecha de Emisión:** Agosto 2026 (Línea Base) | Revisión 3º Corte: Noviembre 2026 (Avance 15% / Cierre 30%)  

---

## 1. Información General del Proyecto
* **Nombre del Proyecto:** ORBE360 — Experiencia Virtual 360° e Inclusión (PEVCI)
* **Patrocinador / Cliente:** Universidad Simón Bolívar — Oficina de Inclusión y Dpto. TI
* **Líder de Proyecto:** Eduardo José Soto Herrera
* **Equipo de Desarrollo:** 5 Ingenieros (Eduardo Soto, Saraic León, Kevin García, Sebastián Omaña, Jesús Avendaño)
* **Presupuesto Consolidado:** $63.000.000 COP | 400.84 PFA | 59.40 Persona-Mes (COCOMO II)
* **Metodología:** Híbrida (Predictiva con WBS/Gantt/PERT + Ágil con Scrum/Jira)

---

## 2. Acuerdo Formal de Evaluación — Tercer Corte (30% del Proyecto)
En atención a las directrices de la docente Ing. Nataly Duque Páez, el 30% del proyecto se divide formalmente en:
1. **Primer 15% (Avance al 11 de Noviembre de 2026 — Entrega Actual):**
   - Software funcional con locución humana universitaria real (grabada por Saraic Noemí León) integrada canónicamente en `scenes/` y `hotspots/`.
   - Optimización del visor 360: eliminación de excepciones de cámara (`resolveInitialView`), algoritmo de precarga por adyacencia espacial (`preloadNeighbors`) y transiciones rápidas a 110ms.
   - Rediseño de landing page accesible con acordeón dinámico de sedes (`.sedes-accordion`), fondo ambiental (`.page-bg`), contraste WCAG AA en modo claro/oscuro y Bento Grid de 3 columnas.
   - Especificación formal de pruebas bajo normas ISO/IEC/IEEE 29119 (CRUD) e ISO/IEC 25010 (Lighthouse).
2. **Segundo 15% (Cierre Definitivo al 24 de Noviembre de 2026 — Previo Final):**
   - Culminación del 100% del software ('todo el sogo') desplegado en producción.
   - Ejecución y certificación del 100% del banco de 80+ pruebas de software en Playwright.
   - Expansión de fotografías 360° en una segunda sede universitaria (Sede 1 / Sede 3).
   - Entrega final del Acta de Aceptación del Cliente UAT firmada.

---

## 3. Desglose del Alcance (100% Total)
* **70% Inicial (Segundo Corte — Aprobado):** Motor Marzipano WebGL, autenticación por roles en Convex, recorrido piloto de biblioteca, WBS de 123 tareas y 54 tickets Jira.
* **15% Avance (Tercer Corte — 11 de Noviembre):** Locución humana real de Noemí, precarga espacial sin retardo, acordeón elástico de sedes, tokens claro/oscuro y diseño de pruebas.
* **15% Final (Compromiso Previo — 24 de Noviembre):** Ejecución total de pruebas, nueva sede universitaria, despliegue 100% y acta UAT.

---

## 4. Mockups y Arquitectura Visual de la Aplicación
```text
+-----------------------------------------------------------------------------------------+
|  ORBE360  [Logo USB]            [Recorrido 360]   [Características]   [Sedes]   [ES/EN] [[CLARO]/[OSCURO]] |
+-----------------------------------------------------------------------------------------+
|                                                                                         |
|       Transforma tus espacios físicos en experiencias 360° interactivas                  |
|       Recorridos virtuales de alta fidelidad con accesibilidad universal WCAG 2.1 AA   |
|                                                                                         |
|       [  [PLAY] Iniciar Recorrido Virtual  ]        [  [ADMIN] Panel de Administración  ]          |
+-----------------------------------------------------------------------------------------+
|  ACORDEÓN DINÁMICO DE SEDES:                                                            |
|  [ Sede 1: Bloques A-C ]  [ Sede 2: Biblioteca (EXPANDIDA) ]  [ Sede 3: Ciencias Salud ] |
+-----------------------------------------------------------------------------------------+
```
