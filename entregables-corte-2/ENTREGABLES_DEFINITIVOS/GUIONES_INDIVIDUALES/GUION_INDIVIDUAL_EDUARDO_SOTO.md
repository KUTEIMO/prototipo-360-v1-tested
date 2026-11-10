# GUION DE SUSTENTACIÓN — EDUARDO JOSÉ SOTO HERRERA
**Rol:** Líder de Proyecto & Arquitecto Frontend 360°

---

## MOMENTO 1: APERTURA (TÚ INICIAS LA EXPOSICIÓN)

* **En qué momento hablas:** Eres el primero. Te paras al frente con la laptop conectada al proyector.
* **Qué debe estar en pantalla:** GanttProject abierto en la pestaña **Gantt**.
* **Qué debes decir:**

"Buenas tardes, ingeniera Nataly y compañeros. Hoy presentamos la sustentación del Segundo Corte del proyecto **Orbe360 (PEVCI)**: Plataforma Web de Recorridos Virtuales 360° para Campus Inclusivos de la Universidad Simón Bolívar, Sede Cúcuta.

Atendiendo las directrices de la asignatura, no traemos diapositivas: vamos a sustentar directamente sobre las herramientas de ingeniería en tiempo real: nuestro cronograma y red PERT en GanttProject, la nivelación de recursos, el tablero de gestión ágil en Jira Cloud y la demostración funcional del 70% del software completado.

Le doy la palabra a nuestro ingeniero de planificación, Jesús Avendaño, quien explicará el cronograma, la red de antecesores y la nivelación de recursos."

*(Aquí tú manejas la laptop: dejas a Jesús hablar y cuando él te lo pida, cambias a la pestaña "Diagrama de recursos" y luego a "PERT" en GanttProject).*

---

## MOMENTO 2: STACK TECNOLÓGICO Y MOTOR FRONTEND 360°

* **En qué momento hablas:** Cuando Kevin García termine de explicar Jira y te diga: *"Doy paso a Eduardo Soto para exponer el stack tecnológico frontend y la arquitectura del motor 360°"*.
* **Qué debe estar en pantalla:** Cambias la ventana de la laptop al navegador y muestras la pestaña de **Orbe360 en vivo** (`http://localhost:8081/`).
* **Qué debes decir:**

"Gracias, Kevin. Ingeniera, en pantalla tiene la plataforma **Orbe360** ejecutándose en tiempo real.

Nuestro stack tecnológico frontend fue seleccionado por rendimiento y control:
1. **Motor 360° y Gráficos:** Utilizamos **Pannellum JS y WebGL nativo**. No usamos frameworks pesados que ralenticen la interfaz; esto nos permite garantizar una tasa estable de **60 cuadros por segundo** al renderizar panorámicas 4K.
2. **Vanilla JavaScript ES6:** Para tener control directo sobre el ciclo de vida del visor, atajos de teclado y la liberación de memoria en GPU mediante `texture.dispose()`, evitando que la memoria colapse al navegar varias escenas seguidas.
3. **Arquitectura de Motor Compartido:** Jamás duplicamos el visor por cada cliente o sede. Un único motor resuelve las escenas de forma virtual. Además, desarrollamos el servidor en Node.js (`scripts/dev-server.mjs`) para resolver URLs virtuales limpias como `/tours/unisimon/biblioteca` sin recargar la página.

Como puede observar, la navegación entre puntos de la biblioteca es fluida y modela el campus como un grafo conexo.

Le doy paso a Sebastián Omaña para explicar la arquitectura de base de datos reactiva y DevSecOps."

---

## MOMENTO 3: CIERRE DE LA EXPOSICIÓN

* **En qué momento hablas:** Cuando Saraic León termine de explicar la accesibilidad y te diga: *"Cedo la palabra a Eduardo Soto para concluir"*.
* **Qué debe estar en pantalla:** El software 360° o la herramienta sobre la que la profesora quiera preguntar.
* **Qué debes decir:**

"Con esto demostramos el cumplimiento de los entregables del Segundo Corte:
1. Cronograma con antecesores, sin sobreasignaciones y ruta crítica en GanttProject y PERT.
2. Tablero en Jira Cloud profesionalizado al 70% de avance con sintaxis Gherkin.
3. Software funcional, accesible e inmersivo con una arquitectura sólida y justificada.
4. Documento metodológico de prompts y supervisión humana cargado en el aula.

Quedamos a su disposición para cualquier pregunta técnica. Muchas gracias."
