# client.py
import socket

def start_client(host='localhost', port=20000):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Choose operation: generate or correct
    operation = input("Enter 'generate' to generate Hamming code or 'correct' to correct a Hamming code: ").strip().lower()

    if operation == 'generate':
        # Input the binary data to generate the Hamming code
        data = input("Enter the binary data to generate Hamming code (e.g., 1011001): ").strip()
    elif operation == 'correct':
        # Input the binary Hamming code to detect/correct errors
        data = input("Enter the binary Hamming code to correct (e.g., 101110101011): ").strip()
    else:
        print("Invalid operation. Exiting.")
        client_socket.close()
        return

    # Send request to server
    client_socket.send(f"{operation}:{data}".encode('utf-8'))

    # Receive response from server
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Server response: {response}")

    client_socket.close()

if __name__ == '__main__':
    start_client()
