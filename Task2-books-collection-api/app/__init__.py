from flask import Flask
from app.routes import initialize_routes

app = Flask(__name__)
initialize_routes(app)


app.run()