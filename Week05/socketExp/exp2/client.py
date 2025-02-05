import socket
import pickle

# Data to send
data = {"name": "Alice", "age": 30, "role": "developer"}

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 65433))

# Serialize and send data
pickled_data = pickle.dumps(data)
client_socket.sendall(pickled_data)

# Close connection
client_socket.close()

