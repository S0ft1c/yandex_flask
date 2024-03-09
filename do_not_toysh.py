from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """
    Модель пользователя для системы Mars Explorer.
    """

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    surname = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    position = db.Column(db.String, nullable=False)
    speciality = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    hashed_password = db.Column(db.String(255), nullable=False)
    modified_date = db.Column(db.DateTime, default=datetime.utcnow)
