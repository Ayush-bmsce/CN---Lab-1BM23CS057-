import socket

HOST = "127.0.0.1"
PORT = 5001

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print("UDP Server is running...")

while True:
    filename, client_addr = server_socket.recvfrom(1024)
    filename = filename.decode()

    print("Client requested file:", filename)

    try:
        with open(filename, "r") as f:
            data = f.read()
        server_socket.sendto(data.encode(), client_addr)
    except FileNotFoundError:
        server_socket.sendto("File not found".encode(), client_addr)
