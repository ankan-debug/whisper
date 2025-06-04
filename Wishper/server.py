# server.py
import socket
import threading
import json
from utils import load_config
from cipher import decrypt_message

# Load user settings
config = load_config()

# Server setup
HOST = '0.0.0.0'  # Listen to all interfaces
PORT = 9999       # Pick any unused port

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"[📡] Listening on {HOST}:{PORT}...")

clients = []

def broadcast(message, _client):
    for client in clients:
        if client != _client:
            try:
                client.send(message)
            except:
                clients.remove(client)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024).decode()

            if config["secret_mode"]:
                message = decrypt_message(message)

            print(f"[💬] Received: {message}")
            broadcast(message.encode(), client)
        except:
            clients.remove(client)
            client.close()
            break

def receive_connections():
    while True:
        client, address = server.accept()
        print(f"[🔗] Connected with {str(address)}")

        clients.append(client)
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

receive_connections()
