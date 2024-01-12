from src.dto import Model
from typing import Optional, Annotated
from pydantic import Field, field_validator as validator, ValidationInfo
from ..helper.pydantic import PydanticObjectId
from ..helper.validator import email, newEmail, notEmpty
from bson import ObjectId

class CreateUserDto(Model):
  name: str
  email: str
  password: str

  # validator unique email and valid email
  @validator('email')
  @classmethod
  def email_must_be_valid(cls, v: str) -> str:
    return newEmail(v)

  @validator('name', 'password', 'email')
  @classmethod
  def must_not_empty(cls, v: str, info:ValidationInfo ) -> str:
    return notEmpty(v, info.field_name)


class UpdateUserDto(Model):
  name: Optional[str]
  email: Optional[str]
  password: Optional[str]

class UserDto(Model):
  id: Optional[Annotated[ObjectId, PydanticObjectId]] = Field(None, alias="_id") 
  name: str = Field(...)
  email: str = Field(...)
  password: Optional[str] = Field(None, exclude=True)
  refresh_token: Optional[str] = Field(None, exclude=True)

  class Config:
    json_schema_extra = {
      "example": {
        "name": "John Doe",
        "email": "jhondoe@gmail.com",
        "password": "12345678", # this is not included in response
        "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM5IiwibmFtZSI6IkpvaG4gRG9lIiwiZW1haWwiOiJqb2huZG9lQGdtYWlsLmNvbSIsImV4cCI6MTY" # this is not included in response
      }
    }

class UserLoginDto(Model):
  email: str 
  password: str

  @validator('email')
  def email_must_be_valid(cls, v: str) -> str:
    return email(v)

  @validator('password')
  def password_must_not_empty(cls, v: str) -> str:
    return notEmpty(v, 'password')
