import os

path = r"..\ORBE360_ENTREGA_SEGUNDO_CORTE_70\LEAME_PRIMERO_ENTREGA_CORTE_2.txt"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

old_needle = 'if (-not (Test-Path "ORBE-GP")) { git clone https://github.com/KUTEIMO/ORBE-GP.git }; cd ORBE-GP;'
new_needle = 'if (Test-Path "ORBE-GP") { cd ORBE-GP; if (Test-Path .git) { git pull } } else { git clone https://github.com/KUTEIMO/ORBE-GP.git; cd ORBE-GP };'

if old_needle in text:
    text = text.replace(old_needle, new_needle)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("LEAME txt updated successfully")
else:
    print("Already updated or needle not matched")
