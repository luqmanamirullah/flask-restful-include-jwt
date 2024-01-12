from . import Service
from ..dto.user_dtos import UserLoginDto, CreateUserDto, UserDto
import bcrypt
class Auth(Service):
  def __init__(self):
    super(Auth, self).__init__() 
    self.bcrypt = bcrypt
  
  def login(self, user: UserLoginDto):
    try:
      print('data nya bos', user.to_json())

      data = self.db.users.find_one({"email": user.email})
      if data == None:
        return self.response_error('User is not registered', self.status.HTTP_404_NOT_FOUND)
      
      # TODO: matching password 
      password = user.password.encode('utf-8')
      match = self.bcrypt.checkpw(password, data['password'].encode('utf-8'))
      if not match:
        return self.response_error('Wrong password', self.status.HTTP_400_BAD_REQUEST)
            
      access_token = self.generate_token({
        "sub": str(data['_id']),
        "name": data['name'],
        "email": data['email'],
      })
      if access_token == None:
        return self.response_error('Internal Server Error', self.status.HTTP_500_INTERNAL_SERVER_ERROR)

      
      # NOTE: refresh token = hashed access token 
      salt = self.bcrypt.gensalt()
      refresh_token = self.bcrypt.hashpw(password=access_token.encode('utf-8'), salt=salt)
      exp = self.datetime.datetime.utcnow() + self.datetime.timedelta(days=30)
      self.db.users.update_one({"_id": data['_id']}, {"$set": {"refresh_token": refresh_token}})

      # TODO & NOTE: set refresh token to cookie with httponly
      
      self.response.Response().set_cookie(
        key='refresh_token',
        value=refresh_token,
        max_age=None,
        expires=exp,
        httponly=True,
      )
  
      return self.response_success('Login success', {
        "access_token": access_token,
      }, self.status.HTTP_200_OK)     

    except Exception as e:
      self.traceback.print_exc()
      print('error nya bos', e)
      return self.response_error('Internal Server Error', self.status.HTTP_500_INTERNAL_SERVER_ERROR)  


  def register(self, user: CreateUserDto):
    try:
      print('data nya bos', user.to_json())
      
      # NOTE: hash password
      password = user.password.encode('utf-8')
      salt = self.bcrypt.gensalt()
      hashed = self.bcrypt.hashpw(password, salt)
      user.password = hashed
      
      # NOTE: email  is ready to use because it has been validated in CreateUserDto
      # NOTE: insert to db
      self.db.users.insert_one(user.to_json())

      return self.response_success('Register success', None, self.status.HTTP_201_CREATED)
    except Exception as e:
      self.traceback.print_exc()
      print('error nya bos', e)
      return self.response_error('Internal Server Error', self.status.HTTP_500_INTERNAL_SERVER_ERROR)  

      
  def logout(self, user: UserDto):
    try:
      self.response.Response.delete_cookie(self.response.Response(), key='refresh_token', httponly=True)
      self.db.users.update_one({"_id": user.id}, {"$set": {"refresh_token": None}})
      return self.response_success('Logout success', None, self.status.HTTP_200_OK)
    except Exception as e:
      self.traceback.print_exc()
      print('error nya bos', e)
      return self.response_error('Internal Server Error', self.status.HTTP_500_INTERNAL_SERVER_ERROR)  
    

  # NOTE: this just for testing jwt, me data can be accessed with request to this endpoint, fe can decode the access_token and get the data
  def me(self, current_user: UserDto):
    try:
      return self.response_success('Get me success', current_user.to_json(), self.status.HTTP_200_OK)
    except Exception as e:
      self.traceback.print_exc()
      print('error nya bos', e)
      return self.response_error('Internal Server Error', self.status.HTTP_500_INTERNAL_SERVER_ERROR)