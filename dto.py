from pydantic import BaseModel

class UserDto(BaseModel):
    username: str
    password: str