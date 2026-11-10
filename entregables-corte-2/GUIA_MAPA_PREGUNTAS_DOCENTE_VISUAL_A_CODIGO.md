# GUÍA MAPA DE PREGUNTAS DEL PARCIAL: DE LO VISUAL AL CÓDIGO
**Proyecto:** ORBE360 — Plataforma de Experiencias Espaciales 360° Inclusivas  
**Propósito:** Preparación exhaustiva para la sustentación del 2° Corte (Gestión de Proyectos).  
**Destinatarios:** Eduardo Soto, Sebastián Omaña, Saraic León, Jesús Avendaño, Kevin García.  
**Ubicación:** `entregables-corte-2/GUIA_MAPA_PREGUNTAS_DOCENTE_VISUAL_A_CODIGO.md` *(Fuera de la carpeta definitiva de entrega para estudio interno)*.

---

## 🎯 Instrucción Táctica para el Equipo

Cuando la docente señale la pantalla y pregunte:  
> *"¿Y este botón/efecto dónde está programado? Muéstrenme en qué archivo y qué función hace eso."*

**NUNCA titubeen ni duden.** Apliquen siempre la **Fórmula de Respuesta en 3 Pasos (15 a 20 segundos):**
1. **Archivo y Ubicación:** *"Profe, ese elemento visual está en el archivo `[Ruta del Archivo]`, en la función o selector `[Nombre]`."*
2. **Cómo está programado:** *"Funciona mediante `[Tecnología o Lógica: Canvas 2D, EventListener, Marzipano, Convex, etc.]`."*
3. **Justificación / Arquitectura:** *"Se implementó así para garantizar `[Accesibilidad WCAG / Rendimiento / Routing Multi-tenant]`."*

---

# 🗺️ MAPA VISUAL COMPLETO: PANTALLA POR PANTALLA

---

## 1. PANTALLA: LANDING PAGE DE LA PLATAFORMA (`/`)

### 🔘 1.1. Botón de Modo Oscuro / Claro (Icono Sol / Luna en el Header)
* **¿Qué señala la docente?:** El botón con icono de sol/luna ubicado arriba a la derecha en la barra de navegación.
* **Archivo de Estructura (HTML):** [`plataforma/index.html`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/plataforma/index.html) $\to$ `<button id="themeToggle" class="icon-btn icon-btn--theme">` (línea ~48).
* **Archivo de Lógica (JS):** [`plataforma/marketing-motion.js`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/plataforma/marketing-motion.js) $\to$ Función `initThemeToggle()` (líneas ~35-70).
* **Archivo de Estilos (CSS):** [`plataforma/marketing.css`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/plataforma/marketing.css) $\to$ selectores `[data-theme="dark"]` y `.icon-btn--theme`.
* **Cómo explicarlo (Respuesta de 15 segundos):**
  > *"Profe, el botón de tema está en `plataforma/index.html` con ID `themeToggle`. Su lógica está en `marketing-motion.js`. Al hacer clic, conmuta el atributo `data-theme` en la etiqueta `<html>` entre `'dark'` y `'light'`, y guarda la elección en `localStorage.setItem('orbe_theme', ...)` para que cuando el usuario recargue o regrese, la página recuerde su preferencia visual."*

---

### 🔘 1.2. Barra de Navegación Superior Transparente / Esmerilada (Header)
* **¿Qué señala la docente?:** La barra superior con el logo de ORBE360, enlaces y botones que al inicio no tiene franja rígida y al bajar se vuelve un cristal borroso.
* **Archivo HTML:** [`plataforma/index.html`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/plataforma/index.html) $\to$ `<header class="public-nav" id="publicNav">` (línea ~35).
* **Archivo JS:** [`plataforma/marketing-motion.js`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/plataforma/marketing-motion.js) $\to$ Listener `onScroll` con `nav.classList.toggle("is-scrolled", window.scrollY > 24)` (línea ~84).
* **Archivo CSS:** [`plataforma/marketing.css`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/plataforma/marketing.css) $\to$ `.public-nav` (transparente en reposo) e `.public-nav.is-scrolled` con `backdrop-filter: blur(20px)` (líneas ~140-180).
* **Cómo explicarlo:**
  > *"El header está en `plataforma/index.html` (`#publicNav`). En `marketing.css` lo diseñamos para que al tope de la página sea 100% transparente y no corte el fondo del Hero. En `marketing-motion.js`, cuando el scroll supera los 24px, le inyectamos la clase `.is-scrolled` que activa el cristal esmerilado con `backdrop-filter: blur(20px)` para asegurar contraste al leer el menú sobre cualquier contenido."*

