# Here is to a simple TCP client 

import socket

target_host = "www.google.com"
target_port = 80

# Create a socket object
# AF_INET parameter indicates that a IPv4 address or hostname will be used
# SOCK_STREAM indicates that it will be a TCP client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the client
client.connect((target_host,target_port))

# Send some data
client.send(b"GET /HTTP/1.1\r\nHost: google.com\r\n\r\n")

# Receive some data
response = client.recv(4096)

print(response.decode())
client.close()