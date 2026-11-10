import os
import re

gp_dir = r"c:\Users\SOTO\APLICATIVOS\proyectos unisimon\ORBE-GP\plataforma"

# 1. UPDATE index.html
path_html = os.path.join(gp_dir, "index.html")
with open(path_html, "r", encoding="utf-8") as f:
    html = f.read()

# Add cursor canvas if missing
if 'id="cursorOrbCanvas"' not in html:
    html = html.replace(
        '<body class="marketing">',
        '<body class="marketing">\n  <!-- Interactive Foreground Cursor Canvas -->\n  <canvas id="cursorOrbCanvas" class="cursor-canvas" aria-hidden="true"></canvas>'
    )

# Replace duplicate CTA with single unified CTA
cta_pattern = r'<!-- CTA Final -->\s*<section class="cta-band".*?</section>\s*<!-- Pre-Footer CTA -->\s*<section class="cta-band".*?</section>'
unified_cta = '''    <!-- CTA Final Unificada -->
    <section class="cta-band" data-story-chapter="6" aria-labelledby="cta-title">
      <div class="container" data-reveal="up">
        <h2 id="cta-title" data-i18n="cta.title">Lleva tus espacios al siguiente nivel digital</h2>
        <p data-reveal="up" data-reveal-delay="1" data-i18n="cta.lede">Contacta a nuestro equipo para solicitar una demostración del motor ORBE360 adaptado a tu organización.</p>
        <div class="cta-row cta-row--center" data-reveal="up" data-reveal-delay="2">
          <a class="btn btn--primary btn--hero" href="/plataforma/login.html" data-i18n="foot.login">Acceder al Panel Admin</a>
          <a class="btn btn--ghost btn--hero" href="#tours" data-i18n="cta.secondary">Explorar Recorridos 360°</a>
        </div>
      </div>
    </section>'''

if re.search(cta_pattern, html, re.DOTALL):
    html = re.sub(cta_pattern, unified_cta, html, count=1, flags=re.DOTALL)
    print("Unified CTA replaced duplicate CTA successfully!")
else:
    print("CTA pattern did not match directly, checking fallback...")

with open(path_html, "w", encoding="utf-8") as f:
    f.write(html)
print("index.html saved.")

# 2. UPDATE marketing.css
path_css = os.path.join(gp_dir, "marketing.css")
with open(path_css, "r", encoding="utf-8") as f:
    css = f.read()

# Ensure .cursor-canvas is present
if ".cursor-canvas" not in css:
    css = """/* ==========================================================================
   FOREGROUND CURSOR ORB CANVAS (Siempre visible por encima de todas las capas)
   ========================================================================== */
.cursor-canvas {
  position: fixed;
  inset: 0;
  width: 100vw;
  height: 100vh;
  pointer-events: none;
  z-index: 999;
}
""" + css

# Fix .public-nav to be transparent at top and only frosted when .is-scrolled
old_nav = """/* ==========================================================================
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
}"""

new_nav = """/* ==========================================================================
   PUBLIC NAVIGATION - THEME ADAPTIVE & FROSTED GLASS (SEAMLESS AT TOP)
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
  padding: 1.1rem clamp(1rem, 3.5vw, 2.5rem);
  background: transparent;
  border-bottom: 1px solid transparent;
  backdrop-filter: none;
  -webkit-backdrop-filter: none;
  box-shadow: none;
  transition:
    background 300ms ease,
    border-color 300ms ease,
    box-shadow 300ms ease,
    backdrop-filter 300ms ease,
    padding 300ms ease;
}

[data-theme="dark"] .public-nav {
  background: transparent;
  border-bottom: 1px solid transparent;
  box-shadow: none;
  backdrop-filter: none;
  -webkit-backdrop-filter: none;
}

.public-nav.is-scrolled {
  background: rgba(255, 255, 255, 0.85);
  border-bottom: 1px solid rgba(226, 232, 240, 0.85);
  backdrop-filter: blur(20px) saturate(160%);
  -webkit-backdrop-filter: blur(20px) saturate(160%);
  box-shadow: 0 8px 25px -4px rgba(15, 23, 42, 0.06);
  padding-top: 0.75rem;
  padding-bottom: 0.75rem;
}

[data-theme="dark"] .public-nav.is-scrolled {
  background: rgba(11, 18, 32, 0.85);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.5);
}"""

if old_nav in css:
    css = css.replace(old_nav, new_nav)
    print("Replaced public-nav with seamless navigation styles!")
else:
    print("Old public-nav block not found verbatim, checking regex...")

# Make section backgrounds transparent and remove hard partition borders
seamless_sections_rules = """
/* ==========================================================================
   SEAMLESS UNIFIED CANVAS BACKGROUNDS (Sin franjas partidas ni cortes)
   ========================================================================== */
.hero {
  background: transparent !important;
}
.hero__mesh {
  opacity: 0.3 !important;
}
.section--logos {
  background: transparent !important;
  border-bottom: none !important;
}
.section {
  background: transparent !important;
  border-top: none !important;
  border-bottom: none !important;
}
.section--paper,
[data-theme="dark"] .section--paper,
.section--problem,
[data-theme="dark"] .section--problem,
.section--solutions {
  background: transparent !important;
}
.cta-band {
  background: transparent !important;
  border-top: none !important;
}
.cta-band__orb {
  display: none !important;
}
.site-foot {
  background: transparent !important;
  border-top: 1px solid rgba(226, 232, 240, 0.5) !important;
}
[data-theme="dark"] .site-foot {
  border-top: 1px solid rgba(255, 255, 255, 0.08) !important;
}
"""

if "SEAMLESS UNIFIED CANVAS BACKGROUNDS" not in css:
    css += seamless_sections_rules
    print("Added seamless section background rules.")

with open(path_css, "w", encoding="utf-8") as f:
    f.write(css)
print("marketing.css saved.")