---

### 🔘 1.3. Orbe Pequeño que Sigue al Mouse con Halo y Estela (Cursor Interactivo)
* **¿Qué señala la docente?:** El orbe azul resplandeciente que persigue suavemente el puntero del mouse por toda la pantalla.
* **Archivo HTML:** [`plataforma/index.html`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/plataforma/index.html) $\to$ `<canvas id="cursorOrbCanvas" class="cursor-canvas">` (línea ~23).
* **Archivo JS:** [`plataforma/marketing-motion.js`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/plataforma/marketing-motion.js) $\to$ Objeto `mouseOrb`, listeners `mousemove` y bloque de renderizado en `cCtx` dentro de `render()` (líneas ~445-474 y ~640-685).
* **Archivo CSS:** [`plataforma/marketing.css`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/plataforma/marketing.css) $\to$ `.cursor-canvas` con `position: fixed; inset: 0; z-index: 999; pointer-events: none;`.
* **Cómo explicarlo:**
  > *"Ese es nuestro orbe interactivo de primer plano. Se renderiza en un canvas HTML5 dedicado (`#cursorOrbCanvas`) ubicado en la capa superior `z-index: 999` con `pointer-events: none` para no interferir con los clics. En `marketing-motion.js` capturamos las coordenadas del mouse y aplicamos una interpolación lineal de inercia (`mouseOrb.x += (targetX - x) * 0.18`), dibujando el halo con un gradiente radial y una cola de estela de 7 puntos anteriores."*

---

### 🔘 1.4. Burbujas Flotantes de Fondo que Rebotan en los Bordes (Físicas Salvapantallas)
* **¿Qué señala la docente?:** Las burbujas volumétricas translúcidas que se mueven de fondo por toda la página y rebotan elásticamente al tocar los lados.
* **Archivo HTML:** [`plataforma/index.html`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/plataforma/index.html) $\to$ `<canvas id="ambient3dCanvas" class="story-bg__canvas">` (línea ~27).
* **Archivo JS:** [`plataforma/marketing-motion.js`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/plataforma/marketing-motion.js) $\to$ Array `orbs` (8 orbes distribuidos del Hero al Footer) y función de renderizado en `bgCtx` (líneas ~335-440 y ~505-590).
* **Cómo explicarlo:**
  > *"Son las partículas ambientales en `#ambient3dCanvas` (`z-index: 0`). En `marketing-motion.js` programamos un array de 8 orbes con velocidades vectoriales `vx` y `vy`. Tienen físicas elásticas inspiradas en salvapantallas: al colisionar con el borde de la ventana (`orb.x <= 0` o `orb.x >= width`), invierten su velocidad y sufren una deformación elástica de aplastamiento (`squishX = 0.74, squishY = 1.26`) que se recupera armónicamente. Además, si el cursor se acerca, sufren una repulsión magnética calculada con `Math.hypot`."*

---

### 🔘 1.5. Anillo 3D Geométrico de Puntos (Wireframe Espacial)
* **¿Qué señala la docente?:** La figura geométrica 3D transparente hecha de puntos y líneas que rota en perspectiva a la derecha del Hero y a lo largo del scroll.
* **Archivo JS:** [`plataforma/marketing-motion.js`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/plataforma/marketing-motion.js) $\to$ Array `ringPoints`, ecuaciones de rotación trigonométrica 3D (`rotX, rotY, rotZ`) y proyección matemática con campo de visión (`fov = 420`) (líneas ~475-486 y ~590-640).
* **Cómo explicarlo:**
  > *"Es un render 3D matemático ejecutado directamente en Canvas 2D sin bibliotecas pesadas. En `marketing-motion.js` definimos un toroide de 32 puntos tridimensionales $(x, y, z)$. En cada fotograma calculamos matrices de rotación en los tres ejes vinculadas al tiempo y al progreso del scroll del usuario, proyectándolas al plano 2D mediante una fórmula de perspectiva con distancia focal (`fov = 420 / (fov + z)`)."*

---

