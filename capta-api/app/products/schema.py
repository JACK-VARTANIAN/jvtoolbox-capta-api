import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField

from .models import ProductsModel as Products
from .serializer import ProductsType


class Query(graphene.ObjectType):
    products = SQLAlchemyConnectionField(ProductsType.connection)
    product = graphene.Field(ProductsType, pk = graphene.String())

    @classmethod
    def resolve_products(cls, _, info, *args, **kwargs):
        return  Products.query.all()

    @classmethod
    def resolve_products_by_cpros(cls, _, info, pk, *args, **kwargs):
        return Products.query.filter_by(cpros=pk)
