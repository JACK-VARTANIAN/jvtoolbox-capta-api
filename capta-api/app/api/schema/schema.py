import graphene

from query import Query
from mutation import Mutation

from types.books import Products

schema = graphene.Schema(query=Query, mutation=Mutation, types=[Products])