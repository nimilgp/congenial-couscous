# client.py
import socket

def start_client(host='localhost', port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Choose operation: encode or verify
    operation = input("Enter 'encode' to generate CRC or 'verify' to check data: ").strip().lower()

    if operation == 'encode':
        # Input the binary data and the key (polynomial) to generate CRC
        data = input("Enter the binary data to encode (e.g., 1011001): ").strip()
        key = input("Enter the CRC key (polynomial) (e.g., 1101): ").strip()
    elif operation == 'verify':
        # Input the binary data with CRC and the key (polynomial) to verify
        data = input("Enter the binary data with CRC to verify (e.g., 1011001110): ").strip()
        key = input("Enter the CRC key (polynomial) (e.g., 1101): ").strip()
    else:
        print("Invalid operation. Exiting.")
        client_socket.close()
        return

    # Send request to server
    client_socket.send(f"{operation}:{data}:{key}".encode('utf-8'))

    # Receive response from server
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Server response: {response}")

    client_socket.close()

if __name__ == '__main__':
    start_client()
