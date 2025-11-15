import socket

HOST = "127.0.0.1"
PORT = 5000

client_socket = socket.socket()
client_socket.connect((HOST, PORT))

filename = input("Enter filename to request: ")
client_socket.send(filename.encode())

data = client_socket.recv(4096).decode()
print("\n--- Server Response ---")
print(data)

client_socket.close()
