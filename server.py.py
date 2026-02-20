
#                  Server Code : (Multi - client + Logging)
import socket
import threading
from crypto_utils import decrypt_message
import datetime

HOST = "0.0.0.0"
PORT = 5000

clients = {}
# socket : username


def log_message(message):
    with open("chat.log", "a") as f:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        f.write(f"{time} | {message}\n")


def broadcast(data, sender_socket=None):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(data)
            except:
                client.close()
                remove_client(client)


def remove_client(client):
    if client in clients:
        username = clients[client]
        print(f"{username} disconnected")
        del clients[client]


def handle_client(client_socket):
    try:
        username_data = client_socket.recv(4096)
        username = decrypt_message(username_data)
        clients[client_socket] = username

        join_msg = f"{username} joined the chat"
        print(join_msg)
        log_message(join_msg)

    except:
        return

    while True:
        try:
            data = client_socket.recv(4096)
            if not data:
                break

            message = decrypt_message(data)
            full_message = f"{username}: {message}"

            print(full_message)
            log_message(full_message)

            broadcast(data, client_socket)

        except:
            break

    remove_client(client_socket)
    client_socket.close()


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print("Server started on port", PORT)

    while True:
        client_socket, addr = server.accept()
        print("Client connected:", addr)

        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()


start_server()