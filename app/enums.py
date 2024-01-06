


# enum for roles
from enum import Enum


class RoleEnum(str,Enum):
    ADMIN = "admin"
    LAWYER = "lawyer"
    USER = "user"


## create  enum for status : Approved,  Rejected , Pending

class StatusEnum(str,Enum):
    APPROVED = "approved"
    REJECTED = "rejected"
    PENDING = "pending"