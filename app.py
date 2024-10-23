import os

from flask import Flask, session, g, render_template
from flask_debugtoolbar import DebugToolbarExtension

# from forms import 
from models import db, connect_db, User, Chore, Category

CURR_USER_KEY = "curr_user"

app = Flask(__name__)

# Get DB_URI from environ variable (useful for production/testing) or,
# if not set there, use development local db.
app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ.get('DATABASE_URL', 'postgresql:///chores_app'))

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "it's a secret")
toolbar = DebugToolbarExtension(app)

connect_db(app)

##########################################################################################
## Parent User sign up / login / logout 

@app.before_request
def add_user_to_g():
    """If we're logged in, add curr user to Flask global."""

    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])

    else:
        g.user = None


def do_login(user):
    """Log in user."""

    session[CURR_USER_KEY] = user.id


def do_logout():
    """Logout user."""

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]

### app.route signup

### app.route login

### app.route logout

### app.route add child 

### app.route edit child

### app.route remove child

### app.route parent invite other parent

### app.route chore data from API 

### app.route create 

### app.route edit

### app.route delete chores

### app.route assign chores

### app.route unassign chores

#### ALL USERS 

### app.route boolean mark chore as complete 