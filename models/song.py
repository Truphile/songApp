from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from repositories.database import Base


class song(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200),nullable=False)
    artist = Column(String(200),nullable=False)

    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("user", back_populates="songs")