from flask import request, jsonify
from app.database import books
from app.models import validate_book
from bson.objectid import ObjectId


def initialize_routes(app):
    @app.route('/', methods=['GET'])
    def home():
        return jsonify({
            "message": "Welcome to the Books Collection API!",
            "endpoints": [
                {"GET": "/books - Fetch all books"},
                {"POST": "/books - Add a new book"},
                {"PUT": "/books/<id> - Update a book by ID"},
                {"DELETE": "/books/<id> - Delete a book by ID"},
                {"POST": "/books/<id>/takeaways - Add a takeaway for a book"},
                {"GET": "/books/<id>/takeaways - Get all takeaways for a book"},
            ]
        }), 200
    @app.route('/books', methods=['GET'])
    def get_books():
        all_books = list(books.find())
        for book in all_books:
            book['_id'] = str(book['_id'])
        return jsonify(all_books), 200
    @app.route('/books', methods=['POST'])
    def add_book():
        try:
            data = validate_book(request.json)
            book_id = books.insert_one(data).inserted_id
            return jsonify({"message": "Book added"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    @app.route('/books/<id>', methods=['PUT'])
    def update_book(id):
        try:
            data = validate_book(request.json)
            result = books.update_one({"_id": ObjectId(id)}, {"$set": data})
            if result.matched_count == 0:
                return jsonify({"error": "Book not found"}), 404
            return jsonify({"message": "Book updated"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    @app.route('/books/<id>', methods=['DELETE'])
    def delete_book(id):
        result = books.delete_one({"_id": ObjectId(id)})
        if result.deleted_count == 0:
            return jsonify({"error": "Book not found"}), 404
        return jsonify({"message": "Book deleted"}), 200
    @app.route('/books/<id>/takeaways', methods=['POST'])
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


    @app.route('/books/<id>/takeaways', methods=['GET'])
    def get_takeaways(id):
        book = books.find_one({"_id": ObjectId(id)}, {"takeaways": 1, "_id": 0})
        if not book:
            return jsonify({"error": "Book not found"}), 404

        takeaways = book.get("takeaways", [])
        return jsonify({"takeaways": takeaways}), 200

        