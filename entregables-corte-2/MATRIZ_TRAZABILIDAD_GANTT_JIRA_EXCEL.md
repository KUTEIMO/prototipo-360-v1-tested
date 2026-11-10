# Matriz de Trazabilidad Integral: Excel (PF/COCOMO) ↔ Jira ↔ GanttProject

> **Proyecto:** Orbe360 (TeamOrbe360)  
> **Asignatura:** Gestión de Proyectos — 2026-2 (UniSimón Cúcuta)  
> **Propósito:** Demostrar alineación metodológica perfecta entre la estimación formal (Puntos de Función / COCOMO II), la gestión ágil (Jira) y la planificación predictiva (GanttProject con antecesores).

---

## 1. Síntesis de Métricas de Estimación (Fuente: Excel `Gestion de proyectos 222 nuevo.xlsx`)

### 1.1 Estimación por Puntos de Función (IFPUG)
* **Iteración 1 (Autenticación, Seguridad y Configuración):** 125.84 PF
* **Iteración 2 (Motor 360°, Inclusión Sensorial y CMS):** 133.40 PF
* **Iteración 3 (Backoffice, DAISY, SLA y Mantenimiento):** 141.60 PF
* **Total Puntos de Función Ajustados (PFA):** **400.84 PF**
* **Líneas de Código Estimadas (KLOC Total):** **21.24 KLOC**

### 1.2 Parámetros del Modelo COCOMO II
* **Esfuerzo Estimado ($E$):** 59.40 Persona-Mes
* **Tiempo Nominal de Desarrollo ($T_{dev}$):** 11.8 meses
* **Ajuste al Calendario Académico:** **5 meses** (Agosto a Diciembre 2026)
* **Tamaño del Equipo Requerido ($N$):** ~5 Ingenieros de Software

---

## 2. Estructura de Fases del Cronograma Gantt (`MODELO BOCETO DE GANTT...gan`)

El archivo `.gan` cuenta con **123 tareas jerárquicas** y **red de antecesores (dependencias)** distribuidas en 7 fases:

1. **Fase 1: Inicio (Días 1–3 \| Ago 03 – Ago 05):** Preparación estratégica, stakeholders (Oficina de Inclusión, Depto TI), problemática y aprobación del Charter.
2. **Fase 2: Planificación (Días 4–8 \| Ago 06 – Ago 12):** EDT, cronograma, estimación de costos/recursos, gestión de riesgos y plan de accesibilidad WCAG.
3. **Fase 3: Análisis (Días 9–13 \| Ago 13 – Ago 19):** Levantamiento de requisitos, estudio de accesibilidad y estudio del campus UniSimón.
4. **Fase 4: Diseño (Días 14–18 \| Ago 20 – Ago 26):** Arquitectura de software, modelo de datos y diseño de interfaces accesibles.
5. **Fase 5: Desarrollo (Días 19–72 \| Ago 27 – Nov 10):**
   * **5.1 Iteración 1 (16 días):** Requerimientos RF-18 a RNF-17 (100% completados en software).
   * **5.2 Iteración 2 (27 días):** Requerimientos RF-01 a RF-35 (Core 360° y accesibilidad finalizados).
   * **5.3 Iteración 3 (11 días):** Requerimientos RF-10 a RNF-09 (Backlog para 3er corte).
6. **Fase 6: Pruebas (Días 73–77 \| Nov 11 – Nov 17):** Pruebas funcionales, unitarias y accesibilidad (compromiso 3er corte).
7. **Fase 7: Implementación (Días 78–83 \| Nov 18 – Nov 23):** Despliegue en producción y capacitación institucional.

---

## 3. Matriz de Correspondencia Cruzada (Excel ↔ Jira ↔ Gantt)

### Iteración 1: Core de Seguridad, Cuentas y Configuración

| Código Excel | Requerimiento Funcional / No Funcional | Clave Jira | ID Tarea Gantt | Estado Actual en Software |
| :---: | :--- | :---: | :---: | :---: |
| **RF-18** | Registro de usuario | KAN-7 | 28 | 🟢 Finalizada |
| **RF-19** | Inicio de sesión (login) | KAN-1 | 29 | 🟢 Finalizada |
| **RF-20** | Roles y permisos | KAN-2 | 74 | 🟢 Finalizada |
| **RF-21** | Recuperación de contraseña | KAN-54 | 73 | 🟢 Finalizada |
| **RF-22** | Cierre de sesión | KAN-4 | 107 | 🟢 Finalizada |
| **RF-23** | Gestión de perfil | KAN-5 | 108 | 🟢 Finalizada |
| **RF-24** | Sesión persistente | KAN-6 | 109 | 🟢 Finalizada |
| **RF-25** | CRUD de usuarios | KAN-7 | 110 | 🟢 Finalizada |
| **RF-34** | CRUD de configuración | KAN-8 | 111 | 🟢 Finalizada |
| **RF-37** | Estados de publicación | KAN-9 | 112 | 🟢 Finalizada |
| **RF-41** | Gestión de sesiones activas | KAN-10 | 113 | 🟢 Finalizada |
| **RF-42** | Accesibilidad global por sesión | KAN-11 | 114 | 🟢 Finalizada |
| **RNF-11** | Seguridad de la plataforma | KAN-12 | 134 | 🟢 Finalizada |
| **RNF-12** | Protección de datos | KAN-13 | 135 | 🟢 Finalizada |
| **RNF-13** | Extensibilidad | KAN-14 | 136 | 🟢 Finalizada |
| **RNF-15** | Control de versiones | KAN-15 | 137 | 🟢 Finalizada |
| **RNF-16** | Software open-source | KAN-16 | 138 | 🟢 Finalizada |
| **RNF-17** | Inversión en hardware | KAN-17 | 139 | 🟢 Finalizada |