### 🔘 1.6. Carrusel Interactivo de las 4 Sedes en Formato Acordeón
* **¿Qué señala la docente?:** La sección donde aparecen las fotos de Campus Central, Biblioteca, Laboratorios de Salud y Simulación, y al pasar el mouse una se expande y las otras se encogen.
* **Archivo HTML:** [`plataforma/index.html`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/plataforma/index.html) $\to$ `<div class="sedes-accordion">` con las 4 tarjetas `<a class="sede-card">` (líneas ~215-265).
* **Archivo JS:** [`plataforma/marketing-motion.js`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/plataforma/marketing-motion.js) $\to$ Función `initSedesAccordion()` (líneas ~275-308).
* **Archivo CSS:** [`plataforma/marketing.css`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/plataforma/marketing.css) $\to$ Clases `.sedes-accordion`, `.sede-card` y `.sede-card.is-active` (uso de `flex: 1` y `flex: 3.5` para la expansión suave).
* **Cómo explicarlo:**
  > *"Es nuestro acordeón interactivo de campus. El HTML está en `index.html` dentro de `.sedes-accordion`. En CSS usamos Flexbox dinámico: las tarjetas inactivas tienen `flex: 1` y la activa tiene `flex: 3.5` con transición suave de 400ms. En `marketing-motion.js` programamos la función `initSedesAccordion()` con un retardo seguro de 85 milisegundos (`setTimeout`) al pasar el cursor; esto evita que si el usuario cruza el mouse rápidamente la interfaz salte bruscamente."*

---

### 🔘 1.7. Botón "Ingresar al Tour 360°" de una Sede
* **¿Qué señala la docente?:** El enlace o botón dentro de una tarjeta de sede que te lleva al recorrido virtual.
* **Archivo HTML:** [`plataforma/index.html`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/plataforma/index.html) $\to$ `href="/unisimoncucuta/experienciavirtual/?sede=1"` (o sede 2, 3, 4).
* **Archivo de Redirección / Servidor:** [`scripts/dev-server.mjs`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/scripts/dev-server.mjs) $\to$ Middleware de reescritura de URLs virtuales.
* **Cómo explicarlo:**
  > *"Ese enlace invoca la URL amigable multi-empresa `/{organizacion}/{tour}/?sede=ID`. Nuestro servidor Node.js en `scripts/dev-server.mjs` intercepta esa ruta virtual sin duplicar el motor ni crear carpetas repetidas, y sirve el visor Marzipano cargando en memoria la escena inicial de esa sede específica desde `config.json`."*

---

### 🔘 1.8. Botón "Acceso Panel Admin" o "Acceder"
* **¿Qué señala la docente?:** El botón azul principal en el header o en el CTA final para entrar a la plataforma.
* **Archivo HTML:** [`plataforma/index.html`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/plataforma/index.html) $\to$ `<a href="/plataforma/login.html">`.
* **Archivo Destino:** [`plataforma/login.html`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/plataforma/login.html) y lógica de validación en [`plataforma/auth.js`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/plataforma/auth.js).
* **Cómo explicarlo:**
  > *"Ese enlace conduce a `plataforma/login.html`. Desde allí se gestiona la autenticación de los administradores de la organización mediante tokens de sesión validados en `auth.js` antes de dar paso al Control Web o al panel de configuración institucional."*

---

# 🌐 2. PANTALLA: RECORRIDO VIRTUAL 360° (`/{org}/{tour}/`)

### 🔘 2.1. El Visor Panorámico 360° (La Imagen Esférica que se Arrastra)
* **¿Qué señala la docente?:** El visor interactivo donde se puede mirar en 360 grados arrastrando con el mouse.
* **Archivo HTML:** [`index.html`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/index.html) $\to$ `<div id="pano"></div>`.
* **Archivo JS Principal:** [`src/viewer.js`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/src/viewer.js) y [`src/main.js`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/src/main.js).
* **Motor Base:** Marzipano (`marzipano.js`).
* **Cómo explicarlo:**
  > *"El contenedor `#pano` está en `index.html`. En `src/viewer.js` inicializamos la instancia de Marzipano (`new Marzipano.Viewer(panoElement)`). `viewer.js` carga los panoramas equirectangulares configurados en `config.json`, inicializa la geometría esférica, la cámara de perspectiva y escucha los eventos de arrastre táctil y de ratón."*

---

