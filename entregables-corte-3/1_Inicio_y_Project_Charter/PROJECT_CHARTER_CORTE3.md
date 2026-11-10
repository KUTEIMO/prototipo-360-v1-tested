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
   - Culminación del 100% del software desplegado.
   - Ejecución y certificación del 100% del banco de 80+ pruebas de software en Playwright.
   - Carga fotográfica 360° en Sede 4 (Bloque G) y extensión hacia Sedes 1 y 3 (Bloques A, E y F).
   - Entrega final del Acta de Aceptación del Cliente UAT firmada.

---

## 3. Desglose del Alcance (100% Total)
* **70% Inicial (Segundo Corte — Aprobado):** Motor Marzipano WebGL, autenticación por roles en Convex, recorrido piloto de Sede 2 (Bloques B, C y D), WBS de 123 tareas (257 antecesores) y 54 tickets Jira.
* **15% Avance (Tercer Corte — 11 de Noviembre -> 85% Acumulado):** Locución humana real de Saraic Noemí, Estudio de Audio Salomé en Control Web, auth multi-rol Convex sin mocks, precarga espacial, Sede 4 (Bloque G) en borrador, rediseño UI/UX Soft Clay y 50%+ de pruebas ISO 29119 / ISO 25010.
* **15% Final (Compromiso Previo — 24 de Noviembre):** Ejecución total de pruebas, carga fotográfica multi-sede, despliegue 100% y acta UAT.

---

## 4. Trazabilidad a las Correcciones del Primer Corte
1. **Duración COCOMO II vs. Semestre:** 11.8 meses nominales secuenciales cubiertos en 5 meses con 5 ingenieros concurrentes (59.40 Persona-Mes).
2. **Presupuesto unificado:** consolidado en **$63.000.000 COP**.
3. **Puntos de Función (IFPUG):** matriz de 54 RF/RNF y 14 GSC = **400.84 PFA** (`21.24 KLOC`).
4. **Antecesores y Nivelación Gantt:** 123 tareas con 257 predecesores (`depend`), red PERT y 0% barras rojas de sobreasignación.
5. **Avance real en software:** evolución de documentación (1er corte) -> 70% funcional (2do corte) -> **85% acumulado (Avance 15% Corte 3)**.
6. **Reencuadre PM:** inclusión WCAG 2.1 AA tratada como NFR medible bajo alcance acotado piloto vs. backlog.

---

## 5. Mockups y Arquitectura Visual de la Aplicación
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
|  ACORDEÓN DINÁMICO DE SEDES (UNISIMÓN CÚCUTA):                                         |
|  [ Sede 1: Bloque A ]  [ Sede 2: Bloques B, C y D (ACTIVA) ]  [ Sede 3: E y F ] [ Sede 4: G ] |
+-----------------------------------------------------------------------------------------+
```
