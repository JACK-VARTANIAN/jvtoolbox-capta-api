import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from .models import ProductsModel

class ProductsType(SQLAlchemyObjectType):
    pk = graphene.String(source="cpros")

    class Meta:
        model = ProductsModel
        interfaces = (relay.Node,)