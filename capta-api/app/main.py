import os
from flask import Flask
from flask_restful import Api

from app.api.getToken import getToken
from app.api.productInfo import productInfo
from app.api.productStock import productStock
from app.api.customerInfo import customerInfo

from app.config.connection import connection
from app.config.database.db_session import db_session
from app.api.schema.schema import schema

conn = connection()


@app.route("/")
def index():
   return 'Hello World'


app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)

api = Api(app)

connDB = {"conn":conn}


# app.add_url_rule('/graphql', 
#                   view_func=GraphQLView.as_view(
#                      'graphql', 
#                      schema=schema, 
#                      graphiql=True
#                   ))






api.add_resource(getToken, "/api/getToken")

api.add_resource(productStock, "/api/products_stock", resource_class_kwargs=connDB)

api.add_resource(productInfo, "/api/products_by_cpros/<string:reference>", endpoint="products_by_cpros", resource_class_kwargs=connDB)
api.add_resource(productInfo, "/api/products_by_colecoes/<string:reference>", endpoint="products_by_colecoes", resource_class_kwargs=connDB)
api.add_resource(productInfo, "/api/products_by_cgrus/<string:reference>", endpoint="products_by_cgrus", resource_class_kwargs=connDB)

api.add_resource(customerInfo, "/api/customer_by_iclis/<string:customer>", endpoint="customer_by_iclis", resource_class_kwargs=connDB)


