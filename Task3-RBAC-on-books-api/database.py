from pymongo import MongoClient


client = MongoClient("mongodb+srv://samrikdawit:it'sSamri22@intertechhub.a0g3q.mongodb.net/?retryWrites=true&w=majority&appName=Intertechhub", tls=True)
db = client["books_collection"]
books = db.books
users = db.users