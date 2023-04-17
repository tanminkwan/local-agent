import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
COMMANDER_SERVER_URL = 'http://localhost:8809'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')