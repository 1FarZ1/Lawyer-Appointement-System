import inspect
from fastapi import Form
from pydantic import BaseModel,Field
from typing import Annotated, Dict, List, Optional


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
    

def as_form(cls):
    new_params = [
        inspect.Parameter(
            field_name,
            inspect.Parameter.POSITIONAL_ONLY,
            default=model_field.default,
            annotation=Annotated[model_field.annotation, model_field.metadata, Form()],
        )
        for field_name, model_field in cls.model_fields.items()
    ]

    cls.__signature__ = cls.__signature__.replace(parameters=new_params)

    return cls

# @as_form
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
    wilaya_id : str
    city_id:str
    longitude : str
    latitude : str
    categorie_id : str

class LawyerUserSchemaForm:
    def __init__(
        self,
        fname: str = Form(...),
        lname: str = Form(...),
        email: str = Form(...),
        password: str = Form(...),
        phone : str = Form(...),
        address : str = Form(...),
        description : str = Form(...),
        ## MAKE THE schedule like this [{time:"tt",day"monday"},{time:"tt",day"friday"}]
        # schedule: List[str] = Form(...),  # Accept as a list of dictionaries
        social : str = Form(...),
        wilaya_id : str = Form(...),
        city_id:str = Form(...),
        longitude : str = Form(...),
        latitude : str = Form(...),
        categorie_id : str = Form(...),

    ):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password = password
        self.phone = phone
        self.address = address
        self.description = description
        # self.schedule = schedule
        self.social = social
        self.wilaya_id = wilaya_id
        self.city_id = city_id
        self.longitude = longitude
        self.latitude = latitude
        self.categorie_id = categorie_id


        ## to string
    def __repr__(self):
        return f"User({self.fname!r}, {self.lname!r}, {self.email!r}, {self.password!r}, {self.phone!r}, {self.address!r}, {self.description!r}, {self.social!r}, {self.wilaya_id!r}, {self.city_id!r}, {self.longitude!r}, {self.latitude!r}, {self.categorie_id!r})"
    

class LawyerInfoSchema(BaseModel):
    phone : str
    address : str
    description : str
    # schedule : List[str]
    social : str
    certificat_url:str
    wilaya_id : str
    city_id : str
    longitude : str
    latitude : str
    categorie_id : str




    

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
    day:str
    time:str
    date:str



class CheckEmailSchema(BaseModel):
    email: str




##  Lawyer 
## 