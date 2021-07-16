import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from app.api.models.Products import Products as ProductsModel

class Products(SQLAlchemyObjectType):
    class Meta:
        model = ProductsModel
        interfaces = (graphene.relay.Node,)

class ProductsAttribute:
    cpros = graphene.String()
    qtds = graphene.Float()
    empos = graphene.String()
    rclis = graphene.String()