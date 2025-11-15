import socket

HOST = "127.0.0.1"     # localhost
PORT = 5000            # any free port

server_socket = socket.socket()
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Server started. Waiting for client...")

conn, addr = server_socket.accept()
print("Connected to:", addr)

filename = conn.recv(1024).decode()

try:
    with open(filename, "r") as f:
        data = f.read()
    conn.send(data.encode())
except FileNotFoundError:
    conn.send("File not found".encode())

conn.close()
server_socket.close()
