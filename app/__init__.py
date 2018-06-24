from flask import Flask
from config import Config

# The __name__ variable passed to the Flask class is a Python predefined variable, which is set to the name of the
# module in which it is used.
app = Flask(__name__)
app.config.from_object(Config)

# Call routes for register domains
from app import routes