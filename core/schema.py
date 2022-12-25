
import graphene 
import Eemail.schema
from Eemail.schema import Mutation
from graphene_django import*
from Eemail.graphapi.resolvers import resolve_Welcome,resolve_sendmail
from Eemail.graphapi.mutation import CreateMessageMutation


 
class Query(Eemail.schema.Query,graphene.ObjectType):
    pass


class Mutation(Mutation,graphene.ObjectType):
     pass






schema=graphene.Schema(query=Query,mutation=Mutation)