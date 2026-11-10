# GUION MAESTRO Y FLUJO DE PANTALLA — SUSTENTACIÓN SEGUNDO CORTE
## PROYECTO ORBE360 (PEVCI) — ASIGNATURA: GESTIÓN DE PROYECTOS (2026-2)
**Docente Evaluadora:** Ing. Nataly Duque Páez  
**Duración Total Estimada:** 12 a 15 minutos  
**Modalidad de Presentación:** Laptop de Eduardo conectada al proyector (Sin diapositivas — 100% herramientas en vivo).

---

## 1. PREPARACIÓN PREVIA DE LA LAPTOP (ANTES DE PASAR AL FRENTE)

Tener abiertas y minimizadas exactamente estas 3 ventanas (nada más):
1. **Ventana 1 — GanttProject (Aplicación de escritorio):**
   - Archivo abierto: `GANTT_ORBE360_CORTE_2.gan`.
   - Pestaña inicial lista: **Gantt**.
2. **Ventana 2 — Navegador Web (Pestaña 1: Jira Cloud):**
   - URL lista: Tablero del proyecto KAN (`https://orbe-experience360.atlassian.net/jira/software/projects/KAN/boards`).
   - Tener localizado a la mano el ticket `KAN-18` (Recorrido virtual 360°) o `KAN-1` para abrirlo al hacer clic.
3. **Ventana 2 — Navegador Web (Pestaña 2: Software en Vivo Orbe360):**
   - URL lista: `http://localhost:8081/` (o la ruta del tour de la Biblioteca Anita Consuegra).
   - Servidor ya corriendo en terminal con `npm start`.

---

## 2. MAPA DE TIEMPOS Y ORDEN DE INTERVENCIÓN

```text
┌──────────────────────┬─────────────────────────────┬──────────────────────────┬───────────┐
│ ACTO                 │ EN PANTALLA (EDUARDO OPERA) │ RESPONSABLE QUE HABLA    │ TIEMPO    │
├──────────────────────┼─────────────────────────────┼──────────────────────────┼───────────┤
│ 1. Apertura          │ GanttProject (Vista Gantt)  │ Eduardo Soto (Líder)     │ 1.5 min   │
│ 2. Planificación     │ GanttProject (Gantt,        │ Jesús Avendaño           │ 3.0 min   │
│    y Cronograma      │ Recursos y PERT)            │ (Planificación)          │           │
│ 3. Gestión Ágil Jira │ Navegador (Tablero KAN      │ Kevin García             │ 2.5 min   │
│    y Requerimientos  │ y detalle de KAN-18)        │ (Backend / Jira)         │           │
│ 4. Stack Técnico     │ Navegador (Software 360°    │ Eduardo Soto             │ 2.0 min   │
│    y Motor Frontend  │ en vivo: navegación)        │ (Frontend 360°)          │           │
│ 5. Base de Datos     │ Navegador (Software 360°    │ Sebastián Omaña          │ 2.0 min   │
│    y DevSecOps       │ y panel de control)         │ (DevSecOps / Base Datos) │           │
│ 6. Accesibilidad     │ Navegador (Software 360°    │ Saraic León              │ 2.5 min   │
│    WCAG e Inclusión  │ con audio, LSC y teclado)   │ (Líder Calidad / WCAG)   │           │
│ 7. Cierre y Preguntas│ Gantt / Jira según pregunte │ Eduardo Soto (Líder)     │ 1.5 min   │
└──────────────────────┴─────────────────────────────┴──────────────────────────┴───────────┘
```

---

## 3. FLUJO DE PANTALLA Y DIÁLOGO PASO A PASO

### ACTO 1: APERTURA FORMAL
* **Qué se ve en pantalla:** GanttProject — Pestaña **Gantt**.
* **Quién habla:** **EDUARDO SOTO** (Líder de Proyecto).
* **Diálogo:**
  > "Buenas tardes, ingeniera Nataly y compañeros. Hoy el equipo presenta la sustentación del Segundo Corte del proyecto **Orbe360 (PEVCI)**: Plataforma Web de Recorridos Virtuales 360° para Campus Inclusivos de la Universidad Simón Bolívar, Sede Cúcuta.
  > 
  > Atendiendo las directrices de la asignatura, no traemos diapositivas estáticas: vamos a sustentar directamente sobre nuestras herramientas de ingeniería de software en tiempo real: nuestro cronograma predictivo en GanttProject, la red PERT y nivelación de recursos, nuestro tablero de gestión ágil en Jira Cloud y la demostración funcional del 70% del software completado.
  > 
  > Inicio dando la palabra a nuestro ingeniero de planificación, Jesús Avendaño, quien explicará el cronograma, la red de antecesores y la nivelación de recursos."

