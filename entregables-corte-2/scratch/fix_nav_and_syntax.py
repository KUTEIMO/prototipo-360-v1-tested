import os

GP_DIR = r"c:\Users\SOTO\APLICATIVOS\proyectos unisimon\ORBE-GP"
CSS_PATH = os.path.join(GP_DIR, "plataforma", "marketing.css")
HTML_PATH = os.path.join(GP_DIR, "plataforma", "index.html")

# 1. FIX SYNTAX ERROR IN index.html
with open(HTML_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# Wrap script in async IIFE
old_script = """  <script type="module">
    import { apiQuery } from "/plataforma/convex-client.js";
    import { publicTourHref, DEFAULT_TOUR_SLUG, DEFAULT_ORG_SLUG } from "/src/tourSlug.js";

    function escapeHtml(s) {
      return String(s)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;");
    }

    try {
      const demos = await apiQuery("graph:listPublishedDemos", {});
      if (!Array.isArray(demos) || demos.length === 0) return;"""

new_script = """  <script type="module">
    import { apiQuery } from "/plataforma/convex-client.js";
    import { publicTourHref, DEFAULT_TOUR_SLUG, DEFAULT_ORG_SLUG } from "/src/tourSlug.js";

    function escapeHtml(s) {
      return String(s)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;");
    }

    (async function initPublishedDemos() {
      try {
        const demos = await apiQuery("graph:listPublishedDemos", {});
        if (!Array.isArray(demos) || demos.length === 0) return;"""

if old_script in html:
    html = html.replace(old_script, new_script)
    # Also close the async IIFE before </script>
    # find where this script ends
    idx = html.find("initPublishedDemos()")
    close_idx = html.find("</script>", idx)
    html = html[:close_idx] + "\n    })();\n  " + html[close_idx:]
    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(html)
    print("Sintaxis de index.html reparada (envuelta en async IIFE).")
else:
    print("Bloque viejo de script no encontrado exactamente.")

# 2. FIX CSS IN marketing.css
with open(CSS_PATH, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_nav_css = """
/* ==========================================================================
   PUBLIC NAVIGATION - THEME ADAPTIVE & FROSTED GLASS
   ========================================================================== */
.public-nav {
  position: fixed;
  inset: 0 0 auto;
  z-index: 50;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem 1.25rem;
  padding: 0.85rem clamp(1rem, 3.5vw, 2.5rem);
  background: rgba(255, 255, 255, 0.82);
  border-bottom: 1px solid rgba(226, 232, 240, 0.9);
  backdrop-filter: blur(20px) saturate(160%);
  -webkit-backdrop-filter: blur(20px) saturate(160%);
  box-shadow: 0 4px 20px -2px rgba(15, 23, 42, 0.04);
  transition:
    background 300ms ease,
    border-color 300ms ease,
    box-shadow 300ms ease,
    padding 300ms ease;
}

[data-theme="dark"] .public-nav {
  background: rgba(11, 18, 32, 0.82);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  box-shadow: 0 4px 25px rgba(0, 0, 0, 0.4);
}

.public-nav.is-scrolled {
  background: rgba(255, 255, 255, 0.95);
  border-bottom-color: var(--orbe-line);
  box-shadow: 0 10px 25px -4px rgba(15, 23, 42, 0.08);
  padding-top: 0.65rem;
  padding-bottom: 0.65rem;
}

[data-theme="dark"] .public-nav.is-scrolled {
  background: rgba(11, 18, 32, 0.95);
  border-bottom-color: rgba(255, 255, 255, 0.1);
  box-shadow: 0 10px 35px rgba(0, 0, 0, 0.6);
}

.brand {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-family: var(--mk-display);
  font-weight: 700;
  font-size: 1.15rem;
  letter-spacing: 0.06em;
  color: var(--orbe-ink);
  text-decoration: none;
  transition: color 200ms ease;
}

[data-theme="dark"] .brand {
  color: #ffffff;
}

.brand span {
  color: var(--orbe-accent);
}

[data-theme="dark"] .brand span {
  color: var(--orbe-signal);
}

.brand__orb {
  width: 1.35rem;
  height: 1.35rem;
  border-radius: 50%;
  border: 2px solid currentColor;
  box-shadow: inset 0 0 0 3px transparent, 0 0 0 1px rgba(56, 189, 248, 0.4);
  background:
    radial-gradient(circle at 35% 32%, rgba(255, 255, 255, 0.85), transparent 40%),
    radial-gradient(circle at 50% 50%, var(--orbe-signal), var(--orbe-accent-deep));
  flex-shrink: 0;
}

.public-nav nav {
  display: flex;
  flex-wrap: wrap;
  gap: 0.35rem 1.25rem;
  align-items: center;
}

.public-nav nav a {
  color: var(--orbe-muted);
  text-decoration: none;
  font-weight: 500;
  font-size: 0.92rem;
  padding: 0.35rem 0.6rem;
  border-radius: 8px;
  transition: color 180ms ease, background 180ms ease;
  position: relative;
}

[data-theme="dark"] .public-nav nav a {
  color: rgba(255, 255, 255, 0.78);
}

.public-nav nav a:hover {
  color: var(--orbe-accent);
  background: rgba(2, 132, 199, 0.06);
}

[data-theme="dark"] .public-nav nav a:hover {
  color: #ffffff;
  background: rgba(255, 255, 255, 0.08);
}

.public-nav nav a.is-active {
  color: var(--orbe-accent);
  font-weight: 600;
}

[data-theme="dark"] .public-nav nav a.is-active {
  color: var(--orbe-signal);
}

.public-nav nav a.is-active::after {
  content: "";
  position: absolute;
  left: 0.6rem;
  right: 0.6rem;
  bottom: 0;
  height: 2px;
  background: var(--orbe-accent);
  border-radius: 2px;
}

[data-theme="dark"] .public-nav nav a.is-active::after {
  background: var(--orbe-signal);
}

.public-nav__tools {
  display: flex;
  align-items: center;
  gap: 0.55rem;
}

.icon-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 2.25rem;
  height: 2.25rem;
  padding: 0;
  border-radius: 9px;
  background: rgba(15, 23, 42, 0.04);
  border: 1px solid rgba(15, 23, 42, 0.12);
  color: var(--orbe-ink);
  font-weight: 700;
  font-size: 0.75rem;
  letter-spacing: 0.06em;
  cursor: pointer;
  font-family: inherit;
  transition: all 180ms ease;
}

[data-theme="dark"] .icon-btn {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.14);
  color: #ffffff;
}

.icon-btn:hover,
.icon-btn:focus-visible {
  border-color: var(--orbe-accent);
  color: var(--orbe-accent);
  background: rgba(2, 132, 199, 0.08);
  transform: translateY(-1px);
}

[data-theme="dark"] .icon-btn:hover,
[data-theme="dark"] .icon-btn:focus-visible {
  border-color: var(--orbe-signal);
  color: var(--orbe-signal);
  background: rgba(56, 189, 248, 0.12);
}

.icon-btn--theme .icon-moon { display: none; }
[data-theme="dark"] .icon-btn--theme .icon-sun { display: none; }
[data-theme="dark"] .icon-btn--theme .icon-moon { display: block; }

.btn--nav {
  padding: 0.5rem 1.15rem;
  font-size: 0.88rem;
  font-weight: 600;
  border-radius: 9px;
  background: var(--orbe-accent);
  color: #ffffff !important;
  border: 1px solid var(--orbe-accent);
  text-decoration: none;
  box-shadow: 0 2px 10px rgba(2, 132, 199, 0.25);
  transition: all 200ms ease;
}

.btn--nav:hover {
  background: var(--orbe-accent-deep);
  border-color: var(--orbe-accent-deep);
  box-shadow: 0 4px 14px rgba(2, 132, 199, 0.35);
  transform: translateY(-1px);
}
"""

# Reemplazar exactamente lineas 136 a 273 (0-indexed 135 a 273)
idx_start = -1
idx_end = -1
for i, l in enumerate(lines):
    if ".public-nav {" in l and idx_start == -1:
        idx_start = i - 1 # include comment line before
    if ".btn {" in l and idx_start != -1 and idx_end == -1:
        idx_end = i
        break

if idx_start != -1 and idx_end != -1:
    print(f"Reemplazando lineas {idx_start+1} a {idx_end} en marketing.css...")
    new_lines = lines[:idx_start] + [new_nav_css + "\n"] + lines[idx_end:]
    with open(CSS_PATH, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
    print("marketing.css actualizado con exito.")
else:
    print(f"Indices no encontrados: start={idx_start}, end={idx_end}")
