import os
from flask import Flask
from flask_restful import Api
from flask_graphql import GraphQLView
from schemas.products import schema
from jv_token import getToken

from database.db_session import db_session
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


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


# api = Api(app)
# api.add_resource(getToken, "/api/getToken")


# api.add_resource(productStock, "/api/products_stock", resource_class_kwargs=connDB)

# api.add_resource(productInfo, "/api/products_by_cpros/<string:reference>", endpoint="products_by_cpros", resource_class_kwargs=connDB)
# api.add_resource(productInfo, "/api/products_by_colecoes/<string:reference>", endpoint="products_by_colecoes", resource_class_kwargs=connDB)
# api.add_resource(productInfo, "/api/products_by_cgrus/<string:reference>", endpoint="products_by_cgrus", resource_class_kwargs=connDB)

# api.add_resource(customerInfo, "/api/customer_by_iclis/<string:customer>", endpoint="customer_by_iclis", resource_class_kwargs=connDB)