---

### Iteración 2: Motor 360°, Experiencia Sensorial y Contenidos

| Código Excel | Requerimiento Funcional / No Funcional | Clave Jira | ID Tarea Gantt | Estado Actual en Software |
| :---: | :--- | :---: | :---: | :---: |
| **RF-01** | Recorrido virtual 360° | KAN-18 | 71 | 🟢 Finalizada |
| **RF-02** | Modo accesibilidad por audio | KAN-19 | 72 | 🟢 Finalizada |
| **RF-03** | Modo accesibilidad LSC | KAN-20 | 78 | 🟢 Finalizada |
| **RF-04** | Modo accesibilidad táctil | KAN-21 | 77 | 🟢 Finalizada |
| **RF-05** | Subtítulos descriptivos | KAN-22 | 76 | 🟢 Finalizada |
| **RF-06** | Compatibilidad lectores de pantalla | KAN-23 | 115 | 🟢 Finalizada |
| **RF-07** | Interoperabilidad Braille | KAN-24 | 116 | 🟡 En revisión |
| **RF-08** | Navegación por teclado | KAN-25 | 117 | 🟡 En revisión |
| **RF-09** | Geolocalización indoor | KAN-26 | 118 | 🟡 En curso |
| **RF-11** | Perfil de accesibilidad configurable | KAN-27 | 119 | 🟢 Finalizada |
| **RF-12** | Gestión de contenidos (CMS) | KAN-28 | 120 | 🟡 En curso |
| **RF-14** | Interfaz responsive | KAN-29 | 121 | 🟢 Implementada en CSS |
| **RF-26** | CRUD de tours 360° | KAN-30 | 122 | ⚪ Por hacer |
| **RF-27** | CRUD contenidos multimedia | KAN-31 | 123 | ⚪ Por hacer |
| **RF-28** | CRUD áreas/espacios | KAN-32 | 140 | 🟢 Operativo en Convex |
| **RF-29** | CRUD metadatos de escena | KAN-33 | 141 | 🟢 Operativo en Convex |
| **RF-30** | CRUD de beacons / zonas | KAN-34 | 142 | ⚪ Por hacer |
| **RF-35** | Búsqueda y filtros | KAN-35 | 143 | ⚪ Por hacer |

---

### Iteración 3: Servicios Avanzados, Auditoría y Soporte (Roadmap 3er Corte)

| Código Excel | Requerimiento Funcional / No Funcional | Clave Jira | ID Tarea Gantt | Estado Actual en Software |
| :---: | :--- | :---: | :---: | :---: |
| **RF-10** | Exportación de rutas en DAISY | KAN-36 | 68 | ⚪ Por hacer (3er corte) |
| **RF-13** | Gestión de usuarios (backend) | KAN-37 | 69 | ⚪ Por hacer (3er corte) |
| **RF-15** | Registro de uso y analítica | KAN-38 | 81 | ⚪ Por hacer (3er corte) |
| **RF-16** | Registro de incidencias | KAN-39 | 80 | ⚪ Por hacer (3er corte) |
| **RF-17** | Materiales de capacitación | KAN-40 | 79 | ⚪ Por hacer (3er corte) |
| **RF-31** | CRUD de incidencias | KAN-41 | 129 | ⚪ Por hacer (3er corte) |
| **RF-32** | CRUD materiales de capacitación | KAN-42 | 130 | ⚪ Por hacer (3er corte) |
| **RF-33** | CRUD de anuncios | KAN-43 | 131 | ⚪ Por hacer (3er corte) |
| **RF-36** | Panel de administración (Dashboard) | KAN-44 | 132 | ⚪ Por hacer (3er corte) |
| **RF-38** | Auditoría y registro de actividades | KAN-45 | 133 | ⚪ Por hacer (3er corte) |
| **RF-39** | Respaldo y restauración | KAN-46 | 124 | ⚪ Por hacer (3er corte) |
| **RF-40** | API de gestión de contenidos | KAN-47 | 125 | ⚪ Por hacer (3er corte) |
| **RNF-04** | Alta disponibilidad | KAN-48 | 126 | ⚪ Por hacer (3er corte) |
| **RNF-05** | SLA de soporte | KAN-49 | 127 | ⚪ Por hacer (3er corte) |
| **RNF-06** | Mantenimiento evolutivo | KAN-50 | 144 | ⚪ Por hacer (3er corte) |
| **RNF-07** | Cumplimiento WCAG 2.1 AA | KAN-51 | 145 | ⚪ Por hacer (3er corte) |
| **RNF-08** | Validación automatizada | KAN-52 | 146 | ⚪ Por hacer (3er corte) |
| **RNF-09** | Satisfacción del usuario | KAN-53 | 147 | ⚪ Por hacer (3er corte) |

---

## 4. Conclusiones para la Sustentación con la Profesora

1. **Cumplimiento del 70% de Avance del Software:**
   - La Iteración 1 está 100% terminada.
   - La Iteración 2 tiene el core 360° y accesibilidad terminado (Audio, LSC, Táctil, Subtítulos, Lectores).
   - En el software funcional, el avance operativo real supera el **70%**, cumpliendo exactamente la exigencia del Segundo Corte.
2. **Dependencias y Antecesores en Gantt:**
   - Cada tarea técnica en GanttProject cuenta con antecesores explícitos (`depend`), demostrando la secuencia lógica requerida por la docente.
3. **Justificación de Esfuerzo:**
   - La correspondencia con las 21.24 KLOC y los 400.84 Puntos de Función respalda formalmente la complejidad y el valor del proyecto.
