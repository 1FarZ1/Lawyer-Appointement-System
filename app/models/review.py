
from sqlalchemy import Column, Integer, String, ForeignKey
from app.config.database import Base
from sqlalchemy.orm import relationship

class Review (Base):
    __tablename__ = "review"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    lawyer_id = Column(Integer, ForeignKey('lawyer.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    lawyer = relationship("Lawyer", back_populates="review")
    user = relationship("User", back_populates="review")
    rating = Column(Integer)
    description = Column(String(255))
    # user = relationship("User", back_populates="reviews")
    # lawyer = relationship("Lawyer", back_populates="reviews")