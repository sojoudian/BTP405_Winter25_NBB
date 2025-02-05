import socket

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('localhost', 65432)
client_socket.connect(server_address)

# Send data
message = "Hello, Server!"
client_socket.sendall(message.encode())

# Receive response
response = client_socket.recv(1024).decode()
print(f"Server replied: {response}")

# Close connection
client_socket.close()

