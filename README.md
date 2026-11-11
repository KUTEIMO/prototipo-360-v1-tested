# ORBE360 — Plataforma Multi-Tenant de Recorridos Virtuales 360° Accesibles

Plataforma B2B para crear, publicar y administrar experiencias espaciales **360° interactivas** con accesibilidad **WCAG 2.1 AA** integrada, aislamiento multi-organización (`white-label` por cliente vía `TourBranding`), locución neural sincronizada y editor visual en navegador (**Control Web**).

---

## 1. Demo y Entorno Público en Producción (`$0` Free Tier)

La plataforma está desplegada en Internet sobre infraestructura **HTTPS** desacoplada, sin exponer secretos, archivos `.env*`, código fuente de backend ni herramientas internas:

| Superficie | URL Pública | Descripción |
| :--- | :--- | :--- |
| **Portal Orbe360** | https://orbe360-unisimon.pages.dev/ | Landing principal (`Soft Clay #0284c7`), selector bilingüe EN/ES, tema claro/oscuro y catálogo vivo de tours publicados. |
| **Visor 360° Piloto (Sede 2)** | https://orbe360-unisimon.pages.dev/unisimoncucuta/experienciavirtual/ | Recorrido completo (**88 escenas**, **178 hotspots**, audiodescripción Salomé `es-CO`, subtítulos WebVTT y Bloque D integrado). |
| **Acceso profundo (Bloque D)** | https://orbe360-unisimon.pages.dev/unisimoncucuta/experienciavirtual/?scene=bloque-d-plazoleta-acreditacion | Enlace directo a escena específica vía `?scene=`. |
| **Sandbox Orbe360** | https://orbe360-unisimon.pages.dev/orbe/sandbox/ | Entorno demostrativo aislado con identidad neutra de plataforma. |
| **Inicio de sesión** | https://orbe360-unisimon.pages.dev/plataforma/login.html | Acceso autenticado multi-rol (`superadmin`, `orgAdmin`, `tourEditor`). |
| **Panel de Organización** | https://orbe360-unisimon.pages.dev/unisimoncucuta/org-admin.html | Gestión de tours, branding `TourBranding`, checklist WCAG, métricas, bitácora y perfil. |
| **Control Web (Editor 360°)** | https://orbe360-unisimon.pages.dev/unisimoncucuta/experienciavirtual/control-web/ | Editor visual de escenas, hotspots, conexiones espaciales, vistas iniciales y audio/VTT. |
| **Accesibilidad y Legales** | https://orbe360-unisimon.pages.dev/plataforma/accesibilidad.html | Declaración WCAG, privacidad, cookies, términos y tratamiento de datos. |

---

## 2. Arquitectura Cloud (`Convex Cloud` + `Cloudflare Pages`)

```text
  Navegador (HTTPS)
         │
         ├──► Cloudflare Pages (orbe360-unisimon.pages.dev)
         │       ├── Estáticos excluidos (_routes.json): /media/*, /css/*, /src/*, /vendors/*
         │       │     (entrega CDN global gratuita e ilimitada para panoramas y audio MP3/VTT)
         │       └── Pages Function (functions/[[path]].js):
         │             • Enruta virtualmente /{org}/{tour}/, /{org}/org-admin.html y /{org}/{tour}/control-web/
         │             • Redirige rutas heredadas (/plataforma/* → /)
         │             • Bloquea archivos internos y dotfiles (404/410 en /.env*, /convex/*, /docs/*, /panoramas/*)
         │
         └──► Convex Cloud (https://careful-gnu-592.convex.cloud · proyecto orbe360-unisimon)
                 ├── Queries / Mutations reactivas sobre HTTPS/WSS
                 ├── Tablas: organizations, tours, tourBrandings, scenes, hotspots,
                 │           connections, platformUsers, sessions, auditLogs, tourMetrics, loginAttempts
                 └── Convex File Storage: subida autenticada de panoramas y audios desde Control Web
```

