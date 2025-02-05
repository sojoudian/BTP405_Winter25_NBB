import socket

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 65434))

# Send data
message = "Hello, Server!"
client_socket.sendall(message.encode())

# Receive response
response = client_socket.recv(1024).decode()
print(f"Server replied: {response}")

# Close connection
client_socket.close()

