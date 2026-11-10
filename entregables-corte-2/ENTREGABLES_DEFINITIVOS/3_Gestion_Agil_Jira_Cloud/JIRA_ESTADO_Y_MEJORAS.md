# Auditoría, Estado y Mejoras del Proyecto Jira (TeamOrbe360 - KAN)

> **Instancia:** `https://orbe-experience360.atlassian.net`  
> **Proyecto:** TeamOrbe360 (Clave: `KAN`)  
> **Tipo de Proyecto Jira:** Team-managed Software (Next-Gen)  
> **Total de Requerimientos:** 53 incidencias  
> **Conexión:** Vía Model Context Protocol (`atlassian-mcp-server`)  

---

## 1. Diagnóstico Actual del Tablero

A través de la inspección directa mediante el MCP de Atlassian, se verificó el estado real de los 53 tickets del proyecto:

| Estado Actual | Cantidad | Porcentaje | Interpretación para la Profesora |
| :--- | :---: | :---: | :--- |
| **Finalizada** | 24 | 45.3% | Funcionalidades concluidas, listas para demo en vivo. |
| **En revisión** | 2 | 3.8% | Funcionalidades implementadas en fase de pruebas de usabilidad. |
| **En curso** | 2 | 3.8% | Trabajo actualmente activo (CMS y Geolocalización). |
| **Tareas por hacer** | 25 | 47.1% | Backlog priorizado y hoja de ruta futura (Siguientes Fases). |
| **Total** | **53** | **100%** | Cobertura integral del ciclo de vida del producto. |

### Hallazgos de la Auditoría Técnica:
1. **Puntos Fuertes:**
   - La granularidad de las tareas es excelente: desglosa con detalle aspectos clave como accesibilidad sensorial (audio, LSC, subtítulos, lectores), seguridad, sesiones y arquitectura.
   - Refleja un proyecto con visión de producto completo, no un simple ejercicio de aula.
2. **Oportunidades de Mejora (Profesionalización sin alterar claves KAN):**
   - **Descripciones vacías:** La mayoría de las tareas solo tienen el título (`summary`) y no cuentan con descripción ni Criterios de Aceptación (DoD).
   - **Falta de agrupación por Épicas (Epics):** Las tareas están “sueltas” en el tablero. Agruparlas en 5 grandes Épicas hace que el Roadmap nativo de Jira se vea visualmente impecable y profesional.
   - **Etiquetas (`Labels`) no asignadas:** Al agregar etiquetas estándar (`accesibilidad`, `seguridad`, `frontend`, `backend`, `corte-2`), se pueden crear filtros rápidos para la presentación.
   - **Alineación 1:1 con el Gantt:** El cronograma `.gantt` debe agrupar estas mismas 53 tareas en las mismas fases para mostrar coherencia metodológica absoluta.

---

## 2. Inventario Completo de Tareas (53 Tickets)

### 🟢 Bloque 1: Tareas Finalizadas (24) — Base de la Demostración

