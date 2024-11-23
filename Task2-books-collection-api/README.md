# 📚 Books Collection API

The **Books Collection API** is a RESTful API built with Flask for managing a personal collection of books. Users can perform CRUD operations on books, validate book data, store and retrieve takeaways for books, and more.

## Features

- Manage books (Add, Read, Update, Delete).
- Validate book data fields such as title, author, ISBN, and published year.
- Store and fetch takeaways (key lessons or notes) for each book.
- MongoDB integration for persistent storage.
- Hosted online for public access.

---

## 📂 Endpoints

### Base URL
**Deployed API Base URL**: [https://your-api-url.com](https://your-api-url.com)

### Default Route (`/`)
- **`GET /`**
  - **Description**: Displays a welcome message and lists all available endpoints.
  - **Response**:
    ```json
    {
      "message": "Welcome to the Books Collection API!",
      "endpoints": [
        {"GET": "/books - Fetch all books"},
        {"POST": "/books - Add a new book"},
        {"PUT": "/books/<id> - Update a book by ID"},
        {"DELETE": "/books/<id> - Delete a book by ID"},
        {"POST": "/books/<id>/takeaways - Add a takeaway for a book"},
        {"GET": "/books/<id>/takeaways - Get all takeaways for a book"}
      ]
    }
    ```

### Book Management

#### **`GET /books`**
- **Description**: Fetch all books from the database.
- **Response**:
  ```json
  [
    {
      "_id": "book_id",
      "title": "Book Title",
      "author": "Author Name",
      "isbn": "1234567890123",
      "published_year": 2023
    }
  ]

#### **`POST /books`**
- **Description**: Add a new book to the database.
- **Request body**:
```json
    {
    "title": "Book Title",
    "author": "Author Name",
    "isbn": "1234567890123",
    "published_year": 2023
    }
```
- **Response**:
  ```json
    {
    "_id": "book_id",
    "title": "Book Title",
    "author": "Author Name",
    "isbn": "1234567890123",
    "published_year": 2023
    }

#### **`PUT /books/<id>`**
- **Description**: Update a book's information by its ID.
- **Request body**: Same as POST /books.
- **Response**:
  ```json
    {
    "message": "Book updated"
    }
#### **`DELETE /books/<id>`**
- **Description**:Delete a book by its ID.
- **Response**:
  ```json
    {
    "message": "Book deleted"
    }

### Takeaways

#### **`POST /books/<id>/takeaways`**
- **Description**: Add a takeaway (lesson, note) for a specific book.
- **Request body**:
  ```json
    {
    "takeaway": "The key lesson from this book is..."
    }
- **Response**:
  ```json
    {
    "message": "Takeaway added successfully"
    }
#### **`GET /books/<id>/takeaways`**
- **Description**: Retrieve all takeaways for a specific book.
- **Response**:
  ```json
    {
    "takeaways": [
        "Takeaway 1",
        "Takeaway 2"
    ]
    }


## 🚀 Getting Started
### Prerequisites
- Python 3.8+
- MongoDB (local or cloud-hosted, e.g., MongoDB Atlas)
### Setup
1. Clone the repository:

```bash
git clone https://github.com/SamrawitDawit/IntertechHub_tasks.git
cd Task2-books-collection-api
``` 
2. Install dependencies:

```bash
pip install -r requirements.txt
```
3. Set up environment variables:

- Create a .env file in the project root:
```arduino
MONGO_URI=mongodb://<your uri>
```
4. Run the application:

```bash
python app.py
```
The API will be available at `http://localhost:5000`.

## 🗂 Deployment
The API is deployed and publicly accessible. Visit 

## 🤝 Contributing
Contributions are welcome! Please submit a pull request with detailed information about your changes.

