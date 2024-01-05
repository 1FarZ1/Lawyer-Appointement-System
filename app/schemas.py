from pydantic import BaseModel
from typing import List, Optional


class LoginSchema(BaseModel):
    email: str
    password: str

class GoogleUserSchema(BaseModel):
    fname: str
    lname: str
    email: str
    password: Optional[str] = None
    

class LawyerUserSchema(BaseModel):
    fname: str
    lname: str
    email: str
    password: Optional[str] = None
    phone : str
    address : str
    description : str
    # schedule : List[str]
    social : str
    wilaya : str
    longitude : float
    latitude : float
    categorie_id : int
    user_id : int

class LawyerSchema(BaseModel) :
    phone : str
    address : str
    description : str
    # schedule : List[str]
    social : str
    wilaya : str
    longitude : float
    latitude : float
    categorie_id : int
    user_id : int
    
    

class ReviewSchema(BaseModel):
    rating : int
    lawyer_id : int
    description : str

class AppointementSchema(BaseModel):
    lawyer_id : int
    date:str
    time:str



##  Lawyer 
## 