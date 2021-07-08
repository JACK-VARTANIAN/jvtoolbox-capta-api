import os
from flask import Flask
from flask_restful import Api

from app.api.getToken import getToken
from app.api.productInfo import productInfo
from app.api.productStock import productStock
from app.api.customerInfo import customerInfo

def start_app(testing: bool = True):
   app = Flask(__name__)
   app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

   
   @app.route("/")
   def index():
      return 'Hello World'


   api = Api(app)
   api.add_resource(getToken, "/api/getToken")

   api.add_resource(productStock, "/api/stock/<string:reference>")

   api.add_resource(productInfo, "/api/products_by_cpros/<string:reference>", endpoint="products_by_cpros")
   api.add_resource(productInfo, "/api/products_by_colecoes/<string:reference>", endpoint="products_by_colecoes")
   api.add_resource(productInfo, "/api/products_by_cgrus/<string:reference>", endpoint="products_by_cgrus")

   api.add_resource(customerInfo, "/api/customer_by_iclis/<string:customer>", endpoint="customer_by_iclis")



   return app

