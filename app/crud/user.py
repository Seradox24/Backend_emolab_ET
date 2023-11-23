# app/crud/user.py
from sqlalchemy.orm import Session
from app.db.models import User

def create_user(db: Session, full_name: str, email: str, username: str, password: str):
    hashed_password = hash_password(password)
    db_user = User(full_name=full_name, email=email, username=username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()
