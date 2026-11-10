import os
import re

gp = r"c:\Users\SOTO\APLICATIVOS\proyectos unisimon\ORBE-GP"
index_path = os.path.join(gp, "plataforma", "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    text = f.read()

scripts = re.findall(r'<script[^>]*src=["\']([^"\']+)["\']', text)
inline_scripts = len(re.findall(r'<script(?![^>]*src)[^>]*>', text))
styles = re.findall(r'<link[^>]*href=["\']([^"\']+\.css[^"\']*)["\']', text)

print("Styles:", styles)
print("External Scripts:", scripts)
print("Inline Scripts count:", inline_scripts)

# Check theme handling
for m in re.finditer(r'(theme|dark|light|matchMedia|color-scheme)', text, re.I):
    start = max(0, m.start() - 60)
    end = min(len(text), m.end() + 60)
    print("Theme match:", text[start:end].replace("\n", " "))
    break
