from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# The __name__ variable passed to the Flask class is a Python predefined variable, which is set to the name of the
# module in which it is used.
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Call routes for register domains
from app import routes, models