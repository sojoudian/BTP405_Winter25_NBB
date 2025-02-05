# Concurrent Socket Server Handling Multiple Clients with Threads

## Overview
This example demonstrates:

- Launching multiple threads for concurrent execution using sockets.
- Managing concurrent access to shared memory safely.
- Handling multiple clients simultaneously with a threaded TCP server.

## Scenario
- A TCP server accepts multiple clients.
- Each client sends a message, and the server responds.
- The server uses threading to handle multiple clients concurrently.
- A shared counter (protected with a lock) tracks the number of connected clients.

## Server Code (`server.py`)
```python
import socket
import threading

# Global shared resource (number of clients)
client_counter = 0
counter_lock = threading.Lock()

# Function to handle each client
def handle_client(client_socket, address):
    global client_counter
    with counter_lock:  # Ensure safe access to shared memory
        client_counter += 1
        client_id = client_counter

    print(f"Client {client_id} connected from {address}")

    # Receive message from client
    data = client_socket.recv(1024).decode()
    print(f"Client {client_id} says: {data}")

    # Send a response
    response = f"Hello Client {client_id}, server received your message!"
    client_socket.sendall(response.encode())

    # Close connection
    client_socket.close()
    print(f"Client {client_id} disconnected.")

# Main server function
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65434))
    server_socket.listen(5)  # Allow up to 5 queued connections

    print("Server is listening on port 65434...")

    while True:
        client_socket, addr = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_thread.start()  # Start a new thread to handle the client

# Run the server
if __name__ == "__main__":
    start_server()
```

## Client Code (`client.py`)
```python
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
```

## Explanation
### 1. Server:
- Uses **threads** to handle multiple clients concurrently.
- Shared counter (`client_counter`) tracks connected clients.
- Uses a **lock (`counter_lock`)** to ensure safe access to the shared counter.
- Accepts multiple clients and assigns a **thread for each connection**.

### 2. Client:
- Connects to the server and **sends a message**.
- Receives and prints the server’s response.
- Closes the connection.

## Expected Output

### Server Console (Handling Multiple Clients):
```
Server is listening on port 65434...
Client 1 connected from ('127.0.0.1', 50000)
Client 1 says: Hello, Server!
Client 2 connected from ('127.0.0.1', 50001)
Client 2 says: Hello, Server!
Client 1 disconnected.
Client 2 disconnected.
```

### Client Console:
```
Server replied: Hello Client 1, server received your message!
```

## Key Takeaways
✔ **Threads allow multiple clients to connect to the server concurrently.**  
✔ **Lock ensures shared memory (client count) is updated safely.**  
✔ **Demonstrates multi-threaded network programming using sockets.**  

## How to Run
1. Start the **server** first:
   ```bash
   python server.py
   ```
2. Then, start multiple **clients** in different terminals:
   ```bash
   python client.py
   ```

