# Guía de despliegue en producción — Orbe360

Este directorio documenta la arquitectura recomendada para publicar Orbe360 en Internet mediante HTTPS real sin exponer archivos fuente, pruebas ni credenciales.

## Arquitectura recomendada

1. **Backend y Storage:** **Convex Cloud** (`npx convex deploy`)
   - Despliega las funciones `convex/*.ts` y el esquema multi-tenant.
   - Configura variables de entorno de producción en Convex Cloud:
     - `ALLOW_OPEN_SEED=0` (por defecto desactivado; no expongas seed abierto).
     - Opcional para bootstrap inicial: `SEED_SANDBOX_PASSWORD` fuerte.
2. **Frontend estático + Media (`/media/*`):** **Cloudflare Pages** (recomendado) o **Firebase Hosting**
   - El paquete estático generado por `npm run build:prod` coloca:
     - `dist/index.html` ← portal Orbe360 (`plataforma/index.html`)
     - `dist/viewer.html` ← visor 360° (`index.html`)
     - `dist/_redirects` y `dist/_headers` para Cloudflare Pages
     - `dist/firebase.json` para Firebase Hosting (rewrites `/:org/:tour/`, `/:org/org-admin.html`, `/:org/:tour/control-web/`)
   - Nota de ancho de banda: la carpeta `media/` actual supera los `275 MB` en panoramas; Cloudflare Pages ofrece ancho de banda ilimitado y hasta `25 MiB` por archivo, evitando agotar cuotas mensuales de transferencia en planes gratuitos como Spark (10 GB/mes).

## Pasos para generar e impulsar un despliegue real

1. Desplegar el backend en Convex Cloud:
   ```powershell
   npx convex deploy
   ```
   Anota la URL HTTPS asignada (ej. `https://tu-instancia.convex.cloud`).

2. Construir el paquete estático limpio inyectando la URL de Convex Cloud:
   ```powershell
   $env:ORBE_CONVEX_URL = "https://tu-instancia.convex.cloud"
   npm run build:prod
   ```
   El script excluye automáticamente `.env*`, `convex/`, `docs/`, `scripts/`, `backups/`, `tests/` y `entregables-*`.

3. Publicar `./dist`:
   - **Con Cloudflare Pages (Wrangler):**
     ```powershell
     npx wrangler pages deploy dist --project-name=orbe360
     ```
   - **Con Firebase Hosting:**
     ```powershell
     firebase deploy --only hosting --config dist/firebase.json
     ```

## Checklist previo a pasar URL pública

- [ ] Cambiar contraseñas de demo heredadas antes de habilitar usuarios externos (`auth:changePassword` o `auth:resetUserPassword`).
- [ ] Confirmar que `ALLOW_OPEN_SEED` no está en `"1"` en producción.
- [ ] Verificar `/`, `/{org}/{tour}/`, `/{org}/org-admin.html`, `/{org}/{tour}/control-web/` y respuesta `200` de imágenes en `/media/`.
- [ ] Probar `Esc` / modal de hotspots, branding del tour y subida de panoramas en Chrome.

