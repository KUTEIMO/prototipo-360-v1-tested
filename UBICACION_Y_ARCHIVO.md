# Ubicación y archivo — ORBE (producto Orbe360)

**Fecha de consolidación:** 2026-09-16  
**Marca de producto:** Orbe360  
**Carpeta canónica:** `ORBE` (nombre del hogar SaaS en docs/repo; la marca UI es Orbe360)

---

## Ruta oficial (producto avanzado / SaaS)

`C:\Users\SOTO\APLICATIVOS\proyectos unisimon\ORBE`

Esta es la **versión de producto avanzada**: plataforma multi-tenant de tours 360° inclusivos (white-label), con Convex, Control Web, branding, authz y piloto UniSimón Cúcuta. Se desarrolla **más allá del alcance académico** con intención de publicar.

Runtime típico:

```bash
cd "C:\Users\SOTO\APLICATIVOS\proyectos unisimon\ORBE"
npx convex dev    # terminal 1
npm start         # terminal 2 → http://127.0.0.1:8081/
```

Stack: web estático + Convex (local hoy; cloud opcional con `npx convex login`). Deploy hosting público multi-tenant: **aún no** (docs: migration-ready / portable).

---

## NO confundir con el prototipo de curso

| Rol | Path |
|-----|------|
| **Producto SaaS (este repo)** | `C:\Users\SOTO\APLICATIVOS\proyectos unisimon\ORBE` |
| **Prototipo / curso (madurez menor)** | `C:\Users\SOTO\Documents\ED\simon\2026 2\gestion de proyectos\PROTOTIPO-360-CURSOR-V1` |

`PROTOTIPO-360-CURSOR-V1` en Documents es la copia de **gestión de proyectos / Cursor V1 / entrega académica**. Misma familia técnica, **madurez distinta**: no es el hogar de desarrollo del SaaS. **No sustituye** a ORBE.

Repo histórico de tip: https://github.com/KUTEIMO/prototipo-360-v1-tested

Mapa curso ↔ producto: `docs/producto/58-curso-vs-orbe-aplicativos.md` · filosofía: `docs/producto/57-orbe-saas-home-aplicativos.md`.

---

## Dónde estaba y por qué hay archivo

| Ubicación | Rol |
|-----------|-----|
| Antes: `EXTRAS\repos\ORBE` | Hogar SaaS previo a la reorg APLICATIVOS |
| Archivo (stub tras reunir): `C:\Users\SOTO\APLICATIVOS\_archivo_duplicados\unisimon\20260916\ORBE` | Marcador: el árbol completo se **movió** a la ruta oficial UniSimón (no se borró el contenido; se reunificó) |
| Restos de locks: `ORBE\_restos_exras_bloqueados\` | `.convex` / `node_modules` parciales que quedaron bloqueados en EXTRAS; reunidos aquí tras cerrar Convex/esbuild |
| Puntero EXTRAS: `EXTRAS\repos\ORBE` | Solo documentación de redirección |

Backups de sqlite local (misma sesión ~55 MB):

- Activo: `.convex\local\default\convex_local_backend.sqlite3` (sesión EXTRAS más reciente)
- `….sqlite3.from-archive-move-20260916`
- `….sqlite3.from-extras-restos-20260916`

---

## Advertencia

- **No borrar** `_archivo_duplicados` ni los backups sqlite hasta verificación manual.
- **No borrar** la carpeta del curso en Documents.
- Tras abrir en la ruta nueva: `npm install` si hace falta y `npx convex dev` para re-vincular.
