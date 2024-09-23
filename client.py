import socket

HOSTNAME = "127.0.0.1"
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOSTNAME, PORT))
    s.sendall("Hello Server!".encode())

    data = s.recv(1024)
    print(data)

