from pydantic_core import PydanticCustomError
from ..config.database.mongodb import db
def email(email: str) -> str:
    if '@' not in email:
      raise PydanticCustomError(
         'invalid email',
         'Email must be a valid email',
         {'email': email}
      )
    return email

def newEmail(newMail: str, collection: str = 'users') -> str:
    email(newMail)
    data = db[collection].find_one({'email': newMail})
    if data:
      raise PydanticCustomError(
         'unique value',
         'email already exists',
         {'email': newMail}
      )
    return newMail

# if value is empty like '', None, False, 0, [], {}, ()
def notEmpty(value: str, field: str) -> str:
    if not value:
      raise PydanticCustomError(
         'required',
         f'{field} is required',
         {field: value}
      )
    return value