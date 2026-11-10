import os

path = r"c:\Users\SOTO\APLICATIVOS\proyectos unisimon\ORBE-GP\plataforma\marketing.css"
with open(path, "r", encoding="utf-8") as f:
    css = f.read()

imp = '@import url("/plataforma/tokens.css");'
if imp in css:
    css = css.replace(imp, "")

css = imp + "\n\n" + css.strip() + "\n"

with open(path, "w", encoding="utf-8") as f:
    f.write(css)

print("Import tokens.css placed at line 1 successfully.")
