# GUION DE SUSTENTACIÓN — SEBASTIÁN DAVID OMAÑA VILLAMIZAR
**Rol:** Ingeniero DevSecOps, Base de Datos Reactiva (Convex) & Automatización E2E

---

## TU MOMENTO DE HABLAR (ERES EL QUINTO)

* **En qué momento hablas:** Cuando Eduardo Soto termine de explicar el motor frontend 360° y te diga: *"Le doy paso a Sebastián Omaña para explicar la arquitectura de base de datos reactiva y DevSecOps"*.
* **Qué debe estar en pantalla:** Eduardo tiene en pantalla el **software Orbe360 en vivo** en el navegador.

---

## LO QUE DEBES DECIR

"Gracias, Eduardo. En la capa de infraestructura y backend elegimos **Convex**:

1. **Por qué Convex:** Es una base de datos reactiva de última generación que sincroniza datos en tiempo real mediante WebSockets nativos. Cuando una escena o hotspot se actualiza en el panel de administración, el visor en el cliente refleja el cambio al instante sin necesidad de refrescar la página ni configurar polling manual.
2. **Modelo de Grafos Conexo:** Diseñamos el esquema en `convex/schema.ts` donde cada recinto es un nodo y cada hotspot es una arista dirigida. Las mutaciones aplican la política de *in-place patch* para asegurar que si se actualiza el nombre de una escena, jamás se rompan las conexiones del recorrido.
3. **Seguridad y Control de Acceso (RBAC):** Blindamos las funciones de mutación (`userCanEditTour`): un Superadmin institucional tiene visibilidad global, pero tiene expresamente restringida la edición directa del contenido de los tours de un cliente para preservar la integridad de la autoría.
4. **DevSecOps y Calidad:** Contamos con el script `npm run check:drift` para asegurar que el repositorio local sea siempre la única fuente de verdad, y ejecutamos suites de pruebas E2E automatizadas con **Playwright** que validan la carga y navegación en menos de 2 segundos.

Doy paso a Saraic León para sustentar el núcleo de accesibilidad universal e inclusión."
