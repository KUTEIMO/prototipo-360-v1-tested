import os
import shutil
import zipfile

SOURCE_GP = r"c:\Users\SOTO\APLICATIVOS\proyectos unisimon\ORBE-GP"
MASTER_ENTREGA = r"c:\Users\SOTO\APLICATIVOS\proyectos unisimon\ORBE360_ENTREGA_SEGUNDO_CORTE_70"
ENTREGABLES_REPO = r"c:\Users\SOTO\APLICATIVOS\proyectos unisimon\ORBE\entregables-corte-2\ENTREGABLES_DEFINITIVOS"

# 1. Update the uncompressed ORBE-GP inside 01_Software_Desarrollado_70_Porciento
dest_uncompressed_gp = os.path.join(MASTER_ENTREGA, "01_Software_Desarrollado_70_Porciento", "ORBE-GP", "plataforma")
for fname in ["index.html", "marketing.css", "marketing-motion.js"]:
    src_f = os.path.join(SOURCE_GP, "plataforma", fname)
    dst_f = os.path.join(dest_uncompressed_gp, fname)
    if os.path.exists(src_f) and os.path.exists(dest_uncompressed_gp):
        shutil.copyfile(src_f, dst_f)
        print(f"Copied {fname} to master uncompressed ORBE-GP folder.")

# 2. Build updated ORBE-GP-Software-70.zip from SOURCE_GP
zip_temp = os.path.join(r"c:\Users\SOTO\APLICATIVOS\proyectos unisimon", "temp_orbe_gp_70.zip")
if os.path.exists(zip_temp):
    os.remove(zip_temp)

print("Building new clean zip from ORBE-GP...")
with zipfile.ZipFile(zip_temp, "w", zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk(SOURCE_GP):
        # Exclude unwanted directories
        dirs[:] = [d for d in dirs if d not in [".git", "node_modules", "entregables-corte-2", ".tempmediaStorage", "coverage", "playwright-report"]]
        for f in files:
            if f.endswith(".zip") or f.endswith(".log") or f.startswith(".temp"):
                continue
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, SOURCE_GP)
            # Prefix with ORBE-GP/ so it extracts cleanly into its own folder
            archive_name = os.path.join("ORBE-GP", rel_path)
            zf.write(full_path, archive_name)

zip_size_mb = os.path.getsize(zip_temp) / (1024 * 1024)
print(f"Zip created successfully! Size: {zip_size_mb:.2f} MB")

# 3. Distribute the zip to the deliverable targets
target_locations = [
    os.path.join(MASTER_ENTREGA, "01_Software_Desarrollado_70_Porciento", "ORBE-GP-Software-70.zip"),
    os.path.join(ENTREGABLES_REPO, "6_Proyecto_Software_70_Porciento", "ORBE-GP-Software-70.zip"),
    os.path.join(ENTREGABLES_REPO, "ORBE-GP-Software-70.zip")
]

for target in target_locations:
    os.makedirs(os.path.dirname(target), exist_ok=True)
    shutil.copyfile(zip_temp, target)
    print(f"Updated zip at: {target}")

if os.path.exists(zip_temp):
    os.remove(zip_temp)

print("All package distributions updated successfully!")