---

### ACTO 2: CRONOGRAMA, ANTECESORES, RECURSOS Y PERT
* **Quién habla:** **JESÚS AVENDAÑO** (Ingeniero de Planificación).
* **Acción de Eduardo en pantalla:** Mantiene abierta la pestaña **Gantt** y hace zoom moderado sobre las fases.
* **Diálogo de Jesús (Parte 1 — Gantt y Antecesores):**
  > "Gracias, Eduardo. Ingeniera, en pantalla observa nuestro cronograma oficial en GanttProject. El proyecto está estructurado formalmente en 7 fases WBS: Inicio, Planificación, Análisis, Diseño, Desarrollo (con 3 iteraciones Scrum), Pruebas y Despliegue.
  > 
  > Como usted nos indicó en clase, **todas las tareas técnicas cuentan con sus antecesores y predecesores obligatorios**, garantizando la lógica secuencial del proyecto y permitiendo calcular la ruta crítica. El cronograma total abarca exactamente las 20 semanas del semestre 2026-2."

* **Acción de Eduardo en pantalla:** Cambia a la pestaña **Diagrama de recursos** en GanttProject.
* **Diálogo de Jesús (Parte 2 — Nivelación de Recursos y Eliminación de Barras Rojas):**
  > "Aquí en el Diagrama de Recursos, ingeniera, queremos destacar un punto clave de ingeniería: en el software inicial, cuando teníamos tareas concurrentes en paralelo, GanttProject sumaba las cargas y marcaba barras rojas de sobreasignación del 300% al 600%. 
  > 
  > Aplicando las buenas prácticas de nivelación de recursos (*Resource Leveling* del PMI), ajustamos la carga diaria de forma algorítmica entre las tareas paralelas. Como puede observar en pantalla, **no existe ningún día en sobrecarga (0% barras rojas)**; todos los integrantes estamos al 100% o 50% de capacidad diaria máxima, además de tener asignadas nuestras funciones profesionales oficiales."

* **Acción de Eduardo en pantalla:** Cambia a la pestaña **PERT** (o muestra la vista de red).
* **Diálogo de Jesús (Parte 3 — Red PERT y Cierre):**
  > "Finalmente, en el diagrama de red PERT se observa el encadenamiento lógico de actividades que conectan el diseño del motor con el desarrollo backend y las pruebas de accesibilidad.
  > 
  > Paso la palabra a nuestro compañero Kevin García para sustentar la gestión ágil y los requerimientos en Jira Software."

---

### ACTO 3: GESTIÓN ÁGIL, REQUERIMIENTOS Y JIRA CLOUD
* **Quién habla:** **KEVIN GARCÍA** (Líder Backend & Jira).
* **Acción de Eduardo en pantalla:** Cambia de ventana en la laptop. Abre el navegador con la pestaña de **Jira Software (Tablero KAN)**.
* **Diálogo de Kevin (Parte 1 — Tablero y 70% de Avance):**
  > "Gracias, Jesús. Ingeniera, en pantalla tenemos nuestro tablero oficial en Atlassian Jira Cloud (`orbe-experience360.atlassian.net`). 
  > 
  > Tenemos inventariados los 54 requerimientos del proyecto (RF-01 a RF-42 y RNF-04 a RNF-19) correspondientes a las 3 iteraciones de desarrollo. Para este segundo corte, el avance del 70% solicitado se evidencia en las columnas: tenemos 38 incidencias en estado 'Finalizada' y 'En revisión', cubriendo la totalidad de los módulos core del campus."

* **Acción de Eduardo en pantalla:** Hace clic en el ticket `KAN-18` (RF-01: Recorrido virtual 360º) o `KAN-1` para abrir su panel lateral de detalle.
* **Diálogo de Kevin (Parte 2 — Historias de Usuario, Gherkin y MCP):**
  > "Cada requerimiento no es una simple tarea vacía: cada ticket cuenta con:
  > 1. Su **Historia de Usuario ágil** ('Como... Quiero... Para...').
  > 2. Sus **Criterios de Aceptación bajo sintaxis Gherkin** ('Dado que... Cuando... Entonces...'), que definen la Definición de Terminado (DoD).
  > 3. Su bloque de **trazabilidad técnica** vinculando el código WBS, el código del Excel de estimación y la complejidad IFPUG.
  > 
  > Adicionalmente, profesionalizamos este tablero conectando directamente nuestros agentes mediante el protocolo Atlassian MCP (`atlassian-mcp-server`), manteniendo trazabilidad 1:1 sin modificar las claves históricas `KAN-1` a `KAN-54`.
  > 
  > Doy paso a Eduardo Soto para exponer el stack tecnológico frontend y la arquitectura del motor 360°."

