from app.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
import bcrypt

salt = bcrypt.gensalt()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(20), nullable=False)
    location = Column(String(20), nullable=False)
    description = Column(String(500))
    occupation = Column(String(20), nullable=False)

    @validates('username')
    def validate_email(self, key, username):
        assert len(username) > 5

        return username

    @validates('email')
    def validate_email(self, key, email):
        assert '@' in email

        return email

    @validates('password')
    def validate_password(self, key, password):
        assert len(password) > 5

        return bcrypt.hashpw(password.encode('utf-8'), salt)