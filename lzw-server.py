# server.py
import socket
from lzw import lzw_compress, lzw_decompress

def start_server(host='localhost', port=10000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        # Receive command and data from the client
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        
        # First, extract the operation (compress or decompress) and the actual data
        command, data = data.split(":", 1)
        print(f"Received command: {command}")
        print(f"Received data: {data}")

        # Perform compression or decompression based on the command
        if command == "c":
            compressed_data = lzw_compress(data)
            print(f"Compressed data: {compressed_data}")
            client_socket.send(str(compressed_data).encode('utf-8'))
        elif command == "d":
            # Convert received string back to list of integers
            compressed_list = eval(data)
            decompressed_data = lzw_decompress(compressed_list)
            print(f"Decompressed data: {decompressed_data}")
            client_socket.send(decompressed_data.encode('utf-8'))
        else:
            client_socket.send(b"Invalid command")

        client_socket.close()

if __name__ == '__main__':
    start_server()