---

### ACTO 4: STACK TECNOLÓGICO FRONTEND Y MOTOR 360°
* **Quién habla:** **EDUARDO SOTO** (Líder de Proyecto & Frontend 360°).
* **Acción de Eduardo en pantalla:** Cambia a la pestaña del navegador con el **Software Orbe360 en vivo** (`http://localhost:8081/`).
* **Diálogo de Eduardo:**
  > "Gracias, Kevin. Ingeniera, en pantalla tiene la plataforma **Orbe360** ejecutándose en tiempo real. 
  > 
  > Nuestro stack tecnológico frontend fue elegido bajo estrictos criterios de rendimiento:
  > * **Motor 360° y Gráficos:** Utilizamos **Pannellum JS y WebGL nativo**. No usamos frameworks pesados que añadan capas de abstracción innecesarias; esto nos permite garantizar una tasa de refresco sostenida de **60 cuadros por segundo** al renderizar imágenes equirectangulares 4K.
  > * **Vanilla JavaScript ES6:** Para tener control milimétrico sobre el ciclo de vida del visor, la captura de eventos de teclado y la liberación de memoria en GPU mediante `texture.dispose()`, evitando caídas de memoria al transitar por el campus.
  > * **Arquitectura de Motor Compartido (Shared Virtual Motor):** Nunca duplicamos el visor por cada cliente o sede. Un único motor resuelve las escenas de forma virtual. Implementamos además el ruteo virtual en Node.js (`scripts/dev-server.mjs`) para resolver URLs limpias como `/tours/unisimon/biblioteca` sin recargar la página.
  > 
  > Como observa al interactuar, las transiciones de pitch, yaw y zoom son fluidas y modelan el campus Anita Consuegra como un grafo conexo.
  > 
  > Doy paso a Sebastián Omaña para explicar la arquitectura de base de datos reactiva y DevSecOps."

---

### ACTO 5: BASE DE DATOS REACTIVA (CONVEX), SEGURIDAD Y DEVSECOPS
* **Quién habla:** **SEBASTIÁN OMAÑA** (Ingeniero DevSecOps & Base de Datos).
* **Acción de Eduardo en pantalla:** Mantiene el software en pantalla, mostrando brevemente la carga fluida de datos o el panel de control.
* **Diálogo de Sebastián:**
  > "Gracias, Eduardo. En la capa de infraestructura y backend elegimos **Convex**:
  > * **Por qué Convex:** Es una base de datos reactiva de última generación que sincroniza datos en tiempo real mediante WebSockets nativos. Cuando una escena o hotspot se actualiza en el panel de administración, el visor en el cliente refleja el cambio al instante sin necesidad de refrescar la página ni configurar polling manual.
  > * **Modelo de Grafos Conexo:** Diseñamos el esquema en `convex/schema.ts` donde cada recinto es un nodo y cada hotspot es una arista dirigida. Las mutaciones aplican la política de *in-place patch* para asegurar que si se actualiza el nombre de una escena, jamás se rompan las conexiones del recorrido.
  > * **Seguridad y Control de Acceso (RBAC):** Blindamos las funciones de mutación (`userCanEditTour`): un Superadmin institucional tiene visibilidad global, pero tiene expresamente restringida la edición directa del contenido de los tours de un cliente para preservar la integridad de la autoría.
  > * **DevSecOps y Calidad:** Contamos con el script `npm run check:drift` para asegurar que el repositorio local sea siempre la única fuente de verdad, y ejecutamos suites de pruebas E2E automatizadas con **Playwright** que validan la carga y navegación en menos de 2 segundos.
  > 
  > Doy paso a Saraic León para sustentar el núcleo de accesibilidad universal e inclusión."

---

