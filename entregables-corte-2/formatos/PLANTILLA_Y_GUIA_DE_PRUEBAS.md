# Plantilla y Guía Metodológica de Pruebas de Software — Orbe360

> **Asignatura:** Gestión de Proyectos — 2026-2 (UniSimón Cúcuta)  
> **Docente:** Ing. Nataly  
> **Proyecto:** Orbe360 (Recorrido Virtual e Inclusión 360°)  
> **Referencia Académica:** Entrega Oficial en 3er Corte (Con avance estratégico en 2do Corte)

---

## 1. Estructura General del Plan de Pruebas

Siguiendo las directrices de la docente, el sistema de pruebas se compone de dos niveles:
1. **Acta General de Pruebas (Única):** Documento formal de inicio, alcance, entorno y aprobación general del plan de pruebas. Se diligencia **una sola vez**.
2. **Fichas de Pruebas por Funcionalidad (Extensas):** Se aplican a cada requerimiento/módulo del software, desglosando:
   - **Pruebas de Aceptación:** Validación de usuario y criterios de satisfacción.
   - **Pruebas de Caja Negra:** Validación de entradas, salidas, interfaces y límites sin inspeccionar el código interno.
   - **Pruebas de Caja Blanca:** Validación de caminos de ejecución, lógica interna, manejo de excepciones y ramas condicionales.
   - **Pruebas Unitarias / Automatizadas:** Scripts ejecutables en código fuente (JavaScript / Playwright / Node.js).

---

## 2. Formato 1: Acta General de Pruebas de Software (Se hace 1 sola vez)

| ACTA GENERAL DE CONTROL Y APROBACIÓN DE PRUEBAS | CÓDIGO: ACT-PRU-01 |
| :--- | :--- |
| **Nombre del Proyecto:** Orbe360 | **Versión del Software:** 1.0-RC |
| **Líder de Desarrollo:** Eduardo José Soto Herrera | **Fecha de Elaboración:** Octubre 2026 |
| **Objetivo General:** Garantizar la calidad, estabilidad y accesibilidad del software antes del despliegue final. |

### 2.1 Entorno de Pruebas
* **Sistemas Operativos:** Windows 11 / Linux Ubuntu / Android 13+ / iOS 17+.
* **Navegadores Homologados:** Google Chrome (v120+), Mozilla Firefox (v122+), Safari (v17+).
* **Herramientas de Soporte:** Playwright Test Runner, NVDA Screen Reader, DevTools Lighthouse.
* **Base de Datos / Backend:** Convex Cloud Backend / Local SQLite Graph.

### 2.2 Tipología de Pruebas Aplicadas
- [x] Pruebas Unitarias en código fuente.
- [x] Pruebas de Integración y End-to-End (E2E).
- [x] Pruebas de Caja Negra (Funcionales y de Interfaz).
- [x] Pruebas de Caja Blanca (Cobertura de lógica y seguridad).
- [x] Pruebas de Aceptación y Accesibilidad Universal (WCAG 2.1 AA).

### 2.3 Firmas de Aprobación
| Rol | Nombre | Firma | Fecha |
| :--- | :--- | :--- | :--- |
| **Líder QA / Pruebas** | Equipo QA Orbe360 | __________________ | __/__/2026 |
| **Líder de Proyecto** | Eduardo José Soto Herrera | __________________ | __/__/2026 |
| **Docente Evaluador** | Ing. Nataly | __________________ | __/__/2026 |

---

## 3. Formato 2: Ficha Técnica de Pruebas por Funcionalidad

> *Este formato se replica por cada módulo/ticket del software.*

```text
================================================================================
FICHA DE PRUEBA FUNCIONAL: [CÓDIGO_TICKET - NOMBRE_FUNCIONALIDAD]
================================================================================
Módulo: [Nombre del Módulo / Épica]
Objetivo: [Qué valida esta prueba]
Precondiciones: [Estado previo requerido del sistema y del usuario]
Tipo de Prueba: [Caja Negra / Caja Blanca / Aceptación / Unitaria]
================================================================================
```

### Tabla de Casos de Prueba:

