from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from repositories.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(255))
    email = Column(String(255), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)

    role = Column(String(50), default="user")

    songs = relationship("Song", back_populates="owner")