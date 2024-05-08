import socket
import uuid

SERVER_IP = "172.22.9.105"
SERVER_PORT = 12345

def get_mac_address():
    mac_num = hex(uuid.getnode()).replace('0x', '')
    mac = ':'.join(mac_num[i: i + 2] for i in range(0, 11, 2))
    return mac

def listen_commands(client_socket):
    while True:
        command = client_socket.recv(4096).decode()
        if command == 'ping':
            client_socket.send('pong'.encode())
        elif command == 'exit':
            client_socket.close()
            break

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, SERVER_PORT))

    # Send MAC address to server
    mac_address = get_mac_address()
    client_socket.send(mac_address.encode())

    listen_commands(client_socket)

if __name__ == "__main__":
    main()
