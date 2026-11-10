import os

GP_DIR = r"c:\Users\SOTO\APLICATIVOS\proyectos unisimon\ORBE-GP"
JS_PATH = os.path.join(GP_DIR, "plataforma", "marketing-motion.js")

with open(JS_PATH, "r", encoding="utf-8") as f:
    js = f.read()

# 1. Actualizar manejo de tema para escuchar preferencias del sistema/PC
old_theme_block = """/* == Theme == */
function getPreferredTheme() {
  const stored = localStorage.getItem(THEME_KEY);
  if (stored === "light" || stored === "dark") return stored;
  return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
}

function applyTheme(theme) {
  document.documentElement.setAttribute("data-theme", theme);
  localStorage.setItem(THEME_KEY, theme);
  const btn = document.getElementById("themeToggle");
  if (btn) {
    btn.setAttribute("aria-pressed", theme === "dark" ? "true" : "false");
    const lang = getLang();
    const label =
      theme === "dark"
        ? document.documentElement.lang === "en"
          ? "Switch to light mode"
          : "Activar modo claro"
        : document.documentElement.lang === "en"
          ? "Switch to dark mode"
          : "Activar modo oscuro";
    btn.setAttribute("aria-label", label);
  }
}

function initTheme() {
  applyTheme(getPreferredTheme());
  const btn = document.getElementById("themeToggle");
  if (btn) {
    btn.addEventListener("click", () => {
      const current = document.documentElement.getAttribute("data-theme") || "light";
      applyTheme(current === "dark" ? "light" : "dark");
      applyI18n();
    });
  }
}"""

new_theme_block = """/* == Theme with OS/Browser Preference Auto-Sync == */
const sysDarkQuery = window.matchMedia("(prefers-color-scheme: dark)");

function getPreferredTheme() {
  const stored = localStorage.getItem(THEME_KEY);
  if (stored === "light" || stored === "dark") return stored;
  return sysDarkQuery.matches ? "dark" : "light";
}

function applyTheme(theme, save = true) {
  document.documentElement.setAttribute("data-theme", theme);
  if (save) {
    localStorage.setItem(THEME_KEY, theme);
  }
  const btn = document.getElementById("themeToggle");
  if (btn) {
    btn.setAttribute("aria-pressed", theme === "dark" ? "true" : "false");
    const lang = getLang();
    const label =
      theme === "dark"
        ? document.documentElement.lang === "en"
          ? "Switch to light mode"
          : "Activar modo claro"
        : document.documentElement.lang === "en"
          ? "Switch to dark mode"
          : "Activar modo oscuro";
    btn.setAttribute("aria-label", label);
  }
}

function initTheme() {
  applyTheme(getPreferredTheme(), false);
  
  // Escuchar cambios de preferencia del sistema operativo en tiempo real
  sysDarkQuery.addEventListener("change", (e) => {
    // Si el usuario no ha forzado manualmente en esta sesion, o cambia el sistema
    applyTheme(e.matches ? "dark" : "light", false);
  });

  const btn = document.getElementById("themeToggle");
  if (btn) {
    btn.addEventListener("click", () => {
      const current = document.documentElement.getAttribute("data-theme") || "light";
      applyTheme(current === "dark" ? "light" : "dark", true);
      applyI18n();
    });
  }
}"""

if "/* == Theme == */" in js or "getPreferredTheme()" in js:
    import re
    js = re.sub(r'/\* == Theme == \*/.*?function initTheme\(\)\s*\{.*?\}\s*\}', new_theme_block, js, flags=re.DOTALL)
    print("Logica de tema actualizada con soporte OS en tiempo real.")

