# Project Charter (Acta de Constitución del Proyecto) — Orbe360

> **Código:** CHR-ORBE-01  
> **Proyecto:** Orbe360 — Plataforma Web de Recorridos Virtuales 360° con Inclusión y Accesibilidad Universal  
> **Institución:** Universidad Simón Bolívar (Sede Cúcuta)  
> **Asignatura:** Gestión de Proyectos — 2026-2  
> **Fecha de Emisión:** Agosto 2026 (Línea Base) \| Revisión 2º Corte: Octubre 2026  

---

## 1. Información General del Proyecto

| Parámetro | Detalle |
| :--- | :--- |
| **Nombre del Proyecto** | Orbe360 — Experiencia Virtual 360° e Inclusión |
| **Patrocinador / Cliente** | Universidad Simón Bolívar — Oficina de Inclusión y Depto. TI |
| **Líder de Proyecto** | Eduardo José Soto Herrera |
| **Equipo de Desarrollo** | Equipo de 5 Ingenieros (Estimación COCOMO II) |
| **Duración Estimada** | 5 Meses Académicos (Agosto 2026 – Diciembre 2026) |
| **Metodología de Gestión** | Híbrida (Predictiva con WBS/Gantt/PERT + Ágil con Scrum/Jira) |

---

## 2. Justificación y Planteamiento del Problema

### Problemática:
El campus de la Universidad Simón Bolívar (Sede Cúcuta) presenta barreras físicas y de orientación para nuevos estudiantes, visitantes y, en particular, para personas en situación de discapacidad visual, auditiva o motriz. Los mapas tradicionales en PDF o fotografías estáticas no proporcionan una experiencia inmersiva ni cuentan con adaptaciones sensoriales.

### Solución Propuesta (Orbe360):
Desarrollar una plataforma web accesible de recorridos 360° interactivos del campus que incorpore:
1. Navegación fluida entre espacios mediante grafos de panoramas equirectangulares.
2. Modos de accesibilidad sensorial: audio guía descriptiva, videos en Lengua de Señas Colombiana (LSC), navegación 100% por teclado y compatibilidad con lectores de pantalla (WCAG 2.1 AA).
3. Panel de gestión para la administración de escenas, puntos de interés (hotspots) y usuarios.

---

## 3. Objetivos del Proyecto

* **Objetivo General:** Desarrollar e implementar la plataforma web Orbe360 para la exploración inmersiva del campus universitario, garantizando al menos un nivel AA de conformidad con las pautas de accesibilidad WCAG 2.1.
* **Objetivos Específicos:**
  1. Diseñar la arquitectura de datos y motor WebGL para renderizado panorámico 360° interactivo.
  2. Implementar los módulos de accesibilidad universal (Audio 3D, LSC, alto contraste, lectores de pantalla).
  3. Establecer un sistema de autenticación, roles y seguridad de la información.
  4. Gestionar el proyecto mediante estimaciones formales (Puntos de Función / COCOMO II) y control de avance en Jira y GanttProject.

---

## 4. Alcance del Proyecto

### Dentro del Alcance (In Scope):
* Recorrido virtual de los espacios piloto del campus (Entrada, Cafetería, Biblioteca, Patios, Zonas culturales).
* Hotspots informativos y de transición con audio y video LSC.
* Módulo de autenticación con roles (Superadmin, Administrador, Estudiante/Aspirante).
* Soporte para dispositivos de escritorio, tabletas y móviles.
* Pruebas de software (Caja Negra, Caja Blanca, Aceptación y Unitarias en 3er corte).

### Fuera del Alcance (Out of Scope para la entrega académica):
* Infraestructura de hardware físico especializado en el campus (beacons Bluetooth físicos).
* Aplicaciones nativas de iOS/Android compiladas (se opta por Web App Responsive / PWA).
* Integración con sistemas de matrícula financiera de la universidad.

---

## 5. Estimación de Esfuerzo, Tamaño y Costos (Métricas Formales)

Basado en el estudio técnico en `Gestion de proyectos 222 nuevo.xlsx`:

* **Puntos de Función (IFPUG):**
  * Iteración 1: 125.84 PF
  * Iteración 2: 133.40 PF
  * Iteración 3: 141.60 PF
  * **Total PFA:** **400.84 Puntos de Función Ajustados**
* **Tamaño del Software:** **21.24 KLOC** (Miles de líneas de código).
* **Modelo COCOMO II:**
  * Esfuerzo: **59.40 Persona-Mes**.
  * Tiempo nominal: 11.8 meses (ajustado por intensidad de equipo a **5 meses**).
  * Equipo nominal: **5 desarrolladores**.

---

## 6. Hitos y Cronograma Maestro

| Hito | Fase Asociada | Fecha Prevista | Estado |
| :---: | :--- | :---: | :---: |
| **H1** | Aprobación del Project Charter y EDT | 05/08/2026 | ✅ Completado |
| **H2** | Planificación, Riesgos y Arquitectura Base | 26/08/2026 | ✅ Completado |
| **H3** | Cierre de Iteración 1 (Seguridad y Auth) | 16/09/2026 | ✅ Completado |
| **H4** | **Sustentación Segundo Corte (70% Avance)** | **14/10/2026** | 🟢 **Hito Actual** |
| **H5** | Cierre de Iteración 3 (CMS y Servicios) | 10/11/2026 | ⚪ En planificación |
| **H6** | Pruebas Integrales y Documentación QA | 17/11/2026 | ⚪ Compromiso 3er Corte |
| **H7** | Despliegue Final y Cierre del Proyecto | 23/11/2026 | ⚪ Compromiso 3er Corte |

---

## 7. Principales Interesados (Stakeholders)

| Stakeholder | Rol en el Proyecto | Nivel de Influencia | Expectativa Principal |
| :--- | :--- | :---: | :--- |
| **Dirección UniSimón** | Sponsor Institucional | Alto | Proyectar la modernidad e inclusión del campus. |
| **Oficina de Inclusión** | Usuario Clave / Asesor | Alto | Accesibilidad real para estudiantes con discapacidad. |
| **Departamento TI** | Soporte Técnico / Infraestructura | Medio | Cumplimiento de estándares web y seguridad. |
| **Docente Evaluadora** | Auditora Metodológica | Alto | Rigor en la gestión predictiva (Gantt/PERT) y ágil (Jira). |
| **Estudiantes / Aspirantes** | Usuarios Finales | Medio | Navegación intuitiva, rápida y sin barreras. |

---

## 8. Riesgos Iniciales y Mitigación

1. **Riesgo 1 (Técnico):** Incompatibilidad de navegadores antiguos con WebGL para panoramas 360°.  
   *Mitigación:* Implementar detección de capacidades y vista fallback accesible 2D.
2. **Riesgo 2 (Gestión):** Desviación en el cronograma por complejidad de las pruebas sensoriales.  
   *Mitigación:* Trasladar la ejecución formal de pruebas al 3er corte y mantener suite automatizada con Playwright.
3. **Riesgo 3 (Metodológico):** Desalineación entre Jira y el archivo Gantt.  
   *Mitigación:* Matriz de trazabilidad cruzada 1:1 con 54 requerimientos mapeados.

---

## 9. Firmas de Aprobación

| Rol | Nombre | Firma | Fecha |
| :--- | :--- | :--- | :--- |
| **Líder de Proyecto** | Eduardo José Soto Herrera | __________________ | __/__/2026 |
| **Docente Evaluador** | Ing. Nataly | __________________ | __/__/2026 |
| **Representante del Cliente** | Delegado UniSimón | __________________ | __/__/2026 |
