
import sqlite3

def update_book(isbn, title, author_id, publication_year):
    # Connect to the existing books database
    conn = sqlite3.connect('books.db')
    c = conn.cursor()

    # Prepare the update statement to update book details
    update_sql = '''
    UPDATE books
    SET title = ?, author_id = ?, publication_year = ?
    WHERE isbn = ?
    '''

    try:
        # Execute the update statement with the provided details
        c.execute(update_sql, (title, author_id, publication_year, isbn))

        # Commit the changes to the database
        conn.commit()

        # Check if the update was successful by checking the rowcount
        if c.rowcount > 0:
            print("Book updated successfully.")
        else:
            print("No book found with the given ISBN.")
    except sqlite3.IntegrityError as e:
        # Handle errors such as violating the uniqueness of ISBN or foreign key constraints
        print(f"Error updating the book: {e}")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")
    finally:
        # Close the connection to the database
        conn.close()

#Example usage
update_book('123-4567890123', 'New Title', 2, 2024)