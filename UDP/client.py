import socket

HOST = "127.0.0.1"
PORT = 5001

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

filename = input("Enter file name to request: ")
client_socket.sendto(filename.encode(), (HOST, PORT))

data, _ = client_socket.recvfrom(4096)

print("\n--- Server Response ---")
print(data.decode())

client_socket.close()
