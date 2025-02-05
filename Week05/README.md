# Sockets and Concurrency in Python

## Overview
This repository contains various examples demonstrating how to use **sockets** and **concurrency** in Python. The examples cover topics such as:

- **Inter-Process Communication (IPC) using sockets**
- **Object serialization and transmission using `pickle`**
- **Multi-threaded socket servers handling multiple clients concurrently**
- **Thread synchronization and shared memory management**

## Topics Covered

### 1. Inter-Process Communication using Sockets
- Demonstrates **basic socket communication** between a client and a server.
- The server listens for connections, and the client sends a message.
- The server responds and closes the connection.

📂 [Example: Inter-Process Communication using Sockets](./inter_process_communication/README.md)

### 2. Object Serialization using `pickle` over Sockets
- Demonstrates how to serialize Python objects with `pickle` and transmit them over a socket.
- The server receives a pickled object from the client, deserializes it, and processes it.

📂 [Example: Object Serialization using `pickle` over Sockets](./serialization_with_pickle/README.md)

### 3. Concurrent Socket Server Handling Multiple Clients with Threads
- Shows how to use **threading** to handle multiple client connections concurrently.
- Uses **thread locks** to protect shared memory (client counter).

📂 [Example: Concurrent Socket Server Handling Multiple Clients with Threads](./multi_threaded_server/README.md)

## Prerequisites
To run these examples, you need:

- **Python 3.x** installed.
- Basic understanding of **networking and sockets**.
- Knowledge of **multi-threading and process synchronization**.

## How to Run Examples
Each example contains its own `README.md` file with instructions. Generally:

1. **Start the server first**:
   ```bash
   python server.py
   ```
2. **Run the client**:
   ```bash
   python client.py
   ```

For concurrent examples, run multiple clients in separate terminals.

## Contributions
Feel free to fork the repository, add new examples, or improve existing ones!

## License
This repository is licensed under the **MIT License**.

