# MANUAL DE DESPLIEGUE Y EJECUCIÓN LOCAL — DOCENTE EVALUADORA
### PROYECTO ORBE360 (PEVCI) — EVALUACIÓN SEGUNDO CORTE (70% DESARROLLADO)

**Docente:** Ing. Nataly Duque Páez  
**Asignatura:** Gestión de Proyectos — Universidad Simón Bolívar (Sede Cúcuta)  

---

## 1. REQUISITOS DEL SISTEMA
* Sistema Operativo: Windows 10/11, macOS o Linux.
* Navegador web moderno: Google Chrome, Microsoft Edge, Mozilla Firefox o Safari.
* Node.js (versión 18.x o superior). *(Si su equipo no lo tiene, se incluye comando de auto-instalación).*

---

## 2. OPCIONES DE EJECUCIÓN RÁPIDA

### Opción A: Ejecución mediante Doble Clic (Método más simple)
1. Descomprima el archivo `ORBE-GP-Software-70.zip` en cualquier carpeta.
2. Haga doble clic sobre el archivo **`INICIAR_PROYECTO.bat`**.
3. El sistema verificará Node.js (instalándolo con winget si falta), abrirá el navegador en `http://localhost:8081/` y levantará el servidor automáticamente.

---

### Opción B: Si su PC NO tiene Git ni Node.js (1 Sola Línea en PowerShell)
Abra Windows PowerShell y pegue esta sola línea:
```powershell
winget install --id Git.Git -e --accept-package-agreements --accept-source-agreements; winget install --id OpenJS.NodeJS.LTS -e --accept-package-agreements --accept-source-agreements; $env:Path = "$([System.Environment]::GetEnvironmentVariable('Path','Machine'));$([System.Environment]::GetEnvironmentVariable('Path','User'))"; git clone https://github.com/KUTEIMO/ORBE-GP.git; cd ORBE-GP; Start-Process "http://localhost:8081/"; npm start
```

---

### Opción C: Clonación estándar desde GitHub (Si ya tiene Git y Node)
```powershell
git clone https://github.com/KUTEIMO/ORBE-GP.git; cd ORBE-GP; npm install; Start-Process "http://localhost:8081/"; npm start
```

---

## 3. RUTAS DE NAVEGACIÓN DISPONIBLES EN LOCAL
* **Portal y Landing Page Oficial:**  
  `http://localhost:8081/`
* **Recorrido Virtual 360° Piloto Unisimón (Biblioteca Anita Consuegra):**  
  `http://localhost:8081/unisimoncucuta/experienciavirtual/`
* **Panel de Control y Administración (CMS):**  
  `http://localhost:8081/unisimoncucuta/experienciavirtual/control-web/`

---

## 4. VERIFICACIÓN DE CARACTERÍSTICAS EVALUADAS (70% DE AVANCE)
1. **Navegación 360°:** Arrastrar el ratón o pantalla táctil para girar 360°. Clic en los hotspots para transitar entre los 18 recintos de la biblioteca.
2. **Audio Guía Espacial:** Presionar la tecla `M` para silenciar o activar la narración descriptiva del recinto en cualquier escena.
3. **Lengua de Señas Colombiana (LSC):** Presionar la combinación `Alt + S` o hacer clic en el botón flotante en la esquina inferior derecha.
4. **Navegación por Teclado:** Utilizar la tecla `Tab` y `Enter` para navegar sin necesidad de ratón, verificando el anillo de foco contrastado (WCAG 2.1 AA).