| Clave | Título del Ticket | Tipo | Prioridad | Módulo Sugerido |
| :---: | :--- | :---: | :---: | :--- |
| **KAN-1** | Inicio de sesion (login) | Tarea | Media | Autenticación y Cuentas |
| **KAN-2** | Roles y permisos | Tarea | Media | Seguridad y Gobierno |
| **KAN-4** | Cierre de sesion | Tarea | Media | Autenticación y Cuentas |
| **KAN-5** | Gestion perfil | Tarea | Media | Autenticación y Cuentas |
| **KAN-6** | Sesion persistente | Tarea | Media | Arquitectura y Sesiones |
| **KAN-7** | CRUD de usuarios | Tarea | Media | Gestión de Usuarios |
| **KAN-8** | CRUD de configuracion | Tarea | Media | Configuración del Sistema |
| **KAN-9** | Estados de publicacion | Tarea | Media | Gestión de Contenidos |
| **KAN-10** | Gestion de sesiones activas | Tarea | Media | Seguridad y Gobierno |
| **KAN-11** | Accesibilidad global por sesion | Tarea | Media | Accesibilidad Universal |
| **KAN-12** | Seguridad de la plataforma | Tarea | Media | Seguridad y Gobierno |
| **KAN-13** | Proteccion de datos | Tarea | Media | Seguridad y Gobierno |
| **KAN-14** | Extensibilidad | Tarea | Media | Arquitectura de Software |
| **KAN-15** | Control de versiones | Tarea | Media | Arquitectura de Software |
| **KAN-16** | Software open-source | Tarea | Media | Arquitectura de Software |
| **KAN-17** | Inversion de en hardware | Tarea | Media | Infraestructura y Costos |
| **KAN-18** | Recorrido virtual 360° | Tarea | Media | Motor y Core 360° |
| **KAN-19** | Modo accesibilidad por audio | Tarea | Media | Accesibilidad Universal |
| **KAN-20** | Modo accesibilidad LSC | Tarea | Media | Accesibilidad Universal |
| **KAN-21** | Modo accesibilidad táctil | Tarea | Media | Accesibilidad Universal |
| **KAN-22** | Subtítulos descriptivos | Tarea | Media | Accesibilidad Universal |
| **KAN-23** | Compatibilidad lectores de pantalla | Tarea | Media | Accesibilidad Universal |
| **KAN-27** | Perfil de accesibilidad configurable | Tarea | Media | Accesibilidad Universal |
| **KAN-54** | Recuperacion de contraseña | Tarea | Media | Autenticación y Cuentas |

---

### 🟡 Bloque 2: Tareas en Revisión (2) y en Curso (2)

| Clave | Título del Ticket | Estado | Prioridad | Módulo Sugerido |
| :---: | :--- | :---: | :---: | :--- |
| **KAN-24** | Interoperabilidad Braille | En revisión | Media | Accesibilidad Universal |
| **KAN-25** | Navegación por teclado | En revisión | Media | Accesibilidad Universal |
| **KAN-26** | Geolocalización indoor | En curso | Media | Navegación Espacial |
| **KAN-28** | Gestión de contenidos (CMS) | En curso | Media | Gestión de Contenidos |

---

### ⚪ Bloque 3: Tareas por Hacer (25) — Roadmap y Siguientes Fases

| Clave | Título del Ticket | Tipo | Prioridad | Módulo Sugerido |
| :---: | :--- | :---: | :---: | :--- |
| **KAN-29** | Interfaz responsive | Tarea | Media | Frontend y UX |
| **KAN-30** | CRUD de tours 360° | Tarea | Media | Gestión de Contenidos |
| **KAN-31** | CRUD contenidos multimedia | Tarea | Media | Gestión de Contenidos |
| **KAN-32** | CRUD áreas/espacios | Tarea | Media | Gestión de Contenidos |
| **KAN-33** | CRUD metadatos de escena | Tarea | Media | Gestión de Contenidos |
| **KAN-34** | CRUD de beacons / zonas | Tarea | Media | Navegación Espacial |
| **KAN-35** | Búsqueda y filtros | Tarea | Media | UX y Navegación |
| **KAN-36** | Exportación de rutas en DAISY | Tarea | Media | Accesibilidad Avanzada |
| **KAN-37** | Gestión de usuarios | Tarea | Media | Panel de Administración |
| **KAN-38** | Registro de uso | Tarea | Media | Métricas y Analítica |
| **KAN-39** | Registro de incidencias | Tarea | Media | Mesa de Ayuda |
| **KAN-40** | Materiales de capacitación | Tarea | Media | Capacitación y Cambio |
| **KAN-41** | CRUD de incidencias | Tarea | Media | Mesa de Ayuda |
| **KAN-42** | CRUD materiales de capacitación | Tarea | Media | Capacitación y Cambio |
| **KAN-43** | CRUD de anuncios | Tarea | Media | CMS Institucional |
| **KAN-44** | Panel de administración | Tarea | Media | Backoffice |
| **KAN-45** | Auditoría y registro de actividades | Tarea | Media | Seguridad y Cumplimiento |
| **KAN-46** | Respaldo y restauración | Tarea | Media | Infraestructura y DevOps |
| **KAN-47** | API de gestión de contenidos | Tarea | Media | Backend e Integraciones |
| **KAN-48** | Alta disponibilidad | Tarea | Media | Infraestructura y SLA |
| **KAN-49** | SLA de soporte | Tarea | Media | Operaciones y Servicio |
| **KAN-50** | Mantenimiento evolutivo | Tarea | Media | Ciclo de Vida |
| **KAN-51** | Cumplimiento WCAG 2.1 AA | Tarea | Media | Calidad y Normativa |
| **KAN-52** | Validación automatizada | Tarea | Media | QA y Testing |
| **KAN-53** | Satisfacción del usuario | Tarea | Media | Validación de Negocio |

