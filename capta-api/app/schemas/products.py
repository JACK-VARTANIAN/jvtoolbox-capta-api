import graphene

import products.schema

from products.serializer import ProductsType


class Query(products.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)