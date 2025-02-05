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

