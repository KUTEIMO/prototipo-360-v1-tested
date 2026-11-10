# Entregables Segundo Corte — Gestión de Proyectos (UniSimón)

> **Centro de Control y Trazabilidad Oficial**  
> **Proyecto:** Orbe360 (PEVCI) — Experiencias Virtuales 360° para Campus Inclusivos  
> **Asignatura:** Gestión de Proyectos — 2026-2 (UniSimón Sede Cúcuta)  
> **Docente Evaluadora:** Ing. Nataly Duque Páez  
> **Equipo (5 Ingenieros):** Eduardo Soto (Líder), Sara, Kevin, David, Omar  

---

## 1. Alcance Actualizado de la Entrega (Segundo Corte)

> 📢 **CAMBIO DE ALCANCE CONFIRMADO:**  
> **Ya NO se entregan diapositivas.** La entrega se enfoca exclusivamente en la solidez técnica y metodológica de 4 pilares:
> 1. **Documento Oficial de TODOS los Prompts de IA Utilizados** (Word `.docx` y Markdown).
> 2. **Jira Software (`KAN`) estructurado y configurado formalmente** (Historias de Usuario, Criterios de Aceptación Gherkin, Etiquetas y Trazabilidad).
> 3. **GanttProject (`.gan`) con Antecesores y Recursos Asignados** (5 ingenieros con roles y cargas de trabajo).
> 4. **Exportaciones Formales de GanttProject** (Diagrama de Gantt, Red PERT y Reporte de Recursos).

---

## 2. Inventario de Entregables Listos para Calificación

| Pilar | Entregable Oficial | Archivo Generado | Estado |
| :---: | :--- | :--- | :---: |
| **01** | **Documento Maestro de Prompts de IA** | [`DOCUMENTO_OFICIAL_PROMPTS_AGENTES_IA.docx`](./DOCUMENTO_OFICIAL_PROMPTS_AGENTES_IA.docx) y [`.md`](./DOCUMENTO_OFICIAL_PROMPTS_AGENTES_IA.md) | 🟢 **Listo en Word y MD** |
| **02** | **Jira Software (`KAN`) Profesional** | `https://orbe-experience360.atlassian.net` (Auditado en [`JIRA_ESTADO_Y_MEJORAS.md`](./JIRA_ESTADO_Y_MEJORAS.md)) | 🟢 **Actualizado vía MCP** |
| **03** | **Cronograma Gantt con Recursos y Antecesores** | [`GANTT_ORBE360_CORTE_2.gan`](./GANTT_ORBE360_CORTE_2.gan) | 🟢 **123 Tareas Asignadas** |
| **04** | **Exportación: Diagrama de Gantt (PDF)** | [`GANTT_ORBE360_CORTE_2.pdf`](./GANTT_ORBE360_CORTE_2.pdf) | 🟢 **Exportado** |
| **05** | **Exportación: Reporte de Recursos y Carga** | [`reportes_gantt/REPORTE_RECURSOS_Y_CARGA.html`](./reportes_gantt/REPORTE_RECURSOS_Y_CARGA.html) | 🟢 **Generado** |
| **06** | **Exportación: Diagrama PERT / Red** | [`reportes_gantt/DIAGRAMA_PERT_RED_DE_ACTIVIDADES.html`](./reportes_gantt/DIAGRAMA_PERT_RED_DE_ACTIVIDADES.html) | 🟢 **Generado** |
| **07** | **Matriz de Trazabilidad 1:1 (54 Reqs)** | [`MATRIZ_TRAZABILIDAD_GANTT_JIRA_EXCEL.md`](./MATRIZ_TRAZABILIDAD_GANTT_JIRA_EXCEL.md) | 🟢 **Listo** |
| **08** | **Métricas Puntos de Función & COCOMO II** | [`Gestion de proyectos 222 nuevo.xlsx`](./Gestion%20de%20proyectos%20222%20nuevo.xlsx) | 🟢 **400.84 PF \| 21.24 KLOC** |
| **09** | **Project Charter Oficial** | [`formatos/acta_constitucion_proyecto_charter_CORTE2_MEJORADA.docx`](./formatos/acta_constitucion_proyecto_charter_CORTE2_MEJORADA.docx) | 🟢 **Cifras Unificadas** |
| **10** | **Software Funcional (70%+ Avance)** | Servidor local `http://127.0.0.1:8081/` (Workspace `ORBE`) | 🟢 **Listo para Demo** |

---

## 3. Estructura de Carpetas

```text
entregables-corte-2/
├── README.md                                       # Este panel central de control
├── DOCUMENTO_OFICIAL_PROMPTS_AGENTES_IA.docx       # Documento Word oficial de prompts para la docente
├── DOCUMENTO_OFICIAL_PROMPTS_AGENTES_IA.md         # Versión Markdown del registro de prompts
├── MATRIZ_TRAZABILIDAD_GANTT_JIRA_EXCEL.md         # Trazabilidad cruzada de 54 requerimientos
├── JIRA_ESTADO_Y_MEJORAS.md                        # Auditoría y bitácora de cambios en Jira
├── Gestion de proyectos 222 nuevo.xlsx             # Modelo de estimación PF y COCOMO II
├── GANTT_ORBE360_CORTE_2.gan                       # GanttProject con 5 recursos y antecesores
├── GANTT_ORBE360_CORTE_2.pdf                       # PDF del cronograma
├── reportes_gantt/
│   ├── REPORTE_RECURSOS_Y_CARGA.html               # Reporte detallado de recursos y asignaciones
│   └── DIAGRAMA_PERT_RED_DE_ACTIVIDADES.html       # Diagrama de red PERT y ruta crítica
├── formatos/
│   ├── acta_constitucion_proyecto_charter_CORTE2_MEJORADA.docx # Charter corregido sin contradicciones
│   ├── PROJECT_CHARTER.md                          # Versión Markdown del Charter
│   └── PLANTILLA_Y_GUIA_DE_PRUEBAS.md              # Estándar de pruebas anticipado para el 3er corte
└── presentacion/
    └── GUION_SUSTENTACION_SEGUNDO_CORTE.md         # Notas y defensa metodológica
```

---

## 4. Guía para Exportar desde GanttProject (Si la docente pide exportación nativa)

1. Abrir **GanttProject** en el computador.
2. Abrir el archivo: `entregables-corte-2/GANTT_ORBE360_CORTE_2.gan`.
3. Para exportar cada vista:
   * **Diagrama de Gantt:** Menú `Proyecto -> Exportar -> Documento PDF -> Vista: Diagrama de Gantt` $\rightarrow$ Guardar como PDF.
   * **Diagrama PERT:** Menú `Proyecto -> Exportar -> Documento PDF / Imagen -> Vista: Diagrama PERT` $\rightarrow$ Guardar como PDF o PNG.
   * **Gráfico de Recursos:** Menú `Proyecto -> Exportar -> Documento PDF / Imagen -> Vista: Diagrama de Recursos` $\rightarrow$ Guardar como PDF.
   *(Los 5 integrantes y las 97 tareas ya están 100% cableados en el archivo, por lo que saldrán completos y sin campos vacíos).*
