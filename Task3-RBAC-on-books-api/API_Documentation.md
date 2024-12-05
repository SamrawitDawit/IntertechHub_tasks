# Books Collection API Documentation

## Published postman documentation can be found here: `https://documenter.getpostman.com/view/33567770/2sAYBYhB5z`
This API allows users to manage a collection of books, including features for user authentication, CRUD operations for books, and adding/getting takeaways for books. The API also includes role-based access control (RBAC) for admin-specific functionalities.


## Base URL
`https://intertech-hub-tasks-pw8a.vercel.app/`


# Endpoints

## 1. Home
### `GET /`
Displays a welcome message and lists the available API endpoints.

**Response:**
```json
{
    "message": "Welcome to the Books Collection API!",
    "endpoints": [
        {"POST": "/auth/signup - Create a new user"},
        {"POST": "/auth/login - Authenticate a user and get JWT"},
        {"GET": "/books - Fetch all books (user-accessible)"},
        {"POST": "/books - Add a new book (user-accessible)"},
        {"PUT": "/books/<id> - Update a book by ID (user-accessible)"},
        {"DELETE": "/books/<id> - Delete a book by ID (admin-only)"},
        {"GET": "/books/all - Fetch all books (admin-only)"},
        {"POST": "/books/<id>/takeaways - Add a takeaway for a book (user-accessible)"},
        {"GET": "/books/<id>/takeaways - Get all takeaways for a book (user-accessible)"}
    ]
}
```
## 2. Authentication
### 2.1 Sign Up
#### `POST /auth/signup`
Creates a new user.

**Request Body:**
```json
{
    "username": "user123",
    "password": "secure_password"
}
```
**Response:**
Success: 201
```json
{
    "message": "User created successfully"
}
```
Error: 400 or 500

### 2.2 Login
`POST /auth/login`
Authenticates a user and returns a JWT.

**Request Body:**

```json
{
    "username": "user123",
    "password": "secure_password"
}
```
**Response:**
Success: 200
```json
{
    "access_token": "<JWT>"
}
```
Error: 401
```json
{
    "error": "Invalid username or password"
}
```
## 3. Books Management
### 3.1 Get All Books (Admin-Only)
#### `GET /books/all`
Fetches all books in the collection. Requires admin access.

**Headers:**

```makefile
Authorization: Bearer <JWT>
```
**Response:**

Success: 200
```json
[
    {
        "_id": "book_id",
        "title": "Book Title",
        "author": "Author Name"
    }
]
```
Error: 403 or 500
### 3.2 Get Books (User-Accessible)
`GET /books`
Fetches all books in the collection.

**Headers:**
```makefile
Authorization: Bearer <JWT>
```
**Response:**
Success: 200
```json
[
    {
        "_id": "book_id",
        "title": "Book Title",
        "author": "Author Name"
    }
]
```
### 3.3 Get Books by Author (User-Accessible)
`GET /books/<author_name>`
Fetches all books written by a specific author.

**Headers:**

```makefile
Authorization: Bearer <JWT>
```
**Response:**
Success: 200
```json
[
    {
        "_id": "book_id",
        "title": "Book Title",
        "author": "Author Name"
    }
]
```
### 3.4 Add a Book (User-Accessible)
`POST /books`
Adds a new book to the collection.

**Headers:**
```makefile
Authorization: Bearer <JWT>
```
**Request Body:**

```json
{
    "title": "Book Title",
    "author": "Author Name"
}
```
**Response:**
Success: 201
```json
{
    "message": "Book added"
}
```
### 3.5 Update a Book by ID (User-Accessible)
`PUT /books/<id>`
Updates a book in the collection by its ID.

**Headers:**

```makefile
Authorization: Bearer <JWT>
```

**Request Body:**

```json
{
    "title": "Updated Title",
    "author": "Updated Author Name"
}
```
**Response:**
Success: 200
```json
{
    "message": "Book updated"
}
```
### 3.6 Delete a Book by ID (Admin-Only)
`DELETE /books/<id>`
Deletes a book from the collection by its ID. Requires admin access.

**Headers:**

```makefile
Authorization: Bearer <JWT>
```
**Response:**
Success: 200
```json
{
    "message": "Book deleted"
}
```
Error: 404 or 403
## 4. Takeaways Management
### 4.1 Add a Takeaway (User-Accessible)
`POST /books/<id>/takeaways`
Adds a takeaway (note or highlight) for a specific book.

**Headers:**

```makefile
Authorization: Bearer <JWT>
```
**Request Body:**

```json
{
    "takeaway": "Key insight or lesson"
}
```
**Response:**
Success: 201
```json
{
    "message": "Takeaway added successfully"
}
```
### 4.2 Get All Takeaways (User-Accessible)
`GET /books/<id>/takeaways`
Fetches all takeaways for a specific book.

**Headers:**

```makefile
Authorization: Bearer <JWT>
```
**Response:**

Success: 200
```json
{
    "takeaways": [
        "Key insight 1",
        "Key insight 2"
    ]
}
```
Error: 404


## Error Codes
- 400: Bad Request (e.g., validation errors).
- 401: Unauthorized (e.g., invalid or missing JWT).
- 403: Forbidden (e.g., admin-only access for non-admins).
- 404: Not Found (e.g., resource does not exist).
- 500: Internal Server Error.
