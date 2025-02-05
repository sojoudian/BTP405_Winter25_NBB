import socket

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to an address and port
server_address = ('localhost', 65432)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)
print("Server is waiting for a connection...")

# Accept connection
connection, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

# Receive data
data = connection.recv(1024).decode()
print(f"Received: {data}")

# Send a response
response = "Hello from server!"
connection.sendall(response.encode())

# Close connection
connection.close()
server_socket.close()

