import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Enum,Boolean,DateTime,JSON
from app.config.database import Base
from sqlalchemy.orm import relationship
from app.enums import RoleEnum, StatusEnum





class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    fname = Column(String(255),)
    lname = Column(String(255))
    email = Column(String(255), unique=True)
    password = Column(String(255),nullable=True)
    createdAt = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    #updatedAt = Column(DateTime(timezone=True), onupdate=func.now())
    role = Column(Enum(RoleEnum), default="user")
    lawyer = relationship("Lawyer", back_populates="user",lazy='joined' )
    review = relationship("Review", back_populates="user")
    appointement = relationship("Appointement", back_populates="user")

class Review (Base):
    __tablename__ = "review"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    description = Column(String(255))
    rating = Column(Integer)
    lawyer_id = Column(Integer, ForeignKey('lawyer.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    lawyer = relationship("Lawyer", back_populates="review")
    user = relationship("User", back_populates="review",lazy='joined')




class Lawyer(Base):
   __tablename__ = "lawyer"
   id = Column(Integer, primary_key=True, index=True, autoincrement=True)
   phone = Column(String(30))
   address = Column(String(255))
   description = Column(String(255))
   image = Column(
        String(255),
        default="https://www.pngitem.com/pimgs/m/146-1468479_my-profile-icon-blank-profile-picture-circle-hd.png",
   )
   social = Column(String(255))
   wilaya_id = Column(
        Integer,
   )
   city_id = Column(
        Integer,
   )
    ## certificat_url 
   certificat_url =  Column( String(255),)
   longitude = Column(Float)
   latitude = Column(Float)  
   rating = Column(Float, default=0)
   n_reviews = Column(Integer, default=0)
   status = Column(String(50), default="pending")  
   status = Column(Enum(StatusEnum), name='lawyer_status',default=StatusEnum.PENDING)
   experience = Column(String(50))
   user_id = Column(Integer, ForeignKey('user.id'))
   user = relationship("User", back_populates="lawyer", lazy='joined')
   review = relationship("Review", back_populates="lawyer")
   categorie_id = Column(Integer, ForeignKey('categorie.id'))
   categorie = relationship("Categorie", back_populates="lawyer",lazy='joined')
   appointement = relationship("Appointement", back_populates="lawyer")
   lawyer_schedule = relationship("LawyerSchedule", back_populates="lawyer",lazy='joined')


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
    day = Column(String(50))
    status = Column(String(50), default="pending")
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="appointement")
    lawyer_id = Column(Integer, ForeignKey('lawyer.id'))
    lawyer = relationship("Lawyer", back_populates="appointement")



## a Schedule Class 

# class Schedule(Base):
#     __tablename__ = "schedule"
#     id = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     date = Column(String(50))
#     time = Column(String(50))
#     lawyer_id = Column(Integer, ForeignKey('lawyer.id'))
#     lawyer = relationship("Lawyer", back_populates="schedule")
    

class LawyerSchedule(Base):
    __tablename__ = 'lawyer_schedule'

    id = Column(Integer, primary_key=True)
    lawyer_id = Column(Integer)
    day_of_week = Column(String(200))
    start_time = Column(String(200))
    end_time = Column(String(200))
    lawyer_id = Column(Integer, ForeignKey('lawyer.id'))
    lawyer = relationship("Lawyer", back_populates="lawyer_schedule")

