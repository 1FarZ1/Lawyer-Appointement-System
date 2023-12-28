from pydantic import BaseModel
from typing import List

class LawyerDto(BaseModel) :
    name : str
    fname : str
    email : str
    phone : str
    address : str
    description : str
    avocat_image : str
    # schedule : List[str]
    rating : float
    # comments : List[str]
    social : str
    wilaya : str
    longitude : float
    latitude : float
    categories_id : int
    
    