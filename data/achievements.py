import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Achievement(SqlAlchemyBase):
    __tablename__ = 'achievements'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    image = sqlalchemy.Column(sqlalchemy.LargeBinary, nullable=False)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    users = orm.relationship(
        "User",
        secondary="user_achievements",
        backref="achievements"
    )
