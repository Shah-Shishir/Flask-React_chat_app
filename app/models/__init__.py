from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import all models here for easier access
from .user_model import User
from .item_model import Item
