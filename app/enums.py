


# enum for roles
from enum import Enum


class RoleEnum(str,Enum):
    ADMIN = "admin"
    LAWYER = "lawyer"
    USER = "user"
