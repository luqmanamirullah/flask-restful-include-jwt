from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

class Model(BaseModel):
  def to_json(self) -> str:
    return jsonable_encoder(self)
  
  def to_bson(self) -> dict:
    data = self.dict(by_alias=True, exclude_none=True)
    if data.get("_id") == None:
      data.pop("_id", None)
    return data      