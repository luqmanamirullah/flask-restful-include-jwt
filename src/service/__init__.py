from ..config.database.mongodb import db
import os
import datetime
import traceback
import jwt
from ..config import config
from ..dto.auth_dtos import JwtPayloadDto
from ..helper.response import response_success, response_error
from flask_api import status, response

class Service(object):
  def __init__(self):
    self.db = db
    self.os = os
    self.datetime = datetime
    self.traceback = traceback
    self.response_success = response_success
    self.response_error = response_error
    self.status = status
    self.response = response

  
  def generate_token(self, payload):
    try:
      payload = JwtPayloadDto(**payload)
      print('payload', payload)
      return jwt.encode(payload.to_bson(), config['JWT_SECRET'], algorithm="HS256")
    except Exception as e:
      self.traceback.print_exc()
      print('error generate token', e)
      return None
    

    