from flask import request
from flask_api import status
from functools import wraps
from ..helper.response import response_error
from ..helper.jwt import verify
from ..config.database.mongodb import db
import traceback
from bson.objectid import ObjectId

def token_required(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    token = None
    if 'Authorization' in request.headers:
      token = request.headers['Authorization'].split(' ')[1]
    if not token:
      return response_error('Forbidden, aunthentication token is missing!', status.HTTP_403_FORBIDDEN)
    
    try:
      print('token', token)
      decoded=verify(token)
      if decoded is None:
        return response_error('Unauthorized!', status.HTTP_401_UNAUTHORIZED)
      print('decoded', decoded)
      current_user = db.users.find_one({'_id': ObjectId(decoded['sub'])})
      print('current_user', current_user)
      if current_user is None:
        return response_error('Token invalid', status.HTTP_403_FORBIDDEN)
    except Exception as e:
      traceback.print_exc()
      print('error verify', e)
      return response_error('Internal server error', status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return f(*args, current_user, **kwargs)

  return decorated
      
      

