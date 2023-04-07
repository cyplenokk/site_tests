import datetime
import sqlalchemy

from .db_session import SqlAlchemyBase

class Requests(SqlAlchemyBase):
    __tablename__ = 'requests'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    request = sqlalchemy.Column(sqlalchemy.String, nullable=True)