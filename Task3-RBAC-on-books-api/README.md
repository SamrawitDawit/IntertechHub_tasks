# 📚 Books Collection API

The **Books Collection API** is a RESTful API built with Flask for managing a personal collection of books. Users can perform CRUD operations on books, validate book data, store and retrieve takeaways for books, and more.

## Features

- Manage books (Add, Read, Update, Delete).
- Validate book data fields such as title, author, ISBN, and published year.
- Store and fetch takeaways (key lessons or notes) for each book.
- MongoDB integration for persistent storage.
- Hosted online for public access.

---


## Authentication & Authorization
* JWT-based authentication is used.
* Role-Based Access Control (RBAC):
* Admins have full access (e.g., delete books, view all books).
* Users can perform CRUD operations except for admin-specific actions.


## 🚀 Getting Started
### Prerequisites
- Python 3.8+
- The database of this project is MongoDB Atlas, but you can change it to MongoDB local by changing the db uri inside database.py
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
4. Run the application:

```bash
python app.py
```
The API will be available at `http://localhost:5000`.

## 🗂 Deployment
The API is deployed and publicly accessible. Visit `https://intertech-hub-tasks-pw8a.vercel.app/`

