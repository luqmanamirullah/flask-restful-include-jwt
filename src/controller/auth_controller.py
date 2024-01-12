from ..service.auth_service import Auth
from ..controller import Controller
from ..dto import user_dtos
from pydantic_core import ValidationError
from ..middleware.auth_middleware import token_required
class AuthController(Controller):
  def __init__(self):
    super(AuthController, self).__init__()
    self.auth = Auth()

  def login(self):    
    raw_user = self.request.get_json()

    try:
      # NOTE: validate payload
      user = user_dtos.UserLoginDto(**raw_user)

      return self.auth.login(user)
    except ValidationError as e:
      print(e)
      error_message = e.errors()[0]['msg']
      return self.response_error(error_message, self.status.HTTP_400_BAD_REQUEST)
    except Exception as e:
      print('error nya bos', e)
      return self.response_error("Internal Server Error", self.status.HTTP_500_INTERNAL_SERVER_ERROR)


  def register(self):
    raw_user = self.request.get_json()
    print('raw user', raw_user)

    try:
      # NOTE: validate payload
      user = user_dtos.CreateUserDto(**raw_user)

      return self.auth.register(user)
    except ValidationError as e:
      print(e)
      error_message = e.errors()[0]['msg']
      return self.response_error(error_message, self.status.HTTP_400_BAD_REQUEST)
    except Exception as e:
      print('error nya bos', e)
      return self.response_error("Internal Server Error", self.status.HTTP_500_INTERNAL_SERVER_ERROR)

  # NOTE: this just for testing jwt, me data can be accessed with request to this endpoint, fe can decode the access_token and get the data
  @token_required
  def me(self, current_user):
    try:
      user = user_dtos.UserDto(**current_user)
      print('user', user)
      return self.auth.me(user)
    except Exception as e:
      print('error nya bos', e)
      return self.response_error("Internal Server Error", self.status.HTTP_500_INTERNAL_SERVER_ERROR)  

  @token_required
  def logout(self, current_user):
    try:
      user = user_dtos.UserDto(**current_user)
      return self.auth.logout(user)
    except Exception as e:
      print('error nya bos', e)
      return self.response_error("Internal Server Error", self.status.HTTP_500_INTERNAL_SERVER_ERROR)