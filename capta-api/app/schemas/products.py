import graphene

from products.schema import Query

from products.serializer import ProductsType

schema = graphene.Schema(query=Query, types=[ProductsType])