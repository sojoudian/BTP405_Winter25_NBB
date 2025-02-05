# Inter-Process Communication using Sockets

## Overview
This example demonstrates how two Python processes can communicate using TCP sockets.

## Scenario
A server waits for a connection from a client. The client sends a message, and the server responds.

## Server Code
```python
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
```

## Client Code
```python
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
```

## Explanation
### The Server:
- Binds to `localhost:65432` and listens for incoming connections.
- Receives a message from the client.
- Responds with a greeting.

### The Client:
- Connects to the server.
- Sends a message.
- Receives and prints the server’s response.

## How to Run
1. Start the **server** first:
   ```bash
   python server.py
   ```
2. Then, start the **client** in another terminal:
   ```bash
   python client.py
   ```

The client will send a message to the server, and the server will respond.

