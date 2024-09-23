#main.py

from server import (start_server)

def main():
    print("Starting Kafka server...")
    HOSTNAME, PORT = "127.0.0.1", 8080
    start_server(HOSTNAME, PORT)


if __name__ == "__main__":
    main()