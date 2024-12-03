from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt
from bson.objectid import ObjectId
from marshmallow import ValidationError
from database import books, users 
from models import validate_book, validate_user
from bcrypt import hashpw, gensalt, checkpw

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "your-secret-key"
jwt = JWTManager(app)

def initialize_routes(app):
    @app.route("/", methods=["GET"])
    def home():
        return jsonify({
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
                {"GET": "/books/<id>/takeaways - Get all takeaways for a book (user-accessible)"},
            ]
        }), 200

    def admin_required(fn):
        @jwt_required()
        def wrapper(*args, **kwargs):
            claims = get_jwt()
            if claims["role"] != "admin":
                return jsonify({"error": "Admin access required"}), 403
            return fn(*args, **kwargs)
        wrapper.__name__ = fn.__name__
        return wrapper



    @app.route("/auth/signup", methods=["POST"])
    def signup():
        try:
            user_data = validate_user(request.json)
            username = user_data.get('username')
            user = users.find_one({"username": username})
            if user:
                return jsonify({"message": "User already exists"}), 400
            
            hashed_password = hashpw(user_data["password"].encode("utf-8"), gensalt())
            user_data["password"] = hashed_password
            
            users.insert_one({"username": username, "password": hashed_password, "role": "user"})
            return jsonify({"message": "User created successfully"}), 201
        except ValidationError as e:
            return jsonify({"errors": e.messages}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500


    @app.route("/auth/login", methods=["POST"])
    def login():
        data = request.json
        username = data.get("username")
        password = data.get("password")

        user = users.find_one({"username": username})
        if not user or not checkpw(password.encode("utf-8"), user["password"]):
            return jsonify({"error": "Invalid username or password"}), 401

        access_token = create_access_token(identity=str(user["_id"]), additional_claims={"role": user["role"]})
        return jsonify({"access_token": access_token}), 200



    @app.route("/books/all", methods=["GET"])
    @admin_required
    def get_all_books():
        all_books = list(books.find())
        for book in all_books:
            book["_id"] = str(book["_id"])
        return jsonify(all_books), 200


    @app.route("/books", methods=["GET"])
    @jwt_required()
    def get_books():
        all_books = list(books.find())
        for book in all_books:
            book["_id"] = str(book["_id"])
        return jsonify(all_books), 200
    
    @app.route("/books/<author_name>", methods=["GET"])
    @jwt_required()
    def get_books_by_author(author_name):
        all_books = list(books.find({"author": author_name}))
        for book in all_books:
            book["_id"] = str(book["_id"])
        return jsonify(all_books), 200

    @app.route("/books", methods=["POST"])
    @jwt_required()
    def add_book():
        try:
            data = validate_book(request.json)
            book = books.insert_one(data)
            return jsonify({"message": "Book added"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 400


    @app.route("/books/<id>", methods=["PUT"])
    @jwt_required()
    def update_book(id):
        data = request.json
        result = books.update_one({"_id": ObjectId(id)}, {"$set": data})
        if result.matched_count == 0:
            return jsonify({"error": "Book not found"}), 404
        return jsonify({"message": "Book updated"}), 200



    @app.route("/books/<id>", methods=["DELETE"])
    @admin_required
    def delete_book(id):
        result = books.delete_one({"_id": ObjectId(id)})
        if result.deleted_count == 0:
            return jsonify({"error": "Book not found"}), 404
        return jsonify({"message": "Book deleted"}), 200


    @app.route("/books/<id>/takeaways", methods=["POST"])
    @jwt_required()
    def add_takeaway(id):
        takeaway = request.json.get("takeaway")
        if not takeaway:
            return jsonify({"error": "Takeaway content is required"}), 400
        result = books.update_one(
            {"_id": ObjectId(id)},
            {"$push": {"takeaways": takeaway}}
        )
        if result.matched_count == 0:
            return jsonify({"error": "Book not found"}), 404

        return jsonify({"message": "Takeaway added successfully"}), 201


    @app.route("/books/<id>/takeaways", methods=["GET"])
    @jwt_required()
    def get_takeaways(id):
        book = books.find_one({"_id": ObjectId(id)}, {"takeaways": 1, "_id": 0})
        if not book:
            return jsonify({"error": "Book not found"}), 404

        takeaways = book.get("takeaways", [])
        return jsonify({"takeaways": takeaways}), 200



