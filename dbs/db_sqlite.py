from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean

db = SQLAlchemy()


def get_db(app):
    db.init_app(app)
    return db


class Todo(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    complete = Column(Boolean, default=False)