### Cómo está desplegado `Convex Cloud`
1. **Instancia productiva:** proyecto `orbe360-unisimon` (`https://careful-gnu-592.convex.cloud`). Al construir `./dist`, la variable `ORBE_CONVEX_URL` inyecta la URL HTTPS en `dist/orbe-config.js` y `dist/plataforma/config.js` sin almacenar llaves privadas ni contraseñas en el repositorio.
2. **Aislamiento multi-tenant y control de acceso (RBAC):**
   - `superadmin` administra organizaciones, altas de tours, usuarios y bitácora global, manteniendo bloqueo explícito en backend (`userCanEditTour`) para alterar contenido de tours de clientes.
   - `orgAdmin` administra tours, marca `TourBranding` (bloqueando acentos propios de plataforma), publicación tras validar checklist WCAG y métricas/bitácora de su organización.
   - `tourEditor` edita escenas, hotspots, conexiones y multimedia en Control Web sin acceso a branding ni publicación.
   - Las sedes en preparación (`sede-1`, `sede-3`, `sede-4`, con `published: false`) permanecen ocultas en consultas públicas (`graph:getTourGraph` y `graph:listPublishedDemos`).
3. **Endurecimiento en producción:**
   - Contraseñas cifradas con **PBKDF2-SHA256** + *salt* aleatorio por cuenta; sesiones revocables y límite de intentos fallidos en `loginAttempts`.
   - `ALLOW_OPEN_SEED` y `SEED_BOOTSTRAP_SECRET` eliminados del entorno productivo (`prod`); las credenciales operativas iniciales se resguardan fuera de Git en `backups/CREDENCIALES_PROD_NO_SUBIR.txt` (gitignored).
4. **Distribución multimedia (`Cloudflare Pages` + `Convex File Storage`):**
   - Los panoramas equirectangulares y paquetes de audio base (`> 395 MB` en `media/`) se sirven desde Cloudflare Pages excluidos de Workers mediante `dist/_routes.json`, aprovechando ancho de banda gratuito ilimitado (`<= 25 MiB` por archivo).
   - Las cargas interactivas posteriores desde Control Web utilizan **Convex File Storage** con claves aisladas por organización y tour (`orgs/{orgId}/tours/{tourId}/...`).

---

## 3. Despliegue Local en Desarrollo (Cualquier Equipo)

Requisitos previos: **Node.js 20 LTS o superior** y **Git** (Windows, macOS o Linux).

### 3.1 Arranque paso a paso (Windows / macOS / Linux)

1. **Clonar e instalar dependencias:**
   ```bash
   git clone https://github.com/KUTEIMO/prototipo-360-v1-tested.git ORBE360
   cd ORBE360
   npm install
   ```

2. **Terminal 1 — Levantar backend Convex local:**
   ```bash
   npx convex dev
   ```
   > En la primera ejecución en un computador nuevo, Convex CLI te permite iniciar sesión o usar despliegue local (`http://127.0.0.1:3210` escrito en `.env.local`, excluido de Git). Usa siempre `npx convex dev` en desarrollo y nunca `deploy` sobre trabajo diario.

3. **Solo la primera vez (BD local vacía) — Sembrar organizaciones, Sandbox y las 88 escenas + audios:**
   ```bash
   npx convex env set ALLOW_OPEN_SEED 1
   npx convex env set SEED_SUPERADMIN_PASSWORD "OrbeSuper2026!"
   npx convex env set SEED_ORGADMIN_PASSWORD "UnisimonAdmin2026!"
   npm run seed
   npm run seed:orbe-sandbox
   npm run sync:fotitos
   ```
   *(Puedes definir cualquier contraseña local de mínimo 10 caracteres; si cambias las contraseñas de desarrollo, pásalas como `ORBE_SUPER_PASS` / `ORBE_UNI_PASS` al ejecutar `npm run sync:fotitos`.)*

4. **Terminal 2 — Levantar servidor web con routing virtual multi-tenant:**
   ```bash
   npm start
   ```
   Abre **`http://127.0.0.1:8081/`** (o `http://localhost:8081/`).

### 3.2 Inicio rápido en Windows y opciones de red

- **Doble clic en [`INICIAR_PROYECTO.bat`](INICIAR_PROYECTO.bat):** comprueba Node.js, instala `node_modules/` automáticamente si falta, levanta `npx convex dev` si el puerto `3210` no responde, abre el navegador y arranca `scripts/dev-server.mjs`.
- **Probar desde otro equipo o celular en tu red Wi-Fi (LAN):**
  ```powershell
  $env:HOST = "0.0.0.0"; npm start
  ```
- **Conectar el frontend local a otro backend Convex:** copia `config.local.js.example` a `config.local.js` (gitignored) o define `localStorage.setItem("orbe360.convexUrl", "https://tu-instancia.convex.cloud")` en la consola de desarrollo.

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

