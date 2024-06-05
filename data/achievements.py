import sqlalchemy

from .db_session import SqlAlchemyBase


class Achievement(SqlAlchemyBase):
    __tablename__ = 'achievements'

    name = sqlalchemy.Column(sqlalchemy.String, primary_key=True, unique=True, nullable=False)
    image = sqlalchemy.Column(sqlalchemy.String)
    description = sqlalchemy.Column(sqlalchemy.String)