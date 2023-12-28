
# from sqlalchemy import Column, Integer, String, ForeignKey
# from app.config.database import Base
# from sqlalchemy.orm import relationship


# class Category(Base):
#    __tablename__ = "categorie"
#    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
#    name = Column(String(50))
#    lawyers = relationship("Lawyer", back_populates="categorie")
# ## description = Column(String(255))
# ## image = Column(String(255))
# ## icon = Column(String(255))
# ## parent_id = Column(Integer,ForeignKey('Categories.id'),nullable=True)
# ## parent = relationship("Category", backref="children", remote_side=[id])
# ## children = relationship("Category")
# ## lawyers = relationship("Lawyer", back_populates="category")
