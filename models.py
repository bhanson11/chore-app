"""SQLAlchemy models for chores app"""

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
db = SQLAlchemy()

class Parent(db.Model):
    """creating parent profile"""

    __tablename__ = 'parents'

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
        db.integer,
        nullable=True        
    )

class Child(db.Model):
    """creating child profile - only parent can create a child profile"""

    __tablename__ = 'children'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.Text, 
        nullable=False,
        unique=True
    )

    password = db.Column(
        db.Text,
        nullable=False
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