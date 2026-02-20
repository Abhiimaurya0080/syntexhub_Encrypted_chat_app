import socket
import threading
from crypto_utils import encrypt_message, decrypt_message

SERVER_IP = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

username = input("Enter your name: ")
client.send(encrypt_message(username))


def receive_messages():
    while True:
        try:
            data = client.recv(4096)
            message = decrypt_message(data)
            print("\n" + message)
        except:
            break


def send_messages():
    while True:
        msg = input()
        full_message = msg
        encrypted = encrypt_message(full_message)
        client.send(encrypted)


threading.Thread(target=receive_messages).start()
send_messages()