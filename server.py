import socket

HOSTNAME = "127.0.0.1"
PORT = 8080
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOSTNAME, PORT))
    s.listen()

    client_conn, client_addr = s.accept()

    with client_conn:
        print("Connected by", client_addr)
        while True:
            data = client_conn.recv(1024)
            if not data:
                break
            client_conn.sendall(data)
