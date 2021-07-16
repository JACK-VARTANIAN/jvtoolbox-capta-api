import jwt
from flask import request, jsonify, make_response
from functools import wraps
import os
from dotenv import load_dotenv
load_dotenv()

USER_JV = os.getenv("USER_JV")
PASSWORD_JV = os.getenv("PASSWORD_JV")
SECRET_KEY = os.getenv("SECRET_KEY")

#BASIC AUTH
def auth_required(f):
   @wraps(f)
   def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and request.authorization.username == USER_JV and request.authorization.password == PASSWORD_JV:
           return f(*args, **kwargs)
      
        return make_response('Could not verify your login!', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})
   return decorated

#BEARER TOKEN
def token_required(f):
   @wraps(f)
   def decorated(*args, **kwargs):
      
      token=request.headers.get('Authorization', '').partition(' ')[2]
      if not token:
         return make_response(jsonify({'message':'Token is missing!'}), 401,{'WWW-Authenticate' : 'Bearer realm="Token Required"'})
      try:
         data = jwt.decode(token, SECRET_KEY, algorithms="HS256")
        
      except:
         return make_response(jsonify({'message':'Token is invalid'}), 401, {'WWW-Authenticate' : 'Bearer realm="Token Required"'})
   
      return f(*args, **kwargs)
   return decorated
