from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for books
books = []
book_id_counter = 1  # To track unique book IDs

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = next((b for b in books if b['id'] == id), None)
    if book:
        return jsonify(book)
    return jsonify({'error': 'Book not found'}), 404

@app.route('/books', methods=['POST'])
def add_book():
    global book_id_counter
    data = request.json
    if not data or 'title' not in data or 'author' not in data or 'year' not in data:
        return jsonify({'error': 'Missing required fields'}), 400

    new_book = {
        'id': book_id_counter,
        'title': data['title'],
        'author': data['author'],
        'year': data['year']
    }
    books.append(new_book)
    book_id_counter += 1

    return jsonify(new_book), 201

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = next((b for b in books if b['id'] == id), None)
    if not book:
        return jsonify({'error': 'Book not found'}), 404

    data = request.json
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    book.update({
        'title': data.get('title', book['title']),
        'author': data.get('author', book['author']),
        'year': data.get('year', book['year'])
    })

    return jsonify(book)

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    global books
    books = [b for b in books if b['id'] != id]
    return jsonify({'message': 'Book deleted successfully'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000, debug=True)