## 4. Despliegue a Producción en la Nube (Cualquier Equipo / Cuenta)

Guía detallada en [deploy/README.md](deploy/README.md) y [docs/producto/67-plan-despliegue-seguro-produccion.md](docs/producto/67-plan-despliegue-seguro-produccion.md).

1. **Desplegar funciones y esquema en Convex Cloud:**
   ```bash
   npx convex deploy
   ```
   Verifica que `ALLOW_OPEN_SEED` no esté habilitado en `--prod` (`npx convex env list --names-only --prod`).

2. **Generar paquete estático sanitizado `./dist`:**
   ```powershell
   # En PowerShell (en Bash: ORBE_CONVEX_URL="https://careful-gnu-592.convex.cloud" npm run build:prod)
   $env:ORBE_CONVEX_URL = "https://careful-gnu-592.convex.cloud"
   npm run build:prod
   ```

3. **Publicar en Cloudflare Pages (o Firebase Hosting):**
   ```bash
   npx wrangler login
   npx wrangler pages deploy dist --project-name=orbe360-unisimon --branch=main
   ```
   *(También incluye `dist/firebase.json` como alternativa para `firebase deploy --only hosting --config dist/firebase.json`.)*

---

## 5. Accesibilidad (WCAG 2.1 AA), Seguridad y Auditoría

- **Accesibilidad:** narración de audio con voz neural colombiana (**Salomé `es-CO-SalomeNeural`**), subtítulos **WebVTT**, transcripción descargable `.txt`, región `aria-live`, matriz dinámica `#wcagAuditDialog`, cálculo automático de contraste (`contrastInkForHex`), navegación completa por teclado (`Tab`, `Esc`, flechas SVG) y modo embebido `?embed=1`.
- **Seguridad:** validación de URLs (`urlSafety.ts`), protección anti-*open-redirect* y *cross-org* en login, bloqueo de rutas sensibles en `dev-server.mjs` y `functions/[[path]].js`, y cabeceras `X-Content-Type-Options: nosniff`, `X-Frame-Options: SAMEORIGIN`, `Referrer-Policy` y `Permissions-Policy`.

| Comando | Cobertura |
| :--- | :--- |
| `npm run check:static` | ESLint (`eslint .`) + Typecheck de Convex (`tsc -p convex/tsconfig.json --noEmit`). |
| `npm run audit:routes` | Verificación de rutas y enlaces internos en código y Markdown. |
| `npm run check:a11y` | Completitud de audiodescripciones, VTT, transcripciones y archivos `.mp3`. |
| `npm run test:unit` | Pruebas unitarias Node (slugs, contraste WCAG, VTT, grafo espacial, checklist). |
| `npm run qa:authz` | Aislamiento RBAC (`superadmin`, `orgAdmin`, `tourEditor`, anónimo). |
| `npm run qa` | Pruebas de contrato backend, branding, snapshot, storage y rate-limit. |
| `npm test` | Suite E2E completa en Chromium con Playwright (`tests/`). |

---

## 6. Estructura y Documentación Técnica

- `plataforma/`: portal web B2B (`index.html`), login, `org-admin.html`, `superadmin.html`, accesibilidad y páginas legales.
- `index.html` + `src/` + `css/` + `vendors/`: visor 360° WebGL desacoplado de identidad cliente.
- `control-web/`: editor espacial visual autenticado.
- `convex/`: esquema y funciones servidor en TypeScript.
- `functions/` + `deploy/`: enrutador multi-tenant Cloudflare Pages Functions y guías de despliegue.
- `media/`: panoramas 360° y activos accesibles aislados por cliente/tour (`/{org}/{tour}/`).
- `docs/`: índice arquitectónico y funcional completo en [docs/README.md](docs/README.md).

---

### Créditos y Delimitación de Repositorios
- **Equipo:** Eduardo José Soto Herrera, Saraic Noemí León Hernández, Kevin Eduardo García Moreno, Sebastián David Omaña Villamizar y Jesús Omar Avendaño Avendaño.
- **Separación de repositorios:** Este repositorio (`prototipo-360-v1-tested`) consolida la versión final completa de ingeniería y despliegue de **Orbe360** aprovechando su documentación técnica de arquitectura, accesibilidad y QA. La versión académica específica de gestión y entregables universitarios se mantiene por separado en [`ORBE-GP`](https://github.com/KUTEIMO/ORBE-GP).
