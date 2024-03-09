from .db_session import SqlAlchemyBase
import sqlalchemy as sa
import sqlalchemy.orm as orm
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=True)
    about = sa.Column(sa.String)
    hashed_password = sa.Column(sa.String, nullable=True)
    email = sa.Column(sa.String, nullable=True, unique=True, index=True)
    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now)

    news = orm.relationship('News', back_populates='user')

    def __repr__(self) -> str:
        return f'<{self.id}> {self.name} {self.email}'

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
