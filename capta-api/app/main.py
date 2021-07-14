import os
from flask import Flask
from flask_restful import Api

from app.api.getToken import getToken
from app.api.productInfo import productInfo
from app.api.productStock import productStock
from app.api.customerInfo import customerInfo

from app.connection import connection

def start_app(testing: bool = True):
   app = Flask(__name__)
   app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
   conn = connection()
   
   @app.route("/")
   def index():
      return 'Hello World'


   api = Api(app)

   connDB = {"conn":conn}
   api.add_resource(getToken, "/api/getToken")

   api.add_resource(productStock, "/api/stock/<string:reference>", resource_class_kwargs=connDB)

   api.add_resource(productInfo, "/api/products_by_cpros/<string:reference>", endpoint="products_by_cpros", resource_class_kwargs=connDB)
   api.add_resource(productInfo, "/api/products_by_colecoes/<string:reference>", endpoint="products_by_colecoes", resource_class_kwargs=connDB)
   api.add_resource(productInfo, "/api/products_by_cgrus/<string:reference>", endpoint="products_by_cgrus", resource_class_kwargs=connDB)

   api.add_resource(customerInfo, "/api/customer_by_iclis/<string:customer>", endpoint="customer_by_iclis", resource_class_kwargs=connDB)


   return app

