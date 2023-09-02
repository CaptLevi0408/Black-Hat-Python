import socket
import threading

# Define the IP address and port to listen on
IP = '0.0.0.0'  # Listen on all available network interfaces
PORT = 1234     # Port number to listen on

# Function to handle incoming client connections
def handle_client(client_socket):
    with client_socket as sock:
        # Receive data from the client (up to 1024 bytes)
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        
        # Send a simple acknowledgment back to the client
        sock.send(b'ACK')

# Main function to set up the server
def main():
    # Create a socket object using IPv4 and TCP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the IP and port
    server.bind((IP, PORT))

    # Listen for incoming connections, allowing up to 5 queued connections
    server.listen(5)
    print(f'[*] Listening on {IP}:{PORT}')

    while True:
        # Accept an incoming connection, client is a new socket object
        # and address is the client's address (IP and port)
        client, address = server.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')

        # Create a new thread to handle the client's communication
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

if __name__ == '__main__':
    main()
