from flask import Flask

app = Flask(__name__)

from src.category import category_controller
from src.user import user_controller
from src.record import record_controller
