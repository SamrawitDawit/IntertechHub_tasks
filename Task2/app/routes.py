from flask import request, jsonify
from app.database import books
from app.models import validate_book
from bson.objectid import ObjectId


def initialize_routes(app):
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
            return jsonify({"_id": str(book_id), **data}), 201
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
    