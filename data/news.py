from .db_session import SqlAlchemyBase
import sqlalchemy as sa
import sqlalchemy.orm as orm
import datetime
from sqlalchemy_serializer import SerializerMixin
from flask_login import UserMixin


class News(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'news'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)

    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now)
    title = sa.Column(sa.String, nullable=True)
    content = sa.Column(sa.String, nullable=True)
    is_private = sa.Column(sa.Boolean, default=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"))

    user = orm.relationship('User')

    categories = orm.relationship('Category', secondary='association', backref='news')

