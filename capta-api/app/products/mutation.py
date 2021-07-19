# import graphene

# from app.config.database.db_session import db_session
# from .models import Products as ProductsModel
# from .serializer import Products


# class SelectProducts(graphene.Mutation):
#     product = graphene.Field(lambda: Products)
#     ok = graphene.Boolean()

#     # class Arguments:
#     #     input = CreateBookInput(required=True)

#     @staticmethod
#     def mutate(self, info, input):
#         data = input_to_dictionary(input)
#         product = BooksModel(**data)
#         db_session.find(product)
#         db_session.commit()
#         ok = True
#         return SelectProducts(product=product, ok=ok)


# class Mutation(graphene.ObjectType):
#     selectProducts = SelectProducts.Field()