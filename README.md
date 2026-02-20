# syntexhub_Encrypted_chat_app
Secure client-server chat application using Python sockets and AES encryption with multi-client support.

Encrypted_chat_app/
│
├── server.py
├── client.py
├── crypto_utils.py
├── chat.log
└── README.md

# 🔐 Encrypted Chat Application


### 1. server.py
This is the main server file of the application.

Responsibilities:
- Starts the chat server
- Listens for incoming client connections
- Handles multiple clients simultaneously using threads
- Receives encrypted messages from clients
- Broadcasts messages to all connected users
- Logs chat messages into `chat.log`

Main tasks performed by server:
- Socket creation
- Client connection management
- Message broadcasting
- Chat logging
- Thread handling

---

### 2. client.py
This file is responsible for the client-side chat application.

Responsibilities:
- Connects the user to the chat server
- Sends encrypted messages to the server
- Receives messages from other users
- Decrypts received messages
- Displays messages in real time

Main features:
- Username input system
- Real-time chat
- Background message receiving using threads
- Secure encrypted communication

---

### 3. crypto_utils.py
This file contains all encryption and decryption logic used in the application.

Responsibilities:
- AES encryption implementation
- Message encryption before sending
- Message decryption after receiving
- Secure key usage
- Initialization Vector (IV) handling

Functions included:
- encrypt_message()
- decrypt_message()

This ensures that:
Messages are not sent in plain text over the network.

---

### 4. chat.log
This file stores the chat history automatically.

It records:
- User join events
- Messages sent by users
- Timestamp of messages

Example log entry:

This helps in:
- Monitoring conversations
- Debugging
- Maintaining chat records

---

### 5. __pycache__/
This folder is automatically created by Python.

It stores:
Compiled Python files (.pyc)

Purpose:
- Improves program performance
- Speeds up execution

You normally **do not upload this folder to GitHub**.

You can ignore it using `.gitignore`.

Example `.gitignore`:

---

### 6. README.md
This file contains documentation of the project.

It includes:
- Project overview
- Features
- Installation steps
- How to run the project
- Project structure
- Example output

This helps developers understand the project easily.
