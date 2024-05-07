import socket

# The server's IP address and port
SERVER_IP = "172.22.9.105"
SERVER_PORT = 12345

def listen_commands(client_socket):
    while True:
        command = client_socket.recv(4096).decode()
        if command == 'ping':
            client_socket.send('pong'.encode())
        # Add other command cases here
        elif command == 'exit':
            client_socket.close()
            break

def main():
    # Create a new socket and connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, SERVER_PORT))

    listen_commands(client_socket)

if __name__ == "__main__":
    main()