# 2. Agregar controlador de Acordeon Dinamico y Canvas 3D al final de marketing-motion.js
additional_modules = """
/* == Dynamic Interactive Sedes Accordion == */
function initSedesAccordion() {
  const accordion = document.querySelector(".sedes-accordion");
  if (!accordion) return;
  const cards = accordion.querySelectorAll(".sede-card");
  if (!cards.length) return;

  let hoverTimer = null;

  function activateCard(card) {
    cards.forEach((c) => c.classList.remove("is-active"));
    card.classList.add("is-active");
    accordion.classList.add("has-interaction");
  }

  // Activar la primera tarjeta por defecto
  if (!accordion.querySelector(".sede-card.is-active")) {
    activateCard(cards[0]);
  }

  cards.forEach((card) => {
    card.addEventListener("mouseenter", () => {
      clearTimeout(hoverTimer);
      // Suave retardo de 85ms: elimina la hipersensibilidad al pasar el cursor rapido
      hoverTimer = setTimeout(() => {
        activateCard(card);
      }, 85);
    });

    card.addEventListener("mouseleave", () => {
      clearTimeout(hoverTimer);
    });

    card.addEventListener("click", (e) => {
      // En desktop, si la tarjeta no esta activa, el primer click la expande
      if (window.innerWidth >= 900 && !card.classList.contains("is-active")) {
        e.preventDefault();
        activateCard(card);
      }
    });
  });

  // Al salir del acordeon, se mantiene abierta la ultima seleccionada
  accordion.addEventListener("mouseleave", () => {
    clearTimeout(hoverTimer);
  });
}

/* == Ambient 3D Motion Canvas ("Como un pez en el agua" & 3D Spatial Geometry) == */
function initAmbient3D() {
  const canvas = document.getElementById("ambient3dCanvas");
  if (!canvas || reduceMotion) return;
  const ctx = canvas.getContext("2d");
  if (!ctx) return;

  let width = 0;
  let height = 0;
  let animationFrameId = null;

  function resize() {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
  }
  window.addEventListener("resize", resize, { passive: true });
  resize();

  // Orbes organicos que nadan suavemente de lado a lado
  const orbs = [
    {
      baseX: 0.22,
      baseY: 0.18,
      radius: 190,
      hue: 202,
      sat: 92,
      light: 48,
      speedX: 0.00075,
      speedY: 0.00055,
      amplitudeX: 135,
      amplitudeY: 55,
      phase: 0
    },
    {
      baseX: 0.78,
      baseY: 0.42,
      radius: 230,
      hue: 216,
      sat: 88,
      light: 44,
      speedX: 0.00062,
      speedY: 0.00072,
      amplitudeX: 155,
      amplitudeY: 75,
      phase: Math.PI * 0.65
    },
    {
      baseX: 0.32,
      baseY: 0.78,
      radius: 175,
      hue: 192,
      sat: 96,
      light: 52,
      speedX: 0.00085,
      speedY: 0.00065,
      amplitudeX: 125,
      amplitudeY: 65,
      phase: Math.PI * 1.25
    }
  ];

  // Geometria 3D espacial (anillo toroidal wireframe con perspectiva)
  const ringPoints = [];
  const ringSegments = 32;
  const ringRadius = 140;
  for (let i = 0; i < ringSegments; i++) {
    const theta = (i / ringSegments) * Math.PI * 2;
    ringPoints.push({
      x: Math.cos(theta) * ringRadius,
      y: Math.sin(theta) * ringRadius,
      z: Math.sin(theta * 2) * 38
    });
  }

  let mouseX = 0;
  let mouseY = 0;
  let targetMouseX = 0;
  let targetMouseY = 0;

  window.addEventListener(
    "mousemove",
    (e) => {
      targetMouseX = (e.clientX / window.innerWidth - 0.5) * 50;
      targetMouseY = (e.clientY / window.innerHeight - 0.5) * 50;
    },
    { passive: true }
  );

  function render(time) {
    const now = time || 0;
    ctx.clearRect(0, 0, width, height);

    const isDark = document.documentElement.getAttribute("data-theme") === "dark";
    const maxScroll = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
    const scrollProgress = window.scrollY / maxScroll;

    // Amortiguacion suave del cursor
    mouseX += (targetMouseX - mouseX) * 0.04;
    mouseY += (targetMouseY - mouseY) * 0.04;

    // 1. Orbes Organicos Flotantes (Movimiento ondulatorio sinusoidal tipo pez)
    orbs.forEach((orb, i) => {
      const swimX = Math.sin(now * orb.speedX + orb.phase) * orb.amplitudeX + Math.cos(now * 0.0004) * 20;
      const swimY = Math.cos(now * orb.speedY + orb.phase) * orb.amplitudeY + Math.sin(now * 0.0003) * 15;
      const scrollDriftY = scrollProgress * height * 0.3 * (i % 2 === 0 ? 1 : -0.7);

      const currentX = orb.baseX * width + swimX + mouseX * (0.8 + i * 0.15);
      const currentY = orb.baseY * height + swimY + scrollDriftY + mouseY * (0.8 + i * 0.15);

      const gradient = ctx.createRadialGradient(
        currentX - orb.radius * 0.22,
        currentY - orb.radius * 0.22,
        orb.radius * 0.06,
        currentX,
        currentY,
        orb.radius
      );

      const alpha = isDark ? 0.34 : 0.17;
      gradient.addColorStop(0, `hsla(${orb.hue}, ${orb.sat}%, ${orb.light}%, ${alpha * 1.5})`);
      gradient.addColorStop(0.55, `hsla(${orb.hue + 12}, ${orb.sat}%, ${orb.light}%, ${alpha * 0.75})`);
      gradient.addColorStop(1, `hsla(${orb.hue + 25}, ${orb.sat}%, ${orb.light}%, 0)`);

      ctx.save();
      ctx.fillStyle = gradient;
      ctx.beginPath();
      ctx.arc(currentX, currentY, orb.radius, 0, Math.PI * 2);
      ctx.fill();
      ctx.restore();
    });

    // 2. Anillo Geometrico Espacial 3D (Mobbin Spatial wireframe)
    const ringCenterY = height * 0.32 + (scrollProgress * height * 0.45) + Math.sin(now * 0.0008) * 30;
    const ringCenterX = width * 0.84 + Math.cos(now * 0.0006) * 40 + mouseX * 1.2;

    const rotX = now * 0.00055 + scrollProgress * Math.PI * 2;
    const rotY = now * 0.00075 + scrollProgress * Math.PI * 1.6;
    const rotZ = now * 0.00028;

    const fov = 420;
    const projected = ringPoints.map((pt) => {
      // Rotacion Y
      const x1 = pt.x * Math.cos(rotY) + pt.z * Math.sin(rotY);
      const z1 = -pt.x * Math.sin(rotY) + pt.z * Math.cos(rotY);
      // Rotacion X
      const y2 = pt.y * Math.cos(rotX) - z1 * Math.sin(rotX);
      const z2 = pt.y * Math.sin(rotX) + z1 * Math.cos(rotX);
      // Rotacion Z
      const x3 = x1 * Math.cos(rotZ) - y2 * Math.sin(rotZ);
      const y3 = x1 * Math.sin(rotZ) + y2 * Math.cos(rotZ);

      const scale = fov / (fov + z2 + 200);
      return {
        x: ringCenterX + x3 * scale,
        y: ringCenterY + y3 * scale,
        scale: scale,
        z: z2
      };
    });

    ctx.save();
    ctx.lineWidth = isDark ? 1.4 : 1.1;
    ctx.strokeStyle = isDark
      ? `rgba(56, 189, 248, ${0.28 + Math.sin(now * 0.001) * 0.08})`
      : `rgba(2, 132, 199, ${0.20 + Math.sin(now * 0.001) * 0.06})`;

    ctx.beginPath();
    for (let i = 0; i < projected.length; i++) {
      const p = projected[i];
      if (i === 0) ctx.moveTo(p.x, p.y);
      else ctx.lineTo(p.x, p.y);
    }
    ctx.closePath();
    ctx.stroke();

    // Vertices brillantes sutiles
    projected.forEach((p, idx) => {
      if (idx % 2 === 0) {
        ctx.fillStyle = isDark ? "rgba(56, 189, 248, 0.42)" : "rgba(2, 132, 199, 0.32)";
        ctx.beginPath();
        ctx.arc(p.x, p.y, 2.2 * p.scale, 0, Math.PI * 2);
        ctx.fill();
      }
    });
    ctx.restore();

    if (!document.hidden) {
      animationFrameId = requestAnimationFrame(render);
    }
  }

  document.addEventListener("visibilitychange", () => {
    if (!document.hidden) {
      cancelAnimationFrame(animationFrameId);
      animationFrameId = requestAnimationFrame(render);
    }
  });

  animationFrameId = requestAnimationFrame(render);
}

// Inicializar nuevos modulos
initSedesAccordion();
initAmbient3D();
"""

if "initSedesAccordion()" not in js:
    js = js + "\n" + additional_modules
    print("Modulos initSedesAccordion e initAmbient3D agregados al final de marketing-motion.js.")

with open(JS_PATH, "w", encoding="utf-8") as f:
    f.write(js)

print("marketing-motion.js actualizado exitosamente.")
