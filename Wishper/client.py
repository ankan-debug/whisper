import socket
import json
import time
from cipher import encrypt_message
from utils import load_config

# Load user settings
config = load_config()

HOST = input("Enter recipient IP (e.g., 192.168.0.105): ")
PORT = 9090

def main():
    print("[🟢] Whisper Client Started")
    print("Created and Maintained By Saha")
    while True:
        message = input("You > ")

        if config['secret_mode']:
            message = encrypt_message(message)

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                s.sendall(message.encode())
        except Exception as e:
            print(f"[❌] Error: {e}")
        
        time.sleep(0.5)

if __name__ == "__main__":
    main()
