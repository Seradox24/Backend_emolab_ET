# database.py
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv() 

DATABASE_URL = "postgresql://fl0user:D0apdLeP8Jxj@ep-green-term-61680709.us-east-2.aws.neon.fl0.io:5432/panamdb?sslmode=require"

#DATABASE_URL = os.getenv('DATABASE_URL')
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# Más abajo en el archivo...
# Agrega la creación de las tablas y otros elementos necesarios

''' 
from dotenv import load_dotenv
import os
# app/db/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import databases

# Utilizar variables de entorno para la URL de la base de datos
load_dotenv()  # Carga las variables de entorno desde el archivo .env

DATABASE_URL = os.getenv('DATABASE_URL')


database = databases.Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

'''

