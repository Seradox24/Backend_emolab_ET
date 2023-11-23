'''
from app.db.models import Base
from sqlalchemy import Column,Integer,String,Boolean,DateTime,ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class User(Base):
    __tablename__="user"
    id=column(Integer,primary_key=True, autoincrement=True)
    p_nombre=column(String)
    s_nombre=column(String)
    p_apellido=column(String)
    s_apellido=column(String)
    telefono=column(Integer)
    direccion=column(String)
    correo=column(String)
    creacion=column(DateTime,default=datetime.now,onupdate=datetime.now)
    estado=column(Boolean)


class TestTable(Base):
    __tablename__ = "test_table"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    p_nombre = Column(String)
    s_nombre = Column(String)
    p_apellido = Column(String)
    s_apellido = Column(String)
    telefono = Column(Integer)
    direccion = Column(String)
    correo = Column(String)
    creacion = Column(DateTime(timezone=True), server_default=func.now())
    estado = Column(Boolean)

class Presentation(Base):
    __tablename__ = "presentation"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    nombre = Column(String)  # nuevo campo de nombre
    url = Column(String)
    user = relationship("User", back_populates="presentations")



User.presentations = relationship("Presentation", order_by=Presentation.id, back_populates="user")

'''

# app/db/models.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from app.db.database import Base

Base = declarative_base()

class TestTable(Base):
    __tablename__ = "test_table"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

# app/db/models.py
from sqlalchemy import Column, Integer, String
from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)


# Agrega otras clases de modelo aquí...