| ID Caso | Escenario / Descripción | Datos de Entrada | Resultado Esperado | Resultado Obtenido | Estado (Pasa / Falla) | Severidad |
| :---: | :--- | :--- | :--- | :--- | :---: | :---: |
| **CP-01** | *[Acción a evaluar]* | *[Valores enviados]* | *[Respuesta esperada]* | *[Comportamiento real]* | ✅ Pasa / ❌ Falla | Alta / Media / Baja |

---

## 4. Ejemplo Real Diligenciado (Para Presentar a la Docente)

A continuación se presenta un caso modelo completamente diligenciado para el módulo core del proyecto:

### Ficha: `PRU-KAN-18` — Recorrido Virtual 360° y Transición de Escenas
* **Módulo:** Motor y Experiencia 360° (Épica 1)
* **Ticket Jira:** [`KAN-18`](https://orbe-experience360.atlassian.net/browse/KAN-18)
* **Precondición:** Servidor web activo (`npm start`), usuario situado en la escena de bienvenida.

#### A. Pruebas de Caja Negra (Funcionalidad Externa e Interfaz)
| ID Caso | Escenario | Datos de Entrada | Resultado Esperado | Resultado Real | Estado |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **CN-18.1** | Carga panorámica inicial | URL `http://127.0.0.1:8081/` | El lienzo WebGL renderiza la imagen equirectangular a 60 FPS sin artefactos. | Renderizado fluido verificado en Chrome/Firefox. | ✅ PASA |
| **CN-18.2** | Interacción con Hotspot | Clic sobre el icono de puerta hacia "Biblioteca" | La cámara rota suavemente y carga la siguiente escena sin recargar la página (`SPA`). | Transición animada correcta con retención de pitch/yaw. | ✅ PASA |
| **CN-18.3** | Giroscopio en dispositivo móvil | Orientación del dispositivo (inclinación física) | La panorámica ajusta su ángulo en tiempo real según el sensor. | Activación exitosa de eventos `DeviceOrientation`. | ✅ PASA |

#### B. Pruebas de Caja Blanca (Lógica Interna y Rutas de Código)
| ID Caso | Flujo Interno / Rama | Condición Evaluada | Comportamiento del Código | Estado |
| :---: | :--- | :--- | :--- | :---: |
| **CB-18.1** | Validación de URL de escena | `if (!scene.imageUrl) throw Error` | Lanza fallback a `placeholder.jpg` y registra advertencia en consola en lugar de congelar el navegador. | ✅ PASA |
| **CB-18.2** | Aislamiento de memoria WebGL | Cambio repetido de 10 escenas consecutivas | El motor invoca `dispose()` sobre texturas previas; no se detectan fugas de memoria en Heap Snapshot. | ✅ PASA |

#### C. Pruebas de Aceptación (Criterios de Usuario & Accesibilidad)
| ID Caso | Criterio de Aceptación | Prueba Ejecutada | Veredicto Usuario |
| :---: | :--- | :--- | :---: |
| **AC-18.1** | El usuario puede recorrer el campus sin requerir mouse | Navegación 100% mediante teclas `Tab`, `Enter`, `Flechas` y accesos rápidos `1..9`. | ✅ CUMPLE |
| **AC-18.2** | Usuario con baja visión puede ubicar los accesos | Los hotspots poseen un ratio de contraste mínimo de 4.8:1 frente al fondo. | ✅ CUMPLE |

#### D. Pruebas Unitarias / Automatizadas en Código
* **Archivo de prueba:** `tests/tour-e2e.spec.js` (Ejecutable con Playwright)
* **Comando de ejecución:** `npx playwright test tests/tour-e2e.spec.js`
* **Fragmento de código de prueba:**
  ```javascript
  import { test, expect } from '@playwright/test';

  test('El visor 360 carga la escena y contiene hotspots accesibles', async ({ page }) => {
    await page.goto('http://127.0.0.1:8081/');
    const viewer = page.locator('#panorama-container');
    await expect(viewer).toBeVisible();

    const hotspots = page.locator('.pnlm-hotspot');
    const count = await hotspots.count();
    expect(count).toBeGreaterThan(0);

    // Verificar accesibilidad de botones
    const firstHotspot = hotspots.first();
    await expect(firstHotspot).toHaveAttribute('aria-label');
  });
  ```
* **Resultado de consola:** `1 passed (1.8s) - 0 errors`.
