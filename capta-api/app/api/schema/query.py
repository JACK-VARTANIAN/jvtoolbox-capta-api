mport graphene
from graphene import relay

from models.products import Products as ProductsModel
from types.books import Products


class Query(graphene.ObjectType):
    node = relay.Node.Field()

    products_by_cpros = graphene.List(Products, cpros=graphene.String())

    @staticmethod
    def resolve_books_by_name(parent, info, **args):
        q = args.get('cpros')

        products_query = Products.get_query(info)

        return products_query.filter(ProductsModel.name.contains(q)).all()
