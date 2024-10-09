# server.py
import socket
from hamming import generate_hamming_code, detect_and_correct_error

def start_server(host='localhost', port=20000):
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

        # Extract the operation (generate or correct) and data
        operation, data = data.split(":")
        print(f"Received operation: {operation}")
        print(f"Received data: {data}")

        if operation == 'generate':
            # Generate Hamming code
            hamming_code = generate_hamming_code(data)
            print(f"Generated Hamming code: {hamming_code}")
            client_socket.send(hamming_code.encode('utf-8'))
        elif operation == 'correct':
            # Detect and correct error in Hamming code
            corrected_code, corrected = detect_and_correct_error(data)
            if corrected:
                print(f"Error detected and corrected: {corrected_code}")
            else:
                print(f"No error detected in the Hamming code: {data}")
            client_socket.send(corrected_code.encode('utf-8'))
        else:
            client_socket.send(b"Invalid operation")

        client_socket.close()

if __name__ == '__main__':
    start_server()