### 🔘 2.2. Flechas de Navegación en el Piso (Hotspots de Enlace entre Escenas)
* **¿Qué señala la docente?:** Las flechas interactivas en el suelo que al hacerles clic te transportan al siguiente pasillo o sala.
* **Archivo JS de Creación:** [`src/hotspotManager.js`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/src/hotspotManager.js) $\to$ Función `createLinkHotspotElement()`.
* **Archivo JS de Orientación Espacial:** [`src/spatialNav.js`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/src/spatialNav.js) $\to$ Cálculo del ángulo de rotación hacia el siguiente nodo.
* **Archivo CSS:** [`css/components/direction-cue.css`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/css/components/direction-cue.css) y [`css/components/nav-hotspot.css`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/css/components/nav-hotspot.css).
* **Cómo explicarlo:**
  > *"Las flechas se generan dinámicamente en `src/hotspotManager.js`. Leen del archivo `config.json` el punto tridimensional (`yaw` y `pitch`) y la escena destino. En `src/spatialNav.js` calculamos la rotación angular precisa para que la flecha siempre apunte en la dirección física real hacia donde queda el siguiente espacio, y `direction-cue.css` le da la animación de pulso invitando a avanzar."*

---

### 🔘 2.3. Pines de Información (Hotspots Informativos con icono "i" o Audio)
* **¿Qué señala la docente?:** Los círculos flotantes con iconos de información o sonido que abren descripciones de los lugares.
* **Archivo JS:** [`src/hotspotManager.js`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/src/hotspotManager.js) $\to$ Función `createInfoHotspotElement()`.
* **Archivo CSS:** [`css/components/hotspots.css`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/css/components/hotspots.css).
* **Cómo explicarlo:**
  > *"Están en `src/hotspotManager.js`. Cada pin es un elemento DOM inyectado en las coordenadas esféricas del visor. Al hacer clic o presionar Enter con el teclado, despacha un evento que invoca el panel lateral de detalles con información accesible."*

---

### 🔘 2.4. Panel Lateral que se Abre al Clicar un Hotspot (Hotspot Panel)
* **¿Qué señala la docente?:** La ventana lateral o modal que emerge con el título, descripción detallada, audio y botón de cerrar.
* **Archivo HTML / Template:** [`index.html`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/index.html) $\to$ `<aside id="hotspot-panel" role="dialog" aria-modal="true">`.
* **Archivo JS:** [`src/hotspotPanel.js`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/src/hotspotPanel.js) $\to$ Funciones `openHotspotPanel()`, `closeHotspotPanel()`.
* **Archivo CSS:** [`css/components/hotspot-panel.css`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/css/components/hotspot-panel.css).
* **Cómo explicarlo:**
  > *"El panel es un diálogo accesible en `index.html` (`#hotspot-panel`). Su controlador está en `src/hotspotPanel.js`. Cumple la norma WCAG: atrapa el foco del teclado dentro del diálogo (`focus trap`), anuncia el título al lector de pantalla mediante ARIA Live Regions, y permite cerrarse tanto con el botón de cruz como con la tecla Escape."*

---

### 🔘 2.5. Botón y Menú de Accesibilidad Universal (Icono de Persona / Discapacidad)
* **¿Qué señala la docente?:** El botón flotante con el icono de accesibilidad que abre las opciones de inclusión.
* **Archivo HTML:** [`index.html`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/index.html) $\to$ Botón `#accessibility-btn` y panel `#accessibility-menu`.
* **Archivo JS:** [`src/accessibility.js`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/src/accessibility.js) $\to$ Módulo de gestión de preferencias accesibles.
* **Archivo CSS:** [`css/menu/accessibility-menu.css`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/css/menu/accessibility-menu.css).
* **Cómo explicarlo:**
  > *"El menú de accesibilidad está estructurado en `index.html` y controlado por `src/accessibility.js`. Gestiona 4 conmutadores clave: Alto Contraste (para baja visión), Tamaño de Texto Dinámico, Narraciones Descriptivas automáticas y Pausa de Animaciones (para personas con sensibilidad vestibular o epilepsia fotosensible)."*

---

### 🔘 2.6. Reproducción de Audios Descriptivos y Subtítulos Sincronizados
* **¿Qué señala la docente?:** Cuando una escena o punto habla con voz narradora y salen subtítulos abajo.
* **Archivo JS de Audio:** [`src/sceneAudio.js`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/src/sceneAudio.js) $\to$ Gestión de la etiqueta `<audio>` y ciclo de vida de pistas.
* **Archivo JS de Subtítulos:** [`src/vttParser.js`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/src/vttParser.js) $\to$ Parser estándar de archivos `.vtt` (WebVTT).
* **Carpeta de Audios y Subtítulos:** `assets/audio/` y `assets/captions/`.
* **Cómo explicarlo:**
  > *"El sistema de audio está en `src/sceneAudio.js`. Al entrar a una escena, verifica si hay una pista de audio asociada en `config.json`. Si el usuario tiene activados los subtítulos, `src/vttParser.js` analiza el archivo WebVTT correspondiente en `assets/captions/` y renderiza el texto sincronizado segundo a segundo con el tiempo de reproducción."*

