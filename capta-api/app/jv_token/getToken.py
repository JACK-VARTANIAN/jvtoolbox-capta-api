import jwt
import datetime
import os

from config.authentication import auth_required
from flask import jsonify
from flask_restful import Resource, request

from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

class getToken(Resource):
      @auth_required
      def get(self):
         token = jwt.encode({'user':request.authorization.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, SECRET_KEY)
         return jsonify({'token': token})

