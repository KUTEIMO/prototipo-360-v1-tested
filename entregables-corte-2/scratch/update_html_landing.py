import os
import re

gp = r"c:\Users\SOTO\APLICATIVOS\proyectos unisimon\ORBE-GP"

# 1. Modificar plataforma/index.html
index_path = os.path.join(gp, "plataforma", "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# Canvas en story-bg
if '<canvas id="ambient3dCanvas"' not in html:
    html = html.replace(
        '<div class="story-bg__orb story-bg__orb--b"></div>',
        '<div class="story-bg__orb story-bg__orb--b"></div>\n    <canvas id="ambient3dCanvas" class="story-bg__canvas"></canvas>'
    )
    print("Canvas ambient3dCanvas agregado a storyBg.")

# Card 1 active inicial
if 'class="sede-card is-active"' not in html:
    html = html.replace(
        '<a href="/unisimoncucuta/experienciavirtual/?sede=1" class="sede-card">',
        '<a href="/unisimoncucuta/experienciavirtual/?sede=1" class="sede-card is-active">'
    )
    print("Sede 1 inicializada con clase is-active.")

# Actualizar script de tema en head
old_theme_script = """    (function () {
      var t = localStorage.getItem("orbe_theme");
      if (t === "dark" || t === "light") document.documentElement.setAttribute("data-theme", t);
      else if (window.matchMedia("(prefers-color-scheme: dark)").matches) document.documentElement.setAttribute("data-theme", "dark");
    })();"""

new_theme_script = """    (function () {
      var t = localStorage.getItem("orbe_theme");
      var sysDark = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
      var theme = (t === "dark" || t === "light") ? t : (sysDark ? "dark" : "light");
      document.documentElement.setAttribute("data-theme", theme);
    })();"""

if old_theme_script in html:
    html = html.replace(old_theme_script, new_theme_script)
    print("Script de tema en head actualizado.")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)

print("index.html actualizado.")
