from flask import Flask
from flask_migrate import Migrate
from app.models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'
db.init_app(app)
migrate = Migrate(app, db)
