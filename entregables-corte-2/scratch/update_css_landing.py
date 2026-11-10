import os

GP_DIR = r"c:\Users\SOTO\APLICATIVOS\proyectos unisimon\ORBE-GP"
CSS_PATH = os.path.join(GP_DIR, "plataforma", "marketing.css")
JS_PATH = os.path.join(GP_DIR, "plataforma", "marketing-motion.js")

# 1. ACTUALIZAR MARKETING.CSS
with open(CSS_PATH, "r", encoding="utf-8") as f:
    css = f.read()

# Anadir soporte canvas en CSS
canvas_css = """
/* Ambient 3D Canvas Layer */
.story-bg__canvas {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 1;
}
"""
if ".story-bg__canvas" not in css:
    css = css + "\n" + canvas_css

# Reemplazar definicion de public-nav
nav_replacement = """/* Public Nav - Theme Adaptive & Glassmorphic */
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
  border-bottom: 1px solid rgba(226, 232, 240, 0.85);
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
  background: rgba(11, 18, 32, 0.85);
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

.public-nav .icon-btn {
  width: 2.25rem;
  height: 2.25rem;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 9px;
  background: rgba(15, 23, 42, 0.04);
  border: 1px solid rgba(15, 23, 42, 0.1);
  color: var(--orbe-ink);
  cursor: pointer;
  font-weight: 600;
  font-size: 0.8rem;
  transition: all 200ms ease;
}

[data-theme="dark"] .public-nav .icon-btn {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.12);
  color: #ffffff;
}

.public-nav .icon-btn:hover {
  border-color: var(--orbe-accent);
  color: var(--orbe-accent);
  background: rgba(2, 132, 199, 0.08);
}

[data-theme="dark"] .public-nav .icon-btn:hover {
  border-color: var(--orbe-signal);
  color: var(--orbe-signal);
  background: rgba(56, 189, 248, 0.12);
}

.public-nav .btn--nav {
  padding: 0.5rem 1.15rem;
  font-size: 0.88rem;
  font-weight: 600;
  border-radius: 9px;
  background: var(--orbe-accent);
  color: #ffffff;
  border: 1px solid var(--orbe-accent);
  text-decoration: none;
  box-shadow: 0 2px 10px rgba(2, 132, 199, 0.25);
  transition: all 200ms ease;
}

.public-nav .btn--nav:hover {
  background: var(--orbe-accent-deep);
  border-color: var(--orbe-accent-deep);
  box-shadow: 0 4px 14px rgba(2, 132, 199, 0.35);
  transform: translateY(-1px);
}
"""

# Reemplazar acordeon
accordion_replacement = """/* Dynamic Sedes Accordion */
.sedes-accordion {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

@media (min-width: 900px) {
  .sedes-accordion {
    flex-direction: row;
    height: 430px;
    align-items: stretch;
    gap: 1rem;
  }
}

.sede-card {
  display: flex;
  flex-direction: column;
  background: var(--orbe-clay-surface);
  border: 1px solid var(--orbe-line);
  border-radius: 18px;
  overflow: hidden;
  text-decoration: none;
  color: inherit;
  flex: 1;
  min-width: 0;
  transition:
    flex 0.65s cubic-bezier(0.16, 1, 0.3, 1),
    transform 0.35s cubic-bezier(0.16, 1, 0.3, 1),
    border-color 0.35s ease,
    box-shadow 0.35s ease,
    opacity 0.35s ease;
  position: relative;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04);
}

@media (min-width: 900px) {
  .sedes-accordion .sede-card {
    flex: 1;
    opacity: 0.85;
  }
  
  .sedes-accordion .sede-card.is-active {
    flex: 3.2;
    opacity: 1;
    border-color: var(--orbe-accent);
    box-shadow: 0 16px 36px -6px rgba(2, 132, 199, 0.16), 0 4px 12px rgba(0, 0, 0, 0.04);
    transform: translateY(-2px);
  }

  [data-theme="dark"] .sedes-accordion .sede-card.is-active {
    border-color: var(--orbe-signal);
    box-shadow: 0 16px 40px rgba(0, 0, 0, 0.5), 0 0 20px rgba(56, 189, 248, 0.2);
  }

  .sedes-accordion .sede-card:hover:not(.is-active) {
    opacity: 0.96;
    border-color: rgba(2, 132, 199, 0.3);
  }
}

.sede-card__img-wrap {
  position: relative;
  height: 235px;
  width: 100%;
  overflow: hidden;
  background: var(--orbe-line);
  flex-shrink: 0;
}

@media (min-width: 900px) {
  .sede-card__img-wrap {
    height: 250px;
  }
}

.sede-card__img-wrap img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.8s cubic-bezier(0.16, 1, 0.3, 1), filter 0.5s ease;
}

.sede-card.is-active .sede-card__img-wrap img {
  transform: scale(1.05);
}

.sede-card:not(.is-active) .sede-card__img-wrap img {
  filter: brightness(0.92);
}

.sede-card__tag {
  position: absolute;
  top: 0.75rem;
  left: 0.75rem;
  background: rgba(255, 255, 255, 0.9);
  color: #0f172a;
  padding: 0.25rem 0.65rem;
  border-radius: 8px;
  font-size: 0.75rem;
  font-weight: 700;
  backdrop-filter: blur(8px);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.12);
  border: 1px solid rgba(255, 255, 255, 0.5);
  z-index: 2;
}

[data-theme="dark"] .sede-card__tag {
  background: rgba(15, 23, 42, 0.85);
  color: #ffffff;
  border-color: rgba(255, 255, 255, 0.15);
}

.sede-card__info {
  padding: 1.15rem 1.25rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  flex-grow: 1;
  background: var(--orbe-clay-surface);
}

.sede-card__info h4 {
  font-family: var(--mk-display);
  font-size: 1.12rem;
  margin: 0 0 0.3rem;
  color: var(--orbe-ink);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.sede-card__info p {
  font-size: 0.86rem;
  color: var(--orbe-muted);
  margin: 0 0 0.75rem;
  line-height: 1.4;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

@media (min-width: 900px) {
  .sede-card.is-active .sede-card__info p {
    white-space: normal;
  }
}

.sede-card__link {
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--orbe-accent);
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  transition: transform 200ms ease, color 200ms ease;
  margin-top: auto;
}

[data-theme="dark"] .sede-card__link {
  color: var(--orbe-signal);
}

.sede-card.is-active .sede-card__link {
  color: var(--orbe-accent);
}

.sede-card:hover .sede-card__link {
  transform: translateX(3px);
}
"""

