"""Entry point of the application"""

from flask import Flask, request, render_template, current_app, session, redirect, url_for
from flask_session import Session
from flask_login import current_user
from config import Config
from models import db, User, fill_db_with_values
from login import login_manager
from account_routes import users

app = Flask(__name__)
app.config.from_object(Config)
Session(app)

db.init_app(app)
with app.app_context():
    db.drop_all()
    db.create_all()
    fill_db_with_values()
login_manager.init_app(app)

app.register_blueprint(users)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/session')
def get_session():
    # TODO: Remove session route
    print(list(str(zip(session.keys(), session.values()))))
    return str(list(zip(session.keys(), session.values())))
