from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, Session, sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(os.environ.get('DB_URL'), echo=True)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(50), nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"
    
    @classmethod # cls è esattamente come il self nei classmethods
    def add_user(cls, username, email, password):
        Base.metadata.create_all(engine) # crea la tabella se non esiste
        session = Session(bind=engine)
        user = cls(username=username, email=email, password=password)
        session.add(user)
        session.commit()
        session.close()
