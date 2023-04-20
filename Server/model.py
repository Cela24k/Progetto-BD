from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, Session, sessionmaker

engine = create_engine('sqlite://', echo=True)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(50), nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"
    
    @classmethod
    async def add_user(cls, username, email, password):
        Session = sessionmaker(bind=engine)
        session = Session
        user = cls(username=username, email=email, password=password) # cls is needed to make this method work in subclasses
        session.add(user)
        session.commit()
        session.close()