---

## 3. Plan de Mejoras Profesionales (Gratuitas en Jira)

Para lograr un impacto sobresaliente ante la docente sin alterar las claves KAN:

### Propuesta de Épicas (Epics) para Agrupar las Tareas:
En Jira Team-managed se pueden activar las Épicas en el menú de configuración de hoja de ruta:

1. **Épica 1: Motor de Recorrido 360° y Espacialidad**
   - Agrupa: KAN-18, KAN-26, KAN-29, KAN-30, KAN-31, KAN-32, KAN-33, KAN-34, KAN-35.
2. **Épica 2: Ecosistema de Accesibilidad Universal (Inclusión)**
   - Agrupa: KAN-11, KAN-19, KAN-20, KAN-21, KAN-22, KAN-23, KAN-24, KAN-25, KAN-27, KAN-36, KAN-51.
3. **Épica 3: Autenticación, Seguridad y Gobierno de Datos**
   - Agrupa: KAN-1, KAN-2, KAN-4, KAN-5, KAN-6, KAN-7, KAN-10, KAN-12, KAN-13, KAN-37, KAN-45, KAN-54.
4. **Épica 4: Plataforma CMS y Backoffice Administrativo**
   - Agrupa: KAN-8, KAN-9, KAN-28, KAN-41, KAN-42, KAN-43, KAN-44, KAN-47.
5. **Épica 5: Calidad, Operaciones, Infraestructura y Soporte**
   - Agrupa: KAN-14, KAN-15, KAN-16, KAN-17, KAN-38, KAN-39, KAN-40, KAN-46, KAN-48, KAN-49, KAN-50, KAN-52, KAN-53.

### Estructura Estándar de Contenido para cada Ticket:
Cada ticket clave debe tener una descripción formateada así:
* **Historia de Usuario:** *Como [rol] quiero [acción] para [beneficio].*
* **Criterios de Aceptación (Gherkin):**
  * *Dado que el usuario navega a la vista 360...*
  * *Cuando interactúa con el control accesible...*
  * *Entonces el sistema responde con...*
* **Definición de Terminado (DoD):** Pruebas funcionales realizadas y validadas en código.

---

## 4. Bitácora de Modificaciones Realizadas en Jira

> *En esta sección se registrarán cronológicamente los ajustes efectuados a través de las herramientas MCP o manuales.*

| Fecha | Ticket | Modificación Realizada | Estado |
| :---: | :---: | :--- | :---: |
| 2026-10-13 | Todos (KAN-1 a 54) | Auditoría diagnóstica y extracción de metadata vía MCP | ✅ Completada |
| 2026-10-13 | KAN-1 | Actualización con RF-19, Historia de Usuario, Criterios DoD y etiquetas | ✅ Aplicada vía MCP |
| 2026-10-13 | KAN-18 | Actualización con RF-01, Historia de Usuario, Criterios DoD y etiquetas | ✅ Aplicada vía MCP |
| 2026-10-13 | KAN-19 | Actualización con RF-02, Historia de Usuario, Criterios DoD y etiquetas | ✅ Aplicada vía MCP |
| 2026-10-13 | KAN-20 | Actualización con RF-03, Historia de Usuario, Criterios DoD y etiquetas | ✅ Aplicada vía MCP |
| 2026-10-13 | KAN-23 | Actualización con RF-06, Historia de Usuario, Criterios DoD y etiquetas | ✅ Aplicada vía MCP |
| 2026-10-13 | KAN-25 | Actualización con RF-08, Historia de Usuario, Criterios DoD y etiquetas | ✅ Aplicada vía MCP |
| 2026-10-13 | KAN-54 | Actualización con RF-21, Historia de Usuario, Criterios DoD y etiquetas | ✅ Aplicada vía MCP |