---

### 🔘 2.7. Menú Inferior de Selección de Escenas (Selector con Miniaturas)
* **¿Qué señala la docente?:** La barra o menú que lista todas las habitaciones, salas y pisos con sus nombres para saltar directamente a una.
* **Archivo JS:** [`src/menu.js`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/src/menu.js) $\to$ Función `initSceneMenu()` y render de miniaturas.
* **Archivo CSS:** [`css/menu/scene-menu.css`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/css/menu/scene-menu.css).
* **Cómo explicarlo:**
  > *"El menú de escenas está programado en `src/menu.js`. Lee el listado de escenas de la organización, genera los botones accesibles con sus etiquetas descriptivas y, al seleccionar una escena, llama al método `switchScene(targetScene)` de `viewer.js` para realizar una transición visual suave."*

---

### 🔘 2.8. Navegación Total por Teclado (Flechas del Teclado, Tab, 1-4)
* **¿Qué señala la docente?:** Cuando navegan sin usar el mouse, solo con el teclado.
* **Archivo JS:** [`src/keyboardControls.js`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/src/keyboardControls.js) $\to$ Listener `keydown` global.
* **Cómo explicarlo:**
  > *"Todo el soporte de teclado está centralizado en `src/keyboardControls.js`. Mapea las flechas del teclado para rotar la cámara (`yaw/pitch`), las teclas `+` y `-` para hacer zoom, `Tab` para recorrer secuencialmente cada hotspot interactivo, y atajos numéricos para saltar rápidamente de escena. Cada elemento enfocado recibe un anillo de contraste conforme a WCAG 2.1 AA."*

---

# ⚙️ 3. PANTALLA: CONTROL WEB / ADMINISTRADOR DE TOURS (`/{org}/{tour}/control-web/`)

### 🔘 3.1. Visor de Edición de Hotspots en Vivo (Donde se Arrastra el Pin)
* **¿Qué señala la docente?:** La pantalla de edición donde se ve la foto 360 y el administrador hace clic para crear un punto o moverlo.
* **Archivo HTML:** [`control-web/index.html`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/control-web/index.html) $\to$ Contenedor `#admin-pano`.
* **Archivo JS:** [`control-web/admin.js`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/control-web/admin.js) $\to$ Escucha de eventos de clic en el visor y conversión de coordenadas pantalla a esféricas `view.screenToCoordinates({ x, y })`.
* **Cómo explicarlo:**
  > *"En `control-web/admin.js` montamos una instancia de Marzipano en modo edición. Cuando el administrador hace clic sobre cualquier parte del panorama, tomamos la posición en pantalla y la transformamos matemáticamente en coordenadas esféricas tridimensionales `yaw` y `pitch`, ubicando de inmediato el marcador editable."*

---

### 🔘 3.2. Formulario Lateral de Configuración de Hotspot
* **¿Qué señala la docente?:** El formulario donde se escribe el título del punto, su descripción y se elige si es de Información, de Navegación o de Audio.
* **Archivo HTML:** [`control-web/index.html`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/control-web/index.html) $\to$ `<form id="hotspot-form">`.
* **Archivo JS:** [`control-web/admin.js`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/control-web/admin.js) $\to$ Función `bindHotspotForm()` y validación de tipos.
* **Cómo explicarlo:**
  > *"Ese formulario está en `control-web/index.html` (`#hotspot-form`) y su lógica reside en `control-web/admin.js`. Permite seleccionar el tipo de hotspot (`info`, `scene`, `audio`), enlazar la escena de destino si es de navegación, y adjuntar las pistas de narración descriptiva."*

---

