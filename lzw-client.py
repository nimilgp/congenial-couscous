# client.py
import socket

def start_client(host='localhost', port=10000):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    # Ask the user whether they want to compress or decompress
    command = input("Enter 'c' to compress data or 'd' to decompress data: ").strip().lower()

    if command == 'c':
        # Get data to compress from user
        data = input("Enter the string you want to compress: ")
    elif command == 'd':
        # Get compressed data to decompress from user (as a list)
        data = input("Enter the compressed data (as a list of integers): ")
    else:
        print("Invalid command. Exiting.")
        client_socket.close()
        return

    # Send command and data to server in the format 'command:data'
    print(f"Sending {command} request to server...")
    client_socket.send(f"{command}:{data}".encode('utf-8'))

    # Receive result from server
    result = client_socket.recv(1024).decode('utf-8')
    print(f"Received result from server: {result}")
    
    client_socket.close()

if __name__ == '__main__':
    start_client()