# Enhanced global contrast
contrast_css = """
/* Enhanced Visual Contrast & Depth */
.showcase-box {
  background: var(--orbe-clay-surface);
  border: 1px solid var(--orbe-line);
  border-radius: 24px;
  padding: clamp(1.25rem, 3vw, 2.25rem);
  box-shadow: 0 12px 36px -6px rgba(15, 23, 42, 0.07), 0 2px 8px rgba(15, 23, 42, 0.03);
}

[data-theme="dark"] .showcase-box {
  background: rgba(26, 35, 50, 0.75);
  border-color: rgba(255, 255, 255, 0.09);
  box-shadow: 0 16px 44px rgba(0, 0, 0, 0.45);
}

.sol-card,
.feature-card,
.step-card {
  background: var(--orbe-clay-surface);
  border: 1px solid var(--orbe-line);
  box-shadow: 0 6px 20px -2px rgba(15, 23, 42, 0.05);
  transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s ease, border-color 0.3s ease;
}

.sol-card:hover,
.feature-card:hover,
.step-card:hover {
  transform: translateY(-4px);
  border-color: rgba(2, 132, 199, 0.35);
  box-shadow: 0 16px 36px -4px rgba(2, 132, 199, 0.12), 0 4px 12px rgba(15, 23, 42, 0.05);
}

[data-theme="dark"] .sol-card,
[data-theme="dark"] .feature-card,
[data-theme="dark"] .step-card {
  background: rgba(26, 35, 50, 0.8);
  border-color: rgba(255, 255, 255, 0.08);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.35);
}

[data-theme="dark"] .sol-card:hover,
[data-theme="dark"] .feature-card:hover,
[data-theme="dark"] .step-card:hover {
  border-color: var(--orbe-signal);
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.5), 0 0 20px rgba(56, 189, 248, 0.15);
}

body.marketing {
  --orbe-ink: #0f172a;
  --orbe-muted: #334155;
}

[data-theme="dark"] body.marketing {
  --orbe-ink: #f8fafc;
  --orbe-muted: #94a3b8;
}
"""

# Reemplazar secciones en CSS
# Reemplazar .public-nav anterior
import re
css = re.sub(r'/\* == Nav == \*/.*?\.public-nav nav a\.is-active::after\s*\{[^}]+\}', nav_replacement, css, flags=re.DOTALL)
# Reemplazar .sedes-accordion anterior
css = re.sub(r'\.sedes-accordion\s*\{.*?\.sede-card__info p\s*\{[^}]+\}', accordion_replacement, css, flags=re.DOTALL)

css = css + "\n" + contrast_css

with open(CSS_PATH, "w", encoding="utf-8") as f:
    f.write(css)

print("marketing.css actualizado con diseno mejorado de navbar, acordeon y contraste.")
