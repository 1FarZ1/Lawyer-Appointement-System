from pydantic import BaseModel,Field
from typing import List, Optional


class LoginSchema(BaseModel):
    email: str
    password: str

class GoogleUserSchema(BaseModel):
    fname: str
    lname: str
    email: str
    



class LUserSchema(BaseModel):
    fname: str
    lname: str
    email: str
    password: str 
    


class LawyerUserSchema(BaseModel):
    fname: str
    lname: str
    email: str
    password: str 
    phone : str
    address : str
    description : str
    # schedule : List[str]
    social : str
    wilaya : str
    city:str
    longitude : float
    latitude : float
    categorie_id : int
    user_id : int

class LawyerInfoSchema(BaseModel):
    phone : str
    address : str
    description : str
    # schedule : List[str]
    social : str
    wilaya : str
    city : str
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
    ## rating will be between 1 and 5
    rating: int = Field(
        ...,
        gt=0,
        le=5
    )
    lawyer_id : int
    description : str

class AppointementSchema(BaseModel):
    lawyer_id : int
    date:str
    time:str


class CheckEmailSchema(BaseModel):
    email: str




##  Lawyer 
## 