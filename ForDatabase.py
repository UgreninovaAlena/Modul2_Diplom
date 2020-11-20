from pprint import pprint

import sqlalchemy as sql
import psycopg2
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import ForVK
from ResultCreation import Result

# DSN = 'postgres+psycopg2://postgres:q*4@localhost:5432/postgres'
# DSN = 'postgres+psycopg2://diplom:0*0@localhost:5432/diplom'
DSN = 'postgres+psycopg2://diplom:0*0@localhost:5432/diplom'

BASE = declarative_base()

engine = sql.create_engine(DSN)
Session = sessionmaker(bind=engine)

session = Session()
# BASE.metadata.create_all(engine)

class Users(BASE):
    __tablename__ = 'Users'
    id = sql.Column(sql.Integer, primary_key = True)#Имеем в виду то, что ид в базе данных = ид в вк

    first_name = sql.Column(sql.String)
    last_name = sql.Column(sql.String)
    sex = sql.Column(sql.Integer)
    country_code = sql.Column(sql.Integer)
    city_code = sql.Column(sql.Integer)


    age = sql.Column(sql.Integer)
    range_age = sql.Column(sql.String)

    dating_users = relationship('DatingUser', backref = 'user')
class DatingUser(BASE):
    __tablename__ = 'DatingUser'
    id = sql.Column(sql.Integer, primary_key=True)

    first_name = sql.Column(sql.String)
    last_name = sql.Column(sql.String)
    age = sql.Column(sql.Integer)
    interest = sql.Column(sql.Boolean)

    id_user = sql.Column(sql.Integer, sql.ForeignKey('Users.id'))
    id_photos = relationship('Photos', backref = 'DatingUser')
class Photos(BASE):
    __tablename__ = 'Photos'
    id = sql.Column(sql.Integer, primary_key=True)

    link = sql.Column(sql.String)
    count_likes = sql.Column(sql.Integer)

    id_DatingUser = sql.Column(sql.Integer, sql.ForeignKey('DatingUser.id'))


def add_user_in_DataBase(VKuser):
    Session().commit()
    DBuser = Session().query(Users).filter(id==VKuser.id).first()
    Session().commit()
    print(f'>>>>>>>>>>>>>>>>>>>>>>>>>>DBuser:{DBuser}')

    # if DBuser == None:
    #     DBuser = Users(id=VKuser.id, first_name=VKuser.firs_name, last_name=VKuser.last_name, sex=VKuser.sex,
    #                   country_code=VKuser.country_code['id'], city_code = VKuser.city_code['id'], age=VKuser.age,
    #                   range_age=f'[{VKuser.age_from}-{VKuser.age_to}')
    #     session.add(DBuser)
    #     session.commit()
    #     result = Result(0, 'Получение информации о пользователе из базы данных', 'Пользователь добавлен в БД')
    #     result.print_result()
    # else:
    #     result = Result(0, 'Получение информации о пользователе из базы данных', 'Пользователь найден в БД')
    #     result.print_result()
    # return [DBuser, result]


def add_person(VKuser_id, VKperson, VKinterest):
    DBperson = Session().query(DatingUser).filter(id = VKperson.id).first()
    print(f'>>>>>>>>>>>>>>>>>>>>>>>>DBperson:{DBperson}')

    if DBperson == None:
        DBperson = DatingUser(id=VKperson.id, first_name=VKperson.first_name, last_name=VKperson.last_name, age=VKperson.age, id_user=VKuser_id, interest=VKinterest)
        DBlist_photos = []
        for VKphoto in VKperson.list_photos:
            DBphoto = Photos(id=VKphoto.id, link= VKphoto.link_photo, count_likes=VKphoto.likes, id_DatingUser=DBperson.id)
            DBlist_photos.append(DBlist_photos)

        session.add(DBperson)
        session.add_all(DBlist_photos)
        session.commit()
        result = Result(0, 'Загрузка данных DatingUser, Photos в БД', 'Информация загружена в БД')
        result.print_result()
        return result
    else:
        result = Result(0, 'Загрузка данных DatingUser, Photos в БД', 'Информация найдена в БД')
        result.print_result()
        return result

def create_metadata():
    BASE.metadata.create_all(engine)

#
# import sqlalchemy as sql
# import psycopg2
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship, sessionmaker
# import ForVK
# from ResultCreation import Result
#
# BASE = declarative_base()
# # DSN = 'postgres+psycopg2://postgres:q**4@localhost:5432/postgres'
# DSN = 'postgres+psycopg2://diplom:012370@localhost:5432/diplom'
#
# # engine = sql.create_engine(DSN)
# # Session = sessionmaker(bind=engine)
# # session = Session()
#
# class Users(BASE):
#     __tablename__ = 'Users'
#     id = sql.Column(sql.Integer, primary_key = True)#Имеем в виду то, что ид в базе данных = ид в вк
#
#     first_name = sql.Column(sql.String)
#     last_name = sql.Column(sql.String)
#     sex = sql.Column(sql.Integer)
#     country_code = sql.Column(sql.Integer)
#     city_code = sql.Column(sql.Integer)
#
#
#     age = sql.Column(sql.Integer)
#     range_age = sql.Column(sql.String)
#
#     dating_users = relationship('DatingUser', backref = 'user')
#
#
# class DatingUser(BASE):
#     __tablename__ = 'DatingUser'
#     id = sql.Column(sql.Integer, primary_key=True)
#
#     first_name = sql.Column(sql.String)
#     last_name = sql.Column(sql.String)
#     age = sql.Column(sql.Integer)
#     interest = sql.Column(sql.Boolean)
#
#     id_user = sql.Column(sql.Integer, sql.ForeignKey('Users.id'))
#     id_photos = relationship('Photos', backref = 'DatingUser')
#
# class Photos(BASE):
#     __tablename__ = 'Photos'
#     id = sql.Column(sql.Integer, primary_key=True)
#
#     link = sql.Column(sql.String)
#     count_likes = sql.Column(sql.Integer)
#
#     id_DatingUser = sql.Column(sql.Integer, sql.ForeignKey('DatingUser.id'))
#
# def init_session_with_DataBase():
#     engine = sql.create_engine(DSN)
#     # BASE.metadata.create_all(engine)
#
#     Session = sessionmaker(bind=engine)
#     session = Session()
#
#
#     session.commit()
#
#     return session
#
#
# def add_user_in_DataBase(VKuser, session):
#
#     DBuser = session.query(Users).filter(id==VKuser.id).all()
#     print(f'>>>>{DBuser}')
#     result = Result(1, 'Получение информации о пользователе из базы данных', 'Пользователь найден в БД')
#     if DBuser == None:
#         DBuser = Users(id=VKuser.id, first_name=VKuser.firs_name, last_name=VKuser.last_name, sex=VKuser.sex,
#                       country_code=VKuser.country_code['id'], city_code = VKuser.city_code['id'], age=VKuser.age,
#                       range_age=f'[{VKuser.age_from}-{VKuser.age_to}')
#
#     session.add(DBuser)
#     session.commit()
#
#     result = Result(1, 'Получение информации о пользователе из базы данных', 'В БД создан новый пользователь')
#     result.print_result()
#     return [DBuser, result]
#
#
# def add_person(session, VKuser_id, VKperson, VKinterest):
#     DBperson = DatingUser(id=VKperson.id, first_name=VKperson.first_name, last_name=VKperson.last_name, age=VKperson.age, id_user=VKuser_id, interest=VKinterest)
#     DBlist_photos = []
#     for VKphoto in VKperson.list_photos:
#         DBphoto = Photos(id=VKphoto.id, link= VKphoto.link_photo, count_likes=VKphoto.likes, id_DatingUser=DBperson.id)
#         DBlist_photos.append(DBlist_photos)
#
#     session.add(DBperson)
#     session.add_all(DBlist_photos)
#     session.commit()
#
#     result = Result(1, 'Загрузка данных DatingUser, Photos в БД', 'Информация загружена')
#     result.print_result()
#     return Result(1, 'Загрузка данных DatingUser, Photos в БД', 'Информация загружена')
#
# def create_metadata():
#     BASE.metadata.create_all(engine)