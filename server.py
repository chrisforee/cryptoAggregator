from flask_app import app
# When creating a new controller be sure to add it to the server.py
from flask_app.controllers import users_controller, comments_controller

if __name__ == "__main__":
    app.run(debug = True, port = 5001)
