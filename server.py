import socket


def handle_response(request):
    id_bytes = (request).to_bytes(4, byteorder="big")
    return len(id_bytes).to_bytes(4, byteorder="big") + id_bytes


def handle_client(client):
    request = client.recv(1024)
    # response = handle_response(request)
    response = handle_response(7)
    client.sendall(response)
    client.close()


def start_server(HOSTNAME = '127.0.0.1', PORT = 8080):
    # Create a server socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOSTNAME, PORT))
    server.listen()
    print('Server is listening on port {}'.format(PORT))

    client_socket, client_add = server.accept()

    while True:
        handle_client(client_socket)

    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #     s.bind((HOSTNAME, PORT))
    #     s.listen()
    #
    #     client_conn, client_addr = s.accept()
    #
    #     with client_conn:
    #         print("Connected by", client_addr)
    #         while True:
    #             data = client_conn.recv(1024)
    #             if not data:
    #                 break
    #             client_conn.sendall(data)
