"""SQLAlchemy models for chores app"""

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
db = SQLAlchemy()

class User(db.Model):
    """creating parent profile"""

    __tablename__ = 'users'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.Text, 
        nullable=False,
        unique=True
    )

    email = db.Column(
        db.Text,
        nullable=False,
        unique=True
    )

    password_hash = db.Column(
        db.Text,
        nullable=False
    )

    parent_id = db.Column(
        db.Integer,
        nullable=True        
    )
    
class Chore(db.Model):
    """creating chores"""

    __tablename__ = 'chores'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.Text,
        nullable=False
    )

    category = db.Column(
        db.Integer,
        db.ForeignKey('categories.id', ondelete="cascade"),
        nullable=False,
    ) 

class Category(db.Model):
    """categories for chores"""

    __tablename__ = 'categories'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.Text,
        nullable=False
    )

def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)