from flask import Flask

app = Flask(__name__)

from src.category import category_controller