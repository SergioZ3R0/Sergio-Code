import subprocess
import sys
import os
from cryptography.fernet import Fernet
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

with open("key.key", "rb") as key_file:
    key = key_file.read()

for file in files:
    with open(file, "rb") as f:
        data = f.read()
    data_decrypted = Fernet(key).decrypt(data)
    with open(file, "wb") as f:
        f.write(data_decrypted)
