from flask import Flask
from routes import initialize_routes, app


initialize_routes(app)

if __name__ == '__main__':
    app.run()