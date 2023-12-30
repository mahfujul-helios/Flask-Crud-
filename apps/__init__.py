from flask_sqlalchemy import SQLAlchemy
import os
from flask import Flask

db = SQLAlchemy()

def configure_database(app):
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    configure_database(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()
        db.session.commit()
    
    return app