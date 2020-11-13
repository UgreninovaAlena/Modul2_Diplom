import sqlalchemy as sql
import psycopg2
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

BASE = declarative_base()
DSN = 'postgres+psycopg2://postgres:qwASzx1404@localhost:5432/diplom'
engine = sql.create_engine(DSN)
Session = sessionmaker(bind=engine)
session = Session()

class User(BASE):
    __tablename__ = 'User'
    id = sql.Column(sql.Integer, primary_key = True)#Имеем в виду то, что ид в базе данных = ид в вк

    first_name = sql.Column(sql.String)
    last_name = sql.Column(sql.String)
    age = sql.Column(sql.Integer)
    range_age = sql.Column(sql.String)
    city = sql.Column(sql.String)

    dating_users = relationship('DatingUser', backref = 'user')


class DatingUser(BASE):
    __tablename__ = 'DatingUser'
    id = sql.Column(sql.Integer, primary_key=True)

    first_name = sql.Column(sql.String)
    last_name = sql.Column(sql.String)
    age = sql.Column(sql.Integer)

    id_user = sql.Column(sql.Integer, sql.ForeignKey('User.id'))
    id_photos = relationship('Photos', backref = 'DatingUser')


class Photos(BASE):
    __tablename__ = 'Photos'
    id = sql.Column(sql.Integer, primary_key=True)

    link = sql.Column(sql.String)
    count_likes = sql.Column(sql.Integer)

    id_DatingUser = sql.Column(sql.Integer, sql.ForeignKey('DatingUser.id'))
