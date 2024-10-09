# server.py
import socket
from crc import encode_data, verify_data

def start_server(host='localhost', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        # Receive request from client
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break

        # Extract the operation (encode or verify) and data
        operation, data, key = data.split(":")
        print(f"Received operation: {operation}")
        print(f"Received data: {data}")
        print(f"Received key: {key}")

        if operation == 'encode':
            # Generate CRC code
            encoded_data = encode_data(data, key)
            print(f"Encoded data with CRC: {encoded_data}")
            client_socket.send(encoded_data.encode('utf-8'))
        elif operation == 'verify':
            # Verify CRC code
            valid = verify_data(data, key)
            if valid:
                print(f"Data is valid with no errors")
                client_socket.send(b"Data is valid (no errors)")
            else:
                print(f"Data contains errors")
                client_socket.send(b"Data contains errors")
        else:
            client_socket.send(b"Invalid operation")

        client_socket.close()

if __name__ == '__main__':
    start_server()