### 🔘 3.3. Botón "Guardar Cambios" y Persistencia en la Base de Datos
* **¿Qué señala la docente?:** El botón de guardar que actualiza los datos para que queden grabados permanentemente.
* **Archivo JS:** [`control-web/admin.js`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/control-web/admin.js) $\to$ Función `saveTourConfiguration()`.
* **Backend y Datos:** Carpeta [`convex/`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/convex/) (mutaciones reactivas) y fallback local en `config.json`.
* **Cómo explicarlo:**
  > *"El botón de guardar ejecuta la función `saveTourConfiguration()` en `control-web/admin.js`. Si el backend cloud está conectado, envía la mutación a nuestra base de datos Convex para sincronización en tiempo real multi-usuario. Si opera de modo autónomo local, actualiza la estructura JSON garantizando persistencia inmediata sin pérdida de enlaces del grafo."*

---

### 🔘 3.4. White-Label: Personalización de Logo y Marca de la Organización
* **¿Qué señala la docente?:** Dónde se configura para que aparezca el logo de la Universidad Simón Bolívar o de cualquier otra empresa cliente.
* **Archivo JS:** [`src/tourBranding.js`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/src/tourBranding.js) $\to$ Función `applyBranding(orgData)`.
* **Archivo de Configuración:** [`orbe-config.js`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/orbe-config.js) y esquema en `convex/schema.ts`.
* **Cómo explicarlo:**
  > *"La arquitectura White-Label se procesa en `src/tourBranding.js`. ORBE360 separa estrictamente la plataforma SaaS del cliente final. `tourBranding.js` lee los metadatos institucionales (nombre, logo SVG/PNG, colores primarios CSS) y los inyecta en el visor y el banner, manteniendo la identidad visual de la institución sin necesidad de alterar el código del motor."*

---

# 🏗️ 4. PREGUNTAS TRAMPA DE ARQUITECTURA (CÓMO DEFENDERSE)

### ❓ Pregunta 1: *"¿Ustedes crearon una copia de la página para la sede 1, otra para la sede 2 y otra para la sede 3?"*
* **Respuesta Correcta:**
  > *"No, profesora. Jamás duplicamos código. Aplicamos **Routing Virtual Multi-Empresa**. Hay un único motor visor compartido (`index.html` + `src/`). Cuando se solicita `/unisimoncucuta/experienciavirtual/?sede=2`, el servidor en `scripts/dev-server.mjs` resuelve la solicitud dinámicamente inyectando en memoria los datos de esa sede. Esto garantiza escalabilidad: si creamos 50 sedes o 10 empresas nuevas, no hay que duplicar ningún archivo HTML ni JS."*

### ❓ Pregunta 2: *"¿Dónde está la base de datos de los hotspots y escenas?"*
* **Respuesta Correcta:**
  > *"La base de datos reactiva está implementada en **Convex Cloud** en la carpeta `convex/` (tablas de organizaciones, tours y grafos de hotspots). Para la entrega offline del aula y portabilidad sin internet, el sistema cuenta con un adaptador de persistencia en `config.json` que contiene el grafo completo de nodos y conexiones de la Universidad Simón Bolívar."*

### ❓ Pregunta 3: *"¿Cómo demuestran que esto cumple accesibilidad y no es solo diseño visual?"*
* **Respuesta Correcta:**
  > *"Cumplimos pautas **WCAG 2.1 nivel AA**. Tenemos navegación completa por teclado en `src/keyboardControls.js`, anunciador de voz ARIA Live en `src/announcer.js`, soporte de subtítulos sincronizados WebVTT en `src/vttParser.js`, y los contrastes de color fueron validados con Chrome DevTools superando la relación mínima de 4.5:1 tanto en modo claro como en modo oscuro."*

---

## 📌 Resumen de Archivos Clave para Mostrar en Pantalla

Si la docente pide: *"Abran el archivo en VS Code para verlo"*, abran de inmediato:
1. **Para la Landing Page:** [`plataforma/index.html`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/plataforma/index.html) y [`plataforma/marketing-motion.js`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/plataforma/marketing-motion.js).
2. **Para el Visor 360:** [`src/viewer.js`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/src/viewer.js) y [`src/hotspotManager.js`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/src/hotspotManager.js).
3. **Para la Accesibilidad:** [`src/accessibility.js`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/src/accessibility.js) y [`src/sceneAudio.js`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/src/sceneAudio.js).
4. **Para el Editor Admin:** [`control-web/admin.js`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/control-web/admin.js).
5. **Para el Servidor y Rutas:** [`scripts/dev-server.mjs`](file:///c:/Users/SOTO/APLICATIVOS/proyectos%20unisimon/ORBE/scripts/dev-server.mjs).
