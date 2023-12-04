from sqlalchemy import Column, Integer, String, Float
from database import Base

# class Item(BaseModel):
#     """
#     Represents an item with a name, description, price, and tax.

#     Attributes:
#         name (str): The name of the item.
#         description (str): The description of the item.
#         price (float): The price of the item.
#         tax (float): The tax rate applied to the item.
#     """
#     name: str
#     description: str 
#     price: float
#     tax: float


class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)