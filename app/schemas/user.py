from pydantic import BaseModel

class UserDto(BaseModel):
    username: str
    email: str
    password: str
