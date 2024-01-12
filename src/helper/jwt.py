import jwt
from ..config import config
import traceback
def verify(token):
  try:
    return jwt.decode(token, config['JWT_SECRET'], algorithms=["HS256"])
  except Exception as e:
    traceback.print_exc()
    print('error verify', e)
    return None
