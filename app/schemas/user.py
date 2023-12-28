from pydantic import BaseModel

class UserDto(BaseModel):
    fname: str
    lname: str
    email: str
    password: str
    
