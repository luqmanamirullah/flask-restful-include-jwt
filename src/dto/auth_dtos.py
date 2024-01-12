from pydantic import Field
from time import time
from typing import Optional
from . import Model
class JwtPayloadDto(Model):
    sub: str = Field(...)
    name: str = Field(...)
    email: str = Field(...)
    exp: Optional[int]= int(time() + 60 * 15) # 15 minutes
