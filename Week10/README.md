# Flask CRUD API with Docker Support

This project implements a **Flask-based CRUD API** for managing books, with an **in-memory database**. The application is containerized using **Docker**, allowing deployment across different platforms.

---

## 📌 Features
- **CRUD API**: Supports Create, Read, Update, and Delete operations on books.
- **In-Memory Database**: Data is stored temporarily in RAM.
- **Docker Support**: Runs as a containerized application.
- **Multi-Platform Build**: Compatible with ARM64 (Apple M1/M2) and x86-64 (Intel/AMD).

---

## 📜 Python Code (app.py)
This is the **Flask application** responsible for handling API requests.

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for books
books = []
book_id_counter = 1  # Unique book IDs

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = next((b for b in books if b['id'] == id), None)
    return jsonify(book) if book else jsonify({'error': 'Book not found'}), 404

@app.route('/books', methods=['POST'])
def add_book():
    global book_id_counter
    data = request.json
    if not all(k in data for k in ['title', 'author', 'year']):
        return jsonify({'error': 'Missing required fields'}), 400
    
    new_book = {'id': book_id_counter, 'title': data['title'], 'author': data['author'], 'year': data['year']}
    books.append(new_book)
    book_id_counter += 1
    return jsonify(new_book), 201

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = next((b for b in books if b['id'] == id), None)
    if not book:
        return jsonify({'error': 'Book not found'}), 404
    
    data = request.json
    book.update({k: data.get(k, book[k]) for k in ['title', 'author', 'year']})
    return jsonify(book)

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    global books
    books = [b for b in books if b['id'] != id]
    return jsonify({'message': 'Book deleted successfully'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000, debug=True)
```


# Running the Python Application
```bash
python -m venv .env && source .env/bin/activate && pip install --upgrade pip flask
python app.py
```

---

## 📡 API Endpoints & cURL Examples
### 1️⃣ Get All Books
```sh
curl -X GET http://127.0.0.1:6000/books
```

### 2️⃣ Get a Specific Book
```sh
curl -X GET http://127.0.0.1:6000/books/1
```

### 3️⃣ Add a New Book
```sh
curl -X POST http://127.0.0.1:6000/books \
     -H "Content-Type: application/json" \
     -d '{"title": "1984", "author": "George Orwell", "year": 1949}'
```

### 4️⃣ Update a Book
```sh
curl -X PUT http://127.0.0.1:6000/books/1 \
     -H "Content-Type: application/json" \
     -d '{"title": "Animal Farm"}'
```

### 5️⃣ Delete a Book
```sh
curl -X DELETE http://127.0.0.1:6000/books/1
```

---

## 🐳 Dockerfile
The **Dockerfile** defines how to build and run the Flask app inside a container.

```dockerfile
FROM python:3.9
WORKDIR /app
COPY app.py /app/
RUN pip install flask
EXPOSE 6000
CMD ["python", "app.py"]
```

---

## 🔧 Docker Commands
### **1️⃣ Build the Docker Image**
```sh
docker build -t btp_docker:v01 .
```

### **2️⃣ Run the Container**
```sh
docker run -d -p 6000:6000 --name btp_container btp_docker:v01
```

### **3️⃣ Tag & Push to Docker Hub**
```sh
docker login
docker tag btp_docker:v01 maziar/btp_docker:v01
docker push maziar/btp_docker:v01
```

### **4️⃣ Pull and Run on Another Device**
```sh
docker pull maziar/btp_docker:v01
docker run -d -p 6000:6000 --name btp_container maziar/btp_docker:v01
```

### **5️⃣ Check Architecture (for Multi-Platform Builds)**
```sh
docker inspect maziar/btp_docker:v01 | grep Architecture
```

### **6️⃣ Multi-Platform Build (for M1/M2 and x86-64 Support)**
```sh
docker buildx create --use
docker buildx build --platform linux/amd64,linux/arm64 -t maziar/btp_docker:v01 --push .
```

### **7️⃣ Stop & Remove Containers**
```sh
docker stop btp_container
docker rm btp_container
```

---

## 📝 Notes
- The Flask app **listens on 0.0.0.0:6000** for compatibility inside Docker.
- **Multi-Platform Build** ensures support for **ARM64 (M1/M2) & x86-64 (Intel/AMD)**.
- Data **resets after each restart** since it's an in-memory database.

---
🚀 **Happy Coding!**
