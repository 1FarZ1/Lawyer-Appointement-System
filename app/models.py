from sqlalchemy import Column, Integer, String, ForeignKey, Float, Enum
from app.config.database import Base
from sqlalchemy.orm import relationship




class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    fname = Column(String(255),)
    lname = Column(String(255))
    email = Column(String(255), unique=True)
    hashed_password = Column(String(255))    
    lawyer = relationship("Lawyer", back_populates="user")
    review = relationship("Review", back_populates="user")
    appointement = relationship("Appointement", back_populates="user")
#    createdAt = Column(dt.Datetime)

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




class Lawyer(Base):
   __tablename__ = "lawyer"
   id = Column(Integer, primary_key=True, index=True, autoincrement=True)
   phone = Column(String(30))
   address = Column(String(255))
   description = Column(String(255))
   avocat_image = Column(String(255), default="https://www.pngitem.com/pimgs/m/146-1468479_my-profile-icon-blank-profile-picture-circle-hd.png")
   rating = Column(Float, default=0)
   social = Column(String(255))
   wilaya = Column(String(50))
   longitude = Column(Float)
   latitude = Column(Float)  
   status = Column(String(50), default="pending")  
   ##status = Column(Enum('pending', 'approved', 'rejected', name='lawyer_status'))
   user_id = Column(Integer, ForeignKey('user.id'))
   user = relationship("User", back_populates="lawyer")
   review = relationship("Review", back_populates="lawyer")
   
   categorie_id = Column(Integer, ForeignKey('categorie.id'))
   categorie = relationship("Categorie", back_populates="lawyer")

   appointement = relationship("Appointement", back_populates="lawyer")






class Categorie(Base):
   __tablename__ = "categorie"
   id = Column(Integer, primary_key=True, index=True, autoincrement=True)
   name = Column(String(50))
   lawyer = relationship("Lawyer", back_populates="categorie") 




class Appointement(Base):
    __tablename__ = "appointement"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    date = Column(String(50))
    time = Column(String(50))
    status = Column(String(50), default="pending")
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="appointement")
    lawyer_id = Column(Integer, ForeignKey('lawyer.id'))
    lawyer = relationship("Lawyer", back_populates="appointement")