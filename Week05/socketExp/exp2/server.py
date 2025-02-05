import socket
import pickle

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 65433))
server_socket.listen(1)

print("Server is waiting for a connection...")
connection, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

# Receive pickled data
data = connection.recv(4096)
received_object = pickle.loads(data)

print(f"Received object: {received_object}")

# Close connection
connection.close()
server_socket.close()

