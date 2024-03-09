from .db_session import SqlAlchemyBase
import sqlalchemy as sa
import sqlalchemy.orm as orm
import datetime
from sqlalchemy_serializer import SerializerMixin

association_table = sa.Table(
    'association',
    SqlAlchemyBase.metadata,
    sa.Column('news', sa.Integer, sa.ForeignKey('news.id')),
    sa.Column('category', sa.Integer, sa.ForeignKey('category.id'))
)
class Category(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'category'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=True)
