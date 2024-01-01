from pydantic import BaseModel
from typing import List, Optional


class LoginSchema(BaseModel):
    email: str
    password: str

class UserSchema(BaseModel):
    fname: str
    lname: str
    email: str
    password: Optional[str] = None
    image: str
    

class LawyerSchema(BaseModel) :
    phone : str
    address : str
    description : str
    # schedule : List[str]
    # rating : float
    # comments : List[str]
    social : str
    wilaya : str
    longitude : float
    latitude : float
    categorie_id : int
    user_id : int
    
    

class ReviewSchema(BaseModel):
    rating : int
    description : str
    lawyer_id : int
    user_id : int

class AppointementSchema(BaseModel):
    lawyer_id : int
    date:str
    time:str



##  Lawyer 
## 