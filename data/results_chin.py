import datetime
import sqlalchemy
from werkzeug.security import generate_password_hash, check_password_hash

from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Results_Chin(SqlAlchemyBase):
    __tablename__ = 'results_chin'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    chin_1 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    chin_2 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    chin_3 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    chin_4 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    chin_5 = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"))

    user = orm.relationship('User')