### ACTO 6: ACCESIBILIDAD UNIVERSAL (WCAG 2.1 AA) E INCLUSIÓN SENSORIAL
* **Quién habla:** **SARAIC LEÓN** (Líder de Calidad & Accesibilidad).
* **Acción de Eduardo en pantalla:** Sigue las indicaciones de Saraic:
  1. Activa el audio de la escena (hace clic en el icono o pulsa `M`).
  2. Muestra la ventana flotante PIP de Lengua de Señas (LSC).
  3. Desconecta o suelta el mouse y navega usando únicamente el **teclado** (Tab, Shift+Tab, Enter) mostrando el indicador visual de foco.
* **Diálogo de Saraic:**
  > "Gracias, Sebastián. Ingeniera, el factor diferenciador y de mayor impacto social de Orbe360 es la **Accesibilidad Universal bajo la norma WCAG 2.1 nivel AA**:
  > 
  > 1. **Audio Descriptivo Espacial (Web Audio API):** Como escucha en este momento, al entrar a la Biblioteca Anita Consuegra la plataforma narra la distribución del espacio para personas con discapacidad visual. Resolvimos técnicamente un reto de ingeniería: implementamos regiones vivas `aria-live="polite"` y atenuación de audio (*Audio Ducking*) para que el sonido ambiental nunca solape ni interfiera con lectores de pantalla como NVDA o JAWS.
  > 2. **Modo LSC (Lengua de Señas Colombiana):** En la esquina inferior derecha disponemos del componente PIP accesible, sincronizado con la escena activa y operable mediante el atajo `Alt + S`.
  > 3. **Navegación 100% por Teclado:** Como Eduardo demuestra en pantalla sin tocar el mouse, todos los hotspots y controles cuentan con anillo de foco visible con contraste 3:1 y navegación limpia con Tab y Enter, cumpliendo el criterio 2.1.1 de la WCAG.
  > 4. **Estrategia de Pruebas:** Atendiendo su indicación docente de que la documentación del 100% de pruebas se entrega en el tercer corte, ya dejamos formalizada el Acta de Pruebas (Norma ISO 29119) y las matrices para pruebas de Caja Negra, Caja Blanca, Unitarias y Aceptación.
  > 
  > Cedo la palabra a Eduardo Soto para concluir."

---

### ACTO 7: CIERRE Y PREGUNTAS
* **Quién habla:** **EDUARDO SOTO** (Líder de Proyecto).
* **Acción de Eduardo en pantalla:** Deja en pantalla el software 360° o cambia al Gantt/Jira según la profesora pregunte.
* **Diálogo de Eduardo:**
  > "Con esto demostramos el cumplimiento riguroso de los entregables del Segundo Corte:
  > 1. Un cronograma con antecesores, sin sobreasignaciones y ruta crítica en GanttProject y PERT.
  > 2. Un tablero en Jira Cloud profesionalizado al 70% de avance con sintaxis Gherkin.
  > 3. Un software funcional, accesible e inmersivo con una arquitectura sólida y justificada.
  > 4. El registro metodológico formal de prompts y supervisión humana radicado en el aula.
  > 
  > Quedamos a su entera disposición para cualquier pregunta técnica. Muchas gracias."

---

## 4. GUÍA RÁPIDA DE RESPUESTAS A PREGUNTAS DIFÍCILES DE LA PROFESORA

* **Si la profe pregunta:** *«¿Por qué no usaron React o Angular para el visor?»*  
  * **Respuesta (Eduardo/Sebastián):** *«Porque en aplicaciones inmersivas 360° con WebGL, el Virtual DOM de React introduce sobrecarga de re-renderizado que causa caídas de frames (*jank*). Con Vanilla JS logramos una tasa fija de 60 FPS y control directo de la recolección de basura de texturas 4K.»*

* **Si la profe pregunta:** *«¿Cómo hicieron para que no hubiera barras rojas en el Gantt?»*  
  * **Respuesta (Jesús):** *«Aplicamos nivelación de recursos (*Resource Leveling*). Calculamos la concurrencia diaria de tareas paralelas de cada ingeniero y distribuimos porcentualmente la dedicación (50%-50% o 33%-33%) para que la carga acumulada por persona nunca excediera el 100% diario.»*

* **Si la profe pregunta:** *«¿Dónde están las pruebas del software?»*  
  * **Respuesta (Saraic):** *«Como usted nos aclaró en clase, la documentación y ejecución del 100% de pruebas se entrega formalmente en el tercer corte con el software finalizado. Para este corte tenemos la suite automatizada E2E con Playwright ejecutándose y la plantilla formal del Acta de Pruebas ISO 29119 lista.»*
