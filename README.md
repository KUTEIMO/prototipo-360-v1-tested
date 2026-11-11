# ORBE360 — Plataforma Multi-Tenant de Recorridos Virtuales 360° Accesibles

Plataforma SaaS B2B para crear, publicar y administrar experiencias espaciales **360° interactivas** con foco nativo en accesibilidad **WCAG 2.1 AA**, aislamiento multi-organización (`white-label` por cliente vía `TourBranding`) y editor espacial integrado (**Control Web**).

> **Delimitación del repositorio vs. archivo académico (`ORBE-GP`):**  
> Este repositorio (`prototipo-360-v1-tested`) contiene el **software completo y activo de Orbe360**, su backend Convex, su empaquetado estático y su despliegue público en la nube.  
> El repositorio académico [`ORBE-GP`](https://github.com/KUTEIMO/ORBE-GP), las carpetas históricas `entregables-corte-2/` y `entregables-corte-3/` y la etiqueta congelada `estable-2026-11-10-solo-sede2` corresponden únicamente al **archivo histórico de entregas del curso** (Universidad Simón Bolívar — Gestión de Proyectos 2026-2) y permanecen separados del ciclo productivo.

---

## 1. Despliegue Público en Producción (`$0` Free Tier)

La aplicación opera en Internet mediante arquitectura desacoplada **HTTPS**, sin costo mensual y sin exponer código fuente interno, variables `.env*` ni credenciales:

| Superficie | URL Pública | Descripción |
| :--- | :--- | :--- |
| **Portal Orbe360** | https://orbe360-unisimon.pages.dev/ | Landing B2B Orbe360 (`Soft Clay #0284c7`), selector EN/ES, tema claro/oscuro y catálogo dinámico de tours publicados. |
| **Visor 360° Unisimón (Sede 2)** | https://orbe360-unisimon.pages.dev/unisimoncucuta/experienciavirtual/ | Recorrido interactivo completo (**88 escenas**, **178 hotspots**, audio-guía Salomé `es-CO`, subtítulos WebVTT, grafo conectado con Bloque D). |
| **Ejemplo escena Bloque D** | https://orbe360-unisimon.pages.dev/unisimoncucuta/experienciavirtual/?scene=bloque-d-plazoleta-acreditacion | Acceso profundo (*deep link*) a la plazoleta de Acreditación en Alta Calidad. |
| **Sandbox Orbe360** | https://orbe360-unisimon.pages.dev/orbe/sandbox/ | Entorno demostrativo aislado para pruebas de identidad neutra Orbe. |
| **Inicio de sesión** | https://orbe360-unisimon.pages.dev/plataforma/login.html | Acceso autenticado para `superadmin`, `orgAdmin` y `tourEditor`. |
| **Panel de Organización** | https://orbe360-unisimon.pages.dev/unisimoncucuta/org-admin.html | Gestión de tours, branding `TourBranding`, publicación WCAG, métricas, bitácora y cuenta propia. |
| **Control Web (Editor 360°)** | https://orbe360-unisimon.pages.dev/unisimoncucuta/experienciavirtual/control-web/ | Editor visual de escenas, hotspots, conexiones espaciales, vistas iniciales y subtítulos/audio. |
| **Declaración WCAG y Legales** | https://orbe360-unisimon.pages.dev/plataforma/accesibilidad.html | Matriz técnica de accesibilidad, privacidad, cookies, términos y tratamiento de datos. |

---

## 2. Cómo Funciona el Despliegue en la Nube (`Convex Cloud` + `Cloudflare Pages`)

```text
  Navegador (HTTPS)
         │
         ├──► Cloudflare Pages (orbe360-unisimon.pages.dev)
         │       ├── Static Assets (_routes.json exclude): /media/*, /css/*, /src/*, /vendors/*
         │       │     (transferencia estática ilimitada gratuita para panoramas y audios MP3/VTT)
         │       └── Pages Function (functions/[[path]].js):
         │             • Reescribe /{org}/{tour}/, /{org}/org-admin.html y /{org}/{tour}/control-web/
         │             • Redirige legacy /plataforma/* → /
         │             • Bloquea archivos internos (404/410 en /.env*, /convex/*, /docs/*, /panoramas/*)
         │
         └──► Convex Cloud (https://careful-gnu-592.convex.cloud · proyecto orbe360-unisimon)
                 ├── Queries / Mutations reactivas sobre HTTPS/WSS
                 ├── Tablas: organizations, tours, tourBrandings, scenes, hotspots,
                 │           connections, platformUsers, sessions, auditLogs, tourMetrics, loginAttempts
                 └── Convex File Storage: subida autenticada de panoramas y audios desde Control Web
```

### Detalles clave de `Convex Cloud` en producción
1. **Deployment productivo:** `orbe360-unisimon` (`https://careful-gnu-592.convex.cloud`). El frontend compilado en `./dist` recibe esta URL en tiempo de build mediante `ORBE_CONVEX_URL` dentro de `orbe-config.js` y `plataforma/config.js`, sin guardar secretos ni claves privadas en el repositorio.
2. **Aislamiento multi-tenant y RBAC:**
   - `superadmin` gestiona organizaciones, altas de tours, usuarios y bitácora global, pero permanece bloqueado a nivel de backend (`userCanEditTour`) para modificar contenido o escenas de clientes.
   - `orgAdmin` administra tours, branding `TourBranding` (validado contra acentos internos de Orbe), publicación WCAG y métricas/bitácora únicamente de su organización.
   - `tourEditor` edita escenas, hotspots, conexiones y multimedia en Control Web sin permisos de publicación ni marca.
   - Los recorridos no publicados (`sede-1`, `sede-3`, `sede-4` en borrador con `published: false`) no se exponen en rutas públicas (`graph:getTourGraph` / `graph:listPublishedDemos`).
3. **Endurecimiento activo en Convex Cloud:**
   - Contraseñas almacenadas con **PBKDF2-SHA256** + *salt* aleatorio por usuario; tokens de sesión revocables y límite de intentos en `loginAttempts`.
   - `ALLOW_OPEN_SEED` y `SEED_BOOTSTRAP_SECRET` **desactivados/eliminados** en producción (verificado en entorno `prod`). Las credenciales reales iniciales se resguardan fuera de Git en `backups/CREDENCIALES_PROD_NO_SUBIR.txt` (gitignored).
4. **Por qué `/media/*` se sirve desde Cloudflare Pages:** los panoramas equirectangulares y paquetes de audio Salomé superan los `395 MB`. Al excluir `/media/*` de `functions/[[path]].js` mediante `dist/_routes.json`, Cloudflare Pages los entrega como estáticos globales con ancho de banda ilimitado en capa gratuita (`<= 25 MiB` por archivo), reservando **Convex File Storage** únicamente para las cargas dinámicas realizadas en vivo desde Control Web.

---

## 3. Despliegue Local en Desarrollo (Cualquier Equipo)

Requisitos previos: **Node.js 20 LTS o superior** y **Git** (en Windows, macOS o Linux).

### 3.1 Instalación y arranque paso a paso (Windows / macOS / Linux)

1. **Clonar e instalar dependencias:**
   ```bash
   git clone https://github.com/KUTEIMO/prototipo-360-v1-tested.git ORBE
   cd ORBE
   npm install
   ```

2. **Terminal 1 — Levantar backend local de Convex:**
   ```bash
   npx convex dev
   ```
   > En la primera ejecución en un equipo nuevo, Convex CLI te guiará para iniciar sesión o elegir despliegue **local** (`http://127.0.0.1:3210` guardado automáticamente en `.env.local`, ignorado por Git). Nunca uses `npx convex deploy` durante desarrollo diario.

3. **Solo la primera vez (en BD local vacía) — Poblar datos base, Sandbox y las 88 escenas (`Bloque D` + `Sede 1, 3 y 4`):**
   ```bash
   npx convex env set ALLOW_OPEN_SEED 1
   npx convex env set SEED_SUPERADMIN_PASSWORD "OrbeSuper2026!"
   npx convex env set SEED_ORGADMIN_PASSWORD "UnisimonAdmin2026!"
   npm run seed
   npm run seed:orbe-sandbox
   npm run sync:fotitos
   ```
   *(Cambia esas contraseñas locales libremente; si usas otras distintas a las de desarrollo local, pásalas como `ORBE_SUPER_PASS` / `ORBE_UNI_PASS` al ejecutar `npm run sync:fotitos`.)*

4. **Terminal 2 — Levantar servidor web con routing virtual multi-tenant:**
   ```bash
   npm start
   ```
   Abre **`http://127.0.0.1:8081/`** en tu navegador (`localhost:8081` también resuelve a Convex local `127.0.0.1:3210`).

### 3.2 Inicio rápido en Windows (`INICIAR_PROYECTO.bat` / PowerShell)

- **Doble clic en [`INICIAR_PROYECTO.bat`](INICIAR_PROYECTO.bat):** verifica Node.js, ejecuta `npm install` si falta `node_modules/`, abre `npx convex dev` si el puerto `3210` no responde, lanza `http://127.0.0.1:8081/` y arranca `scripts/dev-server.mjs`.
- **Prueba en red local (LAN / celular) o apuntando la web local a otro backend Convex:**
  - Copia `config.local.js.example` → `config.local.js` (gitignored) o define en consola del navegador `localStorage.setItem("orbe360.convexUrl", "https://...")` si deseas probar el frontend local contra un despliegue Convex específico.
  - Para abrir desde otro dispositivo de tu misma red Wi-Fi:
    ```powershell
    $env:HOST = "0.0.0.0"; npm start
    ```

### 3.3 Mapa de rutas en local (`127.0.0.1:8081`)

| Superficie | URL Local |
| :--- | :--- |
| **Portal Orbe360** | `http://127.0.0.1:8081/` |
| **Visor Unisimón (Sede 2)** | `http://127.0.0.1:8081/unisimoncucuta/experienciavirtual/` |
| **Org Admin Unisimón** | `http://127.0.0.1:8081/unisimoncucuta/org-admin.html` |
| **Control Web Unisimón** | `http://127.0.0.1:8081/unisimoncucuta/experienciavirtual/control-web/` |
| **Sandbox Orbe + Editor** | `http://127.0.0.1:8081/orbe/sandbox/` y `/orbe/sandbox/control-web/` |
| **Login y Superadmin** | `http://127.0.0.1:8081/plataforma/login.html` y `/plataforma/superadmin.html` |

---

## 4. Despliegue a Producción desde Cualquier Equipo

Consulta también [deploy/README.md](deploy/README.md) y [docs/producto/67-plan-despliegue-seguro-produccion.md](docs/producto/67-plan-despliegue-seguro-produccion.md).

1. **Desplegar esquema y funciones en Convex Cloud:**
   ```bash
   npx convex deploy
   ```
   Asegura que `ALLOW_OPEN_SEED` no esté en `"1"` ni `SEED_BOOTSTRAP_SECRET` siga presente tras inicializar el entorno productivo (`npx convex env list --names-only --prod`).

2. **Construir paquete estático sanitizado `./dist`:**
   ```powershell
   # PowerShell (en Bash usa: ORBE_CONVEX_URL="https://careful-gnu-592.convex.cloud" npm run build:prod)
   $env:ORBE_CONVEX_URL = "https://careful-gnu-592.convex.cloud"
   npm run build:prod
   ```
   El script [`scripts/build-static-dist.mjs`](scripts/build-static-dist.mjs) excluye `.env*`, `convex/`, `docs/`, `scripts/`, `backups/`, `tests/`, `entregables-*` y archivos `.md`, e inyecta la URL HTTPS productiva en `dist/orbe-config.js` y `dist/plataforma/config.js`.

3. **Publicar en Cloudflare Pages (con `functions/[[path]].js`):**
   ```bash
   npx wrangler login
   npx wrangler pages deploy dist --project-name=orbe360-unisimon --branch=main
   ```
   *(Alternativa incluida: `firebase deploy --only hosting --config dist/firebase.json`.)*

---

## 5. Accesibilidad (WCAG 2.1 AA), Seguridad y Verificación

- **Accesibilidad:** audiodescripción por escena y hotspot con voz neural colombiana (**Salomé `es-CO-SalomeNeural`**), subtítulos **WebVTT**, transcripción descargable `.txt`, región `aria-live`, diálogo dinámico de diagnóstico WCAG (`#wcagAuditDialog`), contraste calculado por luminancia relativa (`contrastInkForHex`), navegación completa por teclado (`Tab`, `Esc`, flechas SVG) y soporte `?embed=1`.
- **Seguridad:** saneamiento de URLs de branding y descargas (`urlSafety.ts`), bloqueo de *open redirects* y retornos *cross-org* en `login.html`, bloqueo de rutas internas en `dev-server.mjs` y `functions/[[path]].js`, políticas `X-Content-Type-Options: nosniff`, `X-Frame-Options: SAMEORIGIN`, `Referrer-Policy` y `Permissions-Policy`.

### Comandos de calidad y auditoría

| Comando | Qué valida |
| :--- | :--- |
| `npm run check:static` | ESLint (`eslint .`, reglas `@convex-dev/eslint-plugin`) y `tsc -p convex/tsconfig.json --noEmit`. |
| `npm run audit:routes` | Integridad de enlaces Markdown, rutas HTTP y referencias multimedia multi-tenant. |
| `npm run check:a11y` | Cobertura completa de narración, subtítulos, transcripciones y archivos `.mp3` locales. |
| `npm run test:unit` | Pruebas unitarias Node (`tourSlug`, contraste WCAG, parser WebVTT, grafo espacial y checklist). |
| `npm run qa:authz` | Aislamiento RBAC entre `superadmin`, `orgAdmin`, `tourEditor` y anónimo en Control Web. |
| `npm run qa` | Suite contractual de backend, branding, snapshot, routing, File Storage y rate-limit. |
| `npm test` | Suite E2E completa en Chromium con Playwright (`tests/`). |

---

## 6. Estructura del Repositorio y Documentación

- `plataforma/`: portal web B2B (`index.html`), login, paneles `org-admin.html` / `superadmin.html` y páginas legales/accesibilidad.
- `index.html` + `src/` + `css/` + `vendors/`: motor visor 360° neutro y módulos de accesibilidad WebGL.
- `control-web/`: editor visual autenticado de tours, hotspots y grafo espacial.
- `convex/`: esquema y funciones backend tipadas en TypeScript.
- `functions/` + `deploy/`: router Cloudflare Pages Functions y guía operativa de producción.
- `media/`: panoramas equirectangulares y paquetes de audio/VTT aislados por organización y tour (`/{org}/{tour}/`).
- `docs/`: mapa técnico completo en [docs/README.md](docs/README.md) (incluyendo [reglas UI/UX 66](docs/producto/66-reglas-diseno-ui-ux-y-flujos-orbe360.md), [plan productivo 67](docs/producto/67-plan-despliegue-seguro-produccion.md) y [auditoría final 68](docs/producto/68-desarrollo-final-y-auditoria-validacion.md)).

### Equipo de Desarrollo
**Eduardo José Soto Herrera**, **Saraic Noemí León Hernández**, **Kevin Eduardo García Moreno**, **Sebastián David Omaña Villamizar**, **Jesús Omar Avendaño Avendaño** — Programa de Ingeniería de Sistemas, Universidad Simón Bolívar (Cúcuta